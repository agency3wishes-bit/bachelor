# Source ID Mapping — source_coding_notes.docx vs. approved_source_corpus.md

`resources/source_coding_notes.docx` is an earlier working conversation (Russian/English, apparently using NotebookLM to analyze source PDFs directly) that used a continuous `A01–A31` numbering scheme before the corpus was finalized into the current `A/C/M` split in `resources/approved_source_corpus.md`. Cross-checked line-by-line; **no sources outside the approved 33 appear in the document** — every ID resolves to an existing corpus entry.

| Old ID (docx) | Final ID (approved corpus) | Author (Year) |
|---|---|---|
| A01–A21 | A01–A21 (unchanged) | (see approved_source_corpus.md) |
| A22 | M01 | Snyder (2019) |
| A23 | C01 | Yang (2016) |
| A24 | C02 | Xing et al. (2024) |
| A25 | A25 (unchanged) | Gupta et al. (2023) |
| A26 | C03 | Gao et al. (2022) |
| A27 | C04 | Somoza Medina (2022) |
| A28 | C05 | McCully & Simola (2024) |
| A29 | A29 (unchanged) | Heikkilä et al. (2018) |
| A30 | M02 | Thomas & Harden (2008) |
| A31 | M03 | Page et al. (2021) — PRISMA Statement |
| M04, M05 | M04, M05 (already final in the doc) | Mayring (2014); Page et al. (2021) — PRISMA E&E |

Note: the document's earliest section (roughly its first ~800 lines) contains a provisional draft numbering where A02/A03 briefly denoted Wiesmann (2017) and Espíndola (2023) — these were corrected within the same document to their final IDs (A06, A07) once the numbering stabilized. Use author-name matching, not raw ID matching, when reading the early section.
