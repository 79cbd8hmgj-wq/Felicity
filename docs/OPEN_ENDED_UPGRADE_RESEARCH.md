# Felicity open-ended upgrade discovery policy

**Owner decision:** **No fixed numeric ceiling.** The first 148 research entries were a seed catalog, not the final universe of engineering upgrades. As of October 25 2026, the catalog includes **162** distinct candidate concepts and 162 matching initial research records. Those counts are snapshots and must not be used as a stop condition.

## Continuous discovery scope

Search across automotive supplier engineering, Toyota OEM supersessions, interchangeable platform components, peer-reviewed/SAE and DOE research, real test data, and practical DIY adaptations. Candidate performance **includes** fuel used per distance, electrical load/alternator drag, accessory and driveline losses, heat management and A/C burden, road handling and braking, filtration, durability, acoustics, and functionality—not only horsepower.

A potential upgrade can be cheap/easy, moderate DIY, or a complex longer-term engineering project. Owner's **present shopping preference** for <$50 and ~30 minutes is a *filter on buying now*, **not a restriction on discovery or permanent exclusion**. Lighting LEDs may remain in archive but were explicitly deferred from immediate research by owner.

### Admission criteria for additional candidates

1. Identify a **distinct** intervention or subsystem-level optimization not represented by an existing upgrade ID. Before creating an ID, search all catalog concepts for duplicates; if a specific product is merely an alternative for an existing candidate, add it to evidence under that same candidate rather than create a misleading 'new' upgrade.
2. Assign next stable ID (`UPG-163` onward, no known upper bound); **never renumber** earlier IDs. Preserve UPG-001–148 historical identities.
3. Link an initial technical screening record (`UR-<matching numerical suffix>`) and at least one actual, traceable source. An indirect general engineering study is explicitly **hypothesis support**, not proof of Corolla compatibility.
4. Record **healthy factory baseline** and owner's *currently modified configuration* separately. State improvement mechanism and whether same-vehicle data, independent component tests, manufacturer claims, or hypotheses support it.
5. Research installation access, special tooling, degree of DIY difficulty, safety, equipment/market/production compatibility, negative tradeoffs, measured performance benefit (or `unknown`), and dated costs (or blank/unknown).
6. Keep `candidate` until actual Corolla-specific product fitment is established, and reserve `confirmed` / `vehicle-validated` for the evidence threshold in [EVIDENCE_STANDARD](EVIDENCE_STANDARD.md).
7. Update **all three connected ledgers**: `upgrade_candidates.csv`, `upgrade_research.csv`, and `upgrade_value_matrix.csv`. The matrix is a **decision view**, not a new independent claim.
8. Run the repository tests, `python scripts/validate_database.py --require-upgrade-coverage`, and cross-check value-matrix unique IDs and source references. Do not silently mask errors or make up test execution.
9. Reassess candidate value when better evidence arrives; do not remove research solely because power/mpg gain was unproven.

## Expansion wave 1 — new IDs and outstanding validation

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
