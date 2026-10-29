# Simple-upgrade investigation, pass 3: confirmed carbon alternatives and baseline correction

**Researched:** 2026-10-25. **Target:** 2004 US Corolla LE, 1ZZ-FE/A245E, June 2003 Canadian/NAP production, model ZZE130L-DEPNKA. **Decision rule:** assess benefits against *healthy OEM*, not worn/defective components. No speculative horsepower claims.

## A. Cabin filter: previous "could not find a carbon part" finding is now resolved

**Healthy OE baseline:** Toyota cabin element **88568-02020**, cataloged for this 2004 Corolla's specific model code ZZE130L-DEPNKA. Public Toyota OEM-parts listing ~$20.22, observed 2026-10-25. https://www.toyotapartsdeal.com/oem-2004-toyota-corolla-cabin_air_filter.html

**Definite aftermarket carbon alternatives by model-year/product cross-reference:**

| Filter | Evidence | Observed single-unit listing | Important distinction |
|---|---|---:|---|
| **FRAM Fresh Breeze CF10133** | Activated carbon, **7.835 x 8.622 x 0.748in**, behind glovebox; lists Corolla **2002-08**, cross-references Toyota 88568-02020. https://www.finditparts.com/products/2037023/fram-cf10133 ; https://www1.rockauto.com/en/moreinfo.php?cc=0&pk=1053334&pt=6832 | **$4.72 closeout at RockAuto**, before shipping and tax, 30-day closeout warranty | FRAM Fresh Breeze uses carbon + baking soda for *odor adsorption* (manufacturer claim). Healthy-stock Corolla gas capture or particulate-filter efficiency comparative results **not** established |
| **MAHLE LAK157** | Manufacturer product family coded **LAK** = activated-carbon cabin filter. Retail cross-reference lists Toyota 88568-02020. https://www.finditparts.com/products/15960581/mahle-lak157 ; 2004 Corolla filtered retail listing https://www.partsgeek.com/catalog/2004/toyota/corolla/air_intake/cabin_air_filter.html | **$17.49** on FindItParts, observed 2026-10-25 | More expensive than observed FRAM closeout; independent gas adsorption/microparticle comparison unavailable |
| **TYC 800006P particulate comparator** | Manufacturer directly lists 2003–08 Corolla LE, particulate media, 7.83 x 8.66 x 0.79in, Toyota 88568-02020 interchange. https://www.tycamericas.com/tyc-cabin-air-filter/5637152960.p | Not freshly quoted | Non-carbon healthy generic replacement benchmark, **not** an activated-carbon option |

**Caveat:** Toyota dealership template descriptions of 88568-02020 mention *Premium Charcoal Cabin Air Filters* but do **not** prove the actual 88568-02020 element contains charcoal. Check exact original media identity before claiming carbon is superior to healthy Toyota factory part. Carbon gas adsorption reduces some odor-related exposures; charcoal does not automatically filter particles better, and additional media may increase blower pressure drop. No quantified healthy-OE advantage has been proven for either candidate.

**Installation:** Glovebox/filter-cover access, approximately 5–15 minutes with basic tools; check air-flow arrow and seal. No wiring or undercar work. The manufacturer TYC specifies glovebox fit and under-five-minute nominal installation for its reference.

**Verdict:** **FRAM CF10133 is now an actual suitable carbon product to consider**, subject to comparing against the correct healthy OE media. The previous 'no Corolla carbon SKU identified' gap is closed.

## B. Spark plugs: production-period-correct NAP baseline

Toyota 2004 workshop 1ZZ-FE references **Denso SK16R11 or NGK IFR5A11**, nominal **1.1mm** gap and 120k-mile service interval: https://charm.li/Toyota/2004/Corolla%20L4-1.8L%20%281ZZ-FE%29/Repair%20and%20Diagnosis/Powertrain%20Management/Tune-up%20and%20Engine%20Performance%20Checks/Spark%20Plug/Testing%20and%20Inspection/

An aftermarket NAP EPC mirror listing for model **ZZE130L-DEPNKA** identifies **Toyota 90919-01217 (SK16R11) as an original equipment part for 2002-01 to 2004-05 production**; an example result had a *different donor vehicle VIN in the URL* and was deliberately not embedded in public repository research. Independent reseller catalog https://www.toyotapartsnow.com/oem/toyota~plug-spark~90919-01217 supports SK16R11 fitment and later replacement number **90080-91184**.

