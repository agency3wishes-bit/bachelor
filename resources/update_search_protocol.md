# Final Documented Google Scholar Update Search — Protocol and Logging Template

Purpose: provide the reproducible search record for Chapter 3 (§3.2) and the PRISMA flow diagram (Appendix A). These are **predefined strings for the update search**; they are not, and must not be presented as, the historical strings of the original exploratory search.

**Scope note (2026-07-15, reduced from the original five-string design):** this protocol uses three strings rather than five, each covering a genuinely distinct facet of the research question (barrier-focused, Asia-specific, high-precision title sweep), with a lighter screening depth. This is a deliberate, defensible reduction, not a shortcut around rigour — see §0 for the justification, which should be cited if a supervisor asks why the update search is scoped this way.

## 0. Why this scope is academically defensible

A single-researcher Bachelor's SLR is not held to the standard of a multi-reviewer, database-exhaustive systematic review. Snyder (2019) — the thesis's own methodology source (M01) — explicitly endorses combining a documented, systematic database search with citation searching (backward/forward "snowballing") rather than requiring the database search alone to achieve saturation; the citation-searching side of that combination is already disclosed in Arm 2 of the PRISMA presentation below (§5) and does not need to be re-quantified here. Three well-targeted strings, each addressing a distinct facet of the RQ, satisfy the purpose of the *update* search: to give Chapter 3 a genuine, reproducible, prospectively logged record of *some* search activity, rather than to re-run database saturation for a search whose real discovery work already happened (via the corpus that is now complete and fully verified). Nothing about this scope requires estimating, inventing, or omitting a number — every value logged is still a real, checked observation.

## 1. Predefined search strings (Google Scholar syntax)

Google Scholar supports quoted phrases, OR (uppercase), exclusion with `-`, and `intitle:`. It treats spaces as AND. Run each string exactly as written, record it verbatim in the log, and do not modify strings mid-search (a modified string is a new log row).

| # | Search string | Rationale |
|---|---|---|
| S1 | `"reshoring" OR "backshoring" barriers manufacturing` | Core barrier literature — the RQ's central concept |
| S2 | `"reshoring" OR "backshoring" China OR Asia manufacturing` | Asia-host-specific evidence — the thesis's defining scope condition |
| S3 | `intitle:reshoring OR intitle:backshoring` | High-precision title sweep — naturally small, low-effort, catches anything the other two miss |

These three were kept from the original five because they map directly onto the two concepts the RQ itself names (barriers; Asian markets) plus a low-cost completeness check. The two dropped strings (implementation-only phrasing; capability/supplier sub-theme) substantially overlapped with S1's coverage and are not independently needed for a defensible update-search record.

## 2. Settings and screening rule

- **Publication-year range:** 2013–2026 (custom range in the left sidebar). Rationale: the manufacturing-reshoring research stream is effectively post-2013; earlier foundational work enters the thesis via citation searching and the approved theory sources, not via this update search. Record the range actually applied.
- **Sort order:** relevance (Google Scholar default). Do not sort by date.
- **Screening depth:** screen the **first 30 results** for S1 and S2 (3 pages each). Stop-rule: you may stop early if 10 consecutive results are irrelevant — record the actual number screened either way. For S3 (title sweep), screen **all** displayed results, since a title-restricted search is typically small.
- **Language/access rule:** apply the same manual checks as the original process — English language, full text accessible, peer-review status, publication type, manufacturing relevance — and record exclusions under the reason codes below.
- **Do not use** Google Scholar profiles, alerts, or "since year" quick links for the formal record; only the logged string runs count.

## 3. Exclusion reason codes (for the log and PRISMA)

R1 not manufacturing · R2 not genuine reshoring (China+1, re-offshoring, nearshoring without return, foreign-to-foreign) · R3 not English · R4 full text inaccessible · R5 not peer-reviewed (preprint/blog/report — note: may still be considered as contextual source, log separately) · R6 duplicate of corpus source · R7 duplicate across strings · R8 decision-stage only, no barrier/implementation content and no contextual value · R9 other (state).

## 4. Logging template (one row per string; fill during the session, not afterwards)

| Field | S1 | S2 | S3 |
|---|---|---|---|
| Search date (YYYY-MM-DD) | | | |
| Exact string as entered | | | |
| Year restriction applied | | | |
| Approx. results displayed (GS header) | | | |
| Records actually screened | | | |
| Duplicates (R6/R7) | | | |
| Full texts assessed | | | |
| Full texts excluded (n + reason codes) | | | |
| Newly included studies (n + short refs) | | | |

Also record once per session: browser/incognito status (recommended: logged-out incognito window, to reduce personalisation), and country/interface language.

## 5. PRISMA 2020 presentation (the defensible structure)

Use PRISMA 2020's **two-arm flow**, which exists precisely for this situation:

- **Arm 1 — "Identification of studies via databases and registers":** the documented update search only. All values come from the log above. Platform: Google Scholar (named as a search platform, not a curated database — keep the wording "literature-discovery platform").
- **Arm 2 — "Identification of studies via other methods":** the original exploratory Google Scholar searching, backward reference searching, forward citation ("Cited by") searching, and related-article suggestions. For this arm, report the stages that are genuinely reconstructable from the corpus record: sources assessed at full text (n = 34 held and verified in the corpus; additional assessed-but-rejected sources only if the author can enumerate them), assigned to the formal analytical sample (n = 21), retained as contextual/policy/decision-support sources (n = 8, including the user-approved editorial C06), retained as methodology sources (n = 5). For "records identified" in this arm, state **"not recorded (exploratory phase)"** in a footnote rather than inserting any number.
- The two approved primary theory sources (Williamson, 1985; Barney, 1991) are **not** studies and appear in neither arm.
- Flow-diagram caption wording: "Records identified via the original exploratory search process (Arm 2) were not counted prospectively; the update search (Arm 1) provides the documented, reproducible search record."

## 6. Author checklist for the search session (Part E)

1. Open a logged-out incognito browser window; note the date.
2. Set the custom year range 2013–2026; confirm sort by relevance.
3. Run S1–S3 exactly as written; after each string, immediately record: exact string, approx. displayed count, number screened.
4. For every candidate: check English language → full-text accessibility → peer-review status/publication type → manufacturing relevance → genuine-reshoring definition; log exclusions with reason codes.
5. Log duplicates against the existing 36-entry corpus (R6) and across strings (R7).
6. List any newly included study with full bibliographic details; do not add it to the thesis until it has been through the new-source assessment procedure (see `research/new_source_assessments.md` for the format).
7. Save the completed log as `resources/update_search_log.md`; the PRISMA diagram and the 3.2 placeholder are completed only from this log.
8. Do not estimate anything you failed to record — rerun the string instead.

Expected total time: roughly **15–20 minutes** for all three strings combined, most of it on S1 and S2; S3 is typically a two-minute check.
