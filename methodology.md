# US master's programs leading into cryptography research: methodology

Retrieval date: 2026-11-06. Dataset: `schools.json` in this folder. It has 59 schools and 136 professors (57 schools and 127 professors from the original pass, plus the corrections from the 2026-11-06 independent review; see section 6).

## 1. Professor and school selection

**Who counts.** A person counts if CSrankings lists them as faculty at a US institution (`institutions.csv`, countryabbrv = `us`) and they meet either test below for 2021-2025:
- **Core test:** at least 2 papers at CRYPTO, EUROCRYPT, ASIACRYPT, TCC, PKC or the Journal of Cryptology.
- **Security-venue test:** at least 3 crypto-themed papers at ACM CCS, USENIX Security or IEEE S&P. "Crypto-themed" means the title matches a keyword regex: encryption, zero-knowledge, SNARK, MPC, secret sharing, signatures, lattice/LWE, obfuscation, PIR, ORAM/OT, homomorphic, commitment, proof system, post-quantum, isogeny, key exchange, garbling, FSS/DPF, PSI, PRF, cryptanalysis, and so on.
  - A negative filter drops security papers that only use "obfuscation" or "encrypt" in a non-crypto sense: malware, executables, Let's Encrypt, face-recognition obfuscation, MBA/virtualization obfuscation, patch hiding.
  - The full regex is in `scripts/profs.py` (copied into this folder).

**Data sources**
- **Papers:** dblp SPARQL endpoint (`https://sparql.dblp.org/sparql`), streams `conf/{crypto,eurocrypt,asiacrypt,tcc,pkc,ccs,uss,sp}` and `journals/joc`. CCS, USENIX and S&P are limited to the main proceedings, with workshops excluded. The dblp website and API return an Anubis anti-bot block (HTTP 202), so SPARQL was the only route.
- **Edition year:** taken from the dblp record key (for example `conf/asiacrypt/...24`), not from the publication year.
  - dblp records ASIACRYPT and TCC 2024 with publication year 2025, and their 2025 editions with 2026. An earlier pass that used publication year silently dropped ASIACRYPT 2024 and TCC 2024. That is fixed.
  - Journal of Cryptology uses the publication year.
- **Faculty and affiliations:** CSrankings CSVs from GitHub `emeryberger/CSrankings` (gh-pages): `csrankings-*.csv`, `institutions.csv` and `dblp-aliases.csv`.
- **Name matching:** an exact dblp name or a CSrankings alias. Failing that, names match when the tokens are identical after dropping middle initials (for example "Brent Waters" matches "Brent R. Waters"). A name with a dblp numeric suffix is never matched this way.

**Fields in `schools.json`**
- `papers` is core plus security-venue papers.
- Each entry also carries `papers_core_iacr_joc` and `papers_crypto_themed_ccs_uss_sp`.
- A journal version of a conference paper counts as a separate paper.

**Topic tags.** These are the 1-3 most frequent tags from a title-keyword map: MPC, ZK/SNARKs, FHE/HE, lattices/PQ, iO, ABE/FE, signatures, PIR/ORAM, quantum, symmetric/hash, foundations, consensus, protocols, applied/systems, threshold, anonymity. They are a rough guide only, because they come from titles alone.

**Manual additions.** Two people are not in CSrankings and were added after checking official pages:
- **Susan Hohenberger-Waters (JHU):** Research Professor, https://www.cs.jhu.edu/faculty/susan-hohenberger-waters/
- **James Bartusek (Columbia):** Assistant Professor, https://www.cs.columbia.edu/people/faculty/

