
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
- Local gate: 127 nodes / 376 works / refs consistent. Deployed f467527; public HTML byte-identical. Drive STATE/progress and YAML mirrored. Fresh fiction-page pixel QA passed.

## 2026-09-16 07:41 - intake 294-295 staged
- 294 Ancestral Night -> complete current 3-book White Space card in new-space-opera: Ancestral Night, Machine, The Folded Sky. SFE calls it interstellar Space Opera with forerunner artefacts and post-scarcity culture; Simon & Schuster centers salvagers, alien wrecks and interstellar war. Coordinated official S&S fronts selected in one pass.
- 295 Angel Mage -> alternate-history-fantasy. HarperCollins places it in an alternate European world of musketeers and angelic magic; Allen & Unwin specifies an alternative seventeenth century with controlled angel summoning. Actual magic in reworked early-modern Europe makes Alternate history fantasy closest. One-pass OL 8792047.
- Gate 127 nodes / 378 works / refs consistent. Deployed content commits 794d270 + 4bd9bcd; public HTML byte-identical. Drive STATE/progress and both YAMLs current. Pixel QA passed for Angel Mage and corrected complete White Space grid.

## 2026-09-16 08:12 - intake 296-297 staged
- 296 Annex -> alien-invasion-fiction. SFE says high-tech aliens invade, incapacitate adults and occupy the city; Orbit centers Violet's fight to take it back. Official Hachette front selected.
- 297 Anno Dracula 1999: Daikaiju -> complete six-book Anno Dracula card in vampire-fiction. SFE grounds the alternate world in Dracula marrying Victoria and its vampire history; Titan calls Daikaiju part of the alternate-history vampire series. Official Titan fronts plus one-pass OL 404092 for Dracula Cha Cha Cha.
- Gate 127 nodes / 380 works / refs consistent. Deployed 665770a; public HTML byte-identical. Drive STATE/progress and both YAMLs mirrored. Fresh Annex page and complete six-book Anno Dracula grid pixel-checked.

## 2026-09-16 08:49 - intake 298-299 staged
- 298 Anthropocene Rag -> technomorphosis. SFE/Tor describe nanotech-remade America and emergent AIs recreating human myths; technology reshapes landscape, minds and culture. Official Tor front.
- 299 Architects of Memory -> complete two-book Memory War card in new-space-opera. SFE calls it Hard SF Space Opera with military elements across corporate-dominated inhabited space, ancient alien weapons/civilization; Macmillan confirms alien war and corporate intrigue. Official Macmillan fronts.
- Gate 127 nodes / 382 works / refs consistent. Deployed efbad07; public HTML byte-identical. Drive STATE/progress and both YAMLs mirrored. Fresh Anthropocene Rag page and complete two-book Memory War grid pixel-checked.

## 2026-09-16 09:01 - Fabulation split executed by Gustav ruling
- Fabulation is now umbrella-only, stable #fabulation route retained, with Gustav's children: Books in Books (7 after held intake 292 An American Story) and Worlds in flux (4).
- Books in Books definition: fabulations where a book, journal, manuscript or story artifact enters and destabilizes the world. Worlds in flux: places, histories, identities or causal world stay visibly mutable. Existing ten cards distributed exactly per Gustav's ruling; An American Story added to Books in Books from the held queue item.
- New detailed colorful 2:3 portraits 141 and 142 generated, selected and visually inspected. Gate 129 nodes / 383 works / refs consistent. Deployed b468ba8; public HTML byte-identical. An American Story YAML mirrored to Drive. Both new leaf pages and portraits pixel-checked live.

## 2026-09-16 09:20 - intake 300-301 staged
- 300 Ariosto -> new Renaissance fantasy leaf under Period fantasy. Hachette anchors an alternate Italian Renaissance federation and the historical poet/Medici court, while Ariosto's magical New World fiction reflects that politics. New portrait 144 generated and inspected.
- 301 Armed in Her Fashion -> new Medieval fantasy leaf under Period fantasy. SFE/PW anchor 1328 Flanders and the siege of Bruges, with revenants, chimeras, shapeshifters and supernatural Hell woven into documented politics/religion. New portrait 143 generated and inspected.
- Gate 131 nodes / 385 works / refs consistent. Deployed c079718; public HTML byte-identical. Drive STATE/progress and both YAMLs mirrored. Both new leaf portraits/cards pixel-checked live.

## 2026-09-16 09:50 - intake 302-303 held/skipped
- 302 Around the World in Eighty Days skipped as non-speculative. SFE explicitly says it is not SF because Verne used travel arrangements then existing and modeled Fogg's route on a real journey; Simon & Schuster lists only boat, train, carriage and elephant travel.
- 303 Ascent held for Gustav's Alternate history split ruling. Penguin describes a fictional Soviet fighter pilot/cosmonaut inserted into the real Korean War and Space Race; independent review confirms its counterfactual Soviet Moon landing. This fits the proposed Counterfactual history child, but the parent leaf is capped at 10 and restructure remains held.
- No site mutation. Progress next=304, processed=304, added=243.

## 2026-09-16 09:58 - Medieval fantasy renamed Autumn Kingdoms
- Per Gustav ruling, node id/label is now autumn-kingdoms / Autumn Kingdoms. Definition: 14th-century Europe before the Black Death, using Huizinga's autumn-of-the-Middle-Ages framing and leaving room for future Plague fantasy sibling.
- Armed in Her Fashion remains the sole member. Existing portrait 143 retained byte-for-byte as explicitly requested. #medieval-fantasy redirects to #autumn-kingdoms.
- Commit 618f732; gate 131 nodes / 385 works / refs consistent. Deployment and screenshot pending.

## 2026-09-16 10:21 - intake 304-305 staged
- 304 At the Back of the North Wind -> gaslight-fantasy. Penguin anchors a Victorian fairy tale in mid-19th-century working-class England and an ethereal parallel country reached via North Wind spirit. OL 8245161.
- 305 Atlan -> complete four-book Cija/Atlantis card in sword-and-sorcery. SFE describes imperial conflict, quasihumans, sex, sorcery and garish mad scientists amid collapsing Atlantis. Four one-pass fronts; partial official status.
- Gate 131 nodes / 387 works / refs consistent. Deploy/Drive/QA pending. Sword and sorcery now 9.
