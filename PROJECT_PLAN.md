# Thesis Production Plan

**Thesis:** "Barriers to Reshoring from Asian Markets: A Systematic Literature Review"
**Degree:** Bachelor in International Business, University of Vienna (supervisor per template: Dr. Aveed Raha)
**Governing documents:** `CLAUDE.md` (decision-gate review protocol), `resources/approved_source_corpus.md` (33 approved sources), `resources/Bachelor_Thesis_Template_SS_2026.pdf` (formal template)

---

## 1. Skill-to-template relevance assessment

The `thesis-writing` skill was checked against the uploaded University of Vienna template. **Verdict: relevant and adopted as the writing method, with four binding adaptations.**

Where they agree (skill applies as-is):

| Template requirement | Skill coverage |
|---|---|
| Numbered chapters 1–6 + References, with 1.1/1.2/1.3 Introduction subsections | Identical core-chapter sequence (Introduction → Literature Review → Methodology → Results → Discussion → Conclusion) |
| Abstract, acknowledgements (voluntary), table of contents | Front-matter checklist |
| Discussion split into results/theoretical/practical/limitations (5.1–5.4) | Chapter 5 component list matches one-to-one |
| Flowing prose, no bullet points in final text | "Never submit bullet points"; paragraph architecture (topic → evidence → analysis → transition) |
| APA-style citation for business | Citation-style table: business = Harvard/APA → **APA 7** (also required by CLAUDE.md) |

Binding adaptations (template and repository protocol override the skill):

1. **Scale.** The skill's length row (20,000–100,000+ words) describes Master's/PhD theses. This is a Bachelor's thesis; the template fixes the abstract at **150–200 words** (not the skill's 200–500) and implies a compact document. Working budget in §4 below.
2. **Methodology chapter content.** The skill's Chapter 3 checklist (participants, instruments, ethics approval, consent) assumes primary data collection. This thesis collects **no primary data**. Chapter 3 instead follows the template's 3.1 Research Design / 3.2 Data Collection / 3.3 Data Analysis headings interpreted for an SLR: review design (M01 Snyder), PRISMA search & selection (M03/M05 Page et al.), coding and thematic synthesis (M02 Thomas & Harden; M04 Mayring).
3. **Evidence gathering.** The skill's `zotero-research-lookup` / `semantic-scholar-lookup` tools are not installed, and the review protocol **forbids adding sources** anyway. Stage-1 evidence scaffolds are built exclusively from the 33 approved sources (Phase 1 below replaces the Zotero step).
4. **Review step.** The skill's generic REVIEW checklist is replaced by the repository's decision-gate protocol (`CLAUDE.md`): every chapter must pass through Parts A–G and reach a READY/STOP verdict before it is considered final.

---

## 2. Model assignment

| Role | Model | Rationale |
|---|---|---|
| Planning, structure, outlines, review gates (examiner), final revision pass | **Fable** (this session) | Strongest reasoning for argument architecture and the strict source-audit protocol |
| Evidence extraction — core sources (L1 empirical + core reviews: A01, A02, A06, A09, A13, A16, A18) | **Opus** subagents | Dense extraction requiring judgement (drivers vs. implementation barriers, firm vs. macro level, Asia attribution) |
| Evidence extraction — supporting/context/methodology sources (remaining 26) | **Sonnet** subagents | High-volume, well-specified extraction against a fixed note template |
| First-pass drafts of formulaic chapters (3 Methodology, 4 Results skeleton + tables) | **Opus** subagent | Evidence-dense, template-driven prose |
| Final prose of argument chapters (2, 5, 6) and revision of all chapters for one voice | **Fable** | Writing quality and protocol compliance |

---

## 3. Phases

### Phase 0 — Infrastructure (DONE)
Protocol installed as `CLAUDE.md`; corpus extracted to `resources/approved_source_corpus.md`; template requirements extracted; Chapter 1 first draft committed (`thesis/1_Introduction.md`).

### Phase 1 — Evidence base (Opus + Sonnet) — **IN PROGRESS (revised method)**
**Constraint confirmed twice:** this environment's network policy returns 403 for all academic publisher hosts via direct fetch (curl and WebFetch alike — diva-portal, MDPI, Springer, ScienceDirect, Emerald, PMC, BMJ). Full-text PDFs cannot be downloaded, and no source PDFs were uploaded to `resources/sources/`.

**Working method adopted instead:** the `WebSearch` tool is reachable (confirmed working) and returns search-engine snippets, abstracts, and indexed excerpts even for sources whose full text is unreachable. Phase 1 now proceeds on **abstract/snippet-level evidence**, not full-text extraction. Every subagent is under a hard no-fabrication rule: any claim not directly attributable to a search snippet must be marked UNVERIFIED, and page numbers, sample sizes, countries, or findings must never be invented. This means many Part C source-to-claim checks downstream will land on PARTIAL SUPPORT or UNVERIFIED rather than DIRECT SUPPORT for claims that need page-level detail — that is expected and correctly conservative, not a research failure.

