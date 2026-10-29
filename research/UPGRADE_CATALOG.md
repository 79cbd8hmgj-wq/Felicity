# Upgrade research catalog — broad discovery inventory

**Scope:** 2004 US Corolla LE / June 2003 manufacture / 1ZZ-FE / A245E automatic.  
**Status:** **251 distinct engineering research concepts**, each with linked research and decision matrix, not 225 proven improvements or directly fitting products. The first 148 were screened in the [initial research pass](UPGRADE_RESEARCH_RESULTS.md); subsequent IDs extend that inventory. See [evidence-linked review rows](../database/upgrade_research.csv) and [schema semantics](../docs/UPGRADE_RESEARCH_SCHEMA.md). No condition triage.

The linked [CSV catalog](../database/upgrade_candidates.csv) contains every identified research direction with a stable ID, subsystem, intended benefit, evidence maturity, and verification gate. It distinguishes:
- **documented_lead**: a published Toyota/TRD or manufacturer reference exists for the concept or a related model; not proof of this car's fitment.
- **research_hypothesis**: an engineering concept worth investigating; no product or measured benefit yet confirmed.
- **literature_reviewed**: initial findings or explicit evidence gaps recorded; full verification remains open.
- **candidate / probable**: current fitment classes; none confirmed or vehicle-validated. Original `candidate_unverified` describes the discovery state only.

## Discovery-first expansion beyond repeated subjects (2026-10-29)

[New technology discovery pass](NEW_TECHNOLOGY_DISCOVERY_PASS_2026-10-29.md) adds **nine distinct physically described improvement classes** with corresponding candidates, research, sources and value matrix: **UPG-217** internal cavity wax, **UPG-218** integrated heated seats, **UPG-219** ultrasonic reverse warning, **UPG-220** early Corolla OEM fog lamps, **UPG-221** dedicated winter tire/wheel set, **UPG-222** Toyota mudguards, **UPG-223** progressive hood lift struts, **UPG-224** radar blind-spot/rear cross-traffic detection and **UPG-225** remote start. Novelty was checked against all existing 216 categories. The products are of unequal practicality and maturity; manufacturer fitment is not a VIN installation approval, all are `purchase_ready=no` and none are installed. **Next research should continue pursuing other genuinely different technologies**, not keep expanding evidence for the same suspension, brake and service correction items.

## Second discovery expansion — new classes beyond existing 225 concepts (2026-10-29)

[Five additional new-technology concepts UPG-226–230](ADDITIONAL_MODERNIZATION_DISCOVERY_PASS_2_2026-10-29.md) document ambient/wiper-triggered automatic lighting, a Corolla-specific CURT Class I utility receiver, supplementary fused accessory distribution, heated exterior mirror control, and custom snow/saltwater footwell containment. These are not repeat reviews of factory fixes, tire brands or suspension options. **230 distinct concepts, 230 linked research records, 319 registered sources.** None is VIN-verified, installed or purchase-ready; absolute benefit relative to healthy factory equipment remains unmeasured.

## Third discovery wave: new mechanical, thermal, safety and security architecture (2026-10-29)

[Eight new engineering systems UPG-231–238](NEW_HARDWARE_ARCHITECTURE_DISCOVERY_PASS_3_2026-10-29.md) add hydraulic steering magnetic filtration, independent pressurized engine pre-lubrication, automatic underhood fire suppression, conditional 2004 OEM ABS+EBD architecture feasibility, passive battery radiant/acid shielding, 120V stationary cabin preheating, active intrusion-sensing vehicle security, and partially open rain-excluding ventilation. These are **new functions**, not alternate brands of existing dampers or brake pads. All remain candidate-only / unverified, and no purchase-ready or subject-car installed claims apply. **238 canonical concepts, 238 reviews, 336 sources**; review counted only after CI succeeds.

## Wave 4: new coolant-level, forward warning, active filtration functions (2026-10-29)

