# Crypto Grad Paths: independent review (2026-11-06)

Scope: local `index.html`, `schools.json` (57), `internships.json` (76), both method files, plus live spot checks against official pages (WebFetch/WebSearch only, no browser). The deployed GitHub Pages JSON matches the local copy.

**Overall verdict.** The program logistics are mostly accurate. 18 school pages re-read (deadlines, fees, funding text) all matched. 13 internship postings re-read also matched on deadline, eligibility, letters and pay (a16z, CISPA, ETH SSRF, IDA SCAMP-La Jolla, LANL CSRP, LLNL CSI, Weizmann, EPFL, NTT CIS and others). The weak spots are elsewhere:
- **Faculty coverage:** CSrankings lags behind faculty moves, and some schools are badly undercounted.
- **Costs:** the UC numbers are the wrong figures for Sahmoud.
- **Missing categories:** PhD-direct routes, math-department routes and funded MS.
- **Clutter:** many internship rows he cannot apply to.
- **UI:** no deadline view.

## 1. Errors found

10 factual or data errors. Rows 11-13 are misleading but technically defensible.

| # | Item | Field | Site value | Correct value | Source |
|---|---|---|---|---|---|
| 1 | Stanford | professors / n_professors | 1 (Dan Boneh only) | At least 2. **Mark Zhandry** has been Associate Professor of CS since Fall 2025 (ex-Princeton/NTT; theory and quantum crypto). Emma Dauterman (Asst. Prof., applied crypto systems) is also listed. | https://profiles.stanford.edu/mark-zhandry ; https://simons.berkeley.edu/people/mark-zhandry ; https://profiles.stanford.edu/144458 |
| 2 | UIC (Chicago) | professors / n_professors | 1 (Alexander Block) | Also **Daniel J. Bernstein** (Research Professor; post-quantum and ECC, a major name) and Anrin Chakraborti (Asst. Prof. since Fall 2023, cryptographic tools). | https://cs.uic.edu/profiles/daniel-j-bernstein ; https://cs.uic.edu/news-stories/cryptographic-tools-researcher-joins-cs-department-faculty |
| 3 | Univ. of Chicago | whole school | Missing | Should be listed: David Cash (Assoc. Prof., theoretical and applied crypto) and Aloni Cohen (Asst. Prof., theory crypto and privacy). The MPCS has a "Pre-Doctoral MS in CS" research track. Sahmoud asked about Chicago specifically. | https://computerscience.uchicago.edu/people/david-cash ; https://news.uchicago.edu/profile/david-cash |
| 4 | Cornell | professors | 3 (Ithaca only) | Leaves out the Cornell Tech (NYC) crypto faculty: Rafael Pass, Ari Juels, Tom Ristenpart (all on the Cornell CS directory). This matters for the NYC filter. *Verify why the dblp/CSrankings pass dropped them.* | https://www.cs.cornell.edu/people/rafael-pass ; https://tech.cornell.edu/research/security-group |
| 5 | UW Seattle | professor homepage links | Tessaro and Lin link to `cs.ucsb.edu/~tessaro` and `~rachel.lin` | Both have been at the UW Allen School since about 2019. The links point to their old UCSB pages, which suggests they are still at UCSB. | CSrankings / UW Allen School directory |
| 6 | NTT Research CIS | category | "Big tech" | "Industry research labs". NTT Research is a basic-research lab, not big tech. This miscategorization also hides it from the industry-lab filter. | https://careers.ntt-research.com/cis |
| 7 | NSA GMP (also CASASP, SoS) | deadline source | USAJobs 880807100, cited for "CLOSED 08/15-09/05/2026" | That announcement is the **Cyber Summer Program** (1261601). GMP has its own announcement (intelligencecareers job 1261493), whose close date was not verified. The status is probably closed but is mis-sourced. Re-check before telling him GMP is dead for 2027. | https://www.usajobs.gov/job/880807100 ; https://apply.intelligencecareers.gov/job-description/1261493 |
| 8 | Arizona Winter School 2027 | deadline_summer_2027 | null, so the UI shows "not posted yet" | **Student application deadline is Nov 24, 2026** (18 days away). Also, the school runs **March 6-10, 2027**: it is neither summer nor an internship, and it clashes with his spring semester. | https://swc-math.github.io/aws/2027/index.html |
| 9 | UC Riverside vs other UCs | total_tuition_usd | UCR uses 4 quarters ($40,224); UCSD, UCLA and Berkeley use 6 quarters | Inconsistent basis. On the 6-quarter basis UCR is $60,336. The Student Services Fee ($448/qtr) is also included for UCI, UCR and UCSB but excluded for UCSD, UCLA and Berkeley. | tuition_basis fields in schools.json |
| 10 | Tuition comparisons in general | total_tuition_usd | Labeled "tuition only" | The basis is mixed. UT Austin, FSU and VCU bundle fees in. Texas A&M excludes a $2,565/semester Engineering Program Fee (about $7.7k over 3 semesters), so its $25,092 is understated against its peers. | TAMU, UT, FSU and VCU bases in schools.json |
| 11 | UC schools (Berkeley, UCLA, UCSD, UCI, UCSB, UCR) | total_tuition_usd | Non-resident totals ($57,648 / $60,336) | **He is a CA resident.** Resident tuition: Berkeley, UCLA and UCSD **$27,444** for 2 years (systemwide tuition only); UCI and UCSB **$30,132** including the Student Services Fee; UCR $30,132 for 6 quarters. The "lowest tuition" sort currently ranks UCs mid-pack when they are among his cheapest research options. | Same registrar rates the site cites, minus NRST |
| 12 | Cornell / Princeton / Yale 2-yr | total_tuition_usd | $59,000 / $130,420 / $104,800 | Net cost to him is about $0 plus a stipend (TA-funded). Princeton is also closed for Fall 2027. The cost sort shows sticker price, which is misleading. | Funding notes already in the JSON |
| 13 | a16z Frontier | category / top pick #1 / difficulty | "Blockchain / web3 research", Moderate | The lab is now multidisciplinary (AI, bio, energy, materials, pure math, crypto...). One open call across all fields makes it more competitive than "Moderate". Hard is more honest. The deadline, pay and letter details are correct. | https://boards-api.greenhouse.io/v1/boards/a16z/jobs/8046730003 |

