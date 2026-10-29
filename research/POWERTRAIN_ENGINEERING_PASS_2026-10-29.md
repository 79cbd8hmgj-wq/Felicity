# Felicity — Engine, A245E transmission and electrical countermeasure pass

**Research date:** October 29, 2026. **Target:** U.S.-market **2004 Toyota Corolla LE**, Canadian TMMC June 2003, factory model **ZZE130L-DEPNKA**, 1ZZ-FE / **A245E** (as-built factory label). Actual installed electronics, ECM calibration, valve-body castings and maintenance/repair history **not inspected**. No owner report of erratic shifting, torque-converter slip codes, charging complaints or a P0420 emissions code. Existing front pothole clunks are a separate chassis diagnostic issue.

**Baseline:** 214 canonical upgrade IDs, 25 countermeasure studies, eight independent outcome records. This pass favors upgrading existing evidence for catalogued engine/transmission opportunities rather than creating redundant candidate IDs to inflate the total. Two main technical investigations: **TransGo SK A246** for existing **UPG-074**, and **Toyota EG028-04** ECM/catalyst coordinated remedy related to **UPG-048**. Additional safety/application gates involve **UPG-072** SLT solenoid identification, **UPG-184** diagnostics and **TC002-03** ECM adaptive-values reset.

## 1. Manufacturer-engineered A245E/A246E hydraulic wear correction — existing UPG-074

**TransGo primary engineering source:** https://transgo.com/product-details/toyota-a246e-shift-kit/ , SKU **SK A246**. 2003–2008 Corolla **A245E with EPC pressure-control solenoid**, A246E Matrix/Vibe 2WD applications also listed. Distinct from **A245-HD2**, which is explicitly **1993–2002 A245E without EPC** and not this car's expected system. Supplier provides kit installation instructions under its page; installation is through transmission pan/valve-body access, not a transmission removal.

**Actual engineering:** Manufacturer identifies wear in (a) the **TCC relay boost valve and bushing**, affecting converter-clutch hydraulic engagement/release and temperature, and (b) the **solenoid modulator valve bore**, affecting pressure delivered to control solenoids. Kit includes a **hardened-steel drop-in TCC relay boost valve and bushing**, and **redesigned solenoid-modulator valve assembly, bushing, spring, end plug and retainer**. It explicitly lists intermittent shuttle shifts, flare or bind on 2→3, throttle-related 3rd/4th slip, engine stalling at stop and torque converter clutch codes as targeted complaints. These are **manufacturer design claims**, not independently measured same-car durability outcomes.

- **Current observed source price:** NorCal Transmission Parts **$90.00** for **SK A246**, marked in stock at search time; retail listing https://norcaltransmissionparts.com/sk-a246-toyota-a246-transmission-transgo-shift-kit-2003-08.html . Parts only, not tax/shipping/filter/ATF/pan gasket/solenoid/bench tools/labor. Recheck at purchase.
- **Time/difficulty:** manufacturer says *transmission removal not required*, not *valve body simple*, so classify **advanced/professional precision hydraulic work**. No safe quick DIY time estimate established. Avoid contamination, incorrect check-ball/bolt placement, or blind pressure modification.
- **Why compelling:** A genuine supplier-developed physical redesign of wear-sensitive valve/bushing interfaces, not a performance marketing label or software tune. This meets Felicity's upgrade philosophy, but only if inspection proves worn hydraulic circuits or a rebuild is already warranted; no proof of benefit in a healthy A245E. **A245-HD2 must not be substituted.**
- **Toyota factory link:** Toyota 2004 A245E repair material illustrates separate **S1, S2, SL, SLT** valve-body solenoids and diagnostic routing. Toyota **TC008-04**, Nov 22 2004, documents multi-cause P0741 investigation (wrong speed sensor/parts, lockup hydraulic, converter, ECM, etc.) and gives its *published production VIN table for NUMMI only*, not TMMC; it does not prescribe TransGo conversion. https://charm.li/Toyota/2004/Corolla%20L4-1.8L%20%281ZZ-FE%29/Repair%20and%20Diagnosis/A%20L%20L%20%20Diagnostic%20Trouble%20Codes%20%28%20DTC%20%29/Testing%20and%20Inspection/P%20Code%20Charts/P0741/Troubleshooting/ . **Do not assume P0741 means replace the valve body or torque converter.**
- **Independent outcomes:** No credible long-duration report proving *SK A246 installed in an early TMMC Corolla A245E* and resolving the original defect was found; retain **Level C supplier engineering/application**, **not Level B**.

### Solenoid and casting interchange traps — existing UPG-072

**Rostra transmission component specialist's technical note (May 7 2010):** https://rostratransmission.wordpress.com/2010/05/07/97/ . A245/A246 **SLT / EPC line-pressure solenoid connector** variant **52-0403**, large terminal blades, is catalogued for **2002–03**; **52-0419**, small connector pins, for **2004-on**. They are explicitly **not interchangeable**. This is an exact part identification warning, not evidence the 2004-on solenoid is more reliable than the earlier design.

