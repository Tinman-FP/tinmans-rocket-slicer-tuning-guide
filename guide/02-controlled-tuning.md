# 2. Run controlled material tests in Rocket

Keep the original Tinmans dependency order:

1. Prove the baseline and tool identity.
2. Condition the filament and establish temperature.
3. Establish a conservative maximum volumetric speed.
4. Evaluate pressure advance only through a verified supported method.
5. Set ordinary plastic flow multiplier.
6. Balance cooling and bridges, then retraction and travel.
7. Check dimensions and fits.
8. Refine seams and surfaces.
9. Validate representative parts before releasing the profile.

Later tests depend on earlier ones. Increasing temperature can change flow,
stringing and pressure response. Exceeding the melt limit can make a correct flow
multiplier look too low. A dimensional correction can hide an extrusion fault.

Run this sequence separately for each verified tool/nozzle/material combination.
The ordinary plastic tests below are not approval for an empty-fibre composite
nozzle. For that path, read [Fibre and Matrix](03-fiber-and-matrix.md) first.

## Use separate fixed-setting coupons

A **coupon** is a small sample designed to answer one question. A temperature
coupon might include a wall, short bridge and small detail; a flow coupon needs
a broad, supported top surface. No single model proves everything.

The inspected Rocket build has no verified native filament-calibration generator.
Use the following repeatable method instead of looking for a Tinman Calibration
menu that is not present:

1. Obtain an appropriately licensed geometry-only model, such as an STL. Record
   its source. Check scale, orientation, contact with the plate and tool assignment.
2. Start a clean Rocket project using the correct OEM baseline and a clearly
   labelled candidate material/profile copy. Preserve the stock reference.
3. Choose one variable and state the question, for example: does the next
   supported temperature improve bonding without unacceptable stringing?
4. Save a separate variant for each tested value. Slice and inspect every variant
   in Rocket. Keep geometry and all other listed conditions unchanged.
5. Export and name each actual output so its test value is unambiguous. Print one
   variant, label the cooled specimen and record the outcome before the next.
6. Narrow the range around the useful region. Confirm the candidate in a fresh
   project and a separate print.

A borrowed STL supplies shape, not a temperature or PA schedule. A 3MF may also
carry foreign profiles, tools, model scaling or object settings. Importing a
Tinman/Orca tower does not prove that its height-dependent changes survived in
Rocket. Never send another slicer's G-code as a substitute for a Rocket slice.

Do not put several identical coupons on one plate and assume each has a different
material value. That requires independently verified per-object control. Separate
fixed-setting prints avoid that ambiguity.

## Freeze the comparison conditions

Record and hold the printer, tool/nozzle, spool, drying, plate preparation,
layer height, line widths, orientation, speed, acceleration, fan schedule, bed and
chamber conditions constant unless one is the variable under test. Keep a control
specimen and photograph the same surfaces in similar light. A shorter print is
not a better experiment if it changes several conditions at once.

## Stage A: dry the filament and establish temperature

Use the filament manufacturer's current drying instructions and check that the
spool tolerates them. Record dryer temperature, duration, storage and time out of
the dry box. Popping, bubbles, pits and strings can be moisture symptoms; they do
not prove a temperature error by themselves.

Rocket's inspected plastic-material control is **Extruder temperature**. Verify
which selected material/tool it affects and distinguish normal printing from
first-layer or standby temperatures where separate controls are available.

For fixed-setting temperature coupons:

1. Start within both the material's recommended range and the printer's supported
   range. The narrower applicable limit wins.
2. Use moderate flow and the same geometry, cooling and speed for every sample.
3. Compare walls, detail, bridge anchoring, stringing and cooled layer adhesion.
4. Find a useful region, then refine. A best result at the endpoint means the
   useful region was not bracketed; do not extend beyond supported limits.
5. Select a temperature that meets the required adhesion and detail at the
   intended flow, then confirm it during the flow test.

A photograph cannot prove strength. Use a consistent, safely handled mechanical
comparison when strength matters. Do not copy an old machine's accepted PCTG
temperature into a replacement as if it were already tuned.

## Stage B: establish maximum volumetric speed

**Maximum volumetric flow**, in **mm³/s**, is the volume of plastic requested per
second. It is not travel speed or Flow multiplier. Rocket contains a stored
`maxVolumetricSpeed` property and translated label, but no selectable control for
it was established in the installed editor schemas. Do not treat that label as a
verified menu instruction or edit a backend database to create a calibration method.

For a quick planning estimate:

```text
volume per second ≈ printed speed × line width × layer height
maximum printed speed ≈ volume limit ÷ (line width × layer height)
```

For example, a 0.50 mm line, 0.20 mm layer and 50 mm/s printed speed request
approximately 5 mm³/s. This is an illustration, not a FibreSeeker starting
setting. Slicers use bead models, flow corrections and rounded coordinates, so
the estimate is not an exact audit of the emitted material.

Use a coupon with long enough printed paths to reach steady speed. Begin with
the applicable OEM/material baseline and a conservative rate. Increase the
requested rate in controlled steps, using separate Rocket slices. Keep the
accepted temperature and representative cooling fixed. Check that an unrelated
feature-speed limit or minimum-layer-time rule is not preventing the intended
rate from being requested.

Watch for a sustained loss of gloss consistency, thinning, gaps, missed feed,
grinding, temperature droop or poorer adhesion. Stop at the first meaningful
failure; do not continue until a blockage or leak occurs. If no defect appears,
record only that the tested range passed, not that the last value is the maximum.

