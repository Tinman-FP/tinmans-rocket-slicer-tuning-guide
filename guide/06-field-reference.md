# Rocket field reference

Find the label on your screen, then match its scope and feature context. Repeated labels such as Printing speed or Flow multiplier affect different regions; the internal ID distinguishes them, not a universal shared value.

This working edition indexes 470 template/editor schema fields in Rocket 1.4.0.705. It does not yet claim every runtime dialog/action is covered. 184 renderer controls and 3 additional dialog declarations require exact label/path checks. Missing explanations: 0; unresolved option explanations: 0.

Schema bounds are input constraints, not safe hardware limits. A missing bound/default means unknown, not unrestricted. Mode-dependent variants are listed together; check your actual screen and resolved output. Functional explanations describe the control's purpose, not proof of a safe or successful print.

## Action Mask Rule

### Mask type - maskType

**Scope:** action-mask-rule.

**What does it mean?** Chooses what a modifier or mask region is intended to affect. A mask is an auxiliary region, not automatically a printable part.

**When would I change it?** When deliberately restricting support or applying a documented regional modifier, not during a basic material comparison.

**What changes if I adjust it?** Changing the class can change which toolpaths are permitted in the region. It does not simply change the colour of the region.

**Check together with:** Mask placement and intersections; Support generation and regional settings.

**Selectable choices:**

- **Support blocker:** A region intended to prevent support generation where it intersects. It does not make an unsupported overhang printable without support. Schema contexts: action-mask-rule.
- **Support enforcer:** A region intended to request support. Other support eligibility and geometry rules may still matter; verify the preview rather than assuming support appears everywhere. Schema contexts: action-mask-rule.
- **Internal mask:** Selects the internal-mask class. The precise roles and boundary treatment affected are unresolved in this survey; do not assume it cuts a cavity or changes a tool. Schema contexts: action-mask-rule.
- **Full mask:** Selects the full-mask class. Its exact difference from internal mask is not verified; do not assume it removes the model or applies every setting throughout it. Schema contexts: action-mask-rule.

**Caution:** Internal-mask versus full-mask coverage is not established by these labels; inspect the resulting preview. The option names below are source labels, not a live visibility guarantee.

**Evidence status:** Schema-backed selector; partly interpreted; mask-class details unverified.. Control ID: `action-mask-rule:maskType`.

### name - name

**Scope:** action-mask-rule.

**What does it mean?** Identifies this mask rule so a person can distinguish its purpose from other modifiers.

**When would I change it?** When naming or revising a rule, using a description such as the region and intended support action.

**What changes if I adjust it?** A clearer name improves traceability; the name alone is not evidence that the mask has the intended geometry or settings.

**Check together with:** Mask type; Saved project identity.

**Caution:** The editor control type was not resolved. Do not infer an automatic operation from a descriptive name.

**Evidence status:** Metadata interpretation; control type unresolved.. Control ID: `action-mask-rule:name`.

## Composite Settings

### Build plate temperature - bedTemperature

**Scope:** CFC composite material / Temperature.

**What does it mean?** The requested build-plate temperature for normal composite printing, in degrees Celsius.

**When would I change it?** During a controlled adhesion or thermal-management comparison for the approved matrix/fibre pair and actual plate.

**What changes if I adjust it?** Higher can improve adhesion but increase bottom deformation and heat exposure; lower may reduce those effects but allow lifting.

**Check together with:** First-layers bed temperature; Plate preparation and chamber condition.

**Displayed units:** °C.

**Caution:** A temperature field is not a plate or material rating. Do not use bed heat to compensate for a loose plate or leaking hotend.

**Evidence status:** Functional interpretation; physical result unvalidated.. Control ID: `composite-settings:bedTemperature`.

### Build plate temp. on first layers - bedTemperatureOnFLs

**Scope:** CFC composite material / Temperature.

**What does it mean?** The build-plate temperature requested during the initial-layer stage of the composite material.

**When would I change it?** Only after first-layer geometry and plate preparation are correct, when comparing initial adhesion.

**What changes if I adjust it?** More initial heat may help attachment but can enlarge or soften bottom features. Less may reduce flare but weaken attachment.

**Check together with:** Normal bed temperature; Initial-layer stage and nozzle-to-plate relationship.

**Displayed units:** °C.

**Caution:** The exact transition trigger must be checked in output; do not assume this follows the fan-height or nozzle-temperature-height field identically.

**Evidence status:** Label-based thermal interpretation; transition details unverified.. Control ID: `composite-settings:bedTemperatureOnFLs`.

### Chamber temperature - chamberTemperature

**Scope:** CFC composite material / Temperature.

**What does it mean?** The requested chamber temperature for the composite material, where the machine supports active chamber heating.

**When would I change it?** When qualifying the approved material pair's enclosure conditions, within current machine and material guidance.

**What changes if I adjust it?** A warmer environment can reduce thermal contraction but may worsen small details, feed-path heat exposure or cooling balance.

**Check together with:** Heated-chamber capability and index; Exhaust and part cooling.

**Displayed units:** °C.

**Caution:** Entering a target does not prove a chamber heater exists, its sensor is correct or the target was reached. Never change hardware capability flags to force heating.

**Evidence status:** Functional interpretation; hardware operation not tested.. Control ID: `composite-settings:chamberTemperature`.

### Color - color

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** The colour assigned to the composite material's on-screen representation.

**When would I change it?** To make the selected material identifiable and keep the visual record consistent with the intended spool.

**What changes if I adjust it?** Changes the representation; it does not dye the part, load a fibre or prove which physical spool is installed.

**Check together with:** Material name; Preview and physical spool record.

**Caution:** Colour additives can affect real tuning, but changing this swatch does not retune temperature or flow.

**Evidence status:** Presentation interpretation; no physical qualification.. Control ID: `composite-settings:color`.

### Fiber cost per spool ({symbol}) - costPerSpool

**Scope:** CFC composite material / OTHER.

**What does it mean?** Purchase cost for one continuous-fibre spool, in the application's selected currency.

**When would I change it?** When recording a different price or spool product for cost reporting.

**What changes if I adjust it?** Can change estimated material cost. A higher entered price is not stronger or faster fibre.

**Check together with:** Fibre spool length; Estimated fibre consumption.

**Caution:** The currency placeholder in the source label is dynamic. Cost metadata is not proof of loaded material or route eligibility.

**Evidence status:** Accounting interpretation; exact costing formula unverified.. Control ID: `composite-settings:costPerSpool`.

### Description - description

**Scope:** CFC composite material / OTHER.

**What does it mean?** Free-form notes about this composite-material definition.

**When would I change it?** To record pair compatibility, conditioning, test status, limitations and evidence references.

**What changes if I adjust it?** Improves the human record; notes do not enforce the settings they describe.

**Check together with:** Material revision; External tuning and loading record.

**Caution:** Do not place credentials, private identifiers or unsupported TUNED claims in exported notes.

**Evidence status:** Schema-backed notes field; not an enforcement mechanism.. Control ID: `composite-settings:description`.

### Enable preheat - enablePreheat

**Scope:** CFC composite material / Temperature.

**What does it mean?** Enables the composite material's separate nozzle-preheat behaviour.

**When would I change it?** Only when the supported OEM preparation sequence calls for a separate preheat stage.

**What changes if I adjust it?** Enabling may request the configured preheat temperature before printing; disabling does not itself prove the nozzle stays cold.

**Check together with:** Extruder preheat temperature; Printer preparation and standby routines.

**Caution:** Do not disable preparation requirements to bypass a loading problem. Actual timing and waits must be checked in the supported workflow.

**Evidence status:** Label-based switch interpretation; lifecycle timing unverified.. Control ID: `composite-settings:enablePreheat`.

### Enable print cooling - enablePrintCooling

**Scope:** CFC composite material / Cooling.

**What does it mean?** Allows the composite material's print-cooling schedule to control its assigned part-cooling fan.

**When would I change it?** During a documented cooling comparison, not to silence an unidentified fan.

**What changes if I adjust it?** Enabling allows the configured initial and regular cooling requests; disabling does not prove every machine fan stops.

**Check together with:** First-layers and regular fan speeds; Composite tool fan mapping.

**Caution:** This is not authority to stop a protective hotend heatsink fan. Confirm the physical fan role before changing it.

**Evidence status:** Functional interpretation; fan routing requires hardware verification.. Control ID: `composite-settings:enablePrintCooling`.

### Extra unretract length - extraLengthP

**Scope:** CFC composite material / Retraction.

**What does it mean?** Additional matrix-plastic feed associated with unretraction, beyond restoring the ordinary retracted amount.

**When would I change it?** Only after supported composite retraction is understood and repeated restarts show a genuine matrix shortage.

**What changes if I adjust it?** More can fill a lean restart but create a blob or excess pressure; less can reduce buildup but leave a gap.

**Check together with:** Matrix retract length; Unretract speed and temperature.

**Displayed units:** mm.

**Caution:** This is matrix plastic, not continuous-fibre length or a repair for leakage. Exact restart application must be checked in output.

**Evidence status:** Label-based material interpretation; restart algorithm unverified.. Control ID: `composite-settings:extraLengthP`.

### Extra unretract on tool change - extraLengthPOnToolChange

**Scope:** CFC composite material / Retraction.

**What does it mean?** Additional matrix-plastic feed associated specifically with recovery after a tool change.

**When would I change it?** When a verified tool-change test, rather than ordinary travel, shows a repeatable matrix restart deficit.

**What changes if I adjust it?** Increasing can improve an underfed return but add a blob; decreasing can reduce over-priming while risking starvation.

**Check together with:** Tool-change retract length; Standby temperature and before/after tool-change code.

**Displayed units:** mm.

**Caution:** Do not copy an ordinary plastic value here or use this to alter the continuous-fibre loading cycle.

**Evidence status:** Functional interpretation; complete tool lifecycle unvalidated.. Control ID: `composite-settings:extraLengthPOnToolChange`.

### Plastic flow multiplier - extrusionMultiplierP

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** Scales the matrix-plastic amount commanded for the composite material; it is separate from continuous-fibre feed.

**When would I change it?** For a supported, controlled matrix-flow comparison with the approved pair and loading state held fixed.

**What changes if I adjust it?** Higher requests more matrix and may improve coverage or cause buildup; lower requests less and can leave a poorly wetted or underfilled route.

**Check together with:** Plastic filament diameter; Fibre route geometry, temperature and speed.

**Caution:** A multiplier is not a safe pressure limit or proof that empty-fibre operation is supported. Do not infer a fibre percentage from it.

**Evidence status:** Functional interpretation; actual composite deposition unvalidated.. Control ID: `composite-settings:extrusionMultiplierP`.

### Fiber extrusion speed - extrusionSpeedF

**Scope:** CFC composite material / RESTART.

**What does it mean?** Fibre-feed speed in the composite material's restart settings, measured as strand length per second.

**When would I change it?** Only under a supported composite restart procedure after the physical path and loading state are proven.

**What changes if I adjust it?** A faster feed changes the restart's delivery rate; it is not necessarily the speed of every reinforced model route.

**Check together with:** Fibre restart length; Restart lift, pause and matrix delivery.

**Displayed units:** mm/s.

**Caution:** Do not treat this as ordinary plastic print speed. Excessive strand feeding can buckle, tangle or misplace fibre; exact scheduling is unverified.

**Evidence status:** Restart-context interpretation; exact execution unverified.. Control ID: `composite-settings:extrusionSpeedF`.

### Unretract speed - extrusionSpeedP

**Scope:** CFC composite material / Retraction.

**What does it mean?** The speed used to restore retracted matrix plastic, not the toolhead's model-printing speed.

**When would I change it?** After distance is stable, if supported matrix restart tests show a speed-related gap or surge.

**What changes if I adjust it?** Faster restoration can recover pressure sooner but demand more from the feed system; slower may reduce the surge but delay recovery.

**Check together with:** Matrix retract length and extra unretract; Nozzle temperature and tool-change preparation.

**Displayed units:** mm/s.

**Caution:** Do not copy ordinary FFF unretract settings to this path without an approved composite comparison.

**Evidence status:** Label-based retraction interpretation; physical response unvalidated.. Control ID: `composite-settings:extrusionSpeedP`.

### Fiber diameter - fiberDiameter

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** The stated diameter of the continuous-fibre strand, not the composite nozzle diameter.

**When would I change it?** When accurately defining a different supported fibre product using its specification or reliable measurement.

**What changes if I adjust it?** May affect material calculations or compatibility assumptions. It does not physically resize the guide or nozzle.

**Check together with:** Fibre product and linear density; Composite hardware and route definition.

**Displayed units:** mm.

**Caution:** Do not falsify the diameter to change feed or force an unsupported strand through the system; exact downstream use is unverified.

**Evidence status:** Material-definition interpretation; downstream calculation unverified.. Control ID: `composite-settings:fiberDiameter`.

### Manufacturer of fiber - fiberManufacturer

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** Identifies who supplies the continuous fibre in this pair.

**When would I change it?** When creating the record for the actual fibre product or correcting inaccurate identification.

**What changes if I adjust it?** Distinguishes supply sources; changing the text alone does not change the actual strand or qualify compatibility.

**Check together with:** Fibre name and type; Lot and loading record.

**Caution:** Control type is unresolved. A matching manufacturer name is not proof of equivalent sizing, treatment or performance.

**Evidence status:** Metadata interpretation; control type unresolved.. Control ID: `composite-settings:fiberManufacturer`.

### Fiber name - fiberName

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** The product name identifying the continuous-fibre component.

**When would I change it?** To match the real spool and retain a distinct record when the product changes.

**What changes if I adjust it?** Improves identification but does not load fibre, change the cut cycle or transfer another product's tune.

**Check together with:** Manufacturer and fibre type; Compatible matrix and physical spool.

**Caution:** The form type is unresolved. Do not assume renaming creates a newly compatible material.

**Evidence status:** Metadata interpretation; control type unresolved.. Control ID: `composite-settings:fiberName`.

### Fiber length per spool - fiberSpoolLength

**Scope:** CFC composite material / OTHER.

**What does it mean?** The total continuous-fibre length per spool, with the schema expressing this quantity in kilometres.

**When would I change it?** For a different supported spool size or accurate inventory and cost estimates.

**What changes if I adjust it?** Can change reported available quantity or cost per length. It is not the commanded amount for one route.

**Check together with:** Fibre spool cost; Linear density and consumption estimate.

**Displayed units:** km.

**Caution:** Do not enter metres as kilometres. A remaining-length estimate is not a physical loading or runout check.

**Evidence status:** Inventory interpretation; exact accounting behaviour unverified.. Control ID: `composite-settings:fiberSpoolLength`.

### Fiber type - fiberType

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** Describes the kind of continuous reinforcement used in the pair.

**When would I change it?** Only to identify the actual approved fibre family/product, not to obtain another route by relabelling it.

**What changes if I adjust it?** May participate in material categorisation; the exact dispatch or compatibility effect is not established by the label.

**Check together with:** Fibre product, diameter and matrix pairing; Composite hardware compatibility.

**Caution:** Control type and available choices are unresolved. Do not substitute chopped-fibre plastic for a continuous-fibre type.

**Evidence status:** Metadata/function boundary unresolved; no compatibility qualification.. Control ID: `composite-settings:fiberType`.

### Finish ironing distance - finishIroningDistance

**Scope:** CFC composite material / RESTART.

**What does it mean?** A distance in the composite restart/finish settings associated with ironing or pressing a route end.

**When would I change it?** Only during an OEM-supported composite end/restart investigation with the route and loading state fixed.

**What changes if I adjust it?** A longer distance can extend end treatment; a shorter one can leave less treatment. Exact path, timing and feed behaviour are not established here.

**Check together with:** Cut distance and route tail; Restart lift, pause and material temperature.

**Displayed units:** mm.

**Caution:** This is not ordinary top-surface ironing. Do not use it to hide a failed cut or mechanically loose hotend.

**Evidence status:** Label/context interpretation; exact finishing algorithm unresolved.. Control ID: `composite-settings:finishIroningDistance`.

### First layers fan speed height - firstLayersFanHeight

**Scope:** CFC composite material / Cooling.

**What does it mean?** The height in millimetres over which the composite initial-layer fan setting is intended to apply.

**When would I change it?** When isolating early-layer cooling after adhesion and the supported composite baseline are reliable.

**What changes if I adjust it?** A greater height keeps the initial cooling condition over more of the part; it does not mean that many numbered layers.

**Check together with:** Initial fan speed; Layer height and regular fan speed.

**Displayed units:** mm.

**Caution:** Check the transition in output; rounding to layers and boundary inclusion are not verified. Do not confuse this with initial nozzle-temperature height.

**Evidence status:** Height-based interpretation; boundary details unverified.. Control ID: `composite-settings:firstLayersFanHeight`.

### First layers fan speed - firstLayersFanSpeed

**Scope:** CFC composite material / Cooling.

**What does it mean?** The requested part-cooling percentage during the composite initial cooling stage.

**When would I change it?** For an early-layer adhesion/curl comparison while preserving the correct fan mapping.

**What changes if I adjust it?** More cooling can sharpen edges but weaken attachment or bonding; less retains heat but may permit curling or soft features.

**Check together with:** Initial fan height; Plate, chamber and regular cooling.

**Displayed units:** %.

**Caution:** A percentage is not measured airflow. This must not be confused with a hotend-protection fan.

**Evidence status:** Functional interpretation; airflow and physical result unvalidated.. Control ID: `composite-settings:firstLayersFanSpeed`.

### First layers temp. height - firstLayersHeight

**Scope:** CFC composite material / Temperature.

**What does it mean?** The height in millimetres associated with using the composite initial-layer nozzle temperature.

**When would I change it?** When comparing how long the initial thermal condition should persist after a reliable first layer.

**What changes if I adjust it?** Increasing extends that condition in height; decreasing switches toward normal printing temperature sooner.

**Check together with:** Initial and normal nozzle temperatures; Layer height and heat history.

**Displayed units:** mm.

**Caution:** This is a height, not a layer count. Verify the actual temperature transition and do not infer a separate bed/fan transition from it.

**Evidence status:** Label-based thermal-stage interpretation; boundary details unverified.. Control ID: `composite-settings:firstLayersHeight`.

### Linear density - linearDensity

**Scope:** CFC composite material / OTHER.

**What does it mean?** Fibre mass per length, expressed in tex: grams per 1,000 metres of strand.

**When would I change it?** When defining a supported fibre product from its actual specification.

**What changes if I adjust it?** Changes the relationship between fibre length and estimated mass; it is not ordinary plastic density or a feed-speed percentage.

**Check together with:** Fibre length and mass estimates; Fibre product and cost reporting.

**Displayed units:** tex = g/km.

**Caution:** Do not enter grams per metre or plastic density in this field. Its exact use outside accounting remains unverified.

**Evidence status:** Unit-defined material interpretation; downstream use unverified.. Control ID: `composite-settings:linearDensity`.

### Name - name

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** The human-readable identity of the combined composite-material definition.

**When would I change it?** When creating a separately scoped candidate or recording a revision for the real matrix/fibre pair.

**What changes if I adjust it?** Helps select the intended pair; the label alone does not change physical loading or enforce tool compatibility.

**Check together with:** Matrix and fibre product identities; Saved profile associations and revision record.

**Caution:** Control type and accepted name characters are unresolved here. Do not mark an unvalidated pair TUNED.

**Evidence status:** Metadata interpretation; control type unresolved.. Control ID: `composite-settings:name`.

### Plastic cost per spool ({symbol}) - plasticCostPerSpool

**Scope:** CFC composite material / OTHER.

**What does it mean?** The purchase cost of the matrix-plastic spool, separate from the continuous-fibre spool.

**When would I change it?** When the matrix price or supplied spool changes.

**What changes if I adjust it?** May change job-cost estimates without changing the amount of material printed.

**Check together with:** Matrix spool weight; Matrix consumption and fibre cost.

**Caution:** The currency is a dynamic application choice. Do not treat total composite cost as a strength or coverage measure.

**Evidence status:** Accounting interpretation; exact cost formula unverified.. Control ID: `composite-settings:plasticCostPerSpool`.

### Plastic density - plasticDensity

**Scope:** CFC composite material / OTHER.

**What does it mean?** The density recorded for the matrix plastic, distinct from fibre linear density.

**When would I change it?** For an accurately identified supported matrix product using its specification and the displayed units.

**What changes if I adjust it?** Can affect mass/consumption calculations. A denser value does not by itself mean more commanded matrix flow.

**Check together with:** Matrix material and consumption estimate; Plastic diameter and cost reporting.

**Caution:** This form's unit was not resolved; verify it before entering a number. Do not adjust density as an extrusion-multiplier shortcut.

**Evidence status:** Material/accounting interpretation; unit and exact downstream effect unresolved.. Control ID: `composite-settings:plasticDensity`.

### Plastic filament diameter - plasticDiameter

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** The diameter of the incoming matrix-plastic filament, not the output nozzle or reinforcement strand.

**When would I change it?** When defining the actual supported filament or correcting a proven diameter-entry error.

**What changes if I adjust it?** Diameter can affect conversion between requested plastic volume and feed length. A larger entered diameter generally implies less length for the same volume; confirm actual implementation.

**Check together with:** Matrix flow multiplier; Physical feed path and material identity.

**Displayed units:** mm.

**Caution:** Do not alter this to compensate for a clog or tune flow by falsifying material dimensions.

**Evidence status:** Functional material interpretation; exact feed conversion unverified.. Control ID: `composite-settings:plasticDiameter`.

### Manufacturer of plastic - plasticManufacturer

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** Identifies the manufacturer of the matrix plastic used with the continuous fibre.

**When would I change it?** When documenting the actual product source or creating a distinct material candidate.

**What changes if I adjust it?** Improves traceability; it does not establish equivalent behaviour between brands.

**Check together with:** Matrix name/type; Approved fibre pairing and lot record.

**Caution:** Control type is unresolved. A matching base polymer is not proof of an approved matrix/fibre combination.

**Evidence status:** Metadata interpretation; control type unresolved.. Control ID: `composite-settings:plasticManufacturer`.

### Plastic name - plasticName

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** The product name of the matrix-plastic component, separate from the pair name and fibre name.

**When would I change it?** To match the loaded matrix spool and distinguish formulation or colour variants.

**What changes if I adjust it?** Changes identification; a name change alone does not retune temperature or feed.

**Check together with:** Matrix manufacturer/type; Composite pair and loading record.

**Caution:** The form type is unresolved. Check the real spool instead of trusting a familiar label.

**Evidence status:** Metadata interpretation; control type unresolved.. Control ID: `composite-settings:plasticName`.

### Plastic spool weight - plasticSpoolWeight

**Scope:** CFC composite material / OTHER.

**What does it mean?** The matrix-plastic spool quantity recorded in grams for material accounting.

**When would I change it?** When documenting a different supplied spool amount using Rocket's intended net/gross convention.

**What changes if I adjust it?** Can change cost or capacity estimates; it does not set the amount extruded on one route.

**Check together with:** Matrix spool cost and density; Estimated consumption.

**Displayed units:** g.

**Caution:** Whether the application expects net filament mass or another spool convention is not established. Verify rather than including packaging weight by guess.

**Evidence status:** Accounting interpretation; net/gross convention unresolved.. Control ID: `composite-settings:plasticSpoolWeight`.

### Plastic type - plasticType

**Scope:** CFC composite material / BasicInformation.

**What does it mean?** Classifies the matrix plastic by material family.

**When would I change it?** Only to accurately identify the supported loaded product, not to unlock another preset by relabelling it.

**What changes if I adjust it?** May influence categorisation or matching, but it does not prove the product's temperature, adhesion or fibre compatibility.

**Check together with:** Matrix product and fibre pair; Temperature and conditioning requirements.

**Caution:** Control type/choices and any automatic preset dispatch are unresolved. PCTG, PETG and nylon are not interchangeable because some properties are similar.

**Evidence status:** Metadata/dispatch interpretation; exact selection behaviour unresolved.. Control ID: `composite-settings:plasticType`.

### Priming line height - primingLineHeight

**Scope:** CFC composite material / OTHER.

**What does it mean?** The height associated with the composite priming line used during preparation.

**When would I change it?** Only in a supported preparation calibration, after the physical tool/plate relationship is known.

**What changes if I adjust it?** A changed height alters how the preparation line is deposited or contacts the surface. The exact relationship to nozzle Z is not established here.

**Check together with:** Tool Z calibration; Priming geometry and material loading.

**Displayed units:** mm.

**Caution:** This is not a global first-layer correction. An incorrect preparation height can scrape or produce an unattached prime.

**Evidence status:** Preparation-height interpretation; exact motion semantics unverified.. Control ID: `composite-settings:primingLineHeight`.

### Regular fan speed - regularFanSpeed

**Scope:** CFC composite material / Cooling.

**What does it mean?** The ordinary part-cooling percentage requested after the composite initial cooling stage.

**When would I change it?** For a controlled comparison of route shape and matrix/fibre bonding under representative chamber conditions.

**What changes if I adjust it?** More cooling can improve shape but weaken bonding; less can improve heat retention while increasing softness or curl.

**Check together with:** Initial cooling schedule; Assigned fan, temperature and route speed.

**Displayed units:** %.

**Caution:** Other feature or machine commands may override this request. It is not a measured airflow or hotend-heatsink setting.

**Evidence status:** Functional interpretation; effective fan lifecycle unvalidated.. Control ID: `composite-settings:regularFanSpeed`.

### Retract length on tool change - retractionLengthOnToolChange

**Scope:** CFC composite material / Retraction.

**What does it mean?** The matrix-plastic withdrawal distance associated with changing away from its tool.

**When would I change it?** Only when an approved tool-change comparison isolates ooze or restart problems in this matrix path.

**What changes if I adjust it?** More withdrawal may reduce ooze but delay recovery or disturb feeding; less may leave pressure and dripping.

**Check together with:** Tool-change extra unretract; Standby temperature and tool-change code.

**Displayed units:** mm.

**Caution:** This is not ordinary travel retraction, fibre withdrawal or a full unload. Do not substitute another tool's values.

**Evidence status:** Functional interpretation; composite lifecycle unvalidated.. Control ID: `composite-settings:retractionLengthOnToolChange`.

### Retract length - retractionLengthOnTravel

**Scope:** CFC composite material / Retraction.

**What does it mean?** The matrix-plastic withdrawal distance associated with eligible non-printing travel.

**When would I change it?** Only through a supported composite test after moisture, temperature and physical feeding are stable.

**What changes if I adjust it?** More may relieve pressure but worsen restart gaps or feed disturbance; less may reduce those disturbances while increasing ooze.

**Check together with:** Retract and unretract speeds; Extra matrix feed and route transitions.

**Displayed units:** mm.

**Caution:** Do not use ordinary FFF retraction assumptions for continuous-fibre preparation or cutting. Exact eligibility requires output review.

**Evidence status:** Functional interpretation; applicability and execution unverified.. Control ID: `composite-settings:retractionLengthOnTravel`.

### Retract speed - retractionSpeed

**Scope:** CFC composite material / Retraction.

**What does it mean?** The speed of matrix-plastic withdrawal during supported retraction events.

**When would I change it?** Only after a validated distance, when a supported experiment isolates withdrawal timing.

**What changes if I adjust it?** Faster can relieve pressure sooner but increase feed demands; slower may be gentler but allow more ooze time.

**Check together with:** Matrix retract distance; Unretract speed and hardware feed limits.

**Displayed units:** mm/s.

**Caution:** A UI value is not a motor or pressure rating. This does not set continuous-fibre speed.

**Evidence status:** Functional interpretation; hardware limits not established.. Control ID: `composite-settings:retractionSpeed`.

### Extruder temp. on first layers - temperatureOnFLs

**Scope:** CFC composite material / Temperature.

**What does it mean?** The composite nozzle temperature requested during the initial printed height stage.

**When would I change it?** For a controlled initial deposition/adhesion comparison within both product and machine limits.

**What changes if I adjust it?** Hotter can improve matrix wetting but increase ooze or degradation; cooler may sharpen features but weaken bonding or restrict flow.

**Check together with:** First-layers temperature height; Normal print temperature and loaded pair.

**Displayed units:** °C.

**Caution:** Do not copy an ordinary nozzle's accepted temperature as a composite acceptance result.

**Evidence status:** Functional interpretation; physical pair unvalidated.. Control ID: `composite-settings:temperatureOnFLs`.

### Extruder preheat temperature - temperaturePreheat

**Scope:** CFC composite material / Temperature.

**What does it mean?** The composite nozzle target associated with the enabled preheat stage.

**When would I change it?** Only to follow the approved pair's supported preparation procedure.

**What changes if I adjust it?** A higher target adds preparation heat and may increase ooze; a lower target may reduce readiness or make feeding resistant.

**Check together with:** Enable preheat; Loading sequence, standby and printing temperatures.

**Displayed units:** °C.

**Caution:** Do not feed a composite path before the OEM sequence permits it. A preheat target is not the steady deposition temperature.

**Evidence status:** Thermal-stage interpretation; actual sequencing unverified.. Control ID: `composite-settings:temperaturePreheat`.

### Extruder temperature - temperaturePrint

**Scope:** CFC composite material / Temperature.

**What does it mean?** The requested composite-nozzle temperature during normal deposition of the selected matrix/fibre pair.

**When would I change it?** During a controlled supported pair test, with flow, geometry and cooling fixed.

**What changes if I adjust it?** Hotter generally lowers matrix viscosity but can increase ooze/degradation; cooler can reduce ooze while worsening wetting or backpressure.

**Check together with:** Matrix product, route speed and flow; Initial/standby targets and chamber conditions.

**Displayed units:** °C.

**Caution:** The field does not certify a safe pressure or a dry/empty-fibre operation. Observe the supported loading and temperature limits.

**Evidence status:** Functional interpretation; physical tune not established.. Control ID: `composite-settings:temperaturePrint`.

### Extruder standby temperature - temperatureWait

**Scope:** CFC composite material / Temperature.

**What does it mean?** The standby nozzle target while the composite tool waits rather than normally depositing.

**When would I change it?** During a verified tool-change/idle comparison using the approved pair and OEM sequence.

**What changes if I adjust it?** Lower standby heat may reduce ooze but lengthen recovery or make material resistant; higher may improve readiness but prolong heat exposure.

**Check together with:** Tool-change timing; Preheat/print targets and loaded fibre.

**Displayed units:** °C.

**Caution:** Standby is not a universal unloading temperature or permission to leave a stationary fibre in a hot tool indefinitely.

**Evidence status:** Functional interpretation; idle lifecycle unvalidated.. Control ID: `composite-settings:temperatureWait`.

### Version - version

**Scope:** CFC composite material / OTHER.

**What does it mean?** A version value attached to this composite-material definition.

**When would I change it?** Only according to the supported preset-management/versioning convention.

**What changes if I adjust it?** May affect record comparison or migration; increasing it is not a material-quality improvement.

**Check together with:** Preset saving/import; Parent and application version compatibility.

**Caution:** The exact version semantics are unresolved. Do not use this alone as proof of a tuned revision or rename the application's version.

**Evidence status:** Version metadata interpretation; migration rules unresolved.. Control ID: `composite-settings:version`.

### Z-lift on restart - zHopF

**Scope:** CFC composite material / RESTART.

**What does it mean?** The Z lift associated with the composite fibre restart, expressed in millimetres.

**When would I change it?** Only in an OEM-supported restart/contact investigation with known tool offsets and route geometry.

**What changes if I adjust it?** A larger lift changes clearance and the subsequent restart approach; a smaller lift reduces that clearance. Exact motion ordering is not established.

**Check together with:** Restart pause and fibre feed; Tool Z offsets and preparation contact.

**Displayed units:** mm.

**Caution:** This is not ordinary plastic travel Z-hop. An incorrect change can alter fibre placement or cause contact/collision.

**Evidence status:** Restart-motion interpretation; exact sequence unverified.. Control ID: `composite-settings:zHopF`.

### Restart pause - zHopFPauseAdhesion

**Scope:** CFC composite material / RESTART.

**What does it mean?** A pause, in seconds, associated with composite restart adhesion.

**When would I change it?** Only while qualifying a supported restart sequence and a specific matrix/fibre pair.

**What changes if I adjust it?** More pause changes contact/heat dwell and print time; less reduces dwell but may weaken restart attachment. The exact paused motion phase is unverified.

**Check together with:** Restart lift and strand feed; Temperature, matrix delivery and contact geometry.

**Displayed units:** s.

**Caution:** Do not extend dwell to hide a damaged or leaking nozzle. This is not a general minimum-layer-time cooling control.

**Evidence status:** Label/context interpretation; exact dwell location unverified.. Control ID: `composite-settings:zHopFPauseAdhesion`.

## Extruder C Settings

### Cut G-code - cutCode

**Scope:** extruder-c-settings.

**What does it mean?** Executable G-code used for the composite cutter operation, not an explanatory note.

**When would I change it?** Only for a documented OEM hardware/firmware change with the entire cut/restart sequence reviewed.

**What changes if I adjust it?** Different commands can move actuators, change tool state or feed material; a typo can invalidate a route or cause hardware contact.

**Check together with:** Cutter hardware and cut distance; Fibre restart and firmware macros.

**Caution:** Preserve the OEM code. Never paste a generic servo/cutter command or old-unit code here to tune a filament symptom.

**Evidence status:** Hardware executable hook; not validated for modification.. Control ID: `extruder-c-settings:cutCode`.

### Cut distance - cutDistance

**Scope:** extruder-c-settings.

**What does it mean?** A composite-tool distance parameter associated with the cut and remaining route tail.

**When would I change it?** Only after the actual cutter/feed geometry is measured through the supported hardware calibration procedure.

**What changes if I adjust it?** Changes can alter where cutting occurs relative to the route finish and how much strand remains. Exact sign and reference points are unverified here.

**Check together with:** Cut G-code; Fibre restart length and route-end treatment.

**Displayed units:** mm.

**Caution:** Do not assume this is blade travel or borrow a historical cut-distance number as a new-machine value.

**Evidence status:** Hardware-geometry interpretation; exact reference unresolved.. Control ID: `extruder-c-settings:cutDistance`.

### Cooling fan index - fanIndex

**Scope:** extruder-c-settings.

**What does it mean?** Identifies which firmware fan channel is associated with the composite tool's cooling.

**When would I change it?** Only to match verified OEM wiring or a documented supported hardware change.

**What changes if I adjust it?** Changing the index can route the same percentage request to a different physical fan, not simply increase its speed.

**Check together with:** Has cooling fan; Firmware fan map and composite material cooling.

**Caution:** A wrong index may drive the wrong device or disable required cooling. Confirm actual channel mapping; do not guess from another printer.

**Evidence status:** Hardware mapping; must be independently verified.. Control ID: `extruder-c-settings:fanIndex`.

### Fiber restart length - fiberRestartLength

**Scope:** extruder-c-settings.

**What does it mean?** A hardware restart length for feeding continuous fibre back into the composite operation.

**When would I change it?** Only through the supported fibre-path/cutter calibration for the actual installed assembly.

**What changes if I adjust it?** Too much can overfeed or buckle strand; too little can leave a restart short of the intended location.

**Check together with:** Cut distance; Restart feed speed, lift and pause.

**Displayed units:** mm.

**Caution:** Not an ordinary FFF retract/unretract length or a nozzle-diameter adjustment. Exact restart references must be established before editing.

**Evidence status:** Hardware restart interpretation; exact sequence unverified.. Control ID: `extruder-c-settings:fiberRestartLength`.

### Has cooling fan - hasFan

**Scope:** extruder-c-settings.

**What does it mean?** Declares that the composite tool has an assigned controllable cooling fan.

**When would I change it?** Only to match verified OEM tool hardware, not when comparing fan percentages.

**What changes if I adjust it?** The declaration can enable or suppress cooling output for that tool; it does not physically add a fan.

**Check together with:** Cooling fan index; Composite material cooling schedule.

**Caution:** Do not disable a hardware capability to hide a failed fan. Protective heatsink cooling must remain as specified by the manufacturer.

**Evidence status:** Hardware capability declaration; runtime effect unvalidated.. Control ID: `extruder-c-settings:hasFan`.

### Heat-up speed - heatupSpeed

**Scope:** extruder-c-settings.

**What does it mean?** The composite tool's declared heating rate in degrees Celsius per second.

**When would I change it?** Only when an OEM-supported hardware/timing calibration establishes the actual rate.

**What changes if I adjust it?** May affect heating-time prediction or scheduling. Entering a larger rate does not make the heater more powerful or prove faster heating is safe.

**Check together with:** Preheat/standby scheduling; Heater, sensor and firmware control.

**Displayed units:** °C/s.

**Caution:** Exact scheduling use is unverified. Do not alter this to conceal thermal faults or replace firmware temperature-control calibration.

**Evidence status:** Hardware timing parameter; exact algorithm unresolved.. Control ID: `extruder-c-settings:heatupSpeed`.

### Name - name

**Scope:** extruder-c-settings.

**What does it mean?** The descriptive name for a composite-tool definition.

**When would I change it?** Only when managing a clearly identified hardware definition or its documented revision.

**What changes if I adjust it?** Improves human selection; renaming does not change the physical tool, firmware number or loading path.

**Check together with:** Printer tool associations; Offsets, fan and cutter definition.

**Caution:** Control type is unresolved. A T0 or 0.7 label alone cannot qualify routing or installed nozzle identity.

**Evidence status:** Hardware metadata interpretation; control type unresolved.. Control ID: `extruder-c-settings:name`.

### X offset - offsetX

**Scope:** extruder-c-settings.

**What does it mean?** The composite tool's X positional offset relative to the machine/tool reference.

**When would I change it?** Only during supported tool-alignment calibration for this physical machine.

**What changes if I adjust it?** Changes where this tool's output aligns relative to other tools; it is not whole-part shrinkage compensation.

**Check together with:** Other tool offsets; Firmware coordinate transforms and physical alignment.

**Displayed units:** mm.

**Caution:** Positive/negative application convention is not established here. A wrong offset can misregister material or cause a collision; preserve the OEM baseline.

**Evidence status:** Hardware coordinate parameter; direction convention unverified.. Control ID: `extruder-c-settings:offsetX`.

### Y offset - offsetY

**Scope:** extruder-c-settings.

**What does it mean?** The composite tool's Y positional offset from its defined machine/tool reference.

**When would I change it?** Only when a supported physical tool-alignment procedure demonstrates a Y mismatch.

**What changes if I adjust it?** Moves the tool's registration relative to other paths, not just a printed hole's diameter.

**Check together with:** X/Z offsets; Firmware transform and tool-change positioning.

**Displayed units:** mm.

**Caution:** Do not guess the sign or copy the retained machine's value. Verify the reference frame before any resulting motion.

**Evidence status:** Hardware coordinate parameter; direction convention unverified.. Control ID: `extruder-c-settings:offsetY`.

### Z offset - offsetZ

**Scope:** extruder-c-settings.

