#!/usr/bin/env python3
"""Extract the original Tinman/Orca flow meshes; never import slicer settings.

SPDX-License-Identifier: AGPL-3.0

The input 3MFs are pinned below. Output STLs keep every source triangle and are
translated to the origin only. They contain no account/project metadata, G-code,
material presets, or automatic modifier schedule. The source assets and their
AGPL-3.0 license remain separate from the guide's CC BY 4.0 text.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import shutil
import struct
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "tests" / "tinman-flow"
NS = {"m": "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"}
PIN = "c6065d54fc37abec1992e7366d600251785f6517"
SOURCES = {
    "flowrate-test-pass1.3mf": "6e86280ef6dd912dc4bf8c5eb00d0b21d218f74774602eb10c73c36e5cc2aa5f",
    "flowrate-test-pass2.3mf": "b2ac0302c36a810f9a178e1856c2989f05d283b8b98ee8f8b3b869e2829614af",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def normal(points):
    a, b, c = points
    u, v = [b[i] - a[i] for i in range(3)], [c[i] - a[i] for i in range(3)]
    n = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
    length = math.sqrt(sum(x*x for x in n))
    return tuple(x / length for x in n) if length else (0.0, 0.0, 0.0)


def extract(source_dir):
    manifest = {"schema": "tinman-rocket-flow-geometry.v1", "source_revision": PIN,
                "license": "AGPL-3.0 (upstream repository basis; see NOTICE.md)",
                "conversion": "Original triangles, origin translation only; no resizing or decimation",
                "contains_gcode": False, "contains_parameter_schedules": False,
                "physical_validation": False, "models": []}
    for pass_no, (filename, digest) in enumerate(SOURCES.items(), 1):
        source = source_dir / filename
        data = source.read_bytes()
        if sha(data) != digest:
            raise ValueError("Input differs from the pinned original: " + filename)
        with zipfile.ZipFile(source) as archive:
            model = ET.fromstring(archive.read("3D/3dmodel.model"))
        if model.get("unit") != "millimeter":
            raise ValueError("Unexpected source units")
        objects = {o.get("id"): o for o in model.findall("m:resources/m:object", NS)}
        items = model.findall("m:build/m:item", NS)
        if len(items) != (9 if pass_no == 1 else 10):
            raise ValueError("Unexpected source object count")
        for item in items:
            if item.get("transform"):
                raise ValueError("Unexpected source build transform")
            obj = objects[item.get("objectid")]
            name = obj.get("name", "")
            if not name.startswith("flowrate_"):
                raise ValueError("Unexpected source object label")
            label = int(name.removeprefix("flowrate_").replace("m", "-"))
            vertices = [tuple(float(v.get(k)) for k in ("x", "y", "z"))
                        for v in obj.findall("m:mesh/m:vertices/m:vertex", NS)]
            faces = [tuple(int(t.get(k)) for k in ("v1", "v2", "v3"))
                     for t in obj.findall("m:mesh/m:triangles/m:triangle", NS)]
            if not vertices or not faces or not all(math.isfinite(x) for v in vertices for x in v):
                raise ValueError("Invalid source geometry")
            origin = tuple(min(v[i] for v in vertices) for i in range(3))
            points = [tuple(v[i]-origin[i] for i in range(3)) for v in vertices]
            bounds = [max(v[i] for v in points) for i in range(3)]
            if any(abs(a-b) > 1e-6 for a,b in zip(bounds,(40,30,2))):
                raise ValueError("Unexpected source dimensions")
            outname = f"pass{pass_no}-flow-{label:+03d}pct.stl"
            output = bytearray(b"Tinman/Orca flow geometry; AGPL-3.0; see NOTICE.md".ljust(80,b" "))
            output.extend(struct.pack("<I", len(faces)))
            edge_counts = Counter()
            for face in faces:
                tri = [points[i] for i in face]
                output.extend(struct.pack("<12fH", *normal(tri), *(x for p in tri for x in p), 0))
                for a,b in zip(tri,tri[1:]+tri[:1]):
                    edge_counts[tuple(sorted((a,b)))] += 1
            target = DEST / "models" / outname
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(output)
            manifest["models"].append({"file": "models/"+outname,
                "source_file": "source/"+filename, "source_sha256": digest,
                "source_object_id": obj.get("id"), "source_object_name": name,
                "source_url": f"https://github.com/OrcaSlicer/OrcaSlicer/blob/{PIN}/resources/calib/filament_flow/{filename}",
                "label_percent": label, "pass": pass_no, "dimensions_mm": bounds,
                "triangles": len(faces), "welded_non_two_face_edges": sum(n != 2 for n in edge_counts.values()),
                "sha256": sha(output), "status": "prepared; native Rocket checks tracked in ROCKET_CHECKS.json; not physically validated"})
        originals = DEST / "source"
        originals.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, originals / filename)
    (DEST / "manifest.json").write_text(json.dumps(manifest, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"models":len(manifest["models"]),"schedules":False,"physical_validation":False}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=DEST/"source")
    args = parser.parse_args()
    extract(args.source_dir)


if __name__ == "__main__":
    main()