[Discovery wave 4: three new source-backed systems UPG-239–241](NEW_SYSTEMS_DISCOVERY_WAVE_4_2026-10-29.md) adds a **direct liquid-coolant-loss alarm** separate from ECT gauges, a **professional forward collision/lane warning camera** separate from reversing/side radar, and **powered independent cabin filtration** separate from passive HVAC filters. **241 concepts / 241 research records / 343 registered sources**. Evidence limits include unknown Corolla 35mm hose connection, professional fleet-only Mobileye access and safe cabin mounting. The report also records why generic newer motor mount supersessions, generic acoustic glass, incompatible HUDWAY Drive and replacement digital fan controllers were **not** promoted to new upgrades. All remain research-only, no installed or purchase-ready status.

## Wave 5: exposed corrosion, heated wipers, surround vision, stored-start energy and factory rear heat ducts (2026-10-29)

[Five distinct functions UPG-242–246](NEW_ENGINEERING_DISCOVERY_PASS_5_2026-10-29.md) document a flexible exterior chassis salt barrier, heated blade and pivot anti-icing, four-camera stitched overhead parking vision, a smart main battery with independent stored-start energy (high-price/cold-weather caution), and genuine Toyota NAP rear-seat heater air routing if not already factory installed. **246 concepts, 246 linked research rows, 354 sources.** All remain research-only. Maker 14V maximum for heated blades conflicts with potential normal automotive charging variation until approved; Toyota rear heat ducts may already be fitted and must be physically inspected. All prior IDs preserved, no inflated installed/purchase-ready counts.

## Wave 6: Canadian-market Toyota washer fluid warning and electric trunk actuation (2026-10-29)

[Two new source-backed capabilities UPG-247–248](NEW_FACTORY_AND_REMOTE_CONTROL_DISCOVERY_PASS_6_2026-10-29.md) add Toyota's Canada-only **W1 washer-fluid-level sensor and cluster warning circuit** (original 2004 Corolla EWD533U, genuine `85397-AA040`, connector `90980-11068`) and a 2003–08 Corolla-catalogued **electrically actuated trunk cable-unlatching system** (AutoLoc PK-24294241), a function separate from the original manual remote lever. **248 candidates, 248 linked research records, 362 sources.** These are not installed or purchase-ready, and full individual June-2003 US build retrofit compatibility remains unknown. The original May-2004 nozzle part change `85381-02100 → 85381-12280` was recorded as an unapproved lead with no verified spray or durability improvement; **no extra ID created**.

## Wave 7: new rear-axle, steering-rack, and jounce-load-path engineering (2026-10-29)

[Three mechanical concepts UPG-249–251](MECHANICAL_COMPLIANCE_DISCOVERY_WAVE_7_2026-10-29.md) add distinct **rear torsion-beam pivot compliance** (`Energy Suspension 8.3121`, `PSB222` alternative), **steering rack isolation compliance** (`8.10102`) and **microcellular urethane compression-jounce shaping** (`Monroe 63640`). **251 concepts, 251 linked studies, 393 sources**. Manufacturer applications exist, but **healthy-stock benefit, ride penalty and exact June-2003 TMMC fit remain unverified**; original rear-beam `48725-02230` must not be silently substituted with Japanese-build `48725-12580`. Factory VVT-i solenoid supersessions and an obsolete generic remote window closer were deliberately not admitted as new upgrades. None purchase-ready or vehicle-tested.

## Evidence audit of all 35 new concepts UPG-217–251 (2026-10-29)

[The 35-concept engineering verification report](NEW_CONCEPTS_217_251_EVIDENCE_DEEP_DIVE_2026-10-29.md) is now the **current screening and practical-fitment reference**. It distinguishes 2004 LE model-year maker fit from actual June-2003 TMMC verification, assigns installation and risk gates to every new concept, and identifies practical use-dependent options over healthy OEM. Key findings: exact Corolla `CURT 11265` hitch and `21-27001-02` hood struts are credible application matches; early Corolla `8.3121` rear-beam polyurethane has published bushing bore/sleeve instructions but unmeasured comfort tradeoff; WeatherTech product listings may not indicate *stock*; Rostra Toyota-style heater switch is not necessarily 2004 dashboard-compatible. **Everblades 14V maximum prevents directly approving heated wipers (UPG-243); Monroe 63640 is OE-replacement, not proven healthy-OE improvement (UPG-251); cold LiFePO4 UPG-245 remains poor value.** The follow-up reviewed 35 decision records and substantiated 16 major facts/corrections, adding 7 unique source records. **251 concepts, 251 linked research/decision rows, 393 registered sources**. No item newly confirmed, vehicle-validated or purchase-ready. The vehicle's severe front-end bangs remain a hold on performance driving.

