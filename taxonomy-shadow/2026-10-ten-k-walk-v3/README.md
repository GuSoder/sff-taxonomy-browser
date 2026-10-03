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
- 8,132 works placed, 4,379 cards, 661 leaves, all leaves at 10 or fewer cards.
- 1,937 rows held (holds-by-reason.md lists 1,939; a 2-row difference I did not chase).
- 83 folds onto existing cards. No new seeds in v3; the 7 v2 seeds are unchanged.
- Splits keep the umbrella: the split node stays at 0 direct cards and the children are added.

## Hold categories (rows)
Short form 590 (SHORT-FORM-STORY-OR-NOVELLA 307, SHORT-FORM-STORY-OR-COLLECTION 175, SHORT-FORM-STORY 105, other 3). Children 247. Anthologies and collections about 546 (ANTHOLOGY 230, COLLECTION 221, ANTHOLOGY-OR-OMNIBUS 57, MAGAZINE-ISSUE-OR-ANTHOLOGY 28, others 10 to 18 each). Omnibus 76. Tie-ins 97. Non-fiction and non-speculative about 183. ROMANCE-OUT-OF-SCOPE 43. UNCLEAR-REVISIT 107 (could not pin down from blurb or title; not placed). Other 14 (not-a-book placeholders, duplicate editions, serial episodes, publisher labels).

## Re-home pass: DONE
Mistake: in about 380 cards across the early batches (c001 onward) I named a branch (an umbrella) instead of a real leaf. The autofix script routed those cards to the child with the fewest cards, which is a count-based placement and not a thematic one.
Fix: every card in `rehome-todo.txt` was reviewed against its real post-split location in the tree. Clear misfits were moved to thematic leaves (`m001.txt` to `m006.txt` list the moves, card|new leaf). The earlier 22 dragons-and-courts cards and 12 misfits were moved first. From then on I placed only on real leaf ids.
Honor Harrington (rows 9286, 9287, 9298, 9318, wrongly held as tie-ins) is now one card in captains-and-their-ships.

## Caveats
- Near-fit placements: leaf names are loose and many leaves are full, so some cards sit in a defensible near-fit leaf with room, not the ideal one. Only clear misfits were moved.
- Many cards are named after author batches ("X Standalones", "Author Later", "Author Fantasies"). They are not true series. Re-split by series if a cleaner tree is wanted.
- Placements are often from blurbs or titles only; confidence is low or moderate for many. The title-only tail (rows 9871 to 10068) had no author or blurb and was identified by web search.
- Duplicate or related cards merged: Riftwar (3 names), 1632 / Ring of Fire (4 into 1), Pohl, Renshai, Sword-Dancer, Lyra Selene, Tara Sim, Wit'ch with Wit'ch Fire. Not merged (v1/v2 cards): Sword of Truth (2 names), Semiosis, a possible Damsel card across leaves.
- Doc gaps: no rule for more than 10 sibling leaves; none for moderate-confidence or title-only placements; none for cross-genre series.

## Files
results2.txt (card placements, v3 lines tagged v3), seeds2.txt, splits2.txt, holds3.txt, decided.txt, research.jsonl (blurbs), rehome-todo.txt (the original list of cards to re-home), m001-m006.txt (the re-home moves).
