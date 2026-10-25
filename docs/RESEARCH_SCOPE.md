# Felicity — Engineering & Restoration Research Scope

**Version:** 1.0 (approved)  
**Status:** APPROVED — baseline research charter  
**Date:** 2026-10-25  
**Chosen direction:** Option B — Full engineering and restoration database  
**Change policy:** Scope approved on 2026-10-25. Further expansion may proceed within these boundaries; material scope changes require an explicit charter revision.

## 1. Mission and success definition

Create a rigorous, maintainable, source-traceable technical knowledge base for a specific 2004 Toyota Corolla LE, enabling:
- Component-level understanding of original systems and their operation.
- Evidence-based diagnosis and repair planning.
- Exact-fit sourcing and validated cross-vehicle/manufacturer substitutes.
- High practical reliability, sensible longevity improvements, and evidence-based performance and drivability modifications.
- Safe, economical owner-performed maintenance and repair where appropriate.
- Permanent recording of physical condition, work performed, expenditure and outcomes.

This is **not** a general Toyota encyclopedia, an automatic repair recommendation engine, or a declaration that the photographed car is mechanically healthy.

## 2. Reference vehicle and applicability

| Attribute | Baseline |
|---|---|
| Vehicle | 2004 Toyota Corolla LE |
| Factory model | ZZE130L-DEPNKA |
| Build | June 2003, Toyota Motor Manufacturing Canada |
| Engine | 1ZZ-FE 1.8L (catalog/factory configuration) |
| Automatic transaxle | A245E (manufacturer label) |
| Axle code | 02A |
| Exterior/interior codes | 1C8 / FA11 |
| Mileage | Owner-reported 100,283 mi on 2026-10-25 |
| Observed equipment | One tire photographed 215/45R18 89V; rest not verified |

**Production-date caution:** owner-supplied manual OM12859U explicitly covers 2004 vehicles **from October 2003 production**, while this car was manufactured **June 2003**. Treat its data as a useful reference, not a blanket VIN-correct source. Obtain date-appropriate Toyota references for build-split-sensitive details.

All research must record: U.S. sales-market applicability, actual production date, Corolla LE grade, 1ZZ-FE, A245E, body/equipment differences, and verified distinctions from later-year or Matrix/Vibe configurations.

## 3. In-scope research domains

### 3.1 Mechanical architecture and operation
Develop assembly-to-serviceable-part hierarchies, operating principles, interfaces, failure modes, and inspection/diagnostic methods for:
- Engine long block, valvetrain, timing chain/VVT-i, lubrication, crankcase ventilation, induction, ignition, fuel and emissions.
- Cooling, lubrication consumables, engine mounts, accessory drive.
- A245E automatic transaxle, fluid circuit, valve body, solenoids, sensors, control strategy, mounts and axles.
- Steering, front/rear suspension, alignment, wheels, tires, hubs and bearings.
- Friction and hydraulic brakes, parking brake, ABS only if equipped.
- Charging, starting, battery, grounds, fuses/relays, instrument panel, communications and engine management.
- Lighting and daytime-running-lamp control, HVAC, cabin filtration and other body electrical.
- Structure, corrosion points, body hardware, closures, restraint systems and safety equipment.

Coverage should include serviceable subassemblies; do not create meaningless individual rows for every bolt unless identity/torque/fitment has practical value.

### 3.2 Factory engineering and service information
Record factory-defined specifications, electrical/mechanical diagrams (links and lawful excerpts only), test procedures, tolerances, torque sequences, lubrication and maintenance, fault-code logic, tooling and repair prerequisites. Distinguish owner's manuals from workshop manuals, wiring manuals and bulletins; log publication identifier, revision and production applicability.

### 3.3 OEM and aftermarket parts
Track Toyota original part numbers, build ranges, supersessions, OEM manufacturer when evidenced, candidate aftermarket SKUs, measured geometry/connectors, verified interchange, availability, and dated retail pricing. Classify evidence as **candidate / probable / VIN-or-physical-fitment verified**. A matching generic search-result fitment entry is not proof. Record disallowed or ambiguous interchange separately.

### 3.4 Failure modes, reliability and diagnostics
Document failure mechanism, symptom patterns, differential diagnosis, objective tests, severity, consequences of continued driving, inspection methods, failure frequency only where defensible denominators exist, and confidence. Explicitly separate a common internet complaint from a statistically measured failure rate. Owner's actual failure state must come from physical observation or diagnostics.

