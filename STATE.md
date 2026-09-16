
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

## 2026-09-13 19:30 — historical-fantasy SPLIT (Gustav: by time period) + intake 70
- historical-fantasy is now an umbrella with 4 attested leaves: gaslight-fantasy (5: Babel, JS&MN, Temeraire, Nights at the Circus, Once and Future Witches), fantasies-of-history (2: Declare, Kingdom of Back), nordic-fantasy (2: Last Light of the Sun, Weaver and the Witch Queen), celtic-fantasy (1: Warrior Bards). New generated portraits 60-63. Commit bcccd42, browser-verified (umbrella shows 4 cards; gaslight leaf 5 works).
- Editions default-dress rule live (commit 720476a): fiction pages auto-apply the edition with most books, first-listed wins ties. Verified on Earthsea (2012 reissue auto-dressed).
- Intake 70: Norstrilia -> future-history. OL 477772 (I Books 2003), 8.0, shows_english_title=true. Drive 1D1ebUi97OfLllaVipb1alOEvGGK_d11T.
- Intake 71 HELD: One Hundred Years of Solitude - magic-realism attested (SFE+Eof) but no cap-safe home (fantasy at 10 children; no umbrella trait fits). Boundary call for Gustav.
- CACHE GOTCHA confirmed again: always verify deploys via index.html?nc=<ts> URL, never the bare directory URL.
- Drive scaffolding backlog: new leaves gaslight/fantasies-of-history/nordic/celtic need works folders + yamls moved from historical-fantasy/works.

## 2026-09-13 19:44 — literary-fantastika umbrella (Gustav option 2) + intake 71 + portrait fix
- New umbrella literary-fantastika (portrait 64, provisional) under fantasy, children: magic-realism (NEW leaf, portrait 65, SFE+Eof attested) + contemporary-fantasy (moved; id unchanged so its deep links survive). Fantasy stays at 10 children.
- Intake 71: One Hundred Years of Solitude -> magic-realism. OL 10499988 (Penguin 1999), 8.5. Drive: literary-fantastika 1J3TAEIJdy6DXBsdQeLk-k08FKzN-6Dxl, magic-realism 1ZDtZIPxOZoCGf2R7iE07dk5sfuRbBTnU, works 1nLlrYk_JxJMM_pefA4vgmYyIJARUjsjA, yaml 10j7-4dXNMr8QtJ1jAWp8XEsavG8QSOVL. Commit c14ccc5.
- BUG FIXED (Gustav report): portraits 60-65 were vertically stretched - my converter cropped 2:3 sources to landscape then resized to portrait. Re-converted without crop, commit f2b6452, remote md5-verified, browser-verified correct proportions.
- progress.json: next=72, added=54. Site 200/1000.

## 2026-09-13 19:58 - intake 72-73 deployed (commit bc97173, 202/1000)
- Our Lady of Darkness (1977, Leiber) -> urban-fantasy (SFE leiber_fritz: modern-setting fantasies modeling urban fantasy). Cover OL 10304918 (Fontana 1978), 8.5. Drive 1aza9i23clvzwVqWoFQC5wlMduaiBVaUE. urban-fantasy now 8 works.
- Replay (1987, Grimwood) -> time-travel-fiction (SFE grimwood_ken: Time Loop fantasy). Cover OL 432217 (Berkley 1986), 8.0. Drive 1wvEx0Xqxze9oNUtg2FOmkro9u8csSZTh. time-travel-fiction now 8 works.
- New Drive folders: urban-fantasy 1aza9i23... wait works folder id in new_folders.json; time-travel-fiction under unplaceable. Both browser-verified (8 fictions each).
- Verification note: lazy-loaded below-fold cover imgs have empty currentSrc in DOM checks - verify via works labels/data instead.

## 2026-09-13 20:13 — book pages inherit fiction-page edition cover (Gustav report)
- renderBook hero = active edition's cover for the book (curEd), else the most-books default edition's cover, else the book's own cover. Versions strip 'on' marker follows the shown hero. curEd tracked in state, reset by render/renderFic.
- Earthsea versions backfilled: every edition cover now appears in each book's versions strip (Wizard 8, Tombs 6, Farthest 7, Tehanu 4, Tales 3, Other Wind 3), edition covers first then prior extras, deduped.
- INCIDENT: first push (55c9239) shipped a duplicate let curBook declaration (already declared later) - broke all JS for ~1 min until fix commit 27a4f64. Root cause: asserted count on my new string but not on pre-existing declaration. Rule: after state-var edits, grep for ALL declarations of the touched identifiers before pushing.
- Verified live: fresh deep link to Wizard book page shows 2012 cover bg (10509685); Bantam-1984 tap then Tombs opens with 368884; versions 'on' follows hero.

## 2026-09-15 15:44 - Utopian fiction / Hopepunk restructure
- Executed Gustav's approved shape with corrected spelling Ecotopian. Utopian fiction stays under Future of Earth fiction and retains its stable id and portrait.
- New branches: Satirical Utopia (1), Secluded Utopias (2), Hopepunk -> Ecotopian (3) + Feminist Utopia (3). No cards mixed into intermediate nodes.
- Generated and visually reviewed five new 2:3 detailed colorful portraits (130-134). Drive hierarchy and nine canonical YAMLs mirrored; retired the verified-empty former Utopian works folder.
- Gate: 122 nodes / 326 works / refs consistent. Deployment verification still pending.

## 2026-09-16 06:41 - intake 290-291 staged
- Intake 290: All the Murmuring Bones (2021, A.G. Slatter) -> evil-deals. Titan describes the O'Malley family's ancestral bargain with the mer, safe ships for one child each generation; its inherited supernatural bargain is the plot engine. Official Titan front selected in one pass.
- Intake 291: American War (2017, Omar El Akkad) -> social-dystopia. SFE grounds its near-future dystopian America in climate change, fundamentalism and a second civil war over a fossil-fuel ban; PRH follows the displaced Chestnut family and the generational social consequences. Official PRH front selected in one pass.
- Local gate: 127 nodes / 375 works / refs consistent. Deployed commit 9b2d534; public HTML byte-identical. Drive STATE/progress and both YAMLs mirrored. Fresh fiction deep links and both official covers pixel-checked.

## 2026-09-16 07:07 - encoded apostrophe route fix
- Hash-route segments are now URI-decoded and normalized through the same slug function as titles. This makes `%27`-encoded and literal-apostrophe links resolve to the canonical `a-wizard-s-...` route instead of falling back to the leaf.
- Commits 30aef6f + 23ed8d0; public HTML byte-identical to 23ed8d0. Fresh browser QA confirmed the encoded Wizard link opens its fiction page and cover correctly. Screenshot /downloads/cloud-browser-20260916-050730.png.
- Fabulation and Alternate history restructures remain on hold pending Gustav's ruling.

## 2026-09-16 07:10 - intake 292-293 staged
- Intake 292 HELD: An American Story (2018, Christopher Priest) grounds closest to Fabulation: SFE says it interrogates rival 9/11 narratives and subverts official appearances; Gollancz centers inconsistent memories, truths and fictions. Fabulation is already at the 10-work cap and its split proposal is with Gustav, so this candidate is not added pending his ruling.
- Intake 293: An Unkindness of Ghosts (2017, Rivers Solomon) -> generation-starships. SFE explicitly sets it on a generation starship many years into its journey; Akashic identifies the HSS Matilda as carrying the last of humanity for generations. Official Akashic front selected in one pass.
- Local gate: 127 nodes / 376 works / refs consistent. Deployment, Drive mirror and pixel QA pending.
