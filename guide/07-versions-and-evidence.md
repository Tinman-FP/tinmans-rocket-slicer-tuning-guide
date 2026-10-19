# Versions and evidence

## Use the instructions for the version you have

This edition targets **Rocket 1.4.0.705**. Its field reference separates controls
found in that installed build from features mentioned only in newer documentation.
If your screen differs, check the version and selected print mode before searching
for a renamed control. A bundled field definition can exist without appearing in
your current mode. [ROCKET-LOCAL]

The public **1.4.1** notes describe a new Pro switch controlling Fortified access,
additional infill controls and other changes. They also list fixes affecting
extrusion-area mapping and temperature changes between fibre and plastic layers.
Those notes are a reason to check versions, not permission to describe the new
behavior as present in 1.4.0.705. [OEM-141]

The **1.4.0** notes do not identify build 705, and some preview work is described
as pending merge or validation. For a disputed feature, prefer a recorded
observation in the installed build over an assumption based on a release heading.
[OEM-140]

After an update, reopen a copy of a known project, inspect its resolved settings
and preview, and compare the exported result before printing. Keep the previous
project and settings so you can identify what changed. Successful import alone
does not prove that an old setting retained its meaning. [TG-CORE]

## “Calibration” can mean different things

Machine calibration establishes a hardware relationship, such as bed alignment
or fibre feed length. Material tuning establishes how a particular filament
behaves with a particular nozzle and set of conditions. One does not replace the
other.

For example, FibreSeek documents **Fibre Extrusion Calibration on the printer
touchscreen**. That is not evidence of a Rocket temperature-tower, pressure-advance
or plastic-flow generator. Follow the applicable OEM procedure for hardware
calibration, then use a separately identified material test. [OEM-FIBRE-CAL]

Pressure advance is useful material theory, but this edition has not established
a selectable Rocket 1.4.0.705 pressure-advance control, its supported range or a
native generator. Do not paste another slicer's commands or values into Rocket
to fill that gap. The filament vendor's recommendation to tune pressure response
does not prove that this software exposes the needed control. [3DF-PA]

The same distinction applies to Max volumetric speed: a translated label and
stored property were found, but not a selectable editor in the inspected build.
Use verified feature-speed tests and actual output checks; a backend property or
translated input-range hint is not a user-facing workflow or a hardware rating.

Likewise, a **3MF file is not proof of a working parameter sweep**. It may contain
geometry without the intended per-object or per-layer changes. A test must be
opened in the stated Rocket version and checked after slicing before it is called
a validated native project.

Use Rocket's verified mode and tool assignments. Do not reuse a numerical T0/T1,
slot or extrusion-axis mapping from the earlier experimental TinMan beta merely
because the physical printer has similar nozzle names. Public nozzle specifications
do not establish those software mappings. [OEM-SPEC]

## Read a test file's status before using it

The public test catalog uses these distinctions. Each status belongs to one
specific file revision and software version, not to every file with the same name.

| Status | What it establishes | What it does not establish |
| --- | --- | --- |
| Prepared | A test file and its intended settings have been created. | Correct Rocket import, a working sweep or a successful print. |
| Native project validated | The file has been reopened in the named Rocket build; intended settings and sliced output have been checked and recorded. | Safe physical operation or a measured material result. |
| Printed — physical validation pending | A print attempt is recorded with its conditions. | That the specimen passes the test or that a value is tuned. |
| Physically validated | The specified specimen was examined or measured against stated acceptance criteria, with conditions and evidence recorded. | Validity for another material, nozzle, machine or operating range. |

A future GitHub download must carry its actual status. A public link, a thumbnail
or a successful slice does not promote it to a physically validated test. If a
file is only prepared, say so beside its download—not only in a general disclaimer.

## Keep conclusions attached to their evidence

Record the Rocket version, project revision, machine and nozzle context,
material, conditioning, settings and result. Change one causal variable at a time
after an initial search. Retain a control specimen and test the chosen value on a
representative part before releasing a profile. These are experimental-method
principles adapted from the original guide; they do not require Rocket to share
Orca's menus. [TG-CORE]

Private current-unit records may support a local observation, but they are not
universal printer specifications. Public examples omit unit identifiers,
connection details, raw firmware/configuration exports and account data.
[NEW-UNIT-RECORD]

Where this guide says **not established**, it means the available evidence does
not settle the point. It does not mean the feature is impossible or permanently
unsupported. A later verified observation can close that gap without rewriting
an assumption as an earlier fact.

For source editions and direct links, see [Sources](../SOURCES.md).
