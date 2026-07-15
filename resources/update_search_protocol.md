# Final Documented Google Scholar Update Search — Protocol and Logging Template

Purpose: provide the reproducible search record for Chapter 3 (§3.2) and the PRISMA flow diagram (Appendix A). These are **predefined strings for the update search**; they are not, and must not be presented as, the historical strings of the original exploratory search.

## 1. Predefined search strings (Google Scholar syntax)

Google Scholar supports quoted phrases, OR (uppercase), exclusion with `-`, and `intitle:`. It treats spaces as AND. Run each string exactly as written, record it verbatim in the log, and do not modify strings mid-search (a modified string is a new log row).

| # | Search string | Rationale |
|---|---|---|
| S1 | `"reshoring" OR "backshoring" barriers manufacturing` | Core barrier literature |
| S2 | `"reshoring" OR "backshoring" implementation manufacturing` | Implementation-stage studies |
| S3 | `"reshoring" OR "backshoring" China OR Asia manufacturing` | Asia-host-specific evidence |
| S4 | `"manufacturing reshoring" OR "manufacturing backshoring" "supplier" OR "capabilities" OR "skills"` | Capability/supplier barrier themes |
| S5 | `intitle:reshoring OR intitle:backshoring` | High-precision sweep of titles |

Five strings is deliberate: enough for coverage, few enough to screen honestly. Do not add strings ad hoc during the session; if a gap emerges, finish the protocol first and log any additional string as a clearly marked supplementary search.

## 2. Settings and screening rule

- **Publication-year range:** 2013–2026 (custom range in the left sidebar). Rationale: the manufacturing-reshoring research stream is effectively post-2013; earlier foundational work enters the thesis via citation searching and the approved theory sources, not via this update search. Record the range actually applied.
- **Sort order:** relevance (Google Scholar default). Do not sort by date.
- **Screening depth:** screen the **first 50 results per string** (5 pages). Stop-rule: you may stop a string early if 20 consecutive results are irrelevant — record the actual number screened either way.
- **Language/access rule:** apply the same manual checks as the original process — English language, full text accessible, peer-review status, publication type, manufacturing relevance — and record exclusions under the reason codes below.
- **Do not use** Google Scholar profiles, alerts, or "since year" quick links for the formal record; only the logged string runs count.

## 3. Exclusion reason codes (for the log and PRISMA)

R1 not manufacturing · R2 not genuine reshoring (China+1, re-offshoring, nearshoring without return, foreign-to-foreign) · R3 not English · R4 full text inaccessible · R5 not peer-reviewed (preprint/blog/report — note: may still be considered as contextual source, log separately) · R6 duplicate of corpus source · R7 duplicate across strings · R8 decision-stage only, no barrier/implementation content and no contextual value · R9 other (state).

## 4. Logging template (one row per string; fill during the session, not afterwards)

| Field | S1 | S2 | S3 | S4 | S5 |
|---|---|---|---|---|---|
| Search date (YYYY-MM-DD) | | | | | |
| Exact string as entered | | | | | |
| Year restriction applied | | | | | |
| Approx. results displayed (GS header) | | | | | |
| Records actually screened | | | | | |
| Duplicates (R6/R7) | | | | | |
| Full texts assessed | | | | | |
| Full texts excluded (n + reason codes) | | | | | |
| Newly included studies (n + short refs) | | | | | |

Also record once per session: browser/incognito status (recommended: logged-out incognito window, to reduce personalisation), and country/interface language.

## 5. PRISMA 2020 presentation (the defensible structure)

Use PRISMA 2020's **two-arm flow**, which exists precisely for this situation:

- **Arm 1 — "Identification of studies via databases and registers":** the documented update search only. All values come from the log above. Platform: Google Scholar (named as a search platform, not a curated database — keep the wording "literature-discovery platform").
- **Arm 2 — "Identification of studies via other methods":** the original exploratory Google Scholar searching, backward reference searching, forward citation ("Cited by") searching, and related-article suggestions. For this arm, report the stages that are genuinely reconstructable from the corpus record: sources assessed at full text (n = 33 retained in the corpus; additional assessed-but-rejected sources only if the author can enumerate them), assigned to the formal analytical sample (n = 21), retained as contextual/policy sources (n = 7), retained as methodology sources (n = 5). For "records identified" in this arm, state **"not recorded (exploratory phase)"** in a footnote rather than inserting any number.
- The two approved primary theory sources (Williamson, 1985; Barney, 1991) are **not** studies and appear in neither arm.
- Flow-diagram caption wording: "Records identified via the original exploratory search process (Arm 2) were not counted prospectively; the update search (Arm 1) provides the documented, reproducible search record."

## 6. Author checklist for the search session (Part E)

1. Open a logged-out incognito browser window; note the date.
2. Set the custom year range 2013–2026; confirm sort by relevance.
3. Run S1–S5 exactly as written; after each string, immediately record: exact string, approx. displayed count, number screened.
4. For every candidate: check English language → full-text accessibility → peer-review status/publication type → manufacturing relevance → genuine-reshoring definition; log exclusions with reason codes.
5. Log duplicates against the existing 33-source corpus (R6) and across strings (R7).
6. List any newly included study with full bibliographic details; do not add it to the thesis until it has been through the new-source assessment procedure (see `research/new_source_assessments.md` for the format).
7. Save the completed log as `resources/update_search_log.md`; the PRISMA diagram and the 3.2 placeholder are completed only from this log.
8. Do not estimate anything you failed to record — rerun the string instead.
