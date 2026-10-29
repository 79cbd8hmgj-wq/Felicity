# Felicity — October 29, 2026 recovered handoff and next engineering research

## Later continuation: Phase 2 retail discovery

The historical snapshot below is superseded for current counts by [Phase 2](PHASE2_DEEP_RETAIL_DISCOVERY_2026-10-29.md), continued directly from `87968af` without repeating the 40-location audit. Current continuation totals: **262 concepts/reviews, 108 external evaluations, 635 source records**. Phase 2 adds **63 products across 35 labeled subcategories**, five candidate functions (UPG-258–262), evidence extensions for 14 existing concepts, 29 offer observations and 17 stock/access observations (13 actual individual-branch shelf results). No newly confirmed fit, purchase-ready part or installed result is asserted.

Read the [budget catalog](PHASE2_BUDGET_DIY_CATALOG_2026-10-29.md), [engineering comparisons](PHASE2_ENGINEERING_COMPARISONS_2026-10-29.md) and [supplier coverage / specific untouched families](PHASE2_SUPPLIER_CATEGORY_COVERAGE_2026-10-29.md). Those are the next-work map; do not restart addresses or count the original 45 again. Some new products remain indexed-only leads; keep their confidence separate from the primary technical documents and live branch stock. Check the Phase 2 validation log and current Actions run separately from historical CI claims below.

**Purpose:** preserve a durable starting point after a ChatGPT conversation reached its length limit. This file records the `research/upgrade-evidence` branch **as inspected October 29, 2026**; it is **not** a new experiment, an independent factory fitment verification, a part order, or an installation record.

## 1. Non-negotiable vehicle and mission

- **Subject:** U.S.-market 2004 Toyota Corolla LE, made in Canada in **June 2003**, model label `ZZE130L-DEPNKA`, original 1ZZ-FE / **A245E four-speed automatic**. Engine/transmission have been reported without current diagnostic trouble codes, but that report is not a diagnostic test.
- **Observed nonstock state:** aftermarket cone intake; a photographed tire size **215/45R18**. Do not infer that all four installed tires match, that these are OEM wheels, or that current suspension and wheel offsets are verified.
- **Reported safety symptom:** loud front impact banging on both sides over potholes, cause unknown. No suspension/brake performance road testing and no suspension upgrade purchase approval before physical safety inspection, including strut mounts, links/bushings, ball joints, caliper brackets/pad hardware, brake hoses and fasteners.
- **Toyota manual supplied by owner:** OM12859U expressly applies to **October 2003 onward production**, **not** this June 2003 car. Use it for model-level reference only. For VIN/build-critical parts, wiring, brakes, airbags, driveline controls and torque/specification cutovers obtain appropriate early-production Toyota EPC/service documents. Do not publish private VIN or account identifiers.
- **Whole-car objective:** meaningfully exceed a healthy original Corolla in *ride and sharp-impact comfort, handling/braking, drivetrain response, real energy/fuel efficiency, cabin NVH, useful added functionality, and reliability*. Prevention is a pillar, not the entire program.

## 2. Live branch snapshot, not the older screenshot totals

Observed on the GitHub branch on 2026-10-29:

| Research asset | Observed count | Interpretation |
|---|---:|---|
| `database/upgrade_candidates.csv` | **255** `UPG` rows | Research concepts only. Newest UPG-255 is headlamp lens protection film. |
| `database/upgrade_research.csv` | **255** `UR` rows | One linked review per concept in current data; does **not** prove fitment or benefit. |
| `database/sources.csv` | **408** source IDs | Registered source/provenance records, **not** 408 first-party certifications. |
| `database/factory_countermeasures.json` | **28** `FCM` records | Distinct documented studies with applicability gates. |
| `database/local_parts_supplier_candidates.csv` | **28** `LOC` rows | Eight channels; candidate addresses, not confirmed stocked products or exhaustive eligible shops. |

