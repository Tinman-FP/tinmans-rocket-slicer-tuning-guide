# 1. Establish the machine, material and job identity

Tuning means changing one setting, printing a controlled sample and deciding
whether that change helped. It does not mean trying settings until a printer
with a mechanical fault happens to finish a part.

This chapter comes before every material test. It applies separately to each
physical FibreSeeker, not just to the model name shown in Rocket.

## Know what this guide has and has not verified

The Rocket field survey for this edition inspected the installed macOS bundle
labelled **1.4.0.705**. Its other component version labels differ. Record the
version that your application shows; do not treat an algorithm or exported-file
version as an interchangeable application version. Field availability can change.

No native temperature, maximum-flow, flow-ratio or pressure-advance test generator
was found in that inspected Rocket build. Its **AI Calibration** preprint option
is not evidence of a filament pressure-advance calibration. The controlled tests
in this guide therefore use ordinary models sliced in Rocket at fixed settings.

On October 19, 2026, the owner reported that the replacement FibreSeeker was
received, online and still performing factory calibrations. Those are owner
reports, not independently verified calibration passes or completed Rocket
prints. Its formal physical-unit identity was still pending. Do not copy the
retained machine's targets, offsets, tuning values, repair conclusions or
experimental permissions to the replacement.

## Understand the material paths

The manufacturer distinguishes three material paths, not three independent
printing nozzles:

| Path | What goes through it | What it does |
| --- | --- | --- |
| Ordinary FFF plastic | A supported plastic filament | Prints ordinary plastic roads through the FFF tool |
| Composite plastic, also called matrix | The plastic used with continuous reinforcement | Provides the plastic around a reinforced route |
| Continuous fibre | The specified continuous strand | Reinforces a route through the composite system |

Do not put continuous fibre through the ordinary plastic nozzle. Chopped-fibre
filament, such as a plastic sold as CF-filled, is not the same thing as a
continuous strand. A plastic nozzle's diameter does not prove that it is suitable
for abrasive filled filament.

Old retained-machine exports used tool identifiers such as T0 and T1. Those files
are useful historical evidence, not permission to guess the replacement's
physical mapping. Match the selected tool to the actual nozzle, loading path and
current OEM definition before printing.

## Preserve the starting point

For a new machine, keep an as-found record before updates or unofficial changes:

1. Assign a nonsecret shop identity that distinguishes this unit from every
   other printer of the same model. Keep serial numbers and connection secrets
   in private records, not in a published guide or shared screenshot.
2. Record the firmware and Rocket versions, nozzle/tool labels, plate, supplied
   materials and visible condition. Photograph relevant assemblies and messages.
3. Let active factory calibration finish. Save its actual results, including
   warnings or failed steps. An animation finishing is not proof that every
   calibration passed.
4. Preserve available OEM profiles, projects and version information through
   supported export or backup methods. Do not install SSH merely to follow this
   guide. Record what could not be captured.
5. If an OEM update is appropriate, record its source, version before and after,
   result and any requested recalibration. Never call an after-calibration backup
   a pristine pre-calibration backup.

This creates a factual record for troubleshooting and possible warranty review.
It does not establish warranty coverage or a fault's cause. The old development
unit's reported support or rights waiver is not a waiver for a new unit.

## Inspect before changing material values

Check nozzle cleanliness and condition, filament-path resistance, spool freedom,
fan operation, plate seating and the machine's supported homing/probing checks.
Use the manufacturer's maintenance procedures. Do not change steps, rotation
distance, tool offsets or hidden firmware limits to hide one spool's defect.

Stop if the nozzle leaks, the tool scrapes the plate, the feed grinds or stalls,
the part moves, the machine loses position, or a fault appears. Photograph and
record the event separately from material results. A leak is not an acceptable
way to discover a material's maximum flow.

Prepare the actual plate using its manufacturer's cleaning and adhesive advice.
Textured PEI, smooth coatings and other surfaces are not interchangeable. Keep
plate preparation, bed temperature and the first-layer method consistent between
comparison prints.

## Verify the four descriptions of the same job

| Description | Beginner's check |
| --- | --- |
| Physical machine | Correct unit, installed nozzle, material path, loaded spool and plate |
| Rocket printer selection | Correct model, nozzle/tool definition and intended connection |
| Material and profile selections | Correct plastic or matrix/fibre pair, temperatures and candidate revision |
| Preview and exported output | Correct tool, dimensions, layers, material routes and intended settings |

A familiar name is not enough. Recheck after importing a project, changing a
mode, changing materials, selecting another printer or reopening Rocket.

For a new test, use a clean project and clearly identify its owning printer and
job. Do not repurpose another operator's session or change its target while it is
printing. Rocket work does not require opening TinManX1. Keep only the intended
test on the plate and avoid old calibration projects that may retain overrides.

Before pressing Print, verify the connection belongs to this physical unit,
review the preview, and keep the exact exported file with the test record. Use
Rocket and the printer's supported preparation sequence; do not insert generic
homing, extrusion or tool-change commands from another slicer.

## First-layer pass rule

Watch the first layer. Adjacent roads should meet without deep ploughed ridges;
the sample should stay attached through corners; the nozzle must not scrape.
If the sample detaches, material observations after detachment are invalid.

Do not set global flow from the first layer alone. Plate texture, initial-layer
height and nozzle-to-plate distance deliberately affect its appearance.

When the baseline repeats reliably, proceed to
[Controlled Tuning](02-controlled-tuning.md).

**Basis:** [TG-CORE] chapters 00, 01 and 20; [ROCKET-LOCAL]; [OEM-MANUAL];
[NEW-UNIT-RECORD]. This Rocket adaptation changes the workflow, not the original
guide's requirement to prove the baseline.