**What does it mean?** The composite tool's vertical relationship to the machine/tool reference.

**When would I change it?** Only during supported tool-height/contact calibration after mechanical inspection.

**What changes if I adjust it?** Changes vertical registration/contact. An incorrect value can press the tool into the plate or leave deposition unattached.

**Check together with:** Probe/contact calibration; First-layer geometry and composite restart contact.

**Displayed units:** mm.

**Caution:** This is not a filament-flow adjustment. Sign and reference must be verified; do not repair a nozzle leak or bed defect by changing Z offset.

**Evidence status:** Hardware coordinate parameter; not qualified for casual editing.. Control ID: `extruder-c-settings:offsetZ`.

## Extruder P Settings

### Cooling fan index - fanIndex

**Scope:** extruder-p-settings.

**What does it mean?** The firmware fan channel associated with the ordinary plastic tool's cooling.

**When would I change it?** Only to match independently verified OEM wiring or a supported tool change.

**What changes if I adjust it?** Selects a device channel; it is not a percentage or a fan power limit.

**Check together with:** Has cooling fan; Plastic material fan schedule and firmware mapping.

**Caution:** A wrong channel can command another fan or leave the intended fan off. Do not derive the index from the composite tool's name.

**Evidence status:** Hardware mapping; independent verification required.. Control ID: `extruder-p-settings:fanIndex`.

### Has cooling fan - hasFan

**Scope:** extruder-p-settings.

**What does it mean?** Declares that the ordinary plastic tool has a controllable cooling fan.

**When would I change it?** Only when accurately defining supported installed hardware.

**What changes if I adjust it?** May govern whether material cooling commands are generated; toggling it does not repair or install a fan.

**Check together with:** Fan index; Enable print cooling and material schedule.

**Caution:** Do not use this declaration to bypass a cooling fault or disable protective hotend cooling.

**Evidence status:** Hardware capability declaration; actual output unvalidated.. Control ID: `extruder-p-settings:hasFan`.

### Heat-up speed - heatupSpeed

**Scope:** extruder-p-settings.

**What does it mean?** The ordinary plastic tool's declared heating rate in degrees Celsius per second.

**When would I change it?** Only following supported hardware timing/calibration evidence, not for each spool.

**What changes if I adjust it?** May change heating predictions or scheduling; a larger declared number does not change heater wattage or guarantee thermal readiness.

**Check together with:** Preheat and standby targets; Heater/sensor condition and firmware waits.

**Displayed units:** °C/s.

**Caution:** Do not falsify this to get past a thermal delay or fault. Exact use by the scheduler is not verified.

**Evidence status:** Hardware timing interpretation; exact algorithm unresolved.. Control ID: `extruder-p-settings:heatupSpeed`.

### Name - name

**Scope:** extruder-p-settings.

**What does it mean?** The human-readable name of the ordinary plastic-tool definition.

**When would I change it?** When maintaining a clearly scoped supported hardware definition or revision.

**What changes if I adjust it?** Helps identification; a renamed definition does not prove which physical hotend will execute the job.

**Check together with:** Printer tool associations; Nozzle diameter and offsets.

**Caution:** Control type is unresolved. Tool labels and firmware identifiers must still be matched to hardware.

**Evidence status:** Hardware metadata interpretation; control type unresolved.. Control ID: `extruder-p-settings:name`.

### Nozzle diameter - nozzleDiameter

**Scope:** extruder-p-settings.

**What does it mean?** The declared outlet diameter of the installed ordinary plastic nozzle, in millimetres.

**When would I change it?** After physically verifying a supported nozzle replacement or correcting a demonstrated wrong definition.

**What changes if I adjust it?** Can affect allowed/planned line geometry. Changing the number cannot make the installed opening larger or qualify an abrasive material.

**Check together with:** Layer height and line widths; Flow, physical nozzle wear and compatible profiles.

**Displayed units:** mm.

**Caution:** Never tune this as an extrusion multiplier. A wrong diameter invalidates downstream tests; keep separate nozzle-specific records.

**Evidence status:** Physical hardware declaration; installed size must be verified.. Control ID: `extruder-p-settings:nozzleDiameter`.

### X offset - offsetX

**Scope:** extruder-p-settings.

**What does it mean?** The ordinary plastic tool's X alignment offset from the defined tool/machine reference.

**When would I change it?** Only through supported physical tool-alignment calibration.

**What changes if I adjust it?** Changes registration of this tool relative to other tools, not material shrinkage or model scale.

**Check together with:** Composite tool alignment; Firmware/tool-change coordinate handling.

**Displayed units:** mm.

**Caution:** The sign convention is not established by the label. Incorrect offsets can misplace material or collide with machine fixtures.

**Evidence status:** Hardware coordinate parameter; direction convention unverified.. Control ID: `extruder-p-settings:offsetX`.

### Y offset - offsetY

**Scope:** extruder-p-settings.

**What does it mean?** The ordinary plastic tool's Y alignment offset relative to its reference.

**When would I change it?** When a supported tool-alignment measurement establishes an actual Y offset error.

**What changes if I adjust it?** Changes where that tool registers in Y relative to other deposition and preparation operations.

**Check together with:** X/Z offsets; Firmware coordinate transforms and tool preparation.

**Displayed units:** mm.

**Caution:** Do not copy the other machine's value or guess the correction sign from a photograph.

**Evidence status:** Hardware coordinate parameter; exact transform unverified.. Control ID: `extruder-p-settings:offsetY`.

### Z offset - offsetZ

**Scope:** extruder-p-settings.

**What does it mean?** The ordinary plastic nozzle's vertical alignment relative to the selected machine/tool reference.

**When would I change it?** Only during supported tool-height/probing calibration after checking physical hardware and plate seating.

**What changes if I adjust it?** An incorrect change can cause scraping or poor attachment even if the material multiplier is correct.

**Check together with:** Probe and bed calibration; First-layer height and physical plate.

**Displayed units:** mm.

**Caution:** Not a universal first-layer-flow fix. Verify the sign/reference and use the OEM calibration method, not trial nozzle contact.

**Evidence status:** Hardware coordinate parameter; not qualified for casual editing.. Control ID: `extruder-p-settings:offsetZ`.

## Plastic Settings

### Build plate temperature - bedTemperature

**Scope:** Plastic material / Temperature.

**What does it mean?** The normal printing target for the build plate, in degrees Celsius.

**When would I change it?** During a controlled adhesion/thermal comparison after plate preparation and first-layer geometry are reliable.

**What changes if I adjust it?** Higher can improve attachment but soften or enlarge the bottom; lower can reduce those effects but increase lifting.

**Check together with:** Initial bed target; Plate coating, adhesive and chamber condition.

**Displayed units:** °C.

**Caution:** Stay within both plate and material guidance. More bed heat is not a repair for contamination or a loose plate.

**Evidence status:** Functional interpretation; physical outcome unvalidated.. Control ID: `plastic-settings:bedTemperature`.

### Build plate temp. on first layers - bedTemperatureOnFLs

**Scope:** Plastic material / Temperature.

**What does it mean?** The build-plate target during the initial-layer stage, separate from the normal bed target.

**When would I change it?** For initial adhesion comparisons with the same plate, cleaning and nozzle-to-plate relationship.

**What changes if I adjust it?** More initial heat can improve wetting but increase bottom flare; less may sharpen the bottom while reducing attachment.

**Check together with:** Normal bed target; Initial nozzle temperature and first-layer geometry.

**Displayed units:** °C.

**Caution:** The exact stage transition must be confirmed; do not assume this uses the same trigger as every other first-layers field.

**Evidence status:** Thermal-stage interpretation; transition details unverified.. Control ID: `plastic-settings:bedTemperatureOnFLs`.

### Chamber temperature - chamberTemperature

**Scope:** Plastic material / Temperature.

**What does it mean?** The requested chamber temperature for this plastic where active chamber heating is supported.

**When would I change it?** When qualifying the material's enclosure conditions under current product and printer guidance.

**What changes if I adjust it?** Warmer conditions may reduce contraction and splitting but can worsen heat creep or small details; cooler can do the reverse.

**Check together with:** Heated-chamber capability; Exhaust, part cooling and ambient conditions.

**Displayed units:** °C.

**Caution:** A number in the profile does not prove the heater/sensor works or that the chamber reached it. Do not change hardware flags to force it.

**Evidence status:** Functional interpretation; actual chamber operation unvalidated.. Control ID: `plastic-settings:chamberTemperature`.

### Coast length - coastAtEndLength

**Scope:** Plastic material / Retraction.

**What does it mean?** A length at the end of a plastic path associated with coasting: using remaining pressure instead of continuing ordinary feed.

**When would I change it?** Only after baseline extrusion is stable and repeated line ends show a specific pressure-related buildup.

**What changes if I adjust it?** More coasting can reduce an end blob but leave a thin or open finish; less can restore the finish while leaving excess pressure.

**Check together with:** Flow multiplier and effective pressure behaviour; Wipe, retraction and seam placement.

**Displayed units:** mm.

**Caution:** It is not a substitute for supported PA calibration. The exact path-length convention and eligible features remain unverified.

**Evidence status:** Label-based coasting interpretation; exact planning unverified.. Control ID: `plastic-settings:coastAtEndLength`.

### Color - color

**Scope:** Plastic material / BasicInformation.

**What does it mean?** The colour used to represent this material in the application.

**When would I change it?** To identify the intended spool visually and distinguish material candidates.

**What changes if I adjust it?** Changes a swatch/representation, not physical filament colour, loading or tuning.

**Check together with:** Material name; Preview and spool identification.

**Caution:** Real colour variants can need different tuning. A changed swatch is not validation of a different formulation.

**Evidence status:** Presentation interpretation; not physical evidence.. Control ID: `plastic-settings:color`.

### Spool cost ({symbol}) - costPerSpool

**Scope:** Plastic material / OTHER.

**What does it mean?** Purchase price for the plastic spool in the selected currency.

**When would I change it?** When recording a different price or supplied spool product.

**What changes if I adjust it?** Can change estimated job cost without changing the printed toolpath or material's quality.

**Check together with:** Spool weight; Density and consumption estimate.

**Caution:** The currency placeholder is dynamic. Cost is not a feed-rate, temperature or material-compatibility setting.

**Evidence status:** Accounting interpretation; exact cost calculation unverified.. Control ID: `plastic-settings:costPerSpool`.

### Density - density

**Scope:** Plastic material / OTHER.

**What does it mean?** The material's mass per volume, expressed by this schema in grams per cubic centimetre.

**When would I change it?** To accurately define the product from manufacturer data or a reliable material measurement.

**What changes if I adjust it?** Changes the relationship between estimated volume and mass; increasing density is not the same as increasing commanded flow.

**Check together with:** Consumption and cost estimates; Product formulation and filler content.

**Displayed units:** g/cm³.

**Caution:** Do not alter density to disguise an extrusion fault. Exact uses beyond material accounting are not established here.

**Evidence status:** Unit-backed material interpretation; downstream use unverified.. Control ID: `plastic-settings:density`.

### Description - description

**Scope:** Plastic material / OTHER.

**What does it mean?** Notes associated with this plastic-material definition.

**When would I change it?** To record conditioning, physical scope, test status, limitations and evidence references.

**What changes if I adjust it?** Makes a candidate understandable to another operator, but does not enforce the values or instructions written in it.

**Check together with:** Material revision and name; External experiment record.

**Caution:** Keep credentials and private identifiers out of exported notes. A written TUNED claim needs actual supporting tests.

**Evidence status:** Schema-backed notes field; not an enforcement mechanism.. Control ID: `plastic-settings:description`.

### Enable preheat - enablePreheat

**Scope:** Plastic material / Temperature.

**What does it mean?** Enables the material's separately configured nozzle preheat behaviour.

**When would I change it?** Only when the supported workflow needs that preparation stage or a documented comparison addresses it.

**What changes if I adjust it?** May request the preheat target before normal printing. Disabled does not mean firmware preparation or other heating commands disappear.

**Check together with:** Preheat temperature; Printer start code and standby scheduling.

**Caution:** Do not use the switch to bypass supported preparation or heat-safety checks. Exact waits and timing are unverified.

**Evidence status:** Switch interpretation; lifecycle details unverified.. Control ID: `plastic-settings:enablePreheat`.

### Enable print cooling - enablePrintCooling

**Scope:** Plastic material / Cooling.

**What does it mean?** Allows the material's part-cooling schedule to operate its assigned fan.

**When would I change it?** For a controlled cooling comparison after establishing the correct fan and material baseline.

**What changes if I adjust it?** Allows initial/regular/maximum cooling requests where applicable. Disabling does not prove every physical fan will stop.

**Check together with:** Initial, regular and maximum fan speeds; Physical fan mapping and feature overrides.

**Caution:** Do not stop hotend-protection cooling. Verify effective fan commands instead of equating this switch with all fan behaviour.

**Evidence status:** Functional interpretation; complete fan lifecycle unvalidated.. Control ID: `plastic-settings:enablePrintCooling`.

### Extra unretract length - extraLengthP

**Scope:** Plastic material / Retraction.

**What does it mean?** Extra plastic feed added around unretraction beyond restoring the amount withdrawn.

**When would I change it?** Only when an isolated restart test shows a genuine shortage after moisture, temperature and retraction are stable.

**What changes if I adjust it?** More can fill a lean start but add a blob; less can reduce excess at starts while risking a gap.

**Check together with:** Retract length; Unretract speed, coasting and pressure recovery.

**Displayed units:** mm.

**Caution:** Do not raise this to compensate for a blocked feed path. Confirm the exact restart application in output.

**Evidence status:** Label-based restart interpretation; exact application unverified.. Control ID: `plastic-settings:extraLengthP`.

### Extra unretract on tool change - extraLengthPOnToolChange

**Scope:** Plastic material / Retraction.

**What does it mean?** Additional plastic feed specifically associated with returning after a tool change.

**When would I change it?** When a tool-change test shows a repeatable return deficit that does not occur on ordinary travel.

**What changes if I adjust it?** More can restore a lean return but create a blob; less can reduce over-prime while leaving the next path underfed.

**Check together with:** Tool-change retract length; Standby temperature and change-tool code.

**Displayed units:** mm.

**Caution:** Ordinary travel and tool-change recovery are separate events. Do not copy this value into composite fibre restart settings.

**Evidence status:** Functional interpretation; full tool lifecycle unvalidated.. Control ID: `plastic-settings:extraLengthPOnToolChange`.

### Flow multiplier - extrusionMultiplierP

**Scope:** Plastic material / BasicInformation.

**What does it mean?** Scales the amount of ordinary plastic Rocket requests. This is a dimensionless material multiplier, not speed or pressure advance.

**When would I change it?** During a supported top-surface flow comparison below the usable melt limit, after temperature is stable.

**What changes if I adjust it?** Higher deposits more material and can close channels or cause ridges; lower deposits less and can remove ridges or create gaps.

**Check together with:** Filament diameter and line geometry; Speed, melt capacity and feature-specific flow.

**Caution:** Do not tune it from first-layer appearance alone or use it as whole-part dimensional compensation. Verify the saved ratio, not a borrowed tile label.

**Evidence status:** Functional interpretation; physical calibration unperformed.. Control ID: `plastic-settings:extrusionMultiplierP`.

### Unretract speed - extrusionSpeedP

**Scope:** Plastic material / Retraction.

**What does it mean?** Unretract speed: how fast the feeder restores withdrawn plastic, not normal model-printing speed.

**When would I change it?** After retract distance is established, when isolating a pressure-recovery timing problem.

**What changes if I adjust it?** Faster can restore pressure sooner but increase feed demand; slower may reduce surges while delaying the next clean line.

**Check together with:** Retract length and extra unretract; Temperature and feeder limits.

**Displayed units:** mm/s.

**Caution:** Do not set this from travel speed or the hotend's volumetric limit alone; standalone feed behaviour differs from coordinated deposition.

**Evidence status:** Functional interpretation; actual feed response unvalidated.. Control ID: `plastic-settings:extrusionSpeedP`.

### Filament diameter - filamentDiameter

**Scope:** Plastic material / BasicInformation.

**What does it mean?** The incoming plastic filament's diameter, not the nozzle opening.

**When would I change it?** For an accurately defined supported filament or a confirmed entry error, using representative measurements where appropriate.

**What changes if I adjust it?** Diameter affects the relationship between requested volume and feed length; a larger declared diameter generally needs less length for the same volume.

**Check together with:** Flow multiplier; Physical filament and material-volume calculations.

**Displayed units:** mm.

**Caution:** Do not falsify diameter as a flow-tuning shortcut. A changed nominal field does not make another filament size fit the extruder.

**Evidence status:** Functional material interpretation; exact conversion unverified.. Control ID: `plastic-settings:filamentDiameter`.

### First layers fan speed height - firstLayersFanHeight

**Scope:** Plastic material / Cooling.

**What does it mean?** The initial cooling-stage height in millimetres, not a numbered layer count.

**When would I change it?** When comparing how long early-layer cooling should persist after a reliable adhesion baseline.

**What changes if I adjust it?** A greater height extends the initial fan condition; a smaller height moves to later cooling earlier.

**Check together with:** Initial fan speed; Layer height, regular cooling and adhesion.

**Displayed units:** mm.

**Caution:** Check actual boundary behaviour in output. This setting does not establish the nozzle- or bed-temperature transition by itself.

**Evidence status:** Height-stage interpretation; boundary rounding unverified.. Control ID: `plastic-settings:firstLayersFanHeight`.

### First layers fan speed - firstLayersFanSpeed

**Scope:** Plastic material / Cooling.

**What does it mean?** Part-cooling percentage requested during the material's initial cooling-height stage.

**When would I change it?** For a one-variable early-layer attachment/curl comparison using the same plate preparation.

**What changes if I adjust it?** More can cool edges and sharpen detail but weaken adhesion; less keeps the initial region hotter and may soften features.

**Check together with:** Initial cooling height; Bed, chamber and normal fan settings.

**Displayed units:** %.

**Caution:** This percentage is not measured airflow and is not the protective heatsink fan setting.

**Evidence status:** Functional interpretation; physical cooling unvalidated.. Control ID: `plastic-settings:firstLayersFanSpeed`.

### First layers temp. height - firstLayersHeight

**Scope:** Plastic material / Temperature.

**What does it mean?** The printed height over which the material's initial nozzle temperature applies.

**When would I change it?** When isolating the duration of the initial thermal condition after first-layer geometry is correct.

**What changes if I adjust it?** Increasing extends the initial target in height; decreasing moves toward the regular printing target sooner.

**Check together with:** Initial and regular nozzle temperatures; Layer height and heat history.

**Displayed units:** mm.

**Caution:** Units are millimetres, not layers. Do not assume importing a tower or changing this field creates a multi-temperature sweep.

**Evidence status:** Thermal-stage interpretation; transition implementation unverified.. Control ID: `plastic-settings:firstLayersHeight`.

### Layer time for max fan speed - layerTimeForMaxCooling

**Scope:** Plastic material / Cooling.

**What does it mean?** A layer-duration threshold in seconds associated with using the maximum fan setting on short layers.

**When would I change it?** When a controlled small-feature test shows insufficient cooling or unnecessary fan variation.

**What changes if I adjust it?** A larger threshold can make more layers qualify as short; a smaller one can reserve maximum cooling for shorter layers. Exact interpolation is unverified.

**Check together with:** Regular and maximum fan speeds; Actual layer duration and cooling enable.

**Displayed units:** s.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Do not assume this slows the print to that duration. It is labelled as a fan threshold, not proof of a minimum-layer-time speed control.

**Evidence status:** Label-based cooling-threshold interpretation; exact curve unverified.. Control ID: `plastic-settings:layerTimeForMaxCooling`.

### Manufacturer - manufacturer

**Scope:** Plastic material / BasicInformation.

**What does it mean?** The supplier/manufacturer identity of the plastic material.

**When would I change it?** To accurately identify the actual product and distinguish another manufacturer's candidate.

**What changes if I adjust it?** Supports traceability; a brand label alone does not set or validate temperature, flow or compatibility.

**Check together with:** Material name/type; Colour, formulation and lot record.

**Caution:** The editor control type is unresolved. Do not treat two products with the same polymer name as equivalent tunes.

**Evidence status:** Metadata interpretation; control type unresolved.. Control ID: `plastic-settings:manufacturer`.

### Maximum fan speed - maximumFanSpeed

**Scope:** Plastic material / Cooling.

**What does it mean?** The maximum part-cooling percentage used by the material's normal cooling logic, particularly on short layers.

**When would I change it?** When testing small-feature cooling while checking layer bonding and warp resistance.

**What changes if I adjust it?** Higher can improve tiny features but overcool bonding or cause warping; lower may improve bonding while leaving soft or curled detail.

**Check together with:** Regular fan and layer-time threshold; Initial cooling and feature overrides.

**Displayed units:** %.

**Caution:** Do not assume this caps every bridge, machine or manually emitted fan request. Review the actual cooling sequence.

**Evidence status:** Cooling interpretation; global fan-cap semantics unverified.. Control ID: `plastic-settings:maximumFanSpeed`.

### Name - name

**Scope:** Plastic material / BasicInformation.

**What does it mean?** The human-readable identity of this ordinary plastic-material definition.

**When would I change it?** When creating a scoped candidate or revised material record for the real machine/nozzle/product.

**What changes if I adjust it?** Makes the intended choice distinguishable; it does not enforce compatibility or move a spool into the printer.

**Check together with:** Saved profile associations; Material revision and physical spool record.

**Caution:** Accepted name characters/control type are unresolved. A typed TUNED label is not evidence of completed validation.

**Evidence status:** Metadata interpretation; control type unresolved.. Control ID: `plastic-settings:name`.

### Plastic type - plasticType

**Scope:** Plastic material / BasicInformation.

**What does it mean?** The material-family classification of the ordinary plastic.

**When would I change it?** Only to identify the real supported product or correct its classification.

**What changes if I adjust it?** May participate in selection/category matching; it does not independently establish the physical material's safe settings.

**Check together with:** Manufacturer/product identity; Compatible hardware and material guidance.

**Caution:** Control type/options and exact matching behaviour are unresolved. Relabelling a material does not make it compatible.

**Evidence status:** Metadata/selection interpretation; exact dispatch unresolved.. Control ID: `plastic-settings:plasticType`.

### Regular fan speed - regularFanSpeed

**Scope:** Plastic material / Cooling.

**What does it mean?** The ordinary part-cooling percentage used outside the initial cooling stage and special cooling conditions.

**When would I change it?** During a fixed-temperature cooling comparison on representative walls and features.

**What changes if I adjust it?** More can improve deposited shape but reduce bonding or promote warp; less keeps heat and can improve bonding while softening detail.

**Check together with:** Maximum fan and short-layer threshold; Initial stage and special-feature cooling.

**Displayed units:** %.

**Caution:** Normal fan is not proof of bridge fan or every executed fan command. Confirm the correct physical fan and output.

**Evidence status:** Functional interpretation; effective schedule unvalidated.. Control ID: `plastic-settings:regularFanSpeed`.

### Retract min travel inside part - retractMinimumTravelNoCrossing

**Scope:** Plastic material / Retraction.

**What does it mean?** The travel-length threshold associated with retraction when the travel stays inside the part rather than crossing its boundary.

**When would I change it?** When a controlled toolpath review identifies unnecessary short internal retractions or ooze during longer internal travels.

**What changes if I adjust it?** Higher generally leaves more short internal moves unretracted; lower can add retractions and restart events.

**Check together with:** Travel routing; Retract distance and crossing-part threshold.

**Displayed units:** mm.

**Caution:** This is a trigger distance, not the amount of filament pulled back. Exact boundary classification must be checked in output.

**Evidence status:** Label-based travel-trigger interpretation; exact classifier unverified.. Control ID: `plastic-settings:retractMinimumTravelNoCrossing`.

### Retract min travel cross part - retractMinimumTravelOnCrossing

**Scope:** Plastic material / Retraction.

**What does it mean?** The travel-length threshold for retraction when the path crosses the part boundary/open space.

**When would I change it?** When realistic crossing travels show strings or repeated restarts from excessive triggering.

**What changes if I adjust it?** Lower can retract on more short crossings; higher can reduce events but leave more unretracted ooze time.

**Check together with:** Retraction length and speed; Travel path and inside-part threshold.

**Displayed units:** mm.

**Caution:** Do not confuse the threshold with withdrawal length. A travel that looks nearby can follow a different actual route.

**Evidence status:** Travel-trigger interpretation; exact eligibility unverified.. Control ID: `plastic-settings:retractMinimumTravelOnCrossing`.

### Retract length on tool change - retractionLengthOnToolChange

**Scope:** Plastic material / Retraction.

**What does it mean?** Plastic withdrawal distance used around changing away from this tool.

**When would I change it?** Only for a supported tool-change comparison, after ordinary travel behaviour is separately established.

**What changes if I adjust it?** More can reduce idle ooze but increase recovery demand or feed problems; less may ease recovery but allow dripping.

**Check together with:** Tool-change extra unretract; Standby temperature and tool-change scripts.

**Displayed units:** mm.

**Caution:** Not a full filament-unload distance or an ordinary travel default. Do not copy it to a continuous-fibre path.

**Evidence status:** Functional interpretation; complete change-tool behaviour unvalidated.. Control ID: `plastic-settings:retractionLengthOnToolChange`.

### Retract length - retractionLengthOnTravel

**Scope:** Plastic material / Retraction.

**What does it mean?** The plastic length withdrawn for an eligible ordinary non-printing move.

**When would I change it?** After drying/temperature are stable, to compare supported distances while holding retract speed fixed.

**What changes if I adjust it?** More can reduce strings but cause lean restarts or feed/clog problems; less reduces those demands but may leave thicker strings.

**Check together with:** Travel trigger thresholds; Retract/unretract speeds, extra feed and temperature.

**Displayed units:** mm.

**Caution:** Choose the shortest repeatably useful distance within hardware guidance. Retraction cannot repair moisture, a leaking joint or a partial blockage.

**Evidence status:** Functional interpretation; physical tune unperformed.. Control ID: `plastic-settings:retractionLengthOnTravel`.

### Retract speed - retractionSpeed

**Scope:** Plastic material / Retraction.

**What does it mean?** How fast plastic is withdrawn during ordinary retraction, in millimetres of filament per second.

**When would I change it?** After distance is stable, when an isolated test addresses withdrawal timing or feeder response.

**What changes if I adjust it?** Faster can relieve pressure sooner but demand more grip/acceleration; slower can be gentler while leaving more ooze time.

**Check together with:** Retract distance; Unretract speed and hardware feeder capability.

**Displayed units:** mm/s.

**Caution:** A permitted UI number is not proof that the motor, filament or hotend can safely follow it.

**Evidence status:** Functional interpretation; hardware response unvalidated.. Control ID: `plastic-settings:retractionSpeed`.

### Spool weight - spoolWeight

**Scope:** Plastic material / OTHER.

**What does it mean?** The spool's material quantity recorded in grams for estimates.

**When would I change it?** When accurately defining a different supplied spool size, using the application's intended mass convention.

**What changes if I adjust it?** Can affect cost/capacity reporting, not normal line width or requested print speed.

**Check together with:** Spool cost; Density and consumption estimate.

**Displayed units:** g.

**Caution:** Net filament versus total spool convention is unresolved here. Do not assume entered capacity proves enough physical filament remains.

**Evidence status:** Accounting interpretation; mass convention unresolved.. Control ID: `plastic-settings:spoolWeight`.

### Extruder temp. on first layers - temperatureOnFLs

**Scope:** Plastic material / Temperature.

**What does it mean?** The nozzle target during the material's initial printed-height stage.

**When would I change it?** For a controlled first-layer wetting/adhesion comparison after nozzle height and plate preparation are correct.

**What changes if I adjust it?** Higher can improve wetting but add ooze or bottom distortion; lower may sharpen detail but weaken attachment or flow.

**Check together with:** Initial temperature height; Normal nozzle and initial bed targets.

**Displayed units:** °C.

**Caution:** Keep within the real material/machine limits. A hotter first layer does not fix a nozzle scraping the plate.

**Evidence status:** Functional interpretation; physical initial layer unvalidated.. Control ID: `plastic-settings:temperatureOnFLs`.

### Extruder preheat temperature - temperaturePreheat

**Scope:** Plastic material / Temperature.

**What does it mean?** The nozzle temperature requested for the enabled preheat stage.

**When would I change it?** Only to match the supported preparation requirements of the actual material and machine.

**What changes if I adjust it?** A higher target can improve readiness but increase ooze and heat exposure; a lower one can reduce ooze while delaying readiness.

**Check together with:** Enable preheat; Print/standby targets and preparation code.

**Displayed units:** °C.

**Caution:** It is not automatically the printing temperature or a safe manual load temperature. Confirm supported waits before feeding.

**Evidence status:** Thermal-stage interpretation; exact sequence unverified.. Control ID: `plastic-settings:temperaturePreheat`.

### Extruder temperature - temperaturePrint

**Scope:** Plastic material / Temperature.

**What does it mean?** The normal nozzle temperature requested for this plastic during deposition.

**When would I change it?** During fixed-setting temperature coupons with geometry, flow and cooling held constant.

**What changes if I adjust it?** Higher generally improves melting/adhesion at flow but may increase strings, softness or degradation; lower may sharpen detail while restricting melting/bonding.

**Check together with:** Printed speed and flow multiplier; Moisture, cooling, nozzle and chamber.

**Displayed units:** °C.

**Caution:** Start within current product and machine guidance. A low-speed attractive sample does not prove high-flow strength.

**Evidence status:** Functional interpretation; material tune unperformed.. Control ID: `plastic-settings:temperaturePrint`.

### Extruder standby temperature - temperatureWait

**Scope:** Plastic material / Temperature.

**What does it mean?** The nozzle standby target while the tool waits instead of normally printing.

**When would I change it?** For a supported idle/tool-change comparison after recording the actual sequence.

**What changes if I adjust it?** Lower can reduce ooze but delay reheating or make recovery resistant; higher keeps readiness but adds thermal dwell and ooze.

**Check together with:** Tool-change timing; Preheat/print targets and preparation scripts.

**Displayed units:** °C.

**Caution:** Do not treat standby as an unloading or maintenance temperature without the manufacturer's procedure.

**Evidence status:** Functional interpretation; idle lifecycle unvalidated.. Control ID: `plastic-settings:temperatureWait`.

### Version - version

**Scope:** Plastic material / OTHER.

**What does it mean?** A version value belonging to this material definition.

**When would I change it?** Only according to the supported preset-management convention when a definition is revised.

**What changes if I adjust it?** May affect comparison/import/migration, not physical material quality or firmware version.

**Check together with:** Material saving and parent references; Application compatibility.

**Caution:** Exact migration semantics are unresolved. Keep a human-readable revision/evidence record rather than treating a larger number as validation.

**Evidence status:** Version metadata interpretation; exact rules unresolved.. Control ID: `plastic-settings:version`.

### Wipe nozzle length - wipeNozzleLength

**Scope:** Plastic material / Retraction.

**What does it mean?** The distance associated with wiping the nozzle along a path near retraction or a road ending.

**When would I change it?** After baseline flow is stable, if an isolated seam/end test identifies excess residual material.

**What changes if I adjust it?** A longer wipe can spread/remove residue but thin the finish or add marks; a shorter one reduces that treatment but may leave a blob.

**Check together with:** Retraction, coast length and seam location; Actual wipe path and pressure behaviour.

**Displayed units:** mm.

**Caution:** This label does not establish use of the machine's physical cleaning station. Exact path/timing must be checked in output.

**Evidence status:** Label-based wiping interpretation; implementation unverified.. Control ID: `plastic-settings:wipeNozzleLength`.

### Z-hop height - zHopP

**Scope:** Plastic material / Retraction.

**What does it mean?** The Z lift used for applicable ordinary plastic travel/retraction moves.

**When would I change it?** Only when a demonstrated clearance problem remains after checking part lift, overextrusion and travel routing.

**What changes if I adjust it?** More can clear raised features but adds Z motion, time and ooze opportunity; less reduces those costs while reducing clearance.

**Check together with:** Retraction eligibility and travel paths; Z motion limits and part condition.

**Displayed units:** mm.

**Caution:** Do not use Z-hop to hide nozzle scraping, failed probing or a lifting part. It is separate from composite restart lift.

**Evidence status:** Functional interpretation; eligibility and physical clearance unvalidated.. Control ID: `plastic-settings:zHopP`.

## Printer Settings

### Additional retract length - additionalRetract

**Scope:** Machine/printer template / FEATURES.

**What does it mean?** A printer-level additional withdrawal distance, separate from the material's ordinary retract length.

**When would I change it?** Only after identifying its exact supported use in this printer's preparation/tool-change lifecycle.

**What changes if I adjust it?** More withdrawal can increase the amount later requiring recovery; less can leave more material/pressure in that stage. The exact triggering stage is unresolved.

**Check together with:** Material retraction and tool-change values; Printer preparation scripts.

**Displayed units:** mm.

**Caution:** Do not add it blindly to cure stringing. Printer-level and material-level withdrawals may combine; inspect complete output first.

**Evidence status:** Label-based hardware interpretation; exact trigger unresolved.. Control ID: `printer-settings:additionalRetract`.

### Blocks buffer size - blocksBufferSize

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** A machine/planner block-buffer setting, apparently related to how many motion blocks are handled ahead of execution.

**When would I change it?** Only under a documented OEM firmware/planner procedure, not ordinary filament tuning.

**What changes if I adjust it?** A different value may change planning assumptions or output pacing. The unit, allocation and actual enforcement are not established by this label.

**Check together with:** Postprocessor and firmware motion planner; Segmented paths and acceleration scheduling.

**Caution:** More is not automatically smoother or safer, and this is not a network upload buffer. Preserve the OEM value until semantics are verified.

**Evidence status:** Machine/planner interpretation; exact behaviour unresolved.. Control ID: `printer-settings:blocksBufferSize`.

### Bottom Middle - bottomIntermediateSolidInfillAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for solid bottom layers other than the outermost bottom skin, according to the role label.

**When would I change it?** Only in a controlled motion comparison after basic material and mechanical behaviour are stable.

**What changes if I adjust it?** Higher can shorten internal bottom-fill motion but increase pressure changes/vibration; lower can smooth motion while adding time.

**Check together with:** Bottom-layer roles and speed; Acceleration enable, regular acceleration and firmware limits.

**Displayed units:** mm/s².

**Caution:** Bottom Middle is a feature role, not necessarily a numbered physical layer or the bed-contact first layer. Verify preview/output targeting.

**Evidence status:** Role-label interpretation; exact targeting unverified.. Control ID: `printer-settings:bottomIntermediateSolidInfillAcceleration`.

### Bottom Most - bottomMostSolidInfillAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for the outermost bottom solid-surface role.

**When would I change it?** When separately validating bottom-surface motion and attachment with first-layer geometry already correct.

**What changes if I adjust it?** Lower can make short bottom paths gentler but slower; higher can reduce time while increasing dynamic feed and attachment demands.

**Check together with:** Bottom-most speed/geometry; First-layer rules, acceleration enable and firmware limits.

**Displayed units:** mm/s².

**Caution:** Do not equate this role with all first-layer motion or use acceleration to hide a nozzle-height error.

**Evidence status:** Role-label interpretation; actual override precedence unverified.. Control ID: `printer-settings:bottomMostSolidInfillAcceleration`.

### Bridge - bridgeSolidInfillAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for bridge solid-infill paths.

**When would I change it?** During a controlled bridge-motion comparison after temperature, anchors and bridge flow are credible.

**What changes if I adjust it?** Higher changes tension and pressure faster at bridge starts/ends; lower can soften those transitions but change time spent over the unsupported span.

**Check together with:** Bridge speed, cooling and flow; Span/anchor geometry and firmware limits.

**Displayed units:** mm/s².

**Caution:** Acceleration is not bridge speed or a strength rating. Verify the bridge role actually receives this request.

**Evidence status:** Functional role interpretation; physical bridge result unvalidated.. Control ID: `printer-settings:bridgeSolidInfillAcceleration`.

### Brim - brimAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request while printing the brim attached around a part's base.

**When would I change it?** For a controlled adhesion/motion comparison with clean plate and correct brim geometry.

**What changes if I adjust it?** Lower can make short adhesion paths gentler; higher may reduce time but challenge attachment and pressure consistency.

**Check together with:** Brim speed, gap and width; First-layer geometry and acceleration enable.

**Displayed units:** mm/s².

**Caution:** A gentler brim cannot fix a dirty plate or a gap that prevents it joining the part.

**Evidence status:** Role interpretation; physical adhesion unvalidated.. Control ID: `printer-settings:brimAcceleration`.

### Plastic Sparse Infill - cellularInfillAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for ordinary plastic sparse-infill paths, not continuous-fibre infill.

**When would I change it?** When balancing internal-fill time against motion stability after the melt envelope is established.

**What changes if I adjust it?** Higher can help short infill segments reach speed but increase vibration/feed transients; lower may improve stability while extending print time.

**Check together with:** Sparse-infill pattern and speed; Material throughput and machine limits.

**Displayed units:** mm/s².

**Caution:** An internal feature is not permission to exceed feeder or machine capability. This does not tune fibre-route acceleration.

**Evidence status:** Functional role interpretation; performance unvalidated.. Control ID: `printer-settings:cellularInfillAcceleration`.

### Chamber heatup speed - chamberHeatupSpeed

**Scope:** Machine/printer template / FEATURES.

**What does it mean?** The declared chamber heating rate in degrees Celsius per second.

**When would I change it?** Only after an OEM-supported measurement/calibration establishes the machine's thermal timing.

**What changes if I adjust it?** May alter heat-up predictions or scheduling. A larger entered rate does not increase heater power or establish a stable soaked chamber.

**Check together with:** Heated-chamber declaration/index; Chamber targets and preparation timing.

**Displayed units:** °C/s.

**Caution:** Not a thermal-protection setting or remedy for a failed sensor. Exact scheduler use is unverified.

**Evidence status:** Hardware timing interpretation; exact implementation unresolved.. Control ID: `printer-settings:chamberHeatupSpeed`.

### Acceleration E - defaultAccelerationE

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** The printer definition's baseline acceleration value for the E material-feed axis.

**When would I change it?** Only to match verified supported feeder/firmware capability through machine calibration.

**What changes if I adjust it?** A higher request can change feed-speed transitions but increase grip/motor demands; lower can slow pressure recovery or alter timing.

**Check together with:** Retraction acceleration; Material retraction, pressure behaviour and firmware axis mapping.

**Displayed units:** mm/s².

**Caution:** Do not assume E is interchangeable with composite V/U/P axes or that this is a hard firmware maximum. Exact command mapping needs review.

**Evidence status:** Machine-axis interpretation; mapping and enforcement unverified.. Control ID: `printer-settings:defaultAccelerationE`.

### Acceleration retract - defaultAccelerationRetract

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** The machine's baseline acceleration request for retraction-related feed motion.

