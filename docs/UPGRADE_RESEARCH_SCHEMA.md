# Upgrade research schema

**Living schema notice (2026-10-25):** 193 stable catalog IDs now have matching research and matrix rows. Four orphaned historical links were restored, two narrative leads migrated, and five distinct concepts added in the latest pass. IDs are open-ended; do not renumber or count restored/overlapping studies as new discoveries. See [open-ended policy](OPEN_ENDED_UPGRADE_RESEARCH.md) and [current buying guide](../research/CHEAP_EASY_BUYING_GUIDE.md).

`upgrade_candidates.csv` retains all 148 original IDs, concepts, systems, benefit labels and lead text. Updated research/fitment status and next-validation fields link to `upgrade_research.csv`. Original lead text remains discovery provenance, not an endorsement.

`upgrade_research.csv` is a one-record-per-concept screening ledger. All rows remain `review_state=open`. This pass has not produced L3 repair-ready records. `literature_reviewed` means an initial literature review or an explicit unsuccessful product search, **not complete verification**. Some rows have only general engineering/factory baseline evidence; they expressly state no exact product was authenticated. A general reference supports its stated principle, not the existence, fitment or benefit of a hypothetical product.

## Fields and interpretation

- `research_id`, `upgrade_id`: stable keys; one review currently per concept.
- `reviewed_on`: ISO date of this research pass; not the publication or price-valid-through date.
- `source_ids`: pipe-separated foreign keys to `sources.csv`. Each new source records publisher, URL, scope, locator, access date and limitations. Search-extract-only or failed full-page retrieval is identified where applicable; a URL alone does not certify all claims on a page.
- `manufacturer`, `product_number`, `product_name`, `oem_number`: documented option or explicitly labeled lead. Empty number means none authenticated. Family names and historical instructions are not purchasable SKUs. Related/disallowed parts can appear for comparison; read applicability before counting products.
- `supersession_or_interchange`: distinguishes a shared catalog reference from a verified Toyota supersession. Seller claims stay supplier evidence.
- `verified_facts`: facts about retrieved documents/product identity, **not an assertion of complete fitment**. An unsuccessful search means not established in this pass, not proof that a product does not exist.
- `production_applicability`, `fitment_status`, `fitment_rationale`: candidate / probable / confirmed / vehicle-validated. None in this pass is confirmed or vehicle-validated. Probable remains conditional. A universal material/interface purchase can be purpose-ready within a documented narrow scope without establishing exact-car or production-specific fitment. Read the matrix buying_scope; candidate fitment cannot be purchase-ready.
- `benefit_basis`: hypothesis, manufacturer_claim, factory_reference, oem_corrective_action, independent_test or vehicle_measurement. A maker's dimension/ISO test is distinct from a car-level outcome.
- `measured_vehicle_benefit`: unknown throughout this pass; no subject-car performance testing occurred.
- `engineering_hypothesis`, `disadvantages`, `diy_requirements`, `next_validation`: analyst engineering proposals and checks, not copied factory installation procedures. DIY level is an estimate; explicit maker installation qualifications are retained. There are no invented labor hours or torque values.
- `cost_usd`: single observed listing only, blank when unknown. `cost_basis` records date, scope, inclusions and uncertainty. Most are parts-only; MWR's installed package is explicitly different. MSRP and out-of-stock listings are not orderable quotes. No total job estimate is complete without tools, labor, consumables, tax/freight and supporting parts.

## Validation

Run:

```sh
python -m unittest discover -s tests -v
python scripts/validate_database.py --require-upgrade-coverage
```

The coverage gate requires every original UPG-001–148 ID, linked research for each candidate, valid references, statuses, dates, DIY levels and costs, catalog/research fitment agreement, and explicit evidence before promoting fitment. Automated tests cannot establish physical compatibility, legality, source authenticity or measured gains. Independent technical review remains pending.

## Decision-matrix purchase fields

The matrix retains legacy evaluations and adds `session_reviewed_on`, `decision`, `purchase_ready`, `budget_tier`, `current_vehicle_baseline`, `procedure_source_ids`, `time_basis`, lifting/fabrication/wiring/calibration flags, supporting components/costs, shipping, annual fuel savings, payback, `benefit_confidence` and `buying_scope`. Empty cost/savings/time fields mean unknown, not zero. A legacy numerical time estimate is not a maker procedure or timed measurement; newly researched rows avoid unsupported minutes.

`purchase_ready=no` and `decision=not_reassessed` are conservative defaults for older rows, not fresh rejections. Decision values are worth_buying, worth_buying_for_specific_purpose, promising_but_unverified, poor_value, not_an_improvement_over_healthy_oem, outside_current_diy_scope, and not_reassessed. Budget tiers are screening judgments; unpriced work remains provisional.

Validation checks every matrix-to-research/source reference, cross-candidate linkage, fitment consistency and full coverage. A purchase-ready row requires healthy baseline, incremental function, observed price/basis, procedure sources, installation requirements, benefit confidence, buying scope and modification flags, plus an affirmative decision and fitment above candidate. This is a data-integrity gate, not independent engineering certification. All sources and procedures still need human technical assessment; no automatic test proves safety, stock, performance or physical installation.


## Modernization audit fields (2026-10-25)

The value matrix now adds `modernization_class`, `modernization_priority`, `modernization_rationale`, `modernization_audit_scope` and `evidence_grade`. All193 rows received a semantic assessment against existing evidence, not193 new part verifications. Six role categories are OEM design revision, maintenance/healthy equivalent, measurement/diagnostic, substantive engineering candidate, function/accessory, and outside-program/adverse tradeoff. A substantive candidate is still an investigation, not a purchase recommendation. Priorities P1/P2/P3 mean conditional shortlist/verify next/defer.

Nine rows have `deep_primary_source_review_2026-10-25`; other rows expressly identify semantic screening. `evidence_grade` states both the supported mechanism and the limits of vehicle-level evidence. The `benefit_basis` field retains the existing machine-readable vocabulary. No new physical fitment confirmations or purchase-ready promotions were made. New columns do not replace existing validation or relax purchase gates.

Full-job budget ranges and installation-hour ranges in MODERNIZATION_PROGRAM.md are **analyst planning estimates**, explicitly distinct from observed parts prices, measured DIY times, warranty labor standards and guaranteed checkout totals. Existing historical numerical estimates have not been recast as measurements.