**Checked and correct.** Each school row below was compared with its official page:
- **CMU:** Dec 9 final and Nov 18 early deadlines.
- **Berkeley:** Dec 1; the M.S.-only caveat is noted.
- **Stanford:** Dec 8.
- **Cornell:** Jan 18 and TA funding.
- **UT Austin:** Dec 15, letters Dec 20.
- **CCNY:** May 1.
- **Stony Brook:** Mar 15, 2027 and $1,158/credit.
- **Oregon State:** Jan 5, 2027 (PhD Dec 10).
- **Portland State:** Mar 1.
- **FSU:** Jan 1 / Apr 1.
- **Virginia Tech:** Dec 1.
- **UCLA:** Dec 15.
- **UCSD:** Dec 16.
- **Northwestern:** Nov 30 / Dec 31 / Feb 28 / Jun 15 rounds.
- **Purdue:** Dec 1.
- **Maryland:** Dec 4.

Professors confirmed: Corrigan-Gibbs (Berkeley), Golovnev (Cornell), Miao (Brown), Waters (UT Austin plus NTT), Tyagi (UW), Fermi Ma (NYU).

Internships confirmed: a16z (Nov 20, 12pm PT; 1 letter; $4k/wk Masters), CISPA (Nov 30 AoE; BSc/MSc in CS/CE/EE/telecom or equivalent), ETH SSRF (Dec 16, 13:00 CET; math is OK), IDA SCAMP-L (Nov 14; US citizen; grad students considered), LANL CSRP (to Feb 1, 2027; 3.2 grad GPA; Advanced Cryptography track), LLNL CSI ($10,215/mo; no close date), Weizmann K-G (Jan 20, 2027; GPA 3.6), EPFL (Nov 29, 2026; CS/CE/Telecom/EE only), NTT CIS (Dec 20; PhD).

## 2. Missing schools / internships

### Schools (US, active crypto faculty)
- **University of Chicago** (Cash, Cohen; MPCS Pre-Doctoral MS). This is a high priority because he asked about Chicago.
- **Cornell Tech, NYC** (Pass, Juels, Ristenpart). Give it its own row or a Cornell NYC alt-program; the only master's is the M.Eng, which is worth flagging honestly.
- **UIC** is undercounted (Bernstein), and so is **Stanford** (Zhandry). With those fixed, the Chicago and Bay Area filters change materially.
- **Penn:** Tal Rabin is still described as Penn's Rachleff Professor in public bios. The methodology's "not on the directory" check should be re-done.
- **CSU Los Angeles itself** (his current M.S. Math) as the baseline row: cost, thesis option, time to finish. Every other row is implicitly "vs. staying".
- The requested list is otherwise present: Stanford, MIT, Harvard, Berkeley, UT Austin, Michigan, Wisconsin, Penn, Duke, UCSB, Rice, Stony Brook, ASU, Oregon State, Brown, Princeton and UW are all there. UCSC is absent, which is defensible because it has no qualifying crypto faculty.