**When would I change it?** Only under a supported feeder/motion calibration after the exact retraction path is known.

**What changes if I adjust it?** Higher can make withdrawals/restorations more abrupt; lower can make them gentler but change their duration and pressure response.

**Check together with:** Retract distance and speeds; Feed-axis acceleration and firmware interpretation.

**Displayed units:** mm/s².

**Caution:** A slicer entry is not a safe mechanical rating. Do not use it to force a stalled or obstructed filament path.

**Evidence status:** Machine-motion interpretation; actual use unvalidated.. Control ID: `printer-settings:defaultAccelerationRetract`.

### Acceleration X - defaultAccelerationX

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** The baseline X-axis acceleration declared in the printer definition.

**When would I change it?** Only after supported machine-motion evidence or an OEM configuration change, not for one spool's flow defect.

**What changes if I adjust it?** Higher can permit more abrupt X speed changes but increase vibration or step loss; lower can reduce those loads while extending motion time.

**Check together with:** Kinematics and feature accelerations; Firmware motion limits and X jerk.

**Displayed units:** mm/s².

**Caution:** The field's emitted/limit role must be verified; it is not proof the printer can sustain the requested acceleration.

**Evidence status:** Machine-axis interpretation; exact firmware role unverified.. Control ID: `printer-settings:defaultAccelerationX`.

### Acceleration Y - defaultAccelerationY

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** The printer definition's baseline Y-axis acceleration.

**When would I change it?** Only during supported mechanical/motion qualification or to match a verified OEM baseline.

**What changes if I adjust it?** Higher can reduce time on short Y-related moves but add dynamic loads; lower can improve stability while slowing those moves.

**Check together with:** Kinematics and feature accelerations; Y jerk and firmware limits.

**Displayed units:** mm/s².

**Caution:** Cartesian axis labels do not identify one CoreXY motor. Do not change this to mask an axis-specific dimensional fault.

**Evidence status:** Machine-axis interpretation; exact enforcement unverified.. Control ID: `printer-settings:defaultAccelerationY`.

### Acceleration Z - defaultAccelerationZ

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** The baseline acceleration value declared for vertical Z motion.

**When would I change it?** Only under supported machine calibration after checking the actual Z mechanism and firmware limits.

**What changes if I adjust it?** Higher can make lifts/layer transitions more abrupt; lower softens them but can add travel time.

**Check together with:** Z travel speed and jerk; Tool-change lifts, bed motion and probing.

**Displayed units:** mm/s².

**Caution:** Do not copy XY acceleration into Z or use this as a nozzle-height correction. Unsupported Z motion can cause collisions or registration loss.

**Evidence status:** Machine-axis interpretation; hardware capability unqualified.. Control ID: `printer-settings:defaultAccelerationZ`.

### Jerk E - defaultJerkE

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** The feed-axis jerk-style baseline expressed by the schema as a speed, not acceleration per second.

**When would I change it?** Only with a verified definition of how this OEM firmware interprets the emitted setting.

**What changes if I adjust it?** Depending on firmware, higher can allow sharper feed transitions and lower can soften them; neither equals pressure advance.

**Check together with:** E acceleration and retraction; Postprocessor and firmware motion algorithm.

**Displayed units:** mm/s.

**Caution:** Classic jerk, junction deviation and square-corner velocity are not interchangeable. Do not assume a composite-axis mapping or portable numeric value.

**Evidence status:** Firmware-dependent parameter; exact semantics unverified.. Control ID: `printer-settings:defaultJerkE`.

### Jerk X - defaultJerkX

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** A baseline X jerk-style motion value, expressed in speed units in this schema.

**When would I change it?** Only after verifying the OEM firmware's cornering model and supported machine procedure.

**What changes if I adjust it?** A larger value can allow more abrupt corner transitions; a smaller value can slow corners and change pressure/time.

**Check together with:** X acceleration; Feature jerk requests and firmware cornering rules.

**Displayed units:** mm/s.

**Caution:** Do not translate this blindly into Klipper square-corner velocity or another firmware's jerk. It is not a material-flow multiplier.

**Evidence status:** Firmware-dependent cornering interpretation; actual mapping unverified.. Control ID: `printer-settings:defaultJerkX`.

### Jerk Y - defaultJerkY

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** The Y baseline jerk-style value in the printer definition.

**When would I change it?** Only through supported motion qualification with the effective firmware interpretation known.

**What changes if I adjust it?** Higher may carry more speed through corners but increase disturbance; lower may soften direction changes while adding time and heat dwell.

**Check together with:** Y acceleration and kinematics; Regular/outer-wall jerk and firmware limits.

**Displayed units:** mm/s.

**Caution:** Speed units do not establish identical meaning across firmware families. Avoid arbitrary axis-by-axis changes to chase surface texture.

**Evidence status:** Firmware-dependent parameter; exact semantics unverified.. Control ID: `printer-settings:defaultJerkY`.

### Jerk Z - defaultJerkZ

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** The Z-axis baseline jerk-style value, shown in speed units.

**When would I change it?** Only under the OEM vertical-motion calibration/definition, not as an ordinary material setting.

**What changes if I adjust it?** May change abruptness of Z transitions depending on firmware; more is not automatically faster or more accurate.

**Check together with:** Z acceleration and travel speed; Layer changes and lifts.

**Displayed units:** mm/s.

**Caution:** Do not borrow XY values or assume this is physical Z clearance. Verify command interpretation before modifying it.

**Evidence status:** Firmware-dependent hardware parameter; exact behaviour unresolved.. Control ID: `printer-settings:defaultJerkZ`.

### Description - description

**Scope:** Machine/printer template / OTHER.

**What does it mean?** Notes describing the printer template and its intended hardware/configuration.

**When would I change it?** To record known hardware, supported versions, evidence and limitations while preserving the factory reference.

**What changes if I adjust it?** Improves traceability but does not apply a hardware change or verify a private connection target.

**Check together with:** Printer revision; Physical-unit record and supported profiles.

**Caution:** Keep private addresses, credentials and serials out of shared exports. A claimed nozzle or safety feature still needs physical evidence.

**Evidence status:** Schema-backed notes field; not an enforcement mechanism.. Control ID: `printer-settings:description`.

### Do unretract before tool change - doUnretractBeforeToolChange

**Scope:** Machine/printer template / FEATURES.

**What does it mean?** Requests unretraction before a tool-change operation rather than leaving the previous retracted state untouched.

**When would I change it?** Only when the exact OEM change-tool sequence and material-state bookkeeping are understood.

**What changes if I adjust it?** Can add a restoration feed before changing tools, affecting ooze and the next stage's expected state.

**Check together with:** Material tool-change retraction; Additional retract and before/after change code.

**Caution:** Do not toggle it as a generic stringing fix. Duplicate or missing recovery can create unexpected feed; composite loading is not ordinary unretraction.

**Evidence status:** Label-based lifecycle interpretation; exact sequencing unverified.. Control ID: `printer-settings:doUnretractBeforeToolChange`.

### End G-code - endGCode

**Scope:** Machine/printer template / GCODE.

**What does it mean?** Executable commands appended for the end-of-job procedure.

**When would I change it?** Only for a documented supported printer workflow change with the entire completion/failure lifecycle reviewed.

**What changes if I adjust it?** Can change parking, heaters, fans, material handling and final machine state; it is not merely a message printed in a file.

**Check together with:** Firmware macros and coordinates; Tool/fibre unloading and shutdown sequence.

**Caution:** Preserve OEM code. An otherwise successful part can end with a dangerous or wrong-tool action; never paste another machine's ending block.

**Evidence status:** Executable hardware hook; modification unqualified.. Control ID: `printer-settings:endGCode`.

### Fiber Infill - fiberInfillAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for continuous-fibre infill routes, distinct from ordinary sparse plastic infill.

**When would I change it?** Only during supported composite motion qualification with a compatible pair and reliable loading/cutting.

**What changes if I adjust it?** Higher can change tension and placement at route transitions; lower can reduce abruptness while altering dwell and time.

**Check together with:** Fibre-route speed and geometry; Matrix feed, bend rules and firmware limits.

**Displayed units:** mm/s².

**Caution:** Do not transfer ordinary plastic infill acceleration or use this to force an ineligible route.

**Evidence status:** Composite role interpretation; physical route behaviour unvalidated.. Control ID: `printer-settings:fiberInfillAcceleration`.

### Prime Line - fiberPreparationAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The Prime Line acceleration associated with composite fibre preparation.

**When would I change it?** Only under an OEM-supported preparation calibration after tool/plate alignment and loading are proven.

**What changes if I adjust it?** Changes the motion transient of preparation, potentially affecting priming attachment and feed timing rather than ordinary model speed.

**Check together with:** Priming-line height and geometry; Restart/loading sequence and machine limits.

**Displayed units:** mm/s².

**Caution:** A preparation failure is not a reason to increase motion force. Exact covered commands/roles must be verified.

**Evidence status:** Preparation-role interpretation; exact targeting unverified.. Control ID: `printer-settings:fiberPreparationAcceleration`.

### Code After Extruder Change - gCodeAfterExtruderChange

**Scope:** Machine/printer template / GCODE.

**What does it mean?** Executable commands inserted after an extruder/tool change.

**When would I change it?** Only when an OEM-supported workflow or verified hardware change requires a reviewed post-change sequence.

**What changes if I adjust it?** May position, heat, prime or change material state after selection; it can override earlier targets or offsets.

**Check together with:** Tool mapping and preparation; Retraction state, temperatures and firmware macros.

**Caution:** Do not use it as an undocumented PA injection or copy commands from another tool. Review every change through final output and physical sequence.

**Evidence status:** Executable lifecycle hook; modification unqualified.. Control ID: `printer-settings:gCodeAfterExtruderChange`.

### Code Before Extruder Change - gCodeBeforeExtruderChange

**Scope:** Machine/printer template / GCODE.

**What does it mean?** Executable commands inserted before a tool-change operation.

**When would I change it?** Only for a supported and reviewed alteration of the printer's actual change-tool lifecycle.

**What changes if I adjust it?** Can alter withdrawal, cooling, positioning or preparation before selection; wrong assumptions can leave the next tool state inconsistent.

**Check together with:** Unretract-before-change setting; Tool-change retraction, offsets and firmware macros.

**Caution:** This is not a comment box. Never paste old-unit or generic cutter/feed commands to solve a cosmetic defect.

**Evidence status:** Executable lifecycle hook; modification unqualified.. Control ID: `printer-settings:gCodeBeforeExtruderChange`.

### Has heated chamber - hasHeatedChamber

**Scope:** Machine/printer template / FEATURES.

**What does it mean?** Declares that the printer definition has a supported active chamber heater.

**When would I change it?** Only to match verified installed OEM hardware/configuration.

**What changes if I adjust it?** May expose or generate chamber-heating behaviour; checking the box does not install a heater or validate its sensor.

**Check together with:** Heated chamber index and heat-up rate; Material chamber targets and firmware.

**Caution:** Never enable this to make a desired target available on unsupported hardware or bypass a thermal fault.

**Evidence status:** Hardware capability declaration; physical validation required.. Control ID: `printer-settings:hasHeatedChamber`.

### Has heated build plate - hasHeatedTable

**Scope:** Machine/printer template / FEATURES.

**What does it mean?** Declares that the machine has a controllable heated build plate.

**When would I change it?** Only to accurately represent the verified installed printer hardware.

**What changes if I adjust it?** Can affect bed-temperature controls/output. The declaration does not prove heating, sensor accuracy or plate compatibility.

**Check together with:** Material bed targets; Bed heat-up rate and firmware preparation.

**Caution:** Do not toggle a hardware declaration to bypass a failed heater or missing target. Retain the OEM definition unless the hardware change is supported.

**Evidence status:** Hardware capability declaration; actual operation unvalidated.. Control ID: `printer-settings:hasHeatedTable`.

### Heated chamber index - heatedChamberIndex

**Scope:** Machine/printer template / FEATURES.

**What does it mean?** Identifies the heater/channel assigned to chamber control in the printer definition.

**When would I change it?** Only when the exact OEM firmware/heater mapping is independently established.

**What changes if I adjust it?** A different index can direct a request to another channel; it does not just adjust chamber temperature.

**Check together with:** Has heated chamber; Firmware heater/sensor mapping and material target.

**Caution:** Do not guess the index or infer it from tool numbering. A wrong channel can heat the wrong device or invalidate protection assumptions.

**Evidence status:** Hardware channel mapping; independent verification required.. Control ID: `printer-settings:heatedChamberIndex`.

### Plastic Outer Wall - inset0Acceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for the ordinary plastic outer wall, the visible boundary of the part.

**When would I change it?** During a controlled surface/motion comparison after extrusion is stable.

**What changes if I adjust it?** Lower can reduce corner echoes and pressure transients but increase time; higher can reach speed sooner while worsening vibration or sharp-feature quality.

**Check together with:** Outer-wall speed and jerk; Effective pressure behaviour and firmware limits.

**Displayed units:** mm/s².

**Caution:** A clean short sample does not qualify the highest value for every part. Do not tune beyond supported mechanical limits.

**Evidence status:** Functional role interpretation; physical limit unqualified.. Control ID: `printer-settings:inset0Acceleration`.

### Outer wall jerk - inset0Jerk

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The outer-wall-specific jerk/cornering request, shown in speed units.

**When would I change it?** Only after the actual firmware interpretation is known, in an isolated wall-transition comparison.

**What changes if I adjust it?** Higher may carry more speed through wall corners but amplify disturbance; lower can soften transitions while changing dwell and pressure.

**Check together with:** Outer-wall acceleration and speed; Regular jerk, jerk enable and firmware cornering.

**Displayed units:** mm/s.

**Caution:** Not pressure advance. A familiar jerk value from another firmware is not portable, and exact override precedence must be checked.

**Evidence status:** Firmware-dependent role parameter; mapping unverified.. Control ID: `printer-settings:inset0Jerk`.

### Fiber Perimeter - insetXFAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for continuous-fibre perimeter routes.

**When would I change it?** Only when supported composite testing isolates perimeter placement/tension after loading and geometry are credible.

**What changes if I adjust it?** Sharper acceleration can change strand tension and matrix delivery; gentler motion adds time and changes heat/contact dwell.

**Check together with:** Fibre perimeter speed and bend geometry; Matrix feed and machine limits.

**Displayed units:** mm/s².

**Caution:** Do not borrow plastic perimeter values or force tight routes by increasing acceleration.

**Evidence status:** Composite role interpretation; physical performance unvalidated.. Control ID: `printer-settings:insetXFAcceleration`.

### Plastic Perimeter - insetXPAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for ordinary plastic perimeter roles other than the separately identified outer wall.

**When would I change it?** When balancing perimeter time and motion quality after flow and outer-wall behaviour are stable.

**What changes if I adjust it?** Higher can reduce time on short perimeters but add vibration and feed transients; lower makes them gentler but slower.

**Check together with:** Perimeter speed and wall order; Outer-wall acceleration and firmware limits.

**Displayed units:** mm/s².

**Caution:** Exact wall-role coverage is not established by the label. Check the preview/output instead of assuming all walls receive one value.

**Evidence status:** Role-label interpretation; targeting/precedence unverified.. Control ID: `printer-settings:insetXPAcceleration`.

### Kinematics type - kinematicsType

**Scope:** Machine/printer template / DEFAULTAXES.

**What does it mean?** Declares the machine's motion arrangement so planning can use the appropriate kinematic assumptions.

**When would I change it?** Only to match verified physical hardware in a supported printer definition, never as a material or speed tweak.

**What changes if I adjust it?** Selecting another type changes a machine assumption; it does not physically convert the mechanism or calibrate belts.

**Check together with:** Axis motion settings; Firmware coordinates, motors and planner.

**Selectable choices:**

- **CoreXY:** A coupled XY arrangement in which both motors contribute to Cartesian X/Y motion. Do not identify one axis label with one motor without the actual belt mapping. Schema contexts: Machine/printer template / DEFAULTAXES.
- **Cartesian:** The Cartesian machine class, conventionally using independently driven coordinate axes. This is a machine classification, not a fallback for an unknown CoreXY profile. Schema contexts: Machine/printer template / DEFAULTAXES.

**Caution:** Preserve the OEM choice. The two available labels are not proof that every printer of either type is supported.

**Evidence status:** Schema-backed machine selector; execution effects not independently qualified.. Control ID: `printer-settings:kinematicsType`.

### Overhang - overhangSolidInfillAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for the overhang solid-infill role.

**When would I change it?** During a controlled unsupported-edge comparison after geometry, cooling and speed are stable.

**What changes if I adjust it?** Gentler motion may help attachment and pressure consistency but increases dwell; faster transitions can reduce time while stressing unsupported deposition.

**Check together with:** Overhang speed and cooling; Support below, line geometry and firmware limits.

**Displayed units:** mm/s².

**Caution:** It does not create support or change the overhang angle. Verify exact role classification before interpreting a result.

**Evidence status:** Role interpretation; physical overhang outcome unvalidated.. Control ID: `printer-settings:overhangSolidInfillAcceleration`.

### Postprocessor type - postprocessorType

**Scope:** Machine/printer template / GCODE.

**What does it mean?** Selects the machine-specific output postprocessor that turns planned paths into the target G-code/workflow dialect.

**When would I change it?** Only when creating or maintaining a supported printer definition with a verified firmware contract.

**What changes if I adjust it?** Can change tool, material-axis, preparation and ending command generation. It is not a cosmetic file-format preference.

**Check together with:** Extrusion mode and tool mapping; Start/end/tool-change code and firmware.

**Selectable choices:**

- **SK3:** The named postprocessor option in this schema. Its label is not a complete command specification; retain the OEM selection and verify the actual machine/version output. Schema contexts: Machine/printer template / GCODE.

**Caution:** Only SK3 is exposed in this inspected list. Do not substitute a different postprocessor or infer ordinary-slicer compatibility from an output extension.

**Evidence status:** Schema-backed output selector; full postprocessor contract not reproduced.. Control ID: `printer-settings:postprocessorType`.

### Regular - regularAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The general acceleration request used where a more specific feature setting does not control the move.

**When would I change it?** During supported motion qualification with a stable material baseline and representative geometry.

**What changes if I adjust it?** Higher can reduce time on short segments but add vibration/feed transients; lower can make motion gentler at a time cost.

**Check together with:** Acceleration enable and per-feature values; Firmware limits and requested speed.

**Displayed units:** mm/s².

**Caution:** Do not assume it overrides every role or raises firmware limits. A highest surviving sample is not automatically the best production setting.

**Evidence status:** General motion interpretation; exact precedence unverified.. Control ID: `printer-settings:regularAcceleration`.

### Regular jerk - regularJerk

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The general jerk/cornering-style request used outside more specific role overrides.

**When would I change it?** Only after verifying the OEM firmware's interpretation and supported motion envelope.

**What changes if I adjust it?** Higher can make transitions more abrupt and faster; lower can slow corners, changing surface appearance, pressure and dwell.

**Check together with:** Jerk enable and outer-wall jerk; Acceleration and firmware cornering model.

**Displayed units:** mm/s.

**Caution:** Do not equate it with pressure advance or copy square-corner/junction values from another firmware. Confirm the last effective writer.

**Evidence status:** Firmware-dependent cornering interpretation; exact behaviour unverified.. Control ID: `printer-settings:regularJerk`.

### Skirt - skirtAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for skirt paths printed around, but normally separate from, the model.

**When would I change it?** When a supported preparation comparison addresses skirt consistency without changing the model's material settings.

**What changes if I adjust it?** Lower can make the first surrounding paths gentler; higher can shorten their time but increase attachment/feed demands.

**Check together with:** Skirt speed and geometry; First-layer preparation and acceleration enable.

**Displayed units:** mm/s².

**Caution:** A skirt is not automatically an attached brim or a valid model-flow coupon. Check what the preview generated.

**Evidence status:** Feature-role interpretation; physical result unvalidated.. Control ID: `printer-settings:skirtAcceleration`.

### Plastic Solid Infill - solidInfillAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for ordinary plastic solid-fill paths not handled by more specific surface roles.

**When would I change it?** During controlled time/quality qualification after material throughput and top/bottom support are stable.

**What changes if I adjust it?** Higher may speed short fill strokes but increase vibration and boundary pressure; lower may improve transitions while increasing time/heat dwell.

**Check together with:** Solid-fill speed and pattern; Top/bottom overrides and firmware limits.

**Displayed units:** mm/s².

**Caution:** Do not use acceleration to hide excessive flow or insufficient support below a top surface. Exact role precedence needs output review.

**Evidence status:** Functional role interpretation; exact targeting unverified.. Control ID: `printer-settings:solidInfillAcceleration`.

### Start G-code - startGCode

**Scope:** Machine/printer template / GCODE.

**What does it mean?** Executable commands used during job startup and preparation.

**When would I change it?** Only for a documented supported printer/firmware workflow change with current hardware and complete output reviewed.

**What changes if I adjust it?** Can home, move, heat, select tools, prime and alter coordinate/material state before the model begins.

**Check together with:** Firmware macros, mesh and offsets; Postprocessor, material targets and loading sequence.

**Caution:** Keep the OEM baseline. Never paste generic PA, extrusion, homing or old-unit commands to tune a material; effects may persist beyond the test.

**Evidence status:** Executable hardware hook; modification unqualified.. Control ID: `printer-settings:startGCode`.

### Support - supportIslandAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for ordinary support structures.

**When would I change it?** When qualifying support stability/removal with the same support geometry and material baseline.

**What changes if I adjust it?** Lower may reduce disturbance of thin supports; higher may reduce time while increasing oscillation and attachment demands.

**Check together with:** Support speed and pattern; Support interface, cooling and firmware limits.

**Displayed units:** mm/s².

**Caution:** This does not select support locations or change interface gap. Do not infer part strength from support surviving.

**Evidence status:** Support-role interpretation; physical support result unvalidated.. Control ID: `printer-settings:supportIslandAcceleration`.

### Interface Support - supportIslandInterfaceAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for the interface region between supports and the supported part.

**When would I change it?** During controlled interface quality/removal tests after support generation is correct.

**What changes if I adjust it?** Gentler transitions may improve interface consistency but extend dwell; faster motion can reduce time while disturbing fine contact paths.

**Check together with:** Interface speed, gap and density; Cooling and supported-surface geometry.

**Displayed units:** mm/s².

**Caution:** It is not the support-interface separation distance or an automatic easy-removal setting.

**Evidence status:** Interface-role interpretation; physical outcome unvalidated.. Control ID: `printer-settings:supportIslandInterfaceAcceleration`.

### Build plate heat-up speed - tableHeatupSpeed

**Scope:** Machine/printer template / FEATURES.

**What does it mean?** The declared build-plate heating rate in degrees Celsius per second.

**When would I change it?** Only when a supported hardware/timing calibration measures the real plate's response.

**What changes if I adjust it?** May alter heat scheduling or time prediction. A larger number does not increase heater power or guarantee a uniformly soaked plate.

**Check together with:** Heated-plate declaration; Material bed targets and start preparation.

**Displayed units:** °C/s.

**Caution:** Do not change it to bypass a heater delay/fault. It is not a bed-temperature target or firmware PID calibration.

**Evidence status:** Hardware timing interpretation; scheduler details unverified.. Control ID: `printer-settings:tableHeatupSpeed`.

### Top Middle - topIntermediateSolidInfillAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for solid top-region layers below the final exposed top skin.

**When would I change it?** When qualifying top-support fill motion after shell thickness and extrusion are correct.

**What changes if I adjust it?** Higher can reduce time but increase fill-boundary transients; lower may smooth motion while changing layer time and cooling.

**Check together with:** Top-shell roles and solid-fill speed; Final top-skin acceleration and firmware limits.

**Displayed units:** mm/s².

**Caution:** Top Middle is not the final surface itself or a layer count. Verify which paths receive the role.

**Evidence status:** Role-label interpretation; exact coverage unverified.. Control ID: `printer-settings:topIntermediateSolidInfillAcceleration`.

### Top Most - topMostSolidInfillAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for the outermost visible top solid surface.

**When would I change it?** During a top-surface motion comparison with accepted flow, sufficient support and fixed pattern.

**What changes if I adjust it?** Lower may smooth starts/ends at a time cost; higher may increase throughput but reveal pressure, vibration or boundary defects.

**Check together with:** Top-surface speed, pattern and flow; Regular acceleration and layer cooling.

**Displayed units:** mm/s².

**Caution:** Acceleration cannot close a top skin that lacks support or correct an incorrect global multiplier by itself.

**Evidence status:** Functional surface-role interpretation; physical result unvalidated.. Control ID: `printer-settings:topMostSolidInfillAcceleration`.

### X/Y travel speed - travelSpeedXY

**Scope:** Machine/printer template / TRAVELSPEED.

**What does it mean?** Requested speed for non-printing X/Y travel, in millimetres per second.

**When would I change it?** After checking supported machine capability and actual travel routing, when balancing ooze time and reliable positioning.

**What changes if I adjust it?** Higher can reduce time spent oozing but increase motion demands; lower is gentler but can leave more time for strings or heat marks.

**Check together with:** Travel acceleration and firmware limits; Retraction thresholds, wall crossing and clearance.

**Displayed units:** mm/s.

**Caution:** It does not set printed extrusion speed. Do not raise travel speed to hide a collision, lifting part or failed homing.

**Evidence status:** Functional travel interpretation; mechanical limit unqualified.. Control ID: `printer-settings:travelSpeedXY`.

### Z travel speed - travelSpeedZ

**Scope:** Machine/printer template / TRAVELSPEED.

**What does it mean?** Requested vertical travel speed for supported Z moves.

**When would I change it?** Only during supported machine-motion qualification after checking the actual Z mechanism and firmware limits.

**What changes if I adjust it?** Higher can shorten lifts/layer moves but demand more from the Z system; lower can improve reliability while increasing time and ooze opportunity.

**Check together with:** Z acceleration and jerk; Z-hop, tool-change lift and combined XYZ moves.

**Displayed units:** mm/s.

**Caution:** XY capability does not imply Z capability. Exact treatment of combined XYZ moves must be checked; do not use this to fix probing or nozzle height.

**Evidence status:** Machine-motion interpretation; combined-move behaviour unverified.. Control ID: `printer-settings:travelSpeedZ`.

### Enable acceleration control - useAccelerations

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** Enables Rocket's configured acceleration-control requests.

**When would I change it?** Only when the intended division between slicer requests and OEM firmware motion control is understood.

**What changes if I adjust it?** Enabled can apply general/per-feature acceleration values. Disabled does not make physical acceleration zero; firmware behaviour remains.

**Check together with:** Regular/per-feature acceleration; Default axis settings and firmware limits.

**Caution:** Check actual emitted/effective commands. Toggling control ownership can invalidate a comparison even if every visible speed number stays the same.

**Evidence status:** Control-ownership interpretation; exact command coverage unverified.. Control ID: `printer-settings:useAccelerations`.

### Enable jerk control - useJerks

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** Enables the configured jerk/cornering-style requests from Rocket.

**When would I change it?** Only after verifying how the target OEM firmware interprets those requests and which layer should own them.

**What changes if I adjust it?** Enabled can apply regular/role jerk values. Disabled does not prove corners stop or the firmware's cornering setting is zero.

**Check together with:** Regular/outer-wall jerk; Firmware cornering model and acceleration.

**Caution:** Do not assume jerk, square-corner velocity and junction deviation share one meaning or portable value.

**Evidence status:** Firmware-control interpretation; actual command mapping unverified.. Control ID: `printer-settings:useJerks`.

### Use relative extrusion distances - useRelativeExtrusionDistances

**Scope:** Machine/printer template / GCODE.

**What does it mean?** Selects whether supported material-feed distances are emitted as increments rather than cumulative positions.

**When would I change it?** Only for a verified OEM postprocessor/firmware contract, not routine flow tuning.

**What changes if I adjust it?** Relative and absolute modes interpret the same numerical feed differently. A mismatch can cause a large unintended feed or withdrawal.

**Check together with:** Postprocessor and material-axis mapping; Start/reset commands, retraction and tool-change hooks.

**Caution:** Preserve the OEM mode and audit every feed/reset path. Do not assume standard E-mode commands safely cover composite V/U/P behaviour.

**Evidence status:** Critical command-mode declaration; hardware execution unqualified.. Control ID: `printer-settings:useRelativeExtrusionDistances`.

### Version - version

**Scope:** Machine/printer template / OTHER.

**What does it mean?** A version value associated with the printer definition, not necessarily the firmware or Rocket application version.

**When would I change it?** Only through the supported template-management or documented revision procedure.

**What changes if I adjust it?** May influence migration/comparison; increasing it does not upgrade firmware or prove a hardware change is safe.

**Check together with:** Preset imports and references; Application compatibility and factory baseline.

**Caution:** Keep real software/firmware versions separately. Exact template-version rules are unresolved.

**Evidence status:** Version metadata interpretation; exact migration rules unresolved.. Control ID: `printer-settings:version`.

### Wipe Tower - wipeTowerAcceleration

**Scope:** Machine/printer template / ACCELERATION.

**What does it mean?** The acceleration request for a generated wipe/prime tower used by the selected multi-tool workflow.

**When would I change it?** Only after confirming the tower actually exists and a controlled preparation comparison addresses its stability.

**What changes if I adjust it?** Lower may improve slender-tower consistency at a time cost; higher may reduce time but disturb priming or attachment.

**Check together with:** Tower geometry and speed; Tool changes, material delivery and firmware limits.

**Displayed units:** mm/s².

**Caution:** This is not physical nozzle-cleaning-station acceleration and does not add a tower when none is generated.

**Evidence status:** Feature-role interpretation; visibility and physical result unvalidated.. Control ID: `printer-settings:wipeTowerAcceleration`.

### Z-lift on tool change - zLiftOnToolChange

**Scope:** Machine/printer template / FEATURES.

**What does it mean?** The vertical lift associated with changing tools, separate from ordinary travel Z-hop.

**When would I change it?** Only through a supported tool-change clearance/alignment procedure on the actual machine.

**What changes if I adjust it?** More can increase clearance but add Z motion/time; less reduces the lift and can reduce clearance around fixtures or the part.

**Check together with:** Tool offsets and preparation/parking paths; Before/after tool-change code and Z limits.

**Displayed units:** mm.

**Caution:** Do not guess the amount or copy a previous unit's value. Incorrect clearance can cause a tool/fixture collision.

**Evidence status:** Hardware lifecycle motion; exact sequencing unverified.. Control ID: `printer-settings:zLiftOnToolChange`.

## Profile Settings

### Inner avoid distance coefficient - avoidCrossingInnerOffsetCoeff

**Scope:** Process: general / OOZEPREVENTION; Process: reinforced / OOZEPREVENTION; Process: speedy / OOZEPREVENTION.

**What does it mean?** Scales the clearance used by travel paths routed inside a boundary when avoiding crossings.

**When would I change it?** Review if an avoidance route runs too close to a wall or takes an excessive detour.

**What changes if I adjust it?** A larger clearance coefficient generally moves the route farther from the boundary; smaller keeps it closer.

**Check together with:** Avoid crossing borders; Travel routing; Retraction.

**Caution:** The reference distance and exact routing calculation are not established by the label. Inspect travel preview before relying on a change.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:avoidCrossingInnerOffsetCoeff`.

### Outer avoid distance coefficient - avoidCrossingOuterOffsetCoeff

**Scope:** Process: general / OOZEPREVENTION; Process: reinforced / OOZEPREVENTION; Process: speedy / OOZEPREVENTION.

**What does it mean?** Scales the clearance used by travel paths routed outside a boundary when avoiding crossings.

**When would I change it?** Review if an avoidance route runs too close to a wall or takes an excessive detour.

**What changes if I adjust it?** A larger clearance coefficient generally moves the route farther from the boundary; smaller keeps it closer.

**Check together with:** Avoid crossing borders; Travel routing; Retraction.

**Caution:** The reference distance and exact routing calculation are not established by the label. Inspect travel preview before relying on a change.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:avoidCrossingOuterOffsetCoeff`.

### Extrusion width - bottomIntermediateSkinEWMM

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Planned bead width for intermediate bottom skin—the solid material above the lowest bottom surface.

**When would I change it?** Adjust when adjacent lines fail to meet or the region cannot be filled cleanly.

**What changes if I adjust it?** Wider lines cover more space and require more plastic per distance; narrower lines fit finer details but may leave weak coverage.

**Check together with:** layer height; flow multiplier; nozzle geometry.

**Displayed units:** mm.

**Caution:** This is commanded line width, not physical nozzle diameter. Verify the sliced paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomIntermediateSkinEWMM`.

### Flow multiplier - bottomIntermediateSkinExtrusionMultP

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Scales plastic deposition for intermediate bottom skin—the solid material above the lowest bottom surface.

**When would I change it?** Use after the material's overall flow has been tuned, if this region alone remains overfilled or underfilled.

**What changes if I adjust it?** Higher values add plastic; lower values remove it without deliberately changing the model's dimensions.

**Check together with:** material flow; extrusion width; temperature.

**Caution:** Do not use a local multiplier to hide a blocked nozzle, moisture or wrong layer geometry.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomIntermediateSkinExtrusionMultP`.

### Fill angle - bottomIntermediateSkinInfillAngle

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Initial direction of fill lines for intermediate bottom skin—the solid material above the lowest bottom surface.

**When would I change it?** Change when line direction should suit a bridge span, surface appearance or load direction.

**What changes if I adjust it?** Rotates the pattern rather than making it denser; a different angle changes where lines meet walls.

**Check together with:** fill pattern; model orientation; angle increment.

**Displayed units:** °.

**Caution:** Patterns that are rotationally symmetric may respond differently. Confirm the selected region in Preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomIntermediateSkinInfillAngle`.

### Fill angle step - bottomIntermediateSkinInfillAngleStep

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Rotation added between successive fill layers for intermediate bottom skin—the solid material above the lowest bottom surface.

**When would I change it?** Change when consecutive layers should alternate directions rather than follow one orientation.

**What changes if I adjust it?** A larger step changes direction more per layer; zero requests no additional rotation.

**Check together with:** initial fill angle; fill pattern; layer schedule.

**Displayed units:** °.

**Caution:** This is an angular increment, not extra material or a pressure-advance setting.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomIntermediateSkinInfillAngleStep`.

### Infill/Wall overlap - bottomIntermediateSkinInfillExtendIntoPerimeterRatio

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Overlap where intermediate bottom skin—the solid material above the lowest bottom surface meets surrounding walls.

**When would I change it?** Adjust when the fill-to-wall joint has gaps or causes visible wall bulges.

**What changes if I adjust it?** More overlap improves contact but can overpack the boundary; less overlap eases packing but may weaken the joint.

**Check together with:** wall width; fill width; flow.

**Caution:** Overlap is not a substitute for correct extrusion. Evaluate both the interior joint and the outside surface.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomIntermediateSkinInfillExtendIntoPerimeterRatio`.

### Fill pattern - bottomIntermediateSkinInfillPattern

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Shape of the paths used for intermediate bottom skin—the solid material above the lowest bottom surface.

**When would I change it?** Choose for support, directionality, appearance and practical print time.

**What changes if I adjust it?** Different patterns redirect material and change intersections and travel; they do not guarantee equal strength at equal nominal density.

**Check together with:** fill angle; density or spacing; wall overlap.

**Selectable choices:**

- **Line:** Parallel straight fill paths. A simple directional fill; spacing and angle determine coverage. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Zigzag:** Back-and-forth fill joined where the geometry permits. It reduces separate line starts compared with disconnected lines. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Concentric:** Nested paths following the region's outline. Useful when following contours matters; inspect narrow centers and corners. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**Caution:** An available pattern is not necessarily appropriate for unsupported bridging or continuous fibre. Inspect its actual paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomIntermediateSkinInfillPattern`.

### Printing speed - bottomIntermediateSkinSpeed

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Requested printing speed for intermediate bottom skin—the solid material above the lowest bottom surface.

**When would I change it?** Change to balance that region's finish, bonding and print time.

**What changes if I adjust it?** Higher requests can shorten time but increase flow demand; lower requests can improve control but may increase heat exposure.

**Check together with:** volumetric capacity; acceleration; cooling.

**Displayed units:** mm/s.

**Caution:** Requested speed may be reduced by other limits. Preview and emitted output determine the actual schedule.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomIntermediateSkinSpeed`.

### Extrusion width - bottomMostSkinEWMM

**Scope:** Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.

**What does it mean?** Planned bead width for lowest bottom skin—the exposed underside region, not necessarily every first-layer feature.

**When would I change it?** Adjust when adjacent lines fail to meet or the region cannot be filled cleanly.

**What changes if I adjust it?** Wider lines cover more space and require more plastic per distance; narrower lines fit finer details but may leave weak coverage.

**Check together with:** layer height; flow multiplier; nozzle geometry.

**Displayed units:** mm.

**Caution:** This is commanded line width, not physical nozzle diameter. Verify the sliced paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomMostSkinEWMM`.

### Flow multiplier - bottomMostSkinExtrusionMultP

**Scope:** Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.

**What does it mean?** Scales plastic deposition for lowest bottom skin—the exposed underside region, not necessarily every first-layer feature.

**When would I change it?** Use after the material's overall flow has been tuned, if this region alone remains overfilled or underfilled.

**What changes if I adjust it?** Higher values add plastic; lower values remove it without deliberately changing the model's dimensions.

**Check together with:** material flow; extrusion width; temperature.

**Caution:** Do not use a local multiplier to hide a blocked nozzle, moisture or wrong layer geometry.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomMostSkinExtrusionMultP`.

### Fill angle - bottomMostSkinInfillAngle

**Scope:** Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.

**What does it mean?** Initial direction of fill lines for lowest bottom skin—the exposed underside region, not necessarily every first-layer feature.

**When would I change it?** Change when line direction should suit a bridge span, surface appearance or load direction.

**What changes if I adjust it?** Rotates the pattern rather than making it denser; a different angle changes where lines meet walls.

**Check together with:** fill pattern; model orientation; angle increment.

**Displayed units:** °.

**Caution:** Patterns that are rotationally symmetric may respond differently. Confirm the selected region in Preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomMostSkinInfillAngle`.

### Infill/Wall overlap - bottomMostSkinInfillExtendIntoPerimeterRatio

**Scope:** Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.

**What does it mean?** Overlap where lowest bottom skin—the exposed underside region, not necessarily every first-layer feature meets surrounding walls.

**When would I change it?** Adjust when the fill-to-wall joint has gaps or causes visible wall bulges.

**What changes if I adjust it?** More overlap improves contact but can overpack the boundary; less overlap eases packing but may weaken the joint.

**Check together with:** wall width; fill width; flow.

