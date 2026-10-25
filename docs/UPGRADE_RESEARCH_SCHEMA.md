# Upgrade research schema

**Living schema notice (2026-10-25):** the initial 148 IDs are historical seed identifiers, **not a size limit**. New UPG-149–182 entries have been added with linked UR-149–182 screening records; the [canonical matrix](../database/upgrade_value_matrix.csv) now contains 182 unique UPG IDs. The historical ADD-001/ADD-002 aliases became UPG-150/UPG-149. Preserve all historical IDs and add more as credible topics emerge. See [OPEN_ENDED_UPGRADE_RESEARCH.md](OPEN_ENDED_UPGRADE_RESEARCH.md).

`upgrade_candidates.csv` retains all 148 original IDs, concepts, systems, benefit labels and lead text. Updated research/fitment status and next-validation fields link to `upgrade_research.csv`. Original lead text remains discovery provenance, not an endorsement.

`upgrade_research.csv` is a one-record-per-concept screening ledger. All rows remain `review_state=open`. This pass has not produced L3 repair-ready records. `literature_reviewed` means an initial literature review or an explicit unsuccessful product search, **not complete verification**. Some rows have only general engineering/factory baseline evidence; they expressly state no exact product was authenticated. A general reference supports its stated principle, not the existence, fitment or benefit of a hypothetical product.

## Fields and interpretation

- `research_id`, `upgrade_id`: stable keys; one review currently per concept.
- `reviewed_on`: ISO date of this research pass; not the publication or price-valid-through date.
- `source_ids`: pipe-separated foreign keys to `sources.csv`. Each new source records publisher, URL, scope, locator, access date and limitations. Search-extract-only or failed full-page retrieval is identified where applicable; a URL alone does not certify all claims on a page.
- `manufacturer`, `product_number`, `product_name`, `oem_number`: documented option or explicitly labeled lead. Empty number means none authenticated. Family names and historical instructions are not purchasable SKUs. Related/disallowed parts can appear for comparison; read applicability before counting products.
- `supersession_or_interchange`: distinguishes a shared catalog reference from a verified Toyota supersession. Seller claims stay supplier evidence.
- `verified_facts`: facts about retrieved documents/product identity, **not an assertion of complete fitment**. An unsuccessful search means not established in this pass, not proof that a product does not exist.
- `production_applicability`, `fitment_status`, `fitment_rationale`: candidate / probable / confirmed / vehicle-validated. None in this pass is confirmed or vehicle-validated. Probable remains conditional, not purchase-ready.
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
