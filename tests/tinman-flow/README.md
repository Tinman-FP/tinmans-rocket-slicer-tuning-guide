# Tinman flow tiles for Rocket

Use the original Tinman and Orca Flow Pass 1 and Pass 2 geometry, sliced by Rocket.
This pack contains 19 independent 40 × 30 × 2 mm meshes, their original editable
sources, conversion script and separate [AGPL notices](NOTICE.md). There is no
G-code, machine target, material preset or automatic flow schedule.

**Do not import all tiles and assume their labels change flow.** In this recipe,
slice one tile per job with one explicitly entered material Flow multiplier.
Rocket does not execute Tinman's calibration generator when it imports an STL.

## Before using this test

Establish temperature and a usable throughput region first. Keep any unsupported
PA stage marked unperformed; preserve supported OEM pressure behavior. A nozzle
leak, feed problem, damp filament or incorrect first-layer gap invalidates the
comparison. This first pack addresses ordinary FFF, not CFC/matrix qualification.

Use the actual machine, ordinary FFF nozzle, spool and plate. Start with a copied,
appropriately named candidate process/material pair rather than editing a stock
template. No setting in this pack is an accepted PCTG or replacement-unit value.

## Choose and calculate the candidate

Let `B` be your current candidate material Flow multiplier. A tile marked `d`
means the intended relative percentage change for this comparison:

```text
candidate material Flow multiplier = B × (1 + d / 100)
```

Pass 1 labels are −20, −15, −10, −5, 0, +5, +10, +15 and +20. These are the
original coarse-test labels, not a requirement to print every extreme. Start near
your baseline and use only justified changes. For example, if `B = 0.98`, the
tile labelled `+5` is tested at `0.98 × 1.05 = 1.029`. This is arithmetic, not a
recommended setting for your machine.

Pass 2 labels are 0 through −9. Rebase `B` to the selected coarse candidate;
the same formula applies. Do not subtract the label directly from the multiplier
or compound each new test on the previous tile. A finer intermediate comparison
can reuse the zero-labelled mesh, with the actual value recorded externally.

## Slice in Rocket

1. In **Prepare**, select the intended printer template, ordinary **Plastic**
   material and **Speedy** mode. Identify the actual physical nozzle and material;
   a mode name or template label does not prove the output tool.
2. Use **Add models** and open one STL from `models/`. Import in millimeters,
   flat on the plate, at 100% scale. Verify 40 × 30 × 2 mm.
3. Use **More Options → Plastics → Basic information → Flow multiplier** on
   your copied material, then **Apply**. Copy the relevant OEM process group under
   **Profiles**, select its **Speedy** process, and select that custom group with
   the copied Plastic in Prepare. See [matching selections](../../guide/08-material-and-process-selection.md).
   Enter the calculated value; do not change composite/fiber feed or a
   feature-only flow setting instead. Record the entered value and saved selection.
4. Keep temperature, layer height, line width, walls, top/bottom thickness, infill,
   speeds and cooling identical between candidates. At a 2 mm specimen height,
   make sure the selected layer height and shell settings leave a broad, supported
   top with several solid layers. Do not assume Tinman's ten-layer scaling or
   shell overrides were imported. Do not stretch the model silently for a larger
   nozzle; document any deliberate geometry change as a new variant.
5. Select **Preview** and let Rocket slice. Check every layer for a supported top,
   the intended ordinary-plastic paths, no fiber paths and a rate inside your
   established working region. Cooling and feature-speed limits can change timing.
6. Check the selected material and actual output again before any send. Keep
   printer-specific starting, sensing and preparation behavior from the applicable
   OEM template. Do not run another slicer's G-code or paste firmware commands.

The exact material-editor click path and its emitted effect must be checked for
your installed Rocket version. This working recipe does not claim that a hidden
field or an imported label supplies the intended multiplier. Stop if you cannot
identify the ordinary-plastic Flow multiplier or verify the output.

## Read and confirm the result

After cooling, inspect the whole top under glancing light and with a light touch.
Low flow leaves open channels and poor line joining. Excess flow creates raised
ridges, nozzle plowing and piled-up line ends. Seek an even, closed surface without
broad ridges; do not compensate for bad support below the top by increasing flow.

Record every tile's actual value, conditions and photographs. Confirm the chosen
candidate in a fresh Rocket slice and a representative part. Cosmetic quality
alone does not qualify strength or the complete material profile. See the guide's
[controlled tuning chapter](../../guide/02-controlled-tuning.md).

## Validation status

Mesh dimensions, source identity and triangle preservation are checked by the
included tests for all 19 tiles. The zero-labelled sample was imported and sliced
in Rocket 1.4.0.705 at 0.2 mm in ordinary-FFF Speedy mode. Separate native slices
at material Flow multiplier 1.00 and 0.90 retained identical motion paths; their
XY-deposition ratio was 0.89999921. E-only retraction recovery remained unchanged.
This verifies that comparison, not every tile or all possible settings. Other
tiles have not been individually sliced in this check.

Native observations and limitations are recorded in
[ROCKET_CHECKS.json](ROCKET_CHECKS.json). No tile has been physically validated by this pack. There
is no production TUNED preset or ready-to-print job here.