**Caution:** Overlap is not a substitute for correct extrusion. Evaluate both the interior joint and the outside surface.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomMostSkinInfillExtendIntoPerimeterRatio`.

### Fill pattern - bottomMostSkinInfillPattern

**Scope:** Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.

**What does it mean?** Shape of the paths used for lowest bottom skin—the exposed underside region, not necessarily every first-layer feature.

**When would I change it?** Choose for support, directionality, appearance and practical print time.

**What changes if I adjust it?** Different patterns redirect material and change intersections and travel; they do not guarantee equal strength at equal nominal density.

**Check together with:** fill angle; density or spacing; wall overlap.

**Selectable choices:**

- **Line:** Parallel straight fill paths. A simple directional fill; spacing and angle determine coverage. Schema contexts: Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.
- **Zigzag:** Back-and-forth fill joined where the geometry permits. It reduces separate line starts compared with disconnected lines. Schema contexts: Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.
- **Concentric:** Nested paths following the region's outline. Useful when following contours matters; inspect narrow centers and corners. Schema contexts: Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.
- **Hilbert Curve:** A winding, space-filling path with many right-angle turns. It produces a distinctive surface texture rather than a simple straight-line finish. Schema contexts: Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.
- **Archimedean Chords:** A curved, spiral-derived fill layout. It changes the direction and visual texture of the fill; inspect the actual clipped paths. Schema contexts: Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.
- **Octagram Spiral:** A star-like spiral fill layout. Its repeated turns give a distinctive path and surface pattern, not a guaranteed strength advantage. Schema contexts: Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.

**Caution:** An available pattern is not necessarily appropriate for unsupported bridging or continuous fibre. Inspect its actual paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomMostSkinInfillPattern`.

### Printing speed - bottomMostSkinSpeed

**Scope:** Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.

**What does it mean?** Requested printing speed for lowest bottom skin—the exposed underside region, not necessarily every first-layer feature.

**When would I change it?** Change to balance that region's finish, bonding and print time.

**What changes if I adjust it?** Higher requests can shorten time but increase flow demand; lower requests can improve control but may increase heat exposure.

**Check together with:** volumetric capacity; acceleration; cooling.

**Displayed units:** mm/s.

**Caution:** Requested speed may be reduced by other limits. Preview and emitted output determine the actual schedule.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bottomMostSkinSpeed`.

### Extrusion width - bridgeEWMM

**Scope:** Process: general / BRIDGE; Process: reinforced / BRIDGE; Process: speedy / BRIDGE.

**What does it mean?** Planned bead width for bridging plastic laid across an unsupported gap.

**When would I change it?** Adjust when adjacent lines fail to meet or the region cannot be filled cleanly.

**What changes if I adjust it?** Wider lines cover more space and require more plastic per distance; narrower lines fit finer details but may leave weak coverage.

**Check together with:** layer height; flow multiplier; nozzle geometry.

**Displayed units:** mm.

**Caution:** This is commanded line width, not physical nozzle diameter. Verify the sliced paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bridgeEWMM`.

### Flow multiplier - bridgeExtrusionMultP

**Scope:** Process: general / BRIDGE; Process: reinforced / BRIDGE; Process: speedy / BRIDGE.

**What does it mean?** Scales plastic deposition for bridging plastic laid across an unsupported gap.

**When would I change it?** Use after the material's overall flow has been tuned, if this region alone remains overfilled or underfilled.

**What changes if I adjust it?** Higher values add plastic; lower values remove it without deliberately changing the model's dimensions.

**Check together with:** material flow; extrusion width; temperature.

**Caution:** Do not use a local multiplier to hide a blocked nozzle, moisture or wrong layer geometry.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bridgeExtrusionMultP`.

### Fill angle - bridgeInfillAngle

**Scope:** Process: general / BRIDGE; Process: reinforced / BRIDGE; Process: speedy / BRIDGE.

**What does it mean?** Initial direction of fill lines for bridging plastic laid across an unsupported gap.

**When would I change it?** Change when line direction should suit a bridge span, surface appearance or load direction.

**What changes if I adjust it?** Rotates the pattern rather than making it denser; a different angle changes where lines meet walls.

**Check together with:** fill pattern; model orientation; angle increment.

**Displayed units:** °.

**Caution:** Patterns that are rotationally symmetric may respond differently. Confirm the selected region in Preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bridgeInfillAngle`.

### Infill/Wall overlap - bridgeInfillExtendIntoPerimeterRatio

**Scope:** Process: general / BRIDGE; Process: reinforced / BRIDGE; Process: speedy / BRIDGE.

**What does it mean?** Overlap where bridging plastic laid across an unsupported gap meets surrounding walls.

**When would I change it?** Adjust when the fill-to-wall joint has gaps or causes visible wall bulges.

**What changes if I adjust it?** More overlap improves contact but can overpack the boundary; less overlap eases packing but may weaken the joint.

**Check together with:** wall width; fill width; flow.

**Caution:** Overlap is not a substitute for correct extrusion. Evaluate both the interior joint and the outside surface.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bridgeInfillExtendIntoPerimeterRatio`.

### Fill pattern - bridgeInfillPattern

**Scope:** Process: general / BRIDGE; Process: reinforced / BRIDGE; Process: speedy / BRIDGE.

**What does it mean?** Shape of the paths used for bridging plastic laid across an unsupported gap.

**When would I change it?** Choose for support, directionality, appearance and practical print time.

**What changes if I adjust it?** Different patterns redirect material and change intersections and travel; they do not guarantee equal strength at equal nominal density.

**Check together with:** fill angle; density or spacing; wall overlap.

**Selectable choices:**

- **Line:** Parallel straight fill paths. A simple directional fill; spacing and angle determine coverage. For a bridge, verify that generated lines anchor to supported edges; a selectable pattern is not proof of a printable span. Schema contexts: Process: general / BRIDGE; Process: reinforced / BRIDGE; Process: speedy / BRIDGE.
- **Zigzag:** Back-and-forth fill joined where the geometry permits. It reduces separate line starts compared with disconnected lines. For a bridge, verify that generated lines anchor to supported edges; a selectable pattern is not proof of a printable span. Schema contexts: Process: general / BRIDGE; Process: reinforced / BRIDGE; Process: speedy / BRIDGE.
- **Concentric:** Nested paths following the region's outline. Useful when following contours matters; inspect narrow centers and corners. For a bridge, verify that generated lines anchor to supported edges; a selectable pattern is not proof of a printable span. Schema contexts: Process: general / BRIDGE; Process: reinforced / BRIDGE; Process: speedy / BRIDGE.

**Caution:** An available pattern is not necessarily appropriate for unsupported bridging or continuous fibre. Inspect its actual paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bridgeInfillPattern`.

### Printing speed - bridgeSpeed

**Scope:** Process: general / BRIDGE; Process: reinforced / BRIDGE; Process: speedy / BRIDGE.

**What does it mean?** Requested printing speed for bridging plastic laid across an unsupported gap.

**When would I change it?** Change to balance that region's finish, bonding and print time.

**What changes if I adjust it?** Higher requests can shorten time but increase flow demand; lower requests can improve control but may increase heat exposure.

**Check together with:** volumetric capacity; acceleration; cooling.

**Displayed units:** mm/s.

**Caution:** Requested speed may be reduced by other limits. Preview and emitted output determine the actual schedule.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:bridgeSpeed`.

### Distance from part - brimDistanceToPart

**Scope:** Process: general / BRIMSKIRT; Process: reinforced / BRIMSKIRT; Process: speedy / BRIMSKIRT.

**What does it mean?** The separation between the brim and the part it surrounds.

**When would I change it?** Change when the brim is too difficult to remove or does not hold the part adequately.

**What changes if I adjust it?** A larger gap usually eases removal but weakens attachment; a smaller gap improves attachment but may scar the edge.

**Check together with:** Generate brim; Brim loops; First-layer width.

**Displayed units:** mm.

**Caution:** A brim cannot compensate for an incorrect bed/nozzle setup.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:brimDistanceToPart`.

### Brim extrusion width - brimEWMM

**Scope:** Process: general / BRIMSKIRT; Process: reinforced / BRIMSKIRT; Process: speedy / BRIMSKIRT.

**What does it mean?** The planned width of each plastic line in the brim.

**When would I change it?** Change only when brim lines do not join or the brim needs different coverage.

**What changes if I adjust it?** Wider lines cover more area per loop and need more plastic; narrower lines reduce coverage.

**Check together with:** Brim loops; Brim flow multiplier; First-layer height.

**Displayed units:** mm.

**Caution:** Use a width appropriate to the selected nozzle and material; this is not a nozzle-diameter setting.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:brimEWMM`.

### Flow multiplier - brimExtrusionMultP

**Scope:** Process: general / BRIMSKIRT; Process: reinforced / BRIMSKIRT; Process: speedy / BRIMSKIRT.

**What does it mean?** Scales the plastic delivered while printing the brim.

**When would I change it?** Adjust after verifying first-layer height when the brim is consistently overfilled or underfilled.

**What changes if I adjust it?** Higher delivers more plastic per planned brim path; lower delivers less.

**Check together with:** Brim extrusion width; First-layer height; Material flow settings.

**Caution:** Do not use a brim-only multiplier to hide a general extrusion or bed-level problem.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:brimExtrusionMultP`.

### Brim - brimLoops

**Scope:** Process: general / BRIMSKIRT; Process: reinforced / BRIMSKIRT; Process: speedy / BRIMSKIRT.

**What does it mean?** The number of brim lines added around the part.

**When would I change it?** Increase for additional edge anchoring, or reduce when adhesion is sufficient and cleanup matters.

**What changes if I adjust it?** More loops widen the anchoring area and use more material; fewer make a smaller brim.

**Check together with:** Generate brim; Brim width per line; Distance from part.

**Displayed units:** loops.

**Caution:** Check preview around narrow gaps and nearby parts; more loops do not guarantee adhesion.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:brimLoops`.

### Support interface pattern - classicInterfaceSupportInfillType

**Scope:** Process: general / SUPPORT.

**What does it mean?** The pattern used in the dense support contact region.

**When would I change it?** Choose a pattern when comparing supported surface finish and removal effort.

**What changes if I adjust it?** Different patterns change line direction, contact distribution and continuity rather than simply adding strength.

**Check together with:** Top and bottom interface spacing; Interface generation; Z contact distances.

**Selectable choices:**

- **Rectilinear Interlaced:** Straight-line interface filling with interlaced directions. It spreads contact across directions; inspect how layers alternate in Rocket. Schema contexts: Process: general / SUPPORT.
- **Grid:** Crossing line families forming a grid. This gives connections in more than one direction but creates intersections. Schema contexts: Process: general / SUPPORT.
- **Line:** Parallel straight fill paths. A simple directional fill; spacing and angle determine coverage. Schema contexts: Process: general / SUPPORT.
- **Concentric:** Nested paths following the region's outline. Useful when following contours matters; inspect narrow centers and corners. Schema contexts: Process: general / SUPPORT.

**Caution:** A pattern alone does not set the clearance between support and part.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicInterfaceSupportInfillType`.

### Automatically calculate conventional support brim - classicSupportAutoBrim

**Scope:** Process: general / SUPPORT.

**What does it mean?** Lets Rocket determine the brim used for normal support automatically.

**When would I change it?** Use when the support needs bed anchoring without a manually chosen support brim width.

**What changes if I adjust it?** Enabled delegates support-brim sizing to the slicer; disabled leaves the manual setting relevant where supported.

**Check together with:** Support brim width; Normal support; Build plate only.

**Caution:** The sizing formula is not documented in the inspected declaration; verify the generated brim.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportAutoBrim`.

### Pattern angle - classicSupportBaseFillAngle

**Scope:** Process: general / SUPPORT.

**What does it mean?** The orientation of the lines in normal support's base pattern.

**When would I change it?** Rotate it to compare support stability or how support lines meet the supported area.

**What changes if I adjust it?** Changing the angle rotates the support pattern; it does not change support density by itself.

**Check together with:** Base pattern; Base pattern spacing; Supported geometry.

**Displayed units:** °.

**Caution:** Orientation effects depend on the selected pattern; confirm in layer preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportBaseFillAngle`.

### Base pattern spacing - classicSupportBasePatternSpacing

**Scope:** Process: general / SUPPORT.

**What does it mean?** The spacing between lines of the normal support base pattern.

**When would I change it?** Change when support is unnecessarily bulky or too sparse to remain stable.

**What changes if I adjust it?** Larger spacing generally gives a lighter, more open support; smaller spacing gives denser support and uses more material.

**Check together with:** Base pattern; Support wall; Interface spacing.

**Displayed units:** mm.

**Caution:** Sparse support may fail before it supports the model. Interface density is a separate setting.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportBasePatternSpacing`.

### Base pattern - classicSupportBodyInfillType

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT.

**What does it mean?** The internal pattern of normal support beneath its contact interface.

**When would I change it?** Choose based on support stability, material use and removal behavior.

**What changes if I adjust it?** Patterns change the structure of the support body; spacing remains a separate control.

**Check together with:** Base pattern spacing; Support wall; Support interface pattern.

**Selectable choices:**

- **Line:** Parallel straight fill paths. A simple directional fill; spacing and angle determine coverage. Schema contexts: Process: general / SUPPORT.
- **Grid:** Crossing line families forming a grid. This gives connections in more than one direction but creates intersections. Schema contexts: Process: general / SUPPORT.
- **Honeycomb:** A cellular pattern based on hexagonal cells. It creates repeated cell walls rather than long parallel fill lines. Schema contexts: Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT.
- **Rectilinear:** Straight-line support filling. In the installed schema this is another displayed label for the Line support-body value. Schema contexts: Process: fortified / SUPPORT; Process: reinforced / SUPPORT.
- **Rectilinear grid:** Crossing straight-line support filling. In the installed schema this is another displayed label for the Grid support-body value. Schema contexts: Process: fortified / SUPPORT; Process: reinforced / SUPPORT.

**Caution:** Do not confuse the support-body pattern with the model's own infill.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportBodyInfillType`.

### Bottom interface spacing - classicSupportBottomInterfaceSpacing

**Scope:** Process: general / SUPPORT.

**What does it mean?** Line spacing in the bottom contact interface of normal support.

**When would I change it?** Change when the bottom supported contact is too rough or the interface is unnecessarily dense.

**What changes if I adjust it?** Smaller spacing generally produces a denser contact surface; larger spacing uses less material but supports less continuously.

**Check together with:** Bottom interface generation; Support interface pattern; Bottom Z distance.

**Displayed units:** mm.

**Caution:** Denser contact can increase bonding and removal effort; spacing is not the vertical separation.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportBottomInterfaceSpacing`.

### Bottom Z distance - classicSupportBottomZDistance

**Scope:** Process: general / SUPPORT.

**What does it mean?** The vertical separation at the bottom side of normal support where it meets model material.

**When would I change it?** Change to balance support removal against the quality of that contact surface.

**What changes if I adjust it?** A larger gap usually separates more easily but leaves a less supported surface; a smaller gap improves contact but can fuse.

**Check together with:** Bottom interface spacing; Layer height; Support material.

**Displayed units:** mm.

**Caution:** Check the sliced result: layer quantization can make the effective gap differ from the requested value.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportBottomZDistance`.

### Brim width - classicSupportBrimWidth

**Scope:** Process: general / SUPPORT.

**What does it mean?** The width of the anchoring brim for normal support.

**When would I change it?** Change when support bases lift or when their brim obstructs nearby features.

**What changes if I adjust it?** A wider brim anchors a larger area but uses more bed space and needs more removal.

**Check together with:** Automatically calculate conventional support brim; Support base geometry.

**Displayed units:** mm.

**Caution:** Automatic brim calculation may govern the result instead; inspect which control is active.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportBrimWidth`.

### Normal support expansion - classicSupportExpansion

**Scope:** Process: general / SUPPORT.

**What does it mean?** Expands or contracts the footprint of normal support around the areas being supported.

**When would I change it?** Review when support coverage misses an edge or spreads farther than needed.

**What changes if I adjust it?** More expansion generally broadens support coverage and material use; less keeps it closer to the original support region.

**Check together with:** Support/model XY distance; Overhang generation; Support base pattern.

**Displayed units:** mm.

**Caution:** The accepted sign and exact offset behavior are not established here; preview rather than assuming a negative value is valid.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportExpansion`.

### Maximum classic-support layer height - classicSupportMaxLayerHeight

**Scope:** Process: general / SUPPORT.

**What does it mean?** The upper layer-height bound used when normal support has independent layers.

**When would I change it?** Adjust only when using independent support layers and reviewing their printed quality or time.

**What changes if I adjust it?** Changing the bound changes which support-layer heights can be chosen; coarser layers can save time but reduce vertical detail.

**Check together with:** Independent support layer height; Other support-height bound; Nozzle and support material.

**Displayed units:** mm.

**Declared editor constraints:** {"greaterThanOrEqualField": "classicSupportMinLayerHeight"}. These are not operating recommendations.

**Caution:** Keep the two bounds consistent. A UI-accepted height is not proof that the nozzle can print it.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportMaxLayerHeight`.

### Minimum classic-support layer height - classicSupportMinLayerHeight

**Scope:** Process: general / SUPPORT.

**What does it mean?** The lower layer-height bound used when normal support has independent layers.

**When would I change it?** Adjust only when using independent support layers and reviewing their printed quality or time.

**What changes if I adjust it?** Changing the bound changes which support-layer heights can be chosen; coarser layers can save time but reduce vertical detail.

**Check together with:** Independent support layer height; Other support-height bound; Nozzle and support material.

**Displayed units:** mm.

**Caution:** Keep the two bounds consistent. A UI-accepted height is not proof that the nozzle can print it.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportMinLayerHeight`.

### Normal support generation mode - classicSupportMode

**Scope:** Process: general / SUPPORT.

**What does it mean?** Selects how normal support locations are chosen.

**When would I change it?** Choose automatic coverage, deliberate manual placement, or a combination when support planning needs control.

**What changes if I adjust it?** The mode changes the source of support regions, not their contact gap or material.

**Check together with:** Enable support; Support placement tools; Normal support style.

**Selectable choices:**

- **Auto:** Lets Rocket identify regions needing support automatically. Still inspect the result for missed or unwanted supports. Schema contexts: Process: general / SUPPORT.
- **Manual:** Uses deliberate user support placement rather than relying on automatic coverage. Every needed region must be checked. Schema contexts: Process: general / SUPPORT.
- **Hybrid:** Combines automatic support generation with user-directed placement. Confirm how your additions and exclusions affect the final supports. Schema contexts: Process: general / SUPPORT.

**Caution:** Manual and hybrid placement must be checked in preview; a selected mode does not prove every overhang is supported.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportMode`.

### Remove small overhangs - classicSupportRemoveSmallOverhang

**Scope:** Process: general / SUPPORT.

**What does it mean?** Omits support for small overhanging areas that Rocket considers negligible.

**When would I change it?** Use when many tiny support islands add effort without improving the part.

**What changes if I adjust it?** Enabled may reduce small supports and cleanup; disabled retains more candidate support regions.

**Check together with:** Normal support generation; Overhang shape; Support placement.

**Caution:** The threshold is not established by this label. It removes support candidates, not geometry from your model.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportRemoveSmallOverhang`.

### Top interface spacing - classicSupportTopInterfaceSpacing

**Scope:** Process: general / SUPPORT.

**What does it mean?** Line spacing in the top contact interface of normal support.

**When would I change it?** Change when the top supported contact is too rough or the interface is unnecessarily dense.

**What changes if I adjust it?** Smaller spacing generally produces a denser contact surface; larger spacing uses less material but supports less continuously.

**Check together with:** Top interface generation; Support interface pattern; Top Z distance.

**Displayed units:** mm.

**Caution:** Denser contact can increase bonding and removal effort; spacing is not the vertical separation.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportTopInterfaceSpacing`.

### Top Z distance - classicSupportTopZDistance

**Scope:** Process: general / SUPPORT.

**What does it mean?** The vertical separation at the top side of normal support where it meets model material.

**When would I change it?** Change to balance support removal against the quality of that contact surface.

**What changes if I adjust it?** A larger gap usually separates more easily but leaves a less supported surface; a smaller gap improves contact but can fuse.

**Check together with:** Top interface spacing; Layer height; Support material.

**Displayed units:** mm.

**Caution:** Check the sliced result: layer quantization can make the effective gap differ from the requested value.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportTopZDistance`.

### Independent support layer height - classicSupportUseIndependentLayerHeight

**Scope:** Process: general / SUPPORT.

**What does it mean?** Allows normal support to use a layer schedule distinct from the model's.

**When would I change it?** Use when comparing support efficiency against contact quality.

**What changes if I adjust it?** Enabled permits support-specific layer heights; disabled ties support more closely to the model schedule.

**Check together with:** Minimum classic-support layer height; Maximum classic-support layer height; Model layer height.

**Caution:** Independent support layers still need compatible contact geometry and a printable extrusion height.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportUseIndependentLayerHeight`.

### Support wall - classicSupportWallCount

**Scope:** Process: general / SUPPORT.

**What does it mean?** The number of perimeter walls around normal support.

**When would I change it?** Change when support needs more stability or easier breakup.

**What changes if I adjust it?** More walls reinforce the support boundary but use material and can make removal harder.

**Check together with:** Base pattern; Base spacing; Support geometry.

**Displayed units:** loops.

**Selectable choices:**

- **0:** No perimeter wall around the support body; the internal support pattern provides the structure. Schema contexts: Process: general / SUPPORT.
- **1:** One perimeter wall around the support body, adding a boundary shell. Schema contexts: Process: general / SUPPORT.
- **2:** Two perimeter walls around the support body, adding more shell material and usually more removal effort. Schema contexts: Process: general / SUPPORT.

**Caution:** More walls cannot repair a disconnected or poorly anchored support.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportWallCount`.

### Support/model XY distance - classicSupportXYDistance

**Scope:** Process: general / SUPPORT.

**What does it mean?** The horizontal clearance between normal support and the model.

**When would I change it?** Change when support fuses to side walls or fails to reach near an overhang edge.

**What changes if I adjust it?** Larger clearance reduces side contact but leaves more unsupported edge; smaller clearance improves reach but can fuse.

**Check together with:** Normal support expansion; Z distances; Nozzle width.

**Displayed units:** mm.

**Caution:** This is a side gap, not the top or bottom contact gap.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:classicSupportXYDistance`.

### Correction move fiber feedrate - correctionMoveFiberFeedrate

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The fibre feedrate used during a correction move.

**When would I change it?** Change only when an OEM correction procedure identifies a feed mismatch.

**What changes if I adjust it?** It changes fibre delivery during that special movement rather than setting normal model-printing speed.

**Check together with:** Correction move speed; Fibre tension; Strand feed calibration.

**Displayed units:** %.

**Caution:** The correction move's purpose and direction must be established before changing the feed. Preserve the OEM baseline.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:correctionMoveFiberFeedrate`.

### Correction move speed - correctionMoveSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The movement speed of the special fibre correction move.

**When would I change it?** Leave unchanged unless the OEM procedure calls for a specific correction-motion adjustment.

**What changes if I adjust it?** A higher value requests a faster correction movement; lower requests slower motion, changing its relationship to fibre feed.

**Check together with:** Correction move fiber feedrate; Fibre tension sequence.

**Displayed units:** mm/s.

**Caution:** Do not independently tune motion and strand feed without knowing how the correction sequence coordinates them.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:correctionMoveSpeed`.

### Style - currentNormalSupportStyle

**Scope:** Process: general / SUPPORT.

**What does it mean?** Selects the overall construction style for normal support.

**When would I change it?** Review when choosing the normal-support system; only the installed declared style is described here.

**What changes if I adjust it?** Style determines the support framework while base and interface patterns refine it.

**Check together with:** Support type; Normal support base pattern.

**Selectable choices:**

- **Grid:** The installed normal-support framework uses the Grid style. Base infill pattern and interface pattern are separate choices. Schema contexts: Process: general / SUPPORT.

**Caution:** The only known declared option is Grid; do not assume styles from another slicer are available.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:currentNormalSupportStyle`.

### Type - currentSupportType

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Chooses normal or tree-like support construction.

**When would I change it?** Use normal support for conventional columns/regions or compare tree support for branching reach around a model.

**What changes if I adjust it?** The selection changes support geometry and which related controls apply.

**Check together with:** Normal support style; Tree support styles; Enable support.

**Selectable choices:**

- **Tree:** Branching support that reaches toward contact regions. Its branches and base need enough stability and clearance. Schema contexts: Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.
- **Normal:** Conventional support bodies beneath selected overhang regions, controlled by normal-support base and interface settings. Schema contexts: Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**Caution:** Neither type is universally better. Inspect every contact, branch and bed attachment.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:currentSupportType`.

### Tree support styles - currentTreeSupportStyle

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Chooses the emphasis of tree support's branch structure.

**When would I change it?** Compare a lighter branch structure with a more substantial one when tree support is selected.

**What changes if I adjust it?** Slim favors a less bulky tree; Strong favors a more substantial tree, with corresponding material/removal tradeoffs.

**Check together with:** Support type; Tree branch settings; Contact geometry.

**Selectable choices:**

- **Slim:** The less bulky tree style. Compare its material use and clearance against the stability needed by your model. Schema contexts: Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.
- **Strong:** The more substantial tree style. It favors support robustness but can use more material and be harder to remove. Schema contexts: Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**Caution:** These names do not specify mechanical load ratings or guarantee successful support.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:currentTreeSupportStyle`.

### Description - description

**Scope:** Process: fortified / OTHER; Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** A human-readable note describing the process template.

**When would I change it?** Use it to record purpose, material/nozzle context, experimental status and what changed.

**What changes if I adjust it?** Editing the description should improve identification rather than change slicing parameters.

**Check together with:** Template name; Saved version notes.

**Caution:** A note claiming validation is not evidence of a print result; do not put private machine or account identifiers in public templates.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:description`.

### Avoid crossing borders - doAvoidCrossingPerimeters

**Scope:** Process: general / OOZEPREVENTION; Process: reinforced / OOZEPREVENTION; Process: speedy / OOZEPREVENTION.

**What does it mean?** Asks travel moves to avoid crossing printed boundaries where possible.

**When would I change it?** Enable when travel scars or strings appear across visible surfaces; compare time and route complexity.

**What changes if I adjust it?** Avoiding crossings can hide travel and reduce exposed strings but may lengthen the route.

**Check together with:** Inner and outer avoid coefficients; Retraction only when crossing borders; Travel speed.

**Caution:** It is a routing preference, not a guarantee that every boundary can be avoided.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:doAvoidCrossingPerimeters`.

### Do coast before retract - doCoastAtEnd

**Scope:** Process: general / OOZEPREVENTION; Process: reinforced / OOZEPREVENTION; Process: speedy / OOZEPREVENTION.

**What does it mean?** Ends plastic extrusion before the very end of a path so remaining pressure can finish the line before retraction.

**When would I change it?** Consider only after basic flow and retraction are understood and path ends consistently bulge.

**What changes if I adjust it?** Enabled can reduce end blobs but can also leave thin or incomplete line ends.

**Check together with:** Retraction; Coasting amount or distance; Material flow.

**Caution:** This is not pressure advance. Do not use it to compensate for an unverified material flow setting.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:doCoastAtEnd`.

### Do retract on changing layers - doRetractOnLayerChange

**Scope:** Process: general / OOZEPREVENTION; Process: reinforced / OOZEPREVENTION; Process: speedy / OOZEPREVENTION.

**What does it mean?** Requests retraction when moving to a new layer.

**When would I change it?** Compare when layer changes leave strings or blobs.

**What changes if I adjust it?** Enabled adds layer-change pressure relief but also more retract cycles and possible restart marks.

**Check together with:** Retraction distance and speed; Z-hop policy; Layer-change travel.

**Caution:** Check whether other retraction rules override or combine with it; do not transfer plastic settings to continuous fibre.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:doRetractOnLayerChange`.

### Do retract only when crossing borders - doRetractOnlyWhenCrossingPerimeters

**Scope:** Process: general / OOZEPREVENTION; Process: reinforced / OOZEPREVENTION; Process: speedy / OOZEPREVENTION.

**What does it mean?** Limits retraction to travels that cross printed boundaries.

**When would I change it?** Use to reduce unnecessary retract cycles during internal travel.

**What changes if I adjust it?** Enabled can reduce retract frequency and time, but internal oozing may increase.

**Check together with:** Avoid crossing borders; Retraction on layer change; Retraction length.

**Caution:** It does not itself create an avoidance route or guarantee no visible strings.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:doRetractOnlyWhenCrossingPerimeters`.

### Do wipe nozzle - doWipeNozzle

**Scope:** Process: general / OOZEPREVENTION; Process: reinforced / OOZEPREVENTION; Process: speedy / OOZEPREVENTION.

**What does it mean?** Adds a nozzle wiping movement associated with ending an extrusion path.

**When would I change it?** Consider when path endings leave blobs or excess material.

**What changes if I adjust it?** Enabled spreads or relieves residual material along a wipe path, but can mark a surface or delay travel.

**Check together with:** Retraction; Wipe distance and speed; Coasting.

**Caution:** This is a toolpath action, not a guarantee that the physical nozzle is clean or a bed-cleaning operation.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:doWipeNozzle`.

### Do Z-hop when retract only - doZHop

**Scope:** Process: general / OOZEPREVENTION; Process: reinforced / OOZEPREVENTION; Process: speedy / OOZEPREVENTION.

**What does it mean?** Restricts Z-hop to moves associated with retraction, as the displayed 'when retract only' label indicates.

**When would I change it?** Change when deciding which travel moves should receive an already-configured hop.

**What changes if I adjust it?** Enabled ties lifting to retracting travels; it is not the numerical lift height.

**Check together with:** Z-hop height; Retraction conditions; Travel clearance.

**Caution:** The raw field name sounds like a general enable switch, but the installed label is conditional. Confirm actual travel preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:doZHop`.

### Adjust seam distribution (fiber) - enableAdjustSeamDistributionPositionFiber

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Enables adjustment of where continuous-fibre seams are distributed across paths or layers.

**When would I change it?** Use when a visible seam pattern or repeated starts need deliberate positioning.

**What changes if I adjust it?** Enabled allows the related distribution adjustment to affect seam placement; it does not remove starts and stops.

**Check together with:** Seam distribution controls; Seam start-position adjustment; Path geometry.

**Caution:** Fibre starts and cuts affect strand continuity and anchoring. Preserve the OEM baseline unless a controlled fibre test justifies change.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:enableAdjustSeamDistributionPositionFiber`.

### Adjust seam distribution (plastic) - enableAdjustSeamDistributionPositionPlastic

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Enables adjustment of where plastic seams are distributed across paths or layers.

**When would I change it?** Use when a visible seam pattern or repeated starts need deliberate positioning.

**What changes if I adjust it?** Enabled allows the related distribution adjustment to affect seam placement; it does not remove starts and stops.

**Check together with:** Seam distribution controls; Seam start-position adjustment; Path geometry.

**Caution:** Moving a seam relocates the surface mark; it does not correct over-extrusion or retraction.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:enableAdjustSeamDistributionPositionPlastic`.

### Adjust seam start position (fiber) - enableAdjustSeamStartPositionFiber

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Enables adjustment of the starting location of continuous-fibre seams.

**When would I change it?** Use when the first seam location needs to move away from a visible or critical face.

**What changes if I adjust it?** Enabled allows the related start-position setting to influence the seam; disabled leaves the normal placement rule.

**Check together with:** Seam start-position control; Seam distribution; Print order.

**Caution:** Continuous-fibre start placement can change anchoring and uninterrupted reinforcement; it is not merely a cosmetic plastic seam.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:enableAdjustSeamStartPositionFiber`.

### Adjust seam start position (plastic) - enableAdjustSeamStartPositionPlastic

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Enables adjustment of the starting location of plastic seams.

**When would I change it?** Use when the first seam location needs to move away from a visible or critical face.

**What changes if I adjust it?** Enabled allows the related start-position setting to influence the seam; disabled leaves the normal placement rule.

**Check together with:** Seam start-position control; Seam distribution; Print order.

**Caution:** Inspect the resulting seam in preview. The switch alone does not identify a particular coordinate or angle.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:enableAdjustSeamStartPositionPlastic`.

### Enable arc fitting - enableArcFitting

**Scope:** Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Allows suitable segmented curves to be represented as arcs in the generated toolpath.

**When would I change it?** Consider when the selected machine/export path explicitly supports the emitted arc commands.

**What changes if I adjust it?** It can reduce command count and alter curve representation; it does not increase the resolution of the original model.

**Check together with:** Arc tolerance or segment controls; Machine G-code support; Curve geometry.

**Caution:** Do not enable solely because another slicer uses it. Confirm Rocket's exported commands and the target's support.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:enableArcFitting`.

### Enable height-based speed limit - enableHeightSlowdown

**Scope:** Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Enables a speed limit that depends on print height.

**When would I change it?** Use when tall or flexible parts become less stable higher above the bed.

**What changes if I adjust it?** Enabled allows the height-dependent rule to slow relevant printing; lower speed can reduce shaking but lengthens the job.

**Check together with:** Height slowdown thresholds; Feature speeds; Part stability.

**Caution:** The switch does not define the height or amount of slowdown. Check the associated controls and preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:enableHeightSlowdown`.

### Slow down at overhang - enableSlowDownAtOverhang

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Allows slower printing on overhanging areas.

**When would I change it?** Use when unsupported edges sag or lose detail.

**What changes if I adjust it?** Slowing can improve placement and cooling, but increases local heating time and total print time.

**Check together with:** Overhang speed settings; Cooling; Layer height.

**Caution:** Slowdown does not turn an unprintable overhang into a supported surface.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:enableSlowDownAtOverhang`.

### Slow down for curled perimeters - enableSlowDownAtPredictedWallCurl

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Slows printing where the slicer predicts a wall may curl upward.

**When would I change it?** Use when curling walls or nozzle catches are a recurring feature-specific problem.

**What changes if I adjust it?** Enabled permits extra slowdown in predicted curl regions, potentially reducing collisions at the cost of time.

**Check together with:** Cooling; Overhang slowdown; Wall speeds.

**Caution:** This is a prediction, not a sensor measurement or a guarantee against collisions.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:enableSlowDownAtPredictedWallCurl`.

### Enable minimum layer time slowdown - enableSlowDownAtShortPrintTimeLayer

**Scope:** Process: fortified / OTHER; Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Allows layers to slow down when their estimated printing time is too short.

**When would I change it?** Use for small features that remain soft before the next layer arrives.

**What changes if I adjust it?** Enabled spreads the same layer over more time to allow cooling; excessive slowing can also keep heat near a small area.

**Check together with:** Minimum layer time; Minimum printing speed; Cooling.

**Caution:** The time target and minimum speed can limit the result; this is not a pause or temperature calibration.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:enableSlowDownAtShortPrintTimeLayer`.

### Smooth speed discontinuity areas - enableWallSpeedSmoothing

**Scope:** Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Softens abrupt changes between different wall printing speeds.

**When would I change it?** Use when speed transitions leave visible bands or inconsistent wall finish.

**What changes if I adjust it?** Enabled can make transitions more gradual rather than switching speed sharply, potentially changing time and local finish.

**Check together with:** Wall speeds; Overhang slowdown; Smoothing parameters.

**Caution:** It is not a replacement for machine acceleration tuning or pressure advance.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:enableWallSpeedSmoothing`.

### End G-code - endGCode

**Scope:** Process: fortified / OTHER; Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Custom commands inserted at the end of the generated job.

**When would I change it?** Change only for a documented machine-specific shutdown or finishing requirement.

**What changes if I adjust it?** Commands can alter heaters, motion, extrusion and machine state after the model finishes.

**Check together with:** Machine command dialect; Tool selection; End-of-job safety.

**Caution:** High risk: preserve the OEM sequence. Do not paste commands from TinMan, another printer or an unverified example.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:endGCode`.

### Plastic flow multiplier after cut - fiberAfterCutExtrusionMultP

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** Scales plastic flow in the continuous-fibre path after the strand has been cut.

**When would I change it?** Change only under a documented fibre-tail or termination calibration procedure.

**What changes if I adjust it?** Higher requests more matrix plastic in that after-cut phase; lower requests less.

**Check together with:** Fibre cut timing; Finish length and speed; Matrix material flow.

**Caution:** This concerns matrix plastic around a cut strand, not ordinary filament retraction. Preserve the OEM baseline.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberAfterCutExtrusionMultP`.

### Do Z-hop after cut - fiberDoZHopAfterCut

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** Requests a Z lift after a continuous-fibre cut.

**When would I change it?** Review only when the OEM procedure calls for clearance after cutting.

**What changes if I adjust it?** Enabled changes the post-cut motion sequence and may improve clearance, but can affect strand handling and timing.

**Check together with:** Fibre cut sequence; Z-hop height; Travel clearance.

**Caution:** Do not change this as a general anti-stringing switch; the cutting and strand-release sequence matters.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberDoZHopAfterCut`.

### Fiber extrusion compensation ratio - fiberExtrusionCompensationRatio

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** A compensation factor for the continuous-fibre extrusion calculation.

**When would I change it?** Change only with an OEM-supported fibre-feed calibration and a measured reason.

**What changes if I adjust it?** It changes compensation applied to fibre delivery; the exact formula and direction are not established by the installed label.

**Check together with:** Fibre feed calibration; Matrix flow; Strand path and tension.

**Caution:** High risk: do not treat this as the ordinary plastic flow multiplier or guess a corrected value.

**Evidence status:** Installed label confirmed; compensation formula unresolved; retain OEM value pending documented procedure. Control ID: `profile-settings:fiberExtrusionCompensationRatio`.

### Extrusion width - fiberFLEWMM

**Scope:** Process: fortified / FirstLayer; Process: general / FirstLayer; Process: reinforced / FirstLayer.

**What does it mean?** The planned line width for the first continuous-fibre layer.

**When would I change it?** Change only when a documented first-fibre-layer procedure calls for a different bead geometry.

**What changes if I adjust it?** A wider planned bead occupies more space and changes matrix demand and path placement; a narrower bead does the reverse.

**Check together with:** First fibre-layer height; First fibre-layer flow; Fibre path spacing.

**Displayed units:** mm.

**Caution:** A continuous strand must fit and anchor in the matrix. Do not copy a plastic-nozzle width rule without OEM confirmation.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberFLEWMM`.

### Flow multiplier - fiberFLExtrusionMultP

**Scope:** Process: fortified / FirstLayer; Process: general / FirstLayer; Process: reinforced / FirstLayer.

**What does it mean?** Scales matrix-plastic delivery for the first continuous-fibre layer.

**When would I change it?** Review after the physical fibre-feed setup and first-layer geometry are verified.

**What changes if I adjust it?** Higher supplies more matrix plastic; lower supplies less, changing coverage around the strand.

**Check together with:** First fibre-layer width and height; Material flow; Fibre feed.

**Caution:** This is not a strand-length calibration. Preserve the OEM starting value until a controlled fibre test supports change.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberFLExtrusionMultP`.

### Speed coefficient - fiberFLSpeedCoeff

**Scope:** Process: fortified / FirstLayer; Process: general / FirstLayer; Process: reinforced / FirstLayer.