**Important nuance:** This owner's *model year* is 2004 but the manufacture date is **June 2003**. Rostra source speaks in model years and does not give production-day or plant cutoffs, so inspect the **actual connector pin form and solenoid** before ordering. Do **not** infer early-production 2004 automatically retains the 2003 solenoid. A used/rebuilt transmission may differ from original factory A245E.

**Sonnax 97741-20K** oversized lockup relay valve and **77741-02K** lockup relay control valve explicitly restrict A245E/A246E compatibility to **2005 or later, upper casting 9132**: https://www.sonnax.com/units/255-a340e ; https://www.sonnax.com/parts?categories%5B%5D=3&makes%5B%5D=18&unit_relationships%5B%5D=255 . **Do not install these in an early 2004 casting** without actual cast identification and manufacturer authorization. No performance gain, durability or kit fitment inferred from shared A245E naming.

### Toyota's factory ECU learned-values reset after transmission repair

**Toyota TC002-03 (revised Dec 20 2004)**: https://charm.li/Toyota/2000/Corolla%20LE%20Sedan%20L4-1.8L%20%281ZZ-FE%29/Repair%20and%20Diagnosis/Technical%20Service%20Bulletins/All%20Technical%20Service%20Bulletins/Engine%2FTransmission%20Controls%20-%20Resetting%20ECM%20Memory/ ; 2004 vehicle entry https://workshop-manuals.com/toyota/corolla/l4-1.8l_%281zz-fe%29/relays_and_modules/relays_and_modules_powertrain_management/relays_and_modules_computers_and_control_systems/engine_control_module/component_information/technical_service_bulletins/all_other_service_bulletins_for_engine_control_module/tc002r-03/dec/04/engine/transmission_controls_resetting_ecm_memory/ .

Toyota says after an **automatic transaxle replacement, overhaul or replacement of individual transmission components**, clear ECM *learned values* using the proper model-specific reset procedure to minimize postrepair shift quality issues; bulletin provides two different methods including diagnostic tester or battery disconnection for separate supported applications, with **application chart embedded** and not yet authenticated for this early A245E. **Do not prescribe battery disconnection as a guaranteed relearn method for this car or reset an otherwise healthy automatic preemptively.** This is an important procedural companion to TransGo work, not a new hardware upgrade or an ECU performance tune.

## 2. Toyota EG028-04 factory 1ZZ emission calibration and catalyst matched update — prior UPG-048

Toyota **EG028-04 revised October 8 2004** directly covers 2003–2004 Corolla 1ZZ-FE before specified production breakpoints. Toyota prescribes a **matched ECM reflash + revised catalytic converter/pipe assembly** to address P0420, and states it is the **same intervention as EG016-04 sulfur-odor remedy**, to be done only once. The published replacement repair front-pipe part in repository research is **17410-0D360**, superseding some original 17410-0D150 / 17410-22470 applications. Do **not** treat this as aftermarket high-flow or emissions-delete tuning; emissions and sensor performance remain essential. Factory archived bulletin: https://charm.li/Toyota/2003/Corolla%20CE%20Sedan%20L4-1.8L%20%281ZZ-FE%29/Repair%20and%20Diagnosis/Powertrain%20Management/Technical%20Service%20Bulletins/By%20Symptom/Customer%20Interest/Engine%20Controls%20-%20MIL%20ON%2FDTC%20P0420%20Stored/ .

**Noteworthy new plant evidence:** aftermarket technical-service cross-reference **099-1662** lists Toyota EG028-04 Corolla production change breakpoints:
- Shokki `JTDBR3#E#52048919`
- NUMMI `1NXBR3#E#4Z339353`
- **TMMC `2T1BR3#E#4C312392`**
- Matrix `2T1*R3#E#RC836439`

Reference: https://www.autopartsprime.com/resources/installation/oem/2020/pdf/16130.pdf (one-page distributor technical note; original Toyota image-based VIN table still must be read to elevate this cross-reference). Its TMMC entry makes the earlier public claim **'only NUMMI is relevant' false for EG028-04**; that confusion pertains **Toyota TC008-04 P0741**, a separate automatic-transmission bulletin. A **June 2003 TMMC build likely predates** the listed `4C...` production change, but exact VIN applicability **must be checked privately**, and presence of a previous authorized calibration/pipe change is unknown. Don't post the VIN to GitHub.

Owner result proof: no documented long-term 2004 Corolla exact **ECM calibration plus genuine 17410-0D360 pipe** field result retrieved. P0420 can result from exhaust leaks, mixture faults, aged O2 sensors or genuine converter failure; diagnosis first. Reflash is dealer/specialist work; a failed flash can brick the ECU. Restrict emissions-system modifications to NY road-compliant parts and correctly configured OEM calibration. A currently fault-free healthy vehicle has **no demonstrated acceleration, economy, or longevity gain** from this repair.