### 3.5 Repair execution and economics
For each actionable job: decision gates, necessary safety support/equipment, tools, parts and consumables, verified OEM procedure references, labor/time uncertainty, DIY feasibility (basic/intermediate/advanced/professional), reassembly inspection, test drive/validation, and sourced **dated** price estimates. Costs should distinguish parts, tools, labor, consumables and unforeseen work.

### 3.6 Reliability improvements / modernization
Investigate repair-versus-upgrade options for documented weaknesses, corrosion protection, electrical efficiency, lighting, material improvements, ergonomic and comfort modernization. Evaluate verified fitment, durability evidence, tradeoffs, load/heat/electrical compatibility, legality and reversibility. Prioritize safe OEM-equivalent solutions; do not claim theoretical upgrades produce measured reliability gains.

### 3.7 Performance, handling and drivability engineering
Performance modifications are explicitly **in scope**, including modifications that also improve reliability, efficiency, durability, handling, braking, throttle response or everyday drivability. Research candidate improvements for intake/exhaust, ECU calibration, cooling, ignition, engine internals, transmission behavior/cooling, suspension, wheels/tires, braking and weight reduction when applicable.

For each proposal, document:
- Baseline condition and objective; expected outcome versus actual measured results.
- Evidence of horsepower, torque, acceleration, braking distance, handling, temperature or fuel-use changes where credible testing exists; no fabricated gains.
- Compatibility with the June 2003 1ZZ-FE/A245E build and existing 18-inch wheel installation.
- Side effects on engine/transaxle longevity, drivability, emissions legality, noise, insurance and maintenance cost.
- Required supporting modifications, tuning, installation, test procedure and reversibility.
- Total cost and gains per dollar compared with simply restoring factory condition.

**Prioritization rule:** Safety-critical work remains a prerequisite for safe operation, but research into reliability, repairability, performance, handling, efficiency, aesthetics and comfort is permitted in parallel. Do not automatically subordinate cosmetic or performance modifications to reliability projects. Evaluate proposals individually by owner goals, measured benefits, cost, risk, legality and mechanical dependencies. Substantial performance builds may be researched without presuming that they are worthwhile or road-legal. Never recommend emissions defeat, safety-system removal, or unverified tuning as a harmless upgrade.

### 3.8 Ownership-specific longitudinal data
Capture dated mileage, inspections, photos (redacted), DTC/freeze frame readings, fluid consumption, MPG, parts/service invoices, repairs, costs, outcomes and future checks. Distinguish **planned** from **performed** and **reported** from **measured**.

## 4. Boundaries / excluded by default

- Whole-model comparisons, ranking other vehicles and expanding the database to an unrelated vehicle fleet.
- Emissions-delete, unsafe lighting or restraint-system bypass. Motorsport and forced-induction concepts may be researched as separately risk-rated proposals, not default recommended street modifications.
- Speculative universal interchange or guessing actual installed options from catalog examples.
- Treating a successful DIY guide as certification of roadworthiness.
- Producing/rehosting complete copyrighted OEM manuals and paid database documents.
- Exposing unredacted VIN, plates, exact location, titles, or sensitive insurance/ownership information in a public repo.
- Automatic purchasing, repair actions or public release of sensitive evidence.

Related models (Matrix, Vibe, other Corolla years, other brands) are in scope **only** as engineering references, verified donor applications or economically relevant parts sources.

## 5. Minimum component record schema

- Unique stable ID; name; parent system / location / function.
- Vehicle applicability and assembly/date/equipment constraints.
- Part numbers (Toyota original, supersession, candidate alternatives) with manufacturer attribution where proven.
- Engineering specs, materials, connectors/dimensions and service limits where available.
- Operational dependencies and common failure mechanisms, evidence strength.
- Diagnostic observations, tests, fault-code links and safe repair prerequisites.
- Service procedure/torque references and special tools.
- DIY level, estimated part/labor costs with currency/date/vendor.
- Current **vehicle condition** (uninspected / observed / tested / repaired).
- Sources: publisher, document, revision, relevant page/section, URL/date accessed; conflicts/unanswered questions.
- Research maturity and independent review status.

