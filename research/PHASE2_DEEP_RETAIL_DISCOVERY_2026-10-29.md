# Phase 2 — deep retail product discovery

Continues commit `87968af` on `research/upgrade-evidence`. Research date: October 29, 2026. Vehicle: healthy US 2004 Corolla LE, June-2003 Canadian build, 1ZZ-FE/A245E. This is an additional market-discovery checkpoint, not a repeat of the completed 40-location audit and not a claim that the retail market is exhausted.

## Results and boundaries

| Measure | This continuation | Meaning |
| --- | ---: | --- |
| Additional product evaluations | 63 | DSC-P2-001–063; distinct SKUs or explicitly identified tire size/catalog variants |
| External catalog total | 108 | Original 45 preserved, plus 63; rejected and replacement-only items included |
| Labeled product subcategories | 35 | Several are related architectures; not 35 new upgrade functions |
| Distinct new candidate functions | 5 | UPG-258–262; all remain candidate fitment |
| Existing concepts materially extended | 14 | Clamps, thermal bypass, valve body, fluid, seat support, wheels, jounce, preheat, plugs, steering cooling, belt, water pump, trim isolation, steering filtration |
| Additional advertised offer records | 29 | 22 products have an item/package price; seven competing offers; evidence quality varies |
| New branch-specific shelf results | 13 | Four O'Reilly branches × three products, plus one Advance product/branch |
| Other stock/access observations | 4 | Two call-for-price pages, AutoZone browser restriction, unsuccessful Advance target-store selection |
| New basic / intermediate / advanced / professional evaluations | 14 / 40 / 7 / 2 | Complexity includes the complete intervention, not merely attaching the purchased part |
| New purchase-ready or vehicle-validated products | 0 | Dimensions, supporting cost, early-build interfaces or actual benefit remain unresolved |

Class A/B/D/E dispositions: **23 / 14 / 10 / 16**. A is a conditional engineering lead; B is a functional addition; D is a replacement/service benchmark; E is a rejected or held application/value case. There are no new authenticated Toyota countermeasures. A different size, finish, material or brand does not automatically receive a new UPG.

Prices are not all equally strong. The product-details table retains 20 explicitly indexed-only records and other mixed/limited retrieval stages; they must not be presented as 63 fully verified applications. Full-page primary documents were obtained for important architectures including TransGo EPC/non-EPC separation, Derale thermostat installation, Gates clamp construction, ATE/Pentosin fluid properties, Enkei wheel specifications and legacy window/wiper controllers. Other pages provided retail specifications, source leads or access limitations. No independent controlled before/after result on a healthy June-2003 Corolla was authenticated.

## What to read

- [Budget and DIY catalog](PHASE2_BUDGET_DIY_CATALOG_2026-10-29.md): prices grouped by item budget, package units, practical installation gates and every unpriced product.
- [Mechanical, performance, efficiency, comfort and refinement comparisons](PHASE2_ENGINEERING_COMPARISONS_2026-10-29.md): actual competing architectures, dimensional evidence and tradeoffs.
- [Supplier-category coverage and untouched work](PHASE2_SUPPLIER_CATEGORY_COVERAGE_2026-10-29.md): what was explored in each channel, including the nine unresolved suppliers.
- [External discovery catalog](../database/external_product_discoveries_2026-10-29.csv), [offer ledger](../database/external_product_offers_2026-10-29.csv), [Phase 2 evidence details](../database/phase2_product_details_2026-10-29.csv), [source joins](../database/phase2_evidence_links_2026-10-29.csv), [local stock](../database/phase2_local_stock_2026-10-29.csv).
- [Schema and validation limits](../docs/PHASE2_DISCOVERY_SCHEMA.md).

## Independent discovery and reconciliation

The first category searches covered thermal line protection, fluid filtration, seat internals, trim interfaces, supplier-specific lines and alternative mechanical architectures without using upgrade IDs as search terms. Repository concept names were then read for function-level reconciliation. Subsequent exact-part searches tested candidates and competing products. Discoveries duplicated by the original 45, such as Dorman 628-040, DEI speaker baffles and the Hella horn kit, were excluded from the new SKU count.

The original DSC-40 records, 40-location audit, observation IDs and source relationships were retained. The new ledger can record observed branches outside those 40 using public branch addresses and blank supplier IDs; it does not silently add them to the completed audit or assert a new radius/access verification.

## New functions: exact scope of the claim

