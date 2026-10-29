# Felicity structured database v1

Machine-readable CSV tables with stable identifiers, provenance, applicability and verification states. Readable in spreadsheet software, Python, SQLite, DuckDB, or a web app. **No unredacted VIN or ownership documents.**

See [engineering source and interchange evidence standard](../docs/EVIDENCE_STANDARD.md) for applicability, citations, confidence levels and performance-modification research.

Tables:
- `vehicle.csv`: one vehicle/build record, confirmed vs reference attributes.
- `components.csv`: a 28-item inventory with explicit `parent_id` links for applicable subgroups, checked for missing parents and cycles. Detailed assembly breakdown remains future research.
- `specifications.csv`: 26 reference/observed specifications, now linked to component IDs and explicit production-scope classification.
- `service_tasks.csv`: tasks and checkpoints; due state is **unknown** without repair history.
- `observations.csv`: what was seen/reported on this car, separate from reference facts.
- `sources.csv`: where each claim came from.
- `parts.csv`: OEM/aftermarket components and *verified* fitment only; starts with headers, not invented part numbers.
- `repairs.csv`: completed-work ledger; starts with headers, not fictional service.

Evidence codes:
- `owner_report`: explicitly stated by owner
- `label_photo`: photographed on vehicle label
- `tire_photo`: legible tire marking
- `factory_manual`: original Toyota owner's manual, not a workshop manual
- `catalog_reference`: parts/catalog entry; fitment requires verification
- `research_pending`: a required check, no factual claim

Confidence is about the **claim** and does not prove current health. Use `factory_reference`, `observed`, `owner_confirmed`, `pending` statuses; do not equate unknown maintenance with missed maintenance. Every repair must get a dated record and supporting details.

## Workflow
1. Add component-specific findings with explicit evidence and applicability.
2. Add candidate part numbers only after source checking; distinguish candidate/confirmed and note production-date split.
3. Log service only upon completion; attach non-sensitive receipts/photos separately.
4. Keep up-to-date system summaries and links in the main README.

**Primary 2004 owner-manual reference:** Toyota OM12859U, the published 2004 Corolla owner's manual. Its printed scope states October 2003-onward production while this car was built June 2003. Use it for general 2004 operational/specification research; verify build-sensitive part numbers, wiring and procedures against relevant Toyota EPC/service information. Do not block all model-level research because of this caveat.

## Phase 1 audit status

See [Phase 1 audit](../docs/PHASE1_AUDIT.md). The Python validator checks declared source, component-parent, task-component and vehicle references. A new `claims.csv` stores baseline field-level provenance; further normalization is still needed. The scope calls for relational integrity and test coverage before claiming engineering-grade completeness. Model-specific figures from OM12859U are provisional where early-build applicability is material.

## Validation commands

Run from repository root: `python -m unittest discover -s tests -v` and `python scripts/validate_database.py`. The GitHub Actions workflow runs on changed database and validation files. It checks existing stable IDs, source references, status values, CSV row shape and forbidden sensitive identifier columns. **Current CSV schema includes hierarchy, specification component links and a separate claim ledger, but is not yet fully normalized; the validator does not claim all engineering data are verified.

### Additional evidence data

- `claims.csv`: 10 baseline field-level provenance claims referencing the vehicle and specific sources; not a list of measured mechanical conditions.
- `components.csv`: `parent_id` is optional for root-level categories; where present it must point to another component and not form a cycle.
- `service_tasks.csv`: `component_id` refers to existing inventory groups; legacy human-readable `system` remains for compatibility.

## Specification migration (2026-10-25)

Every existing specification has a `component_id` referring to `components.csv` and `build_applicability` distinguishing `manual_scope_oct_2003_onward` from `individual_vehicle_observed`. The 18 manual-sourced specification entries retain the printed October-2003-onward limitation; eight vehicle observations are not treated as manual-derived. The validator enforces component links and legal scope values. It does **not** prove production fitment, accurate reference page numbers or successful execution of all tests. No new parts or repairs were asserted.

## Integrity verification distinction

On 2026-10-25 a direct cross-table check of the nine current CSV files found zero duplicate primary IDs and zero missing nonblank references in existing records. This is a check of database consistency, not an executed run of the Python tests and not a verification of every engineering specification. GitHub Actions status remains unconfirmed.

## Countermeasure discovery extension (2026-10-29)

`factory_countermeasures.json` adds structured factory/supplier studies keyed by stable FCM IDs and linked to existing UPG catalog IDs. It records original/revised relationships, documentary application, June2003 applicability, actual-vehicle verification and installation status separately. Null cost means unknown, not free. Intervention categories distinguish engineering improvements, restoration/serviceability and diagnostic references. Exclusions and maintenance handling practices do not inflate the candidate count.

`consumer_outcomes.csv` is an evidence ledger, **not Felicity's repair log**. Each OUT ID identifies the reporter's vehicle, intervention/result, follow-up limitations and whether it qualifies for Level B. Cross-market, different-part and unresolved reports remain useful evidence without becoming successful exact-remedy corroboration.

Run `python scripts/validate_countermeasures.py` as well as the existing tests/CSV validator. The supplemental check validates links, identifiers, price structure and evidence/installation promotion gates. It cannot certify source truth, current stock, safe installation or physical fitment. See the [discovery report](../research/FACTORY_DISCOVERY_PASS_2026-10-29.md) and [unresolved backlog](../research/COUNTERMEASURE_BACKLOG_2026-10-29.md).
