# Shadow tree v3 (full per-work walk of the 10k list) - COMPLETE
v1 and v2 folders are untouched. v3 layer = results2.txt (all C/+C lines, v3 lines tagged `v3`), holds3.txt (named hold reasons), decided.txt (rows with a decision).
Per-book analysis lives in `book-analysis/books-NNNN.yaml` (250 queue ids per file, block YAML, greppable). Keys: id title author form has_magic is_real_earth setting genre tags confidence source decision note.
Values: has_magic true/false/?; is_real_earth true/false/?; setting earth_now|earth_past|earth_future|invented_world|space|other_planet|multiverse; source = knowledge|ol|web|title_form|title_guess. `rec.py attrs.txt` upserts records. The walk resumes from these records; do not re-research a record whose source is not title_guess.


## Open these first
- `shadow-tree.txt` - the finished tree, human-readable (whole tree: v1/v2 cards plus v3). Leaves show `NEW (n)` with n cards, cards are the `- ` lines.
- `holds-by-reason.md` - every held row (author, title) grouped by named reason, so a category can be vetoed.
- `book-analysis/` - per-book YAML (has_magic, is_real_earth, setting, genre, confidence, source).

## Final numbers
- Every row of the 10k list has a decision: placed, or held with a named reason. Titan rows (about 2,029) were skipped at my judgment and are not counted.
- 8,132 works placed, 4,280 cards, 661 leaves, all leaves at 10 or fewer cards.
- 1,937 rows held (holds-by-reason.md lists 1,939; a 2-row difference I did not chase).
- 128 folds onto existing cards. No new seeds in v3; the 7 v2 seeds are unchanged.
- Splits keep the umbrella: the split node stays at 0 direct cards and the children are added.

## Hold categories (rows)
Short form 590 (SHORT-FORM-STORY-OR-NOVELLA 307, SHORT-FORM-STORY-OR-COLLECTION 175, SHORT-FORM-STORY 105, other 3). Children 247. Anthologies and collections about 546 (ANTHOLOGY 230, COLLECTION 221, ANTHOLOGY-OR-OMNIBUS 57, MAGAZINE-ISSUE-OR-ANTHOLOGY 28, others 10 to 18 each). Omnibus 76. Tie-ins 97. Non-fiction and non-speculative about 183. ROMANCE-OUT-OF-SCOPE 43. UNCLEAR-REVISIT 107 (could not pin down from blurb or title; not placed). Other 14 (not-a-book placeholders, duplicate editions, serial episodes, publisher labels).

## Re-home pass: DONE
Mistake: in about 380 cards across the early batches (c001 onward) I named a branch (an umbrella) instead of a real leaf. The autofix script routed those cards to the child with the fewest cards, which is a count-based placement and not a thematic one.
Fix: every card in `rehome-todo.txt` was reviewed against its real post-split location in the tree. Clear misfits were moved to thematic leaves (`m001.txt` to `m006.txt` list the moves, card|new leaf). The earlier 22 dragons-and-courts cards and 12 misfits were moved first. From then on I placed only on real leaf ids.
Honor Harrington (rows 9286, 9287, 9298, 9318, wrongly held as tie-ins) is now one card in captains-and-their-ships.

## Duplicate-card correction (6:57 PM Oct 3)
The user spotted that Kingkiller Chronicle sat in Wars of Wizards while the original tree already has The Kingkiller Chronicle under bard-hero. I scanned every card name that appears both in the original tree and in the shadow layer (28 names). 23 shadow cards were duplicates of an original-tree card and are now folded onto it; the works stay placed (8,132 unchanged), only the duplicate card is gone: Beautiful Creatures, Incarnations of Immortality, Locked Tomb, Noble Dead Saga, Renshai, Kingkiller Chronicle, Emberverse, Radiant Emperor, Belisarius, Clockwork Dagger, School of Shards, Liaden Universe, Seven Devils, Gap Cycle, Sun Eater, Kane of Old Mars, Troy Rising, Fall Revolution (v3 cards, now `+C` fold lines onto the original card), and The Books of Babel, I Am Legend, The Expanse, Vorkosigan Saga, Lilith's Brood (older v1 cards, removed from the render by `X`/`XS` lines in splits2.txt, which render3.py applies). Left alone, same name but a different work or an original-tree duplicate: Spell Bound (Rachel Hawkins vs F.T. Lukens), Providence (space-navy novel vs Kepnes), The Bridge (Banks vs Breukelaar vs the space-between card), Transition (Iain M. Banks vs Kisner's The Transition), Wormwood Trilogy (the original tree itself has two cards, in alien-invasion-fiction and near-future-first-contact). Cause: I walked each work from its blurb and never checked whether the series already had a card in the original tree. Files: dedup.py (the fix script), render3.py (render with the removal lines; use it instead of the v2 render2.py). Cards are now 4,356, shadow-branch works 7,409.