## Early June-2003 TMMC fitment and actual parts economics — five important newer candidates

[Detailed parts-and-fitment report for UPG-221/223/227/230/246](FITMENT_ECONOMICS_221_223_227_230_246_2026-10-29.md) is the current reference for production-aware cost and installation gates. **New, actionable findings:** 15in original Toyota NAP steel wheel `42611-02470 → 02471`, Dorman `939-119` published matching 15x6/5x100/54.1/+45 specifications and *1036lb per-wheel rating* requiring actual axle GAWR validation; four Michelin X-Ice Snow winter tires + four Dorman wheels **$971.32 cross-merchant parts-only**. Redline `21-27001-02` requires **hood and fender drilling**; CURT `11265` original instructions specify four M12 fasteners, 86 ft-lb maker torque, nontrailer rack strap and no drilling, with rusty rear frame rail inspection mandatory. Toyota's June-2003 NAP `W(REAR HEATER DUCT)` front carpet is **a distinct factory part** (`58510-02501`) from the no-duct carpet (`58510-02491`); rear duct four-part observed price **$249.97**, possible additional matching carpet **$327.90–$329.28** *only if actually required*. Interior floor mats and liners must match the rear-heater-duct option. Catalog still **251 concepts, 251 research and decision rows, 393 source records**. This is **not a purchase approval** or exact individual vehicle inspection; October-2003-on OM12859U does not cover June-2003 build directly. Validate CI independently.

## Governing whole-car improvement priority (2026-10-29)

[Balanced whole-car engineering first pass](BALANCED_WHOLE_CAR_ENGINEERING_PASS_2026-10-29.md) is now the governing **research objective**: go beyond healthy factory original 2004 Corolla across **ride/NVH, road comfort, handling/braking, fuel/thermal/electrical efficiency, power delivery, reliability and cabin usability**. Pure preventive maintenance and fault-code TSB fixes are subordinate categories. Research concrete retrofit-ready modern technology even without a Toyota defect bulletin.

**First concrete added evidence within existing IDs**: maker-listed **TEIN EnduraPro PLUS VSL00-B1DS2** OEM-height 16-setting dampers (UPG-083), Bilstein B6 complete catalog-listed set `35-053460` front LH, `35-053477` front RH and `24-069243` rear ×2 (US 2004 LE selection; not yet physical early-build inspection) (UPG-080), Whiteline BTR77 2004 LE listed with manufacturer regional-code conflict (UPG-089), Tire Rack 2025 and 2026 comparative touring tire data (UPG-101), wheel/tire sidewall geometry versus observed 18-inch setup (UPG-104), KYB OE-restoration baseline (UPG-082). These are neither new catalog IDs nor installed products. Full TEIN HBS application, four-corner Bilstein completeness, Whiteline exact bracket fit and independent Corolla road results remain gates.

## October 29 continuation: four-corner B6 verification and measurable whole-car research

[Evidence continuation on braking, A245E driveline, efficiency, NVH and suspension](WHOLE_CAR_MEASUREMENT_AND_B6_COMPLETION_2026-10-29.md) closes **UPG-080's former missing-front-SKU gap** using Bilstein's 2020 manufacturer E12 listing cross-checked against Tire Rack's specific 2004 Corolla LE front-left/front-right/rear application and ShockSurplus component specs. A current retailer **four-corner parts-only price of $878** is recorded, not a completed job estimate. Exact June-2003 TMMC fitment and real-world ride comfort remain gates. The same pass records the SAE 2010-36-0396 vibration peak-localization method under existing UPG-129 and strengthens the diagnostic/measurement sequence across previously existing UPG-101/106/107/129/183/184/194. No new upgrade IDs or install approvals.

