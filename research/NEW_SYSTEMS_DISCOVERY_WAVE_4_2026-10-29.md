# Felicity — discovery wave 4: coolant-loss detection, forward-collision warnings, active cabin filtration

**Date:** 2026-10-29. **Vehicle:** 2004 U.S. Corolla LE, June 2003 TMMC Canada, ZZE130L-DEPNKA, 1ZZ-FE / A245E automatic. **Scope:** New *functions* absent from the existing 238-concept catalog, not additional brands, accessories or unproven replacement parts. No modification installed or purchase-ready. Current report of loud front pothole bangs remains a chassis inspection safety hold before road performance tests.

## Decision summary

Three manufacturer-supported technologies add functions missing from original stock engineering. They differ in strength of Corolla-specific compatibility:

| Upgrade | Newly available function | Documentary strength | Actual fitment status | Practical priority |
| --- | --- | --- | --- | --- |
| UPG-239: Davies Craig 1040 | Direct low-*liquid*-coolant warning, distinct from ECT measurement | Maker primary product, current USD221.40, dimensions and install limits | Candidate; **35mm upper hose connection not measured** | Investigate if hose fit confirmed; never create a new coolant leak to prevent an unlikely failure |
| UPG-240: Mobileye 8 Connect | Camera-based forward crash/headway/VRU and lane warnings | Maker official fleet retrofit with technical installation guide | Candidate; **private-car sales, camera calibration and wiring unknown** | Possible major driver-alert feature but pro-only/high-cost and warning-only |
| UPG-241: IQAir Atem Car | Active HEPA/gas-media cabin recirculation powered outside existing HVAC | Manufacturer car-mounted product and US electrical spec; USD399.99 | Candidate; **2004 headrest, airbag and electrical placement uninspected** | Optional refinement / occupant-zone particle filter; not a substitute for HVAC clean filter |

All source references are recorded with limitations in `database/sources.csv`; matching UR and value-matrix rows preserve one-to-one links, no duplication of existing UPG-028, UPG-128 or UPG-136.

## UPG-239 — independently sensed coolant *level* warning

**Manufacturer:** Davies Craig **Low Coolant Alarm Probe Style Kit 1040** (12/24V). This **replaces #1035**; do not quote old 1035 pricing or assume sensor compatibility. Current maker page: https://daviescraig.com/product/low-coolant-level-alarm-probe-kit-35mm-adapter1040/low-coolant-level-alarm-probe-kit-35mm-adapter1040 . Manufacturer explains why coolant temperature can mislead after an empty hose/rapid leak in the earlier engineering article: https://daviescraig.com/blog/davies-craigs-brand-new-low-coolant-level-alarm-kit . An early 2003 Corolla owner's manual says to visually check the expansion bottle LOW/FULL marks; no full-time low-level electronic sensor is established for the subject vehicle: https://manualzz.com/doc/60199399/toyota-corolla-2003-owner-s-manual .

**Technical hardware:** 35 mm upper radiator hose inline adapter, vertical liquid probe, in-cabin electronic display, audible and visual low-level alert, adjustable 15–90-second delay, auto-reset. Maker displays **USD 221.40** excluding any additional hose, clamps, tools or labor. No factory 1ZZ hose measurement or sensor installation image has been observed.

**Novelty:** UPG-028 monitors *coolant temperature*. A direct level warning is a separate physical variable/sensor and can signal hose rupture before the temperature gauge is trustworthy. Temperature gauge and OEM ECU still operate normally.

**Risk:** Cutting into a functional high-temperature pressurized hose creates additional failure points. A loose coupler, trapped air, insufficient straight tube, wrong diameter/reducer or wrongly oriented sensor may become **more dangerous than the failure it targets**. Check genuine engine hose ID, position vs bleeder/thermostat, coolant pressure, release tubing, engine vibration, fan clearance, electrical fused supply and alarms before any proposed installation. **Do not connect ignition-kill control while driving** (maker lists optional relay possibilities). Favor an aftermarket or OEM retrofit only where the installation risk and real benefit make sense.

**Evidence:** Supplier design + generic 2003 Corolla factory-era manual. **No 2004 TMMC direct fit or quantified saved engine damage.** Do not infer numerical durability gain.

## UPG-240 — forward-looking camera collision and lane warnings

**Manufacturer:** Mobileye **Mobileye 8** professional retrofit for fleet vehicles https://ims.mobileye.com/fleets/us/products/mobileye-8-connect/ . The official technical guide https://static.mobileye.com/website/common/files/Mobileye%208%20Connect%E2%84%A2%20-%20Technical%20Installation%20Guide%20-HW5.6q.pdf emphasizes that it alerts the driver and does **not** drive, brake or replace observation.

Maker currently describes forward and urban forward collision warning, lane-departure warning, pedestrian/cyclist collision alert, headway monitoring and speed indication. Camera behind interior mirror, alert display and GPS unit are manufacturer-described architecture. Relevant detection depends on road markings, clear view, season/snow/rain, lighting and target visibility. No false-negative/false-positive rates valid for this Corolla have been published in sources reviewed.

**Novelty:** Existing UPG-224 is rear-looking blind-spot/cross-traffic radar; UPG-219 reverse parking sensors; UPG-192 is a passive recording dashcam; none supplies this dedicated **forward-facing real-time visual safety warning suite**.

**Gate:** Manufacturer's current U.S. page is fleet-oriented, not evidence an end-consumer can order a 2004 Corolla retail kit. A current authorized dealer must validate that a 2004 TMMC sedan can be installed, calibrated, connected without undesirable ECM interference and supported over time. The features provide **warnings, not automatic emergency braking**. No engineering permission to integrate with Toyota ABS or steering actuators. Treat professional and cost-unquoted.

