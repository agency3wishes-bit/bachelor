# Handover — Bachelor's Thesis Project

**Repo:** `agency3wishes-bit/bachelor` · **Branch:** `claude/thesis-examination-protocol-acutfp` · **Written:** 2026-07-15

This file is a one-time handover snapshot for continuing this project in a fresh chat session. It will go stale as work continues — treat it as a starting point, not a live status file. `thesis/AUTHOR_INPUT_NEEDED.md` is the file that should be kept current as the ongoing tracker.

## What this project is

University of Vienna Bachelor's thesis in International Business: *"Barriers to Reshoring from Asian Markets: A Systematic Literature Review"* (author: Serdiuk Aleksandra). The professor approved the topic, scope, and research questions from the original proposal but **rejected its source list**, because several references were AI-generated/non-existent. Everything in this repo since has been rebuilding the thesis on a fully verified, real, open-access-first source corpus, governed by a strict decision-gate examiner protocol (`CLAUDE.md`, checked into the repo root — it auto-loads and governs how any Claude session reviews thesis sections in this repo; read it first).

## What's done

- **Corpus finalised:** 36 entries total — 21 formal analytical studies + 8 contextual + 5 methodology + 2 theory sources (Williamson 1985, Barney 1991). 34 of the 36 are held as full-text PDFs in `resources/sources/` and were read and verified within this project (everything except the two theory books, which are approved on a separate library-access basis — see `resources/open_access_audit.md` for the full reconciled inventory and `resources/approved_source_corpus.md` for per-source detail).
- **Proposal continuity confirmed:** `resources/proposal_continuity_check.md` checks the current thesis against the author's approved proposal PDF (`resources/approved_proposal.pdf`) — same title/RQs/scope/theory/method, and documents exactly which proposal references do/don't appear in the final corpus (none were carried over as citations; a few overlap by coincidence of independent verification).
- **Chapters 1–6 all drafted and review-gated** per the CLAUDE.md protocol: `thesis/1_Introduction.md` through `thesis/6_Conclusion.md`. Review-gate audit files are in `thesis/review_gates/` (ch2–ch6; **Chapter 1 does not have a gate file yet — this is an open item**). Two real errors were caught and corrected during full-text verification: A02's host countries (workbook wrongly said China; full text says Romania/Morocco/Croatia/Hungary) and A15's non-existent labour-migration coding.
- **Compiled draft** available in `thesis/COMPILED_DRAFT_CH1-5.{md,txt,docx}` (predates Chapter 6 — needs regenerating to include it).
- **Update search protocol** reduced to a minimal, defensible 3-string design (`resources/update_search_protocol.md`, §0 justifies the scope via Snyder 2019/M01, the thesis's own methodology source).
- **Update search — in progress, NOT complete.** See "Immediate next step" below — this is exactly where the handover picks up.

## What's NOT done

1. **Finish or formally close out the update search** (see below — this is the one open decision).
2. **Chapter 3 §3.2 still has a bracketed placeholder** pending the completed search log.
3. **Appendix A (PRISMA flow diagram)** not yet built — depends on the same log.
4. **Chapter 1 has no review gate yet** (Chapters 2–6 do).
5. **Abstract is still marked PROVISIONAL** in `thesis/0_Front_Matter.md` — was drafted before Chapter 6 existed; needs rechecking now that Ch. 6 is done.
6. **Reference list not assembled** — corrections are queued (see `thesis/AUTHOR_INPUT_NEEDED.md`: A11 pages 103–117, C01 "Article 3" format, M03/M05 suffix order 2021b/2021a, M04's SSOAR URL now resolved) but nothing has been compiled into an actual APA 7 list yet.
7. **Final .docx assembly in the University of Vienna template** not started — landscape Table 1, Appendix A, Appendix B all need to go in.

## Immediate next step — pick up here

We were running the documented Google Scholar update search **live, interactively** (the author runs searches in their own browser and pastes screenshots; Claude reads titles, flags corpus duplicates, classifies exclusions with reason codes, and does the bookkeeping). This is the ONLY task in the whole project that has to be done by the author personally — an AI-run search would reproduce the exact fabrication problem that got the original proposal's sources rejected, and Google Scholar is also technically unreachable from the sandboxed tool environment (confirmed by a direct connection test).

**State right now** (full detail in `resources/update_search_log.md`):
- **String 1** (`"reshoring" OR "backshoring" barriers manufacturing`) — **complete**. 36 screened (target was 30 — went a bit over), 9 confirmed corpus duplicates, 2 clean exclusions (R2 nearshoring; R5 non-peer-reviewed), 6 flagged candidates for possible future new-source assessment (none added anywhere — full text + assessment still required).
- **String 2** (`"reshoring" OR "backshoring" China OR Asia manufacturing`) — **incomplete**. Only 6 of ~30 target screened.
- **String 3** (`intitle:reshoring OR intitle:backshoring`) — **incomplete**. Only 6 screened; also note its true result count (1,660) was much larger than the protocol's "naturally small" assumption, so it should get the same 30-item screening depth as S1/S2, not "screen everything."
- **Search date and incognito/browser status were never confirmed** by the author for any of the three strings — needed before the log can be finalised.

**The open decision**, posed to the author at the end of the last session, not yet answered:
1. **Finish S2 and S3** properly (another ~10–15 minutes of the same interactive screening), plus confirm the date/browser status, OR
2. **Stop here and disclose the partial search honestly** in Chapter 3's limitations — weaker-looking methodologically, but not fabricated.

Ask the author which they want, then either continue the interactive screening (same style as the rest of the session — read their screenshot, cross-check titles against `resources/approved_source_corpus.md` for duplicates, classify exclusions with reason codes from `resources/update_search_protocol.md` §3, flag genuine new candidates without adding them anywhere) or write Chapter 3's honest disclosure and move on to Appendix A with only the reconstructable full-text-stage numbers.

## After the update search is resolved

Follow this order (matches `thesis/OUTLINE.md`'s drafting order and `thesis/AUTHOR_INPUT_NEEDED.md`):
1. Complete Chapter 3 §3.2 and build Appendix A (PRISMA diagram) from the finalised log.
2. Chapter 1 review gate.
3. Recheck the Abstract now that Chapter 6 exists.
4. Assemble the APA 7 reference list (apply the queued corrections listed above).
5. Regenerate the compiled draft to include Chapter 6.
6. Final .docx assembly in the University of Vienna template (`resources/Bachelor_Thesis_Template_SS_2026.pdf`), with landscape Table 1 and Appendices A/B.

## Key files map

| File | What it is |
|---|---|
| `CLAUDE.md` | The decision-gate examiner protocol governing every section review — auto-loads in any session in this repo |
| `resources/approved_source_corpus.md` | The 36-source corpus, per-source detail, evidence levels, permitted chapters |
| `resources/open_access_audit.md` | Reconciled inventory (36 total / 34 PDFs), full-text verification status |
| `resources/proposal_continuity_check.md` | Continuity check against the approved proposal |
| `resources/update_search_protocol.md` | The 3-string search protocol + rationale (§0) + logging template |
| `resources/update_search_log.md` | **Current, partial** — the live log from this session; needs S2/S3 finished or the incompleteness formally accepted |
| `thesis/0_Front_Matter.md` through `thesis/6_Conclusion.md` | The thesis chapters |
| `thesis/review_gates/` | Per-chapter review-gate audits (ch2–ch6; ch1 missing) |
| `thesis/AUTHOR_INPUT_NEEDED.md` | The living open-items tracker — keep this updated as things resolve |
| `research/source_notes/*.md` | Per-source verification notes (34 files, one per full-text-held source) |
| `research/evidence_matrix.md` | 18 barrier themes × sources, evidence-type tagging |
| `research/new_source_assessments.md` | Format/precedent for assessing any new candidate source before it can be added |

## Working style notes for whoever picks this up

- **Never invent or estimate a number** — search counts, page numbers, quotations, dates. This is the single hardest rule in this project given why the original proposal was rejected.
- The author works interactively for anything requiring a live external tool (Google Scholar) — narrate exactly what you need from them in concrete, minimal steps, screenshot by screenshot.
- Every new claim added to a chapter must trace to a source in the corpus with a stated evidence type (DIRECT/PARTIAL/CONTEXT/UNSUPPORTED/UNVERIFIED per CLAUDE.md).
- Commit and push after every meaningful unit of work, with a descriptive message; this project has been committing frequently rather than batching.