**Do not import the 90919-01240 'from 04/2003' date from a Japanese-production listing** into this Canadian-assembled June 2003 NAP Corolla. Production codes matter; seller interchange is a different level of evidence from dated factory EPC.

**Healthy-OE advantage:** No quantitative power, mileage, ignition durability or load gain established for platinum, ruthenium or Iridium TT replacements versus healthy correct SK16R11/IFR5A11. **No performance purchase recommended.**

**Install:** Simple/moderate coil removal, dirt control, proper plug socket and **25 Nm (19 ft-lb) factory service-spec** on threads/seat in correct condition; verify manufacturer procedure before doing this work: https://charm.li/Toyota/2004/Corolla%20L4-1.8L%20%281ZZ-FE%29/Repair%20and%20Diagnosis/Powertrain%20Management/Tune-up%20and%20Engine%20Performance%20Checks/Spark%20Plug/Specifications/

## C. Lighting: a marketing claim vs an independent *reference* test

- **US Philips X-tremeVision 9006XVB2**: official US site lists **12V, 55W**, 9006, and 'up to 100% more vision' **versus minimum legal low-beam test threshold**, NOT versus healthy original Corolla headlamps. https://www.usa.philips.com/c-p/9006XVB2
- **Sylvania XtraVision**: third-party BulbFacts test dated 2017, updated 2026, reports **379 vs 373 lux** reflector low beam (+1.6%), **981 vs 876 lux** reflector high beam (+12%) against an **OSRAM Original reference test**, and output 1637 vs 1564 lumens (+4.7%), at 55W. https://bulbfacts.com/halogen-bulbs/reviews/sylvania-xtravision-vs-oem.html . **Critical limitation:** their page shows an H7 tested example and a *family* including 9006; do not transfer those numeric gains to the particular North American 9006 bulb or Corolla reflector without confirmed shared test geometry.
- In either case, 55W standard halogen **does not cut electrical demand**, and short/long bulb life is a relevant cost tradeoff. A compliant complete lamp or direct-application halogen with proven road illumination can provide meaningful benefit; legal LED retrofit bulb identity cannot be inferred merely from 'fits 9006'.
- 2004 OM12859U bulb specification is for Oct-2003-onward cars, so early June-2003 physical bulb/housing confirmation remains prudent.

**Verdict:** Sylvania XtraVision is a **research lead** with *some* independent benchmark context, but **not yet a quantified 2004 Corolla 9006 gain**. Philips copy is no evidence of +100% over healthy stock.

## D. Filters and sensors: do not confuse technical specification with outcome

- **FRAM XG4967 engine oil filter** matches year/engine listing and has maker efficiency/anti-drainback documentation, but **no controlled engine-wear improvement over a healthy Toyota oil filter**. Good potential replacement, not a proven reliability upgrade.
- **Engine filter** in subject vehicle is **not the factory airbox**: an open aftermarket cone is owner-photographed. Stock rectangular engine filter numbers can't be ordered as a drop-in to that intake. Manufacturer/filter dimensions and media ratings needed before comparing to current setup and healthy OEM.
- **OBD-II scanner/dashboard** offers a clear functional gain: read original factory ECU-supported RPM, engine coolant temperature, intake temperature, fuel trims and other supported PIDs without replacing a healthy sensor. This is *information/diagnostics*, not horsepower. Exact adapter/application and enhanced A245E PIDs are unverified; generic OBD-II cannot be assumed to expose ATF temperature.

## Outcome vs previous pass

- **Resolved:** 2004 Corolla exact-fit activated carbon product exists (FRAM CF10133; MAHLE LAK157 alternative).
- **Strengthened:** source-sensitive early NAP SK16R11 part baseline and explicit JPP-vs-NAP error prevention.
- **Still open:** healthy stock charcoal media identity, actual controlled healthy-OE odour/particle capture, 9006-specific beam/lifetime data, premium oil-filter healthy Toyota comparison, measured exotic-plug advantage (none found).

No change made to original 148 CSV research verdicts solely based on supplier cross-references. This report supplements—not silently promotes—the structured screening records.