## UPG-241 — powered cabin particulate + gas-phase air purification

**Manufacturer:** IQAir **Atem Car** U.S. retail https://www.iqair.com/products/air-purifiers/atem-car . Official electrical and performance sheet: https://www2.iqair.com/sites/default/files/documents/1566_AtemCarTechSpecs_Update_US.pdf .

**Listed engineering data:** 12–24V input with car 12V adapter, headrest strap/mount, **7/12/18 cfm** default filtered airflow (higher max flow may be listed but do not infer default energy use at MAX), maker default electrical **under 1.5 / 1.9 / 3.4 W** depending on default speed, total with mounting **about 5.28 lb**, replaceable HyperHEPA Plus with gas-phase media, manufacturer retail **USD399.99**. Claims of filtration efficiency apply to the media under manufacturer test assumptions, **not a 99% whole cabin reduction** during highway fresh-air ingress.

**Novelty:** Existing UPG-128 investigates **passive factory HVAC filter media**. This option supplies another **fan**, fresh filter media and a local directed flow path into occupant breathing area, independent of blower/HVAC. Can add targeted cabin air recirculation or run with the car switched on.

**Gate:** Actual 2004 Corolla LE seat/headrest shape, rear seat occupant proximity, any side-curtain airbag concerns, child seat placements, power socket voltage and safe secure mounting unverified. This is an expensive option, not a guaranteed net air-quality gain. First confirm existing cabin air filter seating, outside air recirculation setting, filter changes and **actual in-cabin PM2.5**; then compare at equivalent passenger/vehicle HVAC settings. Inspect device attachment crash safety. Power use is low on paper but noise may offset comfort.

## Explicit novelty rejection and deeper engineering caveats

**A. Engine and transaxle mounting:** Toyota catalogs clearly identify multiple early 2004 physical isolator components and a front mount **12361-22090 → 12361-0D100** service part replacement (https://www.toyotapartsdeal.com/oem/toyota~insulator~engine~mounting~front~for~transverse~12361-22090.html), plus multiple RH motor mount part branches (e.g. 12305-0D021 vs 12305-0D022) and hydraulic-type aftermarket listings. These prove **factory part applicability and replacement**, **not** that the newer mount's rubber compound, cavity fluid, NVH transmissibility or durability is better than healthy June-2003 OE. Record as cross-reference research, not a fictitious new improvement ID. Existing UPG-073 covers transaxle stiffness options, and the project's later factory revision pillar can expand if genuine measured engineering change is discovered.

**B. Acoustic windshield/glazing:** Toyota's actual 2004 Corolla glass references (e.g. **56101-02050**, green **laminated**, approximate 4.76 mm) do **not** prove a later generation *acoustic polymer interlayer* exists with 2004 exact mounting and legal windshield certification. General Toyota acoustic-lamination brochures refer to other vehicles, not this build. No candidate ID admitted without Corolla-specific product/factory engineering support.

**C. Aftermarket HUD fitment conflict:** Manufacturer HUDWAY Drive markets GPS/OBD display (https://hudway.co/drive) but explicitly lists **Toyota Corolla 2002–2008** in its **windshield/dashboard geometry exclusion** list. That is negative manufacturer application evidence. We therefore did not create a head-up display purchase candidate based on the advertisement. A different verified 2004-compatible mechanically secure device could be a future genuinely distinct display-engineering research candidate.

**D. Digital electric radiator fan controllers:** Davies Craig GEN II **0480** is current successor to old **0444**, source https://daviescraig.com/product/digital-thermatic-fan-switch-kit-gen-ii-0480/digital-thermatic-fan-switch-kit-gen-ii-0480 ; manufacturer specifically says an *after-shutdown fan alone* is not meaningful without circulating coolant. This remains within already catalogued UPG-025 engine cooling fan behavior/efficiency (and UPG-173 electric coolant pump feasibility). Do not create a new ID to duplicate same radiator fan functionality; changing original ECU thermal logic without proper integration risks overheating.

**E. Mechanical ride upgrade/noise:** Existing fender liners and factory 2004 hood insulators are baseline OE hardware, not verified modern technology. Stock replacement/repair is subordinate unless new physical redesign or full-system healthy comparison is found. UPG-129/131 already cover damping/absorption classes, so do not inflate the concept count merely for an OEM felt pad. We have no legitimate 2004 Corolla acoustic-glass factory part or measured lower transmission mount transmissibility.

## Outcome

Three **new, distinct, manufacturer-sourced technologies** in `UPG-239` through `UPG-241`, matching `UR-239`–`UR-241`, value-matrix decisions and **seven new sources**. Catalog now **241 research concepts, 241 linked studies, 343 source records**, pending automated CI validation. Old IDs and records preserved; new fitment statuses remain **candidate**; no purchase, installation, or whole-car claim of demonstrable reliability or efficiency gains.

### Priorities for future new discovery

New mechanical engineering should require actual increase in capability over a healthy OE baseline (adaptive isolation, engineered bearing/mount improvements, improved brake hardware material, vibration shaping or matching OEM later-production component), not just an unverified retail part. Favor exact U.S.-market TMMC 1ZZ-FE/A245E fit, material drawings, measurable engineering advantage and DIY appropriateness, while retaining system-wide search across the vehicle. Follow already established suspension/body safety precautions: source of severe front pothole bangs must be safely diagnosed before any road performance evaluations.
