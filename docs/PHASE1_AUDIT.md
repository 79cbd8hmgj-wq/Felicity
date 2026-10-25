# Felicity Phase 1 Audit — 2026-10-25

Status: in progress; this is an initial source and schema audit.

## Confirmed discrepancies

1. Toyota manual OM12859U explicitly covers October 2003 and later production, whereas our Corolla is June 2003. Keep its technical values as reference until independently confirmed for the earlier build.
2. The 28 component records are a flat inventory, not a hierarchical component model. Existing database documentation should not imply otherwise.
3. The service tasks currently link to free-text system names, not validated component identifiers.
4. The single vehicle row combines factory-label details and owner-reported mileage with only one source pointer. Individual claims need provenance.
5. No validated OEM parts or completed repairs exist yet. Empty tables accurately reflect unknown history.
6. The photographed tire size is from one wheel only; other positions and tire condition remain unverified.

## Planned remediation

- Verify a production-appropriate Toyota owner, repair and electrical manual.
- Introduce and test an actual relational schema with source references and component-parent relationships.
- Track original equipment separately from installed modifications and proposed changes.
- Require source-level evidence before marking part interchange as confirmed.
- Keep full vehicle identifiers and original certification photo out of public GitHub.

Source: https://assets.sia.toyota.com/publications/en/om-s/OM12859U/pdf/OM12859U.pdf

Phase 1 is not complete until the source applicability and structural validation issues have been addressed.
