# Phase 2 retail research validation

Starting commit: `87968af63ba21ecaab8d5a1ba5cb950bb3dc4acf`, branch `research/upgrade-evidence`.

## Checkpoint 1

`36a1928` (hosted; local equivalent `b50df37`) — 63 added external product evaluations, scoped evidence/stock/detail tables, five new candidate functions, initial existing-concept comparisons and the Phase 2 integrity checks. Local execution: 39 tests passed; all four validators passed. CSV line endings were normalized back to repository LF before committing; the original 45 product rows were preserved.

## Report and sourcing follow-up

Added the complete budget/DIY, engineering-comparison and supplier-category reports; 50 channel/category coverage rows; exact price units; one live Advance filter quote/pickup result; one explicitly unsuccessful East Greenbush selection; and material steering-filter comparison evidence for UPG-231. The selected Advance store remained 517 Delaware Ave, Albany; no East Greenbush stock was inferred.

Executed against the completed integration on October 29, 2026:

| Check | Result |
| --- | --- |
| `python -m unittest discover -s tests -v` | 39 passed |
| `python scripts/validate_database.py --require-upgrade-coverage` | Passed; 262 concepts/reviews linked |
| `python scripts/validate_countermeasures.py` | Passed; original 28 studies retained |
| `python scripts/validate_supplier_discovery.py` | Passed; original 40 locations retained |
| `python scripts/validate_phase2_discovery.py` | Passed; new product/detail/source/coverage/stock joins and price scope |
| `git diff --check` | Passed |
| Original DSC-40-001–045 | Field-for-field equal to starting commit |
| Original supplier candidate/audit/stock files | Byte-for-byte equal to starting commit |
| `factory_countermeasures.json` | Byte-for-byte equal to starting commit |

New regression tests reject an indexed listing being relabeled as shelf stock, a selected-store display being promoted to another branch checkout, a dangling source relationship and missing detail coverage.

These checks establish data integrity. They do not establish safe installation, exact early-build fit, current availability after the observation, independent healthy-car benefit or purchase readiness. Hosted Actions execution is a separate check recorded after pushing; local tests must not be described as hosted CI.