## Near-name duplicate correction (7:09 PM Oct 3)
Second scan, now by normalized name, near name and author, against the original tree and against other shadow cards.
- Folded onto original cards (18): Sword of Truth -> The Sword of Truth; Riftwar Saga and Riftwar -> The Riftwar Saga; Black Company -> The Black Company; The Divine Cities -> Divine Cities; Rook and Rose -> Rook & Rose Trilogy; Iron Druid -> Iron Druid Chronicles; Deryni -> Deryni Rising; Takeshi Kovacs and Morgan -> Takeshi Kovacs; Greta Helsing -> Dr. Greta Helsing; World of the Five Gods (Penric) -> World of the Five Gods; Amina al-Sirafi -> The Adventures of Amina al-Sirafi; Semiosis (settler copy) -> Semiosis; Sirens of Titan -> The Sirens of Titan; Naamah's -> Kushiel's Legacy; Charles de Lint Newford -> Newford; Nightfall Reichert -> Nightfall Saga; Belisarius Tide of Victory -> Belisarius.
- Shadow cards that duplicated each other and are now one: 1632 series into Ring of Fire (1632); Landover, Jacob's Ladder, Newsflesh, Vatta's War, Black Tide Rising, Freehold, Jill Kismet, Dante Valentine, Imager Portfolio, Spellsong Cycle, Ian Irvine, Ecolitan, Faerie Handmaid, Nantucket Series, Sweep of Stars, Barsoom (same author, same series).
- Left alone, same name or near name but a different work: Damsel (Skye vs Arnold), Spell Bound, Providence, The Bridge, Transition, Drowned World (Chan vs Ballard), Truth series (Cook vs Goodkind), Spin Trilogy (Bannister vs Wilson), Sulien Arthurian (Walton vs Stewart), Eddings (Althalus etc.), Crescent City, Incrementalists, King Rat, Proxima, Combat Command, Time Trials, Asylum Tales, Caine Riordan, Stations of the Tide, Steel Crow Saga, Greta Kelly, Red Rising. A few of these (Stations of the Tide, King Rat, Caine Riordan, Steel Crow Saga) look like the same author and series and need a look.
- Scholomance is a card named for Novik's series but holds two other Novik books; not merged, probably misnamed.
- Wormwood: the original tree card in Alien invasion fiction is the one kept; the shadow layer's Wormwood card is that same card, not a copy.
- Phantom cards removed: 8 names left over from earlier merges (Raymond Feist Riftwar, Renshai Later, Pohl Later Novels, Tara Sim Later, Lyra Selene Fair Folk, 1632 Ring of Fire Evans, Wit'ch Fire) still showed as cards. The render also listed a card twice when two split lists named it. Both are fixed, so the card count falls more than the fold count.
- Known leftover: the leaf Altered selves is defined under two parents (Remade minds and Rewired minds), so it renders twice in shadow-tree.txt (Fools, PKD Maze of Death, Afterparty show twice). Not fixed.
- Works placed 8,132, held 1,937, unchanged. Scripts: dedup2.py, dedup3.py, dedup4.py, render3.py.

## Caveats
- Near-fit placements: leaf names are loose and many leaves are full, so some cards sit in a defensible near-fit leaf with room, not the ideal one. Only clear misfits were moved.
- Many cards are named after author batches ("X Standalones", "Author Later", "Author Fantasies"). They are not true series. Re-split by series if a cleaner tree is wanted.
- Placements are often from blurbs or titles only; confidence is low or moderate for many. The title-only tail (rows 9871 to 10068) had no author or blurb and was identified by web search.
- Duplicate or related cards merged: Riftwar (3 names), 1632 / Ring of Fire (5 into 1), Pohl, Renshai, Sword-Dancer, Lyra Selene, Tara Sim, Wit'ch with Wit'ch Fire; see the near-name correction below.
- Doc gaps: no rule for more than 10 sibling leaves; none for moderate-confidence or title-only placements; none for cross-genre series.

## Files
results2.txt (card placements, v3 lines tagged v3), seeds2.txt, splits2.txt, holds3.txt, decided.txt, research.jsonl (blurbs), rehome-todo.txt (the original list of cards to re-home), m001-m006.txt (the re-home moves).
