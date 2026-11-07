# Crypto Grad Paths: second independent review (2026-11-06)

**Scope**
- **Site:** the live site (https://bubakazouba.github.io/crypto-grad-paths/), byte-identical to local `index.html`.
- **Data:** `schools.json` (59 schools), `internships.json` (76 programs), `routes.json`, and both method files.
- **Facts:** checked against official pages (department, registrar and bursar pages, ATS postings).
- **UX:** headless Edge (Playwright, `channel='msedge'`) at 1280px and 390px, light and dark. Screenshots are in `review2_shots/`, and the scripted run log is `review2_shots/_ux_log.txt`.
- I formed my own view first and read `REVIEW.md` only at the end.

**Verdict**
- **Logistics:** dates, tuition and UC resident math are now mostly right.
  - All 10 school deadline sets were checked and every date matched.
  - The UC resident total of $30,132 checks out at UCSD and Berkeley.
  - All 8 internship deadlines checked out.
- **Remaining problems:**
  - Faculty quality, meaning who actually is a cryptographer.
  - Eligibility conditions that matter to him.
  - Rankings that reward reachability over value to a theory-crypto PhD application.
  - The site still answers "where can I do an MS" better than "where do I apply for a PhD in Dec 2026, and what should I do this summer to get in".

---

## 1. Errors (content accuracy)

**Schools spot-checked**
- **Deadlines, tuition, thesis option, fee and PhD date:** UCSD, Berkeley, Northwestern, UIC, Stony Brook, Oregon State, UMass Amherst, Purdue, Georgetown, Columbia, plus Cornell Tech, NYU PhD and UChicago.
- **Faculty, 24 people at:** Berkeley, Stanford, NYU, Cornell, Rutgers, Delaware, UVA, UIC, UW, Princeton, UCR, USC, Cornell Tech and MIT.

**Internships spot-checked:** LANL CSRP, LLNL CSI, IDA SCAMP La Jolla, CISPA, ETH SSRF, Weizmann Kupcinet-Getz, DoD SMART, PCMI, Google Student Researcher, plus Ethereum Foundation, Cloudflare and SLMath.

**Timeline vs data:** the Apply-by timeline is generated from the same `*_iso` fields, so its 97 default rows match the data by construction. I dumped all rows to `review2_shots/_tl_rows_d.json` and compared them. The only mismatch is the hand-written "Key dates in the next 6 weeks" text in `routes.json` (row 15).

| # | Item | Field | Site value | Correct value | Source |
|---|---|---|---|---|---|
| 1 | UMass Amherst | `program.thesis` | yes (green "thesis/research option" chip; also passes the Thesis=yes filter) | **No.** "The Master's in Computer Science degree is a non-thesis degree"; there is only a 6-credit Master's Project | https://www.cics.umass.edu/academics/ms-computer-science-campus (MS degree requirements) |
| 2 | UC Riverside | professors | Amey Bhangale, "3 theory-venue papers", tags consensus/blockchain, ZK | Bhangale works on PCPs, hardness of approximation and Boolean analysis. He is not a cryptographer, and the blockchain/ZK tags suggest a dblp name mis-match. UCR effectively has **0** crypto faculty, so drop the row or mark it "adjacent". | https://theoryofcomputing.org/articles/v016a016/ (author bio) |
| 3 | USC (his admitted program) | professors | "2 crypto professors" | Mengyuan Li works on systems/TEE security (side channels), not crypto. Jiapeng Zhang is a theory professor who is crypto-adjacent (he teaches SNARKs and lattices). No core USC cryptographer was found, and Muhammad Naveed's directory page returns 404. This matters because the USC deferral is a live decision. | https://viterbi.usc.edu/directory/faculty/Li/Mengyuan ; https://viterbi.usc.edu/directory/faculty/Zhang/Jiapeng |
| 4 | NYU | professors | 6; no Oded Regev | **Oded Regev** (LWE, lattices) is NYU Courant faculty and is missing. Tony Metger (quantum crypto) starts as an Assistant Professor in Sep 2026. Joseph Bonneau is not on the NYU theory-group page; his status was not verified. | https://cs.nyu.edu/theory-group/ |
| 5 | MIT | professors | Vaikuntanathan, Kalai | Rivest and Micali (and Devadas for security) are missing. Check whether they take students before adding them. | https://toc.csail.mit.edu/cis |
| 6 | Oregon State | `app_fee_usd` | null (not shown) | **$85** | https://graduate.oregonstate.edu (admissions/fees) |
| 7 | Columbia | program name | "MS Thesis pathway (by faculty invite only)" | Not invite-only. You find a CS faculty advisor yourself, then elect the thesis. Methodology §4 repeats the "by faculty invitation" claim. | https://www.cs.columbia.edu/education/ms/MSThesis/ |
| 8 | Texas A&M | `total_tuition_usd` | $25,092 (ranked the cheapest unfunded MS) | Excludes the Engineering Program Fee of $2,565 per semester at 9+ hours. The realistic figure is **about $32.8k**, which is above the UC-resident $30,132. This was flagged in REVIEW.md and not fixed. | the row's own `tuition_basis`; https://tuition.tamu.edu |
| 9 | Princeton | cost display / sort | "≈$0 (funded)"; #3 in "lowest tuition for me" | The M.S.E. takes no Fall 2027 applications, so it should drop out of the cost sort and the "Funded MS" filter. | the row's `net_cost_note` |
| 10 | DoD SMART | letters / eligibility / nature | letters "count not verified"; listed as an internship | **3 letters, 3.0 GPA** (kept for the whole award), and **one year of DoD service per year funded**. It is a scholarship-for-service, not an internship. | https://www.smartscholarship.org/smart (page blank to scripts); K-State SMART fact sheet |
| 11 | PCMI 2027 GSS | `ms_students_eligible` | unclear | Effectively **yes**: applicants "will have completed their first year of graduate school", which he will have done by June 2027 | https://www.ias.edu/pcmi |
| 12 | SLMath Summer Grad Schools | eligibility | needs nomination by a member institution | The Director of Graduate Studies of **any** US math department can nominate. Places are first-come from Dec 1, so the CSULA grad director must submit on Dec 1. | https://legacy.slmath.org/web/msri/education/for-graduate-students |
| 13 | ETH SSRF | eligibility | math OK; no graduation-year constraint shown | Also requires **graduation in 2028 or later**. This interacts with the CSULA MS end date and any Fall 2027 PhD start. | https://inf.ethz.ch/studies/summer-research-fellowship/how-to-apply.html |
| 14 | CISPA CSR | eligibility / difficulty | "yes", "Moderate", top pick #3 | The listed fields are CS, CE, EE and telecom "or equivalent". **Math is not listed**, so an MS Math applicant is at risk. Show this as a chip, not a note. | https://career.cispa.de/internship |
| 15 | `routes.json` "Key dates in next 6 weeks" | static text | lists 8 items | Omits DoD SMART (Dec 4), the CMU MS early deadline (Nov 18), Northwestern round 1 (Nov 30), UCSD/UCSB (Dec 16) and the SLMath opening (Dec 1). It is hand-written and will go stale; generate it from the data. | `index.html` timeline |
| 16 | Cloudflare Research intern | `url` | builtin.com copy of the 2026 posting | Stale; no 2027 posting exists. Point to Greenhouse. | https://job-boards.greenhouse.io/cloudflare |
| 17 | Arizona Winter School / SMART / SLMath | timeline type | "Internship" | A March winter school, a scholarship and a 2-week school. Add a "School/workshop" and a "Scholarship" type. | `index.html` `events()` |

**Count:** 17 errors.
- **Factual:** rows 1-8, 10-14 and 16.
- **Display or labelling:** rows 9, 15 and 17.

**Confirmed correct**
- **School deadlines:**
  - UCSD Dec 16, 2026; UCSD tuition $4,574 + SSF $448 per quarter = $30,132 resident.
  - Berkeley Dec 1, 2026 at 8:59pm PST, MS and PhD; ($6,861 + $672) x 4 = $30,132.
  - Northwestern rounds: Nov 30 / Dec 31 / Feb 28 / Jun 15.
  - UIC: Jan 15 recommended, Feb 15 final. UIC tuition of $49,611 is unverifiable (rates are in a Box file).
  - Stony Brook Mar 15, 2027 at $1,158 per credit.
  - Oregon State Jan 5, 2027 at $12,015 x 5.
  - UMass Dec 15 / Mar 15 and $59,355.
  - Purdue Dec 1 and $44,466.
  - Georgetown Jan 15 / Apr 1 and $82,740.
  - Columbia Jan 15 / Feb 15, PhD Dec 15, $84,660.
  - Cornell Tech Dec 1 / Jan 26 / Apr 1 and $73,946.
  - NYU PhD Dec 12.
- **Faculty confirmed:** Corrigan-Gibbs (Berkeley), Goldwasser, Zhandry (Stanford), Dauterman, the NYU group, Golovnev (Cornell, 2026), Spooner, Goel (Rutgers), Mingyuan Wang (Delaware), Doerner and Lin (UVA), Block (UIC), Tyagi (UW), Lombardi (Princeton).
- **Internships confirmed:** LANL Feb 1 rolling, LLNL CSI $10,215/mo, IDA SCAMP Nov 14 (the real deadline), CISPA Nov 30, ETH Dec 16 at 13:00 CET, Weizmann Dec 20 to Jan 20, PCMI Jan 15, Google Student Researcher Jul 16, 2027.

---

## 2. UX bugs (severity-ranked)

Load performance is fine.
- Five fetches total about 118 KB transferred.
- First render takes 0.7 s warm and 1.2 s cold.
- There is no horizontal page scroll at 390px.
- The only console error is a `favicon.ico` 404.

### High
1. **Table view cannot be used from the keyboard.**
   - `<th>` and `<tr class="it">` are plain elements with click handlers, with no tabindex, role or key handler.
   - In the Tab-order trace, focus goes from the "Table" toggle to the scroll `DIV` and then to `BODY`.
   - So you can't sort a column or expand a row without a mouse.
2. **Dark-mode contrast fails on the most important controls.**
   - The active tab, the active Cards/Table toggle, the "Already admitted" chip and the active filter pills use white on `#7b9bff`, which is about **2.6:1** (AA needs 4.5).
   - See `d_dark_tl.png` and `d_dark_ms_table.png`.
3. **Filter menus never close, and they reflow the layout.**
   - The `<details>` menus have no outside-click or Esc close. Several can be open at once.
   - An open menu stretches its own summary box: "Region: all" grows to about 560px wide and pushes Route/Sort onto a second row (`d_light_ms_table.png`).
   - On mobile in the Internships tab, the open menus push the results off the first two screens (`m_light_in_table_expanded.png`).
4. **No error handling on data load.** `Promise.all(...)` has no `.catch`. If any one of the five files fails or has a JSON typo, the page renders an empty shell with no message.
5. **The "Lowest tuition for me" sort is misleading.**
   - The first rows are Yale, Cornell and Princeton at ≈$0.
   - Princeton is closed for Fall 2027.
   - Cornell and Yale's funded tracks are tiny and highly selective.
   - TAMU is understated (error 8).
   - CSULA (his baseline, about $19k for 2 years) and the USC admit are not rows at all, so the sort never shows "vs staying put".

### Medium
6. **Light-mode chip contrast fails AA at 12px.** Green chips (`#1f8a4c` on a 15% green tint) are about 3.7:1 and orange chips (`#b26a00`) about 3.5:1. Past timeline rows (`opacity:.7` on muted grey) are lower still.
7. **Search runs over `JSON.stringify(row)`, URLs included.**
   - "edu" matches 59 of 59 schools, and "yes" or "source" match nearly everything.
   - His own topics return nothing: "memory checking" 0, "lower bound" 0, "garbl" 0.
   - "ORAM" returns 17 schools only because of the coarse `PIR/ORAM` title tag.
8. **Two sort controls disagree in table view.** A clicked column header silently overrides the "Sort:" dropdown, which keeps showing its own choice (for example "Sort: next upcoming deadline" while the table is sorted by PhD deadline).
9. **Table sort arrows are inverted for numeric columns.** The first click shows ▲ but sorts descending, because the keys are negated. In descending tuition order, the null-cost rows (MIT, Harvard) jump to the top.
10. **No sticky table header.** With 59 rows, you lose the column names after the first screen.
11. **The timeline is a wall.**
    - It shows 97 dates by default, mostly MS finals running to Sep 2027.
    - There is no "my shortlist" filter.
    - Winter school, scholarship and "Opens" rows are typed "Internship".
    - The chip colours read backwards: Priority is green and Final is orange, but the priority date is usually the one he must hit.
12. **"Only ones I can apply to" barely filters.**
    - It drops only 3 rows (`ms_students_eligible=='no'`).
    - It ignores GPA, field, graduation-year and citizenship flags.
    - It keeps USC's new-applicant deadlines, though his action there is a deferral request, which has no timeline row.
13. **Mobile: about 520px of chrome before the first result.** That is a 6-line subtitle, 5 wrapped tab pills and 4 rows of controls (`m_light_ms_cards.png`).

### Low
14. **Tab and filter changes use `history.replaceState`,** so the browser Back button leaves the site instead of undoing a filter.
15. **Missing ARIA.**
    - There are no `role=tablist`/`aria-selected` attributes on the tabs.
    - The sort `<select>` has no label.
    - The search boxes have placeholder text only.
16. **`statusOf()` latent bug.** It marks a row "closed" when its priority date has passed and it has no final date, which is wrong for priority-only rows such as ASU, Oregon State, GWU and WSU if reused.
17. **UChicago's Pre-Doctoral MS shows a warning chip, "no thesis option".** It is a research-advisor track built for PhD prep, so the chip mislabels it.
18. **`favicon.ico` returns 404.**

**Count:** 18 UX bugs (5 high, 8 medium, 5 low).

**Works well**
- Multi-select combinations, for example NYC+Chicago+Bay Area with PhD-direct gives 6 schools.
- The per-menu "all" clear works.
- The URL hash persists region, route, view, table column and tab across reloads.
- Row expand works.
- "Show past" works.
- The Methodology Markdown renders properly.
- There is no horizontal scroll on mobile.

---

## 3. Information gaps and noise

### Decision-critical and missing
- **PhD deadlines for all 59 schools.**
  - He is applying for a **Fall 2027 PhD**, and the real action set is the Dec 1-15, 2026 PhD wave.
  - Only 13 schools have `phd_direct`.
  - There are no PhD dates for UCSD, UCLA, UIUC, Purdue, Georgia Tech, UW-Madison's peers, Michigan, Maryland, BU, Northeastern, Penn and others, all of which run strong crypto PhD programs.
  - The MS deadlines are arguably the secondary list.
- **Research fit to his own work** (memory-checking lower bounds, ORAM, PIR, garbling, lower bounds generally).
  - Nothing ranks professors by overlap with his draft.
  - The natural US hosts are:
    - **ORAM / memory checking:** Wei-Kai Lin (UVA), Elaine Shi (CMU), Rafail Ostrovsky (UCLA, the ORAM originator, in LA), Ling Ren (UIUC).
    - **PIR:** Henry Corrigan-Gibbs (Berkeley).
    - **Garbling:** Mike Rosulek (Oregon State), David Heath (UIUC), Vlad Kolesnikov (Georgia Tech).
    - **Lower bounds / foundations:** Rafael Pass (Cornell Tech).
  - None of this is visible, and search for these terms returns 0 results.
- **Whether faculty are taking students,** and whether MS students publish with them. Paper counts measure productivity, not advising capacity or MS access. Examples: Ristenpart is on leave, and the UChicago pre-doc reviewer list excludes Cash and Cohen.
- **MS-to-PhD evidence per school.**
  - Does the MS feed the PhD? CMU and Cornell say no; Wisconsin and UIUC say yes.
  - How many MS students moved to the PhD?
  - Is RA funding for MS students realistic?
  - This lives in prose today; it should be one structured field with a chip.
- **Realistic cost.**
  - Tuition only, with no fees, health insurance or cost of living.
  - For his choice of NYC, Bay Area, Chicago or staying in Pasadena, rent differences (roughly $15-30k a year) outweigh most tuition gaps.
  - There are no CSULA or USC rows in the comparison.
- **Letters and materials.**
  - He has a known letter bottleneck, yet "letters needed" is free prose and the timeline has no letter-request lead dates.
  - Rule of thumb: ask 4 weeks before Dec 1, which means now.
- **Program size and acceptance rate,** where published, for example Berkeley's tiny MS-only intake and Cornell's MS.
- **USC deferral deadline.** The "within one year" request has no date on the timeline.
- **A personal layer.**
  - Missing: a star/shortlist, a notes field, a status per row (considering / applied / submitted letters), a compare view of 3-5 rows, and "export my shortlist".
  - Today he can only bookmark filter states.

### Misleading
- **"Top pick" order rewards reachability over value to his goal.**
  - The criteria behind the order are not shown on the page.
  - #1 is LANL Cyber Fire (a security research school) and #2 is LLNL CSI (cyber/critical infrastructure; "crypto listed as an exposure area").
  - For a theory-crypto PhD application, the payoff is a letter from a cryptographer. That favours IDA SCAMP, CISPA, ETH SSRF, a self-arranged RA with Wei-Kai Lin, and NTT through his existing thread.
- **"Prestige" is the author's own judgment** and is inflated for SLMath and PCMI, which are rated "Top" though they are short math schools, not crypto research.
- **"Reachable / Moderate" difficulty ignores hard gates:**
  - LANL needs a 3.2 *graduate* GPA (he has none until December).
  - Weizmann needs a 3.6.
  - ETH needs a graduation year of 2028 or later.
  - CISPA's field list leaves out math.
  - SMART has a service obligation.
- **The "theory-venue professor" count is inflated.** A threshold of 2 or more papers counts non-cryptographers (Bhangale) and adjacent people (Golovnev, Samson Zhou, Xiaodi Wu). Journal versions double-count.
- **The "Funded MS (≈$0)" filter includes Princeton,** which is closed for Fall 2027.

### Noise to demote
- Undergrad-only and PhD-only rows (NIST SURF, NSA DSP, DIMACS REU, CMU SPUR, Apple ML PhD) are already hidden by default, which is fine.
- Generic IT/security internships (DOE Omni, INL, Meta Product Security, Aerospace hardware security) add little toward a theory-crypto PhD. Tag them "applied/eng" and hide them by default.

---

## 4. Top 10 changes, ranked by value to him

1. **Make the PhD the primary object.** Add a PhD deadline, link and "MS feeds PhD?" field for every school, and a "PhD wave" view, because the Dec 1-15 deadlines are 25-39 days out.
2. **Add research fit to his interests.** Tag each professor for ORAM, memory checking, PIR, garbling and lower bounds, with a sort or filter on fit, and make search work on those terms. Surface Ostrovsky (UCLA, local), Shi, Lin, Ren, Heath, Rosulek, Corrigan-Gibbs and Pass.
3. **Add a shortlist, notes and status per row,** saved locally and in the hash, with "Shortlist only" on every tab including the timeline.
4. **Re-rank internship picks by PhD-application value** (a crypto-researcher letter). Put the self-arranged RA, IDA SCAMP, CISPA and ETH first. Show the hard-gate chips (GPA, field, graduation year, citizenship, service obligation). Demote LLNL CSI and LANL to "fallback".
5. **Fix the data errors in section 1:** UMass thesis, UCR/Bhangale, the USC faculty labels, add Regev, the TAMU fee, Princeton in the cost sort, SMART, PCMI, SLMath, the ETH and CISPA flags, the Oregon State fee and the Columbia wording.
6. **Show a "realistic cost to me"** column (tuition + fees + metro living cost), and add CSULA and USC as baseline rows in the table and cost sort.
7. **Add structured MS-to-PhD and funding evidence:** whether MS students publish, RA odds, internal PhD admits, and program size or acceptance rate, each with a source or "unknown".
8. **Fix accessibility:**
   - Make table headers and rows into buttons.
   - Fix the dark-accent and chip contrast.
   - Close filter menus on Esc or outside click.
   - Add a fetch error message.
9. **Timeline upgrades:**
   - Add the USC deferral date and letter-request lead dates.
   - Correct the event types.
   - Add a shortlist filter.
   - Generate the "Key dates" text from the data.
10. **Search and table polish:**
    - Search named text fields only.
    - Make the table header sticky.
    - Fix the sort arrows and the placement of null values.
    - Use one sort control.
    - Shorten the mobile header.

---

## 5. Still unresolved from REVIEW.md

- **TAMU tuition** still excludes the Engineering Program Fee (REVIEW.md #10). Mixed fee bases at UT Austin, FSU and VCU are still uncorrected.
- **Prestige** is still inflated for SLMath and PCMI. Schools and workshops are still mixed in with internships (same category, same timeline type).
- **CSULA baseline** is only prose in "Other routes"; it is not a comparable row in the cost sort or table.
- **Missing programs never checked:** IDA CCS Bowie SCAMP, KU Leuven COSIC, Galois (to reconcile with his CSV), Duality, IOG and DeepMind Student Researcher.
- **Math-MS eligibility risk chips** (CISPA, EPFL, LANL GPA, Weizmann GPA) are still notes only.
- **Letters** are still unstructured prose with no count.
- **Acceptance-odds band** has not been added.
- **Region values** are still uneven (metros mixed with regions; Ithaca and Princeton under "Northeast").
- **Unverified items:** the UChicago Fall 2027 MS and PhD deadlines, the UNC PhD deadline, and Penn / Tal Rabin.

---

## Fixes applied (round 2), 2026-11-06/07

**Top-10 changes**
1. **PhD-first.** Every school has a `phd` object (deadline, early/priority date, official URL, verbatim quote): **58 of 59** found; City College (CUNY Graduate Center) is null with a note because its site blocks scripts. The PhD deadline is the first line of every card, a sortable table column (default timeline type), and drives "Next deadline". UNC (Mar 9, 2027 final; Dec 15 fellowship) and UChicago (Dec 10, 2026, from a search-index copy because the site is in maintenance) are now filled.
2. **Research fit.** All 138 professors' 2021-2026 dblp titles (6,700+) were pulled from dblp SPARQL and tagged against a fixed vocabulary, with up to two evidence titles per tag (hover a tag). `fit_score` per school, a "Fit to my work" sort (default) and chip, and a "Professors closest to your work" list under Other routes: Wei-Kai Lin is #1 and Rafail Ostrovsky (UCLA) is #2. Search now matches tags ("memory checking" 3 schools, "garbl" 17, "ORAM" 26). 9 dblp records look mixed with a same-name author and are flagged on the card.
3. **Shortlist.** Status (Interested / Applying / Applied / Skip) and notes on every school and internship card and table row, saved in `localStorage` inside try/catch (page renders and works with storage blocked; it says notes won't be saved). "My shortlist" filter on Schools, Internships and Timeline.
4. **Internship picks** re-ranked by letter value for a theory-crypto PhD app, then theory first, then reachability, skipping PhD-only, closed or blocked rows: 1 EF crypto research, 2 CISPA, 3 Weizmann, 4 ETH SSRF, 5 IBM Zurich, 6 a16z, 7-8 IDA SCAMP (CCR-L, CCR-P), 9 Chainlink, 10 LANL CSRP. Each pick shows "Why this rank". Hard gates checked on 49 rows (42 have at least one gate chip: blocks / risk / ok, each with quote + URL), e.g. ETH "Graduation 2028 or later", CISPA and EPFL "Math not listed", LANL GPA 3.2, Weizmann GPA 3.6, SMART one-for-one service commitment, SLMath nomination, NSA cycle closed.
5. **Data errors fixed:** #1 UMass non-thesis; #2 UCR Bhangale marked not-crypto (UCR fit 0); #3 USC: Zhang crypto-adjacent, Li systems/TEE, Naveed not in directory; #4 NYU adds Oded Regev and Tony Metger, Bonneau flagged; #5 MIT: Rivest/Micali advising status unverified, so noted, not added; #6 Oregon State $85; #7 Columbia thesis not invite-only; #8 TAMU now $33,642 incl. Engineering Program Fee; #9 Princeton "closed for Fall 2027", out of cost sort and funded filter; #10 SMART 2-3 references (official KB says at least two, not three), one-for-one DoW service, shown as scholarship-for-service; #11 PCMI MS-eligible = yes; #12 SLMath nomination wording; #13 ETH and #14 CISPA as chips; #15 key dates generated from data; #16 Cloudflare now points to Greenhouse (no 2027 research intern role); #17 timeline types School/workshop and Scholarship. SLMath and PCMI prestige lowered to Good.
6. **Realistic cost:** official cost-of-attendance budgets for 57 of 59 schools plus CSULA (living, fees, insurance; Drexel and Rice have no usable graduate budget). "Realistic total" column/sort = tuition for you + years x (living + fees + insurance). CSULA (current, baseline) row added; USC was already a row.
7. **MS-to-PhD evidence** (`ms_phd`: MS feeds PhD, MS research, RA/TA for MS, size/admit rate), each with quote + URL: 67 fields across 41 schools; everything else is shown as unknown, not "no".
8. **Accessibility:** table headers are buttons with `aria-sort`; rows open from a name button (Enter/Space); dark-mode active controls use dark text on the light accent (8.3:1); chip colours re-tuned (all ≥4.8:1); filter menus are overlays that close on outside click and Escape (one open at a time); a visible error box if any data file fails or is malformed; tabs have `role=tablist`/`aria-selected`, arrow-key navigation, labelled search and sort; favicon 404 gone.
9. **Timeline:** USC deferral row (Jan 15, 2027: per the Viterbi FAQ, updated materials are due by the Fall deadline; no separate form date is printed); "Ask for letters" rows at deadline minus 4 weeks (grouped by date, individual rows for shortlisted schools); correct types; shortlist filter; "only ones I can apply to" also drops rows with a blocking gate and USC's new-applicant MS dates; key dates (next 6 weeks) generated from the same events.
10. **Search/table polish:** search covers named text fields only, tokenized, URLs and domains stripped, tokens of 3 letters or fewer must match a whole word ("edu" now 0); one sort model shared by cards, table and the dropdown (header clicks update the dropdown; arrows reflect the real direction; nulls always last); sticky table header; compact mobile header (one-line subtitle, short tab labels, filters folded into "Filters & sort"): first result at 240px at 390px wide. Tab changes push history so Back works.

**Verification:** headless Edge at 1280 and 390, light and dark, on the live site: all tabs, filters, table sort/expand by keyboard, shortlist persisting across reload, no horizontal scroll, no JS errors (see the commit's verification notes).

**Still unverified / open**
- City College PhD deadline; UChicago PhD date and NYU/Princeton COA came from search-index copies of official pages (blocked to scripts).
- Fit score is a coarse title count (one "lower bounds" title counts like a career); read the evidence titles.
- Letter value and prestige are judgments with linked evidence, not facts.
- Tal Rabin (Penn) and Rivest/Micali (MIT) not added; Bonneau's NYU status unverified.
- Some COA budgets are 12-month or 8-month, or on-campus only (Stanford, UCSB), or undated (UCR); each basis says so.
