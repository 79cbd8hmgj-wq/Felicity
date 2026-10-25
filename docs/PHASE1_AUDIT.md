# Felicity Phase 1 Audit — 2026-10-25

Status: in progress; this is an initial source and schema audit.

## Confirmed discrepancies

1. Toyota manual OM12859U explicitly covers October 2003 and later production, whereas our Corolla is June 2003. Use OM12859U as the primary 2004 owner-manual reference, retaining its printed October-production limitation for build-sensitive parts and procedures.
2. The 28 component records are a flat inventory, not a hierarchical component model. Existing database documentation should not imply otherwise.
3. The service tasks currently link to free-text system names, not validated component identifiers.
4. The single vehicle row combines factory-label details and owner-reported mileage with only one source pointer. Individual claims need provenance.
5. No validated OEM parts or completed repairs exist yet. Empty tables accurately reflect unknown history.
6. The photographed tire size is from one wheel only; other positions and tire condition remain unverified.

## Planned remediation

- Use published Toyota 2004 owner manual OM12859U as the baseline. Obtain VIN/build-correct repair, electrical and parts-catalog details when fitment is production-sensitive.
- Introduce and test an actual relational schema with source references and component-parent relationships.
- Track original equipment separately from installed modifications and proposed changes.
- Require source-level evidence before marking part interchange as confirmed.
- Keep full vehicle identifiers and original certification photo out of public GitHub.

Source: https://assets.sia.toyota.com/publications/en/om-s/OM12859U/pdf/OM12859U.pdf

Phase 1 is not complete until the source applicability and structural validation issues have been addressed.

## Phase 1 progress update

Added `scripts/validate_database.py`, six regression tests, and `.github/workflows/database-validation.yml` to validate existing CSV records automatically. This is non-destructive structural checking, not a full relational schema migration. GitHub Actions execution status must be checked before recording a passing CI result. OM12859U is accepted as the primary 2004 owner's manual, not as unqualified proof for every June 2003 build-specific part.

## 2026-10-25 integrity hardening

- All 26 existing specifications linked to component IDs and given explicit production-scope labels.
- Added validation against blank required source and component links in specifications, tasks, observations, claims, parts and repair records.
- Regression coverage expanded to 15 test methods, including missing required references.
- Existing CSV records remain unchanged in this pass; no manufactured repairs, parts or fitment assertions.
- **Validation limitation:** GitHub connector permits file updates but does not expose a general workflow-runs listing/dispatch endpoint; local runtime could not clone GitHub. Full Python test execution and GitHub Actions conclusions have therefore not been independently observed. Do not label CI green until execution is confirmed.

### Remaining gate

Run `python -m unittest discover -s tests -v` and `python scripts/validate_database.py` in a checked-out repository and confirm GitHub Actions status. Follow with published schema documentation and source-page checks; claims of June-2003 fitment remain conditional on build-sensitive OEM evidence.
