# Felicity open-ended upgrade discovery policy

**Owner decision:** **No fixed numeric ceiling.** The first 148 research entries were a seed catalog, not the final universe of engineering upgrades. As of October 29 2026, the catalog includes **215** catalog IDs with matching research and decision rows (including archived overlapping measurement studies). Those counts are snapshots and must not be used as a stop condition.

## Whole-car engineering objective — top priority, 2026-10-29

**THIS SECTION OVERRIDES THE NARROW PREVENTION-ONLY READING OF THE SECTION BELOW.** The user wants Felicity to improve **every meaningful dimension** of a sound, healthy factory-original 2004 Corolla: ride comfort, NVH, handling/braking, usable performance/power delivery, fuel and accessory efficiency, cabin technology/usability, long-term reliability and durability. Prevention and Toyota defect countermeasures are a valuable subset **not the entire goal**. A manufacturer-engineered damper providing a genuine new adjustable comfort/handling function qualifies even if Toyota never issued a suspension defect TSB. Updated tire technology may also qualify when comparable tests demonstrate relevant gains; 'later' alone is not evidence of improvement.

Track three independent comparisons: **healthy factory original**, **current owner's modified or worn parts** (18-inch wheels and potentially aged struts), and **healthy modern same-geometry alternatives**. Avoid declaring a new product better than healthy OE only because it repairs worn parts, and avoid assigning quantified Corolla gains from tests on another vehicle or tire size. A stock-height engineering modification with explicit application, tradeoffs, complete job economics and controls is preferable to a large speculative catalog.

Prioritize work across **at least these independent vectors**: comfort/impact harshness; cornering/braking; quietness/refinement; driving response; drivetrain/electrical efficiency; reliability/corrosion; convenience/comfort. Fault-specific ECM/catalyst/valve fixes stay in references and should not crowd out positive engineering optimization. Rear roll bars can change slippery-road oversteer and uneven-road harshness; stiffer dampers are not inherently more comfortable. Real vehicle safety defects, especially reported front-end clunks, are diagnosed first.

Read the [active balanced research pass](../research/BALANCED_WHOLE_CAR_ENGINEERING_PASS_2026-10-29.md) and [earlier touring/quality package](../research/MODERNIZATION_PROGRAM.md). Existing IDs were kept; new physical products strengthen matching studies rather than inflate counts. No future arbitrary ceiling on research discovery.

## Healthy-car retrofit priority — owner clarification 2026-10-29

**Highest-priority mandate:** The owner's 2004 Corolla currently has no reported engine/transmission diagnostic trouble codes, and the user wants **retrofit-ready physical improvements over early-production factory parts**, not a catalog dominated by repairs that require MIL/DTCs. Search Toyota later-production design changes, genuine improved superseded parts, and manufacturer-engineered full-system conversions for the exact **June-2003-built US TMMC Corolla LE, 1ZZ-FE/A245E**. See [governing strategy and specific parts](../research/HEALTHY_CAR_PREVENTIVE_ENGINEERING_STRATEGY_2026-10-29.md).

Prioritize preventive designs and service-window opportunities **that could have value before a fault**. Compare the risk of disturbing a healthy original system against documented materials/geometry improvement, target failure mechanism, OEM retrofit compatibility and independent owner long-term outcomes. Never infer superiority from a newer year or part number alone.

Keep three distinct action classes: **(1) defensible proactive improvement after fitment check, (2) install when routine service opens the assembly, (3) fault-only repair/reference**. Explicitly downrank ECM reflash for P0420/P0133, shift-valve repairs without symptoms, and other DTC-specific interventions unless a physical preventable design defect is independently demonstrated. Separate **Toyota improved OE belt tensioner** from **Gates complete decoupler conversion**; never mix mismatched architecture. Retain the full speculative backlog for future verification but do not call its count completed upgrades.

The reported **bilateral front suspension bangs** require mechanical/safety inspection and are independent of check-engine lights; the absence of DTCs does not prove chassis components sound.

## Continuous discovery scope

Search across automotive supplier engineering, Toyota OEM supersessions, interchangeable platform components, peer-reviewed/SAE and DOE research, real test data, and practical DIY adaptations. Candidate performance **includes** fuel used per distance, electrical load/alternator drag, accessory and driveline losses, heat management and A/C burden, road handling and braking, filtration, durability, acoustics, and functionality—not only horsepower.

A potential upgrade can be cheap/easy, moderate DIY, or a complex longer-term engineering project. Owner's **present shopping preference** for <$50 and ~30 minutes is a *filter on buying now*, **not a restriction on discovery or permanent exclusion**. Lighting LEDs may remain in archive but were explicitly deferred from immediate research by owner.

### Admission criteria for additional candidates