**Checked but not added**
- **Tal Rabin:** not on the current Penn CIS faculty or SEAS directory pages, so Penn is unconfirmed.
- **Vipul Goyal:** CMU lists him only as Adjunct Faculty (https://csd.cmu.edu/people/faculty/vipul-goyal).

## 2. Programs

Seven parallel research passes collected program data from official university pages only. Third-party sites were used as leads, never as sources.

**Which program was picked.** For each school, the best route into crypto research: a CS (or ECE) MS with a thesis or research option. Other options are in `alt_programs`.

**Tuition**
- Tuition only, using the published 2026-27 rate. Fall 2027 entrants will likely pay somewhat higher 2027-28 rates.
- `total_tuition_usd` is the out-of-state rate for public schools. For the six UCs, `total_tuition_resident_usd` adds the California-resident total ($30,132 = tuition + Student Services Fee over 2 years at 2026-27 UCOP rates), which the site shows first because Sahmoud is a CA resident.
- `net_cost_note` marks programs that fund MS students (Cornell, Yale 2-year, Princeton).
- `tuition_basis` gives the arithmetic (per-credit x credits, or per-term x terms) and the term-count assumption.
- Totals are estimates and depend on how long he takes.

**Deadlines**
- `deadline_fall2027` is the earliest stated (often priority or funding) deadline. Later and final deadlines are in `deadline_note`.
- 33 of the 54 dated programs show the date with no year on the official page. The Fall 2027 year was assigned by us, and `deadline_note` says so for each.

## 3. Coverage

| Field | Filled | Null, and why |
|---|---|---|
| Deadline | 54 of 57 | MIT and Harvard have no standalone CS master's for outside applicants. Princeton is not taking M.S.E. applications for Fall 2027. |
| Tuition total | 55 of 57 | MIT and Harvard, for the same reason. Harvard's closest option, the CSE M.E. ($101,256), is in `alt_programs`. |
| Program length | 42 of 57 | The other 15 schools only give credit counts. |
| Application fee | 52 of 57 | 5 schools state no amount on any official page. |

53 programs have a thesis or research option.

## 4. Caveats

- **CSrankings coverage.** CSrankings misses some active cryptographers and can lag behind faculty moves. Henry Corrigan-Gibbs is listed at Berkeley; his homepage confirms "associate professor in the EECS Department at UC Berkeley".
- **Who is excluded.** Industry-lab researchers (NTT Research, Google, AWS, Visa and similar) and postdocs are excluded, even when they are prolific.
- **Math departments.** Math-department number theorists and cryptographers were not added (optional; no reliable bulk source).
- **Security-venue-only entries.** Some people qualify only through crypto-themed security-venue papers. They are applied or systems crypto, not theory: Ning Luo, Ruzica Piskac, Fraser Brown, Wenting Zheng, Raluca Popa, Thang Hoang, Mengyuan Li (side channels on crypto implementations), Jonathan Mayer, Evgenios Kornaropoulos, Saba Eskandarian, Ian Miers and Sebastian Angel. For a theoretical-crypto goal, weight the core-venue count.
- **Eligibility flags**
  - Berkeley's EECS M.S. and UCLA's MS CS won't consider applicants who already hold a master's in a "closely related" or "similar" field. Whether a Math MS counts is unconfirmed.
  - Cornell's MS strongly prefers its own undergrads with grader or TA experience.
  - Columbia's MS thesis track is by faculty invitation.
  - CMU and Cornell say their MS is not a path into their PhD.
  - UNC tells PhD-bound applicants to apply to the PhD directly.
- **California residency.** Fixed 2026-11-06: UC rows now carry resident totals, and all six UC non-resident totals use the same basis (tuition + SSF + NRST, 2 years = $60,336).
- **Funded MS programs.** Cornell (TA plus stipend) and Yale (tuition fellowship for TA work) fund their MS students, so the listed tuition overstates the real cost.

## 5. Spot-checks

**Professors.** Each check compares our dblp-derived count with the professor's own homepage.

| # | Professor | Our count | Homepage | Result |
|---|---|---|---|---|
| 1 | Mike Rosulek, Oregon State | 9 core | 9 at the same venues and years (https://garbledcircus.com/) | Exact match. Affiliation confirmed. |
| 2 | Chris Peikert, Michigan | 5 core | 4 (https://web.eecs.umich.edu/~cpeikert/) | The extra paper is a JoC 2024 journal version that the homepage doesn't list separately. Affiliation confirmed. |
| 3 | Henry Corrigan-Gibbs, Berkeley | 5 core | 5 matching titles (https://people.eecs.berkeley.edu/~henrycg/pubs/) | Match. Berkeley affiliation confirmed. |
| 4 | David J. Wu, UT Austin | 31 core | (https://www.cs.utexas.edu/~dwu4/publications.html) | Every venue-year count matches the portion read: TCC 2024 = 4, CRYPTO 2025 = 3, EUROCRYPT 2023 = 2, and so on. The last 46k characters of the page, which cover JoC 2021, were not read. |
| 5 | Saba Eskandarian, UNC | 3 security-venue | (https://www.cs.unc.edu/~saba) | The homepage lists those 3 plus IEEE S&P 2023 "DBREACH" (compression side channels), which the crypto keyword filter correctly left out. Affiliation confirmed. |

**Tuition.** Each rate was re-read from the official source.

| # | School | Rate used | Official source | Result |
|---|---|---|---|---|
| 1 | CMU SCS master's | $31,100 per semester | $31,100 per semester; $62,200 per year (cmu.edu/sfs) | Match |
| 2 | UCSD | $4,574 tuition + $5,034 NRST per quarter | Same (students.ucsd.edu 2026-27 graduate fees) | Match |
| 3 | Georgia Tech | $1,341 per hour; $16,073 flat at 12+ hours | "Master & PhD Candidates ... $1,341 /hr $16,073" (bursar fa26 PDF) | Match |
| 4 | George Mason | $1,571 per credit, out-of-state | "All CEC programs ... $730.00 $1,571.00 $169.00" (AY26-27 PDF) | Match |
| 5 | Maryland | $1,916 per credit, non-resident | "$1,916.00 per credit hour" (billpay.umd.edu) | Match |

Oregon State's $12,015 per term appears in the official table, but the column header could not be cleanly attributed from text extraction, so it was not counted as a check.

## 6. Corrections after the independent review (2026-11-06)

- **Faculty added by hand** (counts from the same dblp SPARQL query, venues and years as above):
  - Stanford: Mark Zhandry (36 theory-venue papers) and Emma Dauterman (applied; below threshold).
  - UIC: Daniel J. Bernstein (3 + 1) and Anrin Chakraborti (below threshold).
  - New row, University of Chicago: David Cash and Aloni Cohen. Both are below the paper threshold, which is why the CSrankings pass missed them.
  - New row, Cornell Tech (NYC): Rafael Pass, Ari Juels and Thomas Ristenpart. Ristenpart is on leave at Toronto from January 2026.
- **Links fixed:** the UW homepage links for Tessaro and Lin now point to UW.
- **Structured dates:** `program.deadline_iso` (final) and `program.priority_iso` (early, priority or round 1) were added alongside the original `deadline_fall2027` (earliest stated).
- **PhD-direct:** a `phd_direct` object {deadline, deadline_iso, url, note} was added where applying straight to the PhD is the real route. That covers MIT, Princeton, Harvard, Berkeley, CMU, Cornell, Cornell Tech, Stanford, Wisconsin, UW, UT Austin, Columbia and NYU. The UNC and UChicago PhD dates were not verified.
- **Your admit:** `his_note` on USC records the unused admit and the deferral policy.