**What does it mean?** Scales printing speed for the first continuous-fibre layer.

**When would I change it?** Change only to address verified first-fibre-layer placement or anchoring behavior.

**What changes if I adjust it?** A higher coefficient requests faster placement relative to its base speed; lower requests slower placement.

**Check together with:** Fibre base speed limits; First fibre-layer geometry; Cooling and adhesion.

**Caution:** The effective speed may be limited elsewhere. Continuous-fibre anchoring is not equivalent to ordinary plastic first-layer tuning.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberFLSpeedCoeff`.

### Layer height - fiberFLThicknessMM

**Scope:** Process: fortified / FirstLayer; Process: general / FirstLayer; Process: reinforced / FirstLayer.

**What does it mean?** The layer height used for the first continuous-fibre layer.

**When would I change it?** Review when setting up the OEM fibre/matrix layer stack, not as a generic first-plastic-layer adjustment.

**What changes if I adjust it?** Changing the height alters strand accommodation and the volume/shape of matrix around it.

**Check together with:** First fibre-layer width; Matrix flow; Overall fibre layer schedule.

**Displayed units:** mm.

**Caution:** Do not infer a physically safe height from UI acceptance. Keep strand size and OEM layer requirements together.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberFLThicknessMM`.

### Max. ending speed - fiberFinishMaxSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The upper speed setting for ending a fibre path.

**When would I change it?** Change only within an OEM-supported continuous-fibre process after reviewing placement quality.

**What changes if I adjust it?** A higher ceiling may permit faster deposition; a lower ceiling limits it. It does not guarantee that speed will be reached.

**Check together with:** Related minimum speed and minimum-limit speed; Fibre feed and tension; Path curvature.

**Displayed units:** mm/s.

**Caution:** Keep the phase settings consistent. Strand handling and matrix delivery can limit speed independently.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberFinishMaxSpeed`.

### Min. ending speed limit - fiberFinishMinLimitSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** An additional minimum-speed limit for ending a fibre path, separate from the ordinary minimum-speed field.

**When would I change it?** Leave unchanged unless OEM documentation explains which limiting stage it controls.

**What changes if I adjust it?** Changing it may alter the lowest speed accepted by the fibre planner. The label alone does not establish when it takes precedence.

**Check together with:** Phase minimum and maximum speeds; Fibre speed coefficients.

**Displayed units:** mm/s.

**Caution:** High risk: do not guess the meaning of two similarly named minimum controls or bypass slowdown constraints.

**Evidence status:** Installed expert field confirmed; precedence and limiting-stage semantics unresolved. Control ID: `profile-settings:fiberFinishMinLimitSpeed`.

### Min. ending speed - fiberFinishMinSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The minimum-speed setting for ending a fibre path.

**When would I change it?** Review only as part of the corresponding fibre phase calibration.

**What changes if I adjust it?** Raising a minimum generally reduces how far that phase may slow; lowering permits slower operation. Exact interaction with the separate minimum-limit field is unresolved.

**Check together with:** Related maximum speed; Minimum-limit speed; Fibre geometry.

**Displayed units:** mm/s.

**Caution:** Do not make it equal to or above another limit merely to force speed. Preserve the OEM relationship.

**Evidence status:** Installed field and phase confirmed; exact combined speed-limit calculation unresolved. Control ID: `profile-settings:fiberFinishMinSpeed`.

### Max. arc segment length - fiberMaxArcSegmentLength

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** Limits the segment length used when representing continuous-fibre curves.

**When would I change it?** Review under an OEM fibre-path procedure when curved paths are too coarse or unnecessarily segmented.

**What changes if I adjust it?** Shorter segments generally represent curves more finely but increase path complexity; longer segments simplify them.

**Check together with:** Minimum arc radius; Arc fitting; Fibre feed and placement.

**Displayed units:** mm.

**Caution:** The label does not prove whether this is output G-code segmentation or an internal planning stage. Validate the resulting path.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberMaxArcSegmentLength`.

### Min. arc radius - fiberMinRadius

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The minimum arc-radius setting used in continuous-fibre path planning.

**When would I change it?** Change only with documented strand-bending constraints.

**What changes if I adjust it?** A larger minimum discourages tighter fibre turns; a smaller minimum permits tighter planned curves.

**Check together with:** Fibre curve segmentation; Path geometry; Strand material.

**Displayed units:** mm.

**Caution:** A permitted radius is not proof the strand can bend, adhere or remain undamaged at that radius.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberMinRadius`.

### Max. normal speed - fiberNormalMaxSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The upper speed setting for the main part of a fibre path.

**When would I change it?** Change only within an OEM-supported continuous-fibre process after reviewing placement quality.

**What changes if I adjust it?** A higher ceiling may permit faster deposition; a lower ceiling limits it. It does not guarantee that speed will be reached.

**Check together with:** Related minimum speed and minimum-limit speed; Fibre feed and tension; Path curvature.

**Displayed units:** mm/s.

**Caution:** Keep the phase settings consistent. Strand handling and matrix delivery can limit speed independently.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberNormalMaxSpeed`.

### Min. normal speed limit - fiberNormalMinLimitSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** An additional minimum-speed limit for the main part of a fibre path, separate from the ordinary minimum-speed field.

**When would I change it?** Leave unchanged unless OEM documentation explains which limiting stage it controls.

**What changes if I adjust it?** Changing it may alter the lowest speed accepted by the fibre planner. The label alone does not establish when it takes precedence.

**Check together with:** Phase minimum and maximum speeds; Fibre speed coefficients.

**Displayed units:** mm/s.

**Caution:** High risk: do not guess the meaning of two similarly named minimum controls or bypass slowdown constraints.

**Evidence status:** Installed expert field confirmed; precedence and limiting-stage semantics unresolved. Control ID: `profile-settings:fiberNormalMinLimitSpeed`.

### Min. normal speed - fiberNormalMinSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The minimum-speed setting for the main part of a fibre path.

**When would I change it?** Review only as part of the corresponding fibre phase calibration.

**What changes if I adjust it?** Raising a minimum generally reduces how far that phase may slow; lowering permits slower operation. Exact interaction with the separate minimum-limit field is unresolved.

**Check together with:** Related maximum speed; Minimum-limit speed; Fibre geometry.

**Displayed units:** mm/s.

**Caution:** Do not make it equal to or above another limit merely to force speed. Preserve the OEM relationship.

**Evidence status:** Installed field and phase confirmed; exact combined speed-limit calculation unresolved. Control ID: `profile-settings:fiberNormalMinSpeed`.

### Printing order - fiberPrintOrder

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** Chooses when continuous-fibre paths are printed relative to other path families.

**When would I change it?** Review when the validated reinforcement strategy requires a particular sequence.

**What changes if I adjust it?** Order changes which material is already present to support or surround the fibre and can change travel.

**Check together with:** Plastic outer-wall order; Layer structure; Fibre anchoring.

**Selectable choices:**

- **First in layer:** Places fibre paths before the other relevant paths in the layer. Verify that the required supporting matrix already exists. Schema contexts: Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.
- **Last in layer:** Places fibre paths after the other relevant paths in the layer, changing the surrounding material present during placement. Schema contexts: Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.
- **Before outer wall:** Places fibre before the outer plastic wall in the layer sequence; it is not necessarily the first operation. Schema contexts: Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**Caution:** Do not treat order as a cosmetic preference; reinforcement and matrix bonding depend on it.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberPrintOrder`.

### Slowing length - fiberSlowLength

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The length of the fibre path over which its ending slowdown is applied.

**When would I change it?** Change only when evaluating the OEM termination sequence.

**What changes if I adjust it?** A longer slowing region starts the transition earlier; a shorter region concentrates it nearer the end.

**Check together with:** Fibre ending speeds; Cut timing; After-cut plastic flow.

**Displayed units:** mm.

**Caution:** Keep slowing, cutting and remaining strand length coordinated; do not use an ordinary retraction recipe.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberSlowLength`.

### Start length - fiberStartLength

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The length assigned to the starting phase of a continuous-fibre path.

**When would I change it?** Change only as part of a documented start/anchoring test.

**What changes if I adjust it?** A longer starting phase applies start behavior over more path; a shorter phase transitions sooner to normal deposition.

**Check together with:** Fibre starting speeds; Fibre anchoring; Normal fibre speed.

**Displayed units:** mm.

**Caution:** This is a path-phase length, not evidence of a filament loading distance. Preserve OEM settings.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberStartLength`.

### Max. starting speed - fiberStartMaxSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The upper speed setting for starting a fibre path.

**When would I change it?** Change only within an OEM-supported continuous-fibre process after reviewing placement quality.

**What changes if I adjust it?** A higher ceiling may permit faster deposition; a lower ceiling limits it. It does not guarantee that speed will be reached.

**Check together with:** Related minimum speed and minimum-limit speed; Fibre feed and tension; Path curvature.

**Displayed units:** mm/s.

**Caution:** Keep the phase settings consistent. Strand handling and matrix delivery can limit speed independently.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberStartMaxSpeed`.

### Min. starting speed limit - fiberStartMinLimitSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** An additional minimum-speed limit for starting a fibre path, separate from the ordinary minimum-speed field.

**When would I change it?** Leave unchanged unless OEM documentation explains which limiting stage it controls.

**What changes if I adjust it?** Changing it may alter the lowest speed accepted by the fibre planner. The label alone does not establish when it takes precedence.

**Check together with:** Phase minimum and maximum speeds; Fibre speed coefficients.

**Displayed units:** mm/s.

**Caution:** High risk: do not guess the meaning of two similarly named minimum controls or bypass slowdown constraints.

**Evidence status:** Installed expert field confirmed; precedence and limiting-stage semantics unresolved. Control ID: `profile-settings:fiberStartMinLimitSpeed`.

### Min. starting speed - fiberStartMinSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The minimum-speed setting for starting a fibre path.

**When would I change it?** Review only as part of the corresponding fibre phase calibration.

**What changes if I adjust it?** Raising a minimum generally reduces how far that phase may slow; lowering permits slower operation. Exact interaction with the separate minimum-limit field is unresolved.

**Check together with:** Related maximum speed; Minimum-limit speed; Fibre geometry.

**Displayed units:** mm/s.

**Caution:** Do not make it equal to or above another limit merely to force speed. Preserve the OEM relationship.

**Evidence status:** Installed field and phase confirmed; exact combined speed-limit calculation unresolved. Control ID: `profile-settings:fiberStartMinSpeed`.

### Tension fiber feedrate - fiberTensionFeedrate

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The feedrate used during a continuous-fibre tensioning operation.

**When would I change it?** Leave at the OEM value unless a specific tension calibration procedure directs otherwise.

**What changes if I adjust it?** It changes how quickly fibre is fed during tension handling; this is not normal plastic extrusion speed.

**Check together with:** Tension length; Tension release fraction; Correction move.

**Displayed units:** %.

**Caution:** Too much or too little tension can disrupt the strand. The UI label does not establish a safe range.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:fiberTensionFeedrate`.

### Tension length - fiberTensionLength

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The length parameter used by the fibre tensioning sequence.

**When would I change it?** Change only under an OEM procedure with the strand path correctly assembled.

**What changes if I adjust it?** Changing it alters the amount of fibre movement associated with tension handling; exact direction depends on the sequence.

**Check together with:** Tension feedrate; Tension release fraction; Fibre loading and cutting.

**Displayed units:** mm.

**Caution:** Do not substitute an ordinary filament retract length or assume positive means pulling back.

**Evidence status:** Installed field confirmed; precise motion direction and sequence require OEM procedure. Control ID: `profile-settings:fiberTensionLength`.

### Tension release fraction - fiberTensionReleaseFraction

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** The fraction used to release tension in the continuous-fibre sequence.

**When would I change it?** Leave unchanged until the OEM procedure establishes the reference amount and intended adjustment.

**What changes if I adjust it?** A larger fraction ordinarily releases a larger share of the referenced tensioning movement; the exact reference is not established here.

**Check together with:** Tension length; Tension feedrate; Strand anchoring.

**Displayed units:** %.

**Caution:** This is not a generic flow percentage. The mechanical sequence must be understood before tuning.

**Evidence status:** Installed label confirmed; reference quantity and exact formula unresolved. Control ID: `profile-settings:fiberTensionReleaseFraction`.

### First layer height - flThickness

**Scope:** Process: general / FirstLayer; Process: reinforced / FirstLayer; Process: speedy / FirstLayer.

**What does it mean?** The height of the first model-printing layer.

**When would I change it?** Choose it for the selected nozzle, material and bed setup when establishing first-layer quality.

**What changes if I adjust it?** A thicker first layer changes bead shape and plastic volume; a thinner layer gives less vertical clearance and is more sensitive to bed/nozzle setup.

**Check together with:** First-layer width and flow; Bed/nozzle calibration; Later layer heights.

**Displayed units:** mm.

**Caution:** This is not a Z-offset correction. Do not use it to hide a physically incorrect nozzle-to-bed distance.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:flThickness`.

### Enable gap infill - gapFillEnabled

**Scope:** Process: general / GAP; Process: reinforced / GAP; Process: speedy / GAP.

**What does it mean?** Adds extrusion paths in narrow spaces left between other planned lines.

**When would I change it?** Enable when the preview shows small unfilled spaces that should be solid.

**What changes if I adjust it?** Enabled can fill otherwise missed gaps but adds short, sometimes slow paths.

**Check together with:** Gap fill flow ratio; Minimum gap fill length; Wall widths.

**Caution:** Gap fill cannot reproduce geometry smaller than the process can print reliably.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:gapFillEnabled`.

### Gap fill flow ratio - gapFillFlowRatio

**Scope:** Process: general / GAP; Process: reinforced / GAP; Process: speedy / GAP.

**What does it mean?** Scales plastic delivery on gap-filling paths.

**When would I change it?** Change when gap-fill lines are visibly overfilled or incomplete after general flow is correct.

**What changes if I adjust it?** Higher adds more plastic per gap-fill path; lower adds less.

**Check together with:** Gap fill width; Material flow; Gap fill speed.

**Displayed units:** %.

**Declared editor constraints:** {"displayMultiplier": 100}. These are not operating recommendations.

**Caution:** Do not use a local ratio to compensate for a general extrusion problem.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:gapFillFlowRatio`.

### Minimum gap fill length - gapFillMinLength

**Scope:** Process: general / GAP; Process: reinforced / GAP; Process: speedy / GAP.

**What does it mean?** The shortest gap-fill path retained by the slicer.

**When would I change it?** Increase when tiny gap-fill fragments create marks or needless starts; reduce when small gaps need filling.

**What changes if I adjust it?** A larger threshold removes more short segments; a smaller threshold preserves more detail and adds small paths.

**Check together with:** Gap fill enabled; Model details; Gap fill speed.

**Displayed units:** mm.

**Caution:** Removing short paths can leave real voids. Check the sliced layer, not only the model surface.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:gapFillMinLength`.

### Gap infill speed - gapFillSpeed

**Scope:** Process: general / GAP; Process: reinforced / GAP; Process: speedy / GAP.

**What does it mean?** The requested printing speed for narrow gap-fill paths.

**When would I change it?** Change when gap filling is unstable, poorly formed or unnecessarily slow.

**What changes if I adjust it?** Higher can save time but raises extrusion demand; lower gives more deposition time but can dwell on small features.

**Check together with:** Gap fill flow and width; Acceleration; Material capacity.

**Displayed units:** mm/s.

**Caution:** Short paths may never reach the requested speed.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:gapFillSpeed`.

### Width transition tolerance - gapFillWidthTransitionTolerance

**Scope:** Process: general / GAP; Process: reinforced / GAP; Process: speedy / GAP.

**What does it mean?** Controls the tolerance used when changing the width of gap-fill paths.

**When would I change it?** Review when variable-width gap fill changes too abruptly or creates excessive tiny transitions.

**What changes if I adjust it?** Changing the tolerance alters how width transitions are accepted or simplified; the exact direction is not established by this label.

**Check together with:** Gap fill line geometry; Minimum gap fill length; Wall widths.

**Displayed units:** mm.

**Caution:** Do not assume this is a dimensional-accuracy tolerance for the whole model.

**Evidence status:** Installed label confirmed; exact transition algorithm and numerical direction unresolved. Control ID: `profile-settings:gapFillWidthTransitionTolerance`.

### Generate brim - generateBrim

**Scope:** Process: general / BRIMSKIRT; Process: reinforced / BRIMSKIRT; Process: speedy / BRIMSKIRT.

**What does it mean?** Creates attached or closely spaced anchoring lines around the part's first layer.

**When would I change it?** Enable when edge lifting or a small contact footprint calls for extra bed attachment.

**What changes if I adjust it?** Enabled uses more bed area and material but can improve anchoring; disabled avoids brim cleanup.

**Check together with:** Brim loops; Distance from part; Brim in holes.

**Caution:** A brim does not replace correct bed preparation or a suitable first layer.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:generateBrim`.

### Generate brim in holes - generateBrimInHoles

**Scope:** Process: general / BRIMSKIRT; Process: reinforced / BRIMSKIRT; Process: speedy / BRIMSKIRT.

**What does it mean?** Allows brim lines inside openings in the first-layer footprint.

**When would I change it?** Enable when inner edges need anchoring; disable when clearing internal openings is difficult.

**What changes if I adjust it?** Enabled anchors eligible interior boundaries but adds material that must be removed from holes.

**Check together with:** Generate brim; Brim loops; Distance from part.

**Caution:** Inspect small holes before printing; internal brim can obstruct or become hard to remove.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:generateBrimInHoles`.

### Generate fiber infills - generateFiberInfill

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** Enables continuous-fibre paths inside the part.

**When would I change it?** Use only for a reinforcement strategy with verified fibre material, tooling and layer placement.

**What changes if I adjust it?** Enabled adds the selected reinforcement pattern and its strand-handling operations.

**Check together with:** Fibre infill pattern; Fibre perimeter generation; Matrix structure and layer layup.

**Caution:** Not a substitute for ordinary plastic infill. Fibre paths must be supported and compatible with the OEM process.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:generateFiberInfill`.

### Generate fiber perimeters - generateFiberPerimeters

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS; profile-settings.

**What does it mean?** Enables continuous-fibre reinforcement around part boundaries.

**When would I change it?** Use when the reinforcement design calls for fibre loops along contours.

**What changes if I adjust it?** Enabled adds fibre contour paths, changing strand continuity, material use and available interior space.

**Check together with:** Inner fibre loop count; Fibre infill; Matrix walls.

**Caution:** A fibre perimeter is not simply an extra plastic wall; tight curves, cuts and anchoring must remain valid.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:generateFiberPerimeters`.

### Build plate only - generateInternalSupport

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** The displayed 'Build plate only' switch restricts support to support that originates on the build plate.

**When would I change it?** Enable to avoid supports starting on the model; disable when support must also start on model surfaces.

**What changes if I adjust it?** Enabled can simplify removal but leaves some upper or enclosed overhangs without support.

**Check together with:** Enable support; Normal or tree support; Support placement.

**Caution:** The UI inverts the raw generateInternalSupport value. Follow the displayed switch meaning, not the internal field name.

**Evidence status:** Installed label and invertBoolean declaration confirmed; resulting support geometry requires preview. Control ID: `profile-settings:generateInternalSupport`.

### Generate skirt - generateSkirt

**Scope:** Process: general / BRIMSKIRT; Process: reinforced / BRIMSKIRT; Process: speedy / BRIMSKIRT.

**What does it mean?** Adds a separate outline around the first-layer area without attaching it to the part.

**When would I change it?** Enable for an early extrusion/first-layer check or priming path where the OEM workflow permits it.

**What changes if I adjust it?** Enabled consumes some bed area and material; it does not anchor the part like a brim.

**Check together with:** Skirt distance and loops; Brim; First-layer setup.

**Caution:** Do not confuse the skirt with a wipe tower or assume it replaces the machine's required start sequence.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:generateSkirt`.

### Enable support - generateSupport

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Enables generated structures beneath model areas that need support.

**When would I change it?** Enable when the chosen orientation has overhangs that cannot print reliably without it.

**What changes if I adjust it?** Enabled adds material and removal work; disabled leaves those areas to bridge or overhang unaided.

**Check together with:** Support type; Support generation mode; Build plate only.

**Caution:** Inspect support placement and clearances; this switch does not guarantee every difficult feature will print.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:generateSupport`.

### Generate bottom interface - generateSupportBottomInterface

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Adds a dedicated contact-interface region at the bottom side of support.

**When would I change it?** Enable when that contact needs a more controlled surface than the support body alone.

**What changes if I adjust it?** Enabled adds interface paths and can improve contact quality but may increase material use and bonding.

**Check together with:** Bottom interface spacing; Bottom Z distance; Support interface pattern.

**Caution:** An interface does not eliminate the need for a suitable separation gap and compatible material.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:generateSupportBottomInterface`.

### Generate top interface - generateSupportTopInterface

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Adds a dedicated contact-interface region at the top side of support.

**When would I change it?** Enable when that contact needs a more controlled surface than the support body alone.

**What changes if I adjust it?** Enabled adds interface paths and can improve contact quality but may increase material use and bonding.

**Check together with:** Top interface spacing; Top Z distance; Support interface pattern.

**Caution:** An interface does not eliminate the need for a suitable separation gap and compatible material.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:generateSupportTopInterface`.

### Generate wipe tower - generateWipeTower

**Scope:** Process: fortified / WIPETOWER; Process: general / WIPETOWER; Process: reinforced / WIPETOWER; Process: speedy / WIPETOWER.

**What does it mean?** Adds a separate structure used for wiping or material transition operations.

**When would I change it?** Use only when the selected multi-material/tool workflow requires it.

**What changes if I adjust it?** Enabled reserves space and consumes material to manage transitions away from the part.

**Check together with:** Tool/material sequence; Tower geometry; OEM start and transition routines.

**Caution:** A tower is not proof that routing or purge amounts are correct. It does not make an unqualified tool combination safe.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:generateWipeTower`.

### Holes expansion - holesExpansion

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** A dimensional compensation applied to holes rather than a change to the CAD model.

**When would I change it?** Consider after measuring a repeatable hole-size error with calibrated flow and machine setup.

**What changes if I adjust it?** It changes the sliced opening size; the sign convention must be confirmed in preview before choosing an amount.

**Check together with:** XY dimensional compensation; Wall widths; Flow calibration.

**Displayed units:** mm.

**Caution:** Do not assume positive enlarges the hole solely from the name. It cannot correct every orientation-dependent error.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:holesExpansion`.

### Infill/Wall overlap - infillExtendIntoPerimeterRatioPlasticCellular

**Scope:** Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL.

**What does it mean?** How far sparse plastic infill overlaps the neighboring wall region.

**When would I change it?** Adjust when infill separates from walls or creates ridges/bulges where it meets them.

**What changes if I adjust it?** More overlap can improve attachment but crowd the wall; less reduces crowding but may leave weak gaps.

**Check together with:** Plastic infill width; Wall width; Plastic flow.

**Caution:** Excess overlap is not a substitute for correct flow or printable line widths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillExtendIntoPerimeterRatioPlasticCellular`.

### Guide angle - infillFAnisogridFillAngle

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The guide orientation for the anisogrid continuous-fibre infill pattern.

**When would I change it?** Change when deliberately aligning reinforcement with the part's intended load directions.

**What changes if I adjust it?** Rotating the guide changes pattern orientation, not the material's intrinsic strength.

**Check together with:** Fibre infill pattern; Rib angles; Fibre density.

**Displayed units:** °.

**Caution:** Do not infer a tested structural rating from a direction setting; inspect the actual fibre paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFAnisogridFillAngle`.

### Fill density - infillFAnisogridFillDensity

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The requested density of the anisogrid continuous-fibre infill.

**When would I change it?** Change as part of a defined reinforcement design balancing material use and load paths.

**What changes if I adjust it?** Higher density generally places more fibre paths or closer ribs; lower leaves larger spaces.

**Check together with:** Fibre pattern angles; Path width; Matrix infill and available space.

**Displayed units:** %.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Strength does not scale automatically with the entered density; corners, anchoring and layer layup still matter.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFAnisogridFillDensity`.

### Anisogrid ribs crossing type - infillFAnisogridRibPlacement

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** Chooses where anisogrid fibre ribs cross in the pattern geometry.

**When would I change it?** Change only when comparing a deliberate anisogrid layout.

**What changes if I adjust it?** The choice relocates crossings and changes local reinforcement geometry rather than simply changing density.

**Check together with:** Anisogrid guide angle; Angle between main ribs; Fill density.

**Selectable choices:**

- **Near apex:** Places the anisogrid crossing nearer an apex of the pattern. It changes local rib junction placement; inspect the generated network. Schema contexts: Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.
- **Middle:** Places the anisogrid crossing toward the middle of the pattern region defined by its ribs. Inspect the resulting junctions. Schema contexts: Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**Caution:** Confirm the resulting crossings in preview; the names do not establish structural performance.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFAnisogridRibPlacement`.

### Angle between main ribs - infillFAnisogridRibsAngle

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The angle between the main rib directions of anisogrid fibre infill.

**When would I change it?** Change when choosing the directions that should carry reinforcement.

**What changes if I adjust it?** A different angle changes the shape and directional balance of the rib network.

**Check together with:** Guide angle; Fibre fill density; Part load directions.

**Displayed units:** °.

**Caution:** Do not treat larger angles as universally stronger; the intended loads and printable turns govern the choice.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFAnisogridRibsAngle`.

### Extrusion width - infillFCellularEWMM

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** The planned line width for cellular fibre infill.

**When would I change it?** Review only when the strand/matrix process calls for different line geometry.

**What changes if I adjust it?** Wider lines occupy more space and change neighboring path placement; narrower lines leave more space.

**Check together with:** Fibre feedrate; Matrix delivery; Fibre density or guide directions.

**Displayed units:** mm.

**Caution:** This is not the strand diameter. Do not apply ordinary plastic line-width advice without checking the OEM fibre process.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFCellularEWMM`.

### Infill extension into perimeters - infillFCellularExtendIntoPerimeters

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** The extension of cellular fibre infill into the surrounding perimeter region.

**When would I change it?** Change only to address a verified reinforcement-to-boundary connection issue.

**What changes if I adjust it?** More extension increases overlap at the boundary; less reduces crowding but can reduce connection.

**Check together with:** Fibre perimeters; Fibre line width; Matrix walls.

**Displayed units:** mm.

**Caution:** Fibre cannot be treated as freely flowing plastic; overlap must not produce invalid strand intersections or bends.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFCellularExtendIntoPerimeters`.

### Fiber feedrate - infillFCellularExtrusionFPercent

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** The fibre-feed percentage for cellular fibre infill, controlling strand delivery rather than ordinary matrix flow.

**When would I change it?** Use only with a documented fibre-feed calibration and correct strand path.

**What changes if I adjust it?** A higher percentage requests more fibre feed relative to its reference; lower requests less.

**Check together with:** Fibre compensation; Matrix extrusion; Path speed and tension.

**Displayed units:** %.

**Caution:** Do not use this to tune plastic bead fullness. The reference/feed calculation and safe range need OEM confirmation.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFCellularExtrusionFPercent`.

### Minimum line length - infillFCellularMinSegmentLength

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** The minimum line length retained for cellular fibre infill.

**When would I change it?** Review when the pattern creates short fibre fragments that are difficult to place or anchor.

**What changes if I adjust it?** A larger threshold suppresses more short paths; a smaller threshold permits more detail and more starts/cuts.

**Check together with:** Fibre pattern geometry; Start and finish lengths; Cut sequence.

**Displayed units:** mm.

**Caution:** Dropping paths can remove intended reinforcement. Check the actual strand layout, not just material totals.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFCellularMinSegmentLength`.

### Printing speed coefficient - infillFCellularSpeedCoeff

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** A multiplier for the printing speed of cellular fibre infill.

**When would I change it?** Change only after establishing the corresponding fibre-placement process.

**What changes if I adjust it?** Higher requests faster placement relative to the base speed; lower requests slower placement, subject to other limits.

**Check together with:** Fibre phase speed limits; Strand feed; Matrix flow.

**Caution:** It is not a volumetric-flow limit. Speed, strand handling and matrix supply must remain coordinated.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFCellularSpeedCoeff`.

### Guide angle - infillFIsogridFillAngle

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The guide orientation for the isogrid continuous-fibre infill pattern.

**When would I change it?** Change when deliberately aligning reinforcement with the part's intended load directions.

**What changes if I adjust it?** Rotating the guide changes pattern orientation, not the material's intrinsic strength.

**Check together with:** Fibre infill pattern; Rib angles; Fibre density.

**Displayed units:** °.

**Caution:** Do not infer a tested structural rating from a direction setting; inspect the actual fibre paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFIsogridFillAngle`.

### Fill density - infillFIsogridFillDensity

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The requested density of the isogrid continuous-fibre infill.

**When would I change it?** Change as part of a defined reinforcement design balancing material use and load paths.

**What changes if I adjust it?** Higher density generally places more fibre paths or closer ribs; lower leaves larger spaces.

**Check together with:** Fibre pattern angles; Path width; Matrix infill and available space.

**Displayed units:** %.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Strength does not scale automatically with the entered density; corners, anchoring and layer layup still matter.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFIsogridFillDensity`.

### Fill density - infillFRhombicFillDensity

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The requested density of the rhombic continuous-fibre infill.

**When would I change it?** Change as part of a defined reinforcement design balancing material use and load paths.

**What changes if I adjust it?** Higher density generally places more fibre paths or closer ribs; lower leaves larger spaces.

**Check together with:** Fibre pattern angles; Path width; Matrix infill and available space.

**Displayed units:** %.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Strength does not scale automatically with the entered density; corners, anchoring and layer layup still matter.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFRhombicFillDensity`.

### First rib angle - infillFRhombicFirstRibAngle

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The angle of the first rib family in rhombic continuous-fibre infill.

**When would I change it?** Change when aligning the two reinforcement directions with the part's intended loads.

**What changes if I adjust it?** Changing one angle alters the diamond-shaped network and its directional balance.

**Check together with:** Other rhombic rib angle; Rhombic density; Part orientation.

**Displayed units:** °.

**Caution:** Check both families together; a visually regular grid is not proof of validated reinforcement.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFRhombicFirstRibAngle`.

### Second rib angle - infillFRhombicSecondRibAngle

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The angle of the second rib family in rhombic continuous-fibre infill.

**When would I change it?** Change when aligning the two reinforcement directions with the part's intended loads.

**What changes if I adjust it?** Changing one angle alters the diamond-shaped network and its directional balance.

**Check together with:** Other rhombic rib angle; Rhombic density; Part orientation.

**Displayed units:** °.

**Caution:** Check both families together; a visually regular grid is not proof of validated reinforcement.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFRhombicSecondRibAngle`.

### Guide directions (°/°/°...) - infillFSolidAngleList

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** A slash-separated list of guide directions for solid continuous-fibre infill.

**When would I change it?** Use when the reinforcement plan specifies multiple fibre orientations.

**What changes if I adjust it?** Changing the angles changes the chosen reinforcement directions; changing their order may change the planned sequence.

**Check together with:** Solid fibre pattern; Layer layup; Fibre path geometry.

**Caution:** The label establishes the angle-list format, not precisely how the sequence repeats across layers. Confirm in preview before relying on a layup.

**Evidence status:** Installed angle-list field confirmed; layer-to-list scheduling not independently validated. Control ID: `profile-settings:infillFSolidAngleList`.

### Extrusion width - infillFSolidEW

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** The planned line width for solid fibre infill.

**When would I change it?** Review only when the strand/matrix process calls for different line geometry.

**What changes if I adjust it?** Wider lines occupy more space and change neighboring path placement; narrower lines leave more space.

**Check together with:** Fibre feedrate; Matrix delivery; Fibre density or guide directions.

**Displayed units:** mm.

**Caution:** This is not the strand diameter. Do not apply ordinary plastic line-width advice without checking the OEM fibre process.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFSolidEW`.

### Infill extension into perimeters - infillFSolidExtendIntoPerimeters

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** The extension of solid fibre infill into the surrounding perimeter region.

**When would I change it?** Change only to address a verified reinforcement-to-boundary connection issue.

**What changes if I adjust it?** More extension increases overlap at the boundary; less reduces crowding but can reduce connection.

**Check together with:** Fibre perimeters; Fibre line width; Matrix walls.

**Displayed units:** mm.

**Caution:** Fibre cannot be treated as freely flowing plastic; overlap must not produce invalid strand intersections or bends.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFSolidExtendIntoPerimeters`.

### Fiber feedrate - infillFSolidExtrusionFPercent

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** The fibre-feed percentage for solid fibre infill, controlling strand delivery rather than ordinary matrix flow.

**When would I change it?** Use only with a documented fibre-feed calibration and correct strand path.

**What changes if I adjust it?** A higher percentage requests more fibre feed relative to its reference; lower requests less.

**Check together with:** Fibre compensation; Matrix extrusion; Path speed and tension.

**Displayed units:** %.

**Caution:** Do not use this to tune plastic bead fullness. The reference/feed calculation and safe range need OEM confirmation.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFSolidExtrusionFPercent`.

### Minimum line length - infillFSolidMinSegmentLength

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** The minimum line length retained for solid fibre infill.

**When would I change it?** Review when the pattern creates short fibre fragments that are difficult to place or anchor.

**What changes if I adjust it?** A larger threshold suppresses more short paths; a smaller threshold permits more detail and more starts/cuts.

**Check together with:** Fibre pattern geometry; Start and finish lengths; Cut sequence.

**Displayed units:** mm.

**Caution:** Dropping paths can remove intended reinforcement. Check the actual strand layout, not just material totals.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFSolidMinSegmentLength`.

### Printing speed coefficient - infillFSolidSpeedCoeff

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL.

**What does it mean?** A multiplier for the printing speed of solid fibre infill.

**When would I change it?** Change only after establishing the corresponding fibre-placement process.

**What changes if I adjust it?** Higher requests faster placement relative to the base speed; lower requests slower placement, subject to other limits.

**Check together with:** Fibre phase speed limits; Strand feed; Matrix flow.

**Caution:** It is not a volumetric-flow limit. Speed, strand handling and matrix supply must remain coordinated.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFSolidSpeedCoeff`.

### Guide angle - infillFTetragridFillAngle

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The guide orientation for the tetragrid continuous-fibre infill pattern.

**When would I change it?** Change when deliberately aligning reinforcement with the part's intended load directions.

**What changes if I adjust it?** Rotating the guide changes pattern orientation, not the material's intrinsic strength.

**Check together with:** Fibre infill pattern; Rib angles; Fibre density.

**Displayed units:** °.

**Caution:** Do not infer a tested structural rating from a direction setting; inspect the actual fibre paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFTetragridFillAngle`.

### Fill density - infillFTetragridFillDensity

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The requested density of the tetragrid continuous-fibre infill.

**When would I change it?** Change as part of a defined reinforcement design balancing material use and load paths.

**What changes if I adjust it?** Higher density generally places more fibre paths or closer ribs; lower leaves larger spaces.

**Check together with:** Fibre pattern angles; Path width; Matrix infill and available space.

**Displayed units:** %.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Strength does not scale automatically with the entered density; corners, anchoring and layer layup still matter.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFTetragridFillDensity`.

### Angle between main ribs - infillFTetragridRibsAngle

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The angle between the main rib directions of tetragrid fibre infill.

**When would I change it?** Change when choosing the directions that should carry reinforcement.

**What changes if I adjust it?** A different angle changes the shape and directional balance of the rib network.

**Check together with:** Guide angle; Fibre fill density; Part load directions.

**Displayed units:** °.

**Caution:** Do not treat larger angles as universally stronger; the intended loads and printable turns govern the choice.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFTetragridRibsAngle`.

### Rib slope angle - infillFTetragridSideAngle

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** The side-rib slope angle in tetragrid fibre infill.

**When would I change it?** Adjust only when intentionally changing the tetragrid reinforcement geometry.

**What changes if I adjust it?** Changing the angle changes how the side ribs run relative to the rest of the network.

**Check together with:** Tetragrid guide angle; Angle between main ribs; Fill density.

**Displayed units:** °.

**Caution:** The label does not establish a mechanically validated angle; inspect the generated network.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFTetragridSideAngle`.

### Fiber infill pattern - infillFType

**Scope:** Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.

**What does it mean?** Selects the geometric pattern used for continuous-fibre infill.

**When would I change it?** Choose according to the reinforcement design rather than treating it as decorative plastic infill.

**What changes if I adjust it?** Different patterns create different rib directions, crossings, density distributions and continuous paths.

**Check together with:** Pattern-specific angles and density; Fibre perimeters; Matrix structure.

**Selectable choices:**

- **Solid:** Uses solid-style fibre filling along the configured guide directions, rather than an open cellular rib pattern. It does not prove a void-free printed composite. Schema contexts: Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.
- **Rhombic grid:** Uses two configured rib directions to form a diamond-like fibre network. The two angles control its directional layout. Schema contexts: Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.
- **Isogrid:** Uses an isogrid-style triangular rib network. Its guide angle and density set orientation and spacing; no structural rating is implied. Schema contexts: Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.
- **Anisogrid:** Uses a directionally arranged rib network with adjustable main-rib angles and crossing placement. It allows an intentionally unequal directional layout. Schema contexts: Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.
- **Tetragrid:** Uses the named multi-rib grid with separate main-rib and side-slope angle controls. Preview those ribs together; the label alone does not define a tested layup. Schema contexts: Process: fortified / REINFORCEDINFILL; Process: general / REINFORCEDINFILL; Process: reinforced / REINFORCEDINFILL; profile-settings.
- **Solid:** Uses solid-style fibre filling along the configured guide directions, rather than an open cellular rib pattern. It does not prove a void-free printed composite. Schema contexts: profile-settings.
- **Rhombic grid:** Uses two configured rib directions to form a diamond-like fibre network. The two angles control its directional layout. Schema contexts: profile-settings.
- **Isogrid:** Uses an isogrid-style triangular rib network. Its guide angle and density set orientation and spacing; no structural rating is implied. Schema contexts: profile-settings.
- **Anisogrid:** Uses a directionally arranged rib network with adjustable main-rib angles and crossing placement. It allows an intentionally unequal directional layout. Schema contexts: profile-settings.
- **Tetragrid:** Uses the named multi-rib grid with separate main-rib and side-slope angle controls. Preview those ribs together; the label alone does not define a tested layup. Schema contexts: profile-settings.

**Caution:** No listed pattern implies a load rating. Keep strand bending, anchoring and OEM process limits in scope.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillFType`.

### Extrusion width - infillPCellularEWMM

**Scope:** Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL.

**What does it mean?** Planned bead width for sparse plastic infill inside the part.

**When would I change it?** Adjust when adjacent lines fail to meet or the region cannot be filled cleanly.

**What changes if I adjust it?** Wider lines cover more space and require more plastic per distance; narrower lines fit finer details but may leave weak coverage.

