#!/usr/bin/env python3
"""Independent, stdlib-only publication checks; not Rocket or print acceptance.

Run ``python3 scripts/build_reference.py --strict`` first, then this file. The
tests neither import the model/reference generators nor execute an application.
Private research, when present, provides an additional option-coverage crosscheck;
the public catalog and evidence-status tests also run without it. Original flow
geometry is checked separately by ``scripts/test_tinman_flow_pack.py``.
"""
from __future__ import annotations

from html.parser import HTMLParser
import ipaddress
import json
import math
from pathlib import Path, PurePosixPath
import re
import unittest
from urllib.parse import urlsplit
import zipfile


ROOT = Path(__file__).resolve().parents[1]
FLOW_PACK = ROOT / "tests/tinman-flow"
EXPECTED_BUILD = "1.4.0.705"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def privacy_findings(text):
    """Bounded common-leak checks, not a claim to recognize every possible secret."""
    findings = []
    patterns = {
        "local absolute path": r"file://|/(?:Users|home|private|Volumes|Applications|tmp|var)/|[A-Za-z]:\\(?:Users|Windows|Program Files)\\",
        "private key": r"-----BEGIN (?:RSA |EC |OPENSSH |ENCRYPTED )?PRIVATE KEY-----",
        "token-shaped secret": r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16}|sk-[A-Za-z0-9_-]{24,})\b",
        "credential assignment": r'''(?i)\b(?:api[_ -]?key|access[_ -]?token|password|private[_ -]?key)["']?\s*[:=]\s*["'][A-Za-z0-9_./+=-]{8,}["']''',
    }
    for label, pattern in patterns.items():
        if re.search(pattern, text):
            findings.append(label)
    for raw in re.findall(r"\b(?:https?|wss?|ftp)://[^\s\"'<>]+", text):
        try:
            url = urlsplit(raw)
            host = (url.hostname or "").rstrip(".").casefold()
            if url.username is not None or url.password is not None:
                findings.append("credentials in URL")
            if host == "localhost" or host.endswith((".local", ".lan", ".internal", ".home", ".home.arpa")):
                findings.append("private URL hostname")
            try:
                if not ipaddress.ip_address(host).is_global:
                    findings.append("non-public URL address")
            except ValueError:
                pass
        except ValueError:
            findings.append("malformed URL")
    for value in re.findall(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])", text):
        try:
            if not ipaddress.ip_address(value).is_global:
                findings.append("non-public IPv4 address")
        except ValueError:
            pass  # Version strings are not necessarily valid IPv4 addresses.
    return sorted(set(findings))


class FieldCards(HTMLParser):
    def __init__(self):
        super().__init__()
        self.articles = 0
        self.uids = []
        self.in_article = False
        self.in_code = False

    def handle_starttag(self, tag, attrs):
        if tag == "article":
            self.articles += 1
            self.in_article = True
        if tag == "code" and self.in_article:
            self.in_code = True

    def handle_endtag(self, tag):
        if tag == "article":
            self.in_article = False
        if tag == "code":
            self.in_code = False

    def handle_data(self, data):
        if self.in_code:
            self.uids.append(data)


class CatalogPublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_json(ROOT / "fields/catalog.json")
        cls.fields = cls.catalog["fields"]
        cls.uids = [field["uid"] for field in cls.fields]

    def test_470_unique_scoped_fields_and_pinned_application(self):
        self.assertEqual(len(self.fields), 470)
        self.assertEqual(len(set(self.uids)), 470)
        self.assertEqual(set(self.catalog["application"]), {"version", "build", "asar_sha256"})
        self.assertEqual(self.catalog["application"]["build"], EXPECTED_BUILD)
        self.assertRegex(self.catalog["application"]["asar_sha256"], r"^[a-f0-9]{64}$")
        for field in self.fields:
            with self.subTest(uid=field["uid"]):
                self.assertRegex(field["uid"], r"^[a-z][a-z-]*:[A-Za-z][A-Za-z0-9_]*$")
                self.assertEqual(field["uid"], field["namespace"] + ":" + field["field"])
                self.assertEqual(set(field["source"]), {"basis", "build"})
                self.assertEqual(field["source"]["build"], EXPECTED_BUILD)

    def test_all_required_prose_and_every_published_choice_are_explained(self):
        choice_count = 0
        for field in self.fields:
            with self.subTest(uid=field["uid"]):
                for key in ("label", "meaning", "when_to_change", "effect", "caution", "status"):
                    self.assertIsInstance(field[key], str)
                    self.assertTrue(field[key].strip(), key)
                for key in ("contexts", "interactions", "types", "units", "options"):
                    self.assertIsInstance(field[key], list)
                self.assertTrue(field["contexts"])
                self.assertTrue(field["interactions"])
                for text in field["contexts"] + field["interactions"]:
                    self.assertIsInstance(text, str)
                    self.assertTrue(text.strip())
                seen = set()
                for option in field["options"]:
                    for key in ("label", "meaning", "source_label_key"):
                        self.assertIsInstance(option[key], str)
                        self.assertTrue(option[key].strip())
                    key = (option["label"], json.dumps(option["value"], sort_keys=True))
                    self.assertNotIn(key, seen)
                    seen.add(key)
                    self.assertTrue(option["contexts"])
                    choice_count += 1
        self.assertEqual(choice_count, 154, "Pinned build's distinct field/label/value choices changed")

    def test_choices_match_installed_inventory_when_private_research_is_present(self):
        path = ROOT / "research/rocket-field-inventory.json"
        if not path.exists():
            self.skipTest("Optional private research is excluded from the public publication")
        inventory = load_json(path)
        labels = load_json(ROOT / "research/rocket-option-labels.json")["labels"]
        self.assertEqual({item["uid"] for item in inventory["fields"]}, set(self.uids))
        published = {field["uid"]: field for field in self.fields}
        for source in inventory["fields"]:
            expected = set()
            for variant in source["variants"]:
                options = variant.get("options", {})
                for option in options.get("items", []) if isinstance(options, dict) else []:
                    value = option.get("value")
                    if isinstance(value, dict):
                        value = value.get("value")
                    if not isinstance(value, (str, int, float, bool)):
                        value = None
                    label = option.get("label") or option.get("label_key")
                    label = str(label if label is not None else value if value is not None else "Unresolved option")
                    expected.add((labels.get(label, label), json.dumps(value, sort_keys=True)))
            actual = {(option["label"], json.dumps(option["value"], sort_keys=True)) for option in published[source["uid"]]["options"]}
            self.assertEqual(actual, expected, source["uid"])

    def test_coverage_does_not_claim_runtime_or_physical_acceptance(self):
        coverage = load_json(ROOT / "fields/coverage.json")
        self.assertEqual(coverage["build"], EXPECTED_BUILD)
        self.assertEqual(coverage["schema_fields"], 470)
        self.assertEqual(coverage["explained_schema_fields"], 470)
        self.assertEqual(coverage["missing_explanations"], [])
        self.assertEqual(coverage["missing_option_explanations"], [])
        for flag in ("complete_runtime_ui_coverage", "runtime_ui_observed", "physical_test_validation"):
            self.assertIs(coverage[flag], False, flag)
        self.assertGreater(coverage["unmapped_renderer_controls"], 0)
        self.assertGreater(coverage["keyed_dialog_fields"], 0)

    def test_generated_markdown_and_html_retain_each_uid_once(self):
        markdown = (ROOT / "guide/06-field-reference.md").read_text(encoding="utf-8")
        for uid in self.uids:
            self.assertEqual(markdown.count("Control ID: `" + uid + "`."), 1, uid)
        parser = FieldCards()
        parser.feed((ROOT / "output/html/index.html").read_text(encoding="utf-8"))
        self.assertEqual(parser.articles, 470)
        self.assertEqual(len(parser.uids), 470)
        self.assertEqual(set(parser.uids), set(self.uids))