### Internships / summer
- **IDA CCS Bowie SCAMP** (third SCAMP site; only La Jolla and Princeton are listed).
- **KU Leuven COSIC** and **Galois** were in Sahmoud's own ranked CSV (`summer_2027_programs_ranked_by_fit_and_prestige.csv`) but are absent or dropped here. Galois is marked "no verifiable program", so reconcile it with his list.
- **Crypto schools:** EPFL-ETH lattice school, IACR-sponsored schools, Simons Institute summer cluster or workshops. The method says "none found for 2027". Keep "watch" rows so they are not forgotten.
- **Companies:** Duality Technologies (FHE, NJ), IOG/Input Output research internships, Google DeepMind Student Researcher. Each needs to be checked; none is confirmed.
- **"Summer RA with a professor (self-arranged)"** is missing as a category. For an MS student without crypto papers, this is the most realistic route, and he already has a live thread: Wei-Kai Lin (UVA, ORAM/MegaBlocks) and his memory-checking draft. Every professor in schools.json is a potential host, so link the two tabs.
- **NSF GRFP** (fellowship, not an internship): his one eligible cycle, with a mid-Nov 2026 deadline. It belongs in a "funding" strip next to the internships.

### Categories he clearly needs
1. **PhD-direct.** MIT, Princeton (MSE closed for Fall 2027), Harvard, Berkeley (M.S./Ph.D.), CMU and Cornell (the MS is "not a path to the PhD") all point to applying straight to the PhD. That is about 6 rows where the actionable item is the PhD deadline (Dec 1-15, 2026, which is **4-6 weeks out**). Today it is buried in notes or null fields.
2. **Funded or near-free MS.** Cornell (TA-funded), Yale 2-yr (tuition fellowship), Wisconsin (traditional MS/PhD pool funds many), WSU, FSU, UIC and Oregon State (TA/RA considered), plus UC resident pricing. This should be a filter.
3. **Math-department routes.** Number-theory and algebraic-geometry groups and math-department cryptographers (for example CU Boulder (Stange, isogenies/lattices), Clemson (Gao), and number-theory groups at UCSD and Wisconsin) are explicitly excluded. That is the natural bridge from his M.S. Math, so it is the biggest structural gap for *his* profile. Each name needs verification before it is added.
4. **His existing USC MS CS admit (deferral possible).** The USC row should say so; it is the only "already admitted" option.

