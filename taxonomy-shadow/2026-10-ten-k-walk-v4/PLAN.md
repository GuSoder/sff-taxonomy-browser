# Shadow tree v4 - plan

v1, v2, v3 folders stay intact. The live tree and original taxonomy files are not touched. Only the Drive/GitHub taxonomy and the 10k list are used.

## Rules applied (from the docs in taxonomy/)
- NAMES.md: search order (established term, then catchy, then general), the tests, hints point to the closest established genre, No A + B names.
- SPLITTING.md: a leaf freezes at 10 cards, split with umbrella, no slush buckets, no dirty branches, a card with no honest leaf holds.
- DUPLICATES.md: one card per series, straddling series go by what the series is about.
- PRIORITY.md: golden rule first (anything at 10 splits), then hanging books seed new leaves, then intake.
- A book's leaf follows what it is about, never its author. No estimation by author.
- Where a book already sits in the original tree, v4 agrees with the original tree.

## Source of truth
Plain YAML in the repo: one file per genre, books by title. No row numbers, no pipe files, no /tmp index. The render is generated from the YAML and is not edited by hand.

## Phases
1. Baseline: convert original tree + v3 placements into per-genre YAML (books by title).
2. Hard walk of every book, root-down, from its own blurb/reviews/title; one record per book (genre-yaml placement + evidence line). Held books get a named reason.
3. Series folding (one card per series).
4. Golden rule splits where a leaf reaches 10, axis from the cards' content, distribution shown first.
5. Names pass: every new genre name tested against NAMES.md, many revisions, graveyard recorded.
6. Audit: no leaf with a slush theme, no umbrella with direct cards, shadow agrees with original tree.
