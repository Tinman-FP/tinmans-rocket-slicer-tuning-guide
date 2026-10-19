# Sources and edition basis

Source labels identify what supports a statement. They do not make every linked
document applicable to every Rocket version or printer. Public web sources below
were accessed on October 19, 2026. Dates marked “updated” are page dates, not proof
of when a feature reached a particular installed build.

## Core method and installed software

- **[TG-CORE]** William Tinney, *Tinmans Tuning Guide*, edition 1.0.4,
  October 19, 2026, source revision
  `be346beec61755bc8a1615569b64e94240567ff6`.
  [Pinned source](https://github.com/Tinman-FP/tinmans-tuning-guide/tree/be346beec61755bc8a1615569b64e94240567ff6).
  The printer-neutral experimental method is adapted with attribution under
  CC BY 4.0. Its Orca/Tinman controls are not evidence that Rocket has the same
  controls. Third-party material retains its separate attribution and license.
- **[ROCKET-LOCAL]** Rocket **1.4.0.705**, installed-build field inventory.
  Read-only inspection of bundled field definitions, labels and defaults can
  establish what that build contains. A static definition alone does not prove
  that a control is visible in every mode, that a saved value reaches G-code, or
  that a printer executes it. Relevant observations belong in the field reference
  with their visibility and validation limits.
- **[OEM-MANUAL]** Manufacturer-authored [FibreSeeker 3 User Manual R1](https://fccid.co/api/files/s2/fccids/2BVZ6-FIBRESEEKER3/files/6a1adb68_13_FibreSeeker_3_Users_Manual_R1.pdf),
  publicly filed copy, 34 pages. Section1.2.3, printed page4/PDF page7 identifies
  separate matrix, fiber and FFF paths; section3.3, printed page22/PDF page25 gives
  the material-loading order. Those pages were text-checked and visually reviewed
  for this edition. Apply the manual only where it matches current tooling/firmware.
  The manual and its diagrams are linked, not redistributed.
- **[NEW-UNIT-RECORD]** Owner's private current-unit evidence. This label is used
  only for explicitly identified local observations, not general Rocket behavior
  or public instructions. It does not publish unit identifiers, firmware dumps,
  connection details or account information, and it does not transfer results
  from an earlier machine.
- **[ROCKET-HISTORY]** William Tinney's historical, version-specific Rocket export
  comparisons and machine observations. These support explicitly bounded examples,
  not generic tool routing or new-machine tuning. Raw exports, embedded session data
  and private machine records are not distributed. Their prior experimental limits
  are not manufacturer ratings.

## FibreSeek primary sources

- **[OEM-SOFTWARE]** [Rocket Slicer software page](https://www.fibreseek3d.com/software.html).
  Undated. Official product name and download entry points; unversioned download
  links do not identify build 705.
- **[OEM-SUPPORT]** [FibreSeek Support](https://www.fibreseek3d.com/support.html).
  Undated. Links the official wiki and video channel. A linked video is not
  treated as reviewed instruction when no transcript or viewing evidence exists.
- **[OEM-QUICKSTART]** [Rocket Slicer Quick Start Guide](https://wiki.fibreseek3d.com/en/software/rocket-slicer/quick-start).
  Created July 30; updated October 10, 2026. Sections on modes, masks, layups,
  template copying, connection and preview. Not a complete build-specific field
  dictionary.
- **[OEM-140]** [Rocket Slicer 1.4.0 release notes](https://wiki.fibreseek3d.com/en/software/rocket-slicer/release-notes/rs-v140).
  Titled September 2026 update; page updated October 10, 2026. Some preview work
  is explicitly described as pending merge or validation. No 705 suffix is given.
- **[OEM-141]** [Rocket Slicer 1.4.1 release notes](https://wiki.fibreseek3d.com/en/software/rocket-slicer/release-notes/rs-v141).
  Created and updated October 16, 2026. Later-version changes only; not proof of
  installed 1.4.0.705 behavior.
- **[OEM-SPEC]** [FibreSeeker 3 product specification](https://usstore.fibreseek3d.com/products/fibreseeker-3).
  Undated. Manufacturer hardware specifications, not measured capabilities of a
  particular unit. The store's older “Aura” software name is not used as Rocket
  version evidence.
- **[OEM-SHELL]** [Improving Shell Quality](https://wiki.fibreseek3d.com/en/printers/FibreSeeker3/troubleshooting/poor-shell-quality).
  Created August 24; updated October 10, 2026. The page's 0.4 mm/PETG examples
  must not become universal 0.7 mm or PCTG defaults.
- **[OEM-FIRST-LAYER]** [First Print Failure](https://wiki.fibreseek3d.com/en/printers/FibreSeeker3/troubleshooting/first-layer-print-failure).
  Created August 14; updated October 10, 2026. First-layer troubleshooting,
  including separate checks for adhesion, temperature and nozzle gap.
- **[OEM-FIBRE-CAL]** [Fibre Layer Defects](https://wiki.fibreseek3d.com/en/printers/FibreSeeker3/troubleshooting/fibre-layer-defects).
  Created September 18; updated October 10, 2026. Includes touchscreen fibre-feed
  calibration; this is not a Rocket plastic-flow test generator.

## Material-manufacturer sources

These sources concern **3D-Fuel Pro PCTG**. They do not establish a
FibreSeek-specific preset, CFC compatibility or the identity of an unverified spool.

- **[3DF-BASE]** [Baseline Pro PCTG Settings for Printers Without a Profile](https://support.3dfuel.com/hc/en-us/articles/33676470547095-Baseline-Pro-PCTG-Settings-for-Printers-Without-a-Profile).
  Updated October 14, 2026. Vendor starting guidance, not a tuned Rocket profile.
- **[3DF-DRY]** [Drying and Storing Pro PCTG](https://support.3dfuel.com/hc/en-us/articles/44227409816727-Drying-and-Storing-Pro-PCTG).
  Updated October 14, 2026. Material conditioning and storage guidance.
- **[3DF-PA]** [Pressure Advance: Why It Matters for Pro PCTG](https://support.3dfuel.com/hc/en-us/articles/44227435834135-Pressure-Advance-Why-It-Matters-for-Pro-PCTG).
  Updated October 14, 2026. Explains the material's pressure response; it does
  not document a Rocket pressure-advance control or numerical range.

The [structured publication source index](source-index.json) records public links, dates and sections;
private research artifacts are not part of the public download. It is an index,
not a replacement manual.
See [Versions and evidence](guide/07-versions-and-evidence.md) before transferring
a setting, test or result between editions.