**Separation warning:** Existing UPG-048 in Felicity refers to a *MagnaFlow high-flow converter study*, and the factory EG028-04 remedy is **not evidence MagnaFlow adds performance or satisfies the factory matched calibration requirements**. Do not falsely reclassify aftermarket product as Toyota's improved part.

## 3. Factory and supplier evidence exclusions

- **Toyota TC014-06 / ECM P2716 harsh shifting** applies to **2005–2007 Corolla/Matrix**, not 2004; the ATRA and aftermarket bulletins identify ECM hardware faults for that later range. Do not prescribe that later ECU to this 2004 car. Manufacturer bulletin mirror: https://images.oreillyauto.com/parts/img/documents/ptq/pb_2005_2007_toyotacorolla_matrixecm.pdf .
- **Toyota EG027-06 engine mount 12305-0D022 → 12305-0D120** addresses **2005–2006**, not 2004; the early original 12305-0D021 build is different. Do not assume direct swap. Existing Felicity backlog records details.
- **Toyota EG022-07 cold-idle ECM flash** is **manual transmission only**, while this vehicle is automatic. Source: https://charm.li/Toyota/2003/Corolla%20CE%20Sedan%20L4-1.8L%20%281ZZ-FE%29/Repair%20and%20Diagnosis/Powertrain%20Management/Relays%20and%20Modules%20-%20Powertrain%20Management/Technical%20Service%20Bulletins/Customer%20Interest/Engine%20Controls%20-%20Idle%20Hunting%20in%20Sub-Freezing%20Temp/ .
- **Toyota EG014-02 (P0125/P0130/P0133 oxygen sensor change)** is **2003 model-year only**, even if its September 2003 *publication date* postdates this car's June 2003 construction; it does **not establish a 2004 model-year O2 sensor revision**. https://charm.li/Toyota/2003/Matrix%202WD%20L4-1.8L%20%281ZZ-FE%29/Repair%20and%20Diagnosis/Powertrain%20Management/Technical%20Service%20Bulletins/Customer%20Interest/Engine%20Controls%20-%20MIL%20ON%2FDTC%20P0125%2FP0130%2FP0133%20Stored/ .
- Toyota's generic **radiator cap inspection revision EG014-05** is **not a stronger radiator cap or a higher pressure specification** and should not create an upgrade ID. Inspect to original identified cap rating; **do not increase system pressure** for perceived performance. https://charm.li/Toyota/2005/Corolla%20L4-1.8L%20%281ZZ-FE%29/Repair%20and%20Diagnosis/Technical%20Service%20Bulletins/All%20Technical%20Service%20Bulletins/Cooling%20System%20-%20Radiator%20Cap%20Inspection%20Procedure/

## 4. Candidate database decisions

- **FCM-026 / existing UPG-074 = Level C**, supplier-supported **SK A246** physical valve and bushing redesign on listed A245E **EPC-equipped** model family. No measured healthy-OEM gain, no owner Level B outcome. **Purchase ready: false**.
- **Existing UPG-072** solenoid research gets **Rostra connector variant** caveat. No newly documented improved OEM solenoid grade or catalog ID.
- **Existing UPG-048** gains **TMMC Corolla production cutoff** cross-reference for Toyota EG028-04; this changes **Toyota OEM remedy documentary confidence only**, not aftermarket converter power claims. No new ID.
- **Existing UPG-184 / FCM-018** gains TC002-03 adaptive reset procedure context and exact-match gating for post-automatic-repair operation. No new ID, no automatic flash authorization.
- **Independent owner outcomes newly authenticated for exact kit:** zero. This is explicit — a manufacturer claim or unspecified shop report is not Level B.
- **Technical importance:** medium to high if the automatic develops verified hydraulic wear or P0420. **Purchase urgency:** low when engine and A245E are currently working normally. No arbitrary engine power/MPG/shift-lifespan numbers.

## 5. Next research gates

1. Verify *installed* A245E original/replacement valve-body casting, EPC SLT solenoid electrical connector and code/history before selecting any kit.
2. Obtain TransGo's current actual **SK A246** instruction edition and compare internal flow/orifices/spring check-ball diagram to exact early A245E valve body; assess full ATF, filter, pan gasket, tool cost, pressure test and transmission leak-check.
3. Obtain matched independent post-install reports of this exact kit in a 2003–08 Corolla A245E and follow-up over multiple service intervals, including failures.
4. Obtain Toyota TC002-03 reset **application chart** and check whether correct 2004 A245E uses tester or battery-based method; never reset a healthy gearbox based on a generic bulletin excerpt.
5. Read Toyota original EG028-04 production VIN and calibration images. Check actual 2004 ECU part/calibration and prior authorized mods without logging VIN publicly.
6. Systematic future searches for *new* 2004 TMMC-compatible starter/charging alternator rectifier/regulator revisions and factory 1ZZ ring/PCV changes: **nothing sufficiently verified in this pass** to add an entry. Avoid inventing a retrofit.

All relevant source findings should be linked in the canonical source and existing candidate ledgers. No actual replacement work performed, no repairs marked done.
