# A245E transmission and drivetrain efficiency — initial factory-reference investigation (2026-10-25)

Vehicle target: US 2004 Corolla LE, 1ZZ-FE, automatic A245E, assembled June 2003 in Canada. The reported aftermarket 18-inch tire size is 215/45R18. Research only: these findings are **not instructions to alter transmission calibration** and are not measurements on this specific vehicle.

## Documented A245E reference values

Toyota new-car technical features literature for the 1ZZ-FE A245E lists: first 3.643, second 2.008, third 1.296, fourth 0.892, reverse 2.977, differential ratio 2.962; Type T-IV ATF. The source's market/calibration applicability to the subject US June-build car still needs confirmation.

Source: https://toyotamanuals.gitlab.io/RM01J1E/htmlweb/rm01j1e/ncf/ncf193e/m_ch_0100.pdf

April 2003 repair service data supplies lockup reference at **5% throttle**:
- O/D gear: lockup ON 61–69 km/h (38–43 mph); OFF 54–62 km/h (34–39 mph).
- 3rd gear with overdrive main switch OFF: ON 68–77 km/h (42–48 mph); OFF 61–69 km/h (38–43 mph).

These are *specified test conditions*, not universal lockup speeds. Manufacturer service data: https://sinref.ru/avtomobili/Toyota/003_00_Toyota_Corolla_repair_manual_2004_english/008.htm

ECT P0741 diagnostics describe ECM comparison of engine speed and output speed/gear ratio to determine lockup behavior and note shift solenoid SL controls lockup relay valve. Source: https://sinref.ru/avtomobili/Toyota/003_00_Toyota_Corolla_repair_manual_2004_english/045.htm

October 2003-onwards Corolla manual specifies Toyota Type T-IV JWS3309/NWS6500, and cautions that unsuitable ATF can adversely affect shifting and lockup, possibly causing transmission damage. **Manual is later than subject build**, so confirm original June-specific repair/owner documentation. Source: https://manuals.plus/m/59c3523e8a45ccd6bf5529301762fe2822c3f65b183f48e07733c5585dccf8b0

## Four priority investigations, not purchase endorsements

1. **Confirm converter lockup during normal cruise:** collect GPS speed, RPM, road grade and steady light-throttle conditions without driver distraction. Compare with confirmed US drivetrain ratios and actual measured tire rolling circumference. OBD generic fuel/tranny PIDs may be unsupported.
2. **Model shift schedule and lockup fuel economy:** analyze baseline logged gear/lockup behavior and fuel used per 100 miles. Do *not* force the torque-converter clutch, bypass the factory solenoid or alter ECM maps to 'save fuel' without independent hydraulic/thermal durability evidence.
3. **Compare *genuine T-IV compatible* fluids:** find friction-versus-temperature, shudder prevention and shear stability data against healthy Toyota T-IV, not worn fluid. No fuel-economy gain is yet established for a replacement fluid.
4. **Correct cruise RPM and MPG comparisons for current wheels:** original LE reference 195/65R15 versus photographed 215/45R18 nominal-size difference; nominal tire diameter is not the actual loaded rolling circumference. Do not present estimated gear RPM as measured until exact A245E ratios and rolling circumference are confirmed.

## Practical value

The best inexpensive next step is **measurement, not aftermarket transmission parts**. First establish whether this healthy transmission operates at expected cruise ratios and torque-converter lockup conditions, then assess a genuine intervention against healthy original behavior. Extra transmission cooler and valve-body modification are already in the database and should not receive duplicate IDs merely for having a new research angle.

The four detailed investigations above can be added as future distinct candidates only after existing-catalog deduplication and full linkage. No claimed MPG or longevity uplift is currently substantiated.
