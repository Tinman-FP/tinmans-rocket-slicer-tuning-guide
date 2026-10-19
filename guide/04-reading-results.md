# 4. Read the result without inventing a winner

Judge the physical specimen against a question and a control. A completed file,
a glossy photograph or a higher final test value is not enough to release a
profile.

## Make comparisons readable

Let parts fully cool. Mark each sample with its actual tested value and tool.
Photograph the same faces under diffuse light and then low-angle, glancing
light. Include an overall view, the relevant feature and a label. Glossy plastic
can hide channels in one direction and exaggerate ridges in another.

For a flow coupon, touch the top carefully after cooling. For dimensions, zero
the instrument, measure several places and retain the raw readings. Do not
measure through a seam, corner bulge or bottom flare and call that the whole
part's size. A tiny difference close to the instrument's uncertainty is not a
defensible improvement.

## Appearance is a clue, not a diagnosis

| Observation | Useful next check | What not to assume |
| --- | --- | --- |
| Popping, pits, wisps or foamy roads | Filament conditioning and a clean feed path | That retraction is the only problem |
| Walls thin only as requested flow rises | Actual rate, temperature, feed grip and resistance | That the global multiplier is necessarily low |
| Broad top channels | Supported top thickness, speed, width and flow | That increasing flow fixes unsupported infill |
| Raised top ridges or nozzle ploughing | Excess deposit, lower-layer compression and path endings | That every glossy highlight means excess flow |
| Corner bulges or lean transitions | Effective OEM pressure behaviour, speed and acceleration | That the seam alone proves a PA value |
| Sagging or broken bridge strands | Anchors, bridge speed, flow and bridge-only cooling | That the normal fan value tells the whole story |
| Gaps immediately after travel | Retraction/restart, pressure recovery and feed continuity | That more retraction will help |
| Repeating texture along steady walls | Speed dependence, motion and hidden geometry | That every vertical mark is ringing |
| Periodic ripples fading after a corner | Motion resonance and a controlled mechanical baseline | That a flow change corrects resonance |
| One axis long and the other short | Multi-size XY measurements, orientation and mechanics | That one shared scale value can correct both |
| Polymer outside the hotend assembly | Stop and record the first visible escape point | That the guide has proved a pressure cause or a repair |

Change one causal variable after these checks. If no tested value looks good,
reject the range or the baseline instead of choosing the least bad number and
calling it tuned.

## Use explicit decisions for each test

### Temperature

Require stable extrusion, usable detail and sufficient cooled adhesion at the
intended rate. The most attractive low-speed surface can still be too cold for
the intended throughput. If the best sample is at the supported test endpoint,
record an unresolved boundary rather than an exact optimum.

### Maximum volumetric speed

Look for the first sustained decline, not one isolated blemish. Select a
working ceiling with margin below a repeatable decline. If all samples pass,
the evidence establishes only the tested passing range. If a sample leaks,
detaches, grinds or faults, stop; that is not a normal acceptable stress point.

### Pressure advance

Low pressure compensation can leave swollen transitions; excessive compensation
can starve them. Read non-seam corners and representative motion conditions.
These are generic interpretation rules, not proof that Rocket exposes a PA
control. In this edition, no supported user-facing Rocket PA method was found;
mark the stage unperformed rather than assigning a visually guessed value.

### Flow multiplier

A useful top surface is continuous and reasonably even without broad open
channels, repeated ploughing or wall buildup. Compare centre and boundary. If
only endpoints are overfilled but the centre is correct, investigate the path
and pressure transition before lowering global flow.

### Cooling and bridges

Compare geometry and cooled adhesion together. A sharper bridge that causes
weak layers elsewhere is not an unconditional improvement. Keep ordinary and
bridge-only fan effects separate, and repeat in the intended chamber state.

### Dimensions

Keep signed errors: measured minus nominal. If several larger features show a
proportionally larger error, investigate material scale. If different sizes
share a nearly constant offset, investigate contour compensation. If only the
bottom is enlarged, investigate first-layer and elephant-foot causes. Verify
the actual Rocket field's convention before applying any correction.

### Seams and surfaces

Separate the finish of one road from the start of the next. Use a repeatable
location while diagnosing. Moving a defect to the back or spreading it around
the model does not prove its cause is fixed. If cosmetic settings repeatedly
move the same broad disturbance, return to tool/nozzle/profile identity.

## Printed labels and requested values can mislead

The embossed number on a borrowed model may describe its original test, not
the output Rocket created. A model's height does not prove temperature, speed
or PA changed at that height. Short segments may not reach requested speed,
and a material cap may reduce it. Keep the actual saved field value and final
output beside the specimen.

Do not use a foreign 3MF's labels as the calibration schedule. For the fixed
coupon method, label each specimen with the real constant value used for that
Rocket slice.

## Separate software outcome from physical outcome

| Recorded event | What it establishes |
| --- | --- |
| Slice succeeded | Rocket produced an output under its current configuration |
| Send request returned | A request was reported, not necessarily physical deposition |
| Printer reports printing | The controller reports an active job |
| Printer reports complete | The controller reached its completion condition |
| Cooled sample inspected and measured | Evidence about the actual physical result |

A timeout does not tell you whether a send or start succeeded. Inspect the
printer's actual current job before any retry; do not create a duplicate start.
A completed job with no filament deposited is not a successful material test.

## Classify failed starts correctly

Failed homing, probing, loading, plate retention, heating or tool preparation
belong in the machine/workflow incident record. Keep them, but do not average
them into the accepted material value. Record where observations became invalid.

Historical Tinmans chapters include a retained-machine seam investigation that
improved after correcting a mistaken nozzle/process baseline. Its lesson is
to verify identity, not to copy its numbers. Older VFA and acceleration examples
likewise demonstrate diagnostic reasoning, not new-unit motion limits.

Proceed to [Records and Profile Release](05-records-and-profile-release.md)
when the result meets an explicit requirement and can be repeated.

**Basis:** [TG-CORE] chapters 02–09, 19 and 20; [ROCKET-LOCAL]. No photograph or
case study in the source guide constitutes replacement-unit acceptance.