**Check together with:** layer height; flow multiplier; nozzle geometry.

**Displayed units:** mm.

**Caution:** This is commanded line width, not physical nozzle diameter. Verify the sliced paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPCellularEWMM`.

### Flow multiplier - infillPCellularExtrusionMultP

**Scope:** Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL.

**What does it mean?** Scales plastic deposition for sparse plastic infill inside the part.

**When would I change it?** Use after the material's overall flow has been tuned, if this region alone remains overfilled or underfilled.

**What changes if I adjust it?** Higher values add plastic; lower values remove it without deliberately changing the model's dimensions.

**Check together with:** material flow; extrusion width; temperature.

**Caution:** Do not use a local multiplier to hide a blocked nozzle, moisture or wrong layer geometry.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPCellularExtrusionMultP`.

### Fill angle - infillPCellularFillAngle

**Scope:** Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.

**What does it mean?** Initial direction of fill lines for sparse plastic infill inside the part.

**When would I change it?** Change when line direction should suit a bridge span, surface appearance or load direction.

**What changes if I adjust it?** Rotates the pattern rather than making it denser; a different angle changes where lines meet walls.

**Check together with:** fill pattern; model orientation; angle increment.

**Displayed units:** °.

**Caution:** Patterns that are rotationally symmetric may respond differently. Confirm the selected region in Preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPCellularFillAngle`.

### Fill angle offset - infillPCellularFillAngleStep

**Scope:** Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.

**What does it mean?** Rotation added between successive fill layers for sparse plastic infill inside the part.

**When would I change it?** Change when consecutive layers should alternate directions rather than follow one orientation.

**What changes if I adjust it?** A larger step changes direction more per layer; zero requests no additional rotation.

**Check together with:** initial fill angle; fill pattern; layer schedule.

**Displayed units:** °.

**Caution:** This is an angular increment, not extra material or a pressure-advance setting.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPCellularFillAngleStep`.

### Fill density - infillPCellularFillDensity

**Scope:** Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.

**What does it mean?** The requested density of sparse plastic infill inside the part.

**When would I change it?** Increase when the interior needs more support or stiffness; reduce when material use and time matter more.

**What changes if I adjust it?** Higher density generally places lines closer together and uses more material; lower leaves larger voids.

**Check together with:** Plastic infill pattern; Top solid layers; Wall count.

**Displayed units:** %.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Strength is direction- and geometry-dependent; density alone is not a structural qualification.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPCellularFillDensity`.

### Fill pattern - infillPCellularFillType

**Scope:** Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.

**What does it mean?** Shape of the paths used for sparse plastic infill inside the part.

**When would I change it?** Choose for support, directionality, appearance and practical print time.

**What changes if I adjust it?** Different patterns redirect material and change intersections and travel; they do not guarantee equal strength at equal nominal density.

**Check together with:** fill angle; density or spacing; wall overlap.

**Selectable choices:**

- **Line:** Parallel straight fill paths. A simple directional fill; spacing and angle determine coverage. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Grid:** Crossing line families forming a grid. This gives connections in more than one direction but creates intersections. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Triangles:** Three-direction line families forming triangular cells. Intersections and orientation affect the resulting structure and print behavior. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Zigzag:** Back-and-forth fill joined where the geometry permits. It reduces separate line starts compared with disconnected lines. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Concentric:** Nested paths following the region's outline. Useful when following contours matters; inspect narrow centers and corners. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Honeycomb:** A cellular pattern based on hexagonal cells. It creates repeated cell walls rather than long parallel fill lines. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Tri-Hexagon:** A pattern combining triangular and hexagonal regions. It changes cell geometry compared with a simple grid or honeycomb. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Gyroid:** A smoothly varying three-dimensional periodic infill pattern. Layer shapes change through the height rather than repeating one flat grid. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **3D Honeycomb:** A honeycomb-style cellular structure that changes through the height. Inspect successive layers rather than judging it from one layer. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Cubic:** A three-dimensional, cube-derived lattice. Its cross-section changes with height and distributes paths across several directions. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Crosshatch:** A crossing-line hatch pattern. It changes the line arrangement and junction layout; compare the actual paths with Grid before choosing. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Diamond:** A diamond-type triply periodic surface pattern: a repeating curved three-dimensional structure, not ordinary diamond-shaped straight ribs. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **TPMS-FK:** The installed FK-named triply periodic surface option. It creates a repeating three-dimensional curved pattern; its exact parameterization is not established by the label. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Primitive:** The Primitive-named triply periodic surface pattern, a repeating three-dimensional cell-and-connection geometry. It is distinct from adding a primitive model object. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Neovius:** The Neovius-named triply periodic surface pattern. It offers a different repeating curved cell geometry; inspect channels and wall paths at the selected density. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Lidinoid:** The Lidinoid-named triply periodic surface pattern. It offers another repeating curved three-dimensional geometry; density alone does not establish its strength. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Hilbert Curve:** A winding, space-filling path with many right-angle turns. It produces a distinctive surface texture rather than a simple straight-line finish. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Archimedean Chords:** A curved, spiral-derived fill layout. It changes the direction and visual texture of the fill; inspect the actual clipped paths. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.
- **Octagram Spiral:** A star-like spiral fill layout. Its repeated turns give a distinctive path and surface pattern, not a guaranteed strength advantage. Schema contexts: Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL; profile-settings.

**Caution:** An available pattern is not necessarily appropriate for unsupported bridging or continuous fibre. Inspect its actual paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPCellularFillType`.

### Printing speed - infillPCellularSpeed

**Scope:** Process: general / CELLULARPLASTICINFILL; Process: reinforced / CELLULARPLASTICINFILL; Process: speedy / CELLULARPLASTICINFILL.

**What does it mean?** Requested printing speed for sparse plastic infill inside the part.

**When would I change it?** Change to balance that region's finish, bonding and print time.

**What changes if I adjust it?** Higher requests can shorten time but increase flow demand; lower requests can improve control but may increase heat exposure.

**Check together with:** volumetric capacity; acceleration; cooling.

**Displayed units:** mm/s.

**Caution:** Requested speed may be reduced by other limits. Preview and emitted output determine the actual schedule.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPCellularSpeed`.

### Extrusion line width - infillPMicroEWMM

**Scope:** Process: general / MICROPLASTICINFILL; Process: reinforced / MICROPLASTICINFILL; Process: speedy / MICROPLASTICINFILL.

**What does it mean?** Planned bead width for Rocket's micro plastic infill.

**When would I change it?** Adjust when adjacent lines fail to meet or the region cannot be filled cleanly.

**What changes if I adjust it?** Wider lines cover more space and require more plastic per distance; narrower lines fit finer details but may leave weak coverage.

**Check together with:** layer height; flow multiplier; nozzle geometry.

**Displayed units:** mm.

**Caution:** This is commanded line width, not physical nozzle diameter. Verify the sliced paths. The exact regions assigned to micro infill are not established by the field label; identify them in preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPMicroEWMM`.

### Flow multiplier - infillPMicroExtrusionMultP

**Scope:** Process: general / MICROPLASTICINFILL; Process: reinforced / MICROPLASTICINFILL; Process: speedy / MICROPLASTICINFILL.

**What does it mean?** Scales plastic deposition for Rocket's micro plastic infill.

**When would I change it?** Use after the material's overall flow has been tuned, if this region alone remains overfilled or underfilled.

**What changes if I adjust it?** Higher values add plastic; lower values remove it without deliberately changing the model's dimensions.

**Check together with:** material flow; extrusion width; temperature.

**Caution:** Do not use a local multiplier to hide a blocked nozzle, moisture or wrong layer geometry. The exact regions assigned to micro infill are not established by the field label; identify them in preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPMicroExtrusionMultP`.

### Fill angle - infillPMicroFillAngle

**Scope:** Process: general / MICROPLASTICINFILL; Process: reinforced / MICROPLASTICINFILL; Process: speedy / MICROPLASTICINFILL.

**What does it mean?** Initial direction of fill lines for Rocket's micro plastic infill.

**When would I change it?** Change when line direction should suit a bridge span, surface appearance or load direction.

**What changes if I adjust it?** Rotates the pattern rather than making it denser; a different angle changes where lines meet walls.

**Check together with:** fill pattern; model orientation; angle increment.

**Displayed units:** °.

**Caution:** Patterns that are rotationally symmetric may respond differently. Confirm the selected region in Preview. The exact regions assigned to micro infill are not established by the field label; identify them in preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPMicroFillAngle`.

### Fill pattern - infillPMicroFillPattern

**Scope:** Process: general / MICROPLASTICINFILL; Process: reinforced / MICROPLASTICINFILL; Process: speedy / MICROPLASTICINFILL.

**What does it mean?** Shape of the paths used for Rocket's micro plastic infill.

**When would I change it?** Choose for support, directionality, appearance and practical print time.

**What changes if I adjust it?** Different patterns redirect material and change intersections and travel; they do not guarantee equal strength at equal nominal density.

**Check together with:** fill angle; density or spacing; wall overlap.

**Selectable choices:**

- **Zigzag:** Back-and-forth fill joined where the geometry permits. It reduces separate line starts compared with disconnected lines. Schema contexts: Process: general / MICROPLASTICINFILL; Process: reinforced / MICROPLASTICINFILL; Process: speedy / MICROPLASTICINFILL.
- **Concentric:** Nested paths following the region's outline. Useful when following contours matters; inspect narrow centers and corners. Schema contexts: Process: general / MICROPLASTICINFILL; Process: reinforced / MICROPLASTICINFILL; Process: speedy / MICROPLASTICINFILL.

**Caution:** An available pattern is not necessarily appropriate for unsupported bridging or continuous fibre. Inspect its actual paths. The exact regions assigned to micro infill are not established by the field label; identify them in preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPMicroFillPattern`.

### Infill/Wall overlap - infillPMicroInfillExtendIntoPerimeterRatio

**Scope:** Process: general / MICROPLASTICINFILL; Process: reinforced / MICROPLASTICINFILL; Process: speedy / MICROPLASTICINFILL.

**What does it mean?** Overlap where Rocket's micro plastic infill meets surrounding walls.

**When would I change it?** Adjust when the fill-to-wall joint has gaps or causes visible wall bulges.

**What changes if I adjust it?** More overlap improves contact but can overpack the boundary; less overlap eases packing but may weaken the joint.

**Check together with:** wall width; fill width; flow.

**Caution:** Overlap is not a substitute for correct extrusion. Evaluate both the interior joint and the outside surface. The exact regions assigned to micro infill are not established by the field label; identify them in preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPMicroInfillExtendIntoPerimeterRatio`.

### Printing speed - infillPMicroSpeed

**Scope:** Process: general / MICROPLASTICINFILL; Process: reinforced / MICROPLASTICINFILL; Process: speedy / MICROPLASTICINFILL.

**What does it mean?** Requested printing speed for Rocket's micro plastic infill.

**When would I change it?** Change to balance that region's finish, bonding and print time.

**What changes if I adjust it?** Higher requests can shorten time but increase flow demand; lower requests can improve control but may increase heat exposure.

**Check together with:** volumetric capacity; acceleration; cooling.

**Displayed units:** mm/s.

**Caution:** Requested speed may be reduced by other limits. Preview and emitted output determine the actual schedule. The exact regions assigned to micro infill are not established by the field label; identify them in preview.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillPMicroSpeed`.

### Top/bottom solid layers count - infillPSolidBottomTopLayerCount

**Scope:** profile-settings.

**What does it mean?** The combined top/bottom solid-layer count exposed for a full-mask override.

**When would I change it?** Use when a full mask should change the solid skin around its affected region.

**What changes if I adjust it?** More solid layers generally create a thicker solid region at a given layer height; fewer reduce its material and coverage.

**Check together with:** Full mask; Process top and bottom solid counts; Layer height.

**Caution:** The installed declaration ties this control to Full mask. Inspect the affected region; do not assume it replaces every process-wide skin count.

**Evidence status:** Installed full-mask dependency confirmed; override interaction and emitted region require preview. Control ID: `profile-settings:infillPSolidBottomTopLayerCount`.

### Infill layer height - infillRatioToMacro

**Scope:** Process: fortified / LayerThickness; Process: general / LayerThickness; Process: reinforced / LayerThickness; Process: speedy / LayerThickness.

**What does it mean?** The displayed infill layer height, derived from the overall layer schedule.

**When would I change it?** Change when intentionally using a different vertical resolution for this path family.

**What changes if I adjust it?** A larger displayed height gives coarser layers and may reduce passes; a smaller displayed height gives finer layers and more passes.

**Check together with:** Macro layer height; Other path-family heights; Nozzle and material.

**Displayed units:** mm.

**Caution:** The UI formats an internal ratio as millimetres. Tune the displayed height, not the raw ratio, and verify layers remain compatible.

**Evidence status:** Installed millimetre label and macro-height formatting confirmed; emitted layer scheduling not validated. Control ID: `profile-settings:infillRatioToMacro`.

### Bottom solid - infillSBottomLayerCount

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** The number of solid layers used at the bottom of the plastic shell.

**When would I change it?** Change when the bottom surface lacks coverage or uses more material than needed.

**What changes if I adjust it?** More layers make a thicker solid region at a given layer height; fewer make it thinner.

**Check together with:** Layer height; Sparse infill support; Bottom skin flow and pattern.

**Displayed units:** layers.

**Caution:** A count is not a fixed physical thickness; layer-height changes alter the result.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillSBottomLayerCount`.

### Top solid - infillSTopLayerCount

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** The number of solid layers used at the top of the plastic shell.

**When would I change it?** Change when the top surface lacks coverage or uses more material than needed.

**What changes if I adjust it?** More layers make a thicker solid region at a given layer height; fewer make it thinner.

**Check together with:** Layer height; Sparse infill support; Top skin flow and pattern.

**Displayed units:** layers.

**Caution:** A count is not a fixed physical thickness; layer-height changes alter the result.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:infillSTopLayerCount`.

### Outer wall - inset0Count

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS; profile-settings.

**What does it mean?** The number of outer plastic wall loops.

**When would I change it?** Increase for a more substantial wall shell; reduce only when the part can tolerate a thinner shell.

**What changes if I adjust it?** More loops use more material and occupy more interior space; fewer leave a thinner shell.

**Check together with:** Outer wall line width; Inner and fibre walls; Part geometry.

**Displayed units:** loops.

**Caution:** More loops do not guarantee dimensions or strength; verify that thin features and intended infill still fit.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:inset0Count`.

### Outer wall extrusion width - inset0EWMM

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Planned bead width for outer plastic walls.

**When would I change it?** Adjust when adjacent lines fail to meet or the region cannot be filled cleanly.

**What changes if I adjust it?** Wider lines cover more space and require more plastic per distance; narrower lines fit finer details but may leave weak coverage.

**Check together with:** layer height; flow multiplier; nozzle geometry.

**Displayed units:** mm.

**Caution:** This is commanded line width, not physical nozzle diameter. Verify the sliced paths.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:inset0EWMM`.

### Flow multiplier - inset0ExtrusionMultP

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Scales plastic deposition for outer plastic walls.

**When would I change it?** Use after the material's overall flow has been tuned, if this region alone remains overfilled or underfilled.

**What changes if I adjust it?** Higher values add plastic; lower values remove it without deliberately changing the model's dimensions.

**Check together with:** material flow; extrusion width; temperature.

**Caution:** Do not use a local multiplier to hide a blocked nozzle, moisture or wrong layer geometry.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:inset0ExtrusionMultP`.

### Printing order - inset0PrintOrder

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Chooses whether the outer-wall sequence proceeds from the outside inward or from the inside outward.

**When would I change it?** Compare when exterior finish, dimensional consistency or overhang support needs attention.

**What changes if I adjust it?** The order changes which neighboring lines exist when a wall is laid down.

**Check together with:** Wall count; Overhangs; Fibre printing order.

**Selectable choices:**

- **Outside in:** Prints the outside wall first, then proceeds inward. This changes dimensional control and the support available beneath an overhanging outside line. Schema contexts: Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.
- **Inside out:** Prints inner wall paths before the outside wall. Existing inner lines may support the outside line but can also influence its final position. Schema contexts: Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**Caution:** No order is best for every shape. Inspect supported and unsupported outer contours separately.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:inset0PrintOrder`.

### Outer wall layer height - inset0RatioToMacro

**Scope:** Process: fortified / LayerThickness; Process: general / LayerThickness; Process: reinforced / LayerThickness; Process: speedy / LayerThickness.

**What does it mean?** The displayed outer wall layer height, derived from the overall layer schedule.

**When would I change it?** Change when intentionally using a different vertical resolution for this path family.

**What changes if I adjust it?** A larger displayed height gives coarser layers and may reduce passes; a smaller displayed height gives finer layers and more passes.

**Check together with:** Macro layer height; Other path-family heights; Nozzle and material.

**Displayed units:** mm.

**Caution:** The UI formats an internal ratio as millimetres. Tune the displayed height, not the raw ratio, and verify layers remain compatible.

**Evidence status:** Installed millimetre label and macro-height formatting confirmed; emitted layer scheduling not validated. Control ID: `profile-settings:inset0RatioToMacro`.

### Printing speed - inset0Speed

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Requested printing speed for outer plastic walls.

**When would I change it?** Change to balance that region's finish, bonding and print time.

**What changes if I adjust it?** Higher requests can shorten time but increase flow demand; lower requests can improve control but may increase heat exposure.

**Check together with:** volumetric capacity; acceleration; cooling.

**Displayed units:** mm/s.

**Caution:** Requested speed may be reduced by other limits. Preview and emitted output determine the actual schedule.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:inset0Speed`.

### F. Inner - insetFInnerCount

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS; profile-settings.

**What does it mean?** The number of inner continuous-fibre perimeter loops, shown as 'F. Inner'.

**When would I change it?** Change only when the reinforcement design calls for more or fewer inner contour loops.

**What changes if I adjust it?** More loops occupy more interior space and add fibre; fewer reduce contour reinforcement and material use.

**Check together with:** Generate fiber perimeters; Fibre line width; Matrix walls and fibre infill.

**Displayed units:** loops.

**Caution:** This is a fibre-loop count, not ordinary plastic wall count. Verify curves, anchoring and available space.

**Evidence status:** Installed field declaration; plain-language functional interpretation; emitted behavior not validated. Control ID: `profile-settings:insetFInnerCount`.

### F. Outer - insetFOuterCount

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS; profile-settings.

**What does it mean?** Number of continuous-fiber shell loops reinforcing the outside contour rather than holes.

**When would I change it?** Change when the outside surface needs a different reinforcement layout.

**What changes if I adjust it?** More loops reserve more room for fiber and add fiber use and print time; fewer leave more room for plastic and infill.

**Check together with:** Fiber shell generation; Inner fiber loops; Plastic shell counts; Minimum fiber perimeter length.

**Displayed units:** loops.

**Caution:** Requires the correct composite tool/material and a verified fiber path. This is not permission to run an empty or leaking fiber head.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetFOuterCount`.

### Fiber shell calculation order - insetXFCalcOrder

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Chooses whether fiber-shell paths are calculated from holes or from the outer contour first.

**When would I change it?** Use when competing fiber loops around holes and the outside need a different placement priority.

**What changes if I adjust it?** Holes first prioritizes hole-side shells; Contour first starts from the exterior. This concerns calculation priority, not a guaranteed visible print order.

**Check together with:** Fiber inner/outer counts; Available wall thickness; Fiber shell generation.

**Selectable choices:**

- **Holes first:** Prioritizes calculating the fiber shell from hole boundaries outward. Schema contexts: Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.
- **Contour first:** Prioritizes calculating the fiber shell from the outer contour inward. Schema contexts: Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**Caution:** Inspect the actual generated paths; narrow walls may not fit every requested loop.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXFCalcOrder`.

### Extrusion width - insetXFEWMM

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Requested laid-composite line width for fiber-shell paths.

**When would I change it?** Change only with evidence that the current composite line geometry needs adjustment.

**What changes if I adjust it?** A larger requested width changes path spacing and coverage; a smaller width packs paths more tightly.

**Check together with:** Composite layer height; Fiber feedrate; Fiber shell count; Contact-radius correction.

**Displayed units:** mm.

**Caution:** Requires the correct composite tool/material and a verified fiber path. This is not permission to run an empty or leaking fiber head. A width entry is a requested geometry, not proof that the nozzle/material can produce it reliably.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXFEWMM`.

### Fiber feedrate - insetXFExtrusionFPercent

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Fiber feed length expressed as a percentage of the planned path length.

**When would I change it?** Adjust only during a controlled fiber-layup calibration after feed mechanics are sound.

**What changes if I adjust it?** Installed help says reducing feed increases fiber tension; increasing feed reduces tension. It is not the plastic flow multiplier.

**Check together with:** Fiber drive mechanics; Composite speed; Fiber material; Path length and cutting.

**Displayed units:** %.

**Caution:** Requires the correct composite tool/material and a verified fiber path. This is not permission to run an empty or leaking fiber head. Excessive tension or slack can cause placement problems; no safe limit is established here.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXFExtrusionFPercent`.

### Printing speed coefficient - insetXFSpeedCoeff

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Multiplier applied to fiber printing speeds.

**When would I change it?** Use to scale fiber-path speeds without editing each speed separately.

**What changes if I adjust it?** Increasing it requests faster fiber motion; decreasing it requests slower motion. Other limits may still cap the result.

**Check together with:** Individual fiber speeds; Composite extrusion; Fiber feedrate; Acceleration.

**Caution:** Requires the correct composite tool/material and a verified fiber path. This is not permission to run an empty or leaking fiber head. A multiplier is not a verified throughput or pressure limit.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXFSpeedCoeff`.

### Plastic perimeters - insetXPCount

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS; profile-settings.

**What does it mean?** Number of plastic loops forming the internal plastic shell.

**When would I change it?** Change wall structure after base flow and dimensional behavior are stable.

**What changes if I adjust it?** More loops add shell thickness, material, and print time; fewer reduce them.

**Check together with:** Perimeter width; Plastic shell height; Fiber shell layout; Infill.

**Displayed units:** loops.

**Caution:** Counts may be limited by available geometry; verify the actual paths rather than assuming every loop fits.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXPCount`.

### Perimeter extrusion width - insetXPEWMM

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Requested extrusion width of plastic shell perimeters.

**When would I change it?** Use for a controlled wall-geometry adjustment, not as the first response to underextrusion.

**What changes if I adjust it?** Increasing width requests wider shell lines and usually greater volume per unit travel; decreasing requests narrower lines.

**Check together with:** Nozzle diameter; Perimeter count; Layer height; Flow multiplier; Speed.

**Displayed units:** mm.

**Caution:** A width entry is a requested geometry, not proof that the nozzle/material can produce it reliably.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXPEWMM`.

### Flow multiplier - insetXPExtrusionMultP

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Additional plastic-flow factor for plastic perimeters.

**When would I change it?** Change when only perimeter paths need a measured correction after the material flow is tuned.

**What changes if I adjust it?** It multiplies the material flow factor. Increasing adds commanded plastic for these paths; decreasing removes it.

**Check together with:** Material Flow multiplier; Perimeter width/height; Speed.

**Caution:** Do not use a feature multiplier to hide a clog, leak, incorrect filament diameter, or bad base flow calibration.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXPExtrusionMultP`.

### P. Inner - insetXPInnerWithFiberCount

**Scope:** Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS; profile-settings.

**What does it mean?** Number of plastic perimeters between the fiber shell and interior cellular infill.

**When would I change it?** Use to change plastic separation and bonding around the inner side of fiber reinforcement.

**What changes if I adjust it?** More loops thicken the plastic region inside fiber; fewer leave more room for infill.

**Check together with:** Fiber shell count; Infill; Perimeter width; Outer plastic count.

**Displayed units:** loops.

**Caution:** The short label 'P. Inner' is specific to the fiber-shell layout; it is not a different physical nozzle.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXPInnerWithFiberCount`.

### P. Outer - insetXPOuterWithFiberCount

**Scope:** Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS; profile-settings.

**What does it mean?** Number of plastic perimeters between the outside wall and the fiber shell.

**When would I change it?** Use to change the plastic cover surrounding fiber near the exterior.

**What changes if I adjust it?** More loops increase plastic cover and consume more wall space; fewer bring fiber closer to the outside.

**Check together with:** Outer-wall geometry; Fiber shell count; Perimeter width; Inner plastic count.

**Displayed units:** loops.

**Caution:** The short label 'P. Outer' describes position in the shell layout, not the tool ID.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXPOuterWithFiberCount`.

### Plastic perimeters layer height - insetXPRatioToMacro

**Scope:** Process: fortified / LayerThickness; Process: general / LayerThickness; Process: reinforced / LayerThickness; Process: speedy / LayerThickness.

**What does it mean?** Layer height used for the thicker internal plastic-perimeter shell within a macrolayer.

**When would I change it?** Change only while checking that the chosen shell height fits the macrolayer arrangement and the nozzle.

**What changes if I adjust it?** Increasing displayed height reduces the number of those shell layers; decreasing adds finer shell layers. The saved field is a ratio even though the editor presents height.

**Check together with:** Macrolayer height; Outer-wall height; Composite layers; Perimeter width.

**Displayed units:** mm.

**Caution:** Do not enter or transfer a raw ratio as though it were millimeters; use the displayed unit and inspect Z positions.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXPRatioToMacro`.

### Printing speed - insetXPSpeed

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Requested printing speed for plastic shell perimeters.

**When would I change it?** Change after flow and temperature are stable, using a wall-speed test.

**What changes if I adjust it?** Faster requests reduce time but raise required flow; slower requests reduce flow demand and may change finish.

**Check together with:** Perimeter width/height; Material throughput; Acceleration; Cooling.

**Displayed units:** mm/s.

**Caution:** The request may be limited by other rules. It does not prove safe nozzle pressure.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:insetXPSpeed`.

### Spiral vase mode - isSpiralVase

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Selects continuous spiral construction for a hollow, single-wall object.

**When would I change it?** Use only for a suitable vase-like part rather than a normal solid or reinforced part.

**What changes if I adjust it?** Enabled requests a continuously rising spiral wall; disabled keeps normal layer-based construction.

**Check together with:** Wall count; Top/bottom geometry; Model shape; Fiber and multi-material features.

**Caution:** Check Preview for the intended hollow result; enabling this is not a general strength or watertightness setting.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:isSpiralVase`.

### Macrolayer height - macroLayerHeight

**Scope:** Process: fortified / LayerThickness; Process: general / LayerThickness; Process: reinforced / LayerThickness; Process: speedy / LayerThickness.

**What does it mean?** Height of the repeated layer package containing the component microlayers.

**When would I change it?** Change when deliberately redesigning the relationship between outer walls, internal plastic, and composite layers.

**What changes if I adjust it?** A larger package changes how constituent layer heights line up; a smaller package changes that schedule in the opposite direction.

**Check together with:** Plastic-perimeter layer height; Outer-wall layer height; Composite layer height; Top/bottom skins.

**Displayed units:** mm.

**Caution:** This is not simply an ordinary slicer's single uniform layer-height field. Verify the entire layer schedule.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:macroLayerHeight`.

### Minimum layer print time - minLayerTimeForSlowing

**Scope:** Process: fortified / OTHER; Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Layer-duration threshold below which Rocket requests a print-speed slowdown.

**When would I change it?** Use when small layers do not have enough time to cool before the next layer.

**What changes if I adjust it?** Increasing the threshold applies slowdown to more short layers; decreasing it allows shorter layers without that slowdown.

**Check together with:** Minimum print speed; Cooling fans; Material; Feature speed.

**Displayed units:** s.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Slowdown cannot guarantee adequate cooling or repair heat-damaged geometry.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:minLayerTimeForSlowing`.

### Minimum print speed - minPrintSpeedForSlowDownAtShortPrintTimeLayer

**Scope:** Process: fortified / OTHER; Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Lowest speed allowed by the short-layer cooling slowdown.

**When would I change it?** Change when cooling slowdown becomes too slow or cannot slow enough for small features.

**What changes if I adjust it?** A higher minimum limits how much Rocket may slow down; a lower minimum permits slower motion.

**Check together with:** Minimum layer print time; Fans; Material; Overhang behavior.

**Displayed units:** mm/s.

**Caution:** Very slow motion is not automatically safer or cleaner; validate a small-feature test.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:minPrintSpeedForSlowDownAtShortPrintTimeLayer`.

### Minimum feature size - minimumFeatureSize

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Smallest feature the variable-width wall generator tries to preserve.

**When would I change it?** Change only when tiny features disappear or create unwanted short paths.

**What changes if I adjust it?** Increasing filters out more fine detail; decreasing asks the generator to keep smaller features.

**Check together with:** Variable-width wall generator; Minimum wall width; Model resolution.

**Displayed units:** %.

**Caution:** The slicer retaining a feature does not mean the nozzle can physically print it.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:minimumFeatureSize`.

### Minimum perimeter length - minimumPerimeterLength

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Minimum accepted length of one continuous-fiber perimeter.

**When would I change it?** Change only during an explicitly controlled short-fiber-contour investigation.

**What changes if I adjust it?** Increasing suppresses more short fiber loops; decreasing permits shorter loops.

**Check together with:** Fiber shell geometry; Minimum bend/cut behavior; Fiber placement.

**Displayed units:** mm.

**Caution:** Requires the correct composite tool/material and a verified fiber path. This is not permission to run an empty or leaking fiber head. Installed help warns that reducing it may cause short-contour layup problems.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:minimumPerimeterLength`.

### Minimum wall width - minimumWallWidth

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Lower width bound requested from the variable-width wall generator.

**When would I change it?** Use when thin-wall paths are too narrow or small features are omitted.

**What changes if I adjust it?** Increasing prevents narrower wall paths; decreasing lets the generator attempt narrower ones.

**Check together with:** Nozzle diameter; Minimum feature size; Wall transitions; Flow.

**Displayed units:** %.

**Caution:** A width entry is a requested geometry, not proof that the nozzle/material can produce it reliably.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:minimumWallWidth`.

### Fiber shell adaptive loops - mustGenerateFiberPerimeters

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** A switch labeled 'Fiber shell adaptive loops' under reinforced-perimeter generation.

**When would I change it?** Leave the reviewed value unless testing this specific fiber-shell algorithm.

**What changes if I adjust it?** The schema proves the switch and its dependency on fiber-perimeter generation, but does not establish precisely how enabling it adapts or forces loops.

**Check together with:** Generate fiber perimeters; Fiber shell counts; Available wall thickness.

**Caution:** The raw ID suggests 'must generate' while the visible label says adaptive loops. Do not infer the Boolean polarity or a no-fiber mode.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:mustGenerateFiberPerimeters`.

### Name - name

**Scope:** Machine/printer template / BasicInformation.

**What does it mean?** Human-readable name of the process/profile.

**When would I change it?** Change to identify machine, nozzle, material, purpose, and revision clearly.

**What changes if I adjust it?** Renaming improves selection and traceability; the name by itself does not alter the underlying print settings.

**Check together with:** Saved template; Selected process; Version.

**Caution:** A name containing TUNED, SAFE, or a nozzle size is not proof of validated values or the selected hardware.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:name`.

### Contact radius - nozzleContactRadius

**Scope:** Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** Composite-nozzle contact-surface radius used by trajectory correction.

**When would I change it?** Change only from measured tooling geometry or a controlled correction study.

**What changes if I adjust it?** Changing it alters the geometric correction applied to composite paths; it is not a filament-flow control.

**Check together with:** Composite trajectory correction; Nozzle geometry; Fiber paths.

**Displayed units:** mm.

**Caution:** Do not substitute nozzle-hole diameter for contact-surface radius. Incorrect geometry can misplace paths.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:nozzleContactRadius`.

### Extended contact radius - nozzleContactRadiusExtended

**Scope:** Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** Composite contact radius used for the trajectory after a fiber cut.

**When would I change it?** Change only when the post-cut correction geometry is understood and measured.

**What changes if I adjust it?** Changing it modifies post-cut path correction, rather than the normal plastic flow.

**Check together with:** Normal contact radius; Fiber cutting; Composite trajectory correction.

**Displayed units:** mm.

**Caution:** This is not a clearance or leak-prevention command. Keep the actual nozzle geometry and cutting sequence in view.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:nozzleContactRadiusExtended`.

### Support interface pattern - organicTreeInterfaceSupportInfillType

**Scope:** Process: general / SUPPORT.

**What does it mean?** Pattern used in tree-support contact-interface layers.

**When would I change it?** Change to compare interface coverage, path continuity, and removal.

**What changes if I adjust it?** The schema offers Zigzag, Grid, Line, and Concentric patterns; pattern choice changes the contact paths, not their validated flow.

**Check together with:** Interface spacing; Interface angles; Top/bottom layer count.

**Selectable choices:**

- **Zigzag:** Back-and-forth fill with a zigzag layout; check how its turns and connections are generated. Schema contexts: Process: general / SUPPORT.
- **Grid:** Intersecting line families forming a grid; crossings change local path overlap. Schema contexts: Process: general / SUPPORT.
- **Line:** Parallel line paths; compare line direction and boundary connections in Preview. Schema contexts: Process: general / SUPPORT.
- **Concentric:** Nested loops following the region boundary; ordinary fill-angle settings generally do not apply. Schema contexts: Process: general / SUPPORT.

**Caution:** Angles do not apply to every pattern. Choose from the active mode's actual list, not broader help text.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeInterfaceSupportInfillType`.

### Automatically calculate tree support brim - organicTreeSupportAutoBrim

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Automatically determines a tree-support brim from the root geometry and support height.

**When would I change it?** Use automatic brim sizing unless a measured adhesion case calls for explicit manual width.

**What changes if I adjust it?** Enabled calculates brim size; disabled makes the separate manual brim width relevant.

**Check together with:** Tree roots; Support height; Manual tree brim width.

**Caution:** Automatic sizing does not prove adhesion or plate fit; inspect the full footprint.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportAutoBrim`.

### Body fill angle - organicTreeSupportBodyFillAngle

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Starting angle of the internal tree-body fill.

**When would I change it?** Change to orient non-hollow body fill.

**What changes if I adjust it?** It rotates internal fill; hollow bodies do not use it.

**Check together with:** Tree body pattern; Body angle step; Body fill density.

**Displayed units:** °.

**Caution:** This does not rotate the whole support tree.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBodyFillAngle`.

### Body angle step - organicTreeSupportBodyFillAngleStep

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Layer-to-layer change in the tree-body fill angle.

**When would I change it?** Use when changing the alternating orientation of the tree's internal fill.

**What changes if I adjust it?** A different step changes orientation between layers rather than fill amount.

**Check together with:** Tree body pattern; Starting body angle.

**Displayed units:** °.

**Caution:** Installed help says hollow and honeycomb bodies do not use this setting.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBodyFillAngleStep`.

### Body fill density - organicTreeSupportBodyFillDensity

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Density of internal fill in a non-hollow tree-support body.

**When would I change it?** Use when tree bodies need a different material/stability tradeoff.

**What changes if I adjust it?** Higher density requests more internal structure and material; lower density leaves a more open body.

**Check together with:** Tree body pattern; Branch diameter; Wall count.

**Displayed units:** %.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Hollow bodies do not use internal fill. More material does not guarantee a stable tall support.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBodyFillDensity`.

### Tree body fill pattern - organicTreeSupportBodyInfillType

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Internal construction pattern of the tree-support body.

**When would I change it?** Change to compare hollow walls with filled support bodies.

**What changes if I adjust it?** Hollow uses only the shell; the other listed choices add patterned internal fill.

**Check together with:** Body fill density; Body angles; Wall count; Branch geometry.

**Selectable choices:**

- **Hollow:** No internal tree-body infill; the body's walls form the support shell. Schema contexts: Process: general / SUPPORT.
- **Line:** Parallel line paths; compare line direction and boundary connections in Preview. Schema contexts: Process: general / SUPPORT.
- **Grid:** Intersecting line families forming a grid; crossings change local path overlap. Schema contexts: Process: general / SUPPORT.
- **Zigzag:** Back-and-forth fill with a zigzag layout; check how its turns and connections are generated. Schema contexts: Process: general / SUPPORT.
- **Honeycomb:** A repeating honeycomb-style internal structure; inspect how much of it fits inside the tree. Schema contexts: Process: general / SUPPORT.

**Caution:** Inspect small branches; the requested pattern may not fit in every cross-section.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBodyInfillType`.

### Bottom interface - organicTreeSupportBottomInterfaceLayerCount

**Scope:** Process: general / SUPPORT.

**What does it mean?** Number of bottom support-interface macrolayers, not a simple on/off switch.

**When would I change it?** Change when the bottom contact region needs a different thickness or removal behavior.

**What changes if I adjust it?** More selected layers create a thicker contact region; zero requests none. Follow top inherits the top-interface layer count.

**Check together with:** Macrolayer height; Interface spacing; Top/bottom Z clearances.

**Displayed units:** layers.

**Selectable choices:**

- **Follow top:** Uses the top-interface layer count for the bottom interface. Schema contexts: Process: general / SUPPORT.
- **0:** Requests no interface macrolayers for this side. Schema contexts: Process: general / SUPPORT.
- **1:** Requests 1 interface macrolayer for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.
- **2:** Requests 2 interface macrolayers for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.
- **3:** Requests 3 interface macrolayers for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.

**Caution:** Some installed help uses old 'flag' wording, but this schema is a layer-count selector. Verify the actual layer count in Preview.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBottomInterfaceLayerCount`.

### Bottom interface spacing - organicTreeSupportBottomInterfaceSpacing

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Gap between adjacent lines in the bottom support interface.

**When would I change it?** Change to balance contact coverage against separation at the support's underside.

**What changes if I adjust it?** Larger spacing leaves more open contact paths; smaller spacing makes them denser.

**Check together with:** Bottom-interface layer count; Bottom Z distance; Interface line width/flow.

**Displayed units:** mm.

**Caution:** This is in-plane line spacing, not vertical clearance or a fill percentage.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBottomInterfaceSpacing`.

### Bottom Z distance - organicTreeSupportBottomZDistance

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Vertical gap between the support's underside and the model surface below it.

**When would I change it?** Use when supports begin on model surfaces and adhere too firmly or too weakly.

**What changes if I adjust it?** Increasing generally eases separation but weakens the support start; decreasing increases proximity/contact.

**Check together with:** Bottom interface; Support/model XY gap; Model layer schedule.

**Displayed units:** mm.

**Caution:** This is not the gap under the supported overhang; that is the top Z distance.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBottomZDistance`.

### Organic branch angle - organicTreeSupportBranchAngle

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Limit on how much the support branches may tilt while growing sideways.

**When would I change it?** Use when branches cannot reach an overhang or take an unsuitable route.

**What changes if I adjust it?** Larger values permit more lateral reach over a given height; smaller values keep branches more upright.

**Check together with:** Branch spacing; Branch diameter; Model collision avoidance.

**Displayed units:** °.

