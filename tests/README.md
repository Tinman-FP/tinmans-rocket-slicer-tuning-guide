# Rocket calibration test catalog

This catalog describes the question each test must answer. A mesh supplies geometry;
it does not schedule temperatures, flow or pressure advance. Rocket must slice the
test with your recorded tool, material, process and deliberate overrides.

## Original Tinman flow geometry

The first [flow pack](tinman-flow/README.md) reuses Tinman's existing coarse and
fine flow tiles, with all source triangles preserved. It supplies 19 separate
STLs, editable upstream originals, conversion source, licenses and a Rocket recipe.
Tile labels are not imported modifiers: use one explicitly calculated material
multiplier per separate Rocket slice.

All 19 meshes pass source/geometry checks. One representative zero-labelled tile
has passed native Rocket import/slicing and a 1.00-versus-0.90 emitted-deposition
comparison. No physical print, tuned preset, CFC qualification or native account
project is included. Read the exact [status](tinman-flow/ROCKET_CHECKS.json).

Temperature and maximum-flow originals are linked below while creator-license
verification and Rocket-specific test setup continue. The raw temperature asset
is a 700 mm, wide-range source model; it must be correctly cropped, not compressed
to make it fit. Numbers in its geometry do not set nozzle temperature.

The four earlier custom coupons are superseded local development history, not
the agreed Tinman-geometry pack. They are excluded from publication.

Do not use a Tinman G-code file as Rocket output or assume an Orca 3MF preserves
calibration modifiers when opened in Rocket. Do not distribute an account database,
connected-printer project or private machine G-code as a generic test.

## Temperature

Original asset: [Tinman/Orca temperature tower](https://github.com/OrcaSlicer/OrcaSlicer/blob/084c58f3653d3b0a555544110d1c11803b51140a/resources/calib/temperature_tower/temperature_tower.drc),
credited upstream to [gaaZolee](https://www.thingiverse.com/thing:2729076).
Redistribution and a Rocket-ready crop remain pending; this edition links the
source rather than redistributing it. Do not scale its Z height to select a range.

Use identical small coupons at separate fixed material temperatures unless a native
height schedule is verified. Compare stable extrusion, supported details, bridges,
stringing and cooled layer strength. Reject detached or motion-damaged specimens.
Stay inside the actual material and hardware operating limits.

## Maximum usable volumetric flow

Original asset: [Tinman/Orca volumetric-speed test](https://github.com/OrcaSlicer/OrcaSlicer/blob/ed1b03fe6db8bf26441cdec9d9cdefa099e68c8a/resources/calib/volumetric_speed/SpeedTestStructure.drc),
credited upstream to [CNC Kitchen](https://www.printables.com/model/342075-extrusion-test-structure).
Creator-license verification and Rocket rate scheduling remain pending; no converted
copy or automatic sweep is supplied here.

Use a long enough wall/path to reach the requested steady deposition rate. Compare
fixed-setting runs and inspect actual flow in the emitted file; acceleration or
cooling may prevent the requested speed from being reached. A cosmetic surface
change, extrusion discontinuity and loss of layer strength are different limits.
Record them separately and retain margin for the intended application.

## Flow multiplier

Use a broad supported top surface with several top layers. Compare candidate material
Flow multiplier values while holding temperature, speed, geometry and cooling fixed.
Look for closed lines without raised ridges or nozzle plowing. Confirm the chosen
value in a fresh job; do not tune global flow from the first layer alone.

## Pressure response

Corner tests can reveal bulging or thinning, but no Rocket 1.4.0.705 pressure-advance
field or automatic generator has been established. Keep OEM pressure behavior and
record this stage as fixed/unqualified rather than inserting arbitrary firmware
commands. A corner mesh alone is not an automatically varying PA test.

## Cooling and retraction

Use supported bridge/overhang and separated-feature geometry after extrusion is
stable. Change one cooling or travel/retraction variable. Keep matrix-only and fiber
movement rules separate; never assume normal-plastic retraction is suitable for CFC.

## Dimensions and fit

Measure fully cooled external spans, holes and fits at multiple locations. Separate
proportional shrinkage from a constant contour/hole offset and bottom-layer flare.
Do not alter axis calibration or global flow to hide a material shrinkage problem.

## Composite and representative validation

Use Rocket's intended fiber/matrix mode, loading and paths. Inspect actual fiber
placement, starts/ends, consolidation and interlayer behavior. Ordinary FFF coupons
cannot qualify fiber length, cutting, matrix delivery or structural strength. Finish
with a part that represents the actual application, and test relevant strength
rather than declaring a structural profile from appearance alone.

## Required release contents

Each public test needs model/source/license, an illustrated Rocket setup recipe,
version/tool/nozzle/material scope, one-variable schedule, fixed conditions, output
checks, interpretation, validation status and known limitations. A native Rocket
project, when supplied, must reopen without private target/account state. Published
results must identify tested conditions without implying universal safe values.
