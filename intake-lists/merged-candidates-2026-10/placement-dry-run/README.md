# Placement dry-run, 2026-10 (analysis only; nothing added to the tree, 10-per-leaf cap disregarded on purpose)

Input: the 10,069 non-Titan candidates in `../candidates.tsv`. The 2,029 Titan-only rows are not placed (low-confidence genre).
Files: `placements.tsv` (every candidate, node, tier, basis), `leaf-projection.tsv` (all 322 leaves), `branch-projection.tsv`, `unmatched-top-authors.tsv`, scripts `ph2.py`, `out2.py`.

## How a candidate gets placed (only easy signals, no per-book research)
- **T1 leaf, easy**: its series matches a tree card, or its author's tree cards all sit in ONE leaf and the author has 4 or fewer candidates. 291 + 45 series matches, about 340.
- **T2 leaf, author cluster**: same one-leaf author but 5+ candidates (prolific). The author's books will probably split across series and leaves, so this is a pressure estimate, not an easy match. 1,027.
- **M**: curated author map from my own knowledge of what an author mainly writes (about 120 authors with 8+ candidates, e.g. Weber, Drake, Ringo, Lackey, Briggs), to a branch, not a leaf. 1,624 to branch, 46 to leaf.
- **B**: author already in the tree across several leaves; placed at the nearest common ancestor branch. 1,289.
- **Unmatched**: 5,792 (57%): author unknown to the tree and the map (5,352), anthologies and collections (246), no author (173), media tie-ins (21). About 1,000 of them are tagged Fantasy and 715 Science Fiction by Tor/Gollancz; the rest have no genre tag.

Totals: leaf-level 1,364 (T1 about 340, T2 1,027 minus overlap in rounding), branch-level 2,913, unmatched 5,792.

## Leaves that would overflow (existing cards + projected - 10)
- Strict (T1 only): 18 leaves overflow, 75 books over cap.
- With author clusters (T2): 67 of the 153 leaves that receive anything overflow, 803 books over cap.
Top cluster pressure (existing + T1 + T2, author driving it):
| Leaf | Existing | T1 | T2 | Main driver |
|---|---|---|---|---|
| fellowship-quest-fantasy | 5 | 2 | 85 | Terry Brooks, Tad Williams, Eddings |
| alt-civil-war | 4 | 0 | 85 | Turtledove (one author, many series: will spread across alt-history) |
| planetary-romance | 7 | 10 | 40 | Anne McCaffrey (Pern) |
| space-succession-opera | 3 | 0 | 45 | Walter Jon Williams, Zahn |
| destiny-quest-fantasy | 3 | 0 | 43 | Feist, Goodkind |
| techno-fiction-in-space | 5 | 0 | 41 | Stross, Morgan |
| hard-magic | 8 | 0 | 35 | Sanderson, Jordan |
| earthly-comic-fantasy | 9 | 11 | 20 | Tom Holt, Rankin |
| revisionist-quest-fantasy | 8 | 0 | 29 | |
| ecotopian | 8 | 0 | 27 | Carrie Vaughn |
| medieval-dynastic-intrigue | 4 | 0 | 29 | |
| animal-fantasy | 5 | 25 | 0 | Brian Jacques (Redwall) |

## Branches under pressure (placed at branch level, no leaf yet)
| Branch | Projected | Leaves under it | Existing cards | Capacity at 10/leaf |
|---|---|---|---|---|
| Epic fantasy | 470 | 31 | 115 | 310 |
| Military science fiction | 324 | 4 | 11 | 40 |
| Urban fantasy | 227 | 10 | 45 | 100 |
| Vampire fantasy | 108 | 3 | 10 | 30 |
| Alternate history | 97 | 7 | 25 | 70 |
| Hard sci-fi | 89 | 6 | 20 | 60 |
| New space opera | 67 | 12 | 42 | 120 |
| Classic quest fantasy | 50 | 3 | 10 | 30 |
| Pulp space opera | 16 | 3 | 14 | 30 |
(Plus 512 placed only to the root and 411 only to Science fiction, 133 to Fantasy: authors spread too wide to localize.)
Biggest structural gaps: Military science fiction (4 leaves, 324 books), Urban fantasy / Vampire fantasy (13 leaves, 335 books), Epic fantasy, Alternate history and Hard sci-fi.

## Caveats
- Author-level matching is a proxy: a book's leaf follows what it is about, and prolific authors span leaves. T2 and the branch tiers show where pressure will be, not where individual books go.
- The tree holds only 865 authors, so 53% of candidates have authors the tree has never seen. That is why unmatched is large; the next lever is series-level mapping for the top unmatched authors (`unmatched-top-authors.tsv`).
- Curated map is my judgment on author reputations, no web check; it does not look at individual titles. Genre fields exist only for Tor and Gollancz rows.
- Cards are series-level in the tree, so a series of 10 candidate rows will usually be one card: book counts overstate card counts. Collapse by series before sizing new leaves.