**Caution:** Permitted tilt is not proof a branch can print unsupported; inspect the whole route.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBranchAngle`.

### Organic branch diameter - organicTreeSupportBranchDiameter

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Reference diameter of tree-support branches.

**When would I change it?** Change when supports are too fragile or consume excessive material.

**What changes if I adjust it?** Larger branches generally improve stability at a material/time cost; smaller branches reduce material but can be fragile.

**Check together with:** Branch spacing; Diameter growth angle; Wall/fill structure.

**Displayed units:** mm.

**Caution:** A diameter request cannot cure poor first-layer adhesion or a collision.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBranchDiameter`.

### Branch diameter angle - organicTreeSupportBranchDiameterAngle

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Controls how rapidly branches thicken toward their roots.

**When would I change it?** Use when trunks need a different growth/stability profile.

**What changes if I adjust it?** Changing it alters rootward thickening and material use; judge the resulting shape rather than treating it as a printing speed.

**Check together with:** Branch diameter; Tree height; Branch tilt.

**Displayed units:** °.

**Caution:** The UI/help identifies the purpose, not a universal safe angle for every tree.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBranchDiameterAngle`.

### Organic branch distance - organicTreeSupportBranchDistance

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Target spacing between neighboring support branches.

**When would I change it?** Change when support contacts are too sparse or trees are unnecessarily dense.

**What changes if I adjust it?** Smaller spacing requests more densely placed branches; larger spacing requests fewer.

**Check together with:** Top contact regions; Tip diameter; Branch diameter.

**Displayed units:** mm.

**Caution:** Spacing is a target constrained by model clearance and the planner.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBranchDistance`.

### Tree support brim width - organicTreeSupportBrimWidth

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Manual width of the tree-support brim when automatic brim sizing is off.

**When would I change it?** Use for a specific support-root adhesion/plate-space adjustment.

**What changes if I adjust it?** Wider gives a larger bed attachment; narrower uses less plate area. Installed help describes zero as no brim.

**Check together with:** Automatic tree brim; Root geometry; Plate layout.

**Displayed units:** mm.

**Caution:** This is the tree-support brim, not the model brim; keep both within the plate.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportBrimWidth`.

### Organic support expansion - organicTreeSupportExpansion

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Horizontal expansion of the tree-support overhang contact region.

**When would I change it?** Use to change the footprint of regions that tree supports must reach.

**What changes if I adjust it?** Increasing the nonnegative expansion grows contact regions subject to model-collision limits; it does not increase branch diameter.

**Check together with:** Top contact density; Model collision avoidance; Support/model clearance.

**Displayed units:** mm.

**Caution:** Current help describes nonnegative values for this tree expansion; do not transfer signed conventional-support offset behavior.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportExpansion`.

### Interface fill angle - organicTreeSupportInterfaceFillAngle

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Direction of the first support-interface fill layer.

**When would I change it?** Change to orient the interface contact paths.

**What changes if I adjust it?** It rotates applicable interface lines without directly changing their spacing.

**Check together with:** Interface pattern; Interface angle step; Top/bottom interfaces.

**Displayed units:** °.

**Caution:** Concentric interface paths do not use the angle according to installed help.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportInterfaceFillAngle`.

### Interface angle step - organicTreeSupportInterfaceFillAngleStep

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Change of support-interface fill angle between adjacent interface layers.

**When would I change it?** Use to control layer-to-layer rotation within contact layers.

**What changes if I adjust it?** Different steps change line orientation rather than interface thickness.

**Check together with:** Initial interface angle; Interface pattern; Interface layer count.

**Displayed units:** °.

**Caution:** Concentric fill does not use this angle step.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportInterfaceFillAngleStep`.

### Tree support generation mode - organicTreeSupportMode

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Selects the source of regions that generate tree supports.

**When would I change it?** Choose based on whether you want automatic detection, manual regions, or both.

**What changes if I adjust it?** Auto uses detected overhangs; Manual uses manually specified regions; Hybrid combines the two.

**Check together with:** Manual support painting/regions; Automatic threshold; Support filtering.

**Selectable choices:**

- **Auto:** Uses automatically detected overhang regions. Schema contexts: Process: general / SUPPORT.
- **Manual:** Uses manually specified support regions only. Schema contexts: Process: general / SUPPORT.
- **Hybrid:** Combines automatic overhang regions and manually specified regions. Schema contexts: Process: general / SUPPORT.

**Caution:** Manual mode does not automatically rescue unmarked overhangs; inspect every unsupported area.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportMode`.

### Preferred branch angle - organicTreeSupportPreferredBranchAngle

**Scope:** Process: general / SUPPORT.

**What does it mean?** Branch tilt preferred by the Organic support planner.

**When would I change it?** Use to influence Organic tree shape after the maximum branch angle is set.

**What changes if I adjust it?** Changes the planner's preferred route; it can still adjust within the allowed maximum.

**Check together with:** Maximum Organic branch angle; Model avoidance; Branch spacing.

**Displayed units:** °.

**Caution:** Preferred does not mean mandatory; inspect the generated branches.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportPreferredBranchAngle`.

### Organic tip diameter - organicTreeSupportTipDiameter

**Scope:** Process: general / SUPPORT.

**What does it mean?** Diameter near an Organic branch's upper contact with its supported region.

**When would I change it?** Use when contacts break too easily or are difficult to remove.

**What changes if I adjust it?** Smaller tips can separate more easily; larger tips give more support/contact.

**Check together with:** Organic top density; Top interface; Branch diameter.

**Displayed units:** mm.

**Caution:** A tiny tip is not necessarily printable or sufficient to hold the overhang.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportTipDiameter`.

### Organic top density - organicTreeSupportTopDensity

**Scope:** Process: general / SUPPORT.

**What does it mean?** Density of Organic branches near the supported surface.

**When would I change it?** Use when overhang coverage is insufficient or removal is too difficult.

**What changes if I adjust it?** Higher density can increase support coverage and material; lower density makes the contact region sparser.

**Check together with:** Organic tip diameter; Interface pattern/spacing; Overhang regions.

**Displayed units:** %.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** This is not the same control as internal tree-body fill density.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportTopDensity`.

### Top interface - organicTreeSupportTopInterfaceLayerCount

**Scope:** Process: general / SUPPORT.

**What does it mean?** Number of top support-interface macrolayers, not a simple on/off switch.

**When would I change it?** Change when the top contact region needs a different thickness or removal behavior.

**What changes if I adjust it?** More selected layers create a thicker contact region; zero requests none.

**Check together with:** Macrolayer height; Interface spacing; Top/bottom Z clearances.

**Displayed units:** layers.

**Selectable choices:**

- **0:** Requests no interface macrolayers for this side. Schema contexts: Process: general / SUPPORT.
- **1:** Requests 1 interface macrolayer for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.
- **2:** Requests 2 interface macrolayers for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.
- **3:** Requests 3 interface macrolayers for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.

**Caution:** Some installed help uses old 'flag' wording, but this schema is a layer-count selector. Verify the actual layer count in Preview.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportTopInterfaceLayerCount`.

### Top interface spacing - organicTreeSupportTopInterfaceSpacing

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Gap between neighboring lines at the top support interface.

**When would I change it?** Use to balance supported-surface quality against removal effort.

**What changes if I adjust it?** Larger spacing makes the interface more open; smaller spacing adds contact coverage.

**Check together with:** Top-interface layers; Top Z distance; Interface line width/flow.

**Displayed units:** mm.

**Caution:** This is millimeter line spacing, not vertical separation or percent fill.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportTopInterfaceSpacing`.

### Top Z distance - organicTreeSupportTopZDistance

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Vertical clearance between the support top and the model above it.

**When would I change it?** Use when overhang undersides are too rough or supports bond too strongly.

**What changes if I adjust it?** Increasing usually aids removal but gives less support; decreasing moves the support closer.

**Check together with:** Top-interface spacing/layers; Model/support layer schedule.

**Displayed units:** mm.

**Caution:** The achievable gap is affected by layers; verify the actual sliced contact rather than just the input number.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportTopZDistance`.

### Tree body wall - organicTreeSupportWallCount

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Number of wall loops around each tree-support cross-section.

**When would I change it?** Change when support branches need a different shell strength/material tradeoff.

**What changes if I adjust it?** Auto chooses from the supported wall counts; 1 or 2 requests that many loops where the cross-section has space.

**Check together with:** Branch diameter; Body fill pattern; Line width.

**Displayed units:** loops.

**Selectable choices:**

- **Auto:** Rocket chooses one or two wall loops from the cross-section geometry. Schema contexts: Process: general / SUPPORT.
- **1:** Requests one wall loop around each suitable support cross-section. Schema contexts: Process: general / SUPPORT.
- **2:** Requests two wall loops where sufficient cross-section space exists. Schema contexts: Process: general / SUPPORT.

**Caution:** This is not a vertical layer count. A second loop only appears where the geometry can fit it.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportWallCount`.

### Support/model XY distance - organicTreeSupportXYDistance

**Scope:** Process: general / SUPPORT.

**What does it mean?** Organic variant: Horizontal distance between tree supports and the model.

**When would I change it?** Use to reduce sidewall bonding or recover support near a boundary.

**What changes if I adjust it?** Larger clearance reduces side contact and available support area; smaller clearance brings branches closer.

**Check together with:** Tree expansion; Branch routing; Top/bottom Z distances.

**Displayed units:** mm.

**Caution:** It does not change vertical contact gaps. Inspect collision avoidance and overhang support together.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:organicTreeSupportXYDistance`.

### Outer contour expansion - outerContourExpansion

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** XY offset applied to the part's outside contour for dimensional correction.

**When would I change it?** Use after flow is calibrated and measured outside dimensions show a repeatable offset.

**What changes if I adjust it?** Positive values enlarge the outside contour; negative values shrink it.

**Check together with:** Hole expansion settings; Material shrinkage; Flow; Model dimensions.

**Displayed units:** mm.

**Caution:** This changes contour dimensions, not overall scaling; verify holes and thin walls separately.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:outerContourExpansion`.

### Extrusion width - overhangEWMM

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Requested line width for overhang infill.

**When would I change it?** Change to tune the path geometry after the material's base flow is sound.

**What changes if I adjust it?** Larger width asks for wider lines and more volume per unit path; smaller width requests narrower lines.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Displayed units:** mm.

**Caution:** The requested width is not proof the nozzle can deliver it.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:overhangEWMM`.

### Flow multiplier - overhangExtrusionMultP

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Additional flow factor for overhang infill.

**When would I change it?** Change only when these paths alone need a measured flow correction.

**What changes if I adjust it?** It multiplies the material flow factor; increasing adds commanded plastic to these paths and decreasing reduces it.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Caution:** Do not compensate for a clog, leak, or incorrect base material flow with a feature multiplier.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:overhangExtrusionMultP`.

### Fill angle - overhangInfillAngle

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Starting direction of fill lines for overhang infill.

**When would I change it?** Change to orient the fill relative to the shape or desired surface appearance.

**What changes if I adjust it?** It rotates applicable fill paths; it does not directly alter fill amount.

**Check together with:** Fill pattern; Angle step where available; Perimeter contact.

**Displayed units:** °.

**Caution:** Concentric paths do not use this angle according to installed help.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:overhangInfillAngle`.

### Infill/Wall overlap - overhangInfillExtendIntoPerimeterRatio

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Fraction of line width by which overhang infill overlaps the surrounding perimeters.

**When would I change it?** Use when the skin-to-wall bond is incomplete or the boundary is excessively crowded.

**What changes if I adjust it?** Increasing grows the overlap; decreasing reduces intrusion into the perimeter region.

**Check together with:** Line width; Perimeter geometry; Material and feature flow.

**Caution:** This is a ratio, not millimeters or a direct percentage entry. Excess overlap can cause ridges.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:overhangInfillExtendIntoPerimeterRatio`.

### Fill pattern - overhangInfillPattern

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Layout used to fill overhang infill.

**When would I change it?** Change to compare surface appearance, path continuity, and print time.

**What changes if I adjust it?** Each listed pattern creates a different path shape; it is not an automatic change in validated flow or strength.

**Check together with:** Fill angle; Layer schedule; Line width; Preview.

**Selectable choices:**

- **Line:** Parallel line paths; compare line direction and boundary connections in Preview. Schema contexts: Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.
- **Zigzag:** Back-and-forth fill with a zigzag layout; check how its turns and connections are generated. Schema contexts: Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.
- **Concentric:** Nested loops following the region boundary; ordinary fill-angle settings generally do not apply. Schema contexts: Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**Caution:** Choose only options actually offered in the active mode; broader help text is not proof all patterns appear everywhere.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:overhangInfillPattern`.

### Printing speed - overhangSpeed

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Requested print speed for overhang infill.

**When would I change it?** Change after temperature and flow are stable using a controlled feature-speed test.

**What changes if I adjust it?** Increasing raises motion and extrusion demand; decreasing reduces it and changes time/heat exposure.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Displayed units:** mm/s.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Other limits can reduce actual speed. No safe throughput or pressure limit follows from this setting.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:overhangSpeed`.

### Override correction move speed - overrideCorrectionSegmentSpeed

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** Allows a separate speed for composite trajectory-correction travel segments.

**When would I change it?** Use only when investigating the correction motion with a known-good composite path.

**What changes if I adjust it?** Enabled uses the separate correction-speed setting; disabled follows the associated print-move speed.

**Check together with:** Correction-segment speed; Composite path speed; Contact radii.

**Caution:** It changes correction motion, not a guaranteed overall travel cap. Validate emitted correction segments.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:overrideCorrectionSegmentSpeed`.

### 100 % overhang speed - percent100OverhangSpeed

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Requested print speed for the 100% overhang category.

**When would I change it?** Change when that category of overhang needs a measured speed adjustment.

**What changes if I adjust it?** A lower requested speed can improve difficult overhangs; a higher one raises motion/flow demand.

**Check together with:** Overhang classification; Other overhang speed categories; Fans; Line width and height.

**Displayed units:** mm/s.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Do not assume what the percentage measures without checking Rocket's classification/Preview; these are not fan percentages.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:percent100OverhangSpeed`.

### 10 % overhang speed - percent10OverhangSpeed

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Requested print speed for the 10% overhang category.

**When would I change it?** Change when that category of overhang needs a measured speed adjustment.

**What changes if I adjust it?** A lower requested speed can improve difficult overhangs; a higher one raises motion/flow demand.

**Check together with:** Overhang classification; Other overhang speed categories; Fans; Line width and height.

**Displayed units:** mm/s.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Do not assume what the percentage measures without checking Rocket's classification/Preview; these are not fan percentages.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:percent10OverhangSpeed`.

### 25 % overhang speed - percent25OverhangSpeed

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Requested print speed for the 25% overhang category.

**When would I change it?** Change when that category of overhang needs a measured speed adjustment.

**What changes if I adjust it?** A lower requested speed can improve difficult overhangs; a higher one raises motion/flow demand.

**Check together with:** Overhang classification; Other overhang speed categories; Fans; Line width and height.

**Displayed units:** mm/s.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Do not assume what the percentage measures without checking Rocket's classification/Preview; these are not fan percentages.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:percent25OverhangSpeed`.

### 50 % overhang speed - percent50OverhangSpeed

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Requested print speed for the 50% overhang category.

**When would I change it?** Change when that category of overhang needs a measured speed adjustment.

**What changes if I adjust it?** A lower requested speed can improve difficult overhangs; a higher one raises motion/flow demand.

**Check together with:** Overhang classification; Other overhang speed categories; Fans; Line width and height.

**Displayed units:** mm/s.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Do not assume what the percentage measures without checking Rocket's classification/Preview; these are not fan percentages.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:percent50OverhangSpeed`.

### 75 % overhang speed - percent75OverhangSpeed

**Scope:** Process: general / OVERHANG; Process: reinforced / OVERHANG; Process: speedy / OVERHANG.

**What does it mean?** Requested print speed for the 75% overhang category.

**When would I change it?** Change when that category of overhang needs a measured speed adjustment.

**What changes if I adjust it?** A lower requested speed can improve difficult overhangs; a higher one raises motion/flow demand.

**Check together with:** Overhang classification; Other overhang speed categories; Fans; Line width and height.

**Displayed units:** mm/s.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Do not assume what the percentage measures without checking Rocket's classification/Preview; these are not fan percentages.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:percent75OverhangSpeed`.

### Plastic extrusion compensation ratio - plasticExtrusionCompensationRatio

**Scope:** Process: fortified / REINFORCEDENTITIES; Process: general / REINFORCEDENTITIES; Process: reinforced / REINFORCEDENTITIES.

**What does it mean?** A ratio that multiplies the calculated plastic extrusion in reinforced-entity processing.

**When would I change it?** Use only when specifically validating this additional compensation layer.

**What changes if I adjust it?** Increasing adds calculated plastic; decreasing reduces it. It can combine with other flow corrections.

**Check together with:** Material flow; Feature flow multipliers; Composite/fiber geometry.

**Caution:** Do not use a feature multiplier to hide a clog, leak, incorrect filament diameter, or bad base flow calibration. Confirm its actual affected paths in the emitted file before applying it globally.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:plasticExtrusionCompensationRatio`.

### Put fiber seam on longest straight edge end - putFiberSeamOnLongestEdgeEnd

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Requests the fiber seam at an end of the contour's longest straight edge.

**When would I change it?** Use when a deliberate fiber start/end position is preferable to other seam choices.

**What changes if I adjust it?** Enabled requests that seam location; disabled leaves seam placement to the remaining seam rules.

**Check together with:** Fiber seam start/distribution; Contour shape; Fiber cutting.

**Caution:** A requested seam can be constrained by actual path geometry; inspect both start and cut positions.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:putFiberSeamOnLongestEdgeEnd`.

### Extrusion width - replaceFiberPlasticSolidEWMM

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Requested line width for the solid-plastic-infill group (described as bottom solid skin in installed help).

**When would I change it?** Change to tune the path geometry after the material's base flow is sound.

**What changes if I adjust it?** Larger width asks for wider lines and more volume per unit path; smaller width requests narrower lines.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Displayed units:** mm.

**Caution:** The requested width is not proof the nozzle can deliver it. The legacy field name refers to fiber replacement while the help calls it bottom skin; verify the active mode's affected paths in Preview.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:replaceFiberPlasticSolidEWMM`.

### Flow multiplier - replaceFiberPlasticSolidExtrusionMultP

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Additional flow factor for the solid-plastic-infill group (described as bottom solid skin in installed help).

**When would I change it?** Change only when these paths alone need a measured flow correction.

**What changes if I adjust it?** It multiplies the material flow factor; increasing adds commanded plastic to these paths and decreasing reduces it.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Caution:** Do not compensate for a clog, leak, or incorrect base material flow with a feature multiplier. The legacy field name refers to fiber replacement while the help calls it bottom skin; verify the active mode's affected paths in Preview.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:replaceFiberPlasticSolidExtrusionMultP`.

### Fill angle - replaceFiberPlasticSolidInfillAngle

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Starting direction of fill lines for the solid-plastic-infill group (described as bottom solid skin in installed help).

**When would I change it?** Change to orient the fill relative to the shape or desired surface appearance.

**What changes if I adjust it?** It rotates applicable fill paths; it does not directly alter fill amount.

**Check together with:** Fill pattern; Angle step where available; Perimeter contact.

**Displayed units:** °.

**Caution:** Concentric paths do not use this angle according to installed help. The legacy field name refers to fiber replacement while the help calls it bottom skin; verify the active mode's affected paths in Preview.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:replaceFiberPlasticSolidInfillAngle`.

### Fill angle step - replaceFiberPlasticSolidInfillAngleStep

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Change in fill direction between successive layers of the solid-plastic-infill group (described as bottom solid skin in installed help).

**When would I change it?** Change to control how the fill orientation alternates across these layers.

**What changes if I adjust it?** A different step changes the layer-to-layer rotation rather than the number of skin layers.

**Check together with:** Initial fill angle; Fill pattern; Skin-layer schedule.

**Displayed units:** °.

**Caution:** Concentric fill does not use this angle step according to installed help. The legacy field name refers to fiber replacement while the help calls it bottom skin; verify the active mode's affected paths in Preview.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:replaceFiberPlasticSolidInfillAngleStep`.

### Infill/Wall overlap - replaceFiberPlasticSolidInfillExtendIntoPerimeterRatio

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Fraction of line width by which the solid-plastic-infill group (described as bottom solid skin in installed help) overlaps the surrounding perimeters.

**When would I change it?** Use when the skin-to-wall bond is incomplete or the boundary is excessively crowded.

**What changes if I adjust it?** Increasing grows the overlap; decreasing reduces intrusion into the perimeter region.

**Check together with:** Line width; Perimeter geometry; Material and feature flow.

**Caution:** This is a ratio, not millimeters or a direct percentage entry. Excess overlap can cause ridges. The legacy field name refers to fiber replacement while the help calls it bottom skin; verify the active mode's affected paths in Preview.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:replaceFiberPlasticSolidInfillExtendIntoPerimeterRatio`.

### Fill pattern - replaceFiberPlasticSolidInfillPattern

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Layout used to fill the solid-plastic-infill group (described as bottom solid skin in installed help).

**When would I change it?** Change to compare surface appearance, path continuity, and print time.

**What changes if I adjust it?** Each listed pattern creates a different path shape; it is not an automatic change in validated flow or strength.

**Check together with:** Fill angle; Layer schedule; Line width; Preview.

**Selectable choices:**

- **Line:** Parallel line paths; compare line direction and boundary connections in Preview. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Zigzag:** Back-and-forth fill with a zigzag layout; check how its turns and connections are generated. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Concentric:** Nested loops following the region boundary; ordinary fill-angle settings generally do not apply. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**Caution:** Choose only options actually offered in the active mode; broader help text is not proof all patterns appear everywhere. The legacy field name refers to fiber replacement while the help calls it bottom skin; verify the active mode's affected paths in Preview.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:replaceFiberPlasticSolidInfillPattern`.

### Printing speed - replaceFiberPlasticSolidSpeed

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Requested print speed for the solid-plastic-infill group (described as bottom solid skin in installed help).

**When would I change it?** Change after temperature and flow are stable using a controlled feature-speed test.

**What changes if I adjust it?** Increasing raises motion and extrusion demand; decreasing reduces it and changes time/heat exposure.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Displayed units:** mm/s.

**Caution:** Other limits can reduce actual speed. No safe throughput or pressure limit follows from this setting. The legacy field name refers to fiber replacement while the help calls it bottom skin; verify the active mode's affected paths in Preview.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:replaceFiberPlasticSolidSpeed`.

### Seam distribution offset (fiber) - seamDistributionPositionOffsetFiber

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Per-layer change of the fiber seam position, expressed as a fraction of the contour perimeter.

**When would I change it?** Use to spread or deliberately move fiber seams between layers.

**What changes if I adjust it?** Installed help describes each new layer moving by offset multiplied by perimeter: positive moves forward along the path and negative moves backward.

**Check together with:** Fiber seam distribution type; Fiber seam start position; Contour direction and perimeter length.

**Caution:** This is a perimeter-relative offset, not millimeters. Random seam settings may supersede specified placement.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:seamDistributionPositionOffsetFiber`.

### Seam distribution offset (plastic) - seamDistributionPositionOffsetPlastic

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Per-layer change of the plastic seam position, expressed as a fraction of the contour perimeter.

**When would I change it?** Use to spread or deliberately move plastic seams between layers.

**What changes if I adjust it?** Installed help describes each new layer moving by offset multiplied by perimeter: positive moves forward along the path and negative moves backward.

**Check together with:** Plastic seam distribution type; Plastic seam start position; Contour direction and perimeter length.

**Caution:** This is a perimeter-relative offset, not millimeters. Random seam settings may supersede specified placement.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:seamDistributionPositionOffsetPlastic`.

### Seam distribution type (fiber) - seamDistributionPositionTypeFiber

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Chooses random or specified fiber seam distribution positioning.

**When would I change it?** Use to trade a repeatable seam location against dispersing the fiber seam marks.

**What changes if I adjust it?** Random delegates position choice to random placement; Specified uses the related offset. Installed help says making either the start or distribution random can randomize both.

**Check together with:** Fiber seam distribution offset; Fiber other seam-position type; Longest-edge fiber seam preference.

**Selectable choices:**

- **Random:** Randomizes seam placement; installed help says either random start or random distribution can randomize both. Schema contexts: Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.
- **Specified:** Uses the corresponding specified offset rather than requesting random placement. Schema contexts: Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**Caution:** Specified does not guarantee one absolute machine coordinate; contour geometry and other seam rules still apply.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:seamDistributionPositionTypeFiber`.

### Seam distribution type (plastic) - seamDistributionPositionTypePlastic

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Chooses random or specified plastic seam distribution positioning.

**When would I change it?** Use to trade a repeatable seam location against dispersing the plastic seam marks.

**What changes if I adjust it?** Random delegates position choice to random placement; Specified uses the related offset. Installed help says making either the start or distribution random can randomize both.

**Check together with:** Plastic seam distribution offset; Plastic other seam-position type; Longest-edge fiber seam preference.

**Selectable choices:**

- **Random:** Randomizes seam placement; installed help says either random start or random distribution can randomize both. Schema contexts: Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.
- **Specified:** Uses the corresponding specified offset rather than requesting random placement. Schema contexts: Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**Caution:** Specified does not guarantee one absolute machine coordinate; contour geometry and other seam rules still apply.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:seamDistributionPositionTypePlastic`.

### Seam start offset (fiber) - seamStartPositionOffsetFiber

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Fixed start-position shift of the fiber seam on all layers, as a fraction of perimeter length.

**When would I change it?** Use when a repeatable fiber start/end location should move away from an unsuitable surface.

**What changes if I adjust it?** Installed help describes positive offsets moving forward and negative offsets moving backward along the contour; this is not the per-layer distribution increment.

**Check together with:** Fiber seam start type; Fiber seam distribution; Contour direction.

**Caution:** This is not an XY coordinate or a millimeter distance. Inspect actual start/end locations and fiber-cut positions.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:seamStartPositionOffsetFiber`.

### Seam start offset (plastic) - seamStartPositionOffsetPlastic

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Fixed start-position shift of the plastic seam on all layers, as a fraction of perimeter length.

**When would I change it?** Use when a repeatable plastic start/end location should move away from an unsuitable surface.

**What changes if I adjust it?** Installed help describes positive offsets moving forward and negative offsets moving backward along the contour; this is not the per-layer distribution increment.

**Check together with:** Plastic seam start type; Plastic seam distribution; Contour direction.

**Caution:** This is not an XY coordinate or a millimeter distance. Inspect actual start/end locations.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:seamStartPositionOffsetPlastic`.

### Seam start type (fiber) - seamStartPositionTypeFiber

**Scope:** Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**What does it mean?** Chooses random or specified fiber seam start positioning.

**When would I change it?** Use to trade a repeatable seam location against dispersing the fiber seam marks.

**What changes if I adjust it?** Random delegates position choice to random placement; Specified uses the related offset. Installed help says making either the start or distribution random can randomize both.

**Check together with:** Fiber seam start offset; Fiber other seam-position type; Longest-edge fiber seam preference.

**Selectable choices:**

- **Random:** Randomizes seam placement; installed help says either random start or random distribution can randomize both. Schema contexts: Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.
- **Specified:** Uses the corresponding specified offset rather than requesting random placement. Schema contexts: Process: fortified / REINFORCEDPERIMETERS; Process: general / REINFORCEDPERIMETERS; Process: reinforced / REINFORCEDPERIMETERS.

**Caution:** Specified does not guarantee one absolute machine coordinate; contour geometry and other seam rules still apply.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:seamStartPositionTypeFiber`.

### Seam start type (plastic) - seamStartPositionTypePlastic

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Chooses random or specified plastic seam start positioning.

**When would I change it?** Use to trade a repeatable seam location against dispersing the plastic seam marks.

**What changes if I adjust it?** Random delegates position choice to random placement; Specified uses the related offset. Installed help says making either the start or distribution random can randomize both.

**Check together with:** Plastic seam start offset; Plastic other seam-position type; Longest-edge fiber seam preference.

**Selectable choices:**

- **Random:** Randomizes seam placement; installed help says either random start or random distribution can randomize both. Schema contexts: Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.
- **Specified:** Uses the corresponding specified offset rather than requesting random placement. Schema contexts: Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**Caution:** Specified does not guarantee one absolute machine coordinate; contour geometry and other seam rules still apply.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:seamStartPositionTypePlastic`.

### Threshold overlap - selfSupportDistanceCoeff

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Overlap with the preceding layer used for automatic support detection.

**When would I change it?** Adjust when automatic supports miss weakly supported areas or support too much geometry.

**What changes if I adjust it?** It changes the overlap test; interpretation as percentage or distance is controlled by the related switch where exposed.

**Check together with:** Threshold overlap uses percent; Threshold angle; Support generation.

**Displayed units:** %.

**Caution:** Do not treat the saved 'Coeff' name as a universal unit. Check the active mode, displayed unit, and Preview.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:selfSupportDistanceCoeff`.

### Distance from part - skirtDistance

**Scope:** Process: general / BRIMSKIRT; Process: reinforced / BRIMSKIRT; Process: speedy / BRIMSKIRT.

**What does it mean?** Separation between the skirt loops and the model.

**When would I change it?** Change to make priming loops clear of the part and other bed objects.

**What changes if I adjust it?** Increasing moves the skirt farther away; decreasing brings it nearer.

**Check together with:** Skirt loops; Brim; Plate layout; Tool priming.

**Displayed units:** mm.

**Caution:** A skirt normally does not attach to the model like a brim; verify bed clearance.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:skirtDistance`.

### Flow multiplier - skirtExtrusionMultP

**Scope:** Process: general / BRIMSKIRT; Process: reinforced / BRIMSKIRT; Process: speedy / BRIMSKIRT.

**What does it mean?** Additional plastic-flow factor for skirt paths.

**When would I change it?** Use only if the skirt needs a separate priming-flow adjustment after base material flow is sound.

**What changes if I adjust it?** It multiplies material flow for the skirt; increasing adds plastic and decreasing reduces it.

**Check together with:** Material flow; Skirt loops; First-layer settings.

**Caution:** Do not use a feature multiplier to hide a clog, leak, incorrect filament diameter, or bad base flow calibration. A good skirt does not certify model flow or adhesion.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:skirtExtrusionMultP`.

### Skirt - skirtLoops

**Scope:** Process: general / BRIMSKIRT; Process: reinforced / BRIMSKIRT; Process: speedy / BRIMSKIRT.

**What does it mean?** Number of loops printed around the model as a skirt.

**When would I change it?** Change when more or less priming path is needed before the part begins.

**What changes if I adjust it?** More loops provide a longer priming path and use more material; fewer reduce both.

**Check together with:** Skirt distance; Priming/start sequence; First layer.

**Displayed units:** loops.

**Caution:** Skirt loops are not a substitute for a clear, loaded nozzle or a verified start sequence.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:skirtLoops`.

### Speed limit end height - slowdownEndHeight

**Scope:** Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Z height where the height-dependent speed ceiling reaches its final speed.

**When would I change it?** Use to control how long the speed-ceiling transition lasts.

**What changes if I adjust it?** A greater separation from start height spreads the transition over more height; a smaller separation compresses it.

**Check together with:** Start height; Start/end speeds; Feature speeds.

**Displayed units:** mm.

**Declared editor constraints:** {"strictlyGreaterThanField": "slowdownStartHeight"}. These are not operating recommendations.

**Caution:** Keep the height ordering coherent and verify how Rocket handles out-of-order entries.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:slowdownEndHeight`.

### Speed at end height - slowdownEndSpeed

**Scope:** Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Maximum applicable extrusion speed at and above the end height.

**When would I change it?** Use to set the final speed ceiling after the height transition.

**What changes if I adjust it?** Lowering restricts later applicable moves; raising relaxes that restriction.

**Check together with:** End height; Start speed; Material throughput.

**Displayed units:** mm/s.

**Caution:** Other speed rules may remain lower. Check emitted speeds rather than relying on this label alone.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:slowdownEndSpeed`.

### Speed limit start height - slowdownStartHeight

**Scope:** Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Z height at which the height-dependent speed ceiling starts.

**When would I change it?** Use when intentionally limiting speed over a chosen height range.

**What changes if I adjust it?** Changing it moves the start of the speed-limiting region up or down.

**Check together with:** Speed at start height; End height; Speed at end height; Feature speeds.

**Displayed units:** mm.

**Caution:** Inspect the resulting speed graph; a ceiling does not make the machine print faster than other limits.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:slowdownStartHeight`.

### Speed at start height - slowdownStartSpeed

**Scope:** Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Maximum applicable extrusion speed at the start of the height-limited range.

**When would I change it?** Change to set the initial ceiling for that range.

**What changes if I adjust it?** A lower value restricts the initial printing speed more; a higher value relaxes this ceiling.

**Check together with:** Start height; End speed; Feature speeds; Flow demand.

**Displayed units:** mm/s.

**Caution:** This is a ceiling for applicable extrusion moves, not a universal motion limit or a guaranteed commanded speed.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:slowdownStartSpeed`.

### Start G-code - startGcode

**Scope:** Process: fortified / OTHER; Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Custom commands inserted in the process start sequence.

**When would I change it?** Change only when the exact printer firmware and Rocket's complete heating/start order have been reviewed.

**What changes if I adjust it?** Commands can change printer state, temperatures, motion, tools, and extrusion. The installed wording about before/after heating is ambiguous.

**Check together with:** Machine start G-code; Material start code; Firmware macros; Selected tools.

**Caution:** Do not paste generic commands or assume insertion order. Audit the complete emitted start sequence before any print.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:startGcode`.

### Bottom interface spacing - supportAirGapBottom

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Spacing between adjacent bottom support-interface lines, according to the current UI/help.

**When would I change it?** Adjust bottom-interface density/removability using the displayed millimeter setting.

**What changes if I adjust it?** Larger spacing leaves a more open interface; smaller spacing packs its lines more closely.

**Check together with:** Bottom-interface layers; Support interface width/flow; Bottom Z distance.

**Displayed units:** mm.

**Caution:** Despite the legacy 'AirGap' ID, this is described as in-plane line spacing, not vertical clearance.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportAirGapBottom`.

### Threshold angle - supportAirGapTop

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Automatic overhang threshold angle, according to the current visible label and help.

**When would I change it?** Use only while comparing automatic support candidates in Preview.

**What changes if I adjust it?** It changes which overhangs become support candidates; the exact relation to the other threshold-angle fields needs mode-specific verification.

**Check together with:** Support threshold angle; Overlap threshold; Automatic support mode.

**Displayed units:** °.

**Caution:** The legacy ID says top air gap; do not use it to tune vertical support separation.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:supportAirGapTop`.

### Bottom interface - supportBottomInterfaceLayerCount

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Number of bottom support-interface macrolayers, not a simple on/off switch.

**When would I change it?** Change when the bottom contact region needs a different thickness or removal behavior.

**What changes if I adjust it?** More selected layers create a thicker contact region; zero requests none. Follow top inherits the top-interface layer count.

**Check together with:** Macrolayer height; Interface spacing; Top/bottom Z clearances.

**Displayed units:** layers.

**Selectable choices:**

- **Follow top:** Uses the top-interface layer count for the bottom interface. Schema contexts: Process: general / SUPPORT.
- **0:** Requests no interface macrolayers for this side. Schema contexts: Process: general / SUPPORT.
- **1:** Requests 1 interface macrolayer for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.
- **2:** Requests 2 interface macrolayers for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.
- **3:** Requests 3 interface macrolayers for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.

**Caution:** Some installed help uses old 'flag' wording, but this schema is a layer-count selector. Verify the actual layer count in Preview.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportBottomInterfaceLayerCount`.

### Threshold overlap uses percent - supportDoAirgaps

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Chooses percentage versus absolute-distance interpretation for the support-overlap threshold.

**When would I change it?** Change only when you intentionally change how the neighboring overlap value is interpreted.

**What changes if I adjust it?** Enabled means percentage according to installed help; disabled means absolute distance.

**Check together with:** Threshold overlap; Automatic support detection; Displayed units.

**Caution:** The legacy name does not mean 'enable air gaps.' Re-evaluate the overlap number when switching units.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportDoAirgaps`.

### Support line width - supportEWMM

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Requested line width of the ordinary support body, in millimeters.

**When would I change it?** Change to adjust support-body path geometry.

**What changes if I adjust it?** Larger width requests wider support-body lines; smaller width requests narrower lines.

**Check together with:** Support-body flow; Support speed; Nozzle diameter; Interface line width.

**Displayed units:** mm.

**Caution:** A width entry is a requested geometry, not proof that the nozzle/material can produce it reliably. Interfaces have a separate width.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportEWMM`.

### Support expansion - supportExpansion

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Horizontal offset of conventional support regions.

**When would I change it?** Use to adjust the supported footprint after checking model avoidance and clearances.

**What changes if I adjust it?** Positive expands regions; negative shrinks them; the installed help describes zero as no added offset.

**Check together with:** Support/model XY distance; Z clearances; Overhang detection.

**Displayed units:** mm.

**Caution:** Expansion is not permission for supports to intersect the model; inspect Preview.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportExpansion`.

### Support flow multiplier - supportExtrusionMultP

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Additional flow multiplier for the conventional support body.

**When would I change it?** Change only when support-body extrusion needs its own measured correction.

**What changes if I adjust it?** It multiplies the support material's flow setting, without being the interface-flow setting.

**Check together with:** Support material flow; Support width/speed; Interface flow; First-layer flow.

**Caution:** Do not use a feature multiplier to hide a clog, leak, incorrect filament diameter, or bad base flow calibration. First-layer paths can use separate rules.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportExtrusionMultP`.

### Pattern angle - supportFillAngle

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Direction of the conventional support fill pattern.

**When would I change it?** Change to orient support lines relative to the model or other pattern layers.

**What changes if I adjust it?** Rotates the support pattern; it does not directly increase support density.

**Check together with:** Support pattern; Base-pattern spacing; Interface direction.

**Displayed units:** °.

**Caution:** The effect depends on the active pattern; inspect actual lines.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportFillAngle`.

### Base pattern spacing - supportFillDensity

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Gap between neighboring conventional support base-pattern lines, in millimeters.

**When would I change it?** Use to trade support coverage against material, time, and removability.

**What changes if I adjust it?** Increasing this spacing makes the base more open; decreasing packs lines more closely.

**Check together with:** Support pattern/angle; Support line width; Interface settings.

**Displayed units:** mm.

**Caution:** Despite the saved 'Density' name, the current label and help specify spacing. Do not enter a percent.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportFillDensity`.

### Support interface line width - supportInterfaceEWMM

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Requested line width of top and bottom support interfaces, in millimeters.

**When would I change it?** Change when the contact-layer geometry needs a separate adjustment from the support body.

**What changes if I adjust it?** Increasing width requests wider contact lines; decreasing requests narrower ones.

**Check together with:** Interface spacing; Interface flow/speed; Nozzle diameter.

**Displayed units:** mm.

