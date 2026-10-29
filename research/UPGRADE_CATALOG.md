# Upgrade research catalog — broad discovery inventory

**Scope:** 2004 US Corolla LE / June 2003 manufacture / 1ZZ-FE / A245E automatic.  
**Status:** **148 distinct engineering research concepts**, all screened in the [initial research pass](UPGRADE_RESEARCH_RESULTS.md), not 148 proven improvements or directly fitting products. See [evidence-linked review rows](../database/upgrade_research.csv) and [schema semantics](../docs/UPGRADE_RESEARCH_SCHEMA.md). No condition triage.

The linked [CSV catalog](../database/upgrade_candidates.csv) contains every identified research direction with a stable ID, subsystem, intended benefit, evidence maturity, and verification gate. It distinguishes:
- **documented_lead**: a published Toyota/TRD or manufacturer reference exists for the concept or a related model; not proof of this car's fitment.
- **research_hypothesis**: an engineering concept worth investigating; no product or measured benefit yet confirmed.
- **literature_reviewed**: initial findings or explicit evidence gaps recorded; full verification remains open.
- **candidate / probable**: current fitment classes; none confirmed or vehicle-validated. Original `candidate_unverified` describes the discovery state only.

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

## Grounding and limitations

- [TRD 1ZZ-FE supercharger installation PDF](https://www.mr2roc.org/Repository/misc/referencelibrary/trd1zzsuperchargerinstall.pdf) explicitly covers 2003–04 Corolla automatic and calls for matching TRD ECU; standard intake airbox matters.
- [Monkeywrench Racing supercharger install offerings](https://www.monkeywrenchracing.com/mwr-supercharger-install-1zz-2zz-toyota-models/) list 2003–04 Corolla/Matrix/Vibe 1ZZ auto. Their offering does not independently certify New York road legality.
- [Bilstein B12 46-182265 listing](https://www.springrates.com/products/bilstein-b12-pro-kit-suspension-kit-for-2003-2008-toyota-corolla) lists 2004 Corolla, but manufacture, trim and wheel combination still matter.
- [Suspension category listing](https://www.throtl.com/parts/suspension/v/toyota/corolla/2003/) identifies Eibach, Progress, Whiteline, KYB, Bilstein and others; catalog results alone are weaker than manufacturers' actual fitment tables.
- [Historical Toyota/Matrix enthusiast discussion](https://us.toyotaownersclub.com/topic/1146-mods-for-noobs/) offers further research leads, not confirmed applicability.

## Research discipline

Do not auto-populate verified parts.csv from this inventory. Record installation evidence separately from genuine factory equipment. No fabricated horsepower claims, MPG gains, dollar estimates, or durability improvements. Many options are mutually exclusive (e.g. forced induction builds, dampers and lowering packages, wheel sizes). Some substantial build concepts will be difficult, illegal for public-road use without certification, or counterproductive; that is why the next phase must separate good upgrades from merely possible modifications.
