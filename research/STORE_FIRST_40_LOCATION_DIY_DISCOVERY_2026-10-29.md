# Felicity: 40-location supplier audit and external product discovery

Research date: **October 29, 2026**. Vehicle: **U.S. 2004 Corolla LE sedan, June 2003 Canadian assembly, ZZE130L-DEPNKA, 1ZZ-FE/A245E**. Research was conducted against a healthy original-car baseline, with the actual cone intake and photographed 215/45R18 wheel/tire combination treated separately.

**Scope achieved:** all 40 original supplier locations received an individual source/access investigation; 45 external products received structured dispositions. **This is not 40 complete branch inventory searches, a completed market census, or a purchase-ready shopping list.** The location ledger is complete at the source/access level; broad shelf inventory, most local prices, physical measurements and independent comparative tests remain incomplete.

The supplier list and previous store-first report were read before research. External retailer categories, product pages, maker documents and supplier capabilities were explored before consulting the 257-concept catalog for deduplication. Some familiar products reappeared independently; those were recorded as corroboration or negative findings, not new concepts.

## Results and counting rules

| Measure | Result | Meaning |
|---|---:|---|
| Original locations individually examined | 40/40 | Individual pages/searches, including failures and conflicting listings |
| Public consumer-facing access supported by website | 28 | Website evidence, not a phone or physical visit |
| Trade-only locations | 2 | United Auto Supply explicitly restricts sales to the trade |
| Reported closed, with conflicting directory | 1 | Advance Watervliet LOC-009; closure reporting + official 404 |
| Operation or branch DIY access unresolved | 9 | Not silently counted as consumer stores or closed businesses |
| External products investigated | 45 | Includes 3 enabling tools, repair-only products and negative controls |
| Class A / B / C / D / E | 11 / 9 / 0 / 9 / 16 | A/B are conditional engineering/function leads, not proven installations |
| Existing concept records updated | 42 | Additional sources, product facts, comparisons, costs or rejection evidence |
| Verified previously undocumented upgrade functions | 0 | No reason to inflate the 257-concept catalog |
| Positive confirmed local shelf-stock results | 0 | No claim of local in-stock availability |
| Explicit branch SKU stock observations | 2 | Both negative at LOC-017; separate observation ledger |
| Approximate radial address/parcel calculations | 4 | Proxies only; 36 ungeocoded; all driving distances unknown |

Class A means plausible improvement over healthy OE supported by an identifiable mechanism, with the row's evidence and gates controlling confidence. Class B adds functionality. Neither letter means verified fit, independently measured benefit, or approval to buy. Class E includes unproven tradeoffs, wrong applications, poor value and the three tools that enable work without improving the vehicle themselves. No new Toyota countermeasure was authenticated in this pass; `factory_countermeasures.json` was preserved.

## Files and evidence navigation

- `database/local_supplier_coverage_audit_2026-10-29.csv`: all LOC-001–040, original/verified address, source, customer access, category scope, linked discoveries, stock-check count and remaining questions.
- `database/external_product_discoveries_2026-10-29.csv`: DSC-40-001–045, exact product identifiers, classification, healthy-OE baseline, interfaces, June build uncertainty, DIY requirements, costs and deduplication links.
- `database/external_product_offers_2026-10-29.csv`: dated supplier offers separate from engineering concepts. National prices never become local quotes.
- `database/local_stock_observations_2026-10-29.csv`: two actual live-browser negative SKU results.
- `database/additional_supplier_discoveries_2026-10-29.csv`: supplemental online suppliers and the separately observed Colonie store context; excluded from the original 40 count.
- `research/STORE_FIRST_40_LOCATION_BACKLOG_2026-10-29.md`: unresolved work and concrete evidence needed.
- `scripts/validate_supplier_discovery.py`: coverage, source/UPG links and price/stock-scope safeguards; added to database CI.

## Location and market-access findings

The six AutoZone, six operating Advance, ten NAPA, one O'Reilly, two Harbor Freight, two Toyota parts departments and Universal Auto Parts account for the 28 website-supported consumer locations. Every branch has its own audit row and individual location source. Their shared corporate product catalogs were explored by channel; the same product list was **not** counted as a completed branch-specific search at every location.