**Caution:** A width entry is a requested geometry, not proof that the nozzle/material can produce it reliably. This does not change the support-body width.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportInterfaceEWMM`.

### Support interface flow multiplier - supportInterfaceExtrusionMultrP

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Additional flow multiplier for support-interface paths.

**When would I change it?** Use when interface extrusion alone needs correction after material flow is tuned.

**What changes if I adjust it?** It multiplies the interface material's flow factor, separately from support-body flow.

**Check together with:** Interface width/spacing; Interface material; First-layer flow.

**Caution:** Do not use a feature multiplier to hide a clog, leak, incorrect filament diameter, or bad base flow calibration. It does not directly change model extrusion.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportInterfaceExtrusionMultrP`.

### Legacy support interface density - supportInterfaceFillDensity

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Legacy support-interface fill percentage.

**When would I change it?** Leave it unchanged unless investigating an older profile/backend path.

**What changes if I adjust it?** The installed help identifies it as legacy; modern interfaces use independent spacing controls instead.

**Check together with:** Top/bottom interface spacing; Imported older profiles; Interface pattern.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Do not assume it still controls current interface density merely because the field is selectable.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:supportInterfaceFillDensity`.

### Support interface pattern - supportInterfaceFillType

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Pattern selector for the conventional support interface.

**When would I change it?** Use to change the contact-path layout after spacing and clearances are established.

**What changes if I adjust it?** The inspected schema variant exposes only Zigzag; a more general help paragraph lists additional patterns not proven selectable here.

**Check together with:** Interface spacing; Interface angle; Top/bottom layers.

**Selectable choices:**

- **Zigzag:** Back-and-forth fill with a zigzag layout; check how its turns and connections are generated. Schema contexts: Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**Caution:** Do not promise other pattern choices from help text alone; choose only options actually shown in the current mode.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportInterfaceFillType`.

### Support interface speed - supportInterfaceSpeed

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Requested speed for top and bottom support-interface paths.

**When would I change it?** Change to improve contact-layer quality or reduce time after reliable extrusion is established.

**What changes if I adjust it?** Faster raises interface flow demand; slower reduces it and changes heat/cooling time.

**Check together with:** Interface width/flow; Support-body speed; First-layer speed.

**Displayed units:** mm/s.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** This is separate from support-body speed; first-layer and other limits may override it.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportInterfaceSpeed`.

### Support speed - supportSpeed

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Requested printing speed for conventional support-body paths.

**When would I change it?** Change after support geometry and extrusion are stable.

**What changes if I adjust it?** Increasing requests faster support printing; decreasing reduces motion and flow demand.

**Check together with:** Support line width/height; Support flow; Interface speed; First-layer speed.

**Displayed units:** mm/s.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** A fast support-body setting is not a proven material-throughput limit.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportSpeed`.

### Threshold angle - supportThresholdAngleDegree

**Scope:** Process: general / SUPPORT.

**What does it mean?** Automatic support threshold measured from horizontal, according to installed help.

**When would I change it?** Adjust when automatic support coverage is too broad or too sparse.

**What changes if I adjust it?** The help says larger positive angles generally create more automatic support; zero has mode-specific behavior rather than one universal meaning.

**Check together with:** Support type; Automatic/manual regions; Overlap threshold.

**Displayed units:** °.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** This does not filter manually enforced support regions. Inspect Preview instead of transferring another slicer's angle convention.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportThresholdAngleDegree`.

### Top interface - supportTopInterfaceLayerCount

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Number of top support-interface macrolayers, not a simple on/off switch.

**When would I change it?** Change when the top contact region needs a different thickness or removal behavior.

**What changes if I adjust it?** More selected layers create a thicker contact region; zero requests none.

**Check together with:** Macrolayer height; Interface spacing; Top/bottom Z clearances.

**Displayed units:** layers.

**Selectable choices:**

- **0:** Requests no interface macrolayers for this side. Schema contexts: Process: general / SUPPORT.
- **1:** Requests 1 interface macrolayer for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.
- **2:** Requests 2 interface macrolayers for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.
- **3:** Requests 3 interface macrolayers for this side; verify the actual sliced contact thickness. Schema contexts: Process: general / SUPPORT.

**Caution:** Some installed help uses old 'flag' wording, but this schema is a layer-count selector. Verify the actual layer count in Preview.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportTopInterfaceLayerCount`.

### Support/model XY distance - supportXYDistance

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Horizontal clearance between conventional supports and the model.

**When would I change it?** Use when supports fuse to sidewalls or sit too far from the area they should support.

**What changes if I adjust it?** Increasing reduces side contact but can reduce support coverage; decreasing brings supports closer.

**Check together with:** Support expansion; Top/bottom Z distance; Line width.

**Displayed units:** mm.

**Caution:** XY distance is not vertical separation; check both independently.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:supportXYDistance`.

### Extrusion width - topIntermediateSkinEWMM

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Requested line width for intermediate solid layers below the final top surface.

**When would I change it?** Change to tune the path geometry after the material's base flow is sound.

**What changes if I adjust it?** Larger width asks for wider lines and more volume per unit path; smaller width requests narrower lines.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Displayed units:** mm.

**Caution:** The requested width is not proof the nozzle can deliver it.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topIntermediateSkinEWMM`.

### Flow multiplier - topIntermediateSkinExtrusionMultP

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Additional flow factor for intermediate solid layers below the final top surface.

**When would I change it?** Change only when these paths alone need a measured flow correction.

**What changes if I adjust it?** It multiplies the material flow factor; increasing adds commanded plastic to these paths and decreasing reduces it.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Caution:** Do not compensate for a clog, leak, or incorrect base material flow with a feature multiplier.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topIntermediateSkinExtrusionMultP`.

### Fill angle - topIntermediateSkinInfillAngle

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Starting direction of fill lines for intermediate solid layers below the final top surface.

**When would I change it?** Change to orient the fill relative to the shape or desired surface appearance.

**What changes if I adjust it?** It rotates applicable fill paths; it does not directly alter fill amount.

**Check together with:** Fill pattern; Angle step where available; Perimeter contact.

**Displayed units:** °.

**Caution:** Concentric paths do not use this angle according to installed help.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topIntermediateSkinInfillAngle`.

### Fill angle step - topIntermediateSkinInfillAngleStep

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Change in fill direction between successive layers of intermediate solid layers below the final top surface.

**When would I change it?** Change to control how the fill orientation alternates across these layers.

**What changes if I adjust it?** A different step changes the layer-to-layer rotation rather than the number of skin layers.

**Check together with:** Initial fill angle; Fill pattern; Skin-layer schedule.

**Displayed units:** °.

**Caution:** Concentric fill does not use this angle step according to installed help.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topIntermediateSkinInfillAngleStep`.

### Infill/Wall overlap - topIntermediateSkinInfillExtendIntoPerimeterRatio

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Fraction of line width by which intermediate solid layers below the final top surface overlaps the surrounding perimeters.

**When would I change it?** Use when the skin-to-wall bond is incomplete or the boundary is excessively crowded.

**What changes if I adjust it?** Increasing grows the overlap; decreasing reduces intrusion into the perimeter region.

**Check together with:** Line width; Perimeter geometry; Material and feature flow.

**Caution:** This is a ratio, not millimeters or a direct percentage entry. Excess overlap can cause ridges.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topIntermediateSkinInfillExtendIntoPerimeterRatio`.

### Fill pattern - topIntermediateSkinInfillPattern

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Layout used to fill intermediate solid layers below the final top surface.

**When would I change it?** Change to compare surface appearance, path continuity, and print time.

**What changes if I adjust it?** Each listed pattern creates a different path shape; it is not an automatic change in validated flow or strength.

**Check together with:** Fill angle; Layer schedule; Line width; Preview.

**Selectable choices:**

- **Line:** Parallel line paths; compare line direction and boundary connections in Preview. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Zigzag:** Back-and-forth fill with a zigzag layout; check how its turns and connections are generated. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Concentric:** Nested loops following the region boundary; ordinary fill-angle settings generally do not apply. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**Caution:** Choose only options actually offered in the active mode; broader help text is not proof all patterns appear everywhere.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topIntermediateSkinInfillPattern`.

### Printing speed - topIntermediateSkinSpeed

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Requested print speed for intermediate solid layers below the final top surface.

**When would I change it?** Change after temperature and flow are stable using a controlled feature-speed test.

**What changes if I adjust it?** Increasing raises motion and extrusion demand; decreasing reduces it and changes time/heat exposure.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Displayed units:** mm/s.

**Caution:** Other limits can reduce actual speed. No safe throughput or pressure limit follows from this setting.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topIntermediateSkinSpeed`.

### Extrusion width - topMostSkinEWMM

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Requested line width for the final top-surface skin.

**When would I change it?** Change to tune the path geometry after the material's base flow is sound.

**What changes if I adjust it?** Larger width asks for wider lines and more volume per unit path; smaller width requests narrower lines.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Displayed units:** mm.

**Caution:** The requested width is not proof the nozzle can deliver it.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topMostSkinEWMM`.

### Flow multiplier - topMostSkinExtrusionMultP

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Additional flow factor for the final top-surface skin.

**When would I change it?** Change only when these paths alone need a measured flow correction.

**What changes if I adjust it?** It multiplies the material flow factor; increasing adds commanded plastic to these paths and decreasing reduces it.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Caution:** Do not compensate for a clog, leak, or incorrect base material flow with a feature multiplier.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topMostSkinExtrusionMultP`.

### Fill angle - topMostSkinInfillAngle

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Starting direction of fill lines for the final top-surface skin.

**When would I change it?** Change to orient the fill relative to the shape or desired surface appearance.

**What changes if I adjust it?** It rotates applicable fill paths; it does not directly alter fill amount.

**Check together with:** Fill pattern; Angle step where available; Perimeter contact.

**Displayed units:** °.

**Caution:** Concentric paths do not use this angle according to installed help.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topMostSkinInfillAngle`.

### Infill/Wall overlap - topMostSkinInfillExtendIntoPerimeterRatio

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Fraction of line width by which the final top-surface skin overlaps the surrounding perimeters.

**When would I change it?** Use when the skin-to-wall bond is incomplete or the boundary is excessively crowded.

**What changes if I adjust it?** Increasing grows the overlap; decreasing reduces intrusion into the perimeter region.

**Check together with:** Line width; Perimeter geometry; Material and feature flow.

**Caution:** This is a ratio, not millimeters or a direct percentage entry. Excess overlap can cause ridges.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topMostSkinInfillExtendIntoPerimeterRatio`.

### Fill pattern - topMostSkinInfillPattern

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Layout used to fill the final top-surface skin.

**When would I change it?** Change to compare surface appearance, path continuity, and print time.

**What changes if I adjust it?** Each listed pattern creates a different path shape; it is not an automatic change in validated flow or strength.

**Check together with:** Fill angle; Layer schedule; Line width; Preview.

**Selectable choices:**

- **Line:** Parallel line paths; compare line direction and boundary connections in Preview. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Zigzag:** Back-and-forth fill with a zigzag layout; check how its turns and connections are generated. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Concentric:** Nested loops following the region boundary; ordinary fill-angle settings generally do not apply. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Hilbert Curve:** A space-filling Hilbert-curve path layout; inspect local turns and small-feature coverage. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Archimedean Chords:** A curved/concentric-style fill layout named Archimedean Chords; verify the actual geometry in Preview rather than assuming it is equivalent to another slicer's implementation. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.
- **Octagram Spiral:** A star/spiral-style fill option named Octagram Spiral; inspect the generated path and sharp direction changes. Schema contexts: Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**Caution:** Choose only options actually offered in the active mode; broader help text is not proof all patterns appear everywhere.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topMostSkinInfillPattern`.

### Printing speed - topMostSkinSpeed

**Scope:** Process: general / SOLIDPLASTICINFILL; Process: reinforced / SOLIDPLASTICINFILL; Process: speedy / SOLIDPLASTICINFILL.

**What does it mean?** Requested print speed for the final top-surface skin.

**When would I change it?** Change after temperature and flow are stable using a controlled feature-speed test.

**What changes if I adjust it?** Increasing raises motion and extrusion demand; decreasing reduces it and changes time/heat exposure.

**Check together with:** Material flow multiplier; Line width and layer height; Feature speed; Pattern and overlap.

**Displayed units:** mm/s.

**Caution:** Other limits can reduce actual speed. No safe throughput or pressure limit follows from this setting.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topMostSkinSpeed`.

### Use micro infill on top surfaces (Beta) - topUseMicroInfill

**Scope:** Process: general / MICROPLASTICINFILL; Process: reinforced / MICROPLASTICINFILL; Process: speedy / MICROPLASTICINFILL.

**What does it mean?** Beta feature for filling top surfaces when the remaining height is less than a normal layer.

**When would I change it?** Use only for an explicitly experimental top-surface case after normal skins work.

**What changes if I adjust it?** Enabled permits the special micro-infill treatment; disabled avoids this beta path.

**Check together with:** Macrolayer/layer schedule; Top skins; Remaining surface height.

**Caution:** Installed help explicitly warns the beta behavior may not work as expected. Inspect Preview and emitted Z/extrusion.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:topUseMicroInfill`.

### Support interface pattern - treeInterfaceSupportInfillType

**Scope:** Process: general / SUPPORT.

**What does it mean?** Pattern used in tree-support contact-interface layers.

**When would I change it?** Change to compare interface coverage, path continuity, and removal.

**What changes if I adjust it?** The schema offers Zigzag, Grid, Line, and Concentric patterns; pattern choice changes the contact paths, not their validated flow.

**Check together with:** Interface spacing; Interface angles; Top/bottom layer count.

**Selectable choices:**

- **Zigzag:** Back-and-forth fill with a zigzag layout; check how its turns and connections are generated. Schema contexts: Process: general / SUPPORT.
- **Grid:** Intersecting line families forming a grid; crossings change local path overlap. Schema contexts: Process: general / SUPPORT.
- **Line:** Parallel line paths; compare line direction and boundary connections in Preview. Schema contexts: Process: general / SUPPORT.
- **Concentric:** Nested loops following the region boundary; ordinary fill-angle settings generally do not apply. Schema contexts: Process: general / SUPPORT.

**Caution:** Angles do not apply to every pattern. Choose from the active mode's actual list, not broader help text.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeInterfaceSupportInfillType`.

### Automatically calculate tree support brim - treeSupportAutoBrim

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Automatically determines a tree-support brim from the root geometry and support height.

**When would I change it?** Use automatic brim sizing unless a measured adhesion case calls for explicit manual width.

**What changes if I adjust it?** Enabled calculates brim size; disabled makes the separate manual brim width relevant.

**Check together with:** Tree roots; Support height; Manual tree brim width.

**Caution:** Automatic sizing does not prove adhesion or plate fit; inspect the full footprint.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportAutoBrim`.

### Body fill angle - treeSupportBodyFillAngle

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Starting angle of the internal tree-body fill.

**When would I change it?** Change to orient non-hollow body fill.

**What changes if I adjust it?** It rotates internal fill; hollow bodies do not use it.

**Check together with:** Tree body pattern; Body angle step; Body fill density.

**Displayed units:** °.

**Caution:** This does not rotate the whole support tree.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBodyFillAngle`.

### Body angle step - treeSupportBodyFillAngleStep

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Layer-to-layer change in the tree-body fill angle.

**When would I change it?** Use when changing the alternating orientation of the tree's internal fill.

**What changes if I adjust it?** A different step changes orientation between layers rather than fill amount.

**Check together with:** Tree body pattern; Starting body angle.

**Displayed units:** °.

**Caution:** Installed help says hollow and honeycomb bodies do not use this setting.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBodyFillAngleStep`.

### Body fill density - treeSupportBodyFillDensity

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Density of internal fill in a non-hollow tree-support body.

**When would I change it?** Use when tree bodies need a different material/stability tradeoff.

**What changes if I adjust it?** Higher density requests more internal structure and material; lower density leaves a more open body.

**Check together with:** Tree body pattern; Branch diameter; Wall count.

**Displayed units:** %.

**Declared editor constraints:** {"integer": true}. These are not operating recommendations.

**Caution:** Hollow bodies do not use internal fill. More material does not guarantee a stable tall support.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBodyFillDensity`.

### Tree body fill pattern - treeSupportBodyInfillType

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Internal construction pattern of the tree-support body.

**When would I change it?** Change to compare hollow walls with filled support bodies.

**What changes if I adjust it?** Hollow uses only the shell; the other listed choices add patterned internal fill.

**Check together with:** Body fill density; Body angles; Wall count; Branch geometry.

**Selectable choices:**

- **Hollow:** No internal tree-body infill; the body's walls form the support shell. Schema contexts: Process: general / SUPPORT.
- **Line:** Parallel line paths; compare line direction and boundary connections in Preview. Schema contexts: Process: general / SUPPORT.
- **Grid:** Intersecting line families forming a grid; crossings change local path overlap. Schema contexts: Process: general / SUPPORT.
- **Zigzag:** Back-and-forth fill with a zigzag layout; check how its turns and connections are generated. Schema contexts: Process: general / SUPPORT.
- **Honeycomb:** A repeating honeycomb-style internal structure; inspect how much of it fits inside the tree. Schema contexts: Process: general / SUPPORT.

**Caution:** Inspect small branches; the requested pattern may not fit in every cross-section.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBodyInfillType`.

### Bottom interface spacing - treeSupportBottomInterfaceSpacing

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Gap between adjacent lines in the bottom support interface.

**When would I change it?** Change to balance contact coverage against separation at the support's underside.

**What changes if I adjust it?** Larger spacing leaves more open contact paths; smaller spacing makes them denser.

**Check together with:** Bottom-interface layer count; Bottom Z distance; Interface line width/flow.

**Displayed units:** mm.

**Caution:** This is in-plane line spacing, not vertical clearance or a fill percentage.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBottomInterfaceSpacing`.

### Bottom Z distance - treeSupportBottomZDistance

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Vertical gap between the support's underside and the model surface below it.

**When would I change it?** Use when supports begin on model surfaces and adhere too firmly or too weakly.

**What changes if I adjust it?** Increasing generally eases separation but weakens the support start; decreasing increases proximity/contact.

**Check together with:** Bottom interface; Support/model XY gap; Model layer schedule.

**Displayed units:** mm.

**Caution:** This is not the gap under the supported overhang; that is the top Z distance.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBottomZDistance`.

### Branch angle - treeSupportBranchAngle

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Conventional tree variant: Limit on how much the support branches may tilt while growing sideways.

**When would I change it?** Use when branches cannot reach an overhang or take an unsuitable route.

**What changes if I adjust it?** Larger values permit more lateral reach over a given height; smaller values keep branches more upright.

**Check together with:** Branch spacing; Branch diameter; Model collision avoidance.

**Displayed units:** °.

**Caution:** Permitted tilt is not proof a branch can print unsupported; inspect the whole route.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBranchAngle`.

### Branch diameter - treeSupportBranchDiameter

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Conventional tree variant: Reference diameter of tree-support branches.

**When would I change it?** Change when supports are too fragile or consume excessive material.

**What changes if I adjust it?** Larger branches generally improve stability at a material/time cost; smaller branches reduce material but can be fragile.

**Check together with:** Branch spacing; Diameter growth angle; Wall/fill structure.

**Displayed units:** mm.

**Caution:** A diameter request cannot cure poor first-layer adhesion or a collision.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBranchDiameter`.

### Branch diameter angle - treeSupportBranchDiameterAngle

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Conventional tree variant: Controls how rapidly branches thicken toward their roots.

**When would I change it?** Use when trunks need a different growth/stability profile.

**What changes if I adjust it?** Changing it alters rootward thickening and material use; judge the resulting shape rather than treating it as a printing speed.

**Check together with:** Branch diameter; Tree height; Branch tilt.

**Displayed units:** °.

**Caution:** The UI/help identifies the purpose, not a universal safe angle for every tree.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBranchDiameterAngle`.

### Branch distance - treeSupportBranchDistance

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Conventional tree variant: Target spacing between neighboring support branches.

**When would I change it?** Change when support contacts are too sparse or trees are unnecessarily dense.

**What changes if I adjust it?** Smaller spacing requests more densely placed branches; larger spacing requests fewer.

**Check together with:** Top contact regions; Tip diameter; Branch diameter.

**Displayed units:** mm.

**Caution:** Spacing is a target constrained by model clearance and the planner.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBranchDistance`.

### Tree support brim width - treeSupportBrimWidth

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Manual width of the tree-support brim when automatic brim sizing is off.

**When would I change it?** Use for a specific support-root adhesion/plate-space adjustment.

**What changes if I adjust it?** Wider gives a larger bed attachment; narrower uses less plate area. Installed help describes zero as no brim.

**Check together with:** Automatic tree brim; Root geometry; Plate layout.

**Displayed units:** mm.

**Caution:** This is the tree-support brim, not the model brim; keep both within the plate.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportBrimWidth`.

### Critical regions only - treeSupportCriticalRegionsOnly

**Scope:** Process: general / SUPPORT.

**What does it mean?** Restricts automatically detected tree supports to critical overhang regions.

**When would I change it?** Use when automatic trees cover too much of the model.

**What changes if I adjust it?** Enabled filters routine automatic regions but retains critical shapes; disabled permits the broader automatic set.

**Check together with:** Tree Auto/Hybrid mode; Manual support regions; Overhang detection.

**Caution:** Installed help says manually enforced regions are not filtered; verify unsupported spans.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportCriticalRegionsOnly`.

### Tree support expansion - treeSupportExpansion

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Horizontal expansion of the tree-support overhang contact region.

**When would I change it?** Use to change the footprint of regions that tree supports must reach.

**What changes if I adjust it?** Increasing the nonnegative expansion grows contact regions subject to model-collision limits; it does not increase branch diameter.

**Check together with:** Top contact density; Model collision avoidance; Support/model clearance.

**Displayed units:** mm.

**Caution:** Current help describes nonnegative values for this tree expansion; do not transfer signed conventional-support offset behavior.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportExpansion`.

### Interface fill angle - treeSupportInterfaceFillAngle

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Direction of the first support-interface fill layer.

**When would I change it?** Change to orient the interface contact paths.

**What changes if I adjust it?** It rotates applicable interface lines without directly changing their spacing.

**Check together with:** Interface pattern; Interface angle step; Top/bottom interfaces.

**Displayed units:** °.

**Caution:** Concentric interface paths do not use the angle according to installed help.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportInterfaceFillAngle`.

### Interface angle step - treeSupportInterfaceFillAngleStep

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Change of support-interface fill angle between adjacent interface layers.

**When would I change it?** Use to control layer-to-layer rotation within contact layers.

**What changes if I adjust it?** Different steps change line orientation rather than interface thickness.

**Check together with:** Initial interface angle; Interface pattern; Interface layer count.

**Displayed units:** °.

**Caution:** Concentric fill does not use this angle step.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportInterfaceFillAngleStep`.

### Maximum support layer height - treeSupportMaxLayerHeight

**Scope:** Process: general / SUPPORT.

**What does it mean?** Upper support-layer-height bound when independent support layers are enabled.

**When would I change it?** Change only with compatible support line geometry and a coherent minimum.

**What changes if I adjust it?** Increasing allows thicker support layers; decreasing caps them more tightly.

**Check together with:** Minimum support layer height; Independent support layers; Nozzle/line width.

**Displayed units:** mm.

**Declared editor constraints:** {"greaterThanOrEqualField": "treeSupportMinLayerHeight"}. These are not operating recommendations.

**Caution:** It must not be below the minimum. This is not a certified machine/nozzle limit.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportMaxLayerHeight`.

### Minimum support layer height - treeSupportMinLayerHeight

**Scope:** Process: general / SUPPORT.

**What does it mean?** Lower support-layer-height bound when independent support layers are enabled.

**When would I change it?** Change to control the finest support layers allowed.

**What changes if I adjust it?** Increasing disallows thinner support layers; decreasing permits them.

**Check together with:** Maximum support layer height; Independent support layers; Support type.

**Displayed units:** mm.

**Caution:** Only applies to the supported layer-schedule mode, not Organic trees according to help.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportMinLayerHeight`.

### Tree support generation mode - treeSupportMode

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Selects the source of regions that generate tree supports.

**When would I change it?** Choose based on whether you want automatic detection, manual regions, or both.

**What changes if I adjust it?** Auto uses detected overhangs; Manual uses manually specified regions; Hybrid combines the two.

**Check together with:** Manual support painting/regions; Automatic threshold; Support filtering.

**Selectable choices:**

- **Auto:** Uses automatically detected overhang regions. Schema contexts: Process: general / SUPPORT.
- **Manual:** Uses manually specified support regions only. Schema contexts: Process: general / SUPPORT.
- **Hybrid:** Combines automatic overhang regions and manually specified regions. Schema contexts: Process: general / SUPPORT.

**Caution:** Manual mode does not automatically rescue unmarked overhangs; inspect every unsupported area.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportMode`.

### Remove small overhangs - treeSupportRemoveSmallOverhangs

**Scope:** Process: general / SUPPORT.

**What does it mean?** Filters small clusters from automatic support detection.

**When would I change it?** Use to reduce unnecessary support for tiny overhang islands.

**What changes if I adjust it?** Enabled removes qualifying small automatic regions; disabled retains them.

**Check together with:** Tree support mode; Critical regions; Manual enforcement.

**Caution:** The help says sharp tails, cantilevers, and manually enforced supports are preserved; confirm the actual result.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportRemoveSmallOverhangs`.

### Threshold angle - treeSupportThresholdAngle

**Scope:** Process: fortified / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Threshold-angle field used when tree supports are selected.

**When would I change it?** Change only while checking tree-support candidates in Preview.

**What changes if I adjust it?** The label and degree unit are confirmed, but this field has no linked explanatory tip; exact zero behavior and direction are not independently established here.

**Check together with:** Tree support type/mode; Other threshold-angle field; Manual regions.

**Displayed units:** °.

**Caution:** Do not assume it has identical conventions to another threshold field or another slicer.

**Evidence status:** Exact Rocket behavior remains unverified; preview and emitted-file checks required.. Control ID: `profile-settings:treeSupportThresholdAngle`.

### Top interface spacing - treeSupportTopInterfaceSpacing

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Gap between neighboring lines at the top support interface.

**When would I change it?** Use to balance supported-surface quality against removal effort.

**What changes if I adjust it?** Larger spacing makes the interface more open; smaller spacing adds contact coverage.

**Check together with:** Top-interface layers; Top Z distance; Interface line width/flow.

**Displayed units:** mm.

**Caution:** This is millimeter line spacing, not vertical separation or percent fill.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportTopInterfaceSpacing`.

### Top Z distance - treeSupportTopZDistance

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Vertical clearance between the support top and the model above it.

**When would I change it?** Use when overhang undersides are too rough or supports bond too strongly.

**What changes if I adjust it?** Increasing usually aids removal but gives less support; decreasing moves the support closer.

**Check together with:** Top-interface spacing/layers; Model/support layer schedule.

**Displayed units:** mm.

**Caution:** The achievable gap is affected by layers; verify the actual sliced contact rather than just the input number.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportTopZDistance`.

### Use independent support layer height - treeSupportUseIndependentLayerHeight

**Scope:** Process: general / SUPPORT.

**What does it mean?** Allows conventional and non-Organic tree supports to use a layer schedule separate from the model.

**When would I change it?** Use to tune support efficiency while preserving the model's layer schedule.

**What changes if I adjust it?** Enabled uses the support minimum/maximum height range; disabled follows the ordinary coupled schedule.

**Check together with:** Minimum/maximum support layer height; Support type; Model layer schedule.

**Caution:** Installed help excludes Organic trees from this option. Verify contact interfaces still line up.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportUseIndependentLayerHeight`.

### Tree body wall - treeSupportWallCount

**Scope:** Process: general / SUPPORT.

**What does it mean?** Conventional tree variant: Number of wall loops around each tree-support cross-section.

**When would I change it?** Change when support branches need a different shell strength/material tradeoff.

**What changes if I adjust it?** Auto chooses from the supported wall counts; 1 or 2 requests that many loops where the cross-section has space.

**Check together with:** Branch diameter; Body fill pattern; Line width.

**Displayed units:** loops.

**Selectable choices:**

- **Auto:** Rocket chooses one or two wall loops from the cross-section geometry. Schema contexts: Process: general / SUPPORT.
- **1:** Requests one wall loop around each suitable support cross-section. Schema contexts: Process: general / SUPPORT.
- **2:** Requests two wall loops where sufficient cross-section space exists. Schema contexts: Process: general / SUPPORT.

**Caution:** This is not a vertical layer count. A second loop only appears where the geometry can fit it.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportWallCount`.

### Support/model XY distance - treeSupportXYDistance

**Scope:** Process: fortified / SUPPORT; Process: general / SUPPORT; Process: reinforced / SUPPORT; Process: speedy / SUPPORT.

**What does it mean?** Conventional tree variant: Horizontal distance between tree supports and the model.

**When would I change it?** Use to reduce sidewall bonding or recover support near a boundary.

**What changes if I adjust it?** Larger clearance reduces side contact and available support area; smaller clearance brings branches closer.

**Check together with:** Tree expansion; Branch routing; Top/bottom Z distances.

**Displayed units:** mm.

**Caution:** It does not change vertical contact gaps. Inspect collision avoidance and overhang support together.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:treeSupportXYDistance`.

### Perimeter trim ratio - trimGapRatio

**Scope:** Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Controls the seam-end gap relative to a plastic perimeter's extrusion width.

**When would I change it?** Use for a controlled seam-overfill investigation after material flow is correct.

**What changes if I adjust it?** The installed help describes zero as closed and one as a gap equal to one line width; increasing creates a larger trim gap.

**Check together with:** Perimeter width; Material/feature flow; Seam position.

**Caution:** These are documented reference meanings, not recommended values. Too much trimming can leave a weak or visible gap.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:trimGapRatio`.

### Use classic wall generator - useClassicWallGenerator

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Chooses the classic wall generator instead of the variable-width generator.

**When would I change it?** Use to compare wall-generation approaches on geometry that slices poorly.

**What changes if I adjust it?** Enabled selects classic generation; disabled uses the alternative variable-width path described by the help.

**Check together with:** Minimum feature size; Minimum wall width; Wall transitions.

**Caution:** Changing generator can alter thin-wall coverage and dimensions. Reinspect the entire wall layout.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:useClassicWallGenerator`.

### Version - version

**Scope:** Process: fortified / OTHER; Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Version metadata for the process/template.

**When would I change it?** Change only to follow the template's revisioning convention.

**What changes if I adjust it?** It identifies a revision; the schema alone does not prove a direct effect on print paths.

**Check together with:** Profile name; Saved template history.

**Caution:** A larger version number is not evidence that the profile is tuned or compatible.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:version`.

### Wall distribution - wallDistributionCount

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Number of neighboring walls over which variable-width adjustments are distributed.

**When would I change it?** Use only when variable-width walls show uneven changes near narrow features.

**What changes if I adjust it?** More walls share the width adjustment across a larger wall group; fewer concentrate it.

**Check together with:** Variable-width generator; Wall counts; Minimum wall width; Transitions.

**Displayed units:** loops.

**Caution:** The requested distribution may be constrained by how many walls fit.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:wallDistributionCount`.

### Speed smoothing coefficient - wallSpeedSmoothingCoefficient

**Scope:** Process: general / OTHER; Process: reinforced / OTHER; Process: speedy / OTHER.

**What does it mean?** Coefficient controlling the length of speed-smoothing transitions.

**When would I change it?** Use when speed changes around wall/overhang features are abrupt.

**What changes if I adjust it?** Installed help says smaller positive values give longer, smoother transitions; larger values shorten them; zero disables smoothing.

**Check together with:** Overhang speeds; Wall geometry; Acceleration; Travel/speed limits.

**Caution:** Do not infer 'higher means smoother.' The locale's suggested numeric range is not a machine capability limit.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:wallSpeedSmoothingCoefficient`.

### Wall transition length - wallTransitionLength

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Length over which variable-width walls change width or wall count.

**When would I change it?** Use when width/count changes look too abrupt or extend too far.

**What changes if I adjust it?** Increasing spreads the geometric transition over a longer path; decreasing makes it more localized.

**Check together with:** Variable-width generator; Wall distribution; Transition filtering.

**Displayed units:** %.

**Caution:** Check narrow regions and endpoints in Preview; geometric smoothing does not guarantee extrusion accuracy.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:wallTransitionLength`.

### Wall transitioning filter margin - wallTransitioningFilterMargin

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Margin used to suppress wall transitions that are too close together.

**When would I change it?** Use only to investigate repeated small transitions or missing wall changes.

**What changes if I adjust it?** It alters the transition-filtering distance; increasing generally filters transitions over a wider neighborhood.

**Check together with:** Wall transition length; Variable-width generator; Small features.

**Displayed units:** %.

**Caution:** The exact filtering algorithm is not established by the label; validate the generated geometry rather than relying on a presumed formula.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:wallTransitioningFilterMargin`.

### Wall transitioning threshold angle - wallTransitioningThresholdAngle

**Scope:** Process: general / WALLS; Process: reinforced / WALLS; Process: speedy / WALLS.

**What does it mean?** Contour-angle threshold for switching between different variable-width wall counts.

**When would I change it?** Use when wall-count changes appear at unsuitable corners.

**What changes if I adjust it?** Changing the angle changes which contour turns qualify for a count transition.

**Check together with:** Variable-width generator; Transition length; Feature size.

**Displayed units:** °.

**Caution:** The installed help identifies a minimum qualifying angle; inspect actual corners rather than importing another slicer's convention.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:wallTransitioningThresholdAngle`.

### Wipe tower brim - wipeTowerBrimLoopsCount

**Scope:** Process: fortified / WIPETOWER; Process: general / WIPETOWER; Process: reinforced / WIPETOWER; Process: speedy / WIPETOWER.

**What does it mean?** Number of brim loops anchoring the wipe tower to the plate.

**When would I change it?** Use when a required wipe tower needs more or less bed attachment.

**What changes if I adjust it?** More loops enlarge its attached footprint; fewer reduce it.

**Check together with:** Wipe tower placement; Bed adhesion; Tower wall count; Material changes.

**Displayed units:** loops.

**Caution:** This concerns the tower, not the model brim. Verify the tower fits the plate and does not collide.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:wipeTowerBrimLoopsCount`.

### Wipe tower wall - wipeTowerLoopsCount

**Scope:** Process: fortified / WIPETOWER; Process: general / WIPETOWER; Process: reinforced / WIPETOWER; Process: speedy / WIPETOWER.

**What does it mean?** Wall-loop setting controlling wipe-tower wall thickness.

**When would I change it?** Use when a required tower's shell is too weak or unnecessarily heavy.

**What changes if I adjust it?** More wall loops thicken the tower shell and use more material; fewer thin it.

**Check together with:** Wipe tower brim; Tool/material-change sequence; Tower geometry.

**Displayed units:** loops.

**Caution:** Do not assume a tower is optional when a composite/tool workflow requires it.

**Evidence status:** Installed schema/help supports this explanation; not physically print-validated.. Control ID: `profile-settings:wipeTowerLoopsCount`.

## Template

### Auxiliary cooling fan - auxiliaryFanPowerPercentage

**Scope:** template.

**What does it mean?** An auxiliary-cooling percentage entry in a renderer template, separate from the ordinary tool's main part fan.

**When would I change it?** Only after confirming that this control is actually exposed for the selected hardware and identifying the physical auxiliary fan.

**What changes if I adjust it?** More side/auxiliary airflow may improve some overhangs but create directional cooling or warp; less reduces those effects.

**Check together with:** Layer-index schedule; Main part cooling, chamber and fan channel mapping.

**Displayed units:** %.

**Declared editor constraints:** {"minValue": 0, "maxValue": 100, "step": 1}. These are not operating recommendations.

**Caution:** The control type and exact schedule application are unresolved. A source template does not prove this printer has that fan or that the entry is visible.

**Evidence status:** Renderer-template field; runtime exposure and execution unresolved.. Control ID: `template:auxiliaryFanPowerPercentage`.

### Exhaust fan - exhaustFanPowerPercentage

**Scope:** template.

**What does it mean?** A percentage entry for an exhaust fan in a renderer template, not the hotend or ordinary part-cooling fan.

**When would I change it?** Only when the actual exhaust hardware, ventilation requirements and supported chamber workflow are established.

**What changes if I adjust it?** More exhaust may remove heat/airborne material but lower chamber stability; less may retain heat while reducing ventilation.

**Check together with:** Layer-index schedule; Chamber target and room ventilation.

**Displayed units:** %.

**Declared editor constraints:** {"minValue": 0, "maxValue": 100, "step": 1}. These are not operating recommendations.

**Caution:** Do not reduce ventilation contrary to material safety guidance. Control type, exposure, routing and precise scheduling are unresolved.

**Evidence status:** Renderer-template field; hardware and execution unverified.. Control ID: `template:exhaustFanPowerPercentage`.

### Layer - layerIndex

**Scope:** template.

**What does it mean?** A layer identifier associated with the renderer's layer/fan schedule entries.

**When would I change it?** Only after confirming the visible schedule control and how it identifies the intended printed layer.

**What changes if I adjust it?** Changing the index can move a scheduled event to another layer. It is not automatically a height in millimetres.

**Check together with:** Auxiliary and exhaust fan entries; Actual sliced layer count and variable layer heights.

**Declared editor constraints:** {"minValue": 1, "step": 1}. These are not operating recommendations.

**Caution:** Whether counting begins at zero or one, how duplicates are handled, and whether a value persists after that layer are not established. Verify output before relying on it.

**Evidence status:** Renderer-template field; index convention and control type unresolved.. Control ID: `template:layerIndex`.

## Unclassified

### Unresolved inline selector - type

**Scope:** unclassified.

**What does it mean?** An unresolved selector whose options refer to Plastic, Composite and Any slot types; its human label and reliable parent menu are missing.

**When would I change it?** Do not prescribe a change until the actual dialog, slot purpose and physical tool context are identified.

**What changes if I adjust it?** It appears to classify or filter a slot definition, but the survey does not establish whether it assigns hardware, filters choices or changes routing.

**Check together with:** Slot/material definition; Physical tool mapping and compatible selections.

**Selectable choices:**

- **Plastic:** The Plastic slot-type choice. Exact assignment/filtering behaviour is unresolved; match any actual use to the verified ordinary plastic path. Schema contexts: unclassified.
- **Composite:** The Composite slot-type choice. It does not prove physical matrix/fibre loading or a safe composite command sequence. Schema contexts: unclassified.
- **Any:** The broad slot-type choice in this selector. Its scope is unresolved; it is not permission to interchange ordinary and composite hardware or materials. Schema contexts: unclassified.

**Caution:** Do not interpret Any as universal hardware compatibility or assume selecting Composite loads fibre. The missing namespace/label is an explicit documentation gap.

**Evidence status:** Unresolved namespace/label and exact behaviour; choices preserved as evidence.. Control ID: `unclassified:type`.
