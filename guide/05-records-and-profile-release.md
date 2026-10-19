# 5. Keep records and release the right profile

A good profile must be repeatable by another person. Keep enough information
to explain what was tested, what actually happened and where the accepted
settings are stored.

## Give every experiment one record

Use a dated record for each print or failed attempt. Include:

- nonsecret physical machine identity and the person performing the action;
- reason for the test and the one variable changed;
- actual tool, nozzle diameter/material, plate and hardware condition;
- plastic, matrix and fibre identities as applicable, including colour, lot,
  drying, storage and actual loading state;
- Rocket and firmware versions, selected mode and material/profile revisions;
- all fixed temperatures, flow limits, multiplier, cooling and motion settings;
- geometry source, scale/orientation, project and final exported output;
- preview observations, intended target/job identity, start response and original
  warning or error messages;
- first-layer, deposition, route/cut and end-of-job observations;
- photographs, raw measurements, final controller state and physical result;
- decision, uncertainty, next isolated test and rollback/reference location.

Keep the final exported file, not just a screenshot or source project. If a
checksum is recorded, a SHA-256 checksum identifies exact file bytes; it does
not prove those bytes are appropriate for a printer. Do not publish connection
addresses, credentials, serials, private configuration or support correspondence.

## Use four honest status labels

| Status | Meaning |
| --- | --- |
| Candidate | A proposed or partially tested value; limitations remain |
| Accepted for the stated test | Repeated evidence supports a defined result, not necessarily an entire production profile |
| Rejected | Unsuitable, failed or invalid under the recorded conditions |
| Superseded or retired | Preserved history that is no longer the current recommended choice |

If the wrong nozzle, tool or inherited settings were used, label the test
**rejected — invalid baseline**. Preserve any useful observations, but do not
promote the numerical value to the intended setup.

Factory calibration still in progress is not passed. A simulated send is not
a physical print. A field not exposed by Rocket is not independently tuned.
An unknown cause remains unknown until new evidence resolves it.

## Name the physical scope clearly

The shop's naming standard separates status, physical machine, nozzle, material
and revision. In a human-readable record, the pattern is:

```text
Filament: STATUS | Machine ID | Nozzle mm | Brand Product Material [variant] | rNN
Process: STATUS | Machine ID | Nozzle mm | Brand Product Material [variant] | Layer mm Purpose | rNN
```

Use CANDIDATE until the required tests and representative validation pass for
that exact combination. Use TUNED only when the record supports that scope.
Include colour, formulation or another variant when it changes tuning. Do not
substitute a model name for a physical unit when two printers share that model.

Verify which characters and lengths the actual Rocket field accepts. A naming
convention is not a compatibility guard: maintain the complete scope in the
record and check the saved/reopened values even if the interface shortens a
display label. Keep the generic or OEM parent untouched as a reference.

## Validate a representative set

Before recommending a profile pair, confirm:

1. A broad top surface and continuous walls without missing deposition.
2. Multiple external dimensions, hole sizes and the intended functional fit.
3. Representative overhangs, bridges, corners, curves and travel distances.
4. The production layer height, wall strategy, speed, plate and chamber condition.
5. Relevant layer adhesion or mechanical behaviour, with conditioning and loading
   recorded, when the part has structural requirements.
6. Complete loading/tool-change/cutting/ending behaviour for a composite job.

Define pass/fail limits before printing. “No visible open top channels under
normal inspection” is useful; “looks perfect in one photograph” is not. A small
coupon does not prove a large footprint, a long print or a different nozzle.

For this inspected Rocket version, independent PA tuning has no verified native
method. State the preserved OEM behaviour and the unperformed stage. Do not
claim an exhaustive material tune or universal operating envelope from the
tests that are available.

## Confirm persistence in a clean project

Save the intended candidate material/profile pair, close or leave the test
project, and reopen a clean project using those saved choices. Verify the
physical unit and tool again; then slice representative geometry and compare
the effective output. A temporary model override must not silently become the
only place an accepted value exists.

Promote the tested candidate rather than making an unrelated copy with guessed
values. Record the recommended pair, revision, accepted stages, unsupported
stages and date. Keep one clearly current recommendation for each scope;
archive older generations recoverably outside ordinary active choices where
Rocket supports that workflow. Do not delete stock parents, other machines'
presets, dependencies or the only backup.

## Record changes with warranty-conscious precision

For the new unit, preserve original photos, messages and exports, and append
dated corrections rather than rewriting history. For every maintenance,
update or configuration change, record the as-found state, exact before/after
values, OEM versus unofficial procedure, reason, actor, result and rollback.
If calibration had already started before capture, say so.

Do not infer factory defect, warranty coverage, repair success or permission
to modify the replacement from the retained unit's history. Keep sensitive
identifiers and correspondence in private storage. A factual incident log is
more useful than an unsupported causal conclusion.

## Recheck after meaningful changes

Run a targeted confirmation after changing nozzle/hotend, material colour/lot,
conditioning, temperatures, substantial cooling, firmware, Rocket version or
tool mapping. Compare a known control before retuning several variables.

The commissioning goal is repeatable representative Rocket operation. Only
then revisit TinManX1. Do not make private beta release gates a prerequisite
for using Rocket, and do not treat a Rocket commissioning result as TinManX1
qualification.

**Basis:** [TG-CORE] chapters 00, 09 and 20 and its experiment/release templates;
[NEW-UNIT-RECORD]; [ROCKET-LOCAL]. Original method: William Tinney, with Codex by
OpenAI; CC BY 4.0. This is a separately titled Rocket adaptation, not an edit to
the original guide or an OEM-endorsed publication.