| New UPG | Discovery | Added function | Healthy-car and DIY qualification |
| --- | --- | --- | --- |
| UPG-258 | Russell 639570 / Speed Bleeder SB7100 and SS | Integral check valve makes subsequent pedal bleeding a one-person task | Serviceability, not stronger brakes; screw cone, engagement and each installed wheel cylinder/caliper must match; intermediate |
| UPG-259 | Hydreon RT-50 | Actual rain sensing controls wipe timing | Distinct from an adjustable-delay stalk; legacy supply and early wiring unresolved; advanced |
| UPG-260 | Directed 530T | One-touch up/down and optional controlled remote window operation | Distinct from remote start/alarm; current product supply and obstruction protection unresolved; advanced |
| UPG-261 | DEI 010457, 010403 / AeroFlow AF91-5000 | Targeted thermal protection around an existing exposed line/harness | Distinct from exhaust wrap, intake panels and rodent tape; useful only where actual exposure warrants it; split sleeve can be basic |
| UPG-262 | Dorman 47237 / OEM nozzle comparison | Adjustable broader washer-fluid distribution | Measure original coverage first; wider spray is not automatically better at road speed; check-valves are supporting conditional leads, not another function |

Pneumatic lumbar support materially develops existing UPG-138. Thermoplastic clamps develop UPG-023. UHMW slip tape develops UPG-129. Neither was assigned a redundant new UPG. A valve-body wear repair is not labeled a new healthy-transmission performance function.

## Local sourcing evidence

O'Reilly's selected store was **1390 Central Ave, Colonie**. The nearby-store modal provided individual results for 1390 and 1929 Central Ave, 1727 State Street Schenectady and 1502 Curry Rd Rotterdam. These four-store results were recorded for:

| Product | Selected item display | Individual shelf result | Separate fulfillment information |
| --- | ---: | --- | --- |
| Gates 32922 | $5.99 each | All four out of stock | Selected Colonie product page offers call-to-order, estimated 24–48 hours; no order placed |
| Permatex 24112 | $30.99, 8 oz | All four out of stock | Selected Colonie page offers transfer pickup at 8 AM October 30; no reservation |
| Dorman 47237 | $19.99, two-nozzle card | All four in stock, approximately one-hour readiness | No actual quantities or reserved stock |

The display price belongs to the selected store context; no other branch checkout price was established. Russell 639570 and DEI 10457 rendered a call-for-price request without a stock result. That is neither shelf availability nor unavailability.

Advance's exact Carquest 20-0012FCQN page displayed **$53.99** under **517 Delaware Ave Ste 7, Albany**, with pickup unavailable and factory-direct shipping as a separate route. Selecting the closer East Greenbush store 6373 did not change the persisted selected store. East Greenbush stock and price therefore remain unknown. AutoZone's Kats 24150 page returned a DataDome automated-activity restriction before target-store selection; its $54.99 search excerpt remains an indexed national price, not Rensselaer stock.

These are dated observations, not promises of later availability. No purchase, store call, reservation or supplier message was made.

## Strong practical findings

The most defensible inexpensive functional opportunity to measure next is **washer coverage**: a $19.99 adjustable nozzle pair actually appeared on nearby shelves, and the OEM and Camry-donor comparators have exact part numbers. Hood-hole and hose compatibility remain open; “universal” does not authorize drilling or prove a useful spray pattern.

**Integral-check bleeders** offer a clear new service function, with a $12 steel pair versus $15 per stainless screw and an $18.99 Russell pair lead. A low item price does not include fluid, safe lifting or the risk of a seized original bleeder. The value is easier future bleeding, not improved braking from replacing healthy screws.

**Split heat sleeve**, **cold A/C-line insulation** and **UHMW slip tape** offer targeted mechanisms with modest material requirements. Each needs an actual measured exposure or rubbing interface. They should not become indiscriminate engine wrapping, hidden moisture traps or a generic soundproofing shopping list.

Mechanical comparisons also prevented waste: the older TransGo performance kit excludes the target transmission, all-years Corolla spark-plug results included incompatible newer geometry, generic “lightweight RPF1” claims used the wrong bolt pattern, and a temperature bypass costs nearly $95 before a cooler installation is complete.

## Remaining gates

The next work should fill the concrete channel/category gaps in the coverage report, obtain exact dimensional/pressure/force-travel data, and seek relevant independent installed outcomes. No same-car damper force curves, higher-efficiency water-pump test, belt-loss test, blanket additive benefit or verified local donor inventory was found. These are open questions, not conclusions that no such improvement exists.

The supplied OM12859U was inspected for baseline constraints: printed p.254 specifies Toyota T-IV for the automatic transmission, DOT3 brake fluid and Dexron II/III steering fluid; p.255 includes the original 15-inch tire/wheel reference. Its footer explicitly says October-2003 production onward. It supports general comparisons while retaining the early-build limitation; it is not an EPC or wiring diagram.
