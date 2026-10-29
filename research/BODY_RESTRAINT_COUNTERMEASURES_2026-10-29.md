# Felicity: body protection, restraint countermeasures and evidence corrections

Research date: October 29, 2026. Parent checkpoint: `32e3b66a610ea4d9f314ea8da0687e2efbcead96`. This pass used other search and direct document retrieval, with no Tavily calls.

## What changed

Two recall studies were added with matched catalog, research and decision records. Eight published concepts received evidence/procedure updates. The branch advanced during this pass; overlapping body studies reuse its published IDs, preserving the newer outcome ledger and validators. A research candidate is not a verified fit, a shopping recommendation or a measured improvement on Felicity. No component was installed or tested, and no private VIN was collected or published.

| ID | Intervention | Finding and limit |
|---|---|---|
| UPG-209 / FCM-019 | Sill paint-isolation tape | Toyota Canada kit 04006-05102; US panel equivalence and current supply remain open. |
| UPG-201 / FCM-009 | Rear handle rust field fix | Corolla kit 04006-22102, two per vehicle. Camry/Matrix kit is different; VIN/components illustrations remain unread. |
| UPG-207 / FCM-016 | Condenser stone mesh | Toyota kit 53112-12190 includes ties, but bulletin covers2005–2006. Early2004 installation/airflow remain unverified. |
| UPG-210 / FCM-020 | SRS ECU plus electrical-noise filter | Separate control-module recall remedy; a historical filter-only repair is insufficient proof of completion. |
| UPG-211 / FCM-021 | Latest specified passenger inflator/assembly | Separate rupture-risk remedy; earlier recall replacement can itself be obsolete. Toyota must resolve installed-part/campaign history. |

## Body protection: documented interventions with controlled application

TSB 2423R identifies paint damage from contamination under sill scuff plates. Its tape parts and production tables were read directly; film is applied to prepared, repaired and cured surfaces, not used to conceal rust. This is a shaped isolation kit, not evidence that a decorative sill accessory or arbitrary film is equivalent. The TMMC production context is useful, but Canadian-market issuance does not prove US coverage.

Bulletin 2543 addresses salted-road rust staining under rear handles. The Corolla-specific kit differs from the color-coded Camry/Matrix kits. Its component and VIN images remain a gap; no coating, alloy or complete-handle redesign is invented from the kit name. No authenticated current US stock or full-job price was obtained for either kit.

AC002-06 specifies added plastic mesh for later Corollas. A later bumper's drilling/attachment pattern cannot be transferred to this car without measurements. Open area, stand-off, attachment security, debris loading and cooling behavior are next engineering checks; dense insect screening is not assumed equivalent. This is a documented donor concept, not a 2004 factory-approved retrofit.

## Seat frame: missing tables recovered, early-build fit still blocked

All three NV012-06 images are now visually read. The parts table begins **May 2004**, later than June 2003, although the narrative says2004–2006. Current part entries say **Same**, rather than identifying changed part numbers. Examples71120-02010 LH and71110-02011 RH are later no-side-airbag frame references, not approved early-build donor parts. TMMC production threshold is shown in the source; this does not resolve the lower date limit. UPG-200 remains gradeD/candidate. The earlier partial-table status in the recovery report is superseded by this finding.

## Restraints: two different failure mechanisms and remedies

The15V043 defect report identifies the SRS controller supplier as **TRW**. It covers a TMMC production period containing June 2003, subject to individual eligibility. The changed remedy pairs a noise filter with a new ECU because an earlier filter-only repair could leave an already damaged controller. It does **not** prove a redesigned ASIC or make a no-warning-light car immune. Historical Corolla ECU variants depend on side-airbag equipment; Matrix variants are not substitutes. Current Toyota campaign instructions control dealer repair.

The inflator campaign addresses propellant degradation and rupture, a separate problem. Toyota announced improved non-Takata replacement parts in 2018. The2022 combined instructions also identify earlier non-desiccated and specified desiccated Takata parts no longer to install. A receipt saying only “airbag recall done” is therefore insufficient to establish the latest remedy or controller repair. These records direct the owner to Toyota campaign/part history; they are not DIY SRS projects or used-module shopping leads. Eligible open recall remedies are described as free, conditional on actual coverage.

Toyota's January 25,2024 amendment states a **DO NOT DRIVE** advisory for certain2003–2004 Corolla/Matrix vehicles with **both 15V285 and15V043 unremedied**. This research has not established that Felicity meets that condition. Verify privately with Toyota; the current NHTSA lookup explains that completed campaigns and some recalls older than 15years are omitted from its VIN results. Avoid treating a blank old-recall result as a complete repair history.

## Repairs and exclusions kept separate from new upgrades

- BO022-03 roof molding lists75555-02030 RH and75556-02030 LH as **Same**. This is useful repair guidance for warped molding, but no improved polymer or changed-number revision is demonstrated. A dealer's75555-12120 supersession is explicitly Japan-built/without-sunroof and is not a TMMC substitution. Published UPG-203 remains classified as restoration; no extra upgrade ID was created.
- BO017-03 clip inspection supports existing UPG-129/131 acoustic trials: damaged/worn clips are replaced; sound clips can be reused. The specified Camry/Solara clip is not assigned to Corolla. Clip inspection itself is not counted as an upgrade.
- EG028-04 links the P0420 calibration/catalyst repair to the same EG016-04 intervention already researched. Its parts table shows repair front pipe 17410-0D360. This does not validate the existing aftermarket converter candidate or justify flash-only/performance claims; UPG-048 gained the cross-reference rather than a duplicate new concept.
- EG053-06's pump manufacturing fix covers2005–2006, and EL001-03's DRL relay correction covers2003. Neither is documented for this2004 configuration. Both are logged as exclusions rather than implied fits.

## Source locators and remaining work

All references and retrieval limits are in `database/sources.csv`. Original documents are linked rather than copied into the repository. Locators inspected in this pass:

| Source | Locator |
|---|---|
| NV012-06 | images 1536639945,1536641304,1536645371: production,warranty,parts |
| TSB 2423R | images 1467701009 and1467783271: production and kit |
| Bulletin 2543 | image 1116697179: Corolla versus Camry/Matrix parts |
| AC002-06 | image 946469309: mesh kit; narrative procedure read |
| BO022-03 | images 1087629843 and1087631163: production and unchanged parts |
| EG028-04 | image 459161727: linked repair parts; calibration/production figures unread |
| 15V043 defect report | PDF pages 2-4: affected production, mechanism and remedy |
| DSB dealer notice | PDF pages 1-4: history, equipment-specific parts,eligibility |
| Inflator combined instructions,2022 | PDF pages 1-8: eligibility,parts and withdrawn-part controls |
| 2024 advisory amendment | Full one-page Toyota document |
| BO017-03 | Full one-page Toyota PDF |

Remaining work: readable handle kit/VIN illustrations, US equivalence of Canadian protection kits, present parts availability and installed-condition checks, early-bumper mesh engineering, current campaign completion, and matching independent long-term outcomes. No gradeB promotion is made from generic complaints, another Toyota model or manufacturer-only evidence.

## Validation

All 31 existing unit tests passed. Full CSV upgrade-coverage validation passed. Supplemental checks verified unique factory IDs, valid candidate/source references and no installation or purchase-ready claims across all 21 factory records. The catalog has 211 stable concept IDs, including unresolved studies; this is not a count of approved upgrades.
