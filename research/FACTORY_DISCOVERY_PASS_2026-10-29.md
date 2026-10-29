# Factory countermeasure discovery - 2026-10-29

Target: US 2004 Corolla LE, Canada/June 2003, 1ZZ-FE, automatic (A245E not yet physically confirmed). Baseline branch head: `296f45410715ce62d540815935d5f0165c6586dc`.

## Milestone 1: overlooked factory hardware and procedure corrections

The starting catalog had 193 concepts. Review of the candidate inventory, source registry, existing research outlines and subsystem reports found detailed engine/accessory, thermal and suspension gates, but relatively little factory brake-hardware, seat/glazing locating-hardware, campaign build-split or diagnostic-calibration coverage. Prior tensioner, gasket, window-run, relay, cooler-line, rear-hub and heater findings are not new discoveries in this pass.

Five distinct concepts are added (UPG-194-198), plus new TCMC-pad evidence linked to existing UPG-107. Detailed structured records are in [factory_countermeasures.json](../database/factory_countermeasures.json); URLs, retrieval limitations and source locators are in [sources.csv](../database/sources.csv).

| Record | Engineering change | Scope and purchase gate |
|---|---|---|
| FCM-001 / UPG-194 | Front caliper bracket and pad-support revision; BR004-07 was superseded by T-SB-0046-08 | US2003-08 1ZZ, pre-2008 production change. Original bracket47721-02140 to47721-02141; latest captured support kit04947-02130. Bump-related brake rattle is a diagnostic alternative, not a conclusion about Felicity's clunks. |
| FCM-002 / UPG-107 | T-SB-0150-13 improved TCMC service pad/shim system | AZ003 toAZ022; does not establish defective original factory pads or better stopping. Displayed $39.27 listing is unavailable. |
| FCM-003 / UPG-195 | EG017-07 P0133-only calibration remedy | 2004 automatic Denso/Delphi branches verified separately. Reflash, NOT ECM purchase; no power/MPG claim. |
| FCM-004 / UPG-196 | T-SB-0141-10 Rev1 top-windshield locator contact correction | Top windshield applies; 2004 Corolla bottom retainers N/A; rear-glass branch is2009 Corolla only. |
| FCM-005 / UPG-197 | SSC80A/08V162 window-bolt retention remedy | June2003 falls in early regulator procedure group; actual recall eligibility/completion must be checked privately by Toyota. |
| FCM-006 / UPG-198 | T-SB-0288-08 Rev1 seat locator squeak remedy | Corrects assembly locator contact, not structural seat mounting. Restraint precautions, current build-specific procedures and symptom localization required. |

Prices checked2026-10-29: bracket$170.26 each at Olathe Toyota; support kit$15.38 at Grieco Toyota. Two brackets plus kit=$355.90 before grease, shims/boots if required, unrelated brake repairs, tools, tax and freight. This is not a complete job quote or proof of stock. A cheap clip-only substitution is not assumed equivalent to Toyota's matched-system remedy.

## Evidence and production controls

- Level A here describes the identified Toyota model/configuration remedy. It does not mean actual hardware, current EPC supersession, fault or installation on Felicity has been verified. The four independent application statuses are recorded separately.
- No candidate has been installed or tested. No quantified fuel, power, dB or lifespan gains are claimed.
- EG022-07 was investigated and excluded: its full applicability specifies MANUAL transmission. Do not infer automatic eligibility from a search summary or even the archive's Matrix4WD folder.
- The supplied OM12859U was inspected locally. PDF page1 explicitly says October2003-onward production despite the L/O0306 header. It cannot settle this June2003 build's part, fluid or wiring details.
- T-SB-0046-08 changes the older brake bulletin's title, application and parts. Follow the later source; preserve BR004-07 as history only. The separate TCMC procedure has different lubricant restrictions. Resolve the current installed brake system in Toyota information before work.
- No authentic matching long-term owner outcomes yet support a Level B promotion. Trade articles repeating a TSB are not independent repair success.

## Milestones 2 and 3: corrosion, material alternatives and consumer outcomes

