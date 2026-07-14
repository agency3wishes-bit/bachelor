# Thesis Workflow Playbook

A reusable, topic-agnostic playbook for running a thesis (or any source-grounded academic writing project) through Claude Code, based on the working setup and lessons learned in this repository (`bachelor` — "Barriers to Reshoring from Asian Markets"). Copy this file into a new repository and adapt every bracketed placeholder to the new topic; the workflow itself does not change.

---

## 0. What this workflow assumes

- A degree-level thesis where **every claim must trace to an approved source**, and where a strict, repeatable examiner protocol is more valuable than ad hoc feedback.
- Method is typically a **Systematic Literature Review** (no primary data), but the same skeleton works for empirical theses — swap the Methodology chapter content accordingly (see §4).
- Writing happens across **multiple Claude sessions/models** over time — planning session, research subagents, drafting session, review passes — so everything that matters must live in the repo, not in any one conversation's memory.

---

## 1. Repository skeleton

Set this up before writing a single sentence of thesis text:

```
CLAUDE.md                        the decision-gate review protocol (see §2) — auto-loads every session
PROJECT_PLAN.md                  topic-specific plan: phases, model assignment, open questions
THESIS_WORKFLOW_PLAYBOOK.md      this file (generic — copy as-is between projects)
.claude/skills/thesis-writing/   the thesis-writing skill (or your institution's equivalent)
resources/
  approved_source_corpus.md      human-readable extract of the approved source list (see §3)
  <corpus>.xlsx                  original source-classification spreadsheet, kept as the authoritative copy
  <institution>_thesis_template.pdf   the formal formatting/structure template
  source_id_mapping.md           only if a supplementary document uses a different numbering scheme (see §6)
research/
  source_notes/<ID>.md           one file per approved source (see §5)
  evidence_matrix.md             consolidated barrier/theme × source matrix (see §7)
thesis/
  OUTLINE.md                     locked chapter/paragraph structure (see §8)
  1_Introduction.md, 2_...md     chapter drafts, one file per chapter
  7_References.md                running APA/Harvard/etc. reference list
```

---

## 2. Write the decision-gate review protocol first (`CLAUDE.md`)

This is the single highest-leverage file. It turns every future session — including ones that know nothing about prior conversations — into a consistent, strict-but-fair examiner. Model it on the structure used here:

