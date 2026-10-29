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

## Next discovery work

Continue body corrosion/water management, seat/trim improvements, EVAP and transmission remedies, supplier-engineered material alternatives, then owner outcomes and economics. Preserve unsupported market/production leads separately. Do not merge this branch to main.
