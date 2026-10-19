#!/usr/bin/env python3
"""Compile reviewed explanations into Markdown and a local searchable HTML guide.

Only explicit publication fields leave the private research inventory. This script
does not execute Rocket, contact a printer, read account stores or publish files.
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".deps"))
TITLE = "Tinmans Rocket slicer tuning guide"

# Exact symbols in installed Rocket 1.4.0.705's
# dist/assets/UnitCatalog-DAd96JGA.js. These are display units, not limits.
UNIT_SYMBOLS = {
    "UnitId.Millimetre": "mm",
    "UnitId.MillimetrePerSecond": "mm/s",
    "UnitId.MillimetrePerSecondSquared": "mm/s²",
    "UnitId.Degree": "°",
    "UnitId.Percent": "%",
    "UnitId.Loop": "loops",
    "UnitId.Layer": "layers",
    "UnitId.DegreeCelsius": "°C",
    "UnitId.Second": "s",
    "UnitId.DegreeCelsiusPerSecond": "°C/s",
    "UnitId.Gram": "g",
    "UnitId.Kilometre": "km",
    "UnitId.Tex": "tex = g/km",
    "UnitId.GramPerCubicCentimetre": "g/cm³",
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def scalar(value):
    if isinstance(value, dict):
        return value.get("value")
    return value


def literal(value):
    value = scalar(value)
    return value if isinstance(value, (str, int, float, bool)) else None


def variant_context(variant):
    return " / ".join(str(p) for p in variant.get("menu_path", [])[1:] if p) or "Unresolved schema context"


def option_items(field, labels=None):
    labels = labels or {}
    found = {}
    for variant in field["variants"]:
        block = variant.get("options", {})
        for item in block.get("items", []) if isinstance(block, dict) else []:
            raw_label = item.get("label") or item.get("label_key")
            if raw_label is None:
                raw_label = literal(item.get("value"))
            raw_label = str(raw_label) if raw_label is not None else "Unresolved option"
            label = labels.get(raw_label, raw_label)
            value = literal(item.get("value"))
            choice = found.setdefault((label, str(value)), {"label": label, "source_label_key": raw_label, "value": value, "contexts": []})
            context = variant_context(variant)
            if context not in choice["contexts"]:
                choice["contexts"].append(context)
    for choice in found.values():
        choice["contexts"].sort()
    return list(found.values())


def compact_values(field, property_name):
    values = set()
    for variant in field["variants"]:
        raw = variant.get(property_name)
        value = literal(raw)
        if property_name == "unit" and isinstance(raw, dict) and raw.get("source_expression"):
            expression = raw["source_expression"]
            value = UNIT_SYMBOLS.get(expression, "Unresolved display unit: " + expression)
        if value is not None:
            values.add(str(value))
    return sorted(values)


def publication_fields(inventory, explanations, labels=None):
    output = []
    missing = []
    missing_options = []
    required = ("meaning", "when_to_change", "effect", "caution", "status")
    for field in inventory["fields"]:
        uid = field["uid"]
        note = explanations.get(uid, {})
        absent = [key for key in required if not str(note.get(key, "")).strip()]
        if absent:
            missing.append({"uid": uid, "missing": absent})
        choices = option_items(field, labels)
        interpretations = {}
        for explanation in note.get("options", []):
            for key in ("label", "source_label_key"):
                if explanation.get(key):
                    interpretations[str(explanation[key])] = str(explanation.get("meaning", ""))
        for choice in choices:
            choice["meaning"] = interpretations.get(choice["label"], interpretations.get(choice["source_label_key"], ""))
            if not choice["meaning"]:
                missing_options.append({"uid": uid, "label": choice["label"]})
                choice["meaning"] = "The label is known, but this option's exact behavior has not been established. Retain the OEM value until its preview/output effect is confirmed."
        sections = sorted({variant_context(v) for v in field["variants"]})
        constraints = []
        for variant in field["variants"]:
            limits = {key: literal(value) for key, value in variant.get("constraints", {}).items() if literal(value) is not None}
            if limits and limits not in constraints:
                constraints.append(limits)
        defaults = []
        for variant in field["variants"]:
            if variant.get("default_status", "").startswith("direct schema") and literal(variant.get("default")) is not None:
                value = literal(variant["default"])
                if value not in defaults:
                    defaults.append(value)
        output.append({
            "uid": uid, "namespace": uid.partition(":")[0],
            "label": field.get("label") or "Unresolved inline selector",
            "field": field["source_field"], "contexts": sections,
            "types": compact_values(field, "type"), "units": compact_values(field, "unit"),
            "schema_constraints": constraints, "schema_defaults": defaults,
            "options": choices, "variant_count": len(field["variants"]),
            "meaning": note.get("meaning", "Explanation is still being reviewed; do not infer behavior from the internal key."),
            "when_to_change": note.get("when_to_change", "Keep the OEM value until the control is understood."),
            "effect": note.get("effect", "Not established."),
            "interactions": note.get("interactions", []),
            "caution": note.get("caution", "Do not treat a schema entry as a validated machine operation."),
            "status": note.get("status", "Unreviewed"),
            "source": {"basis": "Installed renderer definition, not runtime visibility or execution proof", "build": inventory["application"]["build"]}
        })
    return output, missing, missing_options


def field_markdown(fields, coverage):
    lines = ["# Rocket field reference", "", "Find the label on your screen, then match its scope and feature context. Repeated labels such as Printing speed or Flow multiplier affect different regions; the internal ID distinguishes them, not a universal shared value.", "", f"This working edition indexes {len(fields)} template/editor schema fields in Rocket {coverage['build']}. It does not yet claim every runtime dialog/action is covered. {coverage['unmapped_renderer_controls']} renderer controls and {coverage['keyed_dialog_fields']} additional dialog declarations require exact label/path checks. Missing explanations: {len(coverage['missing_explanations'])}; unresolved option explanations: {len(coverage['missing_option_explanations'])}.", "", "Schema bounds are input constraints, not safe hardware limits. A missing bound/default means unknown, not unrestricted. Mode-dependent variants are listed together; check your actual screen and resolved output. Functional explanations describe the control's purpose, not proof of a safe or successful print.", ""]
    current = None
    for field in fields:
        if field["namespace"] != current:
            current = field["namespace"]
            lines += ["## " + current.replace("-", " ").title(), ""]
        lines += ["### " + field["label"] + " - " + field["field"], "", "**Scope:** " + "; ".join(field["contexts"]) + ".", "", "**What does it mean?** " + field["meaning"], "", "**When would I change it?** " + field["when_to_change"], "", "**What changes if I adjust it?** " + field["effect"], ""]
        if field["interactions"]:
            lines += ["**Check together with:** " + "; ".join(field["interactions"]) + ".", ""]
        if field["units"]:
            lines += ["**Displayed units:** " + ", ".join(field["units"]) + ".", ""]
        if field["options"]:
            lines += ["**Selectable choices:**", ""]
            lines += ["- **" + x["label"] + ":** " + x["meaning"] + (" Schema contexts: " + "; ".join(x["contexts"]) + "." if x.get("contexts") else "") for x in field["options"]]
            lines += [""]
        if field["schema_constraints"]:
            lines += ["**Declared editor constraints:** " + "; ".join(json.dumps(x, ensure_ascii=False) for x in field["schema_constraints"]) + ". These are not operating recommendations.", ""]
        if field["schema_defaults"]:
            lines += ["**Literal schema default:** " + json.dumps(field["schema_defaults"], ensure_ascii=False) + ". A selected template may differ.", ""]
        lines += ["**Caution:** " + field["caution"], "", "**Evidence status:** " + field["status"] + ". Control ID: `" + field["uid"] + "`.", ""]
    return "\n".join(line.rstrip() for line in lines)


STYLE = """body{margin:0;background:#f4f6f6;color:#17242a;font:17px/1.6 system-ui,sans-serif}header{background:#15383b;color:white;padding:2rem max(5vw,1rem)}header p{max-width:70ch}main{max-width:1000px;margin:auto;padding:1.5rem}h1,h2,h3{line-height:1.2}h2{margin-top:2.2rem}a{color:#076365}header a{color:#c7ece4}nav{display:flex;gap:1rem;flex-wrap:wrap}article{background:white;border:1px solid #d3dddd;border-radius:10px;padding:1.2rem 1.6rem;margin:1rem 0}article h2{margin:0 0 .7rem;font-size:1.3rem}.meta{font-size:.85rem;color:#4a6066}.badge{display:inline-block;background:#e8f2ef;border-radius:5px;padding:.1rem .5rem;margin:.2rem}input,select{font:inherit;padding:.7rem;border:1px solid #79949a;border-radius:6px;max-width:100%}input{width:65%}.tools{position:sticky;top:0;background:#f4f6f6;padding:1rem 0;z-index:1}table{border-collapse:collapse;width:100%;font-size:.93rem}td,th{border:1px solid #ccd9d9;padding:.5rem;text-align:left;vertical-align:top}pre{overflow:auto;background:#e6eeee;padding:1rem}code{overflow-wrap:anywhere}li{margin:.3rem 0}.warn{border-left:4px solid #a66a13;padding:.7rem 1rem;background:#fff5df}footer{margin:3rem 0;color:#49616a;font-size:.9rem}[hidden]{display:none!important}@media(max-width:600px){main{padding:.7rem}article{padding:1rem}input{width:93%}}"""


def escape(value):
    return html.escape(str(value), quote=True)


def html_shell(title, body, prefix=""):
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + escape(title) + '</title><style>' + STYLE + '</style><header><h1>' + escape(TITLE) + '</h1><p>Rocket 1.4.0.705 working edition · plain-language controls and controlled material tests</p><nav><a href="' + prefix + 'index.html">Search settings</a><a href="' + prefix + 'guide/01-baseline-and-identity.html">Start here</a><a href="' + prefix + 'tests/README.html">Test catalog</a><a href="' + prefix + 'SOURCES.html">Sources</a></nav></header><main>' + body + '<footer>Independent CC BY 4.0 guide; flow models have separate AGPL notices. No printer connection, telemetry, account or Rocket runtime code is included.</footer></main></html>'


def build_html(fields, coverage):
    import markdown
    out = ROOT / "output" / "html"
    out.mkdir(parents=True, exist_ok=True)
    flow_pack = ROOT / "tests" / "tinman-flow"
    docs = [ROOT / "README.md", ROOT / "SOURCES.md", ROOT / "CREDITS.md", *sorted((ROOT / "guide").glob("*.md")), ROOT / "tests" / "README.md", flow_pack / "README.md", flow_pack / "NOTICE.md", ROOT / "templates" / "experiment-log.md"]
    for doc in docs:
        rel = doc.relative_to(ROOT).with_suffix(".html")
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        source = doc.read_text(encoding="utf-8")
        source = re.sub(r"\*\*\[([A-Z0-9-]+)\]\*\*", lambda m: '<a id="ref-' + m[1].lower() + '"></a>**[' + m[1] + ']**', source)
        body = markdown.markdown(source, extensions=["tables", "fenced_code", "toc"])
        body = re.sub(r'href="([^"#]+)\.md([^"]*)"', r'href="\1.html\2"', body)
        prefix = "../" * (len(rel.parts) - 1)
        dest.write_text(html_shell(doc.stem, body, prefix), encoding="utf-8")
    # Keep offline downloads explicit: never mirror research or native job exports.
    assets = [ROOT / "LICENSE", ROOT / "source-index.json", ROOT / "scripts" / "extract_tinman_flow_models.py", flow_pack / "manifest.json", flow_pack / "LICENSE-AGPL-3.0.txt", *sorted((flow_pack / "models").glob("*.stl")), *sorted((flow_pack / "source").glob("*.3mf"))]
    checks = flow_pack / "ROCKET_CHECKS.json"
    if checks.exists():
        assets.append(checks)
    for asset in assets:
        if asset.is_symlink() or not asset.is_file():
            raise ValueError("Publication asset must be a regular file: " + str(asset.relative_to(ROOT)))
        dest = out / asset.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(asset.read_bytes())
    cards = []
    for field in fields:
        choices = "".join("<li><b>" + escape(x["label"]) + ":</b> " + escape(x["meaning"]) + ('<br><span class="meta">Schema contexts: ' + escape("; ".join(x["contexts"])) + '</span>' if x.get("contexts") else '') + "</li>" for x in field["options"])
        scope = "; ".join(field["contexts"])
        data = json.dumps(field, ensure_ascii=False)
        constraints = ('<p><b>Declared editor constraints:</b> ' + escape("; ".join(json.dumps(x, ensure_ascii=False) for x in field["schema_constraints"])) + '. These are input constraints, not operating recommendations or hardware limits.</p>') if field["schema_constraints"] else ''
        defaults = ('<p><b>Literal schema default:</b> ' + escape(json.dumps(field["schema_defaults"], ensure_ascii=False)) + '. A selected template may differ.</p>') if field["schema_defaults"] else ''
        cards.append('<article data-scope="' + escape(field["namespace"]) + '" data-search="' + escape(data.casefold()) + '"><h2>' + escape(field["label"]) + '</h2><p class="meta">' + escape(scope) + '<br><code>' + escape(field["uid"]) + '</code></p><p><b>What does it mean?</b> ' + escape(field["meaning"]) + '</p><p><b>When would I change it?</b> ' + escape(field["when_to_change"]) + '</p><p><b>What happens if I adjust it?</b> ' + escape(field["effect"]) + '</p>' + ('<p><b>Units:</b> ' + escape(", ".join(field["units"])) + '</p>' if field["units"] else '') + ('<ul>' + choices + '</ul>' if choices else '') + constraints + defaults + '<p><b>Check with:</b> ' + escape("; ".join(field["interactions"])) + '</p><p class="warn">' + escape(field["caution"]) + '</p><p class="meta">' + escape(field["status"]) + ' · Defined in installed schema; actual visibility and output remain conditional.</p></article>')
    namespaces = sorted({x["namespace"] for x in fields})
    controls = '<div class="tools"><label for="q">Find a field or question</label><br><input id="q" placeholder="Try flow, bridge, support gap or temperature" autocomplete="off"> <select id="scope"><option value="">All scopes</option>' + ''.join('<option>' + escape(n) + '</option>' for n in namespaces) + '</select><p id="count" class="meta"></p></div>'
    note = '<p class="warn">Working reference: ' + str(len(fields)) + ' schema fields. ' + str(coverage["unmapped_renderer_controls"]) + ' additional renderer controls still need exact labels/paths; this is not exhaustive runtime UI acceptance. Input bounds are not safe hardware ratings.</p>'
    script = '''<script>const q=document.querySelector('#q'),s=document.querySelector('#scope'),cards=[...document.querySelectorAll('article')];function filter(){let n=0;const words=q.value.toLocaleLowerCase().trim().split(/\\s+/).filter(Boolean);for(const c of cards){const ok=(!s.value||c.dataset.scope===s.value)&&words.every(w=>c.dataset.search.includes(w));c.hidden=!ok;n+=ok;}document.querySelector('#count').textContent=n+' of '+cards.length+' fields shown';}q.addEventListener('input',filter);s.addEventListener('change',filter);filter();</script>'''
    (out / "index.html").write_text(html_shell(TITLE, '<h2>What does this Rocket setting do?</h2><p>Search the label, an internal ID or a symptom, then match the feature and material scope. Read the <a href="README.html">introduction</a> before using a test.</p>' + note + controls + ''.join(cards) + script), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Reject missing schema explanations or option explanations")
    parser.add_argument("--skip-html", action="store_true")
    parser.add_argument("--published", action="store_true", help="Rebuild from the public catalog; does not need private research inputs")
    args = parser.parse_args()
    if args.published:
        fields = read_json(ROOT / "fields" / "catalog.json")["fields"]
        coverage = read_json(ROOT / "fields" / "coverage.json")
        if args.strict and (coverage["missing_explanations"] or coverage["missing_option_explanations"]):
            raise SystemExit("Published catalog is incomplete")
        (ROOT / "guide" / "06-field-reference.md").write_text(field_markdown(fields, coverage), encoding="utf-8")
        if not args.skip_html:
            build_html(fields, coverage)
        print(json.dumps({"public_rebuild": True, "fields": len(fields)}))
        return
    inventory = read_json(ROOT / "research" / "rocket-field-inventory.json")
    explanations = {}
    for path in sorted((ROOT / "fields").glob("explanations-*.json")):
        entries = read_json(path)["fields"]
        duplicate = explanations.keys() & entries.keys()
        if duplicate:
            raise ValueError("Duplicate explanation ownership: " + str(sorted(duplicate)))
        explanations.update(entries)
    labels = read_json(ROOT / "research" / "rocket-option-labels.json")["labels"]
    fields, missing, missing_options = publication_fields(inventory, explanations, labels)
    unknown = sorted(set(explanations) - {f["uid"] for f in fields})
    if unknown:
        raise ValueError("Unknown explanation UIDs: " + str(unknown))
    coverage = {"build": inventory["application"]["build"], "schema_fields": len(fields), "schema_occurrences": inventory["summary"]["schema_field_occurrences"], "explained_schema_fields": len(fields) - len(missing), "missing_explanations": missing, "missing_option_explanations": missing_options, "unmapped_renderer_controls": len(inventory["renderer_controls_requiring_label_path_review"]), "keyed_dialog_fields": len(inventory["keyed_dialog_fields"]), "complete_runtime_ui_coverage": False, "runtime_ui_observed": False, "physical_test_validation": False}
    if args.strict and (missing or missing_options):
        raise SystemExit(f"Incomplete: {len(missing)} fields, {len(missing_options)} choices")
    (ROOT / "fields" / "coverage.json").write_text(json.dumps(coverage, indent=2) + "\n", encoding="utf-8")
    (ROOT / "fields" / "catalog.json").write_text(json.dumps({"edition": "0.1 working", "application": {k: inventory["application"][k] for k in ("version", "build", "asar_sha256")}, "fields": fields}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "guide" / "06-field-reference.md").write_text(field_markdown(fields, coverage), encoding="utf-8")
    if not args.skip_html:
        build_html(fields, coverage)
    print(json.dumps({k: coverage[k] for k in ("build", "schema_fields", "explained_schema_fields", "unmapped_renderer_controls", "complete_runtime_ui_coverage")}))


if __name__ == "__main__":
    main()
