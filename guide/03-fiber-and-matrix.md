# 3. Keep fibre and matrix testing separate from ordinary plastic

Continuous-fibre printing combines a plastic matrix with a separate strand.
Both must follow the intended physical route at the intended time. A correct
looking material name does not prove that the strand is loaded or being laid.

This chapter is not an approval for experimental empty-fibre T0 printing. Use
the current OEM-supported material/loading workflow on the actual machine.

## Identify what you are loading

| Material | Meaning | Do not confuse it with |
| --- | --- | --- |
| Ordinary plastic filament | The material used by the ordinary FFF tool | A continuous strand |
| Composite matrix plastic | The plastic selected for reinforced deposition | Proof that continuous fibre is present |
| Continuous fibre | The approved reinforcement strand and its own feed path | A chopped-CF plastic filament |
| Chopped-fibre plastic | Polymer with short dispersed filler | A continuous-fibre spool or automatic compatibility with any nozzle |

Use the approved plastic/fibre pairing for the selected workflow. Similar
polymer names do not establish compatibility. Record the brand, product, colour,
lot, drying/conditioning and loading state of both matrix and fibre.

## Understand the mode names without assuming the toolpath

The inspected Rocket family uses **Speedy**, **Reinforced** and **Fortified**
mode names. They are manufacturing strategies, not just three speed percentages.
Historical retained-machine exports showed ordinary-plastic-only output in
some cases, mixed plastic/composite routes in others and composite-heavy routes
in others. Geometry and effective settings changed the result.

In a later four-export historical comparison, Reinforced selected ordinary T1/E
output for both tested models, while Fortified generated fibre even on a small
specimen intended to be fibre-ineligible. Those observations are not a promise
that every Reinforced job contains fibre, or that a small Fortified part falls
back to matrix-only output.

Always inspect this job's preview and output. A mode name, a nonzero estimate
or a selected fibre material is not a substitute for actual routes and loading
checks. Use the field reference for the mode's individual controls; changing a
mode can change more than one effective setting.

## Loading is a physical state

Follow the current machine's manufacturer instructions and touchscreen sequence.
The public R1 manual distinguishes composite plastic, continuous fibre and FFF
plastic loading, and recommends composite plastic before fibre before FFF
plastic. Verify that the instructions apply to the actual firmware and tooling;
do not interrupt active factory calibration to load for a guide example.

Keep these states separate:

- selecting a fibre material in Rocket;
- physically inserting a strand;
- passing a loading sensor or reaching a reference point;
- completing the supported loading/preparation sequence;
- successfully depositing and cutting a reinforced route.

One does not prove the next. Do not defeat a loading warning or set fibre feed
to zero to make a different workflow appear satisfied.

Historical research did not establish that a stationary fibre strand seals
the matrix inlet. Nor did it establish that matrix-only printing through an
empty composite fibre channel is approved. Absence of an explicit prohibition
is not approval. A selected material cannot repair a leaking joint.

## Tune PCTG per nozzle without inventing a matrix-only mode

Start ordinary plastic commissioning with the verified ordinary tool and its
own PCTG candidate. Follow the material sequence in
[Controlled Tuning](02-controlled-tuning.md).

The composite nozzle is a separate system. Reuse ordinary-tool observations as
background only, not accepted temperature, flow or retraction values. Where
matrix tuning requires a loaded fibre workflow, keep the approved pair and
loading state intact. If the current OEM workflow does not offer an independently
supported matrix-only test, record that limit instead of forcing empty-fibre
operation. Obtain a supported method before claiming the composite nozzle's
matrix has been independently tuned.

Do not introduce a new polymer, fibre strategy, temperature, matrix feed and
fibre feed in one print. Establish the stock supported pair and a small
representative reinforced result first, then isolate a genuine material question.

## Choose a meaningful reinforced specimen

Use a part with enough room for the current strategy's legal paths, bends,
starts and cuts. Inspect the preview for actual reinforced layers and routes.
Do not disable minimum lengths or bend rules merely because a small test has
no fibre. Such a change tests another manufacturing strategy, not the same
material condition.

Before the print, record:

1. Physical unit, tool/nozzle and actual loaded plastic/fibre pair.
2. Rocket version, mode, profile revisions and any changed field.
3. Previewed ordinary and composite routes, reinforced layers and intended
   fibre directions.
4. Complete job output, including preparation, tool changes, fibre starts,
   cuts, tails and ending behaviour.
5. The question, control and physical pass/fail criteria.

Do not paste old cutter, prime, unload or material-axis commands into a new
job. Their distances and feed rates belong to a particular OEM sequence and
firmware context, not to a general calibration recipe.

## Observe the whole job

Watch the first ordinary and reinforced deposition, starts, corners, changes,
cuts and restarts. Check that fibre lies where the preview intended, rather
than forming loose loops, pulling a route off the part or accumulating near
the tool. A tool moving without deposition is a failed physical outcome even
if progress increases.

Stop on a leak, abnormal feed resistance, loose fibre accumulation, part
movement, missing deposition, failed cut or machine fault. Keep photographs
and original messages. Do not diagnose the cause solely from a polymer-covered
hotend photograph, and do not repeat the same fault as a material experiment.

After completion, examine the cooled part, not only the remaining fibre-length
estimate. Compare routing, coverage, defects, dimensions and the relevant
mechanical behaviour against a consistent control. Visual fibre coverage alone
does not establish strength or structural suitability.

## What historical exports may teach

The old matched-geometry exports and backend notes show why preview, effective
settings and the complete tool lifecycle matter. They are version-specific
retained-machine research, not replacement-machine calibration. The four
October 8, 2026 exports are explicitly archived **NEVER PRINT** evidence. Do not
reuse, send or strip metadata from them to make them printable.

Their old experimental flow restrictions are not new OEM ratings. Likewise,
the retained unit's reported repair, later recurrent leak, offsets and special
permissions do not transfer to the replacement. This guide does not recommend
disassembly, hot-tightening or pressure-limit experiments on the new unit.

**Basis:** [OEM-MANUAL]; [OEM-QUICKSTART]; [ROCKET-LOCAL]; [ROCKET-HISTORY];
[NEW-UNIT-RECORD]. Historical mode observations are explicitly bounded, not
general product guarantees.
