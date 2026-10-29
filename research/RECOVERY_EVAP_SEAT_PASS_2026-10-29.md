# Felicity: resumed fuel-filler and seat investigation

Reviewed October 29, 2026; baseline commit `1b7c4352e9ab0f0158218b0b0aa46f045ebb7b2f`.

## Recovery verification

The research branch still contained the prior saved milestone. Tavily search and HTML extraction both succeeded in this session. Later extraction requests returned HTTP429; the connection worked but was rate limited. The Toyota filler bulletin PDF was read through a second retrieval route. Missing seat tables remain explicitly unresolved rather than inferred from snippets.

## UPG-199 / FCM-007: fuel filler sealing revision

Toyota EG051-06 (August 23, 2006), printed/PDF pages1-2, covers 2003-04 Corolla2WD. It changes pipe77201-02080 to77201-12750. When the specified EVAP codes occur, the diagnostic branch inspects the cap seat for corrosion, replaces the pipe if corroded, checks cap-seal damage and confirms the repair through the EVAP monitor. An undamaged cap is not automatically a revised component. No corrosion routes diagnosis elsewhere. The bulletin does not identify the revised material/coating or quantify service life. Document scope includes the early build without proving Felicity has this fault or an original pipe.

Modern Toyota displayed$248.51 and Capistrano Valley Toyota$271.94 for the pipe on the review date; both show the old number as superseded. These are dealer listings, not verified stock or full-job totals. Their mixed-model date descriptions cannot supply a Corolla production breakpoint. The historical0.4 warranty allowance is not a timed DIY job or current labor quote. This is a conditional repair revision, with no measured gain over a healthy sealing original.

Sources: [Toyota bulletin PDF](https://static.oemdtc.com/TSB/EG051-06.pdf), [Modern Toyota](https://wholesaledirect.moderntoyota.com/oem-parts/toyota-fuel-tank-filler-neck-7720112750), [Capistrano Valley Toyota](https://parts.capovalleytoyota.com/oem-parts/toyota-fuel-tank-filler-neck-7720112750).

## UPG-200 / FCM-008: seat frame revision remains conditional

The archived US Toyota NV012-06 narrative, dated December6, 2006, describes replacement with an improved assembly/frame for lower-cushion shifting/noise in pre-change2004-06 Corolla. Production VIN and part tables are embedded images that could not be read in this session. Therefore exact June2003 TMMC eligibility, options and revised service part remain unresolved, with candidate fitment and gradeD. No generic seat-frame seller listing has been substituted for the missing revision table.

This intervention differs from UPG-198's locator-pin contact remedy and UPG-138's support/upholstery concept. Correct seat/restraint configuration and the full factory procedure are prerequisites. No part quote, installation duration, owner success or actual-car result is claimed.

Source: [archived US NV012-06](https://charm.li/Toyota/2004/Corolla%20L4-1.8L%20%281ZZ-FE%29/Repair%20and%20Diagnosis/Technical%20Service%20Bulletins/Customer%20Interest/Seats%20-%20Movement%20Or%20Noise/). The separately indexed Canadian bulletin is not used as US-market applicability proof.

## Exclusions and next evidence

T-SB-0037-11's headliner-water-leak application names other Toyota models, not Corolla; logged as FCX-002, with no candidate count. New source IDs and all three upgrade ledgers link to the structured factory records. Both new candidates remain purchase_ready=no and untested on Felicity. The catalog now contains200 stable concept IDs; this includes unresolved/overlapping historical studies and is not a count of verified upgrades.

Next: obtain readable NV012-06 tables; verify current filler-pipe EPC application and complete-job cost if diagnosis justifies it; seek revision-specific independent repair outcomes. Body corrosion material alternatives remain an open research area.

## Validation

All31 existing unit tests passed. CSV validation with full upgrade coverage passed. The structured-record audit checked unique factory IDs, candidate links, all source references and unchanged no-installation status. These checks establish data integrity; they do not establish physical fitment.