Record a working ceiling below the first repeatable quality-loss region, with
margin for long jobs and material variability. This is not an enforced global
Rocket MVS cap: constrain and check every relevant extrusion feature using the
supported feature speeds for the current width, height and flow multiplier.
Recheck those requests whenever those settings change. Recheck layer strength separately.
Do not change a firmware pressure or motor limit to make this test go farther.

Use the applicable verified feature Printing speed controls, known layer height
and line width to make separate fixed-setting samples. Other profile or machine
limits may reduce the request; a short feature may never reach steady speed.
Checking the actual exported rate requires a verified interpretation of Rocket's
tool, extrusion-axis, coordinate and material-volume conventions; a generic E-axis
or T0 assumption is not sufficient. If that interpretation is unavailable, report
the requested test conditions and the rate as unverified rather than inventing an
achieved throughput. Do not assume a material cap was editable or that a requested
speed was reached. If a later Rocket version exposes a
volumetric limit, verify its scope and emitted effect before using it.

## Stage C: pressure advance has an explicit support boundary

Pressure advance compensates for the delay between changing feed speed and
changing nozzle pressure. It can improve corners and starts, but cannot repair
wet material, a clog or the wrong global flow.

**No user-facing PA/Linear Advance field or native PA generator was found in the
inspected Rocket 1.4.0.705 resources.** AI Calibration is not a substitute. Do not
invent a PA menu, enter a Tinman K value elsewhere, or paste generic firmware
commands into Rocket start code.

For this edition, preserve the applicable OEM pressure behavior, record whether
it can be identified in the supported output, and mark independent PA tuning
**not performed / no verified Rocket method**. Do not call that stage passed.
You may continue bounded ordinary tests using the recorded OEM baseline, but
the released profile must disclose this limitation.

If a later verified Rocket/firmware version supplies a supported method, follow
that version's instructions: keep temperature, safe flow, geometry, cooling,
speed and acceleration fixed; locate a broad useful range; confirm a narrower
range at representative motion; read non-seam corners; then validate a real
part. The numerical range and height formula belong to that method, not to a
borrowed tower. No raw-command workaround is prescribed here.

## Stage D: set Flow multiplier

**Flow multiplier** changes how much plastic Rocket commands. A value near one
is a ratio, not a volumetric-flow rate. Confirm the exact field's units and the
currently selected plastic; composite plastic and continuous fibre have separate
controls and must not be treated as one multiplier.

Use a broad top-surface coupon with enough support and several top layers. Print
below the accepted flow ceiling. Compare actual saved multiplier values in
separate slices; do not assume Orca's labelled coarse/fine tile calculation.

Choose the lowest useful region that closes broad channels without ridges,
ploughing or material piled against the wall. Judge the centre and the boundary
under glancing light and by touch. Confirm on a separate sample.

If the starting ratio is 0.98, a deliberate two-percent relative increase would
be 0.98 × 1.02 = 0.9996. That explains the arithmetic; it does not mean Rocket
adds or multiplies an imported tile label. Enter and record the actual value.

Do not judge global flow from a thin first layer or one caliper reading across a
flexible single wall. Do not raise it to repair only an unsupported top skin.
Recheck the requested flow envelope after a meaningful multiplier change.

## Stage E: cooling and bridges, then retraction

Separate the part fan from heatsink cooling, chamber circulation and exhaust.
Never reduce a protective heatsink fan to improve surface appearance.

Use repeatable overhangs and known bridge spans. Hold material, temperature and
motion fixed. Compare shape, sag, anchoring, curl, lifting and cooled adhesion.
Use the least cooling that meets both geometry and bonding requirements.

Normal cooling and bridge-only cooling are different settings. A bridge override
can request more cooling than ordinary walls. Inspect both; do not copy a
bridge stress-test value into every layer. Chamber conditions must match the
intended use.

Only then assess travel strings. Rule out moisture and nozzle contamination
first. For the ordinary plastic path, Rocket exposes **Retract length**. Keep
retraction speed fixed, compare supported distances, and choose the shortest
repeatably clean result. Excessive retraction can cause lean restarts, grinding
or clogs. Test speed separately only if needed.

Ordinary plastic travel, tool changes and the composite fibre loading/cutting
cycle are different operations. Do not copy an ordinary retraction distance into
the composite system. Keep OEM composite sequences intact.

## Stage F: dimensions, seams and representative validation

Measure fully cooled parts after extrusion and cooling are stable. Test several
sizes, both X and Y, holes and a functional fit. A proportional size error, a
nearly constant contour offset and an enlarged bottom edge need different
corrections. Do not change machine motion calibration to fix material shrinkage.

Confirm Rocket's actual compensation convention before entering a percentage or
offset. Orca's measured-percentage field is not proof that a Rocket field uses
the same formula. If X is long and Y short, stop shared-scale compensation and
investigate the axis-specific cause.

For seams, first choose a repeatable location using controls actually present
in your build. Compare starts and ends separately. Change one supported seam,
travel or wipe control at a time; do not assume Tinman's scarf features exist.
If several settings merely move or spread the defect, recheck nozzle/profile
identity instead of adding more cosmetic changes.

Finally print representative geometry at the intended layer height, speed,
plate and chamber condition. A calibration sample is a candidate. It becomes a
released profile only after the required surface, fit, adhesion and reliability
checks in [Records and Profile Release](05-records-and-profile-release.md).

**Basis:** [TG-CORE] chapters 00–10, 19 and 20; [ROCKET-LOCAL]. The physical
sequence is retained; unsupported native-generator instructions are replaced
with explicitly limited Rocket workflows.