1. Identify a **distinct** intervention or subsystem-level optimization not represented by an existing upgrade ID. Before creating an ID, search all catalog concepts for duplicates; if a specific product is merely an alternative for an existing candidate, add it to evidence under that same candidate rather than create a misleading 'new' upgrade.
2. Assign next stable ID (one above the highest existing numeric suffix; calculate the next ID from the highest actual existing numeric suffix; no known upper bound); **never renumber** earlier IDs. Preserve UPG-001–148 historical identities.
3. Link an initial technical screening record (`UR-<matching numerical suffix>`) and at least one actual, traceable source. An indirect general engineering study is explicitly **hypothesis support**, not proof of Corolla compatibility.
4. Record **healthy factory baseline** and owner's *currently modified configuration* separately. State improvement mechanism and whether same-vehicle data, independent component tests, manufacturer claims, or hypotheses support it.
5. Research installation access, special tooling, degree of DIY difficulty, safety, equipment/market/production compatibility, negative tradeoffs, measured performance benefit (or `unknown`), and dated costs (or blank/unknown).
6. Keep `candidate` until actual Corolla-specific product fitment is established, and reserve `confirmed` / `vehicle-validated` for the evidence threshold in [EVIDENCE_STANDARD](EVIDENCE_STANDARD.md).
7. Update **all three connected ledgers**: `upgrade_candidates.csv`, `upgrade_research.csv`, and `upgrade_value_matrix.csv`. The matrix is a **decision view**, not a new independent claim.
8. Run the repository tests, `python scripts/validate_database.py --require-upgrade-coverage`, and cross-check value-matrix unique IDs and source references. Do not silently mask errors or make up test execution.
9. Reassess candidate value when better evidence arrives; do not remove research solely because power/mpg gain was unproven.

## Expansion wave 1 — IDs 149–162 and outstanding validation

| IDs | New themes | Primary limitations |
|---|---|---|
| **149–150** | Windshield solar shade and exterior rain-repellent glass | Previously documented as ADD-002 and ADD-001; aliases migrated to **UPG-149** and **UPG-150** in the canonical matrix to prevent double counting |
| **151–153** | Infrared-rejecting window film, economy feedback coaching, calibrated fuel logging | Window legality, PID accuracy and behavior-mediated economy |
| **154–156** | Add-on tire pressure monitoring, aerodynamic wheel trims, front-wheel airflow deflectors | Actual rim interface, brake cooling, other-vehicle SAE findings not Corolla guarantees |
| **157–160** | Alternator decoupler, accessory-drive speed engineering, localized seat cooling, efficient automotive USB DC-DC charging | No verified Corolla converter/pulley fitment; possible thermal and charging downsides; USB TI reference design is **not a store product** |
| **161–162** | Parked-car side/rear solar shading and cabin-temperature instrumentation | No matched Corolla temperature or quantified fuel savings yet |

**Priority difference:** cheap/easy currently applicable ideas are available (shade, rain repellent, feedback/logging) but harder **system-efficiency engineering ideas** should stay visible without an artificial budget cutoff.

The old supplemental `ADD-001` (rain repellent) and `ADD-002` (windshield shade) were **not separate catalog candidates**. Their canonical IDs are now `UPG-150` and `UPG-149`. No original UPG IDs were changed. This alias record prevents broken referents in older research drafts.

## Evidence references for new themes

- DOE driver feedback: https://afdc.energy.gov/conserve/driving-behavior
- SAE wheel mass and aerodynamic efficiency study: https://saemobilus.sae.org/downloads/papers/2017-01-1533/Full%20Text%20PDF
- SAE front-wheel deflector simulation: https://saemobilus.sae.org/papers/numerical-simulations-a-car-underbody-effect-front-wheel-deflectors-2004-01-1307
- Gates alternator decouplers: https://www.gates.com/gb/en/power-transmission/power-transmission-components/decoupler-pulley.p.7789-000000-000000.v.7789-10003.html
- 3M infrared window films: https://www.3m.com/3M/en_US/p/c/films-sheeting/window/light-control/i/automotive/post-factory-installations/
- NY DMV light transmission rules: https://dmv.ny.gov/document/mv-80w
- TI automotive USB 12V to 5V design (95% peak measured reference circuit, no consumer product validation): https://www.ti.com/tool/PMP21771

**Do not call the new 14 Corolla-approved upgrades.** They are research leads with defined next experiments and fitment checks. The number can and should increase with the evidence.

## Expansion wave 2 — IDs 163–182

20 new candidates were added with source-linked screening records and matched decision-matrix entries. Themes: convenience oil drain (163), ferrous magnetic drain plug (164), grid/solar battery maintenance (165–166), auxiliary undervoltage protection and real-current monitoring (167–168), engine/cold-oil preheat (169–170), hydraulic steering parasitic load alternatives (171–172), variable electric coolant flow (173), energy-aware A/C and fan redesign (174–175), TOP TIER and E0/E10 fuel-economics comparisons (176–177), silicone aero wipers (178), solar parked ventilation (179), steering-fluid thermal control (180), lab oil analysis (181), and safe battery isolation while stored (182).

This wave includes **real documented hardware** (e.g. Fumoto F103SX, GoldPlug AP03, 1ZZ-FE block heater reference), **other-vehicle/system studies** (e.g. variable compressor and solar ventilation), and **open engineering hypotheses**. Their evidence levels intentionally differ. They are **not 20 confirmed fits, mpg upgrades, or buy recommendations**. For example independent cold-start research finds emissions benefits but no reliably net-positive gasoline savings after considering mains electricity.

Linked investigation: [Expansion wave 2 evidence](../research/EXPANSION_WAVE_2.md).