class FlowPackPublicationTests(unittest.TestCase):
    def test_native_sample_evidence_does_not_promote_the_whole_pack_or_printer(self):
        manifest = load_json(FLOW_PACK / "manifest.json")
        checks = load_json(FLOW_PACK / "ROCKET_CHECKS.json")
        self.assertEqual(manifest["schema"], "tinman-rocket-flow-geometry.v1")
        for flag in ("contains_gcode", "contains_parameter_schedules", "physical_validation"):
            self.assertIs(manifest[flag], False, flag)
        self.assertEqual(checks["schema"], "rocket-flow-pack-checks.v1")
        self.assertEqual(checks["rocket_version"], EXPECTED_BUILD)
        self.assertIs(checks["all_19_geometry_source_checks"], True)
        self.assertIs(checks["native_sample_imported"], True)
        self.assertIs(checks["native_sample_sliced"], True)
        for flag in ("native_all_19_individual_slice_checks", "native_project_export_or_sanitized_reopen",
                     "printer_operations", "physical_print_validation", "PCTG_or_CFC_profile_validation",
                     "public_gcode_included"):
            self.assertIs(checks[flag], False, flag)
        models = {item["file"]: item for item in manifest["models"]}
        self.assertIn(checks["native_sample"], models)
        self.assertEqual(models[checks["native_sample"]]["label_percent"], 0)
        self.assertEqual(checks["sample_mode"], "Speedy")
        self.assertTrue(checks["limitations"])
        for limitation in checks["limitations"]:
            self.assertIsInstance(limitation, str)
            self.assertTrue(limitation.strip())
        for model in models.values():
            self.assertIn("not physically validated", model["status"])

    def test_native_comparison_summary_is_internally_consistent_not_a_print_claim(self):
        checks = load_json(FLOW_PACK / "ROCKET_CHECKS.json")
        for key in ("baseline_gcode_sha256", "changed_gcode_sha256"):
            self.assertRegex(checks[key], r"^[a-f0-9]{64}$")
        self.assertNotEqual(checks["baseline_gcode_sha256"], checks["changed_gcode_sha256"])
        for key in ("baseline_positive_XY_E_mm", "changed_positive_XY_E_mm",
                    "changed_to_baseline_XY_deposition_ratio", "layer_height_mm"):
            self.assertIn(type(checks[key]), (int, float))
            self.assertTrue(math.isfinite(checks[key]) and checks[key] > 0, key)
        multipliers = checks["flow_multiplier_comparison"]
        self.assertEqual(len(multipliers), 2)
        self.assertTrue(all(type(value) in (int, float) and math.isfinite(value) and value > 0
                            for value in multipliers))
        measured = checks["changed_positive_XY_E_mm"] / checks["baseline_positive_XY_E_mm"]
        self.assertAlmostEqual(checks["changed_to_baseline_XY_deposition_ratio"], measured, places=12)
        self.assertAlmostEqual(measured, multipliers[1] / multipliers[0], places=5)
        self.assertIs(checks["same_motion_except_E"], True)
        self.assertIs(checks["E_only_recovery_unchanged"], True)
        self.assertGreater(checks["model_positive_XY_E_move_count_each"], 0)
        self.assertGreater(checks["positive_E_only_recovery_moves_each"], 0)
        self.assertEqual(checks["V_U_P_model_moves_each"], 0)
        self.assertAlmostEqual(checks["layers"] * checks["layer_height_mm"], 2.0)
        self.assertIs(checks["physical_print_validation"], False)


class PublicationPrivacyTests(unittest.TestCase):
    def test_common_leak_detectors_reject_synthetic_examples(self):
        for sample in ("http://192.168.2.5/status", "https://[::1]/", "wss://printer.local/ws", "https://user:password@example.com/", "/Users/example/secret.json", r"C:\Users\example\secret.json", "file:///tmp/state", '"api_key": "abcdefgh12345678"', "-----BEGIN PRIVATE KEY-----", "ghp_" + "a" * 36):
            with self.subTest(kind=sample.partition(":")[0]):
                self.assertTrue(privacy_findings(sample))
        self.assertEqual(privacy_findings("Rocket 1.4.0.705; https://github.com/Tinman-FP/tinmans-tuning-guide"), [])

    def test_public_text_excludes_common_private_paths_endpoints_and_credentials(self):
        paths = [ROOT / name for name in ("README.md", "SOURCES.md", "CREDITS.md", "LICENSE", "fields/catalog.json", "fields/coverage.json", "tests/README.md")]
        paths += sorted((ROOT / "guide").glob("*.md"))
        paths += sorted((ROOT / "templates").glob("*.md"))
        paths += sorted((ROOT / "output/html").rglob("*.html"))
        paths += sorted(path for path in FLOW_PACK.rglob("*") if path.suffix in (".json", ".md", ".txt"))
        self.assertGreater(len(paths), 15)
        for path in paths:
            with self.subTest(file=path.relative_to(ROOT).as_posix()):
                self.assertEqual(privacy_findings(path.read_text(encoding="utf-8")), [])

    def test_public_flow_sources_contain_no_private_or_runnable_payload(self):
        sources = sorted((FLOW_PACK / "source").glob("*.3mf"))
        self.assertEqual(len(sources), 2)
        for path in sources:
            with self.subTest(source=path.name), zipfile.ZipFile(path) as archive:
                self.assertFalse(path.is_symlink())
                names = archive.namelist()
                self.assertEqual(len(names), len(set(names)))
                for name in names:
                    member = PurePosixPath(name)
                    self.assertFalse(member.is_absolute())
                    self.assertNotIn("..", member.parts)
                    self.assertNotIn("\\", name)
                    extension = ".rels" if member.name == ".rels" else member.suffix.lower()
                    self.assertIn(extension, (".model", ".xml", ".rels", ".png"))
                    if extension in (".model", ".xml", ".rels"):
                        self.assertEqual(privacy_findings(archive.read(name).decode("utf-8")), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
