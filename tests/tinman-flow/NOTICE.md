# Original Tinman and Orca flow tile notices

These are the existing flow calibration meshes used by Tinman, not newly designed
test coupons. Credit SoftFever and the OrcaSlicer contributors. The upstream
calibration method also acknowledges inspiration from SuperSlicer.

The two original source models are distributed on the upstream repository's
**GNU Affero General Public License version 3 (AGPL-3.0)** basis. See
[the full license](LICENSE-AGPL-3.0.txt). They and the derived STL meshes are
**not covered by the guide's CC BY 4.0 license**. This notice does not replace
the license or imply OEM endorsement or a physically validated profile.

## Exact sources

The installed Tinman files match these pinned public originals byte-for-byte:

- [Flow Pass 1](https://github.com/OrcaSlicer/OrcaSlicer/blob/c6065d54fc37abec1992e7366d600251785f6517/resources/calib/filament_flow/flowrate-test-pass1.3mf):
  SHA-256 `6e86280ef6dd912dc4bf8c5eb00d0b21d218f74774602eb10c73c36e5cc2aa5f`.
- [Flow Pass 2](https://github.com/OrcaSlicer/OrcaSlicer/blob/c6065d54fc37abec1992e7366d600251785f6517/resources/calib/filament_flow/flowrate-test-pass2.3mf):
  SHA-256 `b2ac0302c36a810f9a178e1856c2989f05d283b8b98ee8f8b3b869e2829614af`.
- [Upstream source and license at the same revision](https://github.com/OrcaSlicer/OrcaSlicer/tree/c6065d54fc37abec1992e7366d600251785f6517).

Unmodified editable originals are in [source/](source/). The source contains only
the original generic model assets, not a user's saved machine/account project.

## Changes on October 19 2026

William Tinney's Rocket guide project, with Codex by OpenAI, extracted each of the
19 source objects as a separate binary STL. Every source triangle is retained.
Each tile is translated to the origin; there is no resizing, remeshing, smoothing,
decimation or relabeling. Binary STL stores float32 coordinates. The conversion
source is [extract_tinman_flow_models.py](../../scripts/extract_tinman_flow_models.py),
licensed under AGPL-3.0 for this conversion and its generated derivatives. The
manifest records each original object, dimensions, triangle count and hash.

To rebuild from the included sources, use Python 3.10 or newer from the repository
root: `python3 scripts/extract_tinman_flow_models.py`. No slicer or network is needed.

STL does not carry units, material settings or calibration modifiers. Import as
millimeters and verify 40 × 30 × 2 mm before slicing. Numbers on the tiles are
geometry, not instructions executed by Rocket. Use the accompanying recipe.
