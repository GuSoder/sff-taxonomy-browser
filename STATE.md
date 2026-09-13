
## 2026-09-13 19:09 — Earthsea editions rebuilt (option a: uniform print runs)
- Earthsea editions[] replaced with 8 verified uniform print runs: First US 1968-72 (2 books), Bantam 1984 (3), Atheneum 1990-2001 (3), Simon Pulse 2001 (3), Harcourt 2001 (2), Orion 2002-03 (2), Earthsea cycle reissue 2012 HMH/Saga (all 6), Gollancz Vess 2018-19 (2).
- Data fixes: removed interior title-page cover 13248496 from Wizard versions; replaced Pulse farthest 15235392 with 436610; dropped non-uniform Penguin/Puffin 1971-92 bucket and Bantam/Spectra mixes.
- Deployed commit b9c3078; browser-verified: 2012 edition dresses all 6 cards uniformly (DOM img srcs = 10509685/9070742/10508403/8753482/9055188/9055173); Bantam 1984 dresses 3, dimmed fallback (opacity .32 grayscale) on tehanu/tales/otherwind. Screenshots: /downloads/cloud-browser-20260913-170855.png, -170944.png.
- Sub-series level parked per Gustav.
- OWED to parent: historical-fantasy split proposal (leaf at 10 works) BEFORE applying.

## 2026-09-13 19:17 — Genre swipe disabled on fiction/book pages (Gustav request)
- touchend swipe-to-shift now returns early when curFic>=0 or curBook>=0 (commit 04541d2). Keyboard arrows unchanged.
- Verified live with synthetic TouchEvents: fiction page swipe = no nav; genre level swipe still moves to sibling (#heroic-fantasy -> #sword-and-sorcery).
- GOTCHA: cloud browser served a stale cached copy of the directory URL (Pages max-age=600); verifying fresh deploys needs the explicit index.html URL with a fresh query (?nc=<ts>).