**LOC-009, Advance 2611 2nd Ave Watervliet:** the official branch URL returned 404; dated reporting names this address as closed. Yellow Pages still posts hours. Treat as a reported closure with conflicting directory evidence, not an available pickup stop. [Closure report](https://hudsonvalleycountry.com/advance-auto-parts-closes-new-york-stores/).

**LOC-036/039, United Auto Supply:** both facilities are on official location pages. The company's [Who We Serve](https://unitedautosupply.com/who-we-serve/) page explicitly says it sells exclusively to the trade. Its [product-lines directory](https://unitedautosupply.com/product-lines/) was explored across brakes, HVAC, suspension, drivetrain, electrical and tools; the trade portal was not accessed. Transfer schedules do not establish customer inventory. Do not infer retail access from the heading “Over-The-Counter Sales,” whose text describes supplying retail businesses.

**LOC-020/021, Fisher:** individual 13 Cannon St and 69 Terminal St recruiting pages support business-address evidence. The [corporate products page](https://www.fisherautoparts.com/products.aspx) explicitly welcomes DIY customers, but this does not prove either branch's walk-in policy or SKU availability. The Green Island job's October 6 expiration is not business closure. The initial guessed `/locations/` path failed; the actual [retail locator](https://www.fisherautoparts.com/fisher-store-locator.aspx) was subsequently accessed.

**LOC-018/019:** Read/Carquest has a dedicated directory entry, not authenticated current branch inventory. Its phone matches a historic Advance listing, a possible business-lineage issue needing resolution. Riverside's linked Auto Value branch page redirected to the national locator. Preserve both unresolved records. No Auto Value or Carquest shelf stock was invented.

**LOC-022, Universal:** [official speed-shop page](https://www.albanyuniversalautoparts.com/speed-shop.php) advertises AeroFlow fittings, adapters, unions, hose, gauges, tools, Holley, Accel, Aeromotive and MagnaFlow. The public catalog returned template placeholders/“No Results,” so exact shop SKUs and prices are unknown. Its machine/driveline service is distinctive, but a longitudinal high-performance driveshaft is not an applicable Corolla FWD upgrade. MagnaFlow's actual Corolla product was investigated separately; line affiliation does not prove local supply.

**LOC-023/026/027/034/035:** Anca's, MoonLawn, Sunshine, Autopart International and Ackner retain individual unresolved dispositions. Third-party pages do not establish current DIY parts sales. Autopart's official link returned 502. Ackner's BBB page initially loaded, then an address-find request returned 404. No donor VIN, live Corolla inventory, price, wheel condition or later-Toyota retrofit mounting drawing was obtained from the salvage sources.

**LOC-024/025:** both genuine Toyota channels were individually examined. Northway explicitly permits owners to buy parts for DIY installation and offers a tire-center channel; Lia's generic category price comparison is not a 2004 Corolla part quote. June 2003 supersessions and factory convenience retrofits require actual early-build EPC returns and dealer quotations, not a modern accessories page. No order request was sent.

**Geography:** central Rensselaer was defined for provisional calculations as City Hall, 62 Washington Street, using [OSM-derived coordinates](https://mapcarta.com/W85989700) 42.63869, -73.74506. Haversine calculations to third-party same-address/parcel proxies yielded LOC-001 **2.7 mi**, LOC-016 **15.2 mi**, LOC-027 **21.3 mi**, LOC-036 **17.0 mi** straight-line. These are not verified branch entrances or driving distances; the directory coordinates for three were available only in search excerpts after direct-open timeouts. No strict radius certification or outside-radius conclusion is made for the other 36. Coordinates/provenance are in the audit. Supplemental online suppliers are explicitly outside the verified-local-branch count.

## Best affordable DIY candidates

All amounts are dated displayed prices before tax/shipping. These are research candidates; check the selected branch and actual car first. Complete costs below assume the named existing supplies/tools, not undisclosed free new materials.

| Budget / complexity | Candidate | Defensible DIY cost statement | What it changes; remaining gate |
|---|---|---|---|
| Under $25 / basic, no lift | **Scosche SCPDC30-RP1**, DSC-40-001 | **$9.99** for the plug-in job if a suitable USB-C cable is already owned; otherwise cable extra | Useful USB-C PD charging absent from OE. Check socket, cable, total load and hot-cabin rating. No measured alternator-efficiency/MPG gain. |
| Under $25 / basic, no lift | **K-Source C0550 pair**, DSC-40-002 | **$11.99** with supplied adhesive and already-owned cleaning supplies | Adds wide-angle view; dry-fit without sacrificing too much main mirror area. Distance distortion and winter adhesive durability remain. |
| Under $50 material / basic, no lift expected | **Sylvania 9006XV-2 pair**, DSC-40-014 | **$43.99** pair; no new harness if correct lamp/bulb interface; early-car fit/aim still to verify | Maker claims downroad gain versus Sylvania Basic. That is not a measured comparison to exact healthy Toyota OE. Same wattage, no electrical-efficiency claim. |
| Price pending / basic filter access | **Bosch 6026C**, DSC-40-003 | NAPA local price and full delivered cost unknown | Promising particle-media distinction from ordinary filter and carbon odor-control variants. Measure tray seal and compare airflow/defog against clean OE. **6055C is the later-generation false positive.** |
| $50–100 material / intermediate, no lift | **Dorman 628-040**, DSC-40-005 | AutoZone **$63.50** national display; O'Reilly **$63.99** under Colonie store context. Full job unknown until circuit/switch/supporting hardware are checked | Actual new heated-seat capability. Includes pads, harness, switch and upholstery supplies, but needs upholstery removal, safe SRS/seat procedure and run-only fused power. Not a plug-in cushion or basic electrical job. |
| $50–100 material / intermediate trim work | **DEI 050110**, DSC-40-008 | AutoZone **$57.99** material; full area/adhesive/clips not quoted | Acoustic/thermal padding behind suitable trim. Resolve **24×54 versus 70×24-inch** package discrepancy and half-inch thickness before budgeting. |

The first two are the clearest inexpensive, reversible functionality additions from this pass. They are modest improvements, not substitutes for substantial ride/brake/NVH engineering. No precise install times were fabricated.

## Consequential engineering opportunities

| Area | Product or route | Engineering assessment and next proof |
|---|---|---|
| Ride and wheel impacts | Modest 15-inch package and modern touring tires; DSC-40-042 | A photographed 215/45R18 has nominal sidewall 96.75mm; a 195/65R15 has 126.75mm. The geometric 30mm difference is not a quantified ride improvement. Verify June placard, wheel/lug/offset/load/clearance, actual tire construction and complete mounted quote. Returning from 18s to OE size is modified-car correction; better modern tire behavior versus healthy factory tires needs comparative tests. Michelin **08771 is Defender T+H, not Defender2**; RAV4-size Defender2 tests are not Corolla results. |
| Roll control | **Whiteline BTR77**, DSC-40-024 | **$165.88** NAPA/maker national display; complete install/hardware total unknown. Maker identifies **22mm non-adjustable**, contradicting generic NAPA adjustable-bar prose. Chassis-family and explicit 2004 LE catalog evidence are stronger than a year label alone. Check torsion beam, OE bar, mounts and limit-balance tradeoffs after front-noise diagnosis. |
| Damping | **KONI 8050 1087**, DSC-40-023 | NAPA **$104.99 each** rear fixed-valve lead, not proof of current complete kit or adjustable damping. Obtain current maker dimensions, valving/stroke and matched fronts. KYB 344612/Monroe 71373 are OE-restoration benchmarks here, not demonstrated comfort upgrades. |
| Compliance | **Energy 8.3120G / 8.3121R**, DSC-40-025/026 | Front-arm versus rear-beam material changes, **$124.99 / $119.99** parts-only displays. Advanced extraction/press/support/alignment work; no new-OE comparative stiffness/NVH data. More rigid is not automatically more comfortable or durable. |
| Brake refinement | **Akebono ACT923A**, DSC-40-017 | Current front application evidence and low-dust/noise formulation; NAPA **$91.99** national display with contradictory sale/selected-store metadata. Healthy OE may already perform well. Confirm early bracket/pad countermeasure pairing; do not promise shorter wet stops. |
| Brake durability/value | PowerStop S2698 / KOE15366DK / K2316-26, DSC-40-018–020 | Coating and material choices deserve scrutiny at service time. Sound calipers/drums do not need speculative replacement. A drum kit is not a disc conversion. Drilled/slotted Z26 kit lacks a demonstrated daily-driving advantage over quality plain rotors here. |
| Broadband NVH | **DEI 050210 plus appropriate absorber**, DSC-40-007/008 | Distinguish CLD panel damping from acoustic absorption/decoupling. Locate dominant paths/resonances before adding mass. Preserve drains/vapor barriers/service access; quantify repeatable same-road/speed change. No vehicle dB claim. |
| Transmission | **Derale 13106**, DSC-40-034 | **$91.49** displayed, item unavailable on captured page, no local conclusion. Universal cooler is not a complete thermostat-equipped A245E kit. Log temperatures before design; validate winter control, hose/mounts, radiator airflow and full job cost. |
| Steering contamination | **CARDONE 20-0038F**, DSC-40-033 | Primary maker now authenticates this suffix and 3/8-inch hose family. Retail unit is **six filters per pack**, not necessarily one. Product text 190µm conflicts with maker technical flyer 200µm; unresolved, not fine-ATF filtration. Measure return line/flow; added joints bring leak/restriction risk. |
| Powertrain response | K&N 69-8600TR / MagnaFlow 15807 / PC37 BT, DSC-40-038–040 | Manufacturer K&N description says **short-ram** despite cold-air retailer title. Claimed high-rpm dyno gain does not establish low-rpm response/MPG and the car already has an unidentified cone. MagnaFlow is **$789.99** retailer versus **$830/unavailable** maker and may add unwanted sound. Electronic pedal controller cannot operate a mechanical cable throttle; verify actual hardware rather than trust E120 year ranges. No speculative tune/shift/lockup bypass endorsed. |
| Parking functionality | **Hopkins 50002**, DSC-40-011 | Camera, display and ultrasonic warning capability, **$199.99** displayed under Colonie context. LOC-017 explicitly out of stock. Hardwired early-Corolla reverse-power integration and complete mount/wiring cost remain. Dual XCAM100 at **$44.99** is camera-only, not a comparable full kit. |

### Fitment correction that changes a previous research lead

**UPG-097:** SPC's [Toyota application flyer](https://www.spcalignment.com/forms/CarMakeFlyers-2020sm.pdf) maps Corolla 1990–2016 to **81280**; its [EZ Cam sheet](https://www.spcalignment.com/spcalign/public/public/assets/pdf/catalog/1745268590.pdf) identifies that family as replacing **16mm** bolts. Eibach still lists **5.81270K, 15mm, rear** for the model family. This does not authorize either installation. The previous 15mm lead is explicitly held in conflict, and no rear torsion-beam eccentric strut-bolt retrofit is inferred. Measure the actual early front strut bolts and obtain current maker confirmation/drawings first.

## Live stock observations and access limits

The browser successfully opened O'Reilly's product pages. “Check Other Stores,” ZIP **12304**, with out-of-stock stores shown, explicitly returned **1727 State Street, Schenectady: Out of Stock** for **50002** and **628-040**. The page's selected store was **1390 Central Ave Colonie**: **$199.99 / $63.99** belong to that displayed context and are not claimed as Schenectady checkout prices. Colonie's camera ship-to-store estimate was not transferred to Schenectady. No item was ordered, reserved, added to cart or bought.

AutoZone's live Rensselaer browser page returned a DataDome automated-traffic access restriction. Indexed public product/location pages were available to research; they are not a live branch-stock substitute. See [When a website blocks the task](https://help.openai.com/articles/20001280-using-cloud-browser-in-chatgpt#when-a-website-blocks-the-task). Tavily returned 429 and Parallel Search reported its free-tier limit; the connected general search service continued successfully. No attempt was made to bypass those restrictions or send messages/call suppliers.

## Build scope, safety and verification

The attached **OM12859U** was text-inspected. Its footer explicitly says **“2004 COROLLA from Oct. ’03 Prod.”** even though its running header says L/O 0306. Its 9006/55W lamp and 12V/120W outlet references are later-production context, not proof of June 2003 circuits/interfaces. The database's original build limitations were preserved.

The undiagnosed loud front pothole banging is a diagnosis/safety gate before any suspension or brake performance testing. No upgrade here is represented as its repair. Inspect structural integrity, wheel/tire fit, steering, brake hardware and suspension using build-correct procedures. No headlight LED conversion, emissions removal, restraint bypass or speculative transmission control change is installation-ready.

All 257 UPG identifiers and existing citations/decisions were preserved; no product was marked installed, purchased or personally tested. Existing purchase-ready decisions for unrelated primary products were not applied to these new alternatives. Complete numerical costs are intentionally blank where supporting parts, tax, shipping, tools or required services were not established. The backlog is the continuation ledger, not evidence that the entire 40-store market has been exhausted.
