# PREP: Modern Albion myth era split - execution plan (DRAFT, no mutation; execute ONLY on relayed user approval)
Served by parent 14:06 2026-10-28. Axis: publication era (explicit, not mechanism). 5/5.

## Structure (split-with-umbrella per SPLITTING.md default)
## Names revised 14:31 per curator phonemsg-01M61B98RPX3310YANCM1ARV96 (both names must signal modern setting standalone)
## Names as SERVED by main 14:31: Classic modern Albion myth / New modern Albion myth (parent owns naming presentation; ids updated to match)
- modern-albion-myth STAYS, becomes umbrella: works: [] (keep the key - verify_local requires it),
  children: [classic-modern-albion-myth, new-modern-albion-myth]. Def gets one line noting the branch.
- New leaf 1: id classic-modern-albion-myth, label "Classic modern Albion myth", parent modern-albion-myth,
  image 838-classic-modern-albion-myth.webp (next free portrait 838)
  definition: "Modern Albion myth's founding generation, first published 1960-1988 - the books
  that first made the old powers of Albion walk in ordinary present-day life. Not Contemporary
  Albion myth (the 21st-century inheritors of the mode). Not Arthur returned (the old powers of
  Albion's land, not Arthur)."
  works: the-weirdstone-trilogy (1960, Boneland-2012 coda disclosed in its yaml), the-dark-is-rising-sequence (1965),
  the-owl-service (1967), the-albion-triptych (1967), greenmantle (1988)
- New leaf 2: id new-modern-albion-myth, label "New modern Albion myth", parent modern-albion-myth,
  image 839-new-modern-albion-myth.webp
  definition: "Modern Albion myth first published 1998 or later - the old powers of Albion alive
  in ordinary present-day life, worked by the generation that inherited the mode. Not Classic
  Albion myth (the 1960-1988 founding generation). Not Arthur returned (the old powers of Albion's
  land, not Arthur)."
  works: king-rat (1998), prosperos-children (1999), the-green-man-series (2018), lanny (2019),
  a-midwinters-tail (2023)

## Steps on approval
1. Two genre.yaml leaf dirs + def/works as above; modern-albion-myth genre.yaml -> umbrella
   (works: [], children, history entry with the approval message id).
2. index.html: add 2 node dicts (same shape as classic-haunted-house node: id,label,parent,
   children,image,definition,status,works arrays with the 5 cards each, moved verbatim from the
   umbrella's works); umbrella node: works->[], children->[the two ids]. Book/card counts must
   stay 2,571 / 5,857.
3. Each of the 10 works yamls: placement_history += re-walk line (root-down path to the new leaf,
   date, approval message id); canonical_genre updated to the new leaf id.
4. Portraits: two new 2:3 no-text originals (838 classic, 839 contemporary) per portrait rules
   (NO PEOPLE preferred, no franchise refs); upload to Drive folder 0ANZA2OU2lCCCUk9PVA, wire
   image fields. Portrait briefs: classic = carved green-man face / standing stone in English
   woodland, weathered mid-century mood; contemporary = modern village street or estate with an
   old-power intrusion (e.g. leaves through tarmac), present-day light.
5. ./verify_local.sh | grep '^OK'; commit; push; deploy poll; live QA: umbrella view shows 2
   branches, each leaf shows its 5 cards, back button behaves (his Sep-22 bug catch - test it),
   card counts, image loads; record guidance; release lease.
6. Report exact membership + counts + live URLs to parent.
