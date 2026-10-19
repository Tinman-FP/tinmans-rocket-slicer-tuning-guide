#!/usr/bin/env python3
"""Offline qualification of the published geometry pack, not printer acceptance.

Uses only the public source 3MFs, models, manifest, license, notice and extractor.
No installed slicer, private research data, third-party module or network is needed.
Run: python3 scripts/test_tinman_flow_pack.py
"""
from __future__ import annotations

from collections import Counter
import contextlib
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import struct
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "tests" / "tinman-flow"
PIN = "c6065d54fc37abec1992e7366d600251785f6517"
EXPECTED_SOURCES = {
    "flowrate-test-pass1.3mf": "6e86280ef6dd912dc4bf8c5eb00d0b21d218f74774602eb10c73c36e5cc2aa5f",
    "flowrate-test-pass2.3mf": "b2ac0302c36a810f9a178e1856c2989f05d283b8b98ee8f8b3b869e2829614af",
}
EXPECTED_LABELS = {1: {-20, -15, -10, -5, 0, 5, 10, 15, 20}, 2: set(range(-9, 1))}
NS = {"m": "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"}
STL_HEADER = b"Tinman/Orca flow geometry; AGPL-3.0; see NOTICE.md".ljust(80, b" ")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def f32(value):
    return struct.unpack("<f", struct.pack("<f", value))[0]


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def unit_normal(triangle):
    a, b, c = triangle
    n = cross(tuple(b[i] - a[i] for i in range(3)),
              tuple(c[i] - a[i] for i in range(3)))
    length = math.sqrt(sum(x * x for x in n))
    return tuple(x / length for x in n) if length else (0.0, 0.0, 0.0)


def volume(triangles):
    return math.fsum(sum(a[i] * cross(b, c)[i] for i in range(3)) / 6
                     for a, b, c in triangles)


def source_objects(path):
    with zipfile.ZipFile(path) as archive:
        if any(name.lower().endswith((".gcode", ".bgcode")) for name in archive.namelist()):
            raise ValueError("Source archive unexpectedly contains runnable G-code")
        model = ET.fromstring(archive.read("3D/3dmodel.model"))
    if model.get("unit") != "millimeter":
        raise ValueError("Source unit changed")
    objects = {o.get("id"): o for o in model.findall("m:resources/m:object", NS)}
    result = {}
    for item in model.findall("m:build/m:item", NS):
        if item.get("transform"):
            raise ValueError("Source build transform changed")
        obj = objects[item.get("objectid")]
        name = obj.get("name", "")
        if not name.startswith("flowrate_"):
            raise ValueError("Source label changed")
        label = int(name[len("flowrate_"):].replace("m", "-"))
        vertices = [tuple(float(v.get(k)) for k in ("x", "y", "z"))
                    for v in obj.findall("m:mesh/m:vertices/m:vertex", NS)]
        if not vertices or not all(math.isfinite(x) for p in vertices for x in p):
            raise ValueError("Source vertices are invalid")
        origin = tuple(min(v[i] for v in vertices) for i in range(3))
        translated = [tuple(v[i] - origin[i] for i in range(3)) for v in vertices]
        faces = [tuple(int(t.get(k)) for k in ("v1", "v2", "v3"))
                 for t in obj.findall("m:mesh/m:triangles/m:triangle", NS)]
        if not faces or not all(0 <= n < len(vertices) for face in faces for n in face):
            raise ValueError("Source triangle indices are invalid")
        if label in result:
            raise ValueError("Duplicate source label")
        result[label] = {"id": obj.get("id"), "name": name, "origin": origin,
                         "triangles": [tuple(translated[n] for n in face) for face in faces]}
    return result


def binary_stl(data):
    if len(data) < 84:
        raise ValueError("Truncated binary STL")
    count = struct.unpack_from("<I", data, 80)[0]
    if len(data) != 84 + 50 * count:
        raise ValueError("Truncated or trailing-payload STL")
    records = []
    for record in struct.iter_unpack("<12fH", data[84:]):
        records.append((record[:3], (record[3:6], record[6:9], record[9:12]), record[12]))
    return records


class TinmanFlowPackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((PACK / "manifest.json").read_text(encoding="utf-8"))
        cls.entries = cls.manifest["models"]
        cls.sources = {}
        for pass_no, (filename, expected) in enumerate(EXPECTED_SOURCES.items(), 1):
            path = PACK / "source" / filename
            if digest(path.read_bytes()) != expected:
                raise AssertionError("Pinned public source changed: " + filename)
            cls.sources[pass_no] = source_objects(path)

    def test_pins_counts_labels_and_no_acceptance_claim(self):
        m = self.manifest
        self.assertEqual(m["source_revision"], PIN)
        self.assertEqual(m["schema"], "tinman-rocket-flow-geometry.v1")
        self.assertIs(m["contains_gcode"], False)
        self.assertIs(m["contains_parameter_schedules"], False)
        self.assertIs(m["physical_validation"], False)
        self.assertEqual(len(self.entries), 19)
        self.assertEqual({p.name for p in (PACK / "source").iterdir()}, set(EXPECTED_SOURCES))
        self.assertEqual({e["file"] for e in self.entries},
                         {"models/" + p.name for p in (PACK / "models").iterdir()})
        self.assertEqual(len({e["file"] for e in self.entries}), 19)
        for pass_no, labels in EXPECTED_LABELS.items():
            with self.subTest(pass_no=pass_no):
                self.assertEqual(set(self.sources[pass_no]), labels)
                actual = [e["label_percent"] for e in self.entries if e["pass"] == pass_no]
                self.assertEqual(set(actual), labels)
                self.assertEqual(len(actual), len(labels))
        for entry in self.entries:
            with self.subTest(file=entry["file"]):
                source_name = f"flowrate-test-pass{entry['pass']}.3mf"
                self.assertEqual(entry["source_file"], "source/" + source_name)
                self.assertEqual(entry["source_sha256"], EXPECTED_SOURCES[source_name])
                self.assertEqual(entry["source_url"],
                    f"https://github.com/OrcaSlicer/OrcaSlicer/blob/{PIN}/resources/calib/filament_flow/{source_name}")
                self.assertEqual(entry["file"],
                    f"models/pass{entry['pass']}-flow-{entry['label_percent']:+03d}pct.stl")
                self.assertIn("not physically validated", entry["status"])

    def test_every_original_triangle_is_retained_with_only_translation_and_float32(self):
        for entry in self.entries:
            with self.subTest(file=entry["file"]):
                source = self.sources[entry["pass"]][entry["label_percent"]]
                self.assertEqual(entry["source_object_id"], source["id"])
                self.assertEqual(entry["source_object_name"], source["name"])
                records = binary_stl((PACK / entry["file"]).read_bytes())
                self.assertEqual(len(records), len(source["triangles"]))
                self.assertEqual(entry["triangles"], len(records))
                for (_, actual, _), original in zip(records, source["triangles"]):
                    expected = tuple(tuple(f32(x) for x in point) for point in original)
                    self.assertEqual(actual, expected)

    def test_binary_stls_are_exact_hashed_metadata_free_payloads(self):
        for entry in self.entries:
            with self.subTest(file=entry["file"]):
                data = (PACK / entry["file"]).read_bytes()
                self.assertEqual(data[:80], STL_HEADER)
                self.assertEqual(digest(data), entry["sha256"])
                records = binary_stl(data)
                self.assertTrue(records)
                self.assertTrue(all(attribute == 0 for _, _, attribute in records))
                self.assertTrue(all(math.isfinite(value)
                                    for n, triangle, _ in records
                                    for vector in (n, *triangle) for value in vector))

    def test_bounds_closedness_consistent_winding_normals_and_positive_volume(self):
        for entry in self.entries:
            with self.subTest(file=entry["file"]):
                records = binary_stl((PACK / entry["file"]).read_bytes())
                triangles = [triangle for _, triangle, _ in records]
                points = [p for triangle in triangles for p in triangle]
                minimum = tuple(min(p[i] for p in points) for i in range(3))
                maximum = tuple(max(p[i] for p in points) for i in range(3))
                self.assertEqual(minimum, (0.0, 0.0, 0.0))
                self.assertEqual(maximum, (40.0, 30.0, 2.0))
                self.assertEqual(entry["dimensions_mm"], [40, 30, 2])
                directed, welded = Counter(), Counter()
                for triangle in triangles:
                    self.assertNotEqual(unit_normal(triangle), (0, 0, 0), "Degenerate output triangle")
                    for a, b in zip(triangle, triangle[1:] + triangle[:1]):
                        self.assertNotEqual(a, b, "Collapsed output edge")
                        directed[(a, b)] += 1
                        welded[tuple(sorted((a, b)))] += 1
                self.assertEqual(sum(n != 2 for n in welded.values()), 0)
                self.assertEqual(entry["welded_non_two_face_edges"], 0)
                self.assertTrue(all(directed[(a, b)] == directed[(b, a)] for a, b in directed),
                                "Inconsistent winding on a shared edge")
                original = self.sources[entry["pass"]][entry["label_percent"]]["triangles"]
                for (normal, triangle, _), source_tri in zip(records, original):
                    expected = unit_normal(source_tri)
                    self.assertTrue(all(abs(a - b) <= 1e-6 for a, b in zip(normal, expected)))
                    geometric = unit_normal(triangle)
                    self.assertGreater(sum(a * b for a, b in zip(normal, geometric)), 0.999)
                    self.assertAlmostEqual(sum(x * x for x in normal), 1.0, places=5)
                actual_volume, source_volume = volume(triangles), volume(original)
                self.assertGreater(actual_volume, 0)
                self.assertAlmostEqual(actual_volume, source_volume,
                                       delta=max(1e-5, abs(source_volume) * 1e-5))

    def test_license_and_separate_source_notice_are_present(self):
        license_text = (PACK / "LICENSE-AGPL-3.0.txt").read_text(encoding="utf-8")
        self.assertIn("GNU AFFERO GENERAL PUBLIC LICENSE", license_text)
        notice = (PACK / "NOTICE.md").read_text(encoding="utf-8")
        self.assertIn("AGPL", notice)
        self.assertIn(PIN, notice)
        self.assertIn("Orca", notice)
        self.assertIn("CC BY", notice)

    def load_extractor(self):
        spec = importlib.util.spec_from_file_location("public_flow_extractor", ROOT / "scripts" / "extract_tinman_flow_models.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.PIN, PIN)
        self.assertEqual(module.SOURCES, EXPECTED_SOURCES)
        return module

    def test_extractor_reproduces_public_outputs_without_installed_tinman(self):
        module = self.load_extractor()
        with tempfile.TemporaryDirectory(prefix="tinman-flow-public-test-") as tmp:
            module.DEST = Path(tmp) / "pack"
            with contextlib.redirect_stdout(io.StringIO()):
                module.extract(PACK / "source")
            fresh = json.loads((module.DEST / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(fresh, self.manifest)
            for entry in self.entries:
                self.assertEqual((module.DEST / entry["file"]).read_bytes(),
                                 (PACK / entry["file"]).read_bytes())
            for filename in EXPECTED_SOURCES:
                self.assertEqual((module.DEST / "source" / filename).read_bytes(),
                                 (PACK / "source" / filename).read_bytes())

    def test_extractor_rejects_a_changed_pinned_source(self):
        module = self.load_extractor()
        with tempfile.TemporaryDirectory(prefix="tinman-flow-corrupt-test-") as tmp:
            base = Path(tmp)
            module.DEST = base / "output"
            bad_source = base / "input"
            bad_source.mkdir()
            first = next(iter(EXPECTED_SOURCES))
            data = bytearray((PACK / "source" / first).read_bytes())
            data[-1] ^= 1
            (bad_source / first).write_bytes(data)
            with self.assertRaisesRegex(ValueError, "pinned original"):
                module.extract(bad_source)
            self.assertFalse(module.DEST.exists())

    def test_binary_reader_rejects_truncation_and_trailing_metadata(self):
        data = (PACK / self.entries[0]["file"]).read_bytes()
        for damaged in (data[:20], data[:-1], data + b"private-account=not-allowed"):
            with self.subTest(size=len(damaged)), self.assertRaises(ValueError):
                binary_stl(damaged)


if __name__ == "__main__":
    unittest.main(verbosity=2)