## Toyota factory revision and supplier retrofit research (one pillar)

The owner explicitly wants **post-2003 improved physical Toyota parts and supplier-engineered systems** that can benefit an otherwise healthy early-production 2004 Corolla **before a code/failure**. This supersedes recent discovery emphasis on symptom-only factory bulletin remedies; it does not erase their evidence. Use [healthy-car preventive engineering strategy](HEALTHY_CAR_PREVENTIVE_ENGINEERING_STRATEGY_2026-10-29.md) for candidate selection and service-window ranking. High-interest documented baselines: Toyota revised **16620-22013** belt tensioner vs alternatively the complete Gates decoupler system; Toyota improved **17171-22060** intake seal; Toyota revised **15301-22050** oil-level gauge. Identify installed hardware/fitment first, and do not assert durability or economy gains unsupported by data. Future searches prioritize actual later Toyota component improvements with credible drop-in compatibility, not hypothetical ECU reflashes.

## Toyota windshield wind-noise and door-glass countermeasures (2026-10-29)

[Pass 4: windshield reed-noise and independent owner outcomes](FACTORY_DISCOVERY_PASS_4_WINDSHIELD_REED_NOISE_2026-10-29.md) adds **UPG-214 / FCM-024**, a Toyota **T-SB-0257-08** documented repair for exterior windshield molding flutter, and **FCM-025** for existing **UPG-130** Toyota **NV006-05** revised door-glass window runs. **OUT-006–008** record three independent firsthand owner reports, with symptom and part/method/durability limitations preserved. The original 3M 08551 sealer is distributor-listed obsolete; no currently verified drop-in replacement and **no new item is purchase-ready**. Research inventory now **214 concepts**, **25 factory studies**, **8 owner outcomes**, including speculative items. Neither modification addresses bilateral pothole clunks.

## Powertrain engineering and factory control correction (2026-10-29)

[Engine / A245E / electrical countermeasures](POWERTRAIN_ENGINEERING_PASS_2026-10-29.md) records **FCM-026** on existing **UPG-074** (**TransGo SK A246**, hardened TCC boost and solenoid-modulator hydraulic wear remedy for A245E EPC, no verified benefit on healthy transaxle); **new UPG-215 / FCM-027** (Toyota **EG028-04** early Corolla 1ZZ **matched ECM calibration and genuine catalyst** correction for diagnosed P0420, *not* aftermarket high-flow UPG-048); and Rostra's incompatible EPC/SLT terminal variants plus Toyota post-transaxle-repair adaptive reset cautions. **OUT-009** is an independent *fluid/filter* repair report on 2005 Corolla P0741, not validation of the TransGo kit. **215 concepts**, **27 structured studies**, **9 owner reports**, all vehicle-unverified and no new purchase authorization.

## Decision-focused balanced daily-driver package (2026-10-29)

The [balanced performance and quality package](BALANCED_PERFORMANCE_QUALITY_PACKAGE_2026-10-29.md) narrows the broad candidate inventory into an evidence-ranked, staged plan for this vehicle, with actual manufacturer application references, tire-geometry checks, conditional DIY work, costs and specific vehicle-validation gates. The package does **not** classify any candidate as VIN-verified or installed.

## Toyota TSB / factory revision / owner evidence research (2026-10-29)

The [Toyota factory countermeasure and owner evidence catalog](TOYOTA_FACTORY_COUNTERMEASURES_AND_OWNER_EVIDENCE_2026-10-29.md) establishes a new evidence hierarchy and documents **eight Toyota bulletin-led candidate fixes**, measured source distinctions, confirmed conditional part revisions, owner follow-ups, and misleading model-year extrapolations to reject. This includes explicit distinction between Toyota EG021-07 OEM tensioner and *Gates-engineered* alternator-decoupler kit, not Toyota-approved. For reference see [Gates kit analysis](ACCESSORY_DRIVE_DECOUPLER_GATES_2026-10-29.md).

## Continued Toyota factory-discovery pass (2026-10-29)

