# Tinmans Rocket slicer tuning guide

A plain-language handbook for using Rocket Slicer to tune filament and understand
the FibreSeeker 3. It adapts the experimental method in **Tinmans Tuning Guide**
to Rocket's actual controls, templates, print modes, masks and fiber workflows.

**Working edition 0.1, 19 October 2026.** The installed reference is Rocket
1.4.0.705. Later-release additions are labeled separately. A model, profile or
published test file is not evidence of a successful print on your machine.

## Start with a known machine

Complete the manufacturer's machine calibration, preserve the current versions
and settings, identify each physical tool/nozzle and confirm a simple Rocket print
before tuning material. Do not change printer firmware, maintenance settings and
filament settings together to solve one symptom.

Follow this route:

1. [Establish the baseline and tool identity](guide/01-baseline-and-identity.md).
2. [Run controlled material tests](guide/02-controlled-tuning.md): conditioning,
   temperature, usable volumetric flow, pressure response where supported, flow
   multiplier, cooling/retraction, dimensions, seams and representative validation.
3. [Treat fiber and matrix as a separate workflow](guide/03-fiber-and-matrix.md).
4. [Read the result before changing another setting](guide/04-reading-results.md).
5. [Keep records and release a reproducible profile](guide/05-records-and-profile-release.md).

When a copied material leaves the Profile selector empty, use the
[matching material and process instructions](guide/08-material-and-process-selection.md).

The sequence preserves the original guide's core. It does **not** imply that
Rocket has the same automatic calibration generators, menu names, pressure-advance
controls or project overrides as Tinman or OrcaSlicer.

## Find a setting in plain language

The [field reference](guide/06-field-reference.md) follows the installed Rocket
controls. Look up the label you see, then check its material/process/machine scope
and print mode. Each entry distinguishes the control's purpose from a suggested
experiment and identifies options whose exact behavior still needs confirmation.

Useful questions include:

- Why is my part rough if the flow multiplier is correct?
- Is Max volumetric speed the same as printing speed?
- Does this material field affect normal plastic, composite matrix or fiber?
- Is this option changing one model, one mask, one layer range or the whole job?
- Why does a template or field disappear when I change print mode?
- Will this setting repair a mechanical fault, or only hide its symptom?

[Version and evidence rules](guide/07-versions-and-evidence.md) explain how to use
the reference when your Rocket version or hardware differs.

A stored parameter or translated label is not necessarily a selectable control.
For example, a visible Max volumetric speed editor has not been established in
this build. The tuning chapter uses verified feature speeds and exported-rate
checks rather than an assumed MVS menu.

## Calibration files

The [test catalog](tests/README.md) pairs reusable geometry with Rocket-specific
instructions and a validation status. Reusing a model does not carry over a
temperature/speed/flow schedule. Slice the model in Rocket with your recorded
machine, nozzle, material and process settings.

[Download working edition 0.1.0-preview and the original flow tiles](https://github.com/Tinman-FP/tinmans-rocket-slicer-tuning-guide/releases/tag/v0.1.0-preview).
The 19 meshes are source-checked; a representative zero tile has a native Rocket
slice and multiplier-output comparison. Physical validation is still pending.
Temperature/MVS conversion and additional native workflows remain in progress.
Do not substitute Tinman-generated G-code for a Rocket slice.
No universal ready-to-run machine G-code is supplied by this working edition.

## Keep the three kinds of setting separate

**Machine settings** describe the actual hardware and its calibration. **Material
settings** describe a particular polymer or fiber/matrix combination on that
hardware. **Process settings** describe how the part is built. A profile name is
not proof that those settings match your loaded tool and spool.

Copy an OEM template before editing it. Keep the original as a control, name each
candidate clearly, change one causal variable, save the complete project and final
file, and confirm the selected value on a fresh representative part. Never use
flow multiplier or dimensional compensation to disguise a loose, leaking or
partially blocked hotend.

## Safety and support records

Keep clear of hot surfaces and motion. Follow the manufacturer's loading,
maintenance and material instructions. Watch an unproven test and stop on a leak,
scrape, failed probe, lost adhesion, grinding or unstable temperature rather than
trying to tune past it. Continuous fiber adds feed, cutting, path-length and layer
placement conditions that an ordinary plastic coupon does not qualify.

Preserve original photos/logs, versions and settings before and after updates or
modifications, including unsuccessful attempts. The [experiment record](templates/experiment-log.md)
is a practical starting point. A good record supports factual troubleshooting; it
does not establish warranty coverage, certification or structural strength.

## Attribution and sources

William Tinney commissioned this Rocket-specific adaptation of his original guide.
Research, writing and tooling assistance are credited in [Credits](CREDITS.md).
Primary references and the installed-version basis are in [Sources](SOURCES.md).
The original guide remains unchanged. This is independent documentation, not an
official FibreSeek manual or endorsement.

Guide text is [CC BY 4.0](LICENSE). Third-party software, names, documentation and
models retain their own rights and licenses.

## Rebuild or contribute

Use Python 3.11 or newer. Install `requirements-pdf.txt`, then run
`python3 scripts/build_reference.py --published --strict` and
`python3 scripts/build_pdf.py`. The public rebuild does not need an installed
slicer, account database or private research directory. Run
`python3 scripts/test_publication.py` and `python3 scripts/test_tinman_flow_pack.py`
before proposing a change. See the flow pack's notices to reproduce mesh extraction.
