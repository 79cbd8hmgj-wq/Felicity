# Felicity — modernization expansion: design gates and next experiments (2026-10-25)

Vehicle research scope: US 2004 Corolla LE, owner-described June 2003 Canadian build, 1ZZ-FE/A245E, aftermarket intake and 18-inch wheels. **No vehicle work or measured gain is claimed.** Complements `research/MODERNIZATION_PROGRAM.md`, not a replacement for its ranked six.

## Research result: three engineering avenues, not three approved purchases

### 1. Highway cruise control — genuinely added function if absent (conditional)
**Candidate hardware:** Rostra Global Cruise 250-1223 universal mechanical-throttle controller, **not yet a car-specific kit fitment approval**. Rostra's published product describes an external servo/throttle cable and compatible controls. Speed-signal source, brake-switch fail-safe, neutral safety, mechanical-throttle identification, cable routing, actuator brackets, electrical diagrams, and OEM cruise-option inventory require verification. Its manufacturer warns against unsupported vehicle installs and other-brand control switches.

- Baseline: if OEM cruise is already operational, adding another controller has **no incremental value**. If absent, potential highway right-foot comfort is a useful function, not a proven fuel saving.
- Complexity: **advanced electrical/mechanical integration**, not an easy $50 DIY job. Do not order or install until a Corolla-specific complete wiring/actuator safety design and manufacturer support are secured.
- Critical validation: brake pedal release immediately cancels throttle demand, throttle returns freely with cruise deactivated, no interference with accelerator, no nuisance activation; test in a controlled environment before road use. Do not splice into SRS wiring.
- Source: https://www.rostra.com/our-products/250-1223
- Verdict: **research only / not purchase-ready**. Compare a verified factory-equipment retrofit before a universal unit. Exact car may already have cruise.

### 2. Existing aftermarket intake — measured design correction versus current configuration
The existing aftermarket assembly is a potential source of **hot underhood ingestion, altered MAF flow profile and intake noise**. This is explicitly an improvement avenue **versus the owner's currently modified vehicle**, not evidence of exceeding a healthy Toyota stock airbox.

- Toyota-related 1ZZ engineering documentation describes a thermally isolated plastic intake manifold and tuned resonator as deliberate features. Separate Corolla repair-manual material confirms intake-air-temperature sensing is integral with the airflow meter. These documents are **1ZZ family principles**; neither verifies a June 2003 US Corolla part number or the currently fitted aftermarket design.
- Controlled A/B plan: photograph full intake path and MAF mount; log IAT/ambient temperature at steady speed and idle-soak, RPM, long/short fuel trims and intake sound on same route/weather/load, repeating trials; ensure no loose tubing or unfiltered bypass.
- Compare: (A) currently installed intake as-is; (B) properly fitted, complete, VIN-matched factory airbox/ducts/resonator; potentially (C) an engineered sealed cold-air enclosure if supported by measurements.
- Do **not** infer dyno horsepower, mpg gains, or fixes from IAT alone. Test with OEM ECU adapting normally; preserve lawful emissions hardware and avoid exposure to rainwater.
- Sources: https://toyotamanuals.gitlab.io/RM01J1E/htmlweb/rm01j1e/ncf/ncf193e/m_eg_0048.pdf (another 1ZZ application); https://toyotamanuals.gitlab.io/RM01J1E/htmlweb/rm01j1e/rm/rm821e/m_05_0158.pdf (Corolla diagnostic reference).
- Verdict: **high-priority inspection/experiment, no purchase approval**. Can affect the owner's actual NVH and calibration without claiming better-than-healthy-OEM performance.

### 3. Spectrally selective solar film — functional heat management, legal purchase gate
A nearly clear, high-visible-transmittance solar film may limit heat admission compared with otherwise healthy untreated glass. The **glass + film assembly**, not the film's standalone rating or marketing name, determines New York compliance.

- NY Vehicle & Traffic Law §375 and NY inspection standard require at least **70% combined visible light transmittance** on relevant windshield and sedan side glass (with specific windshield upper-band/exemption provisions). Verify each applicable pane and the law before application. 
- 3M Crystalline 90's *2020 product sheet* reports **72% VLT** on illustrative Auto 75 glass that measures 73% without film; total solar energy rejected **46% vs 42%**. These are laboratory reference configurations, not measurements of Felicity's glass and not proof of legal compliance. A 1%-2% margin is particularly sensitive to pane-to-pane variation/meter measurement.
- Before buying: meter factory glass, obtain dated **current-market** installer film specifications, calculate/test resulting combined VLT, obtain written inspection-legal confirmation. Ask for full installed pricing and warranty. No DIY recommendation before evaluating installation skill, glass seals/electronics and compliance.
- **Not** assumed to improve MPG, cooling output or cabin comfort by any quantified amount.
- Sources: https://www.nysenate.gov/legislation/laws/VAT/375 ; https://dmv.ny.gov/document/cr-79 ; https://multimedia.3m.com/mws/media/1704851O/awf-crystalline-90.pdf
- Verdict: **conditional premium comfort option / legality and cost unresolved**; compare low-cost parked shade first.

## Four measurement-first additions to the program
1. **Road-trip driver-effort test:** if cruise absent, 45-60 minutes of steady highway drive with seat posture notes; check whether foot/leg strain is a meaningful problem before a complex retrofit.
2. **Baseline intake log:** at least three comparable warm-engine trips, note ambient/IAT differential, fuel trims, acceleration behavior and perceived induction noise. Vehicle has aftermarket intake, so this experiment is relevant now.
3. **Solar-soak test:** shaded/parked windshield shade A/B with similar outdoor conditions and dashboard/cabin thermometer placement. Do not leave thermometers or mounting accessories near airbags.
4. **Measurement provenance:** record ambient weather, tire size/pressure, fuel level, passenger load, route, traffic and repeat count. Smartphone dB and OBD fuel estimates are comparative instrumentation rather than calibrated engineering-grade evidence.

## Engineering disposition
- **Promote to next research gate:** aftermarket intake identification and A/B data (no purchase).
- **Keep option-specific:** cruise only if absent; requires original wiring/service data and fail-safe validation.
- **Defer purchasing:** solar film until actual window VLT and NY legal checks. Do not mistake high IR rejection for high *total solar energy* rejection.
- **No new mileage/power/dB/temperature gain claims.** No part interchange, safety-system compatibility or June-build fitment asserted.