[Pass 2: factory oil level and brake NVH](FACTORY_DISCOVERY_PASS_2_OIL_LEVEL_BRAKE_NVH_2026-10-29.md) adds **UPG-212 / FCM-022** for genuine Toyota bulletin T-SB-0134-08 (**15301-22030 → 15301-22050** oil gauge and corresponding **3.9 → 4.4 US qt** with-filter refill). Updated specifications and their original manual values are separate database records; early-build/installed-gauge verification is still required. Toyota BR003-05 reversing brake-squeal procedure is linked to existing UPG-107 (not a duplicate ID). Current 212 catalog items are candidate studies, not 212 proven improvements.

 (not ranking owner's goals)

1. **Factory-proven revisions:** Toyota EG045-07 intake gasket and further TSB/supersession investigation.
2. **Documented handling products:** 2003–2008 Corolla suspension listings for Bilstein B12 46-182265, Eibach Pro-Kit, Progress and Whiteline bars. Exact trim, build, wheel clearance, load rating and setup require product-specific review.
3. **Forced induction with historical precedent:** Toyota TRD SC-COR-002-A and present-day Monkeywrench Racing TVS900 offerings include a 2003–04 Corolla/Matrix/Vibe 1ZZ automatic category. Availability, tuning hardware, emissions and cost must be verified.
4. **Current intake architecture:** photographed metal tube/open cone; manufacturer and measurable benefit unknown. Compare to factory airbox, heat shielding, filtration and sensor geometry.
5. **A245E-specific research:** cooling and torque converter/solenoid control are separate projects; generic automatic-transmission parts or software must not be assumed suitable.
6. **Braking and cabin upgrades:** investigate actual vehicle variants, legal requirements, test methods and cost. A generic brake-disc conversion or LED bulb kit is not deemed compatible by listing alone.

## Toyota windshield / door-window wind-noise countermeasures (2026-10-29)

[Factory discovery pass 4](FACTORY_DISCOVERY_PASS_4_WINDSHIELD_REED_NOISE_2026-10-29.md) adds UPG-214 / FCM-024 (Toyota T-SB-0257-08: exterior windshield molding reed-vibration sealing), and FCM-025 linked to existing UPG-130 (Toyota NV006-05: improved sliding door-glass runs). Three real-owner reports are included as OUT-006–008, but exact repaired components and long-term results remain unverified. Totals: 214 concepts / 25 studies / 8 reports; no new installation approved.

## Grounding and limitations

- [TRD 1ZZ-FE supercharger installation PDF](https://www.mr2roc.org/Repository/misc/referencelibrary/trd1zzsuperchargerinstall.pdf) explicitly covers 2003–04 Corolla automatic and calls for matching TRD ECU; standard intake airbox matters.
- [Monkeywrench Racing supercharger install offerings](https://www.monkeywrenchracing.com/mwr-supercharger-install-1zz-2zz-toyota-models/) list 2003–04 Corolla/Matrix/Vibe 1ZZ auto. Their offering does not independently certify New York road legality.
- [Bilstein B12 46-182265 listing](https://www.springrates.com/products/bilstein-b12-pro-kit-suspension-kit-for-2003-2008-toyota-corolla) lists 2004 Corolla, but manufacture, trim and wheel combination still matter.
- [Suspension category listing](https://www.throtl.com/parts/suspension/v/toyota/corolla/2003/) identifies Eibach, Progress, Whiteline, KYB, Bilstein and others; catalog results alone are weaker than manufacturers' actual fitment tables.
- [Historical Toyota/Matrix enthusiast discussion](https://us.toyotaownersclub.com/topic/1146-mods-for-noobs/) offers further research leads, not confirmed applicability.

## Research discipline

Do not auto-populate verified parts.csv from this inventory. Record installation evidence separately from genuine factory equipment. No fabricated horsepower claims, MPG gains, dollar estimates, or durability improvements. Many options are mutually exclusive (e.g. forced induction builds, dampers and lowering packages, wheel sizes). Some substantial build concepts will be difficult, illegal for public-road use without certification, or counterproductive; that is why the next phase must separate good upgrades from merely possible modifications.