1. **Thesis context**: exact title, degree, method, the research question(s) verbatim (never let a model paraphrase these), core scope definition (what counts as the phenomenon under study vs. what looks similar but isn't — e.g. this project's "reshoring vs. China+1" boundary), the analytical framework categories, and the theoretical lenses.
2. **Review principle**: a closed list of the *only* valid reasons to recommend a change (factually wrong, unsupported, off-topic, illogical, misclassified source, contradicts scope, poor structure, real grammar/APA error, could realistically affect the grade) and an explicit list of *invalid* reasons (stylistic preference, "could be shorter," synonyms). This is what stops a review from turning into endless polishing.
3. **Severity classification**: Critical / Major / Minor / Optional, each with concrete examples specific to your thesis's failure modes.
4. **Required academic checks**: section-function awareness (don't grade an Introduction for lacking Results), logical structure, topical relevance (list the specific tangents your thesis is prone to — e.g. "don't drift into general globalisation commentary"), evidence/source linkage (Direct/Partial/Context/Unsupported/Unverified — see §5), the key conceptual distinction your thesis turns on (here: drivers vs. implementation barriers), and natural-writing checks (repetitive paragraph templates, AI-detector-style tells — but never optimize prose *for* an AI detector).
5. **Grade-impact test**: before flagging anything, force the question "what realistic negative effect could this have?" — if none, it's Optional or omitted.
6. **Verdict system**: A (Ready) / B (Ready after minor corrections) / C (Substantive revision required) / D (Not usable) — each with a hard rule about what output format follows (don't rewrite a READY section; don't fabricate a full rewrite for a D-verdict section missing evidence).
7. **Required output format**: fixed Parts A–G (Verdict → Grade-relevant issues table → Source-to-claim check table → Structure/logic → Required corrections → Optional observations → Stop decision). A fixed format is what makes reviews comparable across chapters and sessions.
8. **Prohibited review behaviour**: explicit list — no automatic rewriting, no adding sources, no strengthening claims beyond evidence, no fabricating source support, no optimizing for AI-detection, no continuing to "improve" a section that already meets the standard.

**The stop rule is the most important sentence in the file**: if the section already does its job, say so and stop. Everything else in the protocol exists to make that judgment rigorous rather than lazy.

---

## 3. Assemble the approved source corpus

Whatever list of approved sources exists (a spreadsheet, a reference manager export, a supervisor-approved bibliography), extract it into `resources/approved_source_corpus.md` — one entry per source with at minimum:

- Full APA/Harvard reference
- Evidence level / study type (empirical vs. review vs. conceptual vs. methodological — keep these three types **countable separately**, never blended into one "supports the claim" bucket)
- Topical/geographic specificity relevant to your scope (here: Asia specificity)
- Final role (core empirical / core review / supporting / background-context / methodology / decision-support-only)
- Permitted thesis chapters
- The classifier's own inclusion/exclusion rationale — this is gold; it tells future sessions exactly what a source can and cannot be used to support, so they don't have to re-derive it

If the spreadsheet has a Legend/decision-rules sheet, extract that too — it defines what "Direct/Partial/Context/Unsupported/Unverified" and evidence-level letters mean *for this specific thesis*, which the protocol in `CLAUDE.md` should reference directly.

**Rule for the whole project**: citations to anything outside this corpus are a protocol violation. If a new document later surfaces (see §6), cross-check its source IDs against this corpus before using any of its content — do not silently expand the approved list.

---

## 4. Get (and correctly scope) the thesis-writing skill

A generic `thesis-writing` skill (chapter structure, paragraph architecture, citation integration, literature-review two-stage process) is useful scaffolding but is usually written for Master's/PhD scale and assumes tools you may not have (e.g. a Zotero RAG lookup skill). Before using it:

1. Read the institution's actual template PDF/DOCX and diff it against the skill's assumptions: abstract word count, chapter numbering, required subsections, front-matter requirements, citation style.
2. Flag every place the skill's generic advice conflicts with the template or the thesis's actual method (e.g. a Methodology chapter checklist that assumes primary data collection, when the thesis is a pure literature review — reinterpret that chapter around search strategy, screening, coding, and synthesis instead).
3. If the skill names a literature-lookup tool that isn't installed in this environment, don't invoke it — substitute the multi-agent WebSearch-based research process in §5, and note in the plan that this is a deliberate substitution, not a skipped step.
4. The skill's own "REVIEW" checklist should be treated as **subordinate** to `CLAUDE.md`'s decision-gate protocol — the protocol wins on every point of conflict, since it's the thing actually calibrated to this thesis's grading standard.

Write these adaptation decisions into `PROJECT_PLAN.md` explicitly (see §9) so a later session doesn't have to re-derive them.

---

## 5. Multi-agent research phase

### 5.1 Test network access before promising anything
Academic publisher domains are very often blocked by sandboxed environments' network policies, even when a general web-search tool works fine. Test this explicitly and early:
```
curl -sS "$HTTPS_PROXY/__agentproxy/status"   # check for connect_rejected entries against publisher hosts
```
If direct fetch/WebFetch to publisher domains returns 403 but a `WebSearch`-style tool still works, **switch the whole research phase to abstract/snippet-level evidence gathering** rather than blocking on full-text access. This is a real, working fallback — not a failure state — as long as every downstream note honestly marks what it could and couldn't verify.

### 5.2 Split sources by evidentiary weight, not evenly
Group the approved sources into:
- **Core** (direct empirical / foundational review evidence — the sources the Results/Discussion chapters will lean on hardest): assign your strongest model (e.g. Opus), fewer sources per agent (2–3), more search queries per source (4–5), more scrutiny instructions.
- **Supporting / context / methodology**: assign a faster model (e.g. Sonnet), more sources per agent (5–6), fewer queries per source (2–4).
- **Context-only sources that sit outside your scope definition** (e.g. sources about a related-but-different phenomenon than the one you're studying): give these agents an explicit "boundary check" task — confirm the source does NOT get coded as direct evidence for your phenomenon, and say so explicitly in the note.

### 5.3 The no-fabrication rule is non-negotiable
Every research subagent prompt must contain, verbatim in spirit: *if you cannot find real evidence for a claim, say so explicitly — never invent a page number, sample size, country, industry, or quote.* This single instruction is what keeps a WebSearch-only research phase honest. Pair it with an explicit per-claim verification tag: **DIRECT** (an actual snippet/quote supports it) / **PARTIAL** (suggestive but incomplete) / **UNVERIFIED** (inferred only from title or corpus metadata, not confirmed).

### 5.4 Per-source note template
Each `research/source_notes/<ID>.md` should contain: full reference, corpus classification fields (copy them in — don't make a reader cross-reference), what was actually established from available evidence (with confidence level stated), a coded claims table (claim / driver-vs-outcome-type distinction relevant to your framework / your analytical category / your scope-specificity flag / verification status), and an explicit gaps section stating what full text would be needed to confirm. Context-only and methodology-only sources get a lightly adapted version of this template (see §5.2).

### 5.5 Handling rate limits / session limits gracefully
Background subagents can be interrupted mid-task by API session limits. Because well-behaved agents write output files incrementally (one source finished → one file written, not batched at the end), a failed agent often still leaves real, usable output behind.
- **Check the filesystem before assuming a batch failed.** `ls` the output directory — you likely have more done than the failure notification suggests.
- **Relaunch only the actual gap**, not the whole batch — re-running completed work wastes quota and risks hitting the same limit again.
- If asked to restore full parallelism after a partial failure, split just the remaining sources across a couple of small parallel agents (not one per remaining source, not one giant sequential agent) — and have each agent check the output directory first and skip anything a sibling agent already wrote, since they run concurrently.
- Commit and push after every batch completes, not just at the end — a git history of incremental research commits is itself a safety net.

---

## 6. Incorporating supplementary resources mid-project

Expect the user to hand over more material as the project goes — prior conversation exports, NotebookLM sessions, hand-written coding sheets, extra PDFs. Before treating anything in a new document as usable evidence:

1. Convert it to a readable/searchable format (docx/xlsx → markdown; extract tables in document order, don't just dump text).
2. **Cross-check every source ID or title it references against the approved corpus.** Documents assembled over time often use an earlier or different numbering scheme — build an explicit ID-mapping table (`resources/source_id_mapping.md`) rather than assuming a mismatch means a new, unapproved source. Confirm by author/title match, not just ID string match.
3. If genuinely new sources appear that aren't in the approved corpus, **do not use them** — flag them to the user and wait for explicit approval to add them. Silently expanding the source list is a protocol violation regardless of how good the new material looks.
4. Treat richer supplementary evidence (e.g. content that appears to derive from actual full-text reading via a tool like NotebookLM) as higher-confidence than pure search-snippet evidence, but still state its provenance explicitly in any note you upgrade — a future reviewer needs to know *why* something moved from UNVERIFIED to DIRECT.
5. When upgrading existing source notes with new material, **append a clearly labelled new section rather than silently rewriting** — preserve the audit trail of what was known when.

---

## 7. Consolidate the evidence base

Once source notes are complete, build `research/evidence_matrix.md`: a matrix of your analytical framework's categories (rows or columns) against sources, with the evidence type in each cell (empirical / review / conceptual — kept separable, per §3). This is what turns 30+ individual notes into something a drafting session can actually write from without re-reading everything. Flag any framework cell that rests only on PARTIAL/UNVERIFIED evidence — that's a known weak point the Discussion/Limitations section should acknowledge honestly rather than paper over.

---

## 8. Lock the structure before drafting

Produce `thesis/OUTLINE.md`: full chapter/section list (mapped to the institution's template numbering), word budgets per section, and — critically — which sources from the evidence matrix fill which paragraph's citation slots. Get explicit user sign-off on this before mass-drafting; restructuring after several chapters are written is expensive, restructuring an outline is cheap.

---

## 9. Model assignment and drafting order

Write the assignment into `PROJECT_PLAN.md` explicitly, e.g.:
- **Planning, outlining, and every review-gate pass**: your strongest reasoning model — this is where the decision-gate protocol gets applied, and where structural judgment calls happen.
- **Research subagents**: split by evidentiary weight per §5.2.
- **First-draft prose of formulaic, evidence-dense chapters** (Methodology, Results skeletons): a fast, capable model.
- **First-draft prose of argument-heavy chapters** (Literature Review, Discussion, Conclusion) and the final full-document consistency pass: your strongest model again.

Draft in an order that respects dependencies, not the final chapter order: methodology and results-skeleton first (formulaic, unlocks everything else), then literature review (needs the evidence matrix but not results), then results prose, then discussion, then conclusion, then revise the introduction and write the abstract last (so the roadmap paragraph actually matches what got written).

---

## 10. Review gates — non-negotiable

After every chapter draft, run it through the full `CLAUDE.md` protocol (Parts A–G) before moving to the next chapter. Use the source notes from §5 to actually check Part C's source-to-claim table — don't let a review declare "Direct support" without checking against the note's own verification tags. A chapter that reaches "STOP: ready" is not reopened except for cross-chapter consistency edits later.

---

## 11. Assembly and formatting

Once all chapters pass their review gate: build front matter (title page fields, abstract within the template's word limit, table of contents), do one full-document consistency pass (terminology, spelling variant, tense discipline — methods/results past tense, established facts present tense), then export to the institution's required format (fonts, margins, line spacing, heading numbering) — e.g. via pandoc with a reference document built to the template's exact specs.

---

## 12. Common pitfalls (learned the hard way)

- **Don't assume full-text access.** Test it before promising a research plan that depends on it.
- **Don't let "multi-agent" mean "duplicate work."** Check the filesystem for what's already done before relaunching a batch.
- **Don't treat a "failed" background-agent notification as "nothing happened."** Incrementally-writing agents often leave real, committable output even after an API error killed them mid-task.
- **Don't silently expand the source corpus** when new material surfaces — cross-check IDs, flag anything new, wait for approval.
- **Don't skip the network/tooling reality check on a borrowed skill.** A skill written for a different scale or a different toolset needs explicit, documented adaptation, not silent partial application.
- **Don't let the review protocol become a rewriting machine.** The stop rule exists because "I could make this better" is always true and is not the same as "this needs to change."
- **Commit and push after every meaningful batch**, not just at logical project milestones — background research and drafting work is otherwise one interrupted session away from being lost.

---

## 13. Quick-start checklist for a new thesis topic

1. [ ] Create the repo skeleton (§1).
2. [ ] Write `CLAUDE.md` with this thesis's exact title, RQs, scope boundary, framework categories, theoretical lenses (§2).
3. [ ] Extract the approved source corpus to `resources/approved_source_corpus.md` (§3).
4. [ ] Get the institution's template; diff it against the thesis-writing skill; document adaptations in `PROJECT_PLAN.md` (§4).
5. [ ] Test network access to publisher domains; decide full-text vs. abstract-level research strategy (§5.1).
6. [ ] Split sources into core/supporting groups; dispatch parallel research subagents with the no-fabrication rule baked in (§5.2–5.4).
7. [ ] Consolidate into `research/evidence_matrix.md` (§7).
8. [ ] Lock `thesis/OUTLINE.md` and get sign-off (§8).
9. [ ] Draft chapters in dependency order, running each through the `CLAUDE.md` review gate before moving on (§9–10).
10. [ ] Assemble and format to the institutional template (§11).