## 3. Missing fields / features (ranked by value to him)
1. **Resident vs non-resident cost, plus net cost after typical funding.** This changes the UC and CSU ranking and the funded-MS ranking.
2. **"Apply-by" timeline/calendar with days-left**, across both tabs, with priority and final deadlines as separate columns. For example, the CMU early deadline Nov 18 ($80 vs $100 fee), the Northwestern rounds and the USC scholarship deadline Dec 15 are all buried in prose.
3. **"Can I apply?" hard filter** that hides PhD-only, undergrad-only (NSA DSP, NIST SURF, DIMACS REU, CMU SPUR) and closed programs. Today 23 of 76 internships are "no" for MS students, and 11 more are "unclear".
4. **PhD-direct column** per school: PhD deadline, and whether the MS feeds the PhD (CMU and Cornell say no; Wisconsin says yes without reapplying).
5. **Theory-only professor count.** The headline "N crypto professors" counts security-venue applied people (Popa, Zheng, Brown, Piskac...) the same as theorists. The chip should show "theory profs" first.
6. **Location filter on internships** (NYC, Bay Area, Chicago, LA, remote, abroad). Schools have a region filter; internships have none.
7. **Eligibility risk flags for a Math MS** as a chip (CISPA and EPFL list CS/CE/EE; Berkeley and UCLA have prior-master's rules; LANL needs a 3.2 GPA; Weizmann needs a 3.6 GPA).
8. **Letters needed and turnaround** as a structured count, not prose. He has a 2-letter bottleneck (Mijares plus Krebs).
9. **Status field** (open / not yet posted / closed / watch) instead of a free-text deadline string, so it can sort.
10. **Acceptance-odds band** for schools (MS acceptance rate where published). This is optional, and only with sources.

## 4. UX issues (index.html)
- **No deadline sort or filter on the Internships tab.** The sorts are picks, reach and prestige only. The deadline is a free-text quote, so it cannot be sorted. This is the most-needed control.
- **School deadline sort uses the earliest stated date**, mixing priority, round-1 and final deadlines (Northwestern Nov 30 is round 1 of 4). There is no countdown and no "passed" styling.
- **Cost sort uses sticker non-resident tuition.** It ranks fully funded Cornell above cheaper unfunded schools and leaves Princeton (closed) in the list.
- **Methodology tab dumps raw Markdown** into a `pre-wrap` div. Tables render as pipe characters and bold as `**`. Render it with a small MD library, or pre-render to HTML.
- **Long quote blobs** in every card (eligibility, deadline, "why this prestige", "honest read") make each internship card about 15 lines. Show a one-line summary and put the quote in a `<details>`.
- **`notes` objects are rendered with `JSON.stringify`**, which shows raw braces on some cards.
- **MIT and Harvard show "Program: (not found)"** and blank cost/deadline. They should say "PhD only: apply Dec 1 / Dec 15" with a link.
- **Search is limited:** school search skips notes, `alt_programs` and research_fit_note, and internship search skips eligibility and notes. For example, searching "PhD" or "funded" finds little.
- **No table/compact view** for side-by-side comparison of 57 schools. Cards only; information density is low on desktop.
- **Filters are not in the URL** (only the tab is in localStorage), so he cannot share or bookmark "NYC + thesis + by deadline".
- **Region values are uneven:** "NYC", "Boston" and "Chicago" are metros, while "Northeast" and "Midwest" are regions. Ithaca and Princeton fall under "Northeast", so the NYC filter misses Cornell Tech, and the Chicago filter missed UChicago entirely.
- **Prestige sort is inflated by non-internship schools:** SLMath and PCMI are rated "Top" though neither is crypto. Separate "Schools/workshops" from "Internships" or exclude them from that sort.
- **Mobile is mostly fine:** the kv grid collapses at 600px, nav wraps, and there is no horizontal scroll. However, cards become very long, and the professor lists are only in `<details>`, which is good.

## 5. Top 10 fixes (ranked)
1. **Add an "Apply-by" timeline** (both tabs, days left, priority vs final). The next 6 weeks hold IDA SCAMP (Nov 14), a16z (Nov 20), the AWS winter school (Nov 24), EPFL (Nov 29), CISPA (Nov 30), PhD deadlines (Dec 1-15), ETH (Dec 16) and NTT (Dec 20).
2. **Show CA-resident UC pricing and a net-cost column** (funded MS = about $0), and fix the UCR and fee-basis inconsistencies.
3. **Add PhD-direct as a first-class option** per school with its PhD deadline. It is the real route at MIT, Princeton, Harvard, Berkeley, CMU and Cornell.
4. **Fix the faculty undercounts:** add Zhandry (Stanford), Bernstein and Chakraborti (UIC), UChicago (Cash, Cohen) and Cornell Tech (Pass, Juels, Ristenpart). Re-check Tal Rabin (Penn). Fix the UW homepage links.
5. **Add a "Can I apply?" filter**, on by default, that hides PhD-only, undergrad-only and closed rows. Add Math-MS eligibility risk chips.
6. **Add a deadline sort and a location filter to Internships**, and convert the deadline to a structured date and status.
7. **Add the missing categories:** math-department crypto/number-theory routes, a self-arranged summer RA with a professor (link the professor lists, starting with Wei-Kai Lin at UVA), and a funding strip (NSF GRFP).
8. **Correct the data errors:** move NTT to industry labs, put the AWS winter school's Nov 24 deadline in the deadline field and label it as March, re-source NSA GMP, and recategorize a16z and drop it from Moderate.
9. **Flag his own facts on rows:** the USC admit (deferral), CSULA as the baseline row, and his NTT email (already done; apply the same pattern elsewhere).
10. **UX cleanup:** render the methodology as HTML, collapse long quotes behind a one-line summary, add a compact table view, put filters in the URL, and show theory-professor counts first.

## Fixes applied (2026-11-06, evening)

**Data (schools.json: now 59 schools, 136 professors)**
- **Stanford:** added Mark Zhandry (Assoc. Prof. since Sep 2025; 36 theory-venue papers 2021-25) and Emma Dauterman (applied; below threshold).
- **UIC:** added Daniel J. Bernstein (Research Professor; 3 + 1 papers) and Anrin Chakraborti.
- **New row, University of Chicago (region Chicago):**
  - David Cash and Aloni Cohen. Both are below the method's paper threshold, which explains why CSrankings dropped them.
  - Pre-Doctoral MS: $90 fee, GRE optional, 2025-26 tuition $85,592.
  - Caveat: the 2026-27 list of faculty reviewing Pre-Doctoral applications did not include Cash or Cohen.
- **New row, Cornell Tech (region NYC):**
  - Pass (also listed at Tel Aviv), Juels, and Ristenpart (on leave at Toronto since Jan 2026 and not taking students).
  - M.Eng CS: Dec 1 priority, Jan 26 round 2, Apr 1 rolling deadline; $73,946; no thesis, flagged honestly.
- **UW:** Tessaro and Lin homepage links now point to UW.
- **Penn:** Tal Rabin re-checked. She is still absent from the Penn CIS directory, so she was not added.
- **UC costs:**
  - Added `total_tuition_resident_usd`: $30,132 at all six UCs (2026-27 UCOP tuition + SSF, 2 years; tuition alone $27,444). The site shows this first, with out-of-state in small text.
  - All six non-resident totals are now on one basis ($60,336). This fixes the UCR 4-quarter error and the SSF inconsistency.
  - No MS CS program is on the UCOP PDST list.
- **`net_cost_note`:** Cornell (TA-funded), Yale 2-year (tuition fellowship), Princeton (funded but closed for Fall 2027).
- **`phd_direct`:** added for MIT (Dec 1), Princeton (Dec 15), Harvard (Dec 15), Berkeley (Dec 1), CMU (Nov 18 early / Dec 9), Cornell and Cornell Tech (Dec 15), Stanford (Dec 8), Wisconsin (Dec 15; MS continues to PhD without reapplying), UW (Dec 15), UT Austin (Dec 15), Columbia (Dec 15) and NYU (Dec 12).
- **`deadline_iso` / `priority_iso`:** added to every school with a concrete date. Priority and final dates are kept separate.
- **USC:** `his_note` records the unused Fall 2026 admit and the deferral policy (viterbigradadmission.usc.edu/faq).

**Data (internships.json, 76 rows)**
- **NTT CIS:** moved to Industry research labs.
- **a16z:** moved to Industry research labs, rated Hard, and dropped from top pick #1 to #6.
- **New top picks:** LANL CSRP, LLNL, CISPA, EF, IDA SCAMP-La Jolla, a16z.
- **NSA GMP, CASASP and SoS:** re-sourced to IC jobs 1261493, 1261551 and 1261519. All closed on Sep 5, 2026; 880807100 is the umbrella posting.
- **Arizona Winter School:** Nov 24, 2026 deadline added; flagged as a March school.
- **New fields:** `deadline_iso`, `priority_iso`, `opens_iso`, `deadline_kind`, `status` and `location_bucket`.

**New file: routes.json** ("Other routes" tab)
- **Your situation box:** CSULA M.S. Math as the baseline, with resident fees and the thesis/exam options; the USC admit and deferral rules.
- **Summer RA:** Wei-Kai Lin first, plus how to approach a professor.
- **Math-department routes:** Stange (Boulder), Gao (Clemson), Smith-Tone (Louisville), Eisentraeger (Penn State, PhD only).
- **NSF GRFP:** the NSF 26-526 deadlines (Oct 20 CISE / Oct 23 Math) have passed, and the second-year rule probably makes him ineligible next cycle.

**UI (index.html)**
- **Tabs:** new "Apply-by timeline" tab with days left computed in the browser, priority/final labels and past dates greyed. New "Other routes" tab.
- **Filters:**
  - All filters are multi-select (none ticked = all).
  - "Can I apply?" defaults to MS-eligible yes/unclear and not closed.
  - Internships get a location filter and a deadline sort.
- **Table views:** compact table view on both the MS and Internships tabs, sortable by header, with click-to-expand rows. The table scrolls inside its own box.
- **Other:**
  - Methodology Markdown is rendered as HTML.
  - Long text collapses behind "more".
  - Filters, tab, view and table sort live in the URL hash.
  - Theory-venue professor counts are shown first.
- **Checked in headless Edge** at 1280px and 390px: no horizontal page scroll.

**Could not verify (left null or noted)**
- **UChicago:** the Pre-Doctoral MS Fall 2027 deadline (site down; search index says Mar 1, 2027), its 2026-27 tuition, and the CS PhD Fall 2027 deadline (search index says Dec 10, 2026).
- **UNC:** the CS PhD deadline (site blocked).
- **dblp pids:** for the new faculty, taken from search results and confirmed by name through dblp SPARQL.
- **IDA CCS (Bowie) SCAMP 2027:** no posting found.
- **Not checked:** KU Leuven COSIC, Duality, IOG and DeepMind Student Researcher.
- **Professor details:** Wei-Kai Lin's title comes from his homepage, because the UVA page was blocked. Shuhong Gao's current rank is unverified.
- **CSULA M.S. Math:** official unit count not confirmed.
- **PhD fees** for Princeton, Harvard, Berkeley, CMU and Stanford come from search snippets only. They are not shown as fields.
