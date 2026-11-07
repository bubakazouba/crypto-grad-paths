# Summer 2027 crypto / security research internships: method

**Date retrieved:** 2026-11-06. **File:** `internships.json` (76 programs, list of objects).

## Scope
Summer 2027 research internships and summer research programs in cryptography and nearby areas: security and privacy research, post-quantum, quantum crypto, ZK and FHE, and blockchain cryptography research. Covered in five groups (`category` field):
- Big tech
- Industry research labs
- Blockchain / web3 research
- Government / national labs
- Academic summer programs and schools

Schools and fellowships that aren't internships are kept but marked in `focus_area` / `notes`. Undergrad-only programs (NIST SURF, NSA DSP, DIMACS REU, CMU SPUR) are listed so it's on record that they were checked and are not open to him.

## Sourcing rules
- Every factual field has a `*_source` URL or appears in `sources`. Anything that couldn't be verified is `null`, with the reason in `notes`.
- Eligibility, publication and letter requirements are quoted verbatim from postings where possible. "not stated" means the posting doesn't mention it.
- Official pages and ATS boards (Greenhouse, Lever, Workday, SmartRecruiters, USAJobs, MathJobs) come first. Job-board aggregators (builtin, web3.career and similar) and search snippets are used only when the official page was gone, and are flagged as secondary in `notes`.
- **Spot-checked by hand on 2026-11-06:**
  - **a16z Frontier:** deadline Nov 20 2026 12pm PT; Masters $4,000/wk + $500/wk housing; 1 letter required. Confirmed on the Greenhouse API.
  - **CISPA CSR 2027:** deadline Nov 30 2026 AoE; open to Bachelor's and Master's students; not open to PhD students. Confirmed on career.cispa.de.

## How fields were judged
- **prestige_tier** (my judgment):
  - Top: a recognized leading crypto/security research group, or a highly selective program (regulars at CRYPTO, EUROCRYPT or IEEE S&P, or a national-level program).
  - Strong: a respected research org with a real crypto or security output.
  - Good: solid, but more applied or less known for research.
- **difficulty_for_sahmoud** (my judgment, for his profile: 1st-year M.S. Math at CSULA, BS CS 2017, about 9 years at Amazon/Google/AWS-quantum, no crypto-venue publications, US citizen):
  - Very hard: PhD-only and publications expected.
  - Hard: PhD-preferred or highly selective.
  - Moderate: MS explicitly eligible and his engineering background helps.
  - Reachable: MS or early-grad eligible, low publication bar, direct fit.
- **NTT Research CIS:** includes the Nov 2026 email to him: "typically only take on summer interns who are full-time PhD students and who have already published at the top cryptography conferences like CRYPTO/EUROCRYPT", with exceptions decided by individual researchers. Rated Very hard.

## Caveats
- Many Summer 2027 postings aren't live yet. In that case `deadline_summer_2027` is null and `deadline_last_year_or_typical_window` holds the 2026 cycle's data.
- Some programs had no current posting at all, only older ones: MSR Cryptography, AWS Crypto, Meta crypto/privacy PhD, IBM Zurich crypto, Zama, Visa, Mysten, Aptos, Matter Labs and Algorand. These may not run in 2027.
- **Not found / no entry:**
  - No verifiable intern program for Aleo, Succinct, StarkWare, Coinbase (no crypto research intern among 285 postings), Espresso, Offchain, Nillion, Ingonyama, Fabric, Polygon, Protocol Labs, Ripple, Galois or Thales.
  - No program called "AlgoCRYPT" found at JPMorgan. Its crypto research internships appear as the AI Research Associate (MPC/crypto track) and the GTAR quantum-crypto summer associate instead.
  - No Simons Institute crypto program and no IACR school listed for summer 2027.
- **Already closed for 2027:** NSA GMP (IC job 1261493), CASASP (1261551) and SoS (1261519), all Aug 15 - Sep 5 2026 (re-sourced 2026-11-06; USAJobs 880807100 is the umbrella posting), and the Max Planck internship including MPI-SP (Nov 1 2026). These are 2028 targets.
- **Deadlines that are close as of retrieval:**
  - IDA CCR-La Jolla SCAMP: Nov 14 2026
  - a16z Frontier: Nov 20 2026
  - Summer@EPFL: Nov 29 2026
  - CISPA: Nov 30 2026
  - SMART: Dec 4 2026
  - ETH SSRF: Dec 16 2026
  - NTT CIS: "December 20", year not printed
- **Eligibility gaps for a Math M.S.:** CISPA and EPFL list CS/CE/EE degrees, so a math master's is unclear. CISPA also requires "at least four semesters completed" (his BS should count, but this isn't confirmed). The LANL CSRP needs a 3.2 graduate GPA.
- **Lower-quality sources:** some pages load only with JavaScript and were read through public JSON APIs. Headless Edge was used briefly by some research agents before the stop request; Chrome was never used. A few rows rely on aggregators or search snippets: Chainlink pay, EF pay, the Intel and JPMorgan quantum-crypto rows, Aerospace, INL and Lincoln Lab pay.
- Pay is copied as posted (weekly, monthly or annualized). Nothing was converted or estimated.
- No one was contacted, nothing was applied to, and nothing was logged into.

## Changes after the independent review (2026-11-06)
- **New fields:**
  - `deadline_iso`, `priority_iso` and `opens_iso` hold ISO dates where a concrete date exists.
  - `deadline_kind` is one of final, posting end or opens.
  - `status` is one of open, rolling, not yet posted or closed.
  - `location_bucket` holds one or more of NYC, Chicago, Bay Area, SoCal, Remote, International or Other.
  - The site also treats a row as closed once its final date has passed.
- **NTT Research CIS:** category changed from Big tech to Industry research labs.
- **a16z Frontier:** category changed to Industry research labs (the lab is now multidisciplinary), difficulty raised from Moderate to Hard, and moved from top pick #1 to #6.
- **New top-pick order:**
  1. LANL CSRP
  2. LLNL CSI
  3. CISPA
  4. Ethereum Foundation
  5. IDA SCAMP La Jolla
  6. a16z
- **Arizona Winter School 2027:** the student deadline (Nov 24, 2026) was added. The school runs March 6-10, 2027, so it is a winter school, not a summer program.
- **Not added (unverified):**
  - IDA CCS (Bowie) SCAMP 2027: no official posting found.
  - KU Leuven COSIC, Duality, IOG and Google DeepMind Student Researcher: not checked in this pass.
