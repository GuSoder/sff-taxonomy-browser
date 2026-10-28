# PREP: Green Man card expansion (series = ONE card rule) - NOT YET EXECUTED
Trigger: parent 2026-10-28 13:59 - "Green Man expansion prep allowed under standing series rule".
No original user message limits the card to Quarry alone (checked all McKenna/Quarry phone_messages:
only Sep 24 shelf listing #10 "The Green Man's Quarry - English Green Man").

## Current card
- id: the-green-mans-quarry, title "The Green Man's Quarry", year 2023, leaf modern-albion-myth
- cover: https://wizardstowerpress.com/wp-content/uploads/TheGeenMansQuarry_300.jpg (300x480, BSFA badge cover)

## Proposed card (pattern: the-dark-is-rising-sequence / the-weirdstone-trilogy)
- id: the-green-man-series, title "The Green Man series", year 2018
- card cover_url = book 1 (Heir), per series-card pattern
- placement_note update: keep existing engine text, extend to series scope:
  "Daniel Mackmain, son of a human man and a dryad, sees the supernatural creatures ordinary
  mortals miss; the Green Man sends him to resolve clashes between people and the uncanny across
  present-day England (Wizard's Tower Press series page). Casebook folklore across 8 novels."
- Sources: https://wizardstowerpress.com/books-2/books-by-juliet-e-mckenna/the-green-man-series/
  + https://en.wikipedia.org/wiki/Juliet_E._McKenna

## Volumes (all covers visually reviewed 2026-10-28 - correct titles, clean publisher art, no
## barcodes/stickers/interiors; downloads in /tmp/gm-covers/)
1. The Green Man's Heir (2018)   https://www.julietemckenna.com/wp-content/uploads/The-Greenmans-Heir-cover-651x1024.jpg (651x1024)
2. The Green Man's Foe (2019)    https://www.julietemckenna.com/wp-content/uploads/The-Green-Mans-Foe-front-cover-657x1024.jpg (657x1024)
3. The Green Man's Silence (2020) https://www.julietemckenna.com/wp-content/uploads/GMS-cover-for-web.jpg (397x618)
4. The Green Man's Challenge (2021) https://www.julietemckenna.com/wp-content/uploads/GM4-ebook-cover-600.jpg (600x959)
5. The Green Man's Gift (2022)   https://www.julietemckenna.com/wp-content/uploads/GM5-front-cover-600.jpg (600x959)
6. The Green Man's Quarry (2023) https://wizardstowerpress.com/wp-content/uploads/TheGeenMansQuarry_300.jpg (300x480; BSFA Best Novel 2023 badge is printed on the actual cover - keep)
7. The Green Man's War (2024)    https://www.julietemckenna.com/wp-content/uploads/GM7-ebook-640x1024.jpg (640x1024)
8. The Green Man's Holiday (2025) https://www.julietemckenna.com/wp-content/uploads/GM-8-front-cover.jpg (1563x2500)

## Per-book engine uniformity (publisher blurbs via julietemckenna.com book pages)
- Heir: dryad's son, sees the supernatural; Green Man calls him to handle threats (series page)
- Foe: historic-house renovation, a nix; aided by Finele Wicken, a Swan Maiden (themondayreview)
- Silence: Fens case with Fin (themondayreview)
- Gift: Snowdonia, boy babbling of fairy feasts; wise women ask Dan to investigate
- Quarry: black big-cat deaths investigation (thomaswrightson review)
- War: "someone has decided to put a stop to this interference once and for all" - arc escalation
- Holiday: (2025; uniform series per publisher listing)
Engine invariant: contemporary-folklore casebook on inherited dryad blood. Leaf membership stable.

## Execution checklist (when parent says go)
1. Rename works yaml the-green-mans-quarry.yaml -> the-green-man-series.yaml; update title/year/
   cover_url + add books[] (8 vols, shows_english_title true) + placement_note + sources
2. genre.yaml works list: the-green-mans-quarry -> the-green-man-series
3. index.html: same swap in the flat nodes entry (books count 1 -> 8)
4. ./verify_local.sh | grep '^OK'; commit; push; deploy poll; live QA cache-busted #modern-albion-myth
   (card title in DOM, img complete/naturalWidth after 4-8s settle, recheck -M races)
5. browser_guidance record + release lease; report to parent
