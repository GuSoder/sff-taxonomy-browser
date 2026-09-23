# Gap intake 2022+ (queue built 2026-09-23)

Gustav 2026-09-23 19:02 via parent: "Ok, then I want you to set up that sweep" - fill the post-2021 coverage gap shown by tools/year_sweep.py.

- Builder: `python3 tools/build_gap_queue.py` (add `--fetch` to refresh cached pages in sources/). Deterministic.
- Sources: sfadb.com award pages 2022-2026, novel categories, winners and shortlists: Hugo, Nebula, Arthur C. Clarke, World Fantasy, Locus Awards (SF novel + fantasy novel), BSFA. Plus locusmag.com Recommended Reading 2022-2025, novel sections (SF, Fantasy, Horror, YA, First; 2025 adds Translated), the same sections the first intake used.
- Kept: publication (eligibility) year 2022 or later. Award year 2022 pages are cached but only contribute 2022+ books.
- Deduped internally (title + author surname), against every book in the live tree, and against all 989 first-intake candidates (covers the 245 not added). See dedupe-report.json.
- Order: score (number of source lists) desc, then award wins, then title. progress.json tracks next/processed/added/held.
- Known gaps: WFA 2026 is shortlist only (winners announced later); no Locus Recommended list for 2026 yet (appears Feb 2027). 2026 releases belong to the monitoring layer.
