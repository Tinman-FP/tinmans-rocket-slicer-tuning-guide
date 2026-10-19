# Select a matching material and process in Rocket

Rocket's material selector and process selector are linked. Copying a plastic
material gives it a new identity. A process that accepts the original material
does not automatically accept the copy. If **Profile** becomes empty and Preview
is disabled after you select a copied material, check compatibility before changing
printing parameters.

## Copy the material

In Rocket 1.4.0.705, open **Prepare → Template Settings → More Options → Plastics**.
Choose the applicable OEM material and use its copy icon. Select the new entry
under **Customized**, give it a clear candidate name, and edit the intended value.
For ordinary-plastic flow testing, **Basic information → Flow multiplier** is the
material-wide multiplier. **Apply** saves the edits. The stock material remains
unchanged.

For example, a development-only comparison may use a clearly marked name such as
`CANDIDATE | GUIDE OFFLINE DO NOT PRINT | 0.4mm | OEM PETG | r01`. That is not a
production profile or a starting prescription for PCTG. Real tuning names should
identify your physical machine, nozzle, product and revision.

## Give the copied material a compatible process

Open **Profiles** in the same options panel. Use the copy icon on the applicable
OEM **profile-group header**. This copies the group's processes; it does not make
every copied process appropriate to every mode or nozzle.

Expand the custom group and select the ordinary **Speedy** process for an FFF
comparison. In this SK3 build, custom groups are broadly selectable with copied
materials. There is no reachable Compatible materials page in this workflow.
Do not mistake the custom group's availability for an enforced match to your
machine, nozzle or material; you must check that match yourself.

Use the custom group's rename/pencil action to give it a recognizable candidate
name. Return to Prepare
and explicitly select the copied **Plastic** material, the intended print mode
and the matching **Profile**. Confirm that layer height and other settings have
not reverted or disappeared. Recheck selections after import, reset or mode change.

## Check the slice before sending

Select **Preview** once and wait for slicing to finish. Review the ordinary-plastic
paths, top support and layer count. Print Details should agree with the intended
nozzle/material usage, but its labels alone do not prove the executable tool path.
Save a local G-code copy and verify the applicable emitted settings and routing.

For the flow pack, tile labels do not change the material multiplier. Use one tile
and one explicitly calculated value per slice. Do not confuse the **Composite**
matrix/fiber fields with the ordinary **Plastic** material. Native projects and
G-code can carry account metadata; do not upload raw exports as public test files.