Maintain relational links across components, sources, observations, parts, service tasks, repairs and evidence.

## 6. Provenance and confidence policy

Evidence hierarchy:
1. Direct vehicle labels, measurements, verified tests and VIN-matched Toyota service documentation.
2. Factory model-specific guides, Toyota EPC, bulletins and comparable dated factory material.
3. Reputable suppliers and automotive engineering sources with independently corroborated applicability.
4. Technical community reports and anecdotes as **hypotheses**, never quantified prevalence alone.

Every concrete technical claim needs a pointer. Log conflicts rather than silently resolving them. Publication dates and production cutoff matter. Mark absent evidence as **unknown**, not negative. Never convert research confidence into physical-condition confidence.

## 7. Research completeness grades

- **L0 — Inventory:** component/system identified; applicability provisional.
- **L1 — Identified:** function, location, assembly applicability and basic factory specification cited.
- **L2 — Engineered:** operating mechanism, failure/diagnostic logic and manufacturer service references documented.
- **L3 — Repair-ready:** validated parts options, repair instructions, safety/tool requirements, estimates and verification checklist.
- **L4 — Vehicle-validated:** performed inspection/repair/testing on this exact Corolla, with dated mileage and outcome.

**Research target:** L3 for practical serviceable components. L4 only after physical evidence. Exclude trivial hardware from coverage accounting unless mechanically consequential.

## 8. Phased delivery and gates

**Phase 0 — Scope approval.** Review this document and explicitly approve/adjust included domains, exclusions, priorities and evidence standard.

**Phase 1 — Source and schema audit.** Verify build-correct service literature; reconcile older-production differences; normalize current CSV identifiers; test referential integrity; record trustworthy sources.

**Phase 2 — OEM component inventory.** Build system-by-system tree; tag each component with correct build applicability; no guessed part numbers.

**Phase 3 — Diagnostic and failure research.** Primary-source tests, observed vs hypothetical failures, DTC relationships, safety gates.

**Phase 4 — Parts and repair economics.** Confirmed supersessions, cross-vehicle alternatives, dated prices, DIY procedures and validation steps.

**Phase 5 — Modernization and performance evaluation.** Evidence-rated reliability, handling, braking, drivability and power upgrades; measured gains and cost/reliability/legal tradeoffs; no fictional life-expectancy or horsepower figures.

**Phase 6 — Vehicle evidence integration.** Incorporate mileage-based inspections, service records, receipts and testing whenever available. This phase may proceed incrementally throughout the project.

Prioritize **imminent safety and engine-preservation concerns** (oil level, brakes, tires, structural corrosion) for real-world inspection regardless of research phase.

## 9. Quality acceptance tests

A system is not 'complete' until:
1. Scope and applicable vehicle/build range are explicit.
2. Every asserted specification, part number or repair step has a traceable source.
3. Superseded components and source disagreements are captured.
4. Safety prerequisites, diagnosis and post-repair tests exist for repair-ready jobs.
5. Alternative parts are not labeled verified without reliable fitment evidence.
6. Cost estimates show date, geographic market and uncertainty.
7. Data validates (unique IDs, consistent units, foreign keys, legal status values).
8. Research maturity and current-vehicle condition remain distinct.
9. At least one independent pass checks logical errors and unsupported claims.

Completion reporting should show **coverage by system and level**, missing evidence, unresolved fitment conflicts, and user-observation blockers, not a single vague 'percent complete'.

## 10. Approved scope decisions (2026-10-25)

- [x] L3 research coverage goal for practical serviceable components.
- [x] performance and drivability modifications as an explicit research domain, including reliability-supporting upgrades, with evidence-based tradeoffs and risk grading.
- [x] related-vehicle research exclusively for verified mechanical comparability / parts interchange.
- [x] candidate/probable/verified interchange distinction.
- [x] dated costs and DIY requirements as core database fields.
- [x] early-production documentation verification before production-sensitive part recommendations.
- [x] storing only redacted, non-sensitive vehicle identification data in public GitHub.
- [x] phases 1–6, without requiring actual vehicle inspection to begin literature research.

**Approved:** Seven original review items were approved without change. The safety/reliability-over-performance/cosmetics priority rule was rejected and replaced with a balanced, owner-goal-driven modification policy. This charter is the authoritative scope for subsequent Felicity research.
