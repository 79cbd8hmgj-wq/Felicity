# Felicity — Source and Interchange Evidence Standard

**Approved research scope:** [Engineering charter](RESEARCH_SCOPE.md)  
**Established:** 2026-10-25  
**Role:** Phase 1 evidence policy; applies to original components, cross-manufacturer substitutes, upgrades and performance modifications.

## Separate questions

1. **Document authenticity:** Is this source an identifiable Toyota publication, OEM catalog, engineering document, manufacturer specification, test or owner observation?
2. **Model applicability:** What year, market, model code, engine and transmission does it cover?
3. **Production applicability:** Does it establish a manufacturing period or serial/production breakpoint? Unknown is not equal to confirmed compatible.
4. **Physical compatibility:** Are dimensions, interfaces, connectors, seals, tolerances and installation requirements consistent?
5. **Functional compatibility:** Will the part preserve system operation and required safety/emissions behavior?
6. **Vehicle validation:** Was that precise configuration installed/tested and documented on this car?

## Document evidence types

- **Toyota owner manual:** baseline operating and capacity information; not a parts interchange catalog or workshop service manual.
- **Toyota EPC / factory repair manual / electrical wiring diagram:** high-value OEM identification and procedures, subject to market and production revisions.
- **OEM manufacturer technical sheets:** dimensions and operating ranges; an OEM branding match alone does not establish identical application.
- **Independent engineering/test report:** useful where method, setup and measurement are available.
- **Seller listings, enthusiasts, forums and anecdotal reports:** research leads or candidate evidence; no automatic fitment promotion.
- **Owner photo or measurement:** evidence of current installation only; does not automatically show factory equipment, design intent or durability.

OM12859U is Felicity's **primary 2004 Corolla owner's manual**. Its printed footer says **from October 2003 production** while the car is June 2003 production. This is a documented limitation for build-sensitive claims, not a general prohibition on researching the car. OM12744U is a distinct **2003 model-year** comparative manual; a second OM12859U PDF is a duplicate publication, not independent corroboration.

## Fitment evidence levels

| Level | Meaning | Permitted conclusion |
|---|---|---|
| Candidate | Plausible engineering match, fitment unproven | Further study needed; do not recommend direct purchase |
| Probable | Strong cross-reference and measured or documented compatibility, with remaining gaps | Identify unresolved checks before use |
| Confirmed | Production-correct OEM reference or comprehensive supported fitment proof, with all critical compatibility checks | Can be described as supported for the documented configuration |
| Vehicle-validated | Installed and relevant function verified with dated evidence on the subject car | Verified installed result, not universal fitment |

**Rules:** Never promote a part on brand similarity alone. Do not confuse a parts catalog listing with evidence of current installed condition. Record conflicting catalog breakpoints without silently resolving them. A validated part in another Corolla is not necessarily validated for this car.

## Research and performance modifications

Engine, intake, exhaust, ignition, cooling, driveline, suspension, braking, wheels, electronics, comfort and cosmetic improvements can be researched **without a blanket category priority**. For proposed performance changes, record baseline, manufacturer claims versus measured outcomes, required support changes, durability, drivability, emissions and safety constraints, cost and reversibility.

Existing photographed aftermarket equipment is an **installed-observed modification**, not an OEM fitment record and not proof of a power gain. No maintenance or corrosion investigation is required for research advancement unless the owner explicitly requests it.

## Minimal evidence record per future part

- Stable part and component IDs; exact manufacturer and part number where known.
- Source ID and page/catalog locator; retrieval date, market, production applicability and any supersession.
- Interface/geometry/electrical/material compatibility evidence, plus unresolved gaps.
- Candidate/probable/confirmed/vehicle-validated state with rationale.
- Supporting procedure, cost and risks only where sourced; never guess values.
- Independent owner-installed observations remain separate from factory baseline.

## Source citation conventions

Record **printed page** and **PDF page** independently when different; indicate which numbering system was used. Source content should be quoted minimally and linked rather than copying proprietary manuals into GitHub. Maintain private identifiers outside the public repository. Missing evidence should be visible as pending.

## Phase 1 acceptance check

Existing source identifiers and CSV foreign keys must validate; owner manual source identity is canonical; provenance and documentation limitations remain visible; source-specific claims are not treated as exact replacement-part fitment. Passing automated tests and GitHub Actions must be separately confirmed before declaring the executable validation gate complete.