Last inspected pre-handoff commit: `f8b9a55b046eadeaf30c9ac651d5a51f4698de77`, "docs: integrate 25-mile Rensselaer all-supplier sourcing into Felicity index." **GitHub Actions run #364 succeeded** at this commit: https://github.com/79cbd8hmgj-wq/Felicity/actions/runs/40904080378 . A successful validator checks declared data structure, not engineering truth, legal compliance, price, physical fit or in-stock status. Re-check Actions for any later commit; do not carry over #364 success to new commits.

The older conversation screenshot displayed **216 concepts, 28 countermeasures, 294 sources** at that point in time. Those are historical, not the branch's latest state. Older numbers remain in some historical markdown passages by design; do not mistake them for the current totals.

## 3. Avoid losing the previous research

Core recent work, in reverse order of decision importance:

1. [Balanced whole-car engineering](BALANCED_WHOLE_CAR_ENGINEERING_PASS_2026-10-29.md), [measurement and B6 parts completion](WHOLE_CAR_MEASUREMENT_AND_B6_COMPLETION_2026-10-29.md), and [performance/quality package](BALANCED_PERFORMANCE_QUALITY_PACKAGE_2026-10-29.md).
2. [35-concept evidence deep dive: UPG-217–251](NEW_CONCEPTS_217_251_EVIDENCE_DEEP_DIVE_2026-10-29.md), [external market wave 8](EXTERNAL_MARKET_DISCOVERY_PASS_8_2026-10-29.md), [external parts wave 8](EXTERNAL_AUTO_PARTS_DISCOVERY_WAVE_8_2026-10-29.md).
3. [Factory countermeasure backlog](COUNTERMEASURE_BACKLOG_2026-10-29.md), [powertrain engineering](POWERTRAIN_ENGINEERING_PASS_2026-10-29.md), and [brake modernization gate](BRAKE_MODERNIZATION_GATE_2026-10-25.md).
4. [28-place supplier network](RENSSELAER_25_MILE_PARTS_SUPPLIER_NETWORK_2026-10-29.md) and the candidate machine-readable `LOC` ledger.
5. Governance: [evidence standard](../docs/EVIDENCE_STANDARD.md), [unlimited discovery policy](../docs/OPEN_ENDED_UPGRADE_RESEARCH.md), [recommendation criteria](../docs/UPGRADE_RECOMMENDATION_CRITERIA.md), and [database schema](../docs/UPGRADE_RESEARCH_SCHEMA.md).

No part is automatically purchase-ready because it has a manufacturer model-year selector. Do not silently convert proposed, photographed, installed, or measured statuses into one another. Do not create new UPG IDs for additional vendors of an existing physical function.

## 4. High-information research queue (not a parts shopping list)

### A. Safety condition gate, in parallel with research (not a brake/strut diagnosis)

Because the reported pothole banging could reflect mechanical free play or **Toyota front pad/guide bracket rattle** under bulletin T-SB-0046-08, retain differential diagnosis. A specific bulletin's symptom overlap is not proof of cause. Request inspection results, photographs, measurements and actual build equipment before recommending fixes. Until then, no aggressive brake/handling drive tests.

### B. Chassis/ride — demonstrate genuine improvement over healthy original

- **UPG-083 TEIN EnduraPro PLUS `VSL00-B1DS2`**: maker's 2003–08 US ZZE130L stock-height, four-corner adjustable damper lead; 16 joint damping steps. Confirm exact front/rear cartridge IDs, mount/bump-stop/interface package and whether HBS is actually fitted to this application. Healthy-OE sharp impact response is **unmeasured**.
- **UPG-080 Bilstein B6**: front left `35-053460`, front right `35-053477`, rear `24-069243` each side. Four-corner catalog application has been sourced; **fit and comfort superiority on this individual car remain unproven**. Compare firmer body control against potential impact harshness, not just marketing.
- **UPG-101/104/221 wheels/tires**: verify all installed tire markings, original placard and brake clearance before comparing compliant **195/65R15** wheel/tire architecture to the current 18-inch setup. Improvements over *current modified car* must not be falsely described as improvements over *healthy 2004 OE*. New-technology tire choices may improve grip regardless of wheel changes.
- **UPG-089 Whiteline BTR77**: regional E12 application conflict with US ZZE130L; request actual installation drawings, mount/beam interface and material-specific wet/snow tradeoffs.

