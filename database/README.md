# Felicity structured database v1

Machine-readable CSV tables with stable identifiers, provenance, applicability and verification states. Readable in spreadsheet software, Python, SQLite, DuckDB, or a web app. **No unredacted VIN or ownership documents.**

Tables:
- `vehicle.csv`: one vehicle/build record, confirmed vs reference attributes.
- `components.csv`: hierarchical component inventory and research queue; item presence may be standard/reference, not inspection verified.
- `specifications.csv`: measurable original-factory specification records and source references.
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

Source manual OM12859U is labeled **2004 Corolla from October 2003 production**. This car's label says **June 2003**; owner's manual specifications may broadly align, but **production-range conflicts must be checked** against a period-correct manual/EPC before assigning a part.
