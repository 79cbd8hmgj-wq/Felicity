# Phase 2 external product discovery

Continues `87968af` on `research/upgrade-evidence`. The original 40-location audit and DSC-40 identifiers remain intact. Phase 2 adds DSC-P2 identifiers to the existing external discovery/offer tables. A new SKU evaluation is not necessarily a new function, a confirmed fit, or a recommendation.

- `phase2_product_details_2026-10-29.csv` links one detail row per DSC-P2 record. It separates full page/specification review from an indexed-only lead, identifies price package units, and keeps total job costs explicitly unquoted.
- `phase2_evidence_links_2026-10-29.csv` joins products to `sources.csv`, with evidence roles and scopes. A corporate brand/category listing is a sourcing lead, not exact branch inventory.
- `phase2_local_stock_2026-10-29.csv` records individual branch results separately from selected-store item prices. A blank supplier ID permits an observed nearby branch outside the original 40 audited records without changing that audit. Such rows identify the branch by its observed public address and make no new distance/access audit claim.
- The existing external offers table includes both page-observed and explicitly indexed-only prices. Compare package units and evidence stage before considering totals. An indexed price is not a verified checkout quote.

Run the original three validators and `python scripts/validate_phase2_discovery.py`, plus `python -m unittest discover -s tests -v`. The new checks protect joins, item-price scope and branch-stock provenance. Tests exercise failures where an indexed listing becomes shelf stock or a selected-store price becomes another branch's quote. These are data integrity checks; none proves engineering benefit, individual-car fit, current stock after observation, or safe installation.

The supplier coverage and buying reports define remaining research. Pending prices, dimensions, independent outcomes and June-2003 electrical/physical fit are retained as open gates rather than guessed.