Milestone1 was preserved on the research branch in [1b7c435](https://github.com/79cbd8hmgj-wq/Felicity/commit/1b7c4352e9ab0f0158218b0b0aa46f045ebb7b2f). Its remaining gaps were installed hardware, current supersessions and matching long-term outcomes. A second saved milestone, [e853a73](https://github.com/79cbd8hmgj-wq/Felicity/commit/e853a734c838c37dacf1eadbbd77bcc79f0c6e0a), added UPG-199 filler pipe and UPG-200 seat frame, with missing seat tables and owner outcomes as open gates. This continuation preserves both IDs and all saved prices/sources, expands the filler evidence, reads the seat parts image, and adds nine further catalog concepts (UPG-201-209), two more existing-concept evidence studies, five consumer records and a separate unresolved backlog. No concurrent work was overwritten.

| Record | Newly investigated opportunity | Documentary scope / engineering distinction |
|---|---|---|
| FCM-007 /199 | Fuel filler sealing corrosion revision | USA EG051-06:77201-02080 to77201-12750. Symptom/corrosion-dependent; actual coating change undisclosed. April2003 repair manual reference supports early-build documentary relevance. |
| FCM-019 /209 | Sill protection film under scuff plates | Canada2423R: barrier against concealed paint damage; US tape/cutoff fitment pending. Potential proactive protection if compatibility established. |
| FCM-008 /200 | Seat cushion movement/frame revision | USA NV012-06 narrative includes2004, but captured parts-table rows start May2004. Preserve the earlier candidate on hold; June2003 part applicability not authenticated. |
| FCM-009 /201 | Rear outer handle rust field fix | Canada2543 explicitly includes Corolla; kit contents and US applicability unresolved. No assumed stainless spring. |
| FCM-010 /202 | Pillar garnish condensate drainage | Canada3251 covers2003-08; plastic garnish procedure, not drilling structural bodywork. US trim/SRS match pending. |
| FCM-011 /203 | Warped roof molding remedy | USA BO022-03 includes2003-04; part/cutoff tables missing. Restoration unless improved engineering is authenticated. |
| FCM-012 /204 | Improved ZZ internal lubrication / short-block design | Europe EG-6020 confirms factory piston cooling/lubrication revision. No US ZZE130 block/piston interchange; major-rebuild research only. Distinct from prior forged-piston performance concept. |
| FCM-013 /205 | Repair carpet retainer without replacing carpet | USA T-SB-0014-22,58297-50020. Documented serviceability, not a healthy-anchor upgrade. |
| FCM-014 /206 | Copper-nickel brake hard lines | BrakeQuip engineered material alternative, not a Corolla kit. Dimensions, flare and routing unverified; distinct from existing flexible-hose concept. |
| FCM-015 /existing093 | Mevotech TXK80230 serviceable front link | Manufacturer catalog confirms model-year application and sintered-bearing/seal design; added lubrication requirements and hardware-content discrepancy. No proven healthy-OEM comfort/durability gain. |
| FCM-016 /207 | Condenser mesh debris protection | USA AC002-06 is2005-06, not2004. Early bumper/airflow adaptation research only. |
| FCM-017 /208 | Modified radio/vent bezel | Canada1239/BC-03-013 identifies fit remedy; US exact part/cutoff unverified. Cosmetic/restorative benefit, no proven NVH gain. |
| FCM-018 /existing184 | Original Toyota P0741 source | TC008-04 confirms NUMMI-specific table, not Canadian fitment. Improves existing ATRA diagnostic research; not another efficiency upgrade. |

### Counts and classification

Counts describe this pass, not the evidence quality of all historical193 concepts:

- **16 new catalog candidates**, from193 to209, with **19 structured studies**:16 new concepts and3 existing concepts receiving evidence. The eight previously supplied example revisions were not counted as new.
- **17 studies have Toyota technical documents**;15 of those are new catalog candidates. Toyota documentation alone does not establish the correct market/build.
- **8 Level A**, **0 B**, **1 C**, **10 D**, **0 E** across the19 studies. The eight A records include one conditionally eligible campaign and one restoration/serviceability procedure. Among16 new concepts,7 are A and9 are D. C is new supplier evidence on existing UPG-093.
- **10 studies remain unresolved at the application/design level (D)**; nine are new concepts. **All19** still lack actual-vehicle validation and installation/testing. A/C documentary or manufacturer application is not physical verification.
- **5 independent report records linked to4 concepts** (3 new,1 existing). None authenticates a successful exact revised-part remedy with adequate follow-up for B. One reports success with different aftermarket brake parts; others are unresolved, recurring-noise or corrosion reports. These are not five verified upgrade successes.
- **2 supplier-technology studies**: directly cataloged TTX link (C) and universal copper-nickel material application lead (D). Dorman filler is recorded as a replacement alternative, not a third demonstrated modernization.
- **3 exclusion/hold records**, plus1 maintenance handling practice; none increases catalog totals. The19 studies include15 engineering-improvement investigations,2 restoration entries,1 restoration/serviceability entry and1 diagnostic reference. This is an inventory of evidence quality, not19 proven improvements.

### Most useful priorities

1. **Inspect front brake hardware as part of proper clunk diagnosis.** Toyota's matched bracket/support remedy is the strongest newly found chassis lead. Use actual brake localization, strut/mount/link/control-arm/ball-joint/steering inspection and current Toyota procedure. No diagnosis follows from two noisy front corners or a past sway-bar repair.
2. **Check window campaign status privately.** Early regulator instructions were found; actual eligibility/completion remains separate. Keep this safety countermeasure distinct from elective modernization and from the previously studied wind-noise run-channel revision.
3. **Keep the revised filler tube as a specific EVAP repair option.** It addresses a documented sealing-surface issue. Do not replace it on an otherwise healthy car solely because a newer number exists.
4. **Use locator-contact remedies only for confirmed seat/windshield noise.** They can remove a specific rattle without wholesale replacement, but require exact trim/restraint procedures and are not universal soundproofing.
5. **Advance sill film and corrosion-resistant hard lines through compatibility checks.** These are promising preventative/material directions for long-term preservation. Neither currently has complete early-build purchasing/installation evidence.
6. **Consider TTX links at necessary replacement, after identifying the present repairs.** Construction/serviceability is documented by the supplier. Independent comparative longevity and lubrication requirements remain open. It does not promise softer pothole impacts.

### Costs and DIY assessment

Observed US listings accessed2026-10-29, not guaranteed stock or complete-job quotes:

| Item | Observed parts basis | DIY scope / limit |
|---|---|---|
| Bracket/support remedy | $355.90 subtotal,2 brackets +support kit | Intermediate brake work; grease/shims/boots as needed, diagnostics, freight/tax/tools extra |
| Revised filler pipe | Conicelli$237.39 pipe only | Intermediate with fuel-vapor precautions; hoses/clamps/cap only if required; listing expressly not inventory |
| Carpet retainer | Longo$6.90 displayed | Intermediate trim/carpet work; sales unit uncertain because Toyota packaging is10 pieces; no whole-job total |
| TTX link | FinditParts$70.99 each;2 front positions | Intermediate after geometry/hardware/grease checks; delivered cost/stock unconfirmed |
| Copper-nickel tube | Distributor$55.50/25ft coil; advertised$25.99 US freight extra | Advanced hydraulic fabrication; diameter variant, flare nuts, supports, tools and required length unknown |
| TCMC revised pad set | $39.27 displayed but unavailable | Historical/reference price only; not orderable evidence |
| Other factory trim/ECM/internal-engine leads | Unknown | No fabricated range; ECM specialist, trim/SRS advanced where appropriate, engine rebuild professional |

No fuel savings, horsepower, stopping-distance, noise-level or lifespan gains were quantified. None of these new candidates was marked purchase ready. Existing unrelated purchase decisions were preserved.

### Consumer evidence and contradictory findings

[consumer_outcomes.csv](../database/consumer_outcomes.csv) preserves positive and negative reports with exact limitations. The independent2004 brake case concerns vibration and different parts; it is not proof of Toyota's rattle kit. The2004 filler discussion lacks repair confirmation and includes a rusty-but-still-sealing counterexample. A UK2004 brake-noise owner reports recurrence after renewal. UK2006 hard-line corrosion supports investigating materials, not US kit fitment or long-term Cunifer success. A later2007 EVAP excerpt remains unresolved and does not test the revised filler part.

Additional contradictions are retained: TTX manufacturer says hardware included while retailer says no; live manufacturer catalog subsequently redirects although indexed application remains available. Older brake articles quote superseded support kits. Newer TCMC instructions prohibit reusing old shims and differ in support lubrication. Those conflicts require procedure/box checks, not silent reconciliation.

### Coverage and remaining work

The pass searched factory braking, seat/glazing/trim, body corrosion, EVAP, oil-consumption internals, floor retention, cooling protection, transmission calibration, steering and electrical handling. Existing engine/accessory, suspension, cooling, HVAC, electrical and efficiency studies were checked to avoid duplicates. New authenticated drop-in starter, steering-shaft or early hydraulic-control modernization did not emerge; that is a research gap, not proof none exists.

The [separate backlog](COUNTERMEASURE_BACKLOG_2026-10-29.md) records all ten D studies, missing tables/current parts, exact-car gates and next searches. Research must continue across the whole vehicle; this pass does not claim exhaustive Toyota TIS or paid EPC access. Intermittently inaccessible archive tables were preserved as gaps instead of guessed part numbers. No research was merged to main, no VIN was published, and parts/repairs ledgers remain empty.

Local validation:31 existing unit tests passed; complete209-row CSV/catalog/research/matrix coverage passed; supplemental19-study/5-outcome links and grade/status/price gates passed. Six deliberately corrupted temporary copies were rejected (unsupported B grade, fictional installation, cross-candidate outcome, missing factory source, zero substituted for unknown cost and duplicate study). Whitespace and changed-file identifier checks passed. These checks verify data consistency and guardrails, not mechanical fitment or source truth. Hosted GitHub Actions status is reported separately from local results.