**Dispatch (8 parallel subagents, launched):**
- Opus × 3 — core sources (highest evidentiary weight): A01, A02, A06 · A09, A13 · A16, A18
- Sonnet × 5 — supporting/context/methodology sources: A03–A08 group · A10–A15 group · A17/A19–A21/A25 group · A29+M01–M04 group · M05+C01–C05 group

Each subagent writes `research/source_notes/<ID>.md`: APA 7 reference, corpus classification fields, what was actually established from search snippets (with confidence level), barrier-relevant claims coded to driver/barrier, firm/macro level, Asia-specificity, framework category, and DIRECT/PARTIAL/UNVERIFIED status, plus an explicit gaps section. C01–C05 notes additionally require a boundary check confirming they are not coded as barrier evidence (they describe China+1/macro relocation, not reshoring). M01–M05 notes focus on methodological procedure instead of barrier content.

**Consolidation (next, Fable):** once all 8 batches return, build `research/evidence_matrix.md` — barrier × source matrix with evidence type per cell (direct empirical / review / conceptual, per the corpus Legend), keeping the three evidence types countable separately (workbook decision rule 2), and flag which framework cells rest only on PARTIAL/UNVERIFIED evidence.

**If the user later provides full-text PDFs**, the affected source notes should be re-run to upgrade verification status — this is a reasonable follow-up once Phase 1's first pass is reviewed.

### Phase 2 — Structure lock (Fable)
Full table of contents with thesis-specific subheadings (template allows renaming); per-section word budgets; paragraph-level outline per chapter with citation slots filled from the evidence matrix. Committed as `thesis/OUTLINE.md` for user sign-off before mass drafting.

### Phase 3 — Drafting (order and models)
| Order | Chapter | First draft | Notes |
|---|---|---|---|
| 1 | 3 Research Methodology | Opus | Formulaic; uses M01–M05 only; PRISMA flow description; 33→21 corpus rationale |
| 2 | 2 Literature Review | Fable | Concepts & definitions; relocation-form boundary (reshoring vs. China+1/nearshoring); TCE & RBV; drivers vs. barriers distinction; gap |
| 3 | 4 Results | Opus (skeleton + tables) → Fable (prose) | Barriers by the four categories; evidence weighted by L1/L2 and Asia specificity; no interpretation |
| 4 | 5 Discussion | Fable | 5.1 results, 5.2 theoretical (TCE/RBV), 5.3 practical (SQ2 managerial implications), 5.4 limitations & future research |
| 5 | 6 Conclusion | Fable | Answers RQ, SQ1, SQ2 directly; contributions |
| 6 | 1 Introduction (revision) + Abstract (150–200 words) | Fable | Align roadmap with final content |

Each chapter lives in `thesis/<n>_<Name>.md`. References accumulate in `thesis/7_References.md` (APA 7, alphabetical).

### Phase 4 — Review gates (Fable as examiner)
After each chapter draft: run the full `CLAUDE.md` protocol (Parts A–G), with Part C checked against the Phase-1 source notes (this is what upgrades claims from UNVERIFIED to Direct/Partial/Context). Iterate until "STOP: The section is ready." A chapter that has passed its gate is not reopened except for cross-chapter consistency.

### Phase 5 — Assembly and formatting
Front matter (title page fields from template, abstract, ToC), one full-document consistency pass (terminology, British English except verbatim RQs, tense discipline per skill), then export to `.docx`: Times New Roman 12 pt, 1.5 line spacing, 1-inch margins, numbered headings — via pandoc with a reference docx built to template specs.

---

## 4. Working word budget (provisional — confirm against course guidelines)

The template does not state a total length. Until the user confirms the programme's requirement, drafting targets **~9,000–10,500 words** of core text (chapters 1–6, excluding references/appendices): Ch1 ≈ 1,000 · Ch2 ≈ 2,500 · Ch3 ≈ 1,400 · Ch4 ≈ 2,500 · Ch5 ≈ 1,800 · Ch6 ≈ 800. Budgets are adjusted, not padded, if the confirmed requirement differs.

## 5. Repository layout

```
CLAUDE.md                      review protocol (governs every review)
PROJECT_PLAN.md                this plan
resources/                     template PDF, corpus xlsx + md extract, [sources/ PDFs — Phase 1]
research/source_notes/         per-source evidence notes (Phase 1 output)
research/evidence_matrix.md    barrier × source matrix (Phase 1 output)
thesis/OUTLINE.md              locked structure (Phase 2 output)
thesis/1_Introduction.md …     chapter drafts (Phase 3)
thesis/7_References.md         APA 7 reference list
```

## 6. Open questions for the user

1. **Phase 1 unblock:** upload PDFs to `resources/sources/` (preferred) or relax the environment network policy?
2. **Total word count / page requirement** for the programme (template is silent)?
3. Any supervisor-specific instructions beyond the template (e.g., required appendices such as the PRISMA flow diagram or the coding table — recommended for an SLR and easy to include)?

Until (1) is resolved, source-level claims in drafts remain formally UNVERIFIED under the protocol; Chapters 3 and 2 can proceed furthest without full texts, but Results (Ch. 4) must wait for the evidence base.