### C. Brakes, drivetrain response, efficiency and NVH

- **Brakes:** confirm rear drum/disc and ABS hardware in the June build, evaluate Akebono ACT923A and coated rotors as *refinement/service-window* opportunities, not proven shorter-stopping-distance claims. Test and compare tires as part of braking performance. Retain `UPG-194` Toyota brake hardware countermeasure as diagnostic possibility only.
- **A245E:** log supported actual warm cruise lockup/gear conditions before claiming a converter or hydraulic improvement. Maintain TransGo SK A246 and Toyota calibration/solenoid references as conditional, not prophylactic healthy-transaxle upgrades. Preserve correct Type T-IV fluid criteria and early-build applicability gate.
- **Efficiency:** measure watts, route fuel used and corrected rolling circumference. Keep tire load/pressure, A/C conditions, traffic and alternator load matched; no marketing MPG claim for decoupler, LED or lubricant without evidence.
- **NVH:** compare road, impact, door sealing, intake and ventilation noise at like speeds/loads before selecting weatherstripping, localized constrained-layer damping or absorber. Avoid indiscriminate weight additions or blocking drainage.

### D. Genuine 2003–2008 parts evolution

Continue obtaining **early-production vs later Toyota EPC part chains**, especially water pump, thermostat/thermal system, engine/transaxle mounts, steering rack/CV, belt-drive hardware, electrical regulation, seat/HVAC ducts and sealing materials. Record original and revised numbers, exact production/plant breakpoints, companion hardware and whether a healthy original gains anything by substitution. Genuine early-to-late Toyota physical changes are strong leads, but absence of a TSB is not grounds to exclude an engineered modern upgrade.

### E. Convert local supplier discovery to real procurement evidence

Use **~25-mile geographic radius around Rensselaer**, covering conventional stores and independent counters, Auto Value/Fisher/Universal, genuine Toyota dealers, salvage and specialty tool shops. The 28 `LOC` records are only the starting inventory. Compare exact manufacturer SKU across at least two distinct channel types, when possible; gather branch-level **actual pickup availability, real total price, included hardware, return policy, verified fit and tool requirements**. Record *coming soon*, third-party listed and wholesale-only locations honestly; never claim shelf stock from a generic catalog page. Keep supplier address ledger separate from engineering sources.

## 5. Decision framework and next deliverables

For each candidate produce:
- Original healthy-OE function vs new physical function; evidence and explicit comparison baseline.
- Applicability: model/market, TMMC June production, dimensions, mounting, connectors, original vs changed components.
- Measurable outcome or manufacturer-only claim and confounders (restoration vs upgrade).
- Complete installation scope, proper parts and hardware, DIY difficulty, failure modes and safety/regulatory concerns.
- Current local or manufacturer price when genuinely checked; otherwise `unknown`.
- Correct open/conditional/rejected decision and next test. Never assert personal-vehicle validation without inspection.

**Next autonomous research batch:** close a small number of *high-value* mechanical/evidence gates in depth rather than inflate the concept count: (1) missing early-build Toyota chassis/brake original-vs-revised part identities; (2) comparative 15in modern touring/winter tires versus 18in current geometry with independent controlled data; (3) verify TEIN/B6 component package and total four-corner economics; (4) obtain specific 1ZZ/A245E mount, cooling and OEM supplier part evolutions; (5) establish actual two-channel local quotes for the strongest approved low-risk candidates. Log negative findings and inconclusive applicability rather than presenting confident recommendations.

## 6. Continuity rules

- Continue using `research/upgrade-evidence`, not a new standalone research repository or unrelated branch.
- Do not overwrite valid historical documentation just because its totals are older.
- Tests: `python -m unittest discover -s tests -v`, `python scripts/validate_database.py`, `python scripts/validate_countermeasures.py`; verify the GitHub Actions result for **each commit actually created**.
- Record all newly registered sources/provenance in the structured database when evidence justifies it. A supplier's own website is a procurement source, not necessarily proof of an engineering benefit.
- **No new install or purchase-ready claims** from this chat recovery. This document is a navigation/handoff artifact.
