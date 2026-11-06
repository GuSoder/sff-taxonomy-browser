
## 15:57 - intake 150-151 wired
- 150 Beloved (Morrison 1987) -> ghost-story (6 works). Knopf 1987 first jacket 9780394535975. No SFE/EoF entry - content-grounded haunting call, vetoable. yaml 139ZdNilCfhytcbetYjtXt4Ci5fVhnkLZ (ghost-story works 1n6uuqVgo59fSh3_JBOutYzGOPGMzk82d).
- 151 Black Easter (Blish) -> dark-fantasy (3 works), 2-book card w/ The Day After Judgment. Penguin 1972 9780140034165 + Penguin 1975 id 9396106 (id-form resolves fine). yaml 1wMUvNhzNJ7AQ5MRcfhxjC6xfuIurgamB (dark-fantasy works 1OCABc_9OpE84FHMJkuni-4dIS1VuXfSB).
- Commit d016451 pushed, 84 nodes/261 works, gate OK, deployed verified, both deep links pixel-verified.
- STALE DUP on Drive: dark-fantasy folder 1xdDB1T5nwVFvVxy_4tUNIta6YMbpraoC under 1cYnxNT39GiqhaUMG28UskIgBx59aq1u3 (only banner+portrait, no works; live = 1w0-a6zOqY86AuP9Pt7zcneozwnTWf0vm). the curator's call to trash.
- Next wake: intake 152 (Black Leopard, Red Wolf) + 153; Wheel of Time 15-book single-pass (next audit target).

## 16:36 - intake 152-153 wired
- 152 Black Leopard, Red Wolf -> series card "The Dark Star Trilogy" (2 books) in sword-and-sorcery (6 works). No SFE/EoF entry; wiki says Dark Fantasy but site dark-fantasy is real-Earth branch; S&S mercenary-band call is judgment, vetoable. PRH pair 9780735220171/9780735220201. yaml 1N2LdWk4xwxD8DR6TjqEYQ1ZWkaLnc3GB (s&s works 1_-o2w0M9wgq6wLxDPzlpd5CNUUwDzp9I).
- 153 Black Sun -> series card "Between Earth and Sky" (3 books) in political-fantasy (4 works). SFE roanhorse_rebecca grounded (polder, pre-contact indigenous world, 2025 Hugo series). Picacio Saga set 9781534437678/9781534437739/9781534437708. yaml 1Exl1BA0iT1P_jX8QtSEPFq-bLjkc_wFI (political works 1Is2XoV8c84gOQNTrGHbm-oiUCRt6qgLy).
- Commit 7856caa pushed, gate OK, 84 nodes/263 works, deployed grep + both deep links pixel-verified.
- Next: 154-155; Wheel of Time 15-book single-pass still queued as next audit target.

## 16:52 - audit fix: Wheel of Time 15/15 covers
- hard-magic Wheel of Time card: all 15 books got cover_url. Tor Darrell K. Sweet art set. Card cover = Eye of the World first-ed art (isbn 9780312850098), shows_english_title=true (was id 182341, false).
- Sources: isbn form for New Spring 9780765306296, EotW 9780312850098, Crown of Swords 9780312857677, Winter's Heart 9780312864255, Knife of Dreams 9780812577563 (Tor pb; hc 9780765310538 is a title-page scan on OL, rejected), Gathering Storm 9780765302304, Towers of Midnight 9780765325945, Memory of Light 9780765325952; id form for Great Hunt 182352, Dragon Reborn 603239, Shadow Rising 603240, Fires of Heaven 603821, Lord of Chaos 182398, Path of Daggers 182462, Crossroads 604208.
- Rejected: French/German editions, audiobook CD scan (KoD 871816), green binding scan (WH 5021142), barcode-sticker library scans (GS/ToM id-forms), tiny New Spring 886234.
- GOTCHA: first screenshot showed broken images because OL generates -M sizes on first hit - curl the -M URL once (or wait) before pixel-verifying. Direct-load the image in the browser tab to warm it.
- Commit 670e446 pushed, gate OK, deployed grep + pixel-verified (card hero/grid, knife-of-dreams, new-spring).
- Next: intake 154-155; then Oz 14-book single-pass (next audit target).

## 16:59 - intake 154-155 wired
- 154 Blood Music (Bear 1985) -> singularity-fiction (2 works). SFE bear_greg: grey-goo hive-mind posthuman transcendence. Arbor House first 9780877957201. yaml 1HoRrDQkpiKOGIWGF5OsMOEBLuTfqJa26.
- 155 Camp Concentration (Disch 1968) -> totalitarian-dystopia (7 works). SFE disch_thomas_m: near-future US camp, intelligence drug. Panther 1969 9780586028469. yaml 1m7mxHt16c6XqxX2zOBNOl_pEi_LZaDKl.
- Commit 71b2e0f pushed, gate OK, 84 nodes/265 works, deployed grep + both deep links pixel-verified. OL -M sizes warmed before screenshot (works).
- Next: 156-157; Oz 14-book single-pass audit fix.

## 17:11 - audit fix: Oz 14/14 covers
- portal-fantasy Oz card: all 14 Baum books got cover_url; card cover = 1899 first edition Denslow art (archive.org wonderfulwizardo00baumiala), shows_english_title=true (was id 107689, false).
- OL id-form: Marvelous Land 12648656, Ozma 12648657, Dorothy+Wizard 12648659, Road 8243922, Tik-Tok 8243277, Scarecrow 431586, Lost Princess 854819, Magic 14919873. archive.org /services/img/: Wizard (wonderfulwizardo00baumiala), Emerald City (TheEmeraldCityOfOz), Patchwork Girl (bwb_Y0-AEF-389), Rinkitink (rinkitinkinoz00baum), Tin Woodman (tinwoodmanofoz0000lfra), Glinda (glindaofoz0000unse).
- NEW SOURCE WIN: archive.org advancedsearch (title+creator+year-range) -> /services/img/<id> gives original first-edition scans when OL only has modern reprint junk. Placeholder icon PNG (3777 bytes, 320x220) = item has no cover image, reject.
- Rejected: title-page-only scans, Dover coloring book, omnibus reprints, Prince Classics? (pg_10209395 actually OK but patch3 first-ed better), washed-out 1473369.
- Commit 799c9fb pushed, gate OK, deployed grep + pixel-verified (card hero/grid, glinda deep link).
- Browser: released L-z2azx5..., acquired L-n74xn732hus677xtagdyimk44m (config-c, expires 19:10Z).
- Audit done: OD 18, Dresden 17, Elderlings 16, Vorkosigan 16, WoT 15, Oz 14. Next biggest: Pern 13, Vampire Chronicles 13 (tie), Barsoom 11, Culture 10.
- Next wake: intake 156-157 + Pern or Vampire Chronicles single-pass.

## 17:52 - intake 156-157 + preload feature
- 156 Conan -> sword-and-sorcery (7 works), 12-book Lancer/Ace card, Frazetta covers. Card cover = Conan 1967 (6614295). yaml 1HBhGbXNsn43mbJiH5-DBeTUt63x9beel.
- 157 Crash (Ballard 1973) -> soft-science-fiction (4 works). US pb painted cover id 6484321. yaml 1YGH72rIkGU_zciyy5oPwVB7StpmeDI1n.
- FEATURE (the curator 17:47 directive): renderFic now preloads all book covers (M+L) + edition covers on fiction entry; verified: Conan fiction -> Conan of Aquilonia hero painted ~instantly. Commit ab1c69e.
- Commits: 7cd46c6 (156-157), ab1c69e (preload). 84 nodes/267 works.
- Next: 158-159; Pern or Vampire Chronicles 13-book pass.

## 18:09 — intake 158-159 + preload fix (the curator bug report)
- the curator report (via parent 18:00): tapped into Road to Oz, back, whole Oz fiction reloaded on iPhone.
- ROOT CAUSE: my preload created unreferenced `new Image()` objects -> iOS Safari GCs them (memory cache eviction); desktop Chrome keeps them, which is why my 17:53 verification passed. Compounding: archive.org /services/img serves Cache-Control max-age=300, so HTTP cache expires in 5 min; OL is long-lived. Net: on iOS, Oz's 6 archive.org covers (and any stale OL) refetched on back nav.
- FIX (commit 4feddf8): persistent `ficPreload=[]` store; renderFic clears it and pushes every preloaded Image (books M+L, editions M); render(id) (leaf/home = leaving the fiction) clears it. References held exactly for the fiction's lifetime per the 17:47 directive.
- Verified deployed: instrumented run (performance resource timing, transferSize>0) — Oz fiction open -> Road to Oz book -> back = ZERO network transfers for any cover host. Screenshot saved. Caveat reported to parent: cloud browser is desktop Chrome; asked the curator to retest on iPhone.
- 158 Darker Than You Think (Williamson 1948) -> supernatural-fiction (9). Cover: Fantasy Press 1948 first via archive.org /download/.../page/cover.jpg (872x1317). YAML 1PgRdRk56JRRngzANVl_i6Fq2WJAFN4TL.
- 159 Davy (Pangborn 1964) -> post-apocalyptic-fiction (9). Cover: St Martin's 1964 first (Finegold stained glass), OL id 929120. YAML 1PQWJ_W23CcLK2-_rnUPsJDN3pfztd4Fs.
- Commits: 2249158 (books), 4feddf8 (preload fix). 84 nodes/269 works. progress.json next=160, added=128.
- NEW COVER URL FORM: archive.org /download/<id>/page/cover.jpg gives high-res first-edition scans (vs /services/img small thumb + max-age=300).
- supernatural-fiction works folder: 1pNP7CO7SwQwEneqlLKJcOkXe9Ck9sCuq; post-apocalyptic-fiction works folder: 1bV-ybRXZ1qZF5R3KC2lJXQM4t9ZyJoAs.
- Next wake: intake 160-161 + Pern or Vampire Chronicles 13-book single-pass.

## 18:26 — intake 160-161
- 160 Flatland (Abbott 1884) -> NEW LEAF mathematics under hard-sf (5th child, room). SFE abbott_edwin_a: "a study in Mathematics and Perception"; SFE Mathematics theme attests the label (not provisional). Portrait 89-mathematics.webp generated (oil 2:3, flat figures + Sphere + hypercube), 640x960 straight resize. Cover: Seeley 1884 first-edition wrapper via archive.org /download/.../page/cover.jpg. Drive: leaf folder 1EuBuRvOarOkNewCUNTXlVPi35L_iD9y8, works 1TB9MQmvJ-lYLlly0QHHlUxXB8NEHGVH-, portrait.png 14A1nfwbbzydj2M4keS20ri5_1fFh-g6L, yaml 1ViG1F-t5cXpnmyBFCo47C9Wk-8Vih7rT.
- 161 The Locked Tomb (Muir) -> science-fantasy (8 works), 3-book Ninth card (Gideon/Harrow/Nona), Tommy Arnold Tor.com covers via OL isbn form (9781250313188/9781250313218/9781250854117). SFE muir_tamsyn: "Equipoise between Sword and Sorcery and Space Opera". yaml 1Bxx6PM2k1ER4aZh5qQR1BAX65p4FJI2h.
- Commit 039d3d2 pushed, 85 nodes/271 works, gate OK, deployed grep + both deep links pixel-verified. -M sizes warmed with -L (302 alone doesn't generate).
- NOTE: two STATE.md files exist - /home/sandbox/STATE.md is my live log since 15:57; /home/sandbox/intake-lists/STATE.md ends 15:47 (older canonical). Wake prompt points at the old path.
- Next wake: intake 162-163 + Pern or Vampire Chronicles 13-book single-pass (deferred this wake - preload fix + new-leaf work consumed the cycle).

## 18:38 — preload fix v2 (iOS still failed) + Pern 13/13 + wake prompt fixed
- the curator retest (18:31): Oz STILL reloaded after back on iPhone despite ficPreload retention. Root cause deeper than Image-object GC: iOS Safari also discards DECODED bitmaps for off-DOM/evicted images and every back-nav rebuilt the grid with fresh <img> nodes (opacity:0 until 'ld' load event) — re-render itself is the flash. Fix that survives this: keep the DOM.
- FIX v2 (commit 85ec19b): ficShelf. renderBook moves the fiction grid's live child nodes into a referenced off-DOM div before overwriting content; back.onclick reattaches the SAME nodes (listeners, loaded imgs, 'ld' classes, edition-dress state intact) and restores title/crumb/count/hint/hero/scroll/hash — no re-render, no new img elements, no fade, no refetch. renderFic/render() null the shelf (fresh entry / leaving the fiction). Fallback to full renderFic if no shelf.
- Verified deployed: Oz open -> Road to Oz -> back = 0 network transfers, 14/14 cards restored already-complete with ld, no refade. Deep-link boot to the-road-to-oz then back also restores the 14-card grid. Caveat: still desktop Chrome; iOS reasoning — no re-render happens at all, so eviction can't bite: nothing is re-requested or re-decoded. the curator to retest.
- Wake prompt updated per parent: points at /home/sandbox/STATE.md, stale Gormenghast/Triffids backlog text dropped.
- PERN 13/13 (commit 794fae6): painted picks — Dragonflight id 10306696, Dragonquest id 12077053, White Dragon id 207388 (Whelan), Dragondrums id 11882293, Moreta id 206957, Nerilka id 5921330 (Herder), Dragonsdawn isbn 9780345362551, Renegades archive.org renegadesofpern0000anne (1990 UK painted, OL only had audio/placeholder), All the Weyrs id 5921258, First Fall id 366221, Dolphins id 538388, Masterharper id 208173, Skies isbn 9780345434685. Card cover unchanged (9289913 Ballantine red Dragonflight, title visible). All 12 OL -M variants warmed 200. Pixel-verified card page.
- Audit done: OD 18, Dresden 17, Elderlings 16, Vorkosigan 16, WoT 15, Oz 14, Pern 13. Next: Vampire Chronicles 13, Barsoom 11, Culture 10.
- Next wake: intake 162-163 + Vampire Chronicles single-pass.

## 19:12 CEST — Technofantasy leaf + swipe feature, both shipped & verified live
- Technofantasy leaf (6686aa2): under Fantasy > Fantasy Realms (SFE theme "technofantasy" = EoF-coined). Moved from science-fantasy: The Locked Tomb, A Voyage to Arcturus, The Little Prince (my call: fable magic = actual magic, vetoable). Kept in science-fantasy: Barsoom, Pern, Lord of Light, Riverworld (tech-dressed-as-magic), The Time Quintet (my call: tesseract science spine despite Mrs W's, vetoable). No image yet — TWO portrait variants generated, awaiting the curator's pick.
- Swipe feature (e499ade): horizontal swipe on book pages moves prev/next within the fiction; shelf preserved via fromGrid guard in renderBook.
- Deployed verification (browser, fresh ?v=): Oz book page — Road to Oz →L Emerald City →L Patchwork Girl →R Emerald City →R Road to Oz; back → grid 14/14 cards, 14/14 imgs complete (shelf intact after swipes). #technofantasy renders with 3 fictions (screenshot 171225), Locked Tomb page shows new breadcrumb Speculative fiction › Fantasy › Fantasy Realms › Technofantasy (171234).
- Next: parent report w/ portraits A/B; then wake work = intake 162-163 + Vampire Chronicles cover pass (13 books).

## 19:21 CEST — intake 162-163 (Grendel, Grimus)
- 162 Grendel (Gardner 1971) -> mythic-retelling (6 works, room). SFE gardner_john_2: "recasts the Beowulf legend from the Monster's point of view". Cover: Ballantine Nov 1977 (OL id 9948473), iconic flat monster-with-skull art. Photos (Knopf 1st, Ballantine 73) excluded.
- 163 Grimus (Rushdie 1975) -> magic-realism (4 works, room). SFE rushdie_salman: "a Fabulation (like all his novels see also Magic Realism)". Cover: PRH 9781784878924, 2025 Vintage Classics golden-bird-over-Caf flat illustration. Photos (Gollancz 1st, Modern Library, Panther 77 painted-but-photo) and title-page scan excluded.
- Commit 9dcab98 pushed, gate OK, 273 works. Deployed grep + both deep links pixel-verified (breadcrumbs correct). Yamls: grendel 1jrHiql6XRkeqVlqYOj7IA0hPwv-3srJX, grimus 1LLUzF2BQXoMX9QXzlmI66k2oVOyQjH-Z. progress next=164 added=132.
- NOTE: the only painted Grimus (Panther 1977 white-bird-over-desert) exists online only as a photo of a physical copy - disqualified per flat-art rule; if a flat scan ever surfaces it's an upgrade candidate.

## 19:39 CEST — veto + portrait + Vampire Chronicles 13/13
- Little Prince veto (76e29e8): moved technofantasy -> animal-fantasy, deployed + pixel-verified (breadcrumb ... > Animal fantasy). Technofantasy = 2 fictions (Arcturus, Locked Tomb).
- Portrait A wired (ac965b4): 90-technofantasy.webp 640x960, leaf image live + verified. Drive: folder 1JGuZa7cgiEIbkniQnr84CJj4IsJDQo9P under fantasy-realms 1bTFkwsQHU7Wfk02OuvziYjffOArGpDHg, works 1eTRKwyMr6UMBiUs25jHRDIiNZi7mSsYi, portrait.png 1UmTkzER-7z06ltsxZE58e125WA7K1iR0.
- VAMPIRE CHRONICLES 13/13 (b2b02b0 + e1a831e): Interview 15092741 (RH 2004 blue corridor), Lestat 14843170 (Ballantine 2014 red/gold lion filigree), Queen 10461359 (Sphere 2008 red silk gold flames), Body Thief 15091119 (1994 prone body), Memnoch 8443562 (Ballantine 97 red devil emblem; first pick 8443529 was an ex-library scan w/ sticker - swapped), Armand 10701753 (Ballantine 99 gothic window), Merrick 15091115, Blood and Gold 10703232 (Knopf 2001 Marius painting), Blackwood 12630763 (Ballantine 2003 corridor), Blood Canticle 6403780 (Knopf 2003 Renaissance painting detail), Prince Lestat 11018257 (mansion), Realms of Atlantis 10461336 (cyan), Blood Communion 10701621 (black/gold). All English, flat art. Deployed: 13/13 markers in live HTML; card page + Memnoch book page pixel-verified. All -M warmed.
- Audit done: OD 18, Dresden 17, Elderlings 16, Vorkosigan 16, WoT 15, Oz 14, Pern 13, VC 13. NEXT: Barsoom 11, Culture 10.
- Next wake: intake 164-165 + Barsoom pass.

## 20:00 CEST — social-dystopia split + portrait A + Gulliver/fantastic-voyage
- Split (63ec8bc, the curator-approved): social-dystopia renamed "Social dystopian future" (id unchanged, portrait kept, 6 works); new leaf social-dystopia-modern "Social dystopia" under modern-day with Lord of the Flies, The Power, Naked Lunch, Atlas Shrugged (4 works). Verified live both pages.
- Portrait A wired (9db9e95): 91-social-dystopia-modern.webp, pixel-verified on leaf.
- 164 Gulliver's Travels (dd70526): NEW LEAF fantastic-voyage under SF > Historical (7 children now). SFE fantastic_voyages names Gulliver (1726) as important Proto SF fantastic voyage; no magic -> SF side. Cover: Puffin Classics 1997 flat scan via archive.org gulliverstravels00jona_0 (2476x3840, giant + Lilliputian scaffolding scene). Drive: leaf folder 1JmeUUIgI6UcfLYwcPzshGA1htpm2GEwH, works 1ou2OuKj4mEzpjTGHL3fn_Wje0YiQNv_X, yaml 1K1gq5aX_cv--99DGWNChlqoaLBuBKD2r. Leaf imageless until the curator picks portrait (A = giant bound on beach at dusk; B = Laputa flying island over coast).
- 165 Deathly Hallows = duplicate (Harry Potter card, contemporary-fantasy, 7 books). progress next=166, added=133.
- NOTE: duplicate 'historical' Drive folders exist (10QxaUcGEt2wUxnQNj_Pgeof4cp6IPT6F used/recorded vs 18AVW1W4VHlu5C3vyuZnCjtcJ2HLoAD6p) - flag for the curator's trash call.
- Next wake: intake 166-167 + Barsoom 11-book pass.

## 20:04 CEST — Barsoom pass deferred to next wake
- Barsoom card (science-fantasy): 11 books, ALL missing per-book covers; card cover = OL 11481174 (Princess).
- First OL sweep weak: no work-key hits for A Princess of Mars / Warlord / Chessmen / John Carter via title-prefix search; thin translated/self-pub candidates elsewhere. /tmp/bars/bars_cands.json + /tmp/bars/img hold the 20 downloads.
- NEXT-WAKE STRATEGY: skip OL search; go straight to archive.org advancedsearch per title + known painted editions: Ace 1960s (Frazetta/Krenkel art), Doubleday 1970-71 set (Frazetta), Del Rey 1979+ (Whelan). ISFDB title pages list editions+covers if needed. Single pass per the curator.
- Pending portrait picks with the curator: social-dystopia-modern DONE (A wired 9db9e95). fantastic-voyage A/B sent 20:02, awaiting pick (leaf imageless until then).
- Next wake: intake 166-167 + Barsoom pass (strategy above).

## 20:22 — Fantastic-voyage portrait B + Barsoom 11/11
- Portrait B (Laputa) wired as 92-fantastic-voyage.webp (4766ca8), pixel-verified; portrait.png to Drive 1GZ34POp3JUsxpyqPjqOxxSKhmF6bUxoR. Reported 20:12.
- Barsoom DONE (fc093ce): all 11 books got cover_url. 10 = archive.org flat scans (1963-64 Ballantine painted: princessofmars0000edga_b7c1, godofmars0000unse [dark but clean; better-art copy had library stickers], warlordofmars0000edga_y3z3, thuviamaidofmars00edga [1973 painted, replaced juvenile-adapted ed], chessmenofmars0000edga_e5d9, fightingmanofmar0000edga_h4r5, swordsofmars0000edga, syntheticmenofma0000edga_d4y4, llanaofgathol0000edga) + mastermindofmars0000edga (1928 first-ed RED CLOTH, no art — only clean copy; flagged swap-able) + John Carter of Mars = OL 6698861 (painted Llana/JC omnibus cover, -M warmed 200).
- Deep-link format learned: #<leaf-id>/<work-slug>/<book-slug>. Verified #science-fantasy/barsoom (grid) + .../thuvia-maid-of-mars (book page) live.
- Archive.org Burroughs lending-scan pattern confirmed: <title>0000edga[_suffix]; search "title burroughs" AND mediatype:texts.
- NEXT AUDIT: Culture 10 (Iain M. Banks). Then remaining <10 series.
- Intake resumes at candidates 168-169 next wake (progress.json next=168).

## 20:43 CEST — Supernatural fiction four-way split shipped, portraits awaiting picks
- the curator-approved structure (aac43a3): Supernatural fiction now has four stable child leaves, all imageless until portrait picks: ancient-tormentors (4: It, Darker Than You Think, Master and Margarita, Rosemary's Baby), evil-deals (2: Melmoth, Dorian Gray), surreal-afterlife (2: Third Policeman, Out of Body), fungal-horror stable ID renamed/displayed as Eldritch Fungi (1: Mexican Gothic).
- Gate OK (92 nodes/274 works); committed-blob assertions and deployed-HTML parse passed.
- Generated TWO 2:3 oil-style portrait variants per new leaf, visually inspected all eight. Sheets ready: /downloads/ancient-tormentors-sheet.jpg, evil-deals-sheet.jpg, surreal-afterlife-sheet.jpg, eldritch-fungi-sheet.jpg. Parent report/picks next. No portraits wired yet.

## 20:59 CEST — four approved Supernatural portraits live
- the curator approved recommendations: Ancient Tormentors A, Evil Deals A, Surreal Afterlife B, Eldritch Fungi A.
- Wired 93-ancient-tormentors.webp, 94-evil-deals.webp, 95-surreal-afterlife.webp, 96-eldritch-fungi.webp at 640x960 straight resize; commit 81d0165. Gate OK, committed-blob assertion and deployed-HTML parse passed; all four live leaf pages pixel-verified.
- Full-res portrait.png archived in new Drive leaf folders under supernatural-and-dark-fiction: ancient-tormentors 1uBZBF8NAWMe5Iv8O3gFEJoIBBHhDO3Ll (portrait 1VqxNfl_EZQtLDlfxj-fhMg-1h8GVc_Ac); evil-deals 1ZAwbfXjc74R_Hlev3VHO7CtKCpV9aRgj (portrait 1ZHLzDIi8SRueRe39bE0pf6Go5L505zCc); surreal-afterlife 1_JwtIqe0yVTbGi6ojBGRNCJ0Z2KCz2B7 (portrait 13Dn-FGLNzoxphxopiJbYahiID0BXemAy); fungal-horror 1D4l0bhaUF8xhP-5atgDjNLAPRYg2cg3q (portrait 1L_fvH3XCBymSVf7q0yvwsEdD3CbvppYa). Each has works/; new_folders.json updated.
- Next scheduled work unchanged: candidates 168-169 are Harry Potter duplicates; mark skipped, then Culture 10 cover audit.

## 21:17 CEST — intake 168-169 duplicates + Culture 10/10 covers
- Intake 168 Prisoner of Azkaban and 169 Sorcerer's Stone are duplicates of existing Harry Potter 7-book fiction card in contemporary-fantasy; progress next=170, processed=170, added remains 133.
- CULTURE audit wired (commit pending deploy check): all 10 books got one-pass OL cover picks: Consider Phlebas 6872572 (also replaces card cover; English title visible), Player of Games 44077, Use of Weapons 6797757, State of the Art 941423, Excession 8775183, Inversions 13334421, Look to Windward 476421, Matter 1174791, Surface Detail 6672209, Hydrogen Sonata 8666960. All flat front art, English titles; mix of classic painted and newer colorful designs selected for beauty. Gate/committed blob passed; pushed. Pixel/deploy verification and parent report next.
- 33b05db deployed HTML confirmed 10/10; Culture fiction grid and Use of Weapons detail page pixel-verified. Parent report sent with screenshots.

## 21:43 CEST — Urban fantasy four-way split + branch rename
- the curator-approved split shipped (commit recorded in git): Urban fantasy is now a pure imageless parent with stable child IDs: fae-founders (3: War for the Oaks, October Daye, Dresden Files), paranormal-bricks (3: Neverwhere, Great Cities, Man Who Was Thursday), publicly-paranormal (1: Simon Canderous), modern-goth (2: Conjure Wife, Our Lady of Darkness). Four A/B portrait sheets generated and visually inspected, pending the curator picks; no child portrait wired.
- Renamed label Supernatural and dark fiction -> Supernatural dark; stable id supernatural-and-dark-fiction unchanged.
- Gate, committed blob, and deployed HTML passed.

## 21:54 CEST — three Urban portraits approved/wired; Paranormal Bricks v2 pending
- the curator approved Fae Founders A, Publicly Paranormal A, Modern Goth B. Wired as 97/98/99 webp, commit d36f139; committed blob + deployed HTML passed. New Drive folders under urban-fantasy with works/; approved portrait.png files uploaded. Paranormal Bricks folder created but deliberately imageless.
- Regenerated two Paranormal Bricks options to the curator's exact brief: close paranormal brick on wall corner + upside-down city background. v2 sheet /downloads/paranormal-bricks-v2-sheet.jpg. My lean A: reads as a paranormal brick at thumbnail scale; B is subtler/more beautiful but the human face risks looking like a screen. Await pick.
- Paranormal Bricks v2 A approved and wired as 100-paranormal-bricks.webp, commit 0606532; deployed and pixel-verified. Full-res Drive portrait.png 1T_FgcgWqmZaGJKpwz3cwaWwXgWUHnqu2.

## 22:18 CEST — intake 170-171
- 170 Have Space Suit -- Will Travel -> NEW leaf juvenile-science-fiction under futurist (10th child, at cap), commit ff46670. SFE Heinlein calls it among "the very best juvenile sf ever written" and the Scribner juveniles the most important single contribution to Children's SF; SFE YA distinguishes pre-1960s Juvenile SF. Cover OL 15243049: yellow Scribner/Emsh-style astronaut, flat English. Drive folder 1xPdPtw1ZRr8z8BqegMX6oMe34DtIN2Y2, works 1yD1j6sPS_cYEJ-IPwfTMs7i5Krhe-mOo, yaml 1KsiltFfD6pCFh4OrJPytkUssnpOROh5T. Leaf imageless; two portrait variants generated, sheet /downloads/juvenile-sf-sheet.jpg pending the curator pick. Lean A (young traveler on moon); B is cheerful but busy/retro-domestic.
- 171 Hawksmoor -> paranormal-bricks (now 4 works), same commit. SFE Ackroyd calls his fiction Urban Fantasy treating London as inherently supernatural/living; Hawksmoor binds its chthonic historical topography to modern murders through fabulated correspondences. Cover OL 10195872: richly illustrated Penguin collage (clocks/church/occult London). yaml 1LjhRAkM8SccO3x15U-LtBt4AQIrCIFrd. Both deployed and pixel-verified.
- progress next=172, processed=172, added=135.
- Standing portrait rule changed by the curator 22:21: stop A/B selection round-trip. Generate/select best portrait myself, wire and ship immediately; the curator will request regeneration after seeing it in the live taxonomy. Applied retroactively: Juvenile SF A wired as 101-juvenile-science-fiction.webp, commit 03915b6, deployed/pixel-verified; full-res Drive portrait.png uploaded.

## 22:47 CEST — intake 172-173
- 172 Herland -> utopian-fiction (6 works), 1979 Pantheon botanical/figural flat archive scan herland0000gilm. SFE calls it a book-length feminist Utopia depicting a 2,000-year isolated parthenogenetic society. yaml uploaded (16cA5OG6PmF1NR2F8g-JMv6VUHS9Gv9wW).
- 173 High-Rise -> social-dystopia-modern (5 works), 1977 painted exploding-tower archive scan highrise00ball. SFE calls it a present-set urban disaster novel about breakdown of apartment-block social life and technological landscape reflecting society's worst desires. Drive leaf folder lookup failed: new_folders map has no key and exact folder search returned none; yaml remains /tmp/high-rise.yaml pending folder recovery/creation.
- Commit 9023739, deployed/pixel-verified. Progress next=174 processed=174 added=137.

## 23:18 CEST — intake 174-175
- 174 Hothouse (Aldiss 1962) -> dying-earth (now 4). SFE Aldiss/Far Future: preferred title of The Long Afternoon of Earth; stopped Earth under swollen sun, devolved remnants in continent-spanning tree, explicit Far Future and entropy. Cover: 1979 Avon painted giant bee edition, flat archive scan hothouse00bria. YAML 11Jh3JIARGqXmg4ksuZ7SskrdcQGpxdG7. Commit 09f9204 deployed; deep link parsed/pixel-verified.
- 175 House of Leaves skipped. SFE Danielewski explicitly says it is not technically Fantastika because the impossible house/horror is part of an unreliable-narrator-produced text; excluded rather than forcing literary horror into SFF taxonomy. PRH confirms horror/maze-like house premise but does not override SFE taxonomy.
- Progress next=176, processed=176, added=138.
- GitHub fine-grained PAT must currently be regenerated per push because Vault is fill-only and CLI cannot retrieve it; latest regeneration stored. This is operational overhead, not a site blocker.
- Pending midnight portrait replacements: dedicated Upbeat Sci Fi and Time Travel Disorders.

## 23:49 CEST — intake 176-177
- 176 Howl's Moving Castle -> fantasy-of-manners (now 2 fiction cards), represented as 3-book Howl sequence (Howl 1986, Castle in the Air 1990, House of Many Ways 2008). SFE identifies the sequence and intricate interacting cast; comic secondary-world plot driven by domestic bargains, vanity, courtship, social wit. OL 8783945 moving-castle cover. YAML 1LXhN5MJDynspPtyGnDHaxXB1TR.
- 177 Inverted World -> mathematics (now 2). SFE Priest: hyperboloid world, hard-SF time distortion, pocket-universe geometry and conceptual breakthrough. OL 2950338 blue mountain cover. YAML 1VxBpdiTel1wCyT9y_r_JNugrHRP3BBxi.
- Commit fa9b9af deployed HTML and both deep links pixel-verified. progress next=178 processed=178 added=140.

## 00:20 CEST — final portraits after quota reset
- Dedicated Upbeat Sci Fi portrait and Time Travel Disorders portrait generated, self-selected, visually inspected, wired and shipped as 108-upbeat-sci-fi.webp and replacement 107-time-travel-disorders.webp (0ff679a). Full-res Drive archives 1yVKLGRmxjFVQg3OKce4K3YImnRFi3iSk and 1PxTPLp0M_cshmREy_nFJkCJDR3PRZGan. Deployed HTML verified; separate live tabs pixel-verified.

## 00:53 CEST — intake 178-179
- 178 Invisible Cities -> NEW leaf fabulation under unplaceable. SFE Calvino: fragmented Marco Polo voyages to surreal cities not actually visited; SFE Fabulation explicitly lists Calvino and defines the mode as foregrounding how stories construct worlds. 1974 HBJ line-art flat archive cover invisiblecitie00calv. New portrait: Polo and Khan over impossible atlas-cities. YAML 1-lfwuYCZi5xEvKWnba9AdxgIjInx9A29.
- 179 Jurassic Park -> NEW leaf Genetic Engineering under modern-day, 2-book card with Lost World. SFE Crichton: sequence argues risks of uncontrolled genetic engineering, dinosaurs reconstructed from genetic scraps. OL 8749000 Jurassic World omnibus cover + Lost World 10656102. New portrait: amber mosquito/DNA/lab/dinosaur. YAML 1KfJLw1oztLGToHcWfOH0yVro8YbxPJfA.
- Commit 6d1ab58 deployed, both deep links pixel-verified; 106 nodes/283 works. progress next=180 processed=180 added=142.

## 01:21 CEST — intake 180-181
- 180 Little Brother -> technothriller (now 2 cards), represented as 3-book sequence Little Brother/Homeland/Attack Surface. SFE: teenage hacker resisting near-future surveillance and information control. Archive first-edition Yuko Shimizu cover littlebrother00doct. YAML 1Bb7RCHpNyOobKBajFYNIaWmNWiSia58C.
- 181 Lord Valentine's Castle -> Majipoor 8-book card in science-fantasy (now 6). SFE explicitly calls it luxuriant Planetary Romance and cross-references Science Fantasy. Painted archive scan lordvalentinesca0000robe. YAML 1nqsyLQLZAquLd_9Z1VEIDJFFVTaDrQbe.
- eb75cf7 deployed and both deep links pixel-verified. progress next=182 processed=182 added=144.

## 01:53 CEST — intake 182-183
- 182 Lost Horizon -> utopian-fiction (now 7). SFE calls it a Scientific Romance and romantic Lost-World tale: Shangri-La is a serenely paradisal hidden society maintained through the coming holocaust to aid the re-creation of civilization. OL 6532933: richly painted mountains/valley, flat English cover. YAML 1zpitx7G91TZIGXFR4x6SZPRgYyGSueXo.
- 183 Mistborn -> hard-magic (now 3), represented as the 3-book Era One trilogy: Final Empire, Well of Ascension, Hero of Ages. SFE identifies Sanderson's Heroic Fantasies and names Mistborn; its rule-bound Allomancy/Feruchemy/Hemalurgy makes Hard magic the defining fit. OL trilogy covers 15158368/14658341/14658094; card art is the vivid purple painted first volume. YAML 1-j7i2N5iao3vEDrdKs8xPzFVfl1tcx0q.
- Commit 404bb49 deployed; local gate 106 nodes/287 works, refs consistent. Deployed HTML parsed for both records and both deep links pixel-verified. progress next=184 processed=184 added=146.

## 02:24 CEST — intake 184-185
- 184 Never Let Me Go -> genetic-engineering (now 2). SFE calls it a subtle Scientific Romance/dystopia in alternate-1990s England where clones are bred as organ donors; genetic engineering creates the exploited class. OL 6543832: atmospheric green field/solitary girl, flat English cover. YAML 1vn2g5G_IGz-FXxQ25V8zwgAnc_YcvFFk.
- 185 News from Nowhere -> utopian-fiction (now 8). SFE explicitly calls it Morris's Utopia: a dreaming narrator reaches a perfected post-revolutionary England without poverty, squalor or industrial ugliness. OL 103204: richly patterned William Morris fruit-tree/bird design, flat English cover. Initial OL 8769512 rendered with title below viewport; replaced before report with 103204 and rechecked. YAML 1i8ZNuBGYz5p1o_KxW8cbw2LcH4kUYvtQ updated.
- Final commit 69165af deployed; local gate 106 nodes/289 works, refs consistent. Deployed HTML and both deep links pixel-verified. progress next=186 processed=186 added=148.

## 02:54 CEST — intake 186-187
- 186 Night Watch skipped into the existing Discworld/comic-fantasy boundary backlog. SFE calls Discworld comic Fantasy and lists Night Watch in the series; placing the individual volume elsewhere would violate the one-series-one-card model. Comic-fantasy remains blocked on the curator's fantasy umbrella decision.
- 187 Non-Stop -> NEW leaf generation-starships under Futurist, which becomes its 10th child (at cap, not over). SFE Generation Starships calls Non-Stop a very successful reworking of the crew-forgets-the-ship pattern: surviving generations mistake their multigenerational spacecraft for the world until a conceptual breakthrough. OL 6544849: vivid blue painted jungle/ship interior, flat English cover. New self-selected portrait: tribal travelers discover their lush world lies inside a colossal ship. Drive folder 1BgSg-VVeu2ziMFvUJ-AXL1ajtLQ2_vtV; works 1mLiIFPdmt7p0wHespxSWJebg318pBlJY; portrait 1Yqe67WmhRGfCWad4d6qNUErKxWsVLL_k; YAML 1n0J5tX-P5yfnrQk595ydt6XXTeTFOWLz.
- Commit 904f77f deployed; local gate 107 nodes/290 works, refs consistent. Deployed leaf and Non-Stop deep link pixel-verified. progress next=188 processed=188 added=149.

## 02:55 CEST — intake 186-187
- 186 Night Watch skipped for now. SFE identifies it as part of Discworld and calls Discworld the genre's finest set of pure comedies; it belongs in the pending comic-fantasy leaf, still blocked on the fantasy-side umbrella boundary. Did not force it elsewhere merely because this volume uses time travel.
- 187 Non-Stop -> NEW leaf generation-starships under futurist (10th child, now at cap). SFE Generation Starships calls it a very successful reworking of the classic crew-forgets-the-ship pattern. OL 6544849: vivid blue jungle/ship painted cover, flat English. New self-selected portrait shows tribal travelers in a lush interior world with the immense spacecraft architecture revealed overhead. Drive leaf 1BgSg-VVeu2ziMFvUJ-AXL1ajtLQ2_vtV, works 1mLiIFPdmt7p0wHespxSWJebg318pBlJY, portrait 1Yqe67WmhRGfCWad4d6qNUErKxWsVLL_k, yaml 1n0J5tX-P5yfnrQk595ydt6XXTeTFOWLz.
- Commit 904f77f deployed; local gate 107 nodes/290 works, refs consistent. Deployed HTML, new leaf portrait, and Non-Stop deep link pixel-verified. progress next=188 processed=188 added=149.

## 03:28 CEST — intake 188-189
- 188 Northern Lights -> His Dark Materials 3-book card in portal-fantasy (now 5). SFE describes its Alternate Cosmos and travel among parallel worlds through openings cut by the subtle knife; cross-world passage structures the trilogy. OL 15172988/12614549/12613246, visually coherent symbol/art covers. YAML 1sFMWhRiA-pYZRBJWUBNzN9kndk3qcrak.
- 189 Outlander -> 9-book major-novel card in ancestral-time-travel (now 2). No SFE author entry found; Gabaldon's official account sends Claire from 1946 through standing stones to 1743, where her husband's six-times-great-grandfather is central, and calls time travel a recurring series element. PRH calls it historical fantasy. OL per-book covers; final card cover 6548767 is the richly illustrated mirror/portrait edition. Initial 14428230 silently rendered blank; replaced before report and rechecked. YAML 1lgf6oU8lcdWIImgvzX4hs5EWWLsv7kVe updated.
- Final commit a68f50f deployed; gate 107 nodes/292 works, refs consistent. Both series grids pixel-verified. progress next=190 processed=190 added=151.

## 03:54 CEST — intake 190-191
- 190 Paladin of Souls skipped as duplicate: already the second book inside the existing World of the Five Gods 3-book fiction card in heroic-fantasy. SFE confirms the sequence and Paladin's Hugo/Nebula wins.
- 191 Pattern Recognition -> technothriller (now 3). SFE says Blue Ant eschews future apocalypse and begins in the here-and-now, exploring a volatile information-saturated world where virtual and real blur. Present-day brand/Internet mystery fits the leaf's technology-driven mundane-thriller definition. OL 7997178: bold modern pink/yellow portrait collage, flat English. YAML 18yIDs6U1LylKbQ8t1GekDRYbOP9ZSpML.
- Commit 199b1d1 deployed; gate 107 nodes/293 works, refs consistent. Deep link pixel-verified. progress next=192 processed=192 added=152.

## 04:25 CEST — intake 192-193
- 192 Perfume -> magic-realism (now 3). No SFE author entry found. Penguin describes Grenouille's superhuman smell and the virgin's scent as magical; impossible sensory power and the perfume's mass compulsion are matter-of-fact in realistic 18th-century France. OL 10910286: ornate floral/skull English cover. YAML 1o02Q8vq4ghRNOt-Y9crUbubj31cagAhX.
- 193 Piranesi -> portal-fantasy (now 6). SFE describes the House as a Pocket Universe set in its own universe and ours, with its relationship to 21st-century England gradually revealed; passage between worlds drives entrapment, memory and return. OL 10226290: elegant black/orange faun-on-column first-style cover. YAML 1rZB-nkP0Xc7Ye2z5m-imeXJ7jfNcpq_T.
- Commit a156ef1 deployed; gate 107 nodes/295 works, refs consistent. Both deep links pixel-verified. progress next=194 processed=194 added=154.

## 04:58 CEST — intake 194-195 + split proposal
- 194 Red Shift -> NEW leaf timeslips under time-travel-fiction (now 7 children). SFE says its time shift moves among Roman Britain, the Civil War and now through alter egos focused on a Neolithic axe-head; no built mechanism. OL 241: moody Mow Top silhouette/starburst, flat English. Self-selected portrait layers Roman, Civil War and modern figures around glowing axe/time fractures. Drive leaf 1RApa1MncQ9Q_NKOAVWLnBch-uaVZBLiR; works 18PkEsjD2mTIjems-0SC1wJVhKSbtWSfl; portrait 18v5E91RjXu8OWZQ6_cGcpD51-5rRcxCM; YAML 1VZTFtGS62TatAz4N2nZ812CLmip9e3CE.
- 195 Riddley Walker -> post-apocalyptic-fiction, now exactly 10. SFE calls it a genuine Ruined Earth tale 2,000 years after the Holocaust as gunpowder is rediscovered. OL 8435360: SF Masterworks painted ruined-landscape/punch-figure cover. YAML 1zym_pDDPoTPt-bWqDtjpEeVQDXhh0sHo.
- Commit a986e74 deployed; gate 108 nodes/297 works, refs consistent. Both deep links pixel-verified. progress next=196 processed=196 added=156.
- SPLIT PROPOSAL (not executed): SFE explicitly distinguishes Post-Holocaust from Ruined Earth when enough time has passed. Make post-apocalyptic-fiction a pure umbrella with stable leaf IDs where possible: Post-Holocaust Survival (6: Earth Abides, I Am Legend, Lost Everything, The Road, Station Eleven, These Prisoning Hills) and Ruined Earth (4: A Canticle for Leibowitz, Silo, Davy, Riddley Walker). Needs the curator approval before structural change.

## 2026-09-15 05:26 CEST — indices 196–197 shipped
- 196 River of Gods — added to robots-and-ai. SFE's account makes illegal/advanced machine intelligence central to its 2047 India, climate, politics, and social conflicts. Flat-front OL 474065 selected from one-pass sheet for its vivid India/deity imagery and readable English title. YAML: https://drive.google.com/file/d/1u1KLhyWJFTt5WnrDVqJOj5Z2AV4S4FRm/view
- 197 Rogue Moon — created matter-transmission under hard-sf. SFE explicitly calls the novel Hard SF and describes its lunar alien labyrinth as explored through Matter Transmission/Matter Duplication; this is a genuine mechanism-centered trait, not a leftover bucket. Flat-front SF Masterworks OL 8651995 selected for its strong lunar/labyrinth design. New portrait generated and wired directly per the curator's standing rule. YAML: https://drive.google.com/file/d/1BojLdwKTu92oRCl1gsQDHVLgMYDWsq9p/view
- Local gate: 109 nodes, 299 works, refs consistent.
- Commit: 0c8a383. Progress: next 198, processed 198, added 158.
- Post-apocalyptic-fiction remains unchanged pending the curator's ruling.

## 2026-09-15 05:57 CEST — intake 198–199
- 198 Silverlock -> portal-fantasy (now 7). NESFA describes the protagonist's peregrinations through the Commonwealth of Letters; Black Gate specifies that Shandon is shipwrecked from our world onto that land and journeys among literature/myth/folklore figures. Cross-world arrival and the self-contained literary realm structure the novel. OL 8260665: lush painted ensemble of literary figures, flat English title. YAML 1gR6hd-6DQBVLi4K58b3EB18YmKWsSGQ3.
- 199 Slan -> telepathy-fiction / Mentalism fiction (now 4 cards), represented as the 2-book Slan sequence: Slan and Slan Hunter. SFE calls the Slans a persecuted mutant race whose defining powers include Telepathy, physical superiority, and extraordinary Intelligence; the hidden telepathic society drives its conflict and revelations. Tor confirms Slan Hunter is the sequel completed by Kevin J. Anderson from van Vogt's partial draft and outline. OL 5543912 clean, elegant retro first-edition-like green future-city cover; Slan Hunter OL 6936338. YAML 1EkB6bA5ZiSRp3IhPPTpB0rHVihKOpd4H.
- Commit 39a35fa deployed. Gate 109 nodes/301 works, refs consistent. Both fresh deep links and pixels verified after CDN deployment. progress next=200 processed=200 added=160.
- Neither leaf is at the 10-work split threshold. Post-apocalyptic structure remains untouched pending the curator's ruling.

## 2026-09-15 05:58 CEST — Black Company series cover audit
- Added one-pass flat-front English cover picks for all 9 Black Company books: OL 6978703, 6874911, 603159, 603518, 603084, 603953, 182506, 182508, 604076. The covers form a strong classic painted/illustrated dark-fantasy set; no hunt beyond the one Open Library series search.
- Commit to deploy: c268eb0. Local gate 109 nodes/301 works, refs consistent. Deployed series page parsed and pixel-verified with all 9 cards. Audit report sent.

## 2026-09-15 06:28 CEST — intake 200–201
- 200 Small Gods skipped into the existing Discworld/comic-fantasy boundary hold. SFE explicitly lists it within the Discworld series and calls the novels Fantasy. One-series-one-card means it must not be duplicated as a standalone; comic-fantasy placement still awaits the curator's fantasy-umbrella ruling.
- 201 Spin -> NEW leaf time-distortion under time-travel-fiction (now 8 children), represented as the 3-book Hypotheticals sequence: Spin, Axis, Vortex. SFE calls this a temporal quarantine: Earth is enclosed in a bell jar where time is enormously slowed while millions of years pass outside for every year within. The unequal time rate is the sequence's defining mechanism, matching SFE Time Distortion. OL 6632328/1443032/9348869; card cover is Spin's clean black cosmic-vortex design. New self-selected portrait shows present-day Earth inside a clear temporal membrane while galaxies and the Sun age outside. Drive leaf 1od2CFIkELykntG5yP0gPSfl4eK9JX7dC; works 1gqwX-ZnRl3j0kNv7YZrzmkbjUxy5yHzw; portrait 1Zx7cjud9C6IiqO6nrum_Vzs-n1eWQGoL; YAML 1hE0rNPYCQQD-K9TRNaXhVq312WPj7XtV.
- Commit 70e7bdc deployed; local gate 110 nodes/302 works, refs consistent. Spin deep link and 3-card series grid pixel-verified. progress next=202 processed=202 added=161.
- Time Distortion has 1 fiction and is below split threshold. Post-apocalyptic and Discworld holds remain untouched.

## 2026-09-15 07:01 CEST — intake 202–203
- 202 Tarzan of the Apes -> Tarzan 24-book major-series card in lost-world-fiction (now 4). SFE says the first book is marginally SF, but the long sequence's cartoon Africa is repeatedly studded with Lost Worlds/Lost Races, including Atlantis/Opar, dinosaurs, miniature peoples, and Pellucidar. That repeated discovery pattern defines the whole fiction. Official ERB series pages supplied the canonical title/year set. Per-book covers were added in the same pass; most are colorful flat English Open Library fronts. The Return of Tarzan's initial OL scan visibly had a price sticker, so pixel review replaced it with clean OL 12100604, a painted duology cover that includes the correct title. Card cover OL 6457176, the lush painted Lord of the Jungle edition. YAML 1fuhGz1A2HgM4_UyOT2NtZE_rfTkZKT8m.
- 203 Tehanu skipped as duplicate: already the fourth book in the existing 6-book Earthsea fiction card in heroic-fantasy; SFE confirms the Earthsea sequence.
- Final clean-cover patch 1a28835 deployed; the 24-book card parsed and was pixel-verified. Gate 110 nodes/303 works, refs consistent. progress next=204 processed=204 added=162.
- Lost World fiction has 4 fictions, below threshold. Existing structural holds untouched.

## 2026-09-15 07:29 CEST — intake 204–205
- 204 The Alteration -> alternate-history (now 6). SFE calls it Amis's major full-scale SF work, set in an Alternate History where the Reformation never happened and Roman Catholic domination continues into 1976. The failed Reformation is the identifiable divergence. PRH's current NYRB Classics 9781590176177 cover is a crisp black/yellow architectural illustration with clear title/author and markedly better than the tiny blank-looking OL scan. YAML 1GwxNYj9VzKQQ9mD_zRVdY19Yeba7fwwt.
- 205 The Amazing Adventures of Kavalier & Clay excluded. SFE says its story-likeness is non-mimetic but that Equipoise holds, with the Prague Golem not animate; PRH describes a historical novel beginning in 1939 about two cousins creating comic-book superheroes. No actual magic or SF crosses the curator's fiction boundary.
- Commit 0d21842 deployed; gate 110 nodes/304 works, refs consistent. Alteration deep link and pixels verified. progress next=206 processed=206 added=163.
- Alternate History has 6 works, below threshold. Structural holds untouched.

## 2026-09-15 07:59 CEST — intake 206–207 + Belgariad covers
- 206 The Belgariad skipped as duplicate: existing 5-book card in high-fantasy/Quest fantasy. The intake pass fixed all 5 missing per-book covers in one Open Library pass: 6610126/207288/207283/207292/209046. Deployed grid pixel-verified; colorful English classic-fantasy fronts.
- 207 The Bird King -> fantasies-of-history (now 4). SFE explicitly calls it historical quest fantasy set before Columbus, and the actual magic of Hassan's impossible mapmaking reweaves the documented fall of Granada, fitting the leaf's hidden magical history trait. Selected Grove Atlantic first hardcover: a beautiful black/turquoise/gold floral-bird design with clear English title/author. YAML 17QXpmysznVBs5B_9s8wkxZ5xJMo5IfqS.
- Commit 19beae0 deployed; gate 110 nodes/305 works, refs consistent. Bird King and Belgariad grid pixel-verified. progress next=208 processed=208 added=164.
- Fantasies of History has 4, below threshold. Structural holds untouched.

## 2026-09-15 08:36 CEST
- 208 The Blind Assassin -> fabulation. SFE says considerable SF is concealed in the extensive pulp-SF novel-within-the-novel inside the conventional Canadian frame; the nested authorship/world-making structure is the defining speculative technique. OL 11041760. YAML 1Apy0Zvh0OgKb1NeBR8hEPUu086zOmX2z.
- 209 The Book of Ptath -> reincarnation-fiction. SFE describes a reincarnated amnesiac Far-Future god-figure fighting the usurper who brought him back; recurring identity is the clearest defining mechanism. OL 678924. YAML 15JBMBqMd1yvYi6bB4IMFPXyx8GRGujxw.
- Intake commit 716f928, then the curator approved the pending post-apocalyptic split with `Execute` (phonemsg-01M2HW2SDPW9TC627P32A6G28C). Executed at commit 525ff7a: stable `post-apocalyptic-fiction` is now a pure umbrella; new `post-holocaust-survival` has 6 works (Earth Abides, I Am Legend, Lost Everything, The Road, Station Eleven, These Prisoning Hills), and `ruined-earth` has 4 (A Canticle for Leibowitz, Silo, Davy, Riddley Walker). Generated and selected portraits 115 and 116. Local gate 112 nodes / 307 works, refs consistent. Fresh deployed pages and pixels verified.
- Progress next 210 / processed 210 / added 166. Exactly-at-10 now only Futurist children=10; no leaf has 10 works.

## 2026-09-15 09:04 CEST — intake 210–211
- 210 The Businessman -> Supernatural Minnesota 4-book card in modern-goth (now 3 fiction cards): The Businessman, The M.D., The Priest, The Sub. SFE identifies The Businessman as the first volume of the quartet and an intricately metaphysical horror novel, then names its linked supernatural volumes. Its ghosts, zombie poet, occult Minneapolis and modern social satire match Modern Goth's supernatural darkness embedded in contemporary life. Card OL 8272034; per-book OL 8272034/4037504/417652/418441 from one-pass series review. YAML 1AkWB8Pk4Yuo5s8XdogvtZVOxmioDuKpU.
- 211 The Calculating Stars -> Lady Astronaut 4-book card in alternate-history (now 7): The Calculating Stars, The Fated Sky, The Relentless Moon, The Martian Contingency. SFE explicitly calls the sequence Alternate History: a 1952 meteor devastates the eastern USA and accelerates the space programme, while women challenge their exclusion. Author's official series pages provide the current 4-volume order and clean coherent English covers. YAML 1Fyd26YU-D3e_k-UjswtaF41ne77xwPEW.
- Commit 7f44e57 deployed. Gate 112 nodes/309 works, refs consistent. Deployed HTML byte-identical and both 4-book grids pixel-verified on fresh routes. Progress next=212 processed=212 added=168. No leaf at 10 works; Futurist remains exactly 10 children.

## 2026-09-15 09:33 CEST — intake 212–213 + Narnia covers
- 212 The Case of Charles Dexter Ward -> ancient-tormentors (now 5). Lovecraft's Providence horror centers on Joseph Curwen, an eighteenth-century necromancer whom Ward physically resurrects and who returns to murder and replace his descendant. The ancient enduring occult antagonist is the central supernatural intrusion. OL 8443336: restrained blue-black branch silhouette, flat English cover. YAML 15zVVJbbwFhxNWnU94sPOtGWVyeWDGb6y.
- 213 The Chronicles of Narnia skipped as duplicate: existing 7-book portal-fantasy card. SFE calls it allegorical Fantasy and explicitly describes human children travelling to Narnia, with other dimensions and parallel worlds; current placement stands. One-pass Open Library audit added all seven missing book covers: 8441376/45897/9184719/6950992/9184792/1072931/6529226. Card default changed to 8441376 so the leaf-grid image now visibly carries English title/author. The set is colorful, illustrated, flat-front, and mostly period editions; no extra hunt.
- Commit da35365 deployed. Gate 112 nodes/310 works, refs consistent. Deployed HTML byte-identical; Ward page and Narnia seven-cover grid pixel-verified. Progress next=214 processed=214 added=169. No leaf at 10 works; Futurist remains exactly 10 children.

## 2026-09-15 10:03 CEST — intake 214–215
- 214 The Crying of Lot 49 excluded. SFE describes Tristero as a possible centuries-old conspiracy/Secret Masters system but emphasizes that nothing is clear and that Oedipa's apparent pattern may be apophenia. Under the curator's actual-speculative-event boundary, the novel's radical epistemological ambiguity never establishes the conspiracy as real; did not force it into Fabulation merely for literary form.
- 215 The Crystal Cave -> Mary Stewart's 5-book Arthurian Saga card in mythic-retelling (now 7): The Crystal Cave, The Hollow Hills, The Last Enchantment, The Wicked Day, The Prince and the Pilgrim. It retells Merlin/Arthur in post-Roman Britain, with Merlin's clairvoyant Sight and Morgan le Fay's sorcery. Hachette calls Prince and Pilgrim the final installment. One-pass OL 592134/4987866/4982059/1466724/431498; colorful illustrated flat English covers, though middle scans are low resolution. Card cover OL 592134. YAML 1K45KVpxi8xZTyUUKkqp10og6UQgbhqUu.
- Commit 59080dc deployed. Gate 112 nodes/311 works, refs consistent. Deployed HTML byte-identical; five-book card and pixels verified. Progress next=216 processed=216 added=170. No leaf at 10 works; Futurist remains exactly 10 children.

## 2026-09-15 10:13 CEST — Futurist mapping hold
- the curator clarified that dimension-crossing counts as Intergalactic only if it definitely reaches OUR universe outside the Milky Way. Worm World is not established both outside the Milky Way and within our universe, so The Witches of Karres maps to Milky Way, not Intergalactic.
- Living complete map created at `/home/sandbox/futurist-reorganization-map.md` (snapshot 109 fiction cards / 234 represented books, commit 59080dc). Maintain it as source packets firm up classifications.
- INTAKE HOLD: while this mapping work is ongoing, halt any new candidate that could possibly land under Futurist. Clearly non-Futurist entries may continue. Ambiguous candidates must be held rather than forced elsewhere.
- 10:25 CEST: Futurist living map expanded with all location-qualified subgenres requested by the curator. The 14 split current leaves yield 32 non-empty scope-qualified leaves; 14 reuse the most semantically continuous existing portrait and 18 need new art. Full proposed scope tree is recorded in `/home/sandbox/futurist-reorganization-map.md`. Map-only; no site mutation.

## 2026-09-15 10:32 CEST — intake 216–217 under Futurist hold
- 216 The Day After Judgment skipped as duplicate: already the second book in the existing 2-book Black Easter fiction card in dark-fantasy. SFE says Blish regarded Black Easter and The Day After Judgment as one novel, and explicitly calls Black Easter a strong fantasy where actual black magic is treated with the precision of physics. Both book covers are already wired (ISBN 9780140034165 / OL 9396106), so no audit mutation was needed.
- 217 The Dervish House HELD without placement or mutation under the curator's active Futurist intake hold. SFE describes it as an extremely fast-forward Istanbul; it could plausibly land under Futurist, so it must wait for the scope reorganization rather than be routed around the hold. Source: https://sf-encyclopedia.com/entry/mcdonald_ian.
- No repo mutation/commit this pair. Progress next=218 processed=218 added=170. Futurist map remains `/home/sandbox/futurist-reorganization-map.md`.

## 2026-09-15 10:42 CEST — three-bucket Futurist plan
- the curator parked the five-bucket location proposal under the name `scale-plan`; preserved at `/home/sandbox/scale-plan.md`.
- New plan created at `/home/sandbox/three-bucket-plan.md`: Earthbound (53 cards), Space fiction (50), Otherworldly (6). Complete map covers all 109 current Futurist cards.
- Structure impact: 16/25 leaves move intact; 9 split into 18 qualified leaves; 34 thematic leaves total. 9 split partitions reuse current art, 9 need new art; plus 3 umbrella portraits = 12 new portraits.
- Plan-only; no repo or Drive mutation. Futurist intake hold remains active.
- 10:49 CEST: Three-bucket plan naming refined per the curator: extracted constituents merge at the highest useful established parent rather than mechanically retaining old leaf names. Example applied: Inverted World + Observer -> Earthbound Hard SF. Revised plan has 12 replacement leaves, 28 thematic leaves total, and 9 new portraits including umbrellas. Map-only; hold unchanged.

## 2026-09-15 11:08 CEST — intake 218–219 + Elric cover audit
- 218 The Dwellers in the Mirage -> lost-world-fiction (now 5). SFE describes Merritt's remote Alaskan valley with a hidden prehistory and cosmic-horror entity Khalk'ru; the geographically isolated archaic society and its discovery are the defining Lost World structure. The novel was published and framed in 1932, so Historical. One-pass cover choice: Open Library 8535842, a vivid yellow/orange Patrick Woodroffe-style monster painting with clear English title/author. YAML 1hrt__TYDhvuc78DXgy-SrxRaxhu0xxtl.
- 219 The Elric Saga skipped as duplicate: existing six-book Elric of Melniboné card in sword-and-sorcery. One-pass Open Library audit added five usable flat covers (10098033/7020626/284656/284439/10237221) and changed the default to 10098033 so the leaf card shows English title/author. The Sleeping Sorceress result was a back-cover scan, so it remains blank rather than wiring a bad image.
- Commit 9de1a2f deployed. Gate 112 nodes/312 works, refs consistent; deployed HTML byte-identical after cache-busting. Dwellers fiction page and Elric six-book grid pixel-verified; all five wired Elric images reported healthy. Progress next=220 processed=220 added=171. No leaf reached 10 works. Futurist intake hold remains active.

## 2026-09-15 11:34 CEST — three-bucket naming revision
- Applied the curator's requested Space fiction child names in `/home/sandbox/three-bucket-plan.md`: Anthropological SF, First Contact, New Space Opera and Military SF now drop the redundant Space prefix; Space Techno Fiction becomes Techno Fiction in space; Earthbound Techno Fiction becomes plain Techno Fiction.
- Recommendation after checking the two constituents: keep **Techno Fiction in space**, not Cyberpunk in space. Takeshi Kovacs is securely interstellar cyberpunk, but Accelerando's full defining arc is Singularity/posthuman escalation through superhuman AI, biotechnology, molecular nanotechnology and off-Earth posthuman expansion. Cyberpunk would be precise for one and too narrow for the other; Techno Fiction is their highest honest shared established parent.
- Map-only revision. No taxonomy/Drive mutation; Futurist intake hold remains active.

## 2026-09-15 11:36 CEST — intake 220–221
- 220 The End of Eternity HELD without placement or mutation under the active Futurist intake hold. SFE identifies Eternity as Time Police whose interventions engineer history toward stable outcomes; this could plausibly land in Earthbound Futurist after the reorganization, so it must not be classified around the hold. Sources: https://sf-encyclopedia.com/entry/time_police and https://sf-encyclopedia.com/entry/cultural_engineering.
- 221 The Eyre Affair -> Thursday Next 8-book card in fabulation (now 3): The Eyre Affair, Lost in a Good Book, The Well of Lost Plots, Something Rotten, First Among Sequels, One of Our Thursdays Is Missing, The Woman Who Died a Lot, Dark Reading Matter. SFE calls it an Alternate World sequence whose metafictional topoi interpenetrate the conventions: characters enter books, alter them from within and thereby alter the real world. That story/world feedback is the defining Fabulation trait. Soho Press confirms Dark Reading Matter is the eighth and final adventure, published October 2026. One-pass OL review added five clean English-title covers (2401550/205625/400490/6684444/9435520); rejected Lost in a Good Book's square audiobook and First Among Sequels' blank scan rather than wiring bad images. YAML 1jtPWOSBHlf4pODssXyxnaKFmE2iZN4Oj.
- Commit e2cb6a2 deployed; gate 112 nodes/313 works, refs consistent and deployed HTML byte-identical. Eight-book grid pixel-verified; all five wired images healthy. Progress next=222 processed=222 added=172. No leaf reached 10. Futurist intake hold remains active.

## 2026-09-15 11:38 CEST — Hard SF in space clustering revision
- Updated `/home/sandbox/three-bucket-plan.md` per the curator: Orbital Mechanics, Planetary Science, Matter Transmission and Hard Alien now cluster under `Hard SF in space` inside Space fiction.
- `Hard SF in space` is an intermediate branch, not a leaf: each child has a narrower coherent mechanism/subject and multiple works, so merging their 11 cards into one leaf would erase useful taxonomy. Structure remains 28 terminal thematic leaves plus this one intermediate branch.
- Stable-ID/art plan: migrate existing `hard-sf` branch to `Hard SF in space`; it already parents three of the four children and gains Hard Alien. Reuse `15-hard-sf.webp`; all four children keep their portraits. Zero additional art beyond the existing nine-new-portrait plan.
- Plan only; no taxonomy/Drive mutation. Futurist intake hold remains active.

## 2026-09-15 11:44 CEST — Dystopian Futures clustering revision
- Updated `/home/sandbox/three-bucket-plan.md`: Totalitarian dystopia, Social dystopian future, Post-Holocaust Survival, Ruined Earth, Utopian fiction and Dying Earth now cluster under `Dystopian Futures` inside Earthbound.
- `Dystopian Futures` is an intermediate branch, not a merged leaf. All six children remain distinct; the map still has 28 terminal thematic leaves, now with two intermediate branches (`Dystopian Futures`, `Hard SF in space`).
- Stable-ID/art plan: migrate existing `dystopian-fiction` branch to `Dystopian Futures`; it already ancestors four of the six leaves and gains Utopian fiction and Dying Earth. Reuse `10-dystopian-fiction.webp`; child portraits remain. Retire now-empty Post-apocalyptic fiction, Upbeat Sci Fi and Far future intermediate branches with redirects. Zero extra art; total remains nine new portraits.
- Plan only; no taxonomy/Drive mutation. Futurist intake hold remains active.

## 2026-09-15 12:07 CEST — parallel theme-plan complete
- Created `/home/sandbox/theme-plan.md`, a complete analysis-only map of all 109 current Futurist cards by core theme: Future of Earth fiction 54, Spacefaring fiction 34, Alien fiction 19, Otherworldly fiction 2.
- Theme-plan has 18/25 old terminal leaves move intact; seven split into 11 useful replacement leaves after consolidation. Proposed structure: 28 terminal leaves + Dystopian Futures and Hard SF in space intermediate branches. Estimated 10 new portraits (six replacement + four umbrellas), versus nine in 3B.
- Nine genuine theme-vs-setting boundary packets recorded, including 2001, Martian Chronicles, Stranger, Mission of Gravity, Star Maker, Dune, Dying Earth works, Embassytown, and the unanchored space operas.
- Recommendation: 3B remains leading execution plan because scope is objective/auditable; theme-plan is the stronger reader-facing alternative if conceptual browsing outweighs classification consistency. No site/Drive mutation. Futurist intake hold remains active.

## 2026-09-15 12:08 CEST — intake 222–223
- 222 The Female Man HELD without placement or mutation under the Futurist intake hold. SFE describes its braid of three Alternate Histories and a female Utopia; it could plausibly land in Future of Earth/Earthbound after reorganization, so it remains unclassified. Source: https://sf-encyclopedia.com/entry/russ_joanna.
- 223 The Fionavar Tapestry -> 3-book card in portal-fantasy (now 8): The Summer Tree, The Wandering Fire, The Darkest Road. Kay's official site calls it High Fantasy in the Tolkien tradition, but explicitly says five young Canadians are taken to Fionavar, the first of all worlds; cross-world transport structures the trilogy and makes Portal fantasy its highest fit. One-pass OL covers 295003/295006/295011: coherent, colorful painted English fronts. YAML 1PSC4p5qlaKYIeTZRgpjhyCFDyvdUYUr8.
- Commit ce6f772 deployed; gate 112 nodes/314 works, refs consistent and deployed HTML byte-identical. Three-cover grid pixel-verified; all images healthy. Progress next=224 processed=224 added=173. No leaf reached 10. Futurist intake hold remains active.

## 2026-09-15 12:10 CEST — five-theme-plan complete
- Created `/home/sandbox/five-theme-plan.md`, mapping all 109 current Futurist cards by core theme into: Hard Sci-fi 9, Future of Earth fiction 52, Spacefaring fiction 28, Alien fiction 18, Otherworldly fiction 2.
- 19/25 terminal leaves move intact; six split into nine useful replacement leaves. Structure: 28 terminal leaves + Dystopian Futures intermediate. Estimated nine new portraits, tying 3B and one fewer than four-theme.
- Hard Sci-fi uses a strict core-test, not technical texture: 2001, Ringworld, Moon, Mars Trilogy, Mission of Gravity, Martian, Rogue Moon, Inverted World, Observer. Hard Alien stays under Alien because alien minds/species/civilizations are core.
- Recommendation: strongest reader-facing plan so far, but 3B remains safer execution plan. Five-theme mixes a methodological/rigor axis with four subject axes and introduces hard-SF overlap judgment. No site/Drive mutation; hold active.

## 2026-09-15 12:18 CEST — five-theme execution in progress
- Owner authorization recovered exactly: `phonemsg-01M2J918AE2RK4BMXWZB5MTJ95` at 12:15:36 CEST, “Execute the Five-theme-plan.”
- Nine approved-plan portraits generated and visually inspected together; all are detailed colorful 2:3 paintings and passed selection. Local migration now staged; gate 112 nodes / 314 works, references consistent. No push/Drive mutation yet at this milestone.
- New standing rule from the curator at 12:17: after migration, intake may place works within the five Futurist themes, but no new subgenre may be created directly under Futurist without asking him. This supersedes the broad intake hold once deployment completes.

## 2026-09-15 12:30 CEST — five-theme migration deployed and Drive redistribution
- Executed owner-authorized five-theme migration (owner source `phonemsg-01M2J918AE2RK4BMXWZB5MTJ95`, exact text “Execute the Five-theme-plan”). Commit `9e80080` pushed; local gate 112 nodes / 314 works, all references consistent, all 109 prior Futurist cards present exactly once.
- Live Futurist has exactly five children: Hard Sci-fi, Future of Earth fiction, Spacefaring fiction, Alien fiction, Otherworldly fiction. Public HTML contains all top and replacement leaf IDs. Futurist page pixel-verified at `https://gusoder.github.io/sff-taxonomy-browser/index.html?cb=9e80080#futurist`; screenshot `/downloads/cloud-browser-20260915-102151.png`.
- Drive migration: four new direct theme folders created, existing Hard SF renamed hard-sci-fi; 14 stable branch folders moved under their new themes; seven replacement leaf folders + works folders created. All 22 work YAMLs from the six split leaves redistributed into Techno Fiction (7), Techno Fiction in space (2), Hard Conceptual SF (2), Otherworldly Hard SF (2), Earthbound Military SF (1), Future history of Earth (2), Future history in space (5), Alien cosmic history (1). Those 22 YAMLs were updated in-place to their new leaf/deep-link metadata. New top and replacement portraits uploaded. Source split folders remain as noncanonical leftovers for later cleanup rather than being destroyed.
- Post-migration intake hold is lifted under the curator's 12:17 standing rule: classify inside the five themes normally; never create a new direct Futurist child without consulting him.
- Parked Futurist candidates remain to ship: The Dervish House, The End of Eternity, The Female Man. Resume these before ordinary next=224 intake.

## 2026-09-15 12:35 CEST — parked Futurist intake cleared
- 217 The Dervish House -> Techno Fiction (now 7): SFE's extremely fast-forward Istanbul and the novel's near-future nanotech/AI/finance transformation make terrestrial technology the core. OL 8777419, luminous blue Istanbul arch, English title; one-pass cover review. YAML 1r157ojyZ4dXBehtOEgpEhKeMzb-7oAyF.
- 220 The End of Eternity -> Future history of Earth (now 3): SFE identifies Time Police engineering successive safe historical outcomes, causing terrestrial stagnation and blocking later galactic expansion; civilizational trajectory is the core. OL 6622699, bright yellow orbital/clock geometry, English title. YAML 1HrlfCGpH_VhUqtDw4IttixfJXTqMCAdT.
- 222 The Female Man -> Utopian fiction (now 9): SFE describes alternate Joannas/Histories centered on Whileaway's female utopia, set against gender-war dystopia; social utopian thought experiment is the core. OL 448143, spare mirrored profile, English title. YAML 1KhBFELSiTEjytTwOrQx3Z17vv8DrLmKJ.
- Commit 4ea03e6 deployed; gate 112 nodes / 317 works, refs consistent, public HTML byte-identical. All three fiction routes fresh-loaded; Female Man pixels verified at `/downloads/cloud-browser-20260915-103444.png`. Progress remains next=224 / processed=224 because these held indices were already processed; added increases 173 -> 176. No leaf crossed the 10-work split trigger (Utopian fiction is 9).
- Futurist hold/backlog fully cleared. Ordinary two-candidate intake resumes at index 224 under the no-new-direct-Futurist-child boundary.
- Final Drive corrective audit found two older structural drift pockets and fixed them: Post-Holocaust Survival and Ruined Earth folders were missing from the prior hierarchy, so created them under Dystopian Futures, uploaded portraits, and routed the exact 6/4 work sets. New Space Opera still contained retired Galactic/Transhuman subfolders; consolidated all eight YAMLs into New Space Opera works and moved the old subfolders to trash. Renamed five folders to exact current labels (Social dystopian future, Mentalism fiction, Military SF, Anthropological SF, First Contact). Final recursive Drive hierarchy now has exactly the 5 direct themes, 1 intermediate Dystopian Futures, and 27 terminal leaves - 33 non-works folders total, matching the live taxonomy (28 terminal leaves including the 5 direct-theme trees and one intermediate; site count terminology preserved). Old source containers were trashed, not permanently deleted.

## 2026-09-15 12:40 CEST — intake 224–225
- 224 The Graveyard Book -> ghost-story (now 7). SFE calls it Young Adult fantasy shaped from Jungle Book episodes transposed into a cemetery; the boy raised and protected by ghosts makes the ghost community the defining mechanism. One-pass OL 7099583: flat Dave McKean blue cemetery silhouette with clear English author/title. YAML 1JxgRraSmo0vx5mIYvdc2-hu1L5BV0ozg.
- 225 The Hundred Thousand Kingdoms -> 4-book Inheritance Trilogy card in political-fantasy (now 5): The Hundred Thousand Kingdoms, The Broken Kingdoms, The Kingdom of Gods, The Awakened Kingdom. SFE calls it dynastic fantasy with shaping mythology; Jemisin's official series page centers Arameri rule through enslaved gods, succession and world-scale political conflict. One-pass covers OL 7716902/7360457/7623354; Awakened Kingdom had no usable OL cover. YAML 1epa0twDSdl6vHjwOX8kBQatXzDy11d1B.
- Commit 15fcfed deployed. Gate 112 nodes/319 works, refs consistent; deployed HTML byte-identical. Both routes fresh-loaded and 4-book grid pixel-verified at `/downloads/cloud-browser-20260915-104028.png`. Progress next=226 processed=226 added=178. Neither leaf is at 10.

## 2026-09-15 13:07 CEST — intake 226–227
- 226 The Incomplete Enchanter -> original 3-volume card in portal-fantasy (now 9): The Incomplete Enchanter, The Castle of Iron, Wall of Serpents. SFE records the original Pratt/de Camp sequence; Baen describes psychologists traveling from our world to parallel worlds where magic works and our myths/literatures are real, reached by symbolic logic. The crossings structure the sequence. One-pass OL 7394487 surreal hand-and-eyes flat English cover; later books had no usable OL results in the same series pass. YAML 1T1J4SgSyRg_FF8akKOWcRSrPbnQqNx82.
- 227 The Infernal Desire Machines of Doctor Hoffman -> fabulation (now 4). SFE calls it a quest into dream and identifies appearance/reality as central; desire machines dissolve the narrated world's stability. One-pass OL 12699047 King Penguin orange wind-up organic-machine cover, flat English title. YAML 10MgY4rYQ2wMiyjYfnTQSEHgqIUo7Ooya.
- Commit c291857 deployed; gate 112 nodes/321 works, refs consistent and deployed HTML byte-identical. Both routes fresh-loaded; Hoffman pixels verified at `/downloads/cloud-browser-20260915-110734.png`. Progress next=228 processed=228 added=180. Portal fantasy is 9; neither leaf at 10.

## 2026-09-15 13:20 CEST - Operation Save Cyberpunk complete
- Commit e24e08c deployed.
- Techno Fiction is a pure intermediate under Future of Earth fiction with children Robots and AI, Cyberpunk, Technomorphosis.
- Robots and AI: 5 cards. Cyberpunk: 3 cards. Technomorphosis: 3 cards. Space Techno Fiction remains terminal with stable ID techno-fiction-in-space.
- Eight moved Drive YAML records had leaf/deep links updated. Drive genre metadata/readmes updated or created. Empty obsolete Techno works folder trashed.
- Cache-busted live Technomorphosis route and pixels verified; portrait and three fiction cards render correctly.

## 2026-09-15 15:52 CEST - intake 234-235
- 234 The Prestige -> fabulation (now 6). SFE calls it central late-20th-century Fantastika, sui generis and Equipoisal between SF and fantasy, conjoining stage/perhaps literal magic with Tesla matter transmission/duplication while refusing reliable readings; self-conscious misdirection and unstable narration make Fabulation the closest current leaf. Sources: https://sf-encyclopedia.com/entry/priest_christopher and https://christopher-priest.co.uk/books/the-prestige. One-pass OL 8419414, English film-tie-in optical artwork; title/author visible. YAML 1iiT0S9sLmVCb9remgLb0DYuviEV8L7ks.
- 235 The Satanic Verses -> magic-realism (now 6). SFE frames Rushdie's novels as Fabulation/Magic Realism and the book as an anatomy of religion in fantasy terms; PRH describes modern reality where transformations and miracles merge the actual and imagined. Sources: https://sf-encyclopedia.com/entry/rushdie_salman and https://www.penguinrandomhouse.com/books/139559/the-satanic-verses-by-salman-rushdie/. One-pass OL 8312209, original English Viking cover with title/author visible. YAML 1pRi2Km4nKtj3hZa_vnElXLgWSC81s8pL.
- Commit df9fe1d deployed. Gate 122 nodes/328 works, refs consistent; deployed HTML byte-identical. Both fiction routes cache-busted and pixel-verified: /downloads/cloud-browser-20260915-135220.png and /downloads/cloud-browser-20260915-135228.png. Progress next=236 processed=236 added=187. Neither leaf is at 10.

## 2026-09-15 16:13 CEST - intake 236-237
- 236 The Sirens of Titan -> humorous-science-fiction (now 2). SFE satire/Widescreen Baroque grounding; OL 15063413. YAML 1MYC3TjcnMcyi3tmsHnFv35UvXnQin3My.
- 237 The Space Between Worlds -> new Parallel World fiction under Atemporal (now 1). SFE 380 Parallel Worlds/Doppelganger travel grounding. New portrait 135. OL 10723957. YAML 11MN2Rq5Nndure2n_ztbgg5m409HXAMO3.
- Commit 1a25d91 deployed. Gate 123 nodes/330 works, refs consistent; deployed HTML byte-identical and both pages pixel-verified. Progress next=238 processed=238 added=189.

## 2026-09-15 16:43 CEST - intake 238-239
- 238 The Space Merchants -> 2-book Space Merchants card in social-dystopia (now 7): The Space Merchants + The Merchants' War. SFE calls it a dark satire of ruthless ad agencies dominating the world, addictive consumer products and manipulation; the designed corporate-consumer order is the central dystopia. Sources: https://sf-encyclopedia.com/entry/advertising and https://www.hachette.co.uk/titles/frederik-pohl/the-space-merchants/9780575075283/. One-pass OL 12375902, vivid English front; sequel no usable result. YAML 1wmIMnLoDaBgubHfaWRsCCXUXvy1eNnyo.
- 239 The Swords of Lankhmar -> 7-book Fafhrd and the Gray Mouser card in sword-and-sorcery (now 8). SFE identifies the cycle as central Heroic Fantasy and credits Leiber with coining Sword and Sorcery; this is volume 5. One-pass series review wired OL 10185696 (Swords of Lankhmar) and 12373476 (Swords Against Death); no hunt for others. YAML 1qxxuFQdVbf_kxbkaZ3IO_ffmRUQtg_YX.
- Commit 55ff1db deployed. Gate 123 nodes/332 works, refs consistent and HTML byte-identical. Both pages pixel-verified at /downloads/cloud-browser-20260915-144301.png and -144308.png. Progress next=240 processed=240 added=191. Neither leaf reached 10.

## 2026-09-15 17:14 CEST - intake 240-241
- 240 The Tales of Alvin Maker -> 6-book card in fantasies-of-history (now 5): Seventh Son, Red Prophet, Prentice Alvin, Alvin Journeyman, Heartfire, The Crystal City. SFE describes an Alternate-History early-19th-century USA where magic works; Macmillan says folk magic transforms frontier history. One-pass series search supplied all six OL covers: 9315050/9315058/14476036/6382372/10620724/9315019. Sources https://sf-encyclopedia.com/entry/card_orson_scott and https://us.macmillan.com/series/alvinmaker. YAML 19uly22ItcFA7cYVOgEjL_eLJvu_ZbiTr.
- 241 The Wasp Factory skipped as outside the speculative-fiction taxonomy. SFE says its psychological probing is mimetic despite surreal modern-horror narration; ISFDB marks it non-genre, and Hachette sells it as horror/suspense with no speculative mechanism. Sources https://sf-encyclopedia.com/entry/banks_iain_m and https://www.hachette.co.uk/titles/iain-banks/the-wasp-factory/9780349147161/.
- Commit 2e99fa7 deployed. Gate 123 nodes/333 works, refs consistent and HTML byte-identical. Six-book grid pixel-verified at /downloads/cloud-browser-20260915-151419.png. Progress next=242 processed=242 added=192. No leaf reached 10.

## 2026-09-15 17:54 CEST - intake 242-243
- 242 The Way of Kings -> 5-book Stormlight Archive card in hard-magic (now 4): Way of Kings, Words of Radiance, Oathbringer, Rhythm of War, Wind and Truth. Sanderson foregrounds designed magic systems; Macmillan identifies magical Roshar and the five-book first arc. One-pass OL matching covers 14658316/14658334/14658111/14658361/14836765; visually reviewed together. Sources https://www.brandonsanderson.com/pages/the-stormlight-archive-series and https://us.macmillan.com/series/thestormlightarchive. YAML 1eRI6hdwUSycL-DmaqEkXIoFcEfdGimgW.
- 243 The Well of the Unicorn -> heroic-fantasy (now 8). SFE calls it a Bildungsroman in a world subtly irradiated by magic; the protagonist's growth through rebellion, war and moral leadership is a secondary-world heroic struggle. OL 11742072, illustrated English Ballantine front. Source https://sf-encyclopedia.com/entry/pratt_fletcher. YAML 1mUcyyafITOoIS8eHAX0Ei1nWLcF4uBxd.
- Commit 4270c0d deployed. Gate 123 nodes/335 works, refs consistent and HTML byte-identical. Both routes pixel-verified at /downloads/cloud-browser-20260915-155423.png and -155431.png. Progress next=244 processed=244 added=194. No leaf reached 10.

### 2026-09-15 18:21 CEST - intake 244-245 shipped
- Commit `2cab3e2` deployed two accepted cards; 123 nodes / 337 works.
- The Yiddish Policemen's Union (Michael Chabon, 2007) -> `alternate-history`. SFE explicitly identifies it as Alternate History SF; selected original Will Staehle English cover OL 12745212 in one pass.
- Three Hearts and Three Lions (Poul Anderson, 1961) -> `eldrich-rifts`. SFE identifies a Parallel World fantasy and the translation from wartime Denmark into magical Faerie makes the reality rupture defining; selected OL 407701 over audiobook-style OL 12022738 in one pass.
- Local gate passed; Drive work YAMLs uploaded; progress advanced to next=246, processed=246, added=196.
- GitHub Pages byte identity confirmed; alternate-history and eldrich-rifts routes rendered with 8 and 6 fictions respectively; screenshots saved.

### 2026-09-15 19:15 CEST - intake 246-247
- 246 Tigana -> political-fantasy (now 6). Penguin Random House describes a magically cursed homeland under a despotic conqueror and a rebel campaign to overthrow him and restore its erased name; tyranny, conquest and liberation drive the fantasy. One-pass OL review selected 6821480, the strongest colorful painted English front. YAML 1p-d_K-du6t4uNuyudc5WyfOwgh7FSBTk.
- 247 Time and Again -> 2-book card in timeslips (now 2): Time and Again + From Time to Time. SFE calls the novel Time Travel equipoising SF/fantasy and identifies self-hypnosis as the key, so its psychological non-machine transit into 1882 fits Timeslips. One-pass OL review wired 3841920 and sequel 405925. Sources https://sf-encyclopedia.com/entry/finney_jack, https://sf-encyclopedia.com/entry/hypnosis, https://www.simonandschuster.com/books/Time-and-Again/Jack-Finney/9781982146016. YAML 1weI1x_MIPlulQX9gUZgnVodLVYm0mDEO.
- Commit 15980aa deployed. Gate 123 nodes/339 works, refs consistent; deployed HTML byte-identical. Both deep links fresh-loaded and pixel-verified. Progress next=248 processed=248 added=198. No leaf reached 10.

### 2026-09-15 19:43 CEST - intake 248-249 + cover ride-along
- 248 Titus Alone deduped into the existing 3-book Gormenghast card in isolationist-fantasy; no new fiction card. SFE and Penguin confirm it is the third/final published Gormenghast volume, following Titus beyond the sealed castle. One-pass OL review selected 11730144, a detailed painted English front, and wired it as the third per-book cover. Drive Gormenghast YAML updated in place: 1pTZ9yI8ceG_IGQG3m61YcNT-cn4kO11Z.
- 249 Uncle Silas skipped as non-speculative Victorian Gothic/sensation fiction. Penguin describes a psychological thriller whose villain, son and governess plot to murder Maud for her inheritance; no supernatural mechanism is asserted. Sources https://www.penguinrandomhouse.com/books/261054/uncle-silas-by-joseph-sheridan-le-fanu-edited-with-an-introduction-and-notes-by-victor-sage/ and https://www.penguin.co.uk/books/34473/uncle-silas-by-fanu-j-le/9780141958880.
- Commit 456c87c deployed; gate 123 nodes/339 works, refs consistent, public HTML byte-identical. Gormenghast 3-book grid pixel-verified with new Titus Alone art. Progress next=250 processed=250 added=198. No leaf reached 10.

### 2026-09-15 20:06 CEST - intake 250-251
- 250 Under the Skin -> anthropological-science-fiction (now 7). SFE describes an alien female surgically altered as human who classifies and farms humans as livestock/primates; the inverted anthropological gaze, species norms and observer assumptions drive the novel. Sources https://sf-encyclopedia.com/entry/faber_michel and https://canongate.co.uk/books/26-under-the-skin/. One-pass OL 8260688, stark English road image. YAML 1sDYaMu9sdxSoSIA7-F_uwG-PwHNypBnX.
- 251 Vathek -> evil-deals (now 4). Sourcebooks/OUP describe the caliph accepting the Giaour's path to forbidden knowledge and power, sacrificing innocents, faith and ultimately his soul; the bargain with evil is the engine. One-pass OL 15200443, vivid green/yellow illustrated English front. Sources https://www.sourcebooks.com/9781492699743-vathek-tp.html and https://www.oupjapan.co.jp/en/node/13105?language=en. YAML 1jtKBv09hdZWji-LyUoy4dMTPnQwwLgKM.
- Commit 6e73360 deployed. Gate 123 nodes/341 works, refs consistent and public HTML byte-identical. Both deep links fresh-loaded and pixel-verified. Progress next=252 processed=252 added=200. No leaf reached 10.

### 2026-09-15 20:20 CEST - Operation no-history-slush-bucket complete
- Owner authorization relayed from exact 20:07:25 CEST message: "Execute operation no-history-slush-bucket." Executed approved shape in commit 37cc6ba; gate 125 nodes / 341 works, refs consistent, deployed HTML byte-identical.
- Historical fantasy now has six children: Gaslight fantasy 5, Secret history 3, Rococo fantasy 1, Andalusian fantasy 1, Nordic fantasy 3, Celtic fantasy 1. Fantasies of history removed.
- Secret history strict test encoded: documented history secretly explained by hidden magic, and secrecy is a main theme; public magic disqualifies. Cards: Declare, Aegypt Cycle, Once and Future Witches.
- Kingdom of Back -> new Rococo fantasy; Bird King -> new Andalusian fantasy; Tales of Alvin Maker -> Alternate history (now 9).
- Generated and visually approved detailed colorful 2:3 portraits 136/137/138; all three live routes and Alvin Maker deep link pixel-verified.
- Drive: three new leaf + works folders, genre metadata and portraits uploaded; six YAMLs moved and breadcrumbs updated; old Fantasies of history folder trashed; historical/gaslight genre metadata updated.

### 2026-09-15 20:45 CEST - Historical fantasy three-way structure complete
- Owner authorization verified by main from live iMessage: phonemsg-01M2K5XZB816735KFXAN8NKBB4 at 20:40:37 CEST, exact body "Execute". Commit 1a8a3f4 deployed; gate 127 nodes / 341 works, refs consistent, public HTML byte-identical.
- Historical fantasy now exactly: Period fantasy, Secret history, Alternate history fantasy.
- Period fantasy intermediate inherits Historical fantasy art and parents Gaslight, Nordic, Celtic, Rococo and Andalusian. Definition: historical era is stage, not puzzle; history neither secretly explained nor rewritten.
- Alternate history fantasy new leaf contains unambiguous magic-plus-divergence siblings Tales of Alvin Maker and Temeraire. SF Alternate history returns to 8; Gaslight returns to 4. Definition: divergent timelines where magic is the engine, history openly rewritten and world runs on magic.
- Sibling audit left borderline Babel and Jonathan Strange in Gaslight; both are magical counterhistories but not moved without a ruling under the instruction. Once and Future Witches remains Secret history because secrecy is its main historical mechanism.
- Generated two detailed colorful 1024x1536 portrait variants; variant A is live, variant B retained in Drive and delivered for the curator's choice. Historical, Period and Alternate history fantasy routes pixel-verified.

### 2026-09-15 20:59 CEST - intake 252-253 + Norse rename
- 252 Watchmen -> alternate-history (now 9). SFE calls it an Alternate History superhero story; heroes alter politics/science, producing a 1985 where America won Vietnam, Nixon remains president and nuclear war looms. One-pass OL selected iconic Absolute yellow clock cover 14613329; graphic novel credited Alan Moore/Dave Gibbons. YAML 1jij5INW9eHSdSsh8-kLAa1_cG2WWXBoB.
- 253 11/22/63 -> timeslips (now 3). King/S&S: diner storeroom portal fixed to 1958 and mission to prevent Kennedy assassination; unexplained non-machine portal makes Timeslips the mechanism. One-pass OL 10713447, English newspaper/JFK cover. YAML 1IS5ZxYcxJ-25E8wyPzEyAQfK4obfAIYA.
- Commit 6f35ba7 added both; gate 127 nodes/343 works. Progress next=254 processed=254 added=202.
- Owner-approved rename, source phonemsg-01M2K6T9S2K9SDH5230VVPT3QB: Nordic fantasy -> Norse fantasy. Commit 902b693. Stable scope, ID changed to norse-fantasy and redirect nordic-fantasy -> norse-fantasy added. Drive folder renamed; three work YAML breadcrumbs updated; genre metadata uploaded.
- Final deployed HTML byte-identical. Watchmen, 11/22/63, Norse route and old Nordic redirect all fresh-loaded; pixels verified.

### 2026-09-15 21:19 CEST - Period fantasy portrait selected and deployed
- the curator selected time-gallery variant A via owner message phonemsg-01M2K7PPGMBWFF2D771CS4B1A6.
- Commit be31366 wires new 140-period-fantasy.webp; detailed colorful 1024x1536 gallery with five era vistas. Drive portrait uploaded: 1-lLIYzITbe9grQctU12dfXrWH93En5Gs.
- Gate 127 nodes/343 works; deployed HTML byte-identical; Period fantasy route fresh-loaded and pixel-verified with five child cards.

### 2026-09-15 21:24 CEST - intake 254-255
- 254 334 -> Social dystopian future (now 8). SFE describes a near-future social portrait of degraded 2025 Manhattan, shaped by crowding, deprivation and authorities treating humans harshly; PRH foregrounds rationed babies, sanctioned addiction and institutional decay. The systemically sick society rather than one police state is the defining dystopia. One-pass OL selected 228652, a clean English Vintage front with stark public-housing television/tile image. YAML 1Mq8xNI-YXhaeFIk7M8aZLRm2xdtTUift.
- 255 A Blade So Black -> 3-book Nightmare-Verse card in Whimsical doors (now 4): A Blade So Black, A Dream So Dark, A Crown So Cursed. Macmillan calls it an Alice in Wonderland reimagining in which an Atlanta teen fights monsters in Wonderland and repeatedly crosses the Veil; the enchanted two-world threshold is the defining mechanism. One-pass series review selected coherent illustrated OL fronts 10198641/9191518/10142452. YAML 1eG07A_DmIELobEVBZnXQYY4iit7Yj7Re.
- Commit 819dee8 deployed. Gate 127 nodes/345 works, refs consistent; public HTML byte-identical. Both fiction pages fresh-loaded and pixel-verified, including Nightmare-Verse's three-book grid. Progress next=256 processed=256 added=204. Neither leaf reached 10.

### 2026-09-15 21:30 CEST - intake 256-257
- 256 A Brightness Long Ago -> political-fantasy (now 7). PRH/Hachette set the fantasy in an invented world evoking early Renaissance Italy, driven by rival mercenary commanders, rulers, assassination, courts and religious power; political rivalry is the main engine. One-pass OL selected 8794618, a bold red/orange English front. YAML 1UryPfk-AQW-fBkAGljOh_mRcQeEZfQMc.
- 257 A Broken Darkness -> 3-book Beneath the Rising card in ancient-tormentors (now 6): Beneath the Rising, A Broken Darkness, The Void Ascendant. SFE identifies greedy elder gods and portals repeatedly exposing the world to profound evil; the official publisher confirms the cosmic trilogy. One-pass series review used OL 10208841 plus matching official publisher fronts for books 2/3. YAML 1cesQlAheBt5CDlukshBlcH-RNTOiT5vJ.
- Commit 1a8e691 deployed. Gate 127 nodes/347 works, refs consistent; public HTML byte-identical. Both fiction pages fresh-loaded and pixel-verified, including Beneath the Rising's full three-book grid. Progress next=258 processed=258 added=206. Neither leaf reached 10.

### 2026-09-15 21:39 CEST - anchor-test definitions staged
- Corrected directive scope: no card moved. The Witch's Heart is not currently in the taxonomy; The Weaver and the Witch Queen remains Norse fantasy pending the curator's answer about adding the distinct Witch's Heart card.
- Staged for the next intake commit: Period fantasy anchors to a documented era/source chronicles; Mythic retelling anchors to an inherited story/source the myth itself; Homeric Greece and Arthurian Britain are retelling territory. Local gate passes; not separately pushed per main's instruction.
- the curator closed the Witch's Heart fork at 21:52 (phonemsg-01M2KA18TA2YDTQ60XBCK5MJ3A): no manual add and no move. If it reaches normal intake, classify it as Mythic retelling under the anchor test.

### 2026-09-15 21:59 CEST - intake 258-259 + anchor definitions
- 258 A Children's Bible -> climate-catastrophe (now 3). SFE describes a very-near-future cascade of disasters from earlier generations' destruction of the human home, with a hurricane supplying the Flood; Norton calls it climate/cultural unraveling. One-pass OL selected 9426320, green illustrated English front. YAML 1GUHZ1rM2cZQcXJIaMZeoO4hlKOFE1AcX.
- 259 A Chorus Rises -> 2-book A Song Below Water card in publicly-paranormal (now 2): A Song Below Water + A Chorus Rises. Tor describes contemporary Black sirens and a famous Eloko within today's media/social systems; public exposure and civic life define it. One-pass OL 10131365/10630605, coordinated colorful illustrated English fronts. YAML 19uEFEoOyb4IJ7DKJNXN-omLTEPFh8sqr.
- Commit a2ff00b deployed, including the approved Period fantasy/Mythic retelling anchor definitions. Gate 127 nodes/349 works, refs consistent; public HTML byte-identical. Both fiction pages fresh-loaded and pixel-verified, including the 2-book grid. Progress next=260 processed=260 added=208. Neither leaf reached 10.
- Push correction: first commit 1df6fdb accidentally staged deletion of three prior YAML files when cleaning an empty wrong path; caught immediately after push, restored them and force-with-lease amended main to a2ff00b before deployment. No data cards or live deployed content were lost; final repo is clean.

### 2026-09-15 22:29 CEST - intake 260-261
- 260 A Clash of Kings deduped into existing 5-book A Song of Ice and Fire card in political-fantasy; no new fiction. PRH/Harper confirm it is book 2. One series-pass cover review wired OL 8231751 to book 2; other missing volume covers remain for future biggest-first passes. Drive ASOIAF YAML 1n3lpsu0fmOGeQ9GoXTsTkZt-x-DBDg7F.
- 261 A Connecticut Yankee in King Arthur's Court -> timeslips (now 4). SFE identifies it as SF and specifically cites the crowbar blow as a Timeslip into the past; Penguin confirms unconscious Hank wakes in sixth-century Camelot. The accidental unexplained transfer, not inherited Arthurian story, is defining under the anchor rule. One-pass OL 9168732, antique red illustrated English front. YAML 1wvLolY0I1Awf8P0BlJSKSJJIQP3QVPBO.
- Commit 1922858 deployed. Gate 127 nodes/350 works, refs consistent; public HTML byte-identical. ASOIAF grid pixel-check shows Clash cover newly filled; Connecticut Yankee fiction page pixel-verified. Progress next=262 processed=262 added=209. Neither leaf reached 10.

### 2026-09-15 22:59 CEST - intake 262-263
- 262 A Darker Shade of Magic -> new 3-book Shades of Magic card in eldrich-rifts (now 7): A Darker Shade of Magic, A Gathering of Shadows, A Conjuring of Light. Schwab/Tor/Macmillan describe Antari traveling among parallel Londons where magic differs; magical inter-world crossings define the trilogy. One-pass OL 7410930/7990183/7990184, coherent cream/red/black illustrated English set. YAML 1s4Aa2VJ3XYvlmgRdaFImDRnO_vNY0fgl.
- 263 A Dream So Dark deduped into the existing complete Nightmare-Verse card; no data change. Macmillan identifies it as sequel/book 2, already present with OL 9191518 and pixel-verified at its book route.
- Commit 5bd4e01 deployed. Gate 127 nodes/351 works, refs consistent; public HTML byte-identical. Shades full grid and Dream book page fresh-loaded/pixel-verified. Progress next=264 processed=264 added=210. Neither leaf reached 10.

### 2026-09-15 23:30 CEST - intake 264-265
- 264 A Feast Unknown -> 3-book Lord Grandrith / Doc Caliban card in fabulation (now 7): A Feast Unknown, Lord of the Trees, The Mad Goblin. SFE calls it an exploration/satire of fantasies latent in heroic fiction and a tribute to Tarzan/Doc Savage; Farmer confirms the deliberate rewrites/manipulation by the Nine. Self-aware pulp pastiche makes Fabulation closest. One-pass OL 7376512/7748239/10370591. YAML 13IHwwnKPGNdHoo1skqTJjCEax-v_GUEt.
- 265 A Fine and Private Place -> ghost-story (now 8). S&S explicitly calls it a classic ghost story centered on a cemetery recluse among the newly dead and two ghostly lovers. One-pass OL 294663, detailed illustrated cemetery/raven English front. YAML 1YNVDRwyyEq6IsOwy0AVSsiTEadoH3fo6.
- Commit 3dea441 deployed. Gate 127 nodes/353 works, refs consistent; public HTML byte-identical. Both fiction pages fresh-loaded/pixel-verified, including Grandrith's 3-book grid. Progress next=266 processed=266 added=212. Neither leaf reached 10.

### 2026-09-16 00:01 CEST - intake 266-267
- 266 A Glastonbury Romance -> mythic-retelling (now 8). SFE says it conflates Joseph of Arimathea with its contemporary protagonist and evokes the Holy Grail; Penguin describes modern Glastonbury under older forces and Grail legend. Under the anchor rule its source is inherited Grail story, not documented era. One-pass OL 675174. YAML 1-D-DITIVVIOpMwqCWgOtz6mLr_RwwZUA.
- 267 A Little Hatred -> 3-book Age of Madness card in political-fantasy (now 8): A Little Hatred, Trouble with Peace, Wisdom of Crowds. Abercrombie/Orbit: crown, banks, industry, war, class unrest and ambitions reshape the Union while magic lingers; competing powers drive it. One-pass OL 14543428/14543432/14543429. YAML 1LzUyuOrzd6KIOlgKdoH2t3fWa2VM8o8l.
- Commit 4ab4175 deployed. Gate 127 nodes/355 works, refs consistent; public HTML byte-identical. Both fiction pages fresh-loaded/pixel-verified, including Age of Madness 3-book grid. Progress next=268 processed=268 added=214. Neither leaf reached 10.

### 2026-09-16 00:34 CEST - intake 268-269
- 268 A Man in the Zoo skipped as non-speculative social/allegorical fable. SFE says it plays lightly with the constricting atmosphere of Zoo stories by supplying a human volunteer; the complete public-domain text confirms that John voluntarily contracts to be exhibited and is released to marry, with no impossible mechanism. Sources https://sf-encyclopedia.com/entry/garnett_david, https://sf-encyclopedia.com/entry/zoo, https://www.gutenberg.org/ebooks/66090.
- 269 A Master of Djinn -> complete 3-book Dead Djinn Universe card in alternate-history-fantasy (now 3): A Dead Djinn in Cairo, The Haunting of Tram Car 015, A Master of Djinn. SFE calls the Ministry of Alchemy sequence detective fiction in an Alternate-World Egypt where supernatural creatures interact with society; Clark says al-Jahiz opened the veil between magical and mundane realms forty years before 1912 and transformed the world. Working magic openly rewrites modern history, so Alternate history fantasy is defining rather than mystery alone. One-pass OL 8542858/8566730/10457293. YAML 1dtO-5tsjrxqaKYSB75fXdWAsi85EIPKh.
- Commit 033436d deployed. Gate 127 nodes/356 works, refs consistent; public HTML byte-identical. Dead Djinn 3-book grid fresh-loaded/pixel-verified at /downloads/cloud-browser-20260915-223412.png. Progress next=270 processed=270 added=215. No leaf reached 10.

### 2026-09-16 01:03 CEST - intake 270-271
- 270 A Peculiar Peril -> eldrich-rifts (now 8). Macmillan calls it portal fantasy spanning surreal through-the-looking-glass alternate-history worlds; three doors in an inherited English mansion lead to Aurora, where magic abounds and history is rewritten. The uncanny multi-reality rupture is its entry mechanism, so Eldrich rifts is closer than the historical setting inside the destination. One-pass OL 10520614, detailed floral/animal English front. Sources https://us.macmillan.com/series/themisadventuresofjonathanlambshead, https://www.panmacmillan.com.au/9780374308865/. YAML 1YELqngjrRACF5EB5c7Ng8KjaBSo-alnj.
- 271 A Room Away From the Wolves -> ghost-story (now 9). Hachette and Suma call Catherine House a haunted boarding house with strange voices, dark secrets and girls who may not be what they seem; the publisher explicitly calls it a spellbinding ghost story. One-pass OL 8567714, clean purple illustrated English front. YAML 1OYXdqLP1V8yo0vYa-azfO0j7zSVFftLX.
- Commit c012c0a deployed. First QA caught the initially selected OL 13286436 was an audiobook package despite a clean thumbnail; amended before report to OL 8567714 and force-with-lease updated main. Gate 127 nodes/358 works, refs consistent; public HTML byte-identical. Both fiction pages fresh-loaded/pixel-verified at /downloads/cloud-browser-20260915-230204.png and /downloads/cloud-browser-20260915-230333.png. Progress next=272 processed=272 added=217. Neither leaf reached 10; Ghost story is now 9.

### 2026-09-16 01:35 CEST - intake 272-273
- 272 A Scanner Darkly -> technomorphosis (now 4). SFE calls it Dick's most prolonged exploration of drug-altered perception; Penguin says Substance D splits the user's brain into combative identities until undercover Fred does not know he is surveilling himself as Bob Arctor. Engineered drug plus identity-masking surveillance transform mind, selfhood and social order. One-pass OL 911131, detailed blue hand/flowers English SF Masterworks front. Sources https://sf-encyclopedia.com/entry/perception, https://sf-encyclopedia.com/entry/drugs, https://www.penguinrandomhouse.com/books/40609/a-scanner-darkly-by-philip-k-dick/. YAML 11eLI904CcRdlabp3VnUh6L_QJhBSPg5Z.
- 273 A Sick Gray Laugh -> fabulation (now 8). Word Horde follows a horror author writing a purported nonfiction town history while the Grayness may be malaise, delusion or invasive force; PW describes Cushing's novel and Noelle's work-in-progress exploring the same town. The unstable author-double and book-inside-book use storytelling reliability as fantastic device. One-pass publisher front by Jacob Cornelisz van Oostsanen/Matthew Revert, detailed jester painting and English title. Sources https://wordhorde.com/books/a-sick-gray-laugh/, https://www.publishersweekly.com/9781939905529. YAML 1FIU5u7RgND3SQVqs3iAFVa0ByycWfbhM.
- Commit 1480056 deployed. Gate 127 nodes/360 works, refs consistent; public HTML byte-identical. Both fiction pages fresh-loaded/pixel-verified at /downloads/cloud-browser-20260915-233504.png and /downloads/cloud-browser-20260915-233510.png. Progress next=274 processed=274 added=219. Neither leaf reached 10.

### 2026-09-16 02:04 CEST - intake 274-275
- 274 A Song Below Water deduped into existing complete two-book A Song Below Water card in publicly-paranormal; no data change. The card already contains A Song Below Water (2020, OL 10131365) and A Chorus Rises (2021, OL 10630605), sourced to Tor and pixel-verified in intake 258-259.
- 275 A Song for a New Day -> totalitarian-dystopia (now 8). SFE calls it a Near Future Dystopian America where government answers unrest/pandemic by enforcing solitariness; Penguin says terror and deadly viruses lead to a ban on public gatherings and concerts, with musicians performing illegally while corporate virtual entertainment replaces live connection. State prohibition and enforcement drive it. One-pass OL 8780333, vibrant yellow/teal musician English front. Sources https://sf-encyclopedia.com/entry/pinsker_sarah, https://www.penguinrandomhouse.com/books/598452/a-song-for-a-new-day-by-sarah-pinsker/. YAML 1x1lUz7MolASlNI6w2dfWdHhduC05t-4y.
- Commit 6b80446 deployed. Gate 127 nodes/361 works, refs consistent; public HTML byte-identical. New Day fiction fresh-loaded/pixel-verified at /downloads/cloud-browser-20260916-000343.png. Progress next=276 processed=276 added=220. No leaf reached 10.

### 2026-09-16 03:06 CEST - intake 276-277
- 276 A Storm of Wings -> complete four-work Viriconium card in dying-earth (now 5): The Pastel City, A Storm of Wings, In Viriconium, Viriconium Nights. SFE describes Far-Future science fantasy on a bleak Dying Earth, with Viriconium the City at the end of time; Storm recasts alien invasion through insectoid perception. PRH's collected edition confirms the four core works. One-pass covers: OL 9410274, Goodreads/Sphere 304254, OL 8586480/13507449; PRH omnibus default. YAML 1F0yXg5DeeqtPWYbGPmapo5W8kGETqziU.
- 277 A Strange Manuscript Found in a Copper Cylinder -> satirical-utopia (now 2). SFE calls it an Antarctic Utopia and Lost-Race novel whose inverted society dismantles imperial assumptions; Broadview says the Kosekin value death, abjection and poverty against civilized norms. Designed social inversion is the engine, closer than adventure-only Lost world. One-pass OL 5647709, black/gold illustrated English front. YAML 1H0NfZhe4ZjSYPbpoesi2HqPn78CkPmy_.
- Commit 8e6bc65 deployed. Gate 127 nodes/363 works, refs consistent; public HTML byte-identical. Both pages fresh-loaded/pixel-verified at /downloads/cloud-browser-20260916-010542.png and /downloads/cloud-browser-20260916-010549.png. Progress next=278 processed=278 added=222. No leaf reached 10.

### 2026-09-16 03:38 CEST - intake 278-279
- 278 A Wizard's Guide to Defensive Baking -> fantasy-mystery (now 3). Argyll says bread-magician Mona finds a corpse, faces an assassin targeting magic folk, and follows that threat as the city loses its wizards. The murder investigation depends on specialized magic. One-pass OL 10296774. YAML 10ODHqFx7bMitnh_8eNrR0_AW0ILCrjjP.
- 279 queue typo Ada or Ador normalized to Ada or Ardor -> fabulation (now 9). SFE says its Alternate History/anti-Terra may be Van Veen's Godgame and stresses Nabokov's shaping of the creative act over SF causality; Penguin calls it fairy tale, epic, time treatise and parody of novel history. Self-conscious construction and unstable world make Fabulation closer than literal Alternate history. One-pass OL 14381967. YAML 1d1fE8o17LH_Ok5Iujuuw71FyPUJie9et.
- Commit bba5715 deployed. Gate 127 nodes/365 works, refs consistent; public HTML byte-identical. Both fiction pages fresh-loaded/pixel-verified at /downloads/cloud-browser-20260916-013807.png and /downloads/cloud-browser-20260916-013710.png. Progress next=280 processed=280 added=224. Neither leaf reached 10; Fabulation is now 9.

### 2026-09-16 04:08 CEST - intake 280-281 committed locally, deployment blocked
- 280 Adept's Gambit deduped into existing seven-book Fafhrd and the Gray Mouser card in sword-and-sorcery. SFE identifies it as a Fafhrd/Gray Mouser novella; ISFDB and the Swords in the Mist publication record place it within that collection, already represented as book 3. One-pass series cover pass filled the missing Swords in the Mist book cover with OL 14192616. Existing Drive YAML 1qxxuFQdVbf_kxbkaZ3IO_ffmRUQtg_YX updated.
- 281 Aetherbound -> science-fantasy (now 7). SFE says it equipoises Space Opera and Magic, following gene-mage Pendt into rebellion on a space habitat; Penguin centers her genetic mutation, long-haul space cruiser escape and station takeover. Explicit magic-and-space blend makes Science fantasy closest. One-pass OL 10840472, colorful illustrated English front. YAML 1-CwgloJhYGCtt1xBvs5EfaaIDLj4-ICb.
- Local commit 89426eb. Gate 127 nodes/366 works, refs consistent. Progress next=282 processed=282 added=225. Push failed because the protected credential/helper installed during recovery was absent at this wake; origin remains HTTPS. Per overnight directive intake remains unblocked and the commit is retained locally. Deployment and pixel QA await the push backlog. Neither leaf reached 10.
- 04:13 CEST auth/deploy recovery: parent approved standing self-heal. Minted `sff-taxonomy push 2026-09-16b`, expiry Oct 15, scoped only to GuSoder/sff-taxonomy-browser with Contents read/write + required Metadata read-only. Persisted 0600 ~/.git-credentials and global credential.helper=store, updated the agent vault item, pushed 89426eb, verified origin/main exact and public HTML byte-identical. Fresh-tab pixel QA passed for Aetherbound and Swords in the Mist at /downloads/cloud-browser-20260916-021300.png and /downloads/cloud-browser-20260916-021303.png. Previous 19690264 orphan revocation was attempted, but the GitHub delete control did not expose a stable confirmation action; it remains present and never used. Do not mint another unless push auth is missing; standing self-heal is to repeat this recovery then.

### 2026-09-16 04:39 CEST - intake 282-283
- 282 Affinity skipped as non-speculative historical Gothic. Hachette poses disgraced spiritualist Selina as fraud or prodigy; Kirkus says flashbacks disclose the truth behind her supposed powers. The séance effects are a human deception rather than actual magic, so it does not cross the taxonomy's speculative boundary. Sources https://www.hachette.co.uk/titles/sarah-waters/affinity/9780349018492/ and https://www.kirkusreviews.com/book-reviews/sarah-waters/affinity/. Initial local placement was caught during final reasoning/QA and removed before the reported deployed state; its stray Drive YAML was trashed.
- 283 After London; or, Wild England -> ruined-earth (now 5). SFE calls it an early Scientific Romance and Ruined Earth tale: England has reverted to wilderness and barbarism after an unspecified disaster, with a great inland lake over polluted London; Hachette calls it early post-apocalyptic fiction. Successor society amid transformed ruins makes Ruined Earth closest. One-pass OL 10242194, detailed forest English front. YAML 1nMrG_RsqVW4eYe1Wi9faJoxqZAhy-x8G.
- Commit 520a5b7 deployed. Gate 127 nodes/367 works, refs consistent; public HTML byte-identical. After London page fresh-loaded/pixel-verified at /downloads/cloud-browser-20260916-023754.png. Progress next=284 processed=284 added=226. No leaf reached 10.

### 2026-09-16 05:09 CEST - intake 284-285
- 284 Agency -> complete current 2-book Peripheral sequence card in alternate-history (now 10): The Peripheral + Agency. SFE identifies Agency as volume two and says manipulation of Alternate Histories is central; Penguin confirms different timelines and later actors nudging alternate pasts. One-pass OL 8787492/13090570. YAML 1Fn3BPee6BS0P4FIokYdAjdvSiBTutIDA.
- 285 Ahab's Return; or, The Last Voyage -> fabulation (now 10). SFE says Ahab survives while Ishmael has written Moby-Dick; PW says Moby-Dick is a fictionalized version of reality. Making the canonical novel an unreliable artifact inside its own continuation foregrounds storytelling as the fantastic device. One-pass OL 14290189. YAML 1owKHweYiPUJUknGJqtYqxxoTRtykun0p.
- Commit f7bd919 deployed. Gate 127 nodes/369 works, refs consistent; public HTML byte-identical. Both pages fresh-loaded/pixel-verified at /downloads/cloud-browser-20260916-030912.png and /downloads/cloud-browser-20260916-030913.png. Progress next=286 processed=286 added=228.
- Both Alternate history and Fabulation reached 10. No unilateral restructure. Fabulation sourced split proposal prepared at /tmp/fabulation-split-proposal.yaml: Fictionality fabulation (story artifacts/authorship) vs World-instability fabulation (mutable world/history/identity), both under the existing Fabulation umbrella and grounded in SFE's definition. Alternate history requires its own sourced proposal next cycle.

### 2026-09-16 05:40 CEST - intake 286-287
- Pending max-10 work completed: Alternate history split proposal prepared at /tmp/alternate-history-split-proposal.yaml. Proposed existing Alternate history as umbrella over Counterfactual history (fixed divergent course, 9 cards) and Manipulated timelines (cross-timeline intervention, Peripheral). Grounded in SFE Alternate History/Jonbar Point and Gibson. Proposal only, no live restructure.
- 286 Air (Or, Have Not Have) -> technomorphosis (now 5). SFE says Air's network technology embeds itself in Mae until she in a sense becomes it, forcing her to guide a traditional village into a transformed information world; Hachette centers technology, information overload and social change. Tech merging with mind and reorganizing community is Technomorphosis. One-pass official Hachette English front. YAML 1qeqMJL42DusOrOhU4WJhWESU3AMHdsaF.
- 287 Alas, Babylon -> post-holocaust-survival (now 7). SFE says nuclear war leaves Fort Repose surviving first consequences, then follows the small town coping and modestly flourishing. Lived aftermath and community survival define it. One-pass OL 2540438. YAML 103TcGtedaq2gMV8dA6GHnC0fdrNg9XuT.
- Commit dd64ca1 deployed. Gate 127 nodes/371 works, refs consistent; public HTML byte-identical. Both pages fresh-loaded/pixel-verified after 10-second cover settle at /downloads/cloud-browser-20260916-033957.png and /downloads/cloud-browser-20260916-033958.png. Progress next=288 processed=288 added=230. No new leaf reached 10.

### 2026-09-16 06:10 CEST - intake 288-289
- 288 All Our Hidden Gifts -> complete 3-book Gifts trilogy in contemporary-fantasy (now 6): All Our Hidden Gifts, The Gifts That Bind Us, Every Gift a Curse. Walker identifies the trilogy and describes Maeve's coven using telepathy, telekinesis, sparks and healing in present-day Ireland. Actual magic entering ordinary teenage/civic life makes Contemporary fantasy closest. One-pass coordinated official Walker fronts. YAML 19sgtoyOstN8MYa7j_Rn_Q8W4u5HiuQnm.
- 289 All Systems Red -> complete current 8-book Murderbot Diaries card in robots-and-ai (now 6), through Platform Decay (2026). SFE centers the Robot-cum-Cyborg SecUnit that hacks its governor module and develops independent agency; Macmillan frames an android discovering itself and consciousness through AI. One-pass official Macmillan series fronts. YAML 1Qvig57lGs_UUZwoRmVSjnwlmgLlDxkn0.
- Commit 0e5886e deployed. Gate 127 nodes/373 works, refs consistent; public HTML byte-identical. Both complete grids fresh-loaded/pixel-verified at /downloads/cloud-browser-20260916-041048.png and /downloads/cloud-browser-20260916-041049.png. Progress next=290 processed=290 added=232. No leaf reached 10.

### 2026-09-16 10:53 CEST - intake 306-307
- 306 Atlas Alone -> complete four-book Planetfall card in new-space-opera (now 10): Planetfall, After Atlas, Before Mars, Atlas Alone. Penguin Random House identifies four linked standalone Planetfall novels spanning an alien-world colony, corporate Earth, Mars, and a survivor ship after Earth's destruction; Atlas Alone adds immersive virtual worlds, real killings and a concealed plan for humanity. The interplanetary, multi-society technological sweep makes New Space Opera closest. One-pass official PRH fronts for all four books.
- 307 Atomized -> social-dystopia (now 10). SFE calls it SF whose conclusion reaches fifty years into the twenty-first century, when cloning is routine; Penguin frames the novel's main body as a dissection of atomized contemporary society through two brothers. The future biological replacement grows from the sustained social critique, making Social dystopian future closer than technology-only genetics.
- Commit dae8846 pushed. Gate 131 nodes/389 works, refs consistent. Progress next=308 processed=308 added=247. New Space Opera and Social dystopia both reached 10; prepare sourced split proposals rather than restructuring.

### 2026-09-16 11:22 CEST - intake 308-309
- 308 Attack Surface -> complete three-book Little Brother card in cyberpunk (now 4): Little Brother, Homeland, Attack Surface. SFE identifies it as the third sequence novel and centers an infotech worker discovering her corporate employer enables global repression; Macmillan describes surveillance exploits built for repressive regimes and used against dissidents. Networked corporate power, invasive tech and hackers between establishment and resistance fit Cyberpunk. One-pass official Macmillan fronts.
- 309 Babel-17 -> anthropological-science-fiction (now 8). SFE says language is the central image: the alien code embodies the Whorfian idea that language shapes perception, transforms its poet-linguist decoder, and renders invented societies through thought and speech patterns. Language, culture and observer assumptions define it more than the space-opera frame. One-pass official Hachette front.
- Commit b9cd013 pushed. Gate 131 nodes/391 works, refs consistent. An initial cleanup accidentally staged two pre-existing YAML deletions; caught from commit summary immediately, restored and force-with-lease amended before deployment. Progress next=310 processed=310 added=249. Neither leaf reached 10.

### 2026-09-16 11:53 CEST - intake 310-311
- 310 Baby Teeth skipped as non-speculative psychological thriller. Penguin describes a silent seven-year-old psychopath whose calculated attacks include tampering with medication and setting her mother on fire; nothing requires magic, supernatural agency or speculative science. Source https://www.penguin.com.au/books/baby-teeth-9780143788430.
- 311 Bag of Bones -> ghost-story (now 10). King's official synopsis gives Mike Noonan ghostly cries and psychic visitations at Sara Laughs; Hodder names sinister forces in the lakeside home. The communicative dead and buried-history haunting define it. One-pass official Simon & Schuster front.
- Commit e0996b8 pushed. Gate 131 nodes/392 works, refs consistent. Progress next=312 processed=312 added=250. Ghost story reached 10; sourced proposal-only split drafted as Haunted places (6) and Companion dead (4), no restructuring.

### 2026-09-16 12:04 CEST - approved Alternate history restructure + held Ascent
- Executed the curator's approved structure: Alternate history is now an umbrella. Period alterations is an empty umbrella for forks within living memory of the depicted story. Its leaves are Alt Postwar (4), Alt Civil War (2), Alt Cold War (2), and Alt Present (1). Deep alterations (2) holds centuries-deep transformed world orders.
- Alt Postwar: Fatherland, The Man in the High Castle, The Yiddish Policemen's Union, and newly resolved held intake 303 Ascent. Alt Civil War: The Guns of the South, River of Teeth. Alt Cold War: Watchmen, Lady Astronaut. Alt Present: Peripheral. Deep alterations: The Alteration, The Years of Rice and Salt.
- 303 Ascent resolved from hold. SFE describes a Soviet Korean-War ace who becomes first human on the Moon; wartime fork, postwar space-race world. One-pass official S&S cover. Added count corrected +1 to 251; processed remains 312/next 312.
- Commit 927eda6 pushed. Gate 137 nodes/393 works, refs consistent. Existing work cards/images preserved; old #alternate-history remains the umbrella route.

### 2026-09-16 12:16 CEST - new-node portrait rule corrected + AH portrait batch
- the curator corrected the standing rule: every new subgenre gets its portrait immediately at creation. The supposed tally-to-50 batching rule is retired as erroneous. No A/B approval: generate subject + "beautiful digital artwork", choose and ship, 1024x1536; the curator vetoes after seeing it live.
- Generated and wired distinct 1024x1536 portraits for Period alterations, Alt Postwar, Alt Civil War, Alt Cold War, Alt Present, and Deep alterations. Files 145-150. Commit a526da2 pushed; gate 137 nodes/393 works, refs consistent.

### 2026-09-16 12:23 CEST - intake 312-313
- 312 The Baron in the Trees skipped as non-speculative literary/historical fable. SFE calls it one of Calvino's thematically linked fables; Penguin follows Cosimo's lifelong decision to remain in trees through the Enlightenment, Revolution and Napoleon, without magic or speculative science. Under the curator's actual-magic boundary it does not enter fantasy merely because its life premise is fabulist. Sources https://sf-encyclopedia.com/entry/calvino_italo and https://www.penguin.co.uk/books/437691/the-baron-in-the-trees-by-italo-calvino/9781784874223.
- 313 Barrayar deduped into the existing complete 16-book Vorkosigan Saga card in New space opera. SFE identifies it as the immediate sequel to Shards of Honor; Barrayar is already present with its individual cover. No site data change.
- Progress next=314 processed=314 added=251. Gate unchanged 137 nodes/393 works.

### 2026-09-16 12:54 CEST - intake 314-315
- 314 Beneath the Rising deduped into the existing complete three-book Beneath the Rising card in Ancient tormentors: Beneath the Rising, A Broken Darkness, The Void Ascendant. No data change.
- 315 Beowulf by Maria Dahvana Headley skipped as a new translation of the existing Old English epic, not a new fiction. Macmillan/MCD explicitly identify it as a radical feminist verse translation that recontextualizes the source; SFE catalogs Headley as translator. This intake tracks fictional works, not editions or translations of the same work. Sources https://us.macmillan.com/books/9780374110031/beowulfanewtranslation/ and https://sf-encyclopedia.com/entry/headley_maria_dahvana.
- Progress next=316 processed=316 added=251. Gate unchanged 137 nodes/393 works.

### 2026-09-16 12:57 CEST - approved New space opera split
- Executed the curator's split: New space opera is an umbrella with Political space opera (7) and Alien Delving (3). Political space opera holds Culture, Seven Devils, Teixcalaan, Hyperion Cantos, Imperial Radch, Sun Chronicles, Vorkosigan Saga; its test is the polity as primary field of action. Alien Delving holds White Space, Memory War, Planetfall; its test is humans entering alien wrecks/derelicts/artifacts/structures as story engine.
- Generated distinct 1024x1536 portraits at node creation, files 151-152. Existing cards/covers preserved; #new-space-opera remains umbrella route. Commit 4790d13 pushed; gate 139 nodes/393 works, refs consistent.

### 2026-09-16 13:25 CEST - intake 316-317
- 316 Beyond Black grounded as Ghost story but held because Ghost story is at the 10-card cap pending the curator's split ruling. SFE says Alison is a genuine medium communicating with genuine ghosts and experiencing a horrific afterlife; Harper/4th Estate says spirits infiltrate her body and home. This is an exact fit, but no unilateral 11th card. Sources https://sf-encyclopedia.com/entry/mantel_hilary and https://www.4thestate.co.uk/products/beyond-black-hilary-mantel-9780007157761/.
- 317 Billy Summers skipped as non-speculative crime thriller. King's and S&S's official synopses describe an Iraq-war sniper/contract killer taking one last job; no supernatural or speculative mechanism. Sources https://stephenking.com/works/novel/billy-summers.html and https://www.simonandschuster.com/books/Billy-Summers/Stephen-King/9781982173630.
- Progress next=318 processed=318 added=251. Gate unchanged 139 nodes/393 works. Beyond Black remains held for the Ghost story restructure.

### 2026-09-16 13:28 CEST - pure-branches structure rule reaffirmed
- the curator reaffirmed the Sep 12 rule: books live in leaf genres exclusively. Every non-leaf holds zero works. Any split must partition every work into leaves, with no genre-defining exceptions and no residual cards in the parent. Apply to all future split drafts, including Ghost story.
- Social dystopia split remains proposal-only and explicitly on hold pending the curator's treatment of A Time of Changes and The Lathe of Heaven. Do not execute.

### 2026-09-16 13:56 CEST - intake 318-319
- 318 Binti -> complete three-book Binti trilogy in first-contact-fiction (now 7): Binti, Binti: Home, Binti: The Night Masquerade. SFE/Macmillan follow a Himba student whose university journey is attacked by the Meduse; she survives and mediates a conflict rooted in the university's wrong against them. Transformative first communication drives the trilogy. One-pass official PRH omnibus front; individual editions remain missing for later cover audit.
- 319 Black Magic -> renaissance-fantasy (now 2). Penguin explicitly gives devil worship, black arts and hexing across historical European cities; actual magic operates in the documented historical world. References cluster around the sixteenth century, making Renaissance fantasy the closest current period leaf. One-pass official Penguin front.
- Commit f2fc5c1 pushed. Gate 139 nodes/395 works, refs consistent. Progress next=320 processed=320 added=253.

### 2026-09-16 14:21 CEST - the curator-approved Space dystopias leaf
- Owner approval source: phonemsg-01M2N2977DE8SCKM0H24JZCYHJ. Created Space dystopias as the 8th direct child of Spacefaring fiction. Definition: spacefaring human futures where the social order itself is the horror - closed, oppressive societies off Earth.
- Moved A Time of Changes from Social dystopia (Borthan colony world; Earth-only mismatch) and An Unkindness of Ghosts from Generation Starships (slavery regime is the story engine; generation ship is the container). Generation Starships now contains only Non-Stop. Social dystopia now has 9; no Earth-side split executed.
- Generated and self-selected a distinct 1024x1536 detailed colorful portrait at creation; wired as 153-space-dystopias.webp and archived to Drive. Commit c504379. Gate passed: 140 nodes / 395 works, refs consistent. Public HTML and portrait byte-identical; live Space dystopias route and both covers pixel-verified.
- Drive leaf 1Ad8S6Vh93ddGOxra5rNmKdx8uBEq3qkd; works 1IoSgXK6n8tGjc6fRjaI-VN2CREY-GLfF; portrait 17oR-e_-iGJw3uwyKkN3p7-LU6J7tOkPp. Both moved YAMLs updated in place.
- New standing rule: never create a new leaf directly under Spacefaring fiction without the curator's explicit approval first. the curator floated a future Classic space opera + New space opera umbrella only as a possible slot-saving idea; do not execute. Earth-side Social dystopia split remains uncleared.

### 2026-09-16 14:29 CEST - intake 320-321
- 320 Black Water Sister -> modern-goth (now 4). PRH calls it Malaysian-set contemporary fantasy: a reluctant medium is possessed and coerced by her grandmother's ghost into a world of gods, spirits, vengeance, gangsters and family secrets. Occult intrusion into contemporary family/social life makes Modern Goth the closest existing leaf. SFE catalogs it and notes the misleadingly broad silkpunk label rather than using that as a genre. One-pass OL 11062263, vivid illustrated lantern portrait, flat English front. YAML 1qmy4UkTxrZbBkUp9h0UWk5UGjssLaVc9.
- 321 Black Wings Beating -> complete three-book Skybound Saga card in heroic-fantasy (now 9): Black Wings Beating, Red Skies Falling, Gold Wings Rising. SFE identifies YA fantasy about an embattled nation seeking fabled ghost birds; Macmillan follows falconer twins whose gifts, dangerous Ghost Eagle quest, bonds and choices determine Uztar's war. Individual heroic ordeals/actions in an invented world are the engine. One-pass OL 10174307/10114009/11015198; rejected Red Skies Falling's disc-bearing audiobook image, so that book tile remains blank and status partial. YAML 11NrETtfqoXSZnrcXHw4MUIQgZ3CC4vEA.
- Commit d806d85 deployed. Gate 140 nodes/397 works, refs consistent; public HTML byte-identical. Both fiction pages fresh-session pixel-verified; Black Water Sister cover and Skybound covers 1/3 render, expected middle tile blank. Progress next=322 processed=322 added=255. Heroic fantasy is at 9, not split threshold.

### 2026-09-16 14:54 CEST - Psi powers rename + approved Social dystopia split
- Owner approval source: phonemsg-01M2N431GVP5YY7A7FAYA2C3XY. Renamed Mentalism fiction (`telepathy-fiction`) to Psi powers (`psi-powers`) and retained 33-telepathy-fiction.webp. Broadened definition to the full SFE Psi Powers umbrella: telepathy, precognition, telekinesis, effective dreaming and other psi powers shaping society/story. Existing four stayed; The Lathe of Heaven moved in from Social dystopia via effective dreams. Psi powers now 5.
- Executed ruled pure-branch split. Social dystopian future now holds zero works and has three leaves: Crowded Dystopias 3 (Stand on Zanzibar, 334, The Space Merchants); Childless Dystopias 3 (The Children of Men, The Handmaid's Tale, Atomized); Cli-fi dystopia 2 (The Windup Girl, American War).
- Generated/self-selected distinct subject-matched detailed colorful portraits at creation, 1024x1536 assets 154-156. Commit 4f52df1. Gate passed at 143 nodes / 397 works, refs consistent. Public HTML and all three portraits byte-identical; fresh cache-busted Psi powers and all three dystopia leaf pages pixel-verified.
- Drive: mentalism-fiction folder renamed psi-powers in place (1k7XL_urF3MafY9yM3B0AgJDIQk1Oyn9A), portrait retained. Crowded folder 17dZPOrTMtLmeD3XQSN35ShhrlWVGA8ti / portrait 1GHX1nsjzl1LhXK24l_3xwQ_WtFsxQXul. Childless folder 1ULZEhTy1Yuo7jrJwtGSl2QZcTQEffn02 / portrait 1mQF4KoqlV6yqbYIafvyJECsQp2Ln2GMY. Cli-fi folder 168kE9QSzkPG-inPX6Y_QslFVY5-tz7pR / portrait 1DKgyNnqS02RDB59QKNHU2U5FqxpXut-p. Existing YAMLs moved/updated in place where available.
- Logged only, do not execute: the curator suspects psi-power books have been squeezed elsewhere; possible future audit if commissioned.

### 2026-09-16 14:59 CEST - intake 322-323
- 322 Blackfish City -> cli-fi-dystopia (now 3). SFE sets it in a floating Arctic city surrounded by free water after Climate Change and calls its refuge dystopian; Hachette begins after the climate wars, with corruption, wealth inequality and unrest in the mechanically precarious city. Climate consequence creates and destabilizes the social order, making Cli-fi dystopia the engine-level fit. One-pass OL 8595548, clean neon orca/city English front. YAML 1e7iuc2Ykd-MFldEaCK_fPzx2mMjK-CDN.
- 323 Blackout/All Clear deduped into the existing four-book Oxford Time Travel card in time-machines. SFE explicitly treats Blackout and All Clear as one consecutive story and PRH places them in the Oxford institutional Time Gates sequence; both titles were already represented. One-pass biggest-series cover audit replaced/filled Doomsday Book, Blackout and All Clear with OL 369478/6584391/6626048; rejected To Say Nothing of the Dog's non-English result, leaving that tile blank. Existing YAML converted from standalone Doomsday Book to the complete Oxford card and moved/renamed in place on Drive: 1ULNC-dYP-X9uDtpkb8NuBXRjmYhyqN9j.
- Commit da75261 deployed. Gate 143 nodes/398 works, refs consistent; public HTML byte-identical. Blackfish City and four-book Oxford pages pixel-verified; three Oxford covers render, expected Dog tile blank. Progress next=324 processed=324 added=256. No leaf reached 10.

### 2026-09-16 15:29 CEST - Earthbound Military SF renamed Future War
- Owner approval: phonemsg-01M2N6CSB5CAFH6BTFF2GJV9P1 (`Ok, Future War it is`). Stable leaf renamed from Earthbound Military SF / `earthbound-military-sf` to Future War / `future-war`, same position under Future of Earth fiction. Definition widened/gated: war transformed by technology and fought on Earth; near-future and modern entries allowed, with Earthbound conflict core. Sole work Rogue Sequence remains. Existing 123-earthbound-military-sf.webp portrait retained.
- Commit 4cb3cb3. Gate 143 nodes / 398 works, refs consistent. Public HTML byte-identical; live Future War page and retained portrait/Rogue Sequence card pixel-verified.
- Drive folder renamed in place to future-war: 10COJmLN0aYmewrxXO1ptUW50qUKqyV6b. Rogue Sequence YAML updated in place: 1JSYCxQR1I8vtDQ1fuw6wPA1J3GCZ74VD.

### 2026-09-16 15:52 CEST - intake 324-325
- 324 Blanca & Roja -> fairy-tale-revision (now 6). McLemore's official synopsis calls it a retelling/reformation of Snow-White and Rose-Red, Wild Swans and Swan Lake: two sisters resist an inherited spell that turns one into a swan. Deliberately changed tale roles/outcomes match Fairy Tale Revision. One-pass OL 10118728, illustrated English floral/swan front. YAML 1cq0vfLHTYF6Y5J3PKin1eLSR5nPTtA-k.
- 325 Blindness -> pandemic (now 4). SFE identifies an inexplicable epidemic of white blindness striking nearly everyone, scaling as Disaster and collapsing the social contract; the Saramago Foundation says it could be yesterday, today or tomorrow. The spreading epidemic and civilization-in-progress collapse fit Modern day > Apocalyptic > Pandemic. One-pass OL 115428, stark typographic English front. YAML 1lALpUexTQN-kUIsQdT_kDBJe_2SFjppy.
- Commit ebe5f12 deployed. Gate 143 nodes/400 works, refs consistent; public HTML byte-identical. Both detail pages fresh-loaded/pixel-verified. Progress next=326 processed=326 added=258. No leaf reached 10.

### 2026-09-16 16:56 CEST - intake 326-327 Drive-staged; site publication blocked
- Recovered live STATE, full 989-entry candidate list and progress from Drive after workspace reset. Progress began exactly next=326 processed=326 added=258.
- 326 Bluecrowne -> gaslight-fantasy (would become 6 when published). Kate Milford's official synopsis sets smugglers, magic and pyrotechnics in the magical Greenglass House world; her own introduction fixes the action in 1810 during the Napoleonic wars, and Kirkus identifies a time-traveling kidnapper. Actual magic/time travel inside an early-19th-century historical frame make Gaslight fantasy closest. One-pass illustrated Clarion/Jaime Zollars English front selected; rejected the Open Library result because it was the Recorded Books audio package rather than a flat print front. YAML 1zm8fCEgwFEPt2NSg3_FqD4gDg2onS4p4.
- 327 Bold as Love -> complete five-book Bold as Love card in future-history-of-earth (would become 4 when published): Bold as Love, Castles Made of Sand, Midnight Lamp, Band of Gypsys, Rainbow Bridge. SFE identifies the sequence as near-future SF/fantasy melding into an asserted SF base; Hachette follows UK dissolution, environmental collapse, changing regimes and the rock-star triumvirate across the sequence. Its linked Earthbound social future makes Future history of Earth closest. One-pass official Hachette/Gollancz fronts for all five books. YAML 1hCMh6raSGWFTpQB32hnYdQ_PDh5X9Fbh.
- Drive YAMLs complete under the existing leaf works folders. No Ghost files moved. Site/index mutation, gate, commit, Pages byte check and deployed pixel QA are deferred because the only authorized publication routes are exhausted and main remains ebe5f12. Progress next=328 processed=328 added=260. Neither target leaf reaches 10.

### 2026-09-16 17:23 CEST - intake 328-329 Drive-staged; site publication blocked
- 328 Bone Silence -> complete three-book Revenger card in classic-space-opera (would become 8 when published): Revenger, Shadow Captain, Bone Silence. SFE calls the retro Solar System archipelago a deliberate homage to pre-twenty-first-century Space Opera and makes its lack of computers/networks/automation central; Orbit identifies Bone Silence as the piratical trilogy finale across thousands of worlds. One-pass official Orbit/Hachette coordinated English fronts, complete status. YAML 1_qF0BkHrlyZn8QoR4-iI7kwwYZyWqQtS.
- 329 Brain Wave -> hard-conceptual-sf (would become 3 when published). SFE calls it mature Hard SF and defines the premise: Earth exits a galactic forcefield that inhibited electromagnetic/electrochemical neural processes, increasing intelligence worldwide. Open Road follows the premise through humans, animals and social institutions. The rigorous model and worked implications make Hard Conceptual SF closest. One-pass four-cover review selected Open Road's blue neural-city/red branching-light English front, 7.5. YAML 1Hz8qMLH-hRFDddmJ6hsRqRJnsfmeBSlI.
- Drive YAMLs complete under the existing leaf works folders. No Ghost files moved. Site/index mutation, gate, commit, Pages byte check and deployed pixel QA remain deferred because publication is blocked. Progress next=330 processed=330 added=262. Neither target leaf reaches 10.

### 2026-09-16 18:02 CEST - GitHub auth restored; Ghost and intake 326-329 published
- GitHub CLI device authorization completed as GuSoder; HTTPS Git auth verified. Ghost split commit fe141ad pushed and Pages run 35118743554 succeeded. Gate 145 nodes/400 works/refs consistent; public HTML and portraits 157-158 byte-identical. Fresh Haunted House and Lessons beyond the grave pixels inspected and saved.
- Ghost Drive split completed: Haunted House folder 1AVuEo5LA8aDfW9ZihAxIBxD7jfTD7ODt / portrait 1TjALU7Gym7WFJNwHfI39GCP74juyLoVq; Lessons folder 1me-EwloO6lvKFQdlelamVmtzzzPw1WHu / portrait 1Tg7xk5lfJ0ywtOUfdo8p28ESZoDZjaYv. Nine existing YAMLs moved and canonical_genre updated; A Christmas Carol had no Drive YAML, so none invented. Beyond Black remains held.
- Drive-staged intake 326-329 published in follow-up commit 3b1abea: Bluecrowne, complete Bold as Love, complete Revenger, Brain Wave. Gate 145 nodes/404 works/refs consistent. Pages run 35119110323 succeeded and public HTML is byte-identical. All four deep links fresh-loaded and pixels inspected; all covers/grids render as expected.
- Progress remains next=330 processed=330 added=262; intake 330-331 research began but no classification/YAML/progress mutation completed yet.

### 2026-09-16 18:06 CEST - intake 330-331 deployed
- 330 Breakfast of Champions -> books-in-books (now 8). PRH says Dwayne Hoover takes Kilgore Trout's fiction as literal truth, triggering the satirical crisis; SFE identifies Trout as the recurring in-world sf writer. A story artifact destabilizing lived reality exactly fits Books in Books. One-pass three-cover review selected the official Dial/PRH orange T-shirt English front, 7.0. YAML 1fYrKFUvN-02PTE6KTCZpzSjOuv4OF2_l.
- 331 Bridge 108 -> cli-fi-dystopia (now 4). Anne Charnock's official reveal sets it in late-21st-century climate-ravaged Europe where drought and wildfire drive migration and the boy is trafficked into slavery in locked-down England; SFE places it in dystopian near-future Britain. Climate displacement creates the coercive order. One-pass two-cover review selected the official David Drummond blue bridge-route English front, 7.0. YAML 1VnxMbdunQ8IPf2TchFRAbcTEdLg_5TH2.
- Commit 2e3511b deployed. Gate 145 nodes/406 works/refs consistent; Pages run 35119556246 succeeded; public HTML byte-identical. Both deep links and covers pixel-verified. Progress next=332 processed=332 added=264. No leaf reached 10.

### 2026-09-16 18:49 CEST - intake 332-333 deployed
- 332 Bridge of Birds -> complete three-book Chronicles of Master Li and Number Ten Ox card in fantasy-mystery (now 4): Bridge of Birds, The Story of the Stone, Eight Skilled Gentlemen. PRH identifies the trilogy and makes investigation central: an ancient crime, murder of a mandarin and a Sherlockian chase through magical Ancient China. One-pass official Del Rey/PRH coordinated illustrated English fronts, complete status. YAML 1g5asF9MxUcfRp4js6X159ALPylVyDHJP.
- 333 Briefing for a Descent Into Hell -> science-fantasy (now 8). SFE calls it equipoisal with SF/fantasy, with the protagonist's mythic journey perceived as Venusian consciousness projected from a flying saucer; PRH follows the inner-space voyage through ruined city, mythic island and singing planets while medical reality remains in tension. One-pass two-cover review selected OL 11406742, stark red/green typography on black, 6.5. YAML 1zVYJf21gQeqIRuuzsmpaHsEvEIJ1VLZr.
- Commit 8073c65 deployed. Gate 145 nodes/408 works/refs consistent; Pages run 35124115569 succeeded; public HTML byte-identical. Both deep links, full Master Li three-cover grid and Lessing cover pixel-verified. Progress next=334 processed=334 added=266. No leaf reached 10.

### 2026-09-16 19:18 CEST - intake 334-335 staged for deployment
- 334 Bring the Jubilee -> alt-civil-war (now 3). SFE calls it the first significant alternate history where the South wins the Civil War, then makes Gettysburg the Jonbar Point altered by time travel. One-pass selected Open Road's Confederate/US flag and smoky battlefield English front. YAML 1glCk1_zTOioy51ZwHhOvVfpnmV1-iqbX.
- 335 Bug Jack Barron -> social-dystopia-modern (now 6). SFE describes a near-future, politically corrupt media spectacle centered on Barron's on-air challenge to industrial and political power, and compares it to Fabulation. Its engine is a recognizable society sickened by media/power rather than a distinct future regime, matching Social dystopia's present-facing test. One-pass selected Panther illustrated broadcast-wave English front via OL 13852618. YAML 1zmW9FYTUm3RdWe4mErRgEFs9y3dq-HNw.
- Gate 145 nodes/410 works, refs consistent. Progress next=336 processed=336 added=268. Deployment/pixel QA pending.
- Deployed commit ed4bb78; Pages run 35127329672 succeeded; public HTML byte-identical. Both hash deep links and their cover pixels were inspected and correct. Alt Civil War Drive leaf scaffold created under the canonical alternate-history tree: folder 1ZzaWHbdMcRyAP1Ig-N_8oywVTw4Q1Psl, works 1Xjo-_yi6D30G4h7NuvvkGQDaY4Ga2sx-.

### 2026-09-16 19:49 CEST - intake 336-337 staged for deployment
- 336 Build Your House Around My Body -> modern-goth (now 5). PRH calls it part ghost story and follows women bound through generations by ghosts, ancestors, possessed bodies and possessed lands; Oneworld ties their revenge to Vietnam's colonial past. Those occult forces carry accumulated historical/familial darkness into modern Saigon, making Modern Goth closer than a haunting anchored to one house or a cross-death lesson. One-pass two-cover review selected Oneworld/OL 11556283, illustrated snakes, flowers and night foliage, English front. YAML 1hy0i2l8a36cjrpcptlBPklfAXFtCsJZw.
- 337 Burn -> alternate-history-fantasy (now 5). Ness's official synopsis sets it in 1957 with farm-working dragons, prophecy, a dragon cult, an assassin and FBI agents; actual magic openly transforms mid-century America, so magic is the history-rewriting engine. SFE catalogs it as a 2020 individual title without extended discussion. One-pass cover review selected Quill Tree/OL 10097446, black dragon through layered fire, English front. YAML 112WGMWIl8EqypRAvu-zqEBcHgWzmOcyv.
- Gate 145 nodes/412 works, refs consistent. Progress next=338 processed=338 added=270. Deployment/pixel QA pending.
- Deployed commit 2081c54; Pages run 35130514764 succeeded; public HTML byte-identical. Both hash deep links and cover pixels inspected and correct. STATE/progress mirrored to Drive. No leaf reached 10.

### 2026-09-16 20:19 CEST - intake 338-339 staged for deployment
- 338 By Force Alone -> mythic-retelling (now 9). SFE calls it a dark satire of Arthur and the Matter of Britain; Tidhar's official synopsis explicitly retells King Arthur's rise in post-Roman Britannia among eldritch beings. Named inherited Arthurian figures/narrative are the engine. One-pass selected Tor/OL 10282839, red hand gripping a sword against a red-black landscape, English front. YAML 1-HlJ2rP09fMp0ehKBPFrTRhWTS6wJ-Rf.
- 339 By the Pricking of Her Thumb -> complete two-book Alma sequence in cyberpunk (now 5): The Real-Town Murders and By the Pricking of Her Thumb. SFE defines the first as a near-future noir thriller in a world threatened with immersion into a VR maze by a sophisticated Internet, and identifies the second as its loose same-detective sequel; Hachette confirms it returns to that near future for another impossible murder. Networked VR, concentrated power and street-level investigation make Cyberpunk closest. One-pass series review selected coordinated Gollancz/Hachette English fronts, complete. YAML 19fuiVwCdiZsAcKHsb1-wZ8eq99nrx50u.
- Gate 145 nodes/414 works, refs consistent. Progress next=340 processed=340 added=272. Deployment/pixel QA pending.
- Deployed commit 5f1045e; Pages run 35133688660 succeeded; public HTML byte-identical. By Force Alone standalone and complete two-cover Alma grid fresh-loaded and pixel-inspected. STATE/progress mirrored to Drive. No leaf reached 10; Mythic retelling is at 9.

### 2026-09-16 20:49 CEST - intake 340-341 staged for deployment
- 340 Caravan for China skipped as non-speculative historical adventure. Kirkus describes Roman adventurers under Tiberius traveling to China, then Simon of Cyrene returning to witness Golgotha and carry the cross; the New Yorker's contemporary capsule likewise calls it a romantic adventure from Rome to Peiping in the time of Jesus. A Fantasy100 listing and Kirkus's tonal use of “spirit of fantasy” do not establish actual magic or speculative science. Sources https://www.kirkusreviews.com/book-reviews/a/frank-s-stuart/caravan-for-china/ and https://www.newyorker.com/magazine/1941/01/04/1941-01-04-054-tny-cards-000004687.
- 341 Carrie -> psi-powers (now 6). SFE describes King's first novel as focused on Psi Powers, notably Telekinesis; King's official synopsis centers Carrie discovering telekinetic powers and using them in the prom confrontation. One-pass 15-cover review selected OL 15228374, blood-red face on black with English title/author; non-English and back-cover scans rejected. YAML 1PCsH5xEYsXkacal6lFEB_bwhmJCmNZe3.
- Gate 145 nodes/415 works, refs consistent. Progress next=342 processed=342 added=273. Deployment/pixel QA pending.
- Deployed commit 00c27f7; Pages run 35136836316 succeeded; public HTML byte-identical. Carrie hash deep link and chosen cover fresh-loaded and pixel-inspected. STATE/progress mirrored to Drive. No leaf reached 10.

### 2026-09-16 21:07 CEST - approved Psi split staged
- Owner approval source phonemsg-01M2NSRN3KZ96AHA0RRJGNPPGB (`Ok, do the psi split`), following phonemsg-01M2NSKXWGXNA4BTKM2B40WWAF naming future Psionics and contemporary Psi Powers.
- Existing Futurist > Future of Earth fiction leaf renamed in place to Psionics, retaining 33-telepathy-fiction.webp and four future-set cards per the curator's ruling: The Demolished Man, Ubik, Slan/Slan Hunter, The Lathe of Heaven (set 2002). Definition now future-set SF shaped by psi powers.
- New Modern day > Psi powers leaf created for contemporary-set psi stories in the recognizable present: Dying Inside and Carrie. Generated/self-selected detailed colorful contemporary telekinesis portrait, exact 1024x1536, wired as 159-psi-powers.webp.
- Pure branches preserved. Gate 146 nodes/415 works, refs consistent. Drive: old leaf renamed psionics in place 1k7XL_urF3MafY9yM3B0AgJDIQk1Oyn9A, retained works 1l59N4lsiHPfDsv3FVXXFI0v7Ncv6X-D3 and portrait. New Psi powers folder 11NYS1F0Jn29CRCIVF_HxZ8ed0hJmTq3I, works 1BWfvKSOUCCT9YrS2MgqM1GWF2cIyjmdy, portrait 1WjSFoGeuSlikvY9kSZO1IE4a6ohOuJxe; both contemporary YAMLs moved and canonical_genre updated. Deployment/pixel QA pending.
- Deployed commit 02ea399; Pages run 35138687303 succeeded. Public HTML and new portrait are byte-identical. Fresh Psionics and Psi powers shelf loads pixel-inspected: retained Psionics portrait + 4 works, new contemporary portrait + 2 works render correctly.

### 2026-09-16 21:20 CEST - intake 342-343 staged for deployment
- 342 Cat's Cradle deduped: already represented in Chemical Catastrophe with OL 14572638. No change.
- 343 Catfishing on CatNet -> complete two-book CatNet card in technomorphosis (now 7): Catfishing on CatNet and Chaos on CatNet. SFE identifies the same benevolent emergent AI across both novels; Pan Macmillan centers a sentient AI administering an ordinary social network and the first novel's privacy/out-of-control-tech effects; Tor's sequel pits the community against an AI hacking networks to instigate real-world violence. Technology reorganizing friendship, mutual aid, privacy and everyday social life makes Technomorphosis closest. One-pass four-cover review selected coordinated Tor neon/glitch English fronts, complete. YAML 1v2SXBHPyol6ko_Yq6bJaEEFUKuGYkbTH.
- Gate 146 nodes/416 works, refs consistent. Progress next=344 processed=344 added=274. Deployment/pixel QA pending.
- Deployed commit 3362c4d; Pages run 35139965017 succeeded; public HTML byte-identical. Complete CatNet two-cover grid fresh-loaded and pixel-inspected. STATE/progress mirrored to Drive. No leaf reached 10.

### 2026-09-16 21:55 CEST - Psionics future-science portrait
- Owner request source phonemsg-01M2NWB3Y03CB7F08CR4ZHMZCD. Replaced the retained Psionics portrait with a self-selected 1024x1536 detailed colorful painting of an institutional future psi laboratory: trained espers in neural-interface stations, monitored by scientists and psychic-electronics systems. This is deliberately distinct from Modern day's at-home latent-power image.
- Archived generated source art beside the Drive node as `Psionics - future science portrait.png`: 1o8b0j9yaVG7djJp61YaNhCab1nGUsYaB.
- Commit d6d5f80; Pages run 35143360520 succeeded. Public HTML and portrait are byte-identical. Fresh browser pixel check was attempted but blocked by a connection-level timeout; no visual mismatch was observed because the page did not load.

### 2026-09-16 21:57 CEST - intake 344-345 staged for deployment
- 344 Catherine House -> gothic-science-fiction (now 6). HarperCollins places its mystery inside an isolated elite university with experimental curriculum and a shocking institutional secret; Publishers Weekly identifies plasm research, controversial experimentation and mass hypnosis. Secret science in a decaying coercive institution supplies the mystery and terror, closer than biology-specific Genetic Engineering. One-pass four-cover review selected Custom House/OL 9830444, magenta nerve/root tendrils on midnight blue, English front. YAML 1FeJx5FjVG_tmpxocqi3_a-G_f1ElYIJb.
- 345 Cemetery Boys -> complete two-book card in lessons-beyond-the-grave (now 5): Cemetery Boys and Cemetery Boys: Espíritu. Macmillan and Aiden Thomas center Yadriel summoning Julian's ghost, helping him finish his business, later spirit communication, vanished spirits and a returning demon. Companionship and mutual growth across death drive both books. One-pass four-cover series review selected coordinated illustrated English fronts, complete. YAML 1o7njYLjHPvpykKfN-b4oBHysdVVerof2.
- Gate 146 nodes/418 works, refs consistent. Progress next=346 processed=346 added=276. Deployment/pixel QA pending.

### 2026-09-16 22:02 CEST - Psionics portrait veto and replacement
- the curator vetoed the first future-lab portrait as “way too much” in phonemsg-01M2NWVS9CR0C2NDS7XE0XKJPZ and asked for the normal book-driven process based on the current shelf.
- Replaced it with a quieter full-scene painting synthesized from the shelf: a telepathic confrontation in a future office, with subtly unstable dreamlike city reality and traces of hidden evolved people, drawing on The Demolished Man, Ubik, The Lathe of Heaven and Slan without trying to literalize all four.
- Exact 1024x1536 generated source archived beside node: 1DjZiKtawERUezvKbV9xKfpm24lfgkxmf. Commit 52a0c9b; Pages run 35144044952 succeeded; public portrait byte-identical. Fresh Psionics load and four-card shelf pixel-inspected; screenshot cloud-browser-20260916-200249.png.
- Intake 344-345 deployment: commit 1b27e10; Pages run 35143626919 succeeded; public HTML byte-identical. Fresh Gothic science fiction and Lessons beyond the grave loads inspected; Catherine House cover loaded at native pixels and Cemetery Boys complete two-cover grid had already been visually inspected before publishing. Progress next=346 processed=346 added=276.

### 2026-09-16 22:22 CEST - intake 346-347 staged for deployment
- 346 Chaos on CatNet deduped: already represented as the second volume of the complete CatNet card in technomorphosis, with the official Macmillan cover.
- 347 Charlie and the Chocolate Factory -> complete two-book Charlie card in science-fantasy (now 9): Charlie and the Chocolate Factory and Charlie and the Great Glass Elevator. SFE treats Dahl's best-known juvenile fantasies as a coherent fantastical line and identifies Charlie as its most famous example, assembled with its sequel. Dahl's official synopsis gives the wondrous impossible factory; the sequel continues directly into a glass elevator launched into space. Technological apparatus and fairy-tale impossibility are inseparable, making Science fantasy the closest current leaf. One-pass eight-cover series review selected vintage Schindelman Factory and vivid Quentin Blake Elevator English fronts, complete. YAML 1jhL3PcsrtH722QzvAvEUcKAfKR-5pEZ5.
- Gate 146 nodes/419 works, refs consistent. Progress next=348 processed=348 added=277. Deployment/pixel QA pending. Science fantasy is at 9, below split trigger.
- Deployed initial intake commit c613df0, then corrected the factory cover after deployed QA exposed an Open Library ID that would not load; final cover uses the reliable Open Library ISBN endpoint for the clean English Quentin Blake front. Final cover commit a48f9c0; Pages run 35146560671 succeeded; public HTML byte-identical. Inner-panel scroll fresh-load verified the Charlie card and factory cover pixels at 180x277; source two-cover series sheet had already been visually reviewed. Final YAML 1slhCiZGo6G54nFoiaS724YuX0KPm_Ftt.

### 2026-09-16 22:40 CEST - approved Augmentor dream-lab Psionics portrait
- Owner approval source phonemsg-01M2NYZX3E5RXA5XPND1X61PEV (`Ok, something like that I guess`) followed the explicit proposal of the Augmentor lab from The Lathe of Heaven and the correction that canonical psi lab scenes are intimate: two people and a machine, small room with enormous implications.
- Replaced the prior Psionics portrait with a 1024x1536 intimate institutional scene: one sleeper wired to the Augmentor, one scientist at its compact monitoring console, and the rain-lit city outside subtly splitting into rewritten realities. No crowd, statues, cathedral scale or spectacle. Source art visually inspected before publication.
- Archived source beside the node: 1BvXqoCqmcvPGMvvK8ZD5JJCArUXV6YbX. Commit 33364bc; Pages run 35147873749 succeeded. Public portrait byte-identical; fresh Psionics load showed the new portrait and four-card shelf, visually inspected in cloud-browser-20260916-204056.png.

### 2026-09-16 22:52 CEST - intake 348-349 staged for deployment
- 348 Chercher La Femme -> far-future-first-contact (now 8). Aqueduct's official synopsis sends Julia 9561 to a distant planet to retrieve a failed first-contact crew and establish meaningful contact with humanoid inhabitants whose sex, desirability and motives are unresolved; Publishers Weekly confirms the far-future diplomatic mission. Encounter with the unknown intelligent species is the engine. One-pass selected the sole official Aqueduct English front, pink-violet planetary light over deep blue with an iridescent alien form. YAML 1-wUtQeBme1ua4zM-sZU94yocX1CJju16.
- 349 Children of Blood and Bone -> complete three-book Legacy of Orïsha card in political-fantasy (now 9): Children of Blood and Bone, Children of Virtue and Vengeance, Children of Anguish and Anarchy. Macmillan describes a complete West African-inspired magical trilogy beginning with a monarchy that exterminated the maji, then restoration of magic, civil war, competing factions and the monarchy's fall. Magic is explicit while revolution and rulership drive the sequence. One-pass complete series review selected coordinated Henry Holt/Macmillan English portrait fronts. YAML 1bXTRijgKOQhadVdhWTrUCfFBzVriUsB7.
- Gate 146 nodes/421 works, refs consistent. Progress next=350 processed=350 added=279. Deployment/pixel QA pending. Political fantasy is at 9, below split trigger.
- Deployed commit 3fd5b4c; Pages run 35149171121 succeeded; public HTML byte-identical. Chercher La Femme official cover and Legacy of Orïsha lead cover fresh-loaded at native pixels; both target shelves showed correct 8/9 counts. Source complete three-cover Legacy sheet was visually inspected. No leaf reached 10.

### 2026-09-16 23:23 CEST - intake 350-351 staged for deployment
- 350 Children of Time -> current four-book Children of Time sequence in alien-cosmic-history (now 2): Children of Time, Children of Ruin, Children of Memory, Children of Strife. SFE traces the sequence from uplifted spiders through encounters among successor species after Earth's collapse; Pan Macmillan lists four published volumes through the March 2026 UK publication of Children of Strife. The emergence and interrelation of radically nonhuman civilizations across deep time match Alien cosmic history. One-pass selected four coordinated Tor/Pan Macmillan cosmic English fronts. YAML 1Xp41ALNT4v0Ta5ygi8Amh8FItBQ-p6Ci.
- 351 China Mountain Zhang -> totalitarian-dystopia (now 9). SFE describes a China-dominated twenty-second century where homosexuality is a capital offence; Tor sets Zhang inside a regimented China-led world order after the American Liberation War. Its intimate mosaic of ordinary life under political and social coercion fits Totalitarian dystopia, even though the regime is lived rather than overthrown. One-pass selected SF Masterworks/OL 8779578, a dense neon future street with clean English title. YAML 1QxV_JoLxFIo8DmA434dT9mOsa4PxBKFl.
- Gate 146 nodes/423 works, refs consistent. Progress next=352 processed=352 added=281. Deployment/pixel QA pending. Totalitarian dystopia is at 9, below split trigger.
- Deployed commit f5cfddd; Pages run 35152098732 succeeded; public HTML byte-identical. Children of Time lead cover and China Mountain Zhang cover fresh-loaded at native pixels; target shelves showed correct 2/9 counts. Complete four-cover Children of Time source sheet visually inspected. No leaf reached 10.

### 2026-09-16 23:53 CEST - intake 352-353 staged for deployment
- 352 Chocky -> first-contact-fiction (now 8). Penguin explicitly calls it alien contact: an unseen presence communicates through Matthew, asks alien questions, teaches mathematics and anti-gravity ideas and experiments from afar. The consequential first communication with an extraterrestrial intelligence through a child's mind is the engine. One-pass four-cover review selected NYRB/OL 12215385, interlocking black-grey-red signal curves on a clean English front. YAML 1aDLDPDFPxcgoMftGzpXZRjE1FFEWDM9_.
- 353 Chosen Spirits -> cyberpunk (now 6). SFE calls it an angry near-future India novel rife with surveillance; Simon & Schuster centers a Reality Controller managing celebrity livestreams amid corporate power, elite control, smog and revolution in 2020s Delhi. Networked media, pervasive surveillance and precarious street-level lives make Cyberpunk closest. One-pass selected the sole official S&S India English front, teal circuit-board streets and devices under a distressed red title. YAML 1ieZwLzGlSv7FumVdY6Q6uoJPxws22T3F.
- Gate 146 nodes/425 works, refs consistent. Progress next=354 processed=354 added=283. Deployment/pixel QA pending. No leaf reached 10.
- Deployed commit 79f7959; Pages run 35154830081 succeeded; public HTML byte-identical. Chocky and Chosen Spirits covers fresh-loaded at native pixels; target shelves showed correct 8/6 counts. No leaf reached 10.

### 2026-09-17 00:28 CEST - intake 354-355 deployed
- 354 Cities in Flight -> complete four-book Okie sequence in classic-space-opera (now 9): They Shall Have Stars, A Life for the Stars, Earthman, Come Home, The Triumph of Time. SFE identifies the four novels and their iconic antigravity cities roaming the Galaxy for work; Hachette calls the omnibus a galaxy-spanning future of giant city-spaceships and Galactic empire. Foundational pulp-scale interstellar adventure fits Classic space opera. One-pass complete series review selected four coordinated Arrow illustrated English fronts. YAML 1tOrv1lgRCHYreGuf0LA15v-uo_m3d2jM.
- 355 Cities of the Red Night -> complete three-book trilogy in worlds-in-flux (now 5): Cities of the Red Night, The Place of Dead Roads, The Western Lands. SFE calls Red Night a mixing and breeding of Western genres; Penguin follows its mutant empire, radioactive epidemic and pirate history through a surreal Old West toward Egyptian theology. Mutable genre, history and reality fit Worlds in flux. One-pass series review selected Penguin Modern Classics English fronts for the first two and an illustrated English Western Lands front. YAML 1vWF5ZL5JyG-GlX0k_1fJnIRo8s6JPjvP.
- Drive gap repaired: created missing worlds-in-flux leaf scaffold under fabulation with works folder, and moved its three existing on-site YAMLs plus the new Red Night YAML from the Fabulation works folder. Ada or Ardor's Drive location remains unexamined; not part of this intake.
- Commit 9d17c5a; Pages run 35157630965 succeeded; public HTML byte-identical. Both target shelves fresh-loaded and lead covers pixel-inspected at native pixels after scroll. Gate 146 nodes/427 works/refs consistent. Progress next=356 processed=356 added=285. No leaf reached 10; Classic space opera is at 9.

### 2026-09-17 00:59 CEST - intake 356-357 deployed
- 356 Citizen of the Galaxy -> anthropological-science-fiction (now 9). SFE singles out the Free Traders' exogamous kinship system and starship culture; the publisher edition follows Thorby from slavery through adoption into a merchant clan and across a Galactic culture's social strata. Family, trade, status, custom and belonging across societies make Anthropological SF closer than general space adventure. One-pass selected the Pocket Books green photographic English front via OL ISBN. Initial PRH-hosted URL failed only in the deployed card despite loading directly; corrected to the reliable OL ISBN endpoint. YAML 1IiAz7vC-pPV8F-iQ2q3fAqASQU6LNc62.
- 357 City of Stairs -> complete three-book Divine Cities trilogy in political-fantasy (now 10): City of Stairs, City of Blades, City of Miracles. SFE identifies a secondary-world fantasy whose gods have been killed; PRH traces conquest, colonial rule, diplomacy and espionage, sectarian revolt, assassination and secret war over surviving divine power. Empire and its aftermath shape the trilogy. One-pass official PRH series review selected the coordinated redesigned English fronts. YAML 1NMQoAgv3P0QtVbdXbcODAHZ8eU1nM0uZ.
- Final commit 4606674; Pages run 35160035705 succeeded; public HTML byte-identical. Both fresh shelf loads and lead pixels verified, including corrected Citizen endpoint and Divine Cities. Gate 146 nodes/429 works/refs consistent. Progress next=358 processed=358 added=287.
- Political fantasy reached 10. A sourced pure split proposal is now required before adding more; do not execute without the curator. Candidate axes need a full partition and shared-trait umbrellas rather than leftovers.

### 2026-09-17 01:28 CEST - intake 358-359 deployed
- Before intake, prepared and sent parent a pure 5/5 Political fantasy split proposal: Dynastic political fantasy vs Revolutionary political fantasy. The Age of Madness is the one explicit boundary question. YAML attached in parent report; awaiting the curator. No tree change made.
- 358 City Under the Stars -> science-fantasy (now 10). Open Road places it on far-future Earth in a post-utopian industrial hellhole beside a walled City of God; PW reveals absent alien rulers and ultra-advanced technology granting godlike powers. Sacred fantasy surface and technological explanation are inseparable. One-pass selected the sole Tor English front, dark blue walled city. YAML 1adsZ3qBDWzMwYAVVGAv5bY9KyDqyGlDp.
- 359 Cocaine Nights -> social-dystopia-modern (now 7). SFE places it in Ballard's contemporary-facing Mediterranean line: a spiritually frozen enclave becoming a Keep, with a detective uncovering crimes. Counterpoint describes crime deliberately animating an exclusive society of unlimited leisure. Recognizable present-day sick social order fits Social dystopia. One-pass selected Counterpoint's black vintage-nightlife English front. YAML 1iPc2KodK5tXFS7yWDLH8EhT4LvRVTtDc.
- Final commit f59fc59; Pages run 35162268299 succeeded; public HTML byte-identical. Both shelves and covers fresh-loaded at native pixels. Gate 146 nodes/431 works/refs consistent. Progress next=360 processed=360 added=289.
- Science fantasy reached 10. A sourced pure split proposal is now required, but do not stack a second owner boundary question while the Political fantasy split is awaiting the curator unless next intake needs this leaf.

### 2026-09-17 01:58 CEST - intake 360-361 deployed
- 360 Codex Alera -> complete six-book sequence in hard-magic (now 5): Furies of Calderon through First Lord's Fury. PRH defines Alera by bonds with elemental forces of earth, air, fire, water, wood and metal that produce specific capabilities used in war, protection and survival; Jim Butcher confirms the series is complete. Politics matter, but the explicit elemental system governs action. One-pass complete official Ace/PRH English series review. YAML 1_MgmvsHyPTEP8_OG1JlW8yWipamouH9y.
- 361 Cold Heaven -> ghost-story direct work (node now 1 direct plus its two child branches). SFE describes a dead husband haunting his widow and challenging her faith; PRH begins with his death and missing corpse and identifies supernatural mystery. The returned dead husband is central. One-pass selected Plume/PRH illustrated wake-on-water English front. YAML 16nHL-v_dJejdrmttRmAv-hcb0fS7JGoK.
- Commit b564c3a; Pages run 35164435120 succeeded; public HTML byte-identical. Hard magic card and Ghost story page/direct card fresh-loaded; both lead covers rendered at native pixels. Gate 146 nodes/433 works/refs consistent. Progress next=362 processed=362 added=291. No new leaf reached 10.
- Note: Ghost story is now a mixed branch with one direct work plus child branches, conflicting with the later pure-branch rule. Cold Heaven does not belong specifically in Haunted House or Lessons beyond the grave; this needs a future sourced restructuring decision rather than misclassification. Parent should surface only when not stacking another boundary question.

### 2026-09-17 02:47 CEST - intake 362-363 deployed
- 362 Comet Weather -> complete four-book Fallow Sisters sequence in contemporary-fantasy (now 7): Comet Weather, Blackthorn Winter, Embertide, Salt on the Midnight Fire. SFE identifies the sequence as fantasy; NewCon calls it a completed magical quartet about fey sisters straddling present-day London/rural Somerset and otherworldly past/alternative realms with star spirits and the dead. Open magic crossing ordinary current life fits Contemporary fantasy. One-pass complete official NewCon seasonal-tree English covers. YAML 1-diTw1ZUEQJhCJ7EGoUeiQZbgoKbN-O_.
- 363 Coming Up for Air skipped as non-speculative. Penguin and the Orwell Foundation describe a realistic 1939 insurance salesman's nostalgic return to his childhood town amid impending war, suburban development and social foreboding. Its predictions and thematic path toward Nineteen Eighty-Four are political observation, not magic, alternate history or speculative science. Sources https://www.penguin.co.uk/books/57306/coming-up-for-air-by-george-orwell-with-a-note-on-the-text-by-peter-davison/9780141185699 and https://www.orwellfoundation.com/the-orwell-foundation/orwell/books-by-orwell/coming-up-for-air/.
- Commit eda76ba; Pages run 35167780256 succeeded; public HTML byte-identical. Fallow Sisters lead cover fresh-loaded at native pixels; all four source covers inspected. Gate 146 nodes/434 works/refs consistent. Progress next=364 processed=364 added=292. No new leaf reached 10.

### 2026-09-17 03:15 CEST - intake 364-365 deduped
- 364 Conan the Barbarian / Mark Schultz deduped against the existing complete Conan card in sword-and-sorcery. The candidate refers to the Mark Schultz-illustrated collection of Robert E. Howard's Conan stories, not a new authored work: PRH credits Howard as author and Schultz as illustrator; the current Conan card already represents the sequence. SFE identifies Conan as Howard's founding Sword and Sorcery cycle. Sources https://www.penguinrandomhouse.com/books/83469/the-coming-of-conan-the-cimmerian-by-robert-e-howard/ and https://sf-encyclopedia.com/entry/howard_robert_e.
- 365 Conan the Conqueror / L. Sprague de Camp deduped: it is already the ninth volume inside the existing Conan card. SFE identifies it as Howard's only Conan novel, originally The Hour of the Dragon, later revised/edited by de Camp; de Camp is not the underlying author. Sources https://sf-encyclopedia.com/entry/howard_robert_e and http://www.howardworks.com/conantheconqueror.html.
- No site or Drive content change. Progress next=366 processed=366 added=292. Existing gate remains 146 nodes/434 works/refs consistent.

### 2026-09-17 03:47 CEST - intake 366-367 deployed
- 366 Condomnauts -> humorous-science-fiction (now 3). SFE identifies sex as the universal force organizing its galactic species; Restless calls it an uproarious space adventure and extended dirty joke about sexual diplomacy, first extragalactic contact, culture and alienness. Its comic-satirical mode governs the SF machinery. One-pass official Restless English front visually reviewed and selected. Drive YAML 1VGaWhe7teczbuXqlhMc5rPR6_B6Ra5-Y.
- 367 Confessions of the Fox -> books-in-books (now 9). Random House centers the long-lost Jack Sheppard/Edgeworth Bess manuscript, the scholar's footnotes, its disputed authenticity and the entanglement of manuscript and framing lives. One-pass official One World/Random House English front visually reviewed and selected. Created the missing Books in books Drive leaf scaffold: node 1netiloyadFDCU5CDuOYIRLqU4LEUFk6g / works 1cVVcor4BVYP7c2jLkmWdIJt_CwLvYA5_; YAML 1WyvOZG1t5ADsx7zoS5DTw6eANRoR_J4A.
- Commit 2ae8934; Pages run 35171799293 succeeded; public HTML byte-identical. Both exact detail routes and cover pixels fresh-loaded and visually inspected. Gate 146 nodes/436 works/refs consistent. Progress next=368 processed=368 added=294. No leaf reached 10.

### 2026-09-17 04:20 CEST - intake 368-369 deployed
- 368 Coraline -> whimsical-doors (now 5). Gaiman and HarperCollins center the bricked-up household door into the other home, the other parents and Coraline's return to ordinary life; SFE calls it YA horror. The enchanted threshold organizes the portal story, while horror governs its destination. One-pass selected the clean black HarperCollins English front via OL ISBN. YAML 1KPTm9zQO_UvqBWKa6TQlCCnU8eS2b8Md.
- 369 Cosmicomics -> worlds-in-flux (now 6). SFE describes Qfwfq's linked stories as fantasticated scientific postulates unpacked with absurdist cartoon clarity, fables about life, mathematics, evolution and reality versus appearance; Penguin follows mutable beings and worlds through galaxies, solidifying planets and species transitions. SFE names Calvino in Fabulation. One-pass selected the red-and-gold Penguin Classics English front. YAML 1ZsMT9B5dorwhkTXIMkOadJbrDSNHZuwr.
- Commit 3ec32fc; Pages run 35173902867 succeeded; public HTML byte-identical. Both exact detail routes and cover pixels fresh-loaded and visually inspected. Gate 146 nodes/438 works/refs consistent. Progress next=370 processed=370 added=296. No leaf reached 10.

### 2026-09-17 04:50 CEST - intake 370-371 deployed
- 370 Coyote Songs -> modern-goth (now 6). Hachette calls it a contemporary Southwest mosaic horror/crime novel where ghosts, old gods, a vengeful spirit and a hungry creature guide and haunt people caught in border violence. Occult darkness saturating recognizable modern social life makes Modern Goth closest. One-pass selected the original illustrated English Broken River front via OL 9192133. YAML 1zXkJz4YRVl42X5VY1DgSnDzHDTn4Wr5b.
- 371 Creatures of Charm and Hunger -> complete three-book Diabolist's Library card in secret-history (now 4): Creatures of Will and Temper, Creatures of Want and Ruin, Creatures of Charm and Hunger. John Joseph Adams identifies the connected sequence across Victorian London, Prohibition Long Island and WWII Britain; hidden diabolists, demons, occult institutions and Nazi magical warfare operate behind recorded history. One-pass complete three-cover review. Deployed QA caught a publisher placeholder at the first-book endpoint; corrected to the verified OL 14454987 illustrated front before closeout. YAML 1YYlpo4BOlqg5fsGJrvJcxRbgiotViI3l.
- Initial intake commit ea7221e; final cover commit b26f5b2; Pages run 35175831802 succeeded; public HTML byte-identical. Coyote Songs and corrected Diabolist lead/detail pixels fresh-loaded and visually inspected. Gate 146 nodes/440 works/refs consistent. Progress next=372 processed=372 added=298. No leaf reached 10.

### 2026-09-17 05:19 CEST - intake 372-373 deployed
- 372 Creatures of Want and Ruin deduped: already the second volume of the complete Diabolist's Library card added at intake 371, with its verified illustrated English cover.
- 373 Cross Fire -> complete two-book Exo sequence in anthropological-science-fiction (now 10): Exo and Cross Fire. SFE identifies Earth a century after alien conquest and the sequel's destabilization when the ruling species may withdraw; Lee and Scholastic center divided human loyalties, mixed alien-human social order, peace talks and cooperation among species. Colonial identity, allegiance and belonging make Anthropological SF closest. One-pass selected the complete official Fonda Lee/Scholastic orange-and-blue geometric English fronts. YAML 15MMKyUhY3ajhlKCvu0_j36P-iH_W2WzM.
- Commit 089aeca; Pages run 35177655779 succeeded; public HTML byte-identical. Complete two-cover grid and lead pixels fresh-loaded and visually inspected. Gate 146 nodes/441 works/refs consistent. Progress next=374 processed=374 added=299.
- Anthropological science fiction reached 10. A sourced pure split proposal is required, but do not stack another owner boundary question while the Political fantasy decision remains open unless intake needs this leaf.

### 2026-09-17 05:48 CEST - intake 374-375 skipped/deduped
- 374 Cross Her Heart skipped as non-speculative. HarperCollins and Publishers Weekly describe a realist psychological thriller: a mother living under an assumed identity after a childhood murder conviction is exposed and stalked through secrets, media attention and revenge. No magic, supernatural agency, speculative science or altered history appears. Sources https://harpercollins.co.in/product/cross-her-heart/ and https://www.publishersweekly.com/9780062856791.
- 375 Culture deduped: the existing political-space-opera Culture card already contains the complete ten-title sequence, Consider Phlebas through The Hydrogen Sonata, with per-book covers. SFE identifies Banks's Culture sequence; no site or Drive work change was needed.
- Progress next=376 processed=376 added=299. Existing gate remains 146 nodes/441 works/refs consistent.

### 2026-09-17 06:20 CEST - intake 376-377 deployed
- 376 Curious Toys skipped as non-speculative. SFE explicitly calls it nonfantastic; Hachette and Hand describe a 1915 Chicago historical crime thriller about a girl and Henry Darger hunting a human killer through Riverview amusement park. Sources https://sf-encyclopedia.com/entry/hand_elizabeth and https://www.hachettebookgroup.com/titles/elizabeth-hand/curious-toys/9780316485913/.
- 377 Cyber Mage -> new-weird (now 4). SFE calls it equipoisal, combining AIs and videogames with Hossain's fantastic material; Unnamed Press describes climate-apocalypse Dhaka sustained by biological nanotech, grotesquely altered people, djinn merged with humans, a dark-web AI, hackers and VR, explicitly calling it an SF/fantasy mashup. Science, magic, comedy and body transformation resist a single explanatory genre. One-pass selected the sole official Unnamed Press English front. YAML 1ByfZdY9514NF1BFZgwWsIRqxC8kT5emx.
- Initial site/progress commit e6e22c6; missing local YAML caught immediately and added in 456d7d7 before Drive/deployed closeout. Pages run 35181456962 succeeded; public HTML byte-identical. Cyber Mage exact detail route and cover pixels fresh-loaded and visually inspected. Gate 146 nodes/442 works/refs consistent. Progress next=378 processed=378 added=300. No leaf reached 10.

### 2026-09-17 06:50 CEST - intake 378-379 deployed
- 378 Damsel -> fairy-tale-revision (now 7). Arnold and Harper call it a dark, twisted fairy tale built from the prince-slays-dragon-and-rescues-damsel rite; Ama's recovered understanding overturns her assigned rescued-bride role and exposes the kingdom's legend. Rewriting the familiar plot and its gender values is the engine. One-pass selected the Balzer + Bray jeweled dark English front via OL 12850837. YAML 1e0N516MG9XSlYgtAbWS2r4B5jwDxrsuC.
- 379 Dandelion Wine -> complete three-book Green Town card in magic-realism (now 7): Dandelion Wine, Farewell Summer, Summer Morning, Summer Night. SFE identifies the associated sequence and calls its small-town summer vignettes Magic Realist in intensity; marvels arise inside ordinary 1928 Green Town through memory and wonder. One-pass complete three-cover review selected illustrated English fronts. YAML 1ea8sj4unWMAWW65apDISFvdCHRmpMMq0.
- Commit a37d4a4; Pages run 35183376147 succeeded; public HTML byte-identical. Damsel and complete Green Town grid/lead pixels fresh-loaded and visually inspected. Gate 146 nodes/444 works/refs consistent. Progress next=380 processed=380 added=302. No leaf reached 10.

### 2026-09-17 07:21 CEST - intake 380-381 deployed
- 380 Dark and Deepest Red -> fairy-tale-revision (now 8). McLemore explicitly pairs Strasbourg's 1518 dancing plague and present-day magical red shoes with the forbidding magic of a fairy tale; the inherited Red Shoes pattern is revised through Romani family history, blame and survival. One-pass selected the official Feiwel + Friends pink-purple silhouette English front. YAML 10my_Ykg6JuvqB0rfJDusLSEbHi7AOd4v.
- 381 Darkmans -> timeslips (now 5). SFE calls it a large ambitious Timeslip tale: fifteenth-century jester John Scoggins intrudes into and possesses people in present-day Ashford, producing untimely knowledge and destabilizing reality. Harper describes the past creeping into the modern present. One-pass selected Harper Perennial's vivid jester English front via OL 6945541. YAML 199Q4LCo0k12n_gcbWpv8sFGkXk1ItQHB.
- Commit c44c093; Pages run 35185318844 succeeded; public HTML byte-identical. Both exact detail routes and cover pixels fresh-loaded and visually inspected. Gate 146 nodes/446 works/refs consistent. Progress next=382 processed=382 added=304. No leaf reached 10.

### 2026-09-17 07:52 CEST - intake 382 deployed; 383 blocked
- 382 Darwin's Radio -> complete two-book Darwin sequence in technomorphosis (now 8): Darwin's Radio and Darwin's Children. SFE identifies endogenous retroviral evolution transforming humanity into a posthuman species; PRH follows the outbreak into an altered generation whose biology creates a quarantined social class. Undirected biological change remaking bodies, identity and society fits Technomorphosis over Genetic engineering. One-pass complete two-cover review selected illustrated English fronts. YAML 1PbPbin9Ht1-ENqEt4OeyhuZxC7td9PRJ.
- Commit a8c90d8; Pages run 35187370814 succeeded; public HTML byte-identical. Complete Darwin grid and lead pixels fresh-loaded and visually inspected. Gate 146 nodes/447 works/refs consistent. Progress next=383 processed=383 added=305.
- 383 Daughter of the Blood is researched as the entry to Anne Bishop's twelve-volume Black Jewels sequence. PRH describes magic, matriarchal rulership, prophecy and ruthless political struggle across invented realms. Political fantasy is its closest current leaf, but that leaf is already at 10 and awaiting the curator's split decision; intake pauses before adding it.

### 2026-09-17 08:04 CEST - approved Political fantasy split deployed
- Owner approval source phonemsg-01M2PZ9NNKZB03ERN2JQED95ZP (`Execute`), after final correction in phonemsg-01M2PZ7MHF7JMBRPDM92QH2MAN that The Age of Madness belongs with revolution because the Great Change is the trilogy's spine.
- Political fantasy became a pure umbrella with Court intrigue (4: A Song of Ice and Fire, Forgotten Beasts of Eld, Inheritance Trilogy, A Brightness Long Ago) and Revolutionary fantasy (6: Poppy War, Between Earth and Sky, Tigana, Age of Madness, Legacy of Orïsha, Divine Cities). Both names and partition match the curator's approved ruling.
- Generated and self-selected immediate 1024x1536 detailed colorful portraits for both new leaves; archived source PNGs on Drive. Court node 1-UOj0teJYu1a3_Di3KbiAscPaYgyqJjP / works 18UYDZnGVO8QtF7zsdZHDrSw8OjIY7m6a / source 1xLFSH9wkSi52VkyPrMbOIaleCeFKWHYM. Revolutionary node 1wOn7YtGOUPzWN0bEuZt163mja4wuBabe / works 1AMfeP8P2BjUj3bauJo5WLHpl7YXyoZFp / source 1kBJ83OUtdaGxjoZFH1XPLLRrzotGMrkl. Existing Drive YAMLs moved into their approved leaves.
- Commit bf3e4ef; Pages run 35188209536 succeeded; public HTML byte-identical. Both portraits and 4/6 shelf counts fresh-loaded and visually inspected. Gate 148 nodes/447 works/refs consistent. Intake 383 is unblocked and next.

### 2026-09-17 08:08 CEST - intake 383-384 staged for deployment
- 383 Daughter of the Blood -> complete twelve-book Black Jewels sequence in revolutionary-fantasy (now 7). Anne Bishop and PRH list twelve books through The Queen's Price; PRH frames the opening as a ruthless magical game of politics, intrigue and control of a prophesied Queen. The sequence's contest against coercive rulership and remaking of that order fits Revolutionary fantasy. One-pass complete twelve-cover review selected English illustrated Roc fronts followed by clean English Penguin portraits. YAML 1unxDtYtBgPQTvURPudD_Ih14KZ7HCHdz.
- 384 Day of the Minotaur -> complete three-book Minotaur Trilogy in mythic-retelling (now 10): Cry Silver Bells, The Forest of Forever, Day of the Minotaur. SFE places the sequence in Mycenaean Crete among legendary peoples confronting ascendant humanity; Day recasts the Minotaur as Eunostos, defender of the old mythic world. This matches the leaf's explicit mythic-age rule. One-pass series cover review found a usable English title/author front only for Day, selected via OL 10186823; first two remain without covers rather than hunting. YAML 1w7_uhDFKlZF438_30bdGSlrdIJQlmZGQ.
- Gate 148 nodes/449 works/refs consistent. Progress next=385 processed=385 added=307. Mythic retelling reached 10; next addition there requires a sourced split proposal, not unilateral restructuring.
- Pages run 35188506542 succeeded; public HTML byte-identical. Black Jewels complete twelve-cover grid and lead pixels fresh-loaded; Minotaur complete three-book grid and lead pixels fresh-loaded, including the two intentional missing-cover placeholders. Live visual QA passed.

### 2026-09-17 08:22 CEST - intake 385-386 staged for deployment
- 385 Dead Astronauts -> new-weird (now 5). SFE calls this loose Borne connection a surrealized SF Western and Time Opera through rule-bound worlds, with typographical games that enact bodily chaos and destroyed worlds; MCD adds time-slipping animals, biotech forms, a demon-haunted woman, rebels and multiple Earths. Its SF, fantasy, ecological horror and formal mutation resist one stable mode. One-pass selected OL 9243411, the vivid English FSG/MCD glitch-art front. YAML 1lAIaVfp8jCm-huHe0y6UAJwsyAT8BBT9.
- 386 Dealing in Dreams -> totalitarian-dystopia (now 10). Simon & Schuster explicitly calls it dystopian and centers a founder demanding violent loyalty before Nalah may enter the privileged Towers; PW details guardian gangs, subjugation of men, rigid binary identity and state-sponsored drug dependence. Institutional coercion shaping bodies, hierarchy and belief fits Totalitarian dystopia. One-pass official/library review selected the clean blue-and-yellow illustrated S&S English front. YAML 1HKJJvJp9LmshLW7splTMoFzlGS_ZWxHo.
- Gate 148 nodes/451 works/refs consistent. Progress next=387 processed=387 added=309. Totalitarian dystopia reached 10; next addition there requires a sourced split proposal, not unilateral restructuring.
- Initial deployed visual QA exposed that the OL Dead Astronauts cover endpoint painted blank; replaced it with MCD's exact official cover from the publisher page. Final cover commit 944da1c; Pages run 35189647365 succeeded; public HTML byte-identical. Both exact detail routes and final cover pixels fresh-loaded and visually inspected.

### 2026-09-17 08:56 CEST - intake 387-388 staged for deployment
- 387 Deathless Divide expanded to complete two-book Dread Nation card in alt-civil-war (now 4): Dread Nation and Deathless Divide. HarperCollins centers Confederate and Union dead rising on Civil War battlefields, derailing the war and creating a changed racialized 1880s society. The fork is the US Civil War itself. One-pass selected the coordinated Balzer + Bray English portrait fronts. Drive YAML pending.
- 388 Deep Roots expanded to complete two-book Innsmouth Legacy card in secret-history (now 5): Winter Tide and Deep Roots. SFE identifies the government's internment of Innsmouth's hidden People of the Water; Tor frames Aphra's recovery of that secretly persecuted community within 1940s America. Hidden historical people and their erasure/recovery fit Secret history. One-pass selected the coordinated Tor/Palencar English fronts. Drive YAML pending.
- Gate 148 nodes/453 works/refs consistent. Progress next=389 processed=389 added=311. Deployment/Drive/pixel QA pending. No leaf reached 10.
- Deployed 699f012 + portrait swap 2e146f1; public HTML byte-identical. Fresh Political fantasy and Court intrigue portraits visually verified: the curator's chosen loose-prompt parliament C is on the umbrella, prior umbrella court tableau is on Court intrigue. Dread Nation and Innsmouth Legacy complete two-cover grids and lead pixels visually verified. Drive YAMLs: Dread Nation 15kLIaQM63K4M5o7LIdBMHirYO6dyxceS; Innsmouth 1MIIfZ3RaVg6rL6Zf9cx7PLPAXy6hfGCU.

### 2026-09-17 09:26 CEST - intake 389-390 deployed
- 389 Destroy All Monsters -> worlds-in-flux (now 7). SFE describes Darkside as either a Parallel World or a trauma-born delusion; Harper presents two overlapping realities whose friends rescue each other through recovered memory. Its world remains psychologically and ontologically unstable rather than settling into a literal SF mechanism, making Worlds in flux closer than Parallel World fiction. One-pass selected the HarperTeen English camera/spiral front via Booksense. YAML 11Mo04XYxYN8vZKdJKISj0vpfZ2F0kCBx.
- 390 Devolution -> gothic-science-fiction (now 7). SFE and PRH frame a high-tech eco-community isolated by Mount Rainier's eruption and hunted by a savagely predatory Sasquatch species. The recovered-journal investigation treats Bigfoot as biological possibility, but siege terror and the monstrous outweigh cognition. One-pass selected the official Del Rey/PRH white-and-red footprint English front. YAML 1rWoTJ_HhhxpDf7tk2Se0JYUKDQn4_oNJ.
- Commit d94f01c; public HTML byte-identical. Both exact detail routes and cover pixels fresh-loaded and visually inspected. Gate 148 nodes/455 works/refs consistent. Progress next=391 processed=391 added=313. No leaf reached 10.

### 2026-09-17 09:52 CEST - Totalitarian dystopia split deployed
- Owner approval source phonemsg-01M2Q5DMP4TREDGETHS99ZFCAF (`Execute`), following the named Huxleyan-versus-Orwellian proposal.
- Totalitarian dystopia became a pure umbrella. Huxleyan dystopia has 4 cards: A Clockwork Orange, Brave New World, Camp Concentration, Dealing in Dreams. Orwellian dystopia has 6: Fahrenheit 451, Nineteen Eighty-Four, We, The Hunger Games, A Song for a New Day, China Mountain Zhang.
- Generated and self-selected immediate 1024x1536 detailed colourful portraits: seductive caste-conditioned pleasure state for Huxleyan; monumental surveillance police state for Orwellian. Source PNGs archived on Drive.
- Drive: Huxleyan folder 1M4Od5mZdJWXY2-nDQYHuHYizm_uQVbfn / works 1vz4ugRmruuroIxv8TMUL6KnbI9sDexXK / source 1hTiUHk-6mwoOdzE3_hQSDEhx11qsaQ0D. Orwellian folder 1gPDtuUyNIFPnX9BXCKy18P24L3uUfsZ2 / works 1bVVGT0VvuBYQ-OfU33RMaQEqCmtQgacQ / source 1DDZhysr0Sl10ugsb4G1QJH0UFMqOZSl0. Existing Drive YAMLs partitioned into the two child works folders.
- Commit 6ebd8d9; public HTML byte-identical. Both portraits and 4/6 shelf routes fresh-loaded and visually inspected. Gate 150 nodes/455 works/refs consistent.

### 2026-09-17 09:58 CEST - intake 391-392 deployed
- 391 Dirk Gently expanded to the two completed Dirk Gently novels in humorous-science-fiction (now 4): Dirk Gently's Holistic Detective Agency and The Long Dark Tea-Time of the Soul. SFE identifies the sequence's wide range of SF experiences; Simon & Schuster centers ghosts, time travel and comic detection. Humorous mode governs the genre collision. One-pass complete official S&S English covers. YAML 1H_4c4z-zE53XCegC7p3kduGrfFfy91EV.
- 392 Discworld -> new Comic fantasy leaf under Fantasy Realms (now 1), complete 41-novel card from The Colour of Magic through The Shepherd's Crown. SFE explicitly calls it the bestselling comic Fantasy series and the genre's finest set of pure comedies; official Terry Pratchett archive confirms all 41 novels. One-pass complete official archive cover review selected all 41 English Josh Kirby/Paul Kidby-era fronts. New 1024x1536 detailed colourful Comic fantasy portrait generated, self-selected, deployed and source archived. Drive node 1XzT-HS1tyF9gATrQHPXaLrk1j33gQFjP / works 1u6FNeS9ex6nOxhLI2IhY7FbgvGg7UQ1Y / portrait 1k2mHsBVqBbzrRRNSj_53af7NasaBf5dd / YAML 1wsrYwrGDVzUulmlw21IhWFQtZ-Xn4-LO.
- Commit da7dd58; public HTML byte-identical. Dirk's two-cover grid and Discworld's 41-cover grid/lead pixels fresh-loaded and visually inspected. Gate 151 nodes/457 works/refs consistent. Progress next=393 processed=393 added=315. No leaf reached 10.

### 2026-09-17 10:53 CEST - intake 393-394 deployed
- 393 Donovan's Brain expanded to complete three-book Patrick Cory card in gothic-science-fiction (now 8): Donovan's Brain, Hauser's Memory, Gabriel's Body. SFE identifies the trilogy's preserved brain, psi mind control and identity transfer and explicitly calls the core story more Gothic than scientific. One-pass complete three-cover review; deployed QA caught two unreliable initial endpoints, corrected to verified OL English fronts. Drive corrected YAML 1tTd6SQ-7AvjhVfeVlz-0Z91Pq6yfByz7.
- 394 Downward to the Earth -> reincarnation-fiction (now 3). SFE makes it a notable case of alien biology permitting reincarnation in an explicitly religious frame; Open Road centers Gundersen's journey to witness and undergo the nildoror's sacred rebirth. The rite is more specific than general anthropological SF. One-pass official Open Road English jungle front. YAML 1qrHIeZT0T2AjcpIQ_LZx2nACMseBC0ca.
- Commits 024744d, 43a1311, final cover f81ba36; public HTML byte-identical. Corrected Patrick Cory three-cover grid and Downward lead pixels fresh-loaded and visually inspected. Gate 151 nodes/459 works/refs consistent. Progress next=395 processed=395 added=317. No leaf reached 10.

### 2026-09-17 11:15 CEST - Mythic retelling split + Viking rename deployed
- Owner ruling source phonemsg-01M2QA5AE3W1FF6S9W665X9TSQ: Period fantasy's Norse fantasy renamed Viking fantasy because that leaf is about the Viking age; Norse fantasy belongs under Mythic retelling for Norse mythology. Parent supplied the final pure partition after the curator's no-dirty-branches correction.
- Viking fantasy retains 3 era-anchored cards: The Last Light of the Sun, The Weaver and the Witch Queen, The Broken Sword. Live-source recheck confirmed all three are Viking-era; no misfit found.
- Mythic retelling is now a pure umbrella: Arthurian fantasy (5: Avalon, The Once and Future King, Arthurian Saga, A Glastonbury Romance, By Force Alone); Greek myth fantasy (4: Circe, Phaedra, The Song of Achilles, The Minotaur Trilogy); Norse fantasy (1: Grendel).
- Generated and self-selected immediate 1024x1536 detailed colourful portraits for all three new leaves, deployed and archived full-size on Drive. Arthurian folder 1ZQ51_eaUMz3RVw9HgE9vvNdhVXtbHmJK / works 1DzOdm0hEi0NO0qlUeWTlS7Od82UK9NJF / portrait 1MFKoGAYtFWudMc88x1V3ywtYEvtCgVp7. Greek folder 1rKXbpp1LxyIrrV5r-uhATaHwwB3fjfQU / works 1irNACg6k8OOW3f9x-PFp2sitt3Gb54xO / portrait 1B3iyrBAwl7pW8vukk3RYqgzv---dVPS1. Norse folder 1SLA5cSq0_RcotCSiA1ve5CiGGSyXSjqX / works 1PlQ9eLbZN7RmMcYGE_85il8J6qT9nvOG / portrait 17DrAacBMq842TlvX_HlfoxH62XystWNd. Existing Drive YAMLs partitioned; old era folder renamed Viking fantasy.
- Commit 0951efc; public HTML byte-identical. All four live routes and portraits fresh-loaded and visually inspected. Gate 154 nodes/459 works/refs consistent.

### 2026-09-17 11:24 CEST - Arthurian portrait veto corrected
- Owner veto source phonemsg-01M2QAQGDT7BQXTQR68PR03GKW: Arthurian fantasy portrait needed actual Arthur, male king front and centre, rather than another woman-led myth portrait.
- Generated one dense colourful painted replacement with crowned King Arthur and Excalibur as unmistakable subject; shipped directly, no A/B. Updated deployed 164-arthurian-fantasy.webp and replaced the Drive source PNG in place (1MFKoGAYtFWudMc88x1V3ywtYEvtCgVp7).
- Commit d655028; deployed asset hash matches local. Fresh live route visual QA confirms Arthur is prominent and fully readable behind the title treatment.

### 2026-09-17 11:25 CEST - intake 395-396 deployed
- 395 Dr. Bloodmoney -> post-holocaust-survival (now 8). SFE explicitly calls it a Post-Holocaust USA; Hachette places the Point Reyes survivors seven years after the bombs with a functioning barter economy. Their adaptation and getting along in the lived aftermath make Post-Holocaust Survival closest. One-pass eight-cover review selected the detailed English SF Masterworks illustrated front, OL 8422913. YAML 1qeYh2DdoiMyMl22ejt26crgR0SYmqVnp.
- 396 Dragon Pearl expanded to the complete three-book Thousand Worlds trilogy in technofantasy (now 3): Dragon Pearl, Tiger Honor, Fox Snare. SFE calls it YA space opera increasingly patterned by Korean mythology; Disney describes literal fox magic, shape-shifting, ghosts and spaceships powered by technological and spiritual energy. the curator's actual-magic boundary therefore puts it on the Fantasy side, with Technofantasy closest. One-pass complete series review selected the three coordinated official Disney/Vivienne To English fronts. YAML 1CPWMvpUu2rd_wl4Z_mL-xjfn9vPZD8D8.
- Commit 72768ac; public HTML byte-identical. Both exact detail routes, Dr. Bloodmoney lead cover and the complete Thousand Worlds three-cover grid fresh-loaded and visually inspected. Gate 154 nodes/461 works/refs consistent. Progress next=397 processed=397 added=319. No leaf reached 10.

### 2026-09-17 11:30 CEST - sword-in-the-stone portrait selected live
- Owner selection source phonemsg-01M2QB6B832CSN1H2HX4KQSC3: switch the generated young-Arthur churchyard example onto the Arthurian fantasy site portrait.
- Replaced crowned Arthur with the sword-through-anvil-on-stone scene, showing young squire Arthur pulling it before astonished witnesses. Updated Drive source PNG in place (1MFKoGAYtFWudMc88x1V3ywtYEvtCgVp7).
- Commit c02c737; deployed asset hash matches local. Fresh live pixels visually verified: Arthur, sword, anvil and stone remain legible behind the title treatment.

### 2026-09-17 12:06 CEST - intake 397-398 deployed
- 397 Dread Nation deduped: existing alt-civil-war Dread Nation card already contains both Dread Nation and Deathless Divide with coordinated covers. No site or Drive mutation needed.
- 398 Dreadful Company expanded to complete three-book Dr. Greta Helsing card in paranormal-fantasy (now 5): Strange Practice, Dreadful Company, Grave Importance. Vivian Shaw and Hachette define a contemporary world adjacent to ours where monsters are real and Greta treats vampires, mummies, ghouls and other undead patients. The supernatural society and creature ensemble make Paranormal fantasy closest. One-pass complete series review selected the three coordinated official author-site English illustrated fronts. YAML 1FWVPAOXPIhHNdYm0KHWLaByQF4qgKclN.
- Commit e2d5a42; public HTML byte-identical after delayed Pages pickup. Complete Greta Helsing three-cover grid and lead pixels fresh-loaded and visually inspected. Gate 154 nodes/462 works/refs consistent. Progress next=399 processed=399 added=320. No leaf reached 10.

### 2026-09-17 12:24 CEST - intake 399-400 deployed; Classic space opera at split trigger
- 399 Driving the Deep expanded to complete four-book Finder Chronicles card in classic-space-opera (now 10): Finder, Driving the Deep, The Scavenger Door, Ghostdrift. SFE calls it lively, light-hearted Space Opera starring an interstellar repo man; PRH confirms four action-packed capers across deep-space colonies, AI ships, aliens and heists. Its episodic pulp-adventure shape fits Classic space opera over the political or alien-archaeology New space opera leaves. One-pass complete official PRH cover review selected four coordinated English DAW fronts. YAML 1xT_nVIhBymfkuXS_w9vMbicZ2YB-bmvw.
- 400 Eartheater -> magic-realism (now 8). SFE says its protagonist literally eats earth to gain knowledge of murdered women and explicitly applies Magic Realism on a non-metaphorical understanding. The marvelous power enters contemporary Argentine life as ordinary lived fact. One-pass selected the clean English HarperVia painted-flower front, OL 10405787. YAML 1DCYdKXbR61I0_0oXJEoNl0Lv_xlVRzIU.
- Commit daefc18; public HTML byte-identical. Finder's complete four-cover grid/lead and Eartheater lead pixels fresh-loaded and visually inspected. Gate 154 nodes/464 works/refs consistent. Progress next=401 processed=401 added=322.
- Classic space opera has reached 10. Do not add there again until the curator approves a sourced pure split. Initial source-grounded axis to develop: SFE distinguishes planetary romance's planet-bound landscapes from space opera's large-scale interplanetary action; however the current ten may partition more cleanly as roaming/caper space adventure versus polity/civilizational saga. Needs title-by-title grounding before proposing final names and partition.

### 2026-09-17 13:03 CEST - atemporal Science fantasy restructured
- Owner execution source phonemsg-01M2QGBYMXCKAD9A298D0J0NV8 (`Execute`), approving the plan summarized in phonemsg-01M2QGAKKDW55JB92864R2P172. Science fantasy remains under Atemporal, with the curator's "atemporal by construction" rationale: preserving known physics while producing a fantasy-reading world requires exile from our usable timeline into invented worlds or unplaceable futures.
- Science fantasy is now a pure umbrella: Hard science fantasy 3 (Lord of Light, Riverworld, City Under the Stars); Planetary romance 3 (Dragonriders of Pern, Majipoor, Aetherbound); Old Mars 1 (Barsoom). Hard SF fantasy requires fantasy surface / technological engine / known physics / no FTL or teleportation. Pern therefore belongs in Planetary romance. Old Mars is the specific pre-Mariner 4 romantic-Mars tradition.
- Modern-Earth exits: Charlie removed from Science fantasy because it already exists in Soft science fiction. Time Quintet moved to Timeslips: its sequence repeatedly crosses eras without a stable built machine, including Swiftly Tilting Planet's centuries, Many Waters' Noahic past and An Acceptable Time's temporal opening. Briefing for a Descent Into Hell moved to Worlds in flux under Fabulation: contemporary psychiatric reality and mythic-cosmic voyage never settle into one stable world-model.
- Generated and self-selected immediate detailed colourful portraits for all three new leaves. Drive child folders: Hard 1FODPm2tHnEcE-5XIZfcbEZMi4i4zYMr2 / works 1JV327s8ig8LUvHXH94e1B_PImLQrQFLC / portrait 1y-Gtsxs8ESh4gIb1QB3a9iILxZkdr8CY; Planetary 1msLuH288bUwfPCRe1krIY_UvEGMsm-Vu / works 1QNBWjyKt2-RANcOMLDj9prF1k0CGuAlm / portrait 1SjE21LmeFZOLdTYE-5cO2hu7pFUf-O1J; Old Mars 1TUY8IfbzQh1kJu4mrQ6Rp-gMMreS20le / works 1DqhczjjhQiAasPDsf0DbW7rQdYArk3-f / portrait 1tn8unQnU-tW1aTwBxfpaq91CuVUNscfJ. Existing canonical YAMLs moved to new leaves/exits; umbrella rationale YAML 1aDbyGLpnoymwjHacQnw4LpYlZ1xiNU4O.
- Commit f11aa67; public HTML byte-identical. Umbrella, all three new portraits/leaf counts, Time Quintet's Timeslips route and Briefing's Worlds in flux route fresh-loaded and visually inspected. Gate 157 nodes/463 works/refs consistent.

### 2026-09-17 13:21 CEST - intake 401-402 deployed
- 401 Elatsoe -> fantasy-mystery (now 5). Levine Querido centers a murder investigation whose essential evidence comes from the victim's ghost, with Ellie using her inherited ability to raise animal spirits. The mystery structure and fantastic evidence are more specific than its alternate-contemporary supernatural setting. SFE notes its fantasy/mythopoeic-SF equipoise and Lipan Apache grounding. One-pass official publisher cover review selected Levine Querido's clean English Rovina Cai paperback front. YAML 18vbknDJrCib_clQ1VDlA5E2LR8Du4IOD.
- 402 Elric deduped: existing sword-and-sorcery Elric of Melniboné card already contains six core saga volumes, Elric of Melniboné through Stormbringer, with five covers. Existing Drive YAML 1leFd5d8OGvqdoNpxsufNxvO4TW-AquqU. No site or Drive mutation needed.
- Commit b2c7ef7; public HTML byte-identical. Elatsoe detail route and cover pixels fresh-loaded and visually inspected. Gate 157 nodes/464 works/refs consistent. Progress next=403 processed=403 added=323. Classic space opera remains at 10 pending a sourced pure split proposal.

### Intake 403-404 (2026-09-17 13:52 CEST)
- Added complete Prefect Dreyfus Emergencies trilogy to Space Techno Fiction, grounded in SFE and Hachette: police procedural across Yellowstone's thousands of habitats, driven by neural implants and networked democracy.
- Added complete Embers of War trilogy to Alien Delving, grounded in SFE/Titan: alien artefacts, their planetary memorial works, and returning makers drive the sequence.
- One-pass English-front cover review completed; shipped three covers for each series.
- Gate: 157 nodes / 466 works, references consistent.
- Commit: bd0a48c. Progress: next 405, processed 405, added 325.
- Drive YAMLs: Prefect Dreyfus 16xUTaoXmcQk4sHZpSGSrKRy7Y_xJxOnA; Embers of War 1siaTMll5-_28qj3KDYhaVTdwKAQVcdCb.
- Deployment visually verified at exact leaf routes with both complete three-cover grids.

### Parked Star Wars ruling (the curator, 2026-09-17 13:57 CEST)
- No action now. When Star Wars novelizations or related works reach intake, place them on the SF side for findability, not under Technofantasy.
- Treat the Force through the Psi powers convention as SF pseudoscience.
- Proposed future home at that time: a new `Far Far Away` leaf under Otherworldly fiction under Futurist. Creation waits until intake reaches Star Wars and the curator approves the proposal then.

### 2026-09-17 14:23 CEST - intake 405 blocked; split proposal sent
- 405 Emergence dedupe passed and resolves to the complete 22-book Foreigner series. SFE centers its Planetary Romance/alien civilization and Emergence's human adviser to the atevi crown prince; PRH explicitly calls the series anthropological SF and centers diplomacy and sustained cross-cultural analysis. Best fit Anthropological science fiction, currently at 10, so no addition yet.
- Sent the curator a sourced pure split proposal: Human anthropology (Ammonite, Hainish, Citizen) and Alien anthropology (Fifth Head, Martian Chronicles, Stranger, Mirror, Under the Skin, Babel-17, Exo, plus Foreigner). Await decision; do not execute unilaterally.
- 406 Empire of Sand prep complete as the two-book Books of Ambha card (Empire of Sand, Realm of Ash), best fit Revolutionary fantasy. Hachette grounds resistance to an empire built on enslaved gods, then a crumbling empire whose salvation is questioned. One-pass official coordinated Orbit fronts selected. Hold mutation until 405 structure is resolved so progress remains coherent.
- Cover sheet: /downloads/intake-405-406-cover-sheet.jpg. Progress remains next=405, processed=405, added=325.

### 2026-09-17 14:34 CEST - Classic space opera split + intake 406 deployed
- Owner approval source phonemsg-01M2QNEECAZHNSC6T888H6Z8E3: keep Classic space opera as pure umbrella; split all ten into Pulp space opera (9, every prior work except Dune) and Evergreen space opera (Dune). Big Dumb Object carving remains a possible future split inside Pulp, not now.
- New definitions: Pulp = grand pulp tradition and direct heirs, era + mode. Evergreen = space opera that escaped its era and remains perpetually current. Both new leaves received self-selected generated 1024x1536 portraits, visually checked and deployed. Drive node folders: Pulp 1tODhieyupD_dQAzcCfkOhVnxt3pwetyJ; Evergreen 1eKzPaAfB97JKn6w5wncYFOVS7xkO_PoW. Existing ten YAMLs partitioned into their new works folders; portrait sources archived.
- 406 Empire of Sand expanded to two-book Books of Ambha card in Revolutionary fantasy: Empire of Sand and Realm of Ash. Official coordinated Orbit covers shipped. Drive YAML 1qmH7Nb5iOauQS5ati-J3BVS9PXgqZbct.
- Gate 159 nodes / 467 works / refs consistent. Commit 81d76b2; public HTML byte-identical. Classic umbrella, both new portrait leaves and complete Books of Ambha grid visually verified.
- 405 Emergence remains held pending the curator's Anthropological SF split ruling. Progress advances past completed/skipped cycle to next=407, processed=407, added=326; return to 405 immediately when the split decision arrives.

### 2026-09-17 14:48 CEST - Pulp space opera split deployed
- Owner approval source phonemsg-01M2QPDN4TBNNAJTRK2EP91CKV: `Ok, do Golden Age and Retro`.
- Pulp space opera is now a pure umbrella with Golden Age space opera (7: Double Star, Stars My Destination, Cities in Flight, Witches of Karres, Nova, Heechee Saga, Canopus in Argos) and Retro space opera (2: Revenger, Finder Chronicles).
- Golden Age definition names the original 1950s-1970s pulp wave and first maturity. Retro definition names 21st-century deliberate pulp throwbacks and explicitly distinguishes this from New space opera, the 1990s-2000s modernization movement.
- Both new leaves received self-selected generated 1024x1536 portraits, visually checked and deployed. Existing nine YAMLs partitioned into new works folders. Drive: Golden Age 1mosg8OvTIjhxlPfjMPNceUTXFeqCK0WN; Retro 1Copm4ujWU0DhID5CEUcrLCvKWGWm0XRt.
- Commit 50ee5b9; gate 161 nodes / 467 works / refs consistent; public HTML byte-identical. Pulp umbrella and both new leaf portraits/memberships pixel-verified.
- 405 Emergence and Anthropological SF split remain held.

### 2026-09-17 14:53 CEST - intake 407-408 closed
- 407 Empire of the Sun skipped as non-speculative. SFE says Ballard moved away from SF for this psychological war novel based on his childhood in Japanese-occupied Shanghai/Lunghua camp; Harper/4th Estate confirm the wartime survival and internment-camp story. Its hallucinatory style and relevance to Ballard's later SF imagery do not make its events speculative.
- 408 Empire of Wild -> modern-goth (now 7). SFE calls it a werewolf tale: a Métis man is transformed into a white Christian preacher and his wife must bring him back to the real world to save her people. Predatory religious/colonial occult power haunting contemporary social life makes Modern Gothic more specific than general Paranormal fantasy. One-pass cover review chose the detailed Harper English forest/wolf front, OL 10286612. YAML 10VDbo8-hzZxsjXJZFlOQOWLzYBnSpVVE.
- Gate 161 nodes / 468 works / refs consistent. Commit e0151a7; public HTML byte-identical and Empire of Wild detail route/cover pixels fresh-loaded and visually verified. Progress next=409, processed=409, added=327.
- 405 Emergence/Foreigner remains held pending the curator's Anthropological SF ruling.

### 2026-09-17 15:27 CEST - Anthropological SF split + intake 405 deployed
- Owner execution source phonemsg-01M2QRGMZ5KN3EDHAZCDW20W1H (`Execute`). Anthropological science fiction is now a pure umbrella with the curator's final leaf names.
- Earthborn (3): Ammonite, Hainish Cycle, Citizen of the Galaxy. Definition: society under the microscope is human/human-descended; alien element is cultural estrangement. Naming note records Earthborn as attested SF vocabulary; https://sfdictionary.com/view/1654/earthborn.
- Xenanthropology (8): Fifth Head of Cerberus, Martian Chronicles, Stranger in a Strange Land, Mirror for Observers, Under the Skin, Babel-17, Exo, plus newly added Foreigner. Definition: alien-ness is the point, either alien societies explored or alien eyes on us; term attested in SF criticism. Stranger follows the curator's alien-lens ruling.
- 405 Emergence expanded into complete 22-book Foreigner card, Foreigner through Defiance. SFE/PRH ground the series in human/atevi diplomacy and detailed alien-cultural contact; PRH official series page confirms 22-book order. One-pass complete-series cover retrieval used English OL fronts; full grid visually verified live. YAML 17w-R1tSaFIJ9VHi3joAsHj4REA_mNckh.
- New self-selected 1024x1536 portraits generated, visually checked, deployed and archived. Drive: Earthborn 1s7B69Mgg7u6mI7hw4AYUDfjOeYvgsv1K; Xenanthropology 1OE67X1RRmJq4Ge4EQQMeFBZKpepafr_c.
- Gate 163 nodes / 469 works / refs consistent. Commits 49b9069 and c3974f7; public HTML byte-identical. Umbrella, both leaves and Foreigner 22-cover detail route pixel-verified. Added count now 328; next remains 409.

### 2026-09-17 16:06 CEST - intake 409-410 deployed; Books in Books reaches 10
- 409 Empress of Forever -> political-space-opera (now 8). SFE calls it baroque Space Opera centered on conflict with a galaxy-ruling totalitarian empress; Macmillan makes rebellion against that ruler the rag-tag team's mission. Galactic power, rebellion and rule are the primary field. One-pass selected Tor's English Tommy Arnold front, OL 8598460. YAML 1fEeAwtVBiBFquRqeHiYp3got8TdVROc8.
- 410 Engine Summer -> books-in-books (now 10). SFE reveals Rush That Speaks and his narrated life as a memory embedded in a crystal device, replayed on command: the protagonist is the recorded story artifact. The nested narration/ontological reversal is more specific than the pastoral post-Holocaust setting. One-pass selected the clean English Gollancz SF front, OL 6744965. YAML 1Ur1QXDvbkavL0rwEtwt_kYUxHhOABG2t.
- Gate 163 nodes / 471 works / refs consistent. Commit 37ec2cb; public HTML byte-identical. Both exact detail routes and lead covers fresh-loaded and visually verified. Progress next=411 processed=411 added=330.
- Books in Books is now at 10: do not add another until the curator approves a sourced pure split proposal.

### 2026-09-17 16:50 CEST - intake 411-412 closed
- 411 Engine Summer deduped: it was added as intake 410 immediately before this cycle and already exists in Books in Books with Drive YAML and verified cover. No mutation.
- 412 Escaping Exodus expanded to the complete two-book sequence in generation-starships (now 2): Escaping Exodus and Escaping Exodus: Symbiosis. Harper describes a whole society living in and maintaining the belly of a spacefaring beast; the multigenerational enclosed society and survival of its mobile home make Generation starships closest, with a bioship as the biological variant. One-pass selected coordinated English Harper fronts. YAML 1oICYONAdS37Ay8JUD2u7r73VX_Rkqm1k.
- Gate 163 nodes / 472 works / refs consistent. Commit 1007b2b; public HTML byte-identical after delayed Pages pickup. Complete two-cover grid and lead pixels fresh-loaded and visually verified. Progress next=413 processed=413 added=331.
- Books in Books remains at 10, awaiting sourced pure split before another addition.

### 2026-09-17 17:22 CEST - intake 413-414 deployed
- 413 European Travel for the Monstrous Gentlewoman expanded to the complete three-book Extraordinary Adventures of the Athena Club card in fantasy-mystery (now 6): The Strange Case of the Alchemist's Daughter, European Travel for the Monstrous Gentlewoman, The Sinister Mystery of the Mesmerizing Girl. Simon & Schuster defines the trilogy around daughters of literary mad scientists solving murders, rescuing monstrous women and stopping conspiracies; the recurring investigations depend on fantastic identities and origins, making Fantasy mystery more specific than the Victorian scientific-romance furniture. One-pass selected the coordinated ornate English Saga fronts. YAML 1bepXxMQaGE1n1qBr3c2h1Xsd793WSizs.
- 414 Every Bone a Prayer -> worlds-in-flux (now 9). Blooms describes Misty's literal empathic speech with animals, buildings and land, alongside unexplained objects and transformations in an Appalachian holler. The author explicitly calls the work fabulism or slipstream rather than magical realism; the unstable exchange between trauma, landscape and impossible material change fits Worlds in flux. One-pass selected the clean English Sourcebooks yellow/orange forest front. YAML 19Ah8TqSyCFCzpoKFzbAC5oEqa7_8i5Cw.
- Gate 163 nodes / 474 works / refs consistent. Commit 0cdc420; public HTML byte-identical. Complete Athena Club three-cover grid and both lead pixels fresh-loaded and visually inspected. Progress next=415 processed=415 added=333. No leaf reached 10.

### 2026-09-17 17:51 CEST - intake 415-416 deployed
- 415 Every Heart a Doorway expanded to the current eleven-book Wayward Children card in whimsical-doors (now 6): Every Heart a Doorway through Through Gates of Garnet and Gold (2026). Macmillan defines the series as children returning from portal-fantasy worlds to a school because they cannot readjust; its own first-book description calls it a fresh take on portal fantasy. The individualized enchanted thresholds make Whimsical doors exact. One-pass complete-series review shipped eleven English fronts, using coordinated Tor/Macmillan art where available. YAML 1T-LkiMF9s_uDBSsZnDr_hKiL1HlmzziC.
- 416 Exhalation -> hard-conceptual-sf (now 4). PRH describes nine idea-driven stories tackling old human questions and new quandaries; SFE emphasizes Chiang's formal intellectual control across time, AI, entropy and free will. Rigorous thought experiment is the collection's common engine. One-pass selected Knopf's clean English black constellation front, OL 8793546. YAML 1EXMsqkkQD9oHDnptkdHIWdlItBUAdbAY.
- Gate 163 nodes / 476 works / refs consistent. Commit b5428bd; public HTML byte-identical. Wayward Children's eleven-book route/grid and Exhalation lead pixels fresh-loaded and visually inspected. Progress next=417 processed=417 added=335. No leaf reached 10.

### 2026-09-17 18:20 CEST - intake 417-418 closed
- 417 Expecting Someone Taller -> comic-fantasy (now 2). SFE calls it Holt's first comic fantasy and specifically genially myth-based; Hachette frames Malcolm's accidental inheritance of a giant's world-ruling powers as absurd, hilarious fantasy. Comic mode governs its Wagnerian/Norse myth in contemporary England, making Comic fantasy closest. One-pass selected the sole detailed English illustrated front, OL 284511. YAML 1JtjoPnP2qwkWI5OEPT1vcxJFTrYAFjM8.
- 418 Fafhrd and Grey Mouser deduped against the existing Fafhrd and the Gray Mouser card in sword-and-sorcery. Existing card contains the seven core collections, Two Sought Adventure material through The Knight and Knave of Swords; SFE confirms the cycle and Leiber's central role in Sword and Sorcery. No new site/Drive mutation.
- Gate 163 nodes / 477 works / refs consistent. Commit 8c70e7e; public HTML byte-identical. Expecting Someone Taller route/lead pixels fresh-loaded and visually inspected. Progress next=419 processed=419 added=336. No leaf reached 10.

### 2026-09-17 18:52 CEST - intake 419-420 deployed
- 419 Failed State expanded to the three-book Tropic of Kansas universe card in orwellian-dystopia (now 7): Tropic of Kansas, Rule of Capture, Failed State. SFE treats them as one near-future American sequence, moving from authoritarian rule/resistance to secret trials of state enemies and extrajudicial murder, then national collapse and a tribunal attempting new law. Overt coercion through law, police power and punishment makes Orwellian dystopia closest. One-pass selected three English fronts. YAML 1uEW13pbyaioAzbECT2g_mEBtXbGjCTTV.
- 420 Fall; or, Dodge in Hell -> technomorphosis (now 9). Harper describes technology turning a dead man's scanned brain into digital consciousness and ultimately creating Bitworld, an eternal afterlife for humanity. Technology transforms death, mind, society and the form of human existence rather than remaining a tool. One-pass selected the clean English William Morrow black/red front, OL 8742303. YAML 1pl4OV0tLnO50T6pzD9btui_Gftr_GRnF.
- Gate 163 nodes / 479 works / refs consistent. Commit 472cde3; public HTML byte-identical. Complete Tropic of Kansas three-cover grid and Fall lead pixels fresh-loaded and visually inspected. Progress next=421 processed=421 added=338. No leaf reached 10.

### 2026-09-17 19:22 CEST - intake 421-422 deployed
- 421 Fata Morgana -> fantasy-mystery (now 8). SFE calls the 1871 Paris fabulation proto-Steampunk; Open Road describes Inspector Picard investigating an apparently infallible fortune-telling machine, possible con, murders and a final supernatural confrontation. Investigation supplies the spine and fantastic ambiguity the mystery. One-pass selected Open Road's detailed black-and-white magician front. YAML 11pVqNYVERHzIhSSknLXUjOnF7dqLavgr.
- 422 Fear -> modern-goth (now 8). SFE calls it a classic psychological study of a man tortured by repressed hours and demons of guilt; Galaxy Press describes a contemporary skeptic pursued by an evil turning his familiar town against him. The modern everyday world becoming a persecutory supernatural labyrinth fits Modern Goth. One-pass chose the English blue/green clock-tower illustrated front, OL 6821701. YAML 10XOuNLp8V1OdOIdC9LU5V6gYpXha562d.
- Gate 163 nodes / 481 works / refs consistent. Commit dbc8a86; public HTML byte-identical. Both exact routes and cover pixels fresh-loaded and visually inspected. Progress next=423 processed=423 added=340. No leaf reached 10.

### 2026-09-17 19:51 CEST - intake 423-424 closed, both no-add
- 423 Fight Club skipped as non-speculative. SFE explicitly says its hints of a near-future setting do not quite make it SF; the novel is transgressive satire of cults, consumer anomie and destructive ideology. Tyler is the narrator's dissociated identity, not a fantastic being. No site/Drive mutation.
- 424 Finder deduped against the complete four-book Finder Chronicles card already in retro-space-opera, with Finder, Driving the Deep, The Scavenger Door and Ghostdrift and coordinated PRH covers. SFE confirms the series. No site/Drive mutation.
- Gate 163 nodes / 481 works / refs consistent. Commit ee0e558 records progress only. Progress next=425 processed=425 added=340. No leaf changed.

### 2026-09-17 20:25 CEST - intake 425-426 deployed
- 425 Fire Dance expanded to the complete three-book Harp and Ring Sequence in court-intrigue (now 5): Last Song Before Night, Fire Dance, The Poet King. Macmillan calls it lyrical high fantasy and centers court intrigue, shadowy power, espionage, diplomacy, conspiracy and rulers around magical poets and political crisis. Sustained palace/power struggle makes Court intrigue most specific. One-pass shipped the coordinated detailed English Tor fronts. YAML 10_gylkTOEEHa8V3KkqE693y3fx4SINKb.
- 426 Fleet Elements expanded to the six core novels of Dread Empire's Fall in political-space-opera (now 9): The Praxis, The Sundering, Conventions of War, The Accidental War, Fleet Elements, Imperium Restored. SFE/Harper ground imperial collapse, the multispecies ruling Convocation, civil war and restoration; governance and competing species' claims to power drive both trilogies. One-pass shipped six English space-battle fronts. YAML 1zVa8ugEqzN5XLReDki3T61BHOP1nl3Nc.
- Gate 163 nodes / 483 works / refs consistent. Commit 151cb0d; public HTML byte-identical. Both complete grids/lead pixels fresh-loaded and visually inspected. Progress next=427 processed=427 added=342. No leaf reached 10.

## 2026-09-21 10:53 CEST - intake 679-680
- #679 The Bone Shard Daughter -> complete The Drowning Empire trilogy in Political fantasy -> Court intrigue -> Dynastic intrigues (7->8). Hachette grounds bone-shard constructs enforcing imperial rule, a disinherited heir reclaiming the throne, revolution, weak alliances, rebel armies and threatened Sukai dynasty. Magic supplies the means; contested legitimacy/ruling-house survival governs. Three official covers inspected.
- #680 The Secret Commonwealth DEDUPED into and completed His Dark Materials shared-world card: added the complete Book of Dust trilogy (La Belle Sauvage, The Secret Commonwealth, The Rose Field) to the existing original trilogy. SFE explicitly calls them two conjoined series in one universe. Three Book of Dust publisher covers inspected.
- Gate 246 nodes / 676 visible works / refs consistent. Progress next=681, processed=680, added=533.

## 2026-09-21 11:13 CEST - intake 681-682
- #681 The Book of Form and Emptiness -> Magic realism -> Sensory magic realism (2->3). PRH/Ozeki ground contemporary grief, hoarding, school and library life in Benny's impossible hearing of manufactured objects' emotional voices, including a Book narrating his life. Impossible perception reveals hidden knowledge; official PRH cover inspected.
- #682 The Book of Hidden Things -> Magic realism -> Ontological magic realism (2->3). PRH/PW ground contemporary Puglia crime and friendship alongside miraculous healing, an arcane manuscript and a hidden realm; Dimitri says he used his own world with magic as a base note. Supernatural truth and delusion deliberately remain in competition. Official PRH cover inspected.
- Gate 246 nodes / 678 visible works / refs consistent. Progress next=683, processed=682, added=535.

## 2026-09-21 11:45 CEST - intake 683-684
- #683 The Book of Koli -> complete Rampart trilogy in Ruined Earth (8->9). SFE explicitly sets it far after civilization-ending Holocaust: balkanized successor terrain, buried technology treated as magic, ancient AI; Hachette adds engineered deadly nature and lost London tech. Remote inherited ruins govern over immediate survival. Three official Hachette covers inspected.
- #684 The Book of Lamps and Banners EXCLUDED as predominantly non-speculative crime. Hachette markets it as a hard-boiled psychological thriller/amateur-sleuth hunt; the manuscript's power is only rumored. SFE says the wider Cass Neary series gradually develops uncannily prescient responses, but that marginal thread does not make this candidate's governing engine speculative. Per mixed-oeuvre rule, no card.
- Gate 246 nodes / 679 visible works / refs consistent. Progress next=685, processed=684, added=536.

## 2026-09-21 12:12 CEST - intake 685-686
- #685 The Book of Three HELD at full Quest fantasy. Macmillan grounds the five-novel Chronicles of Prydain in an invented Welsh-inspired land, Taran's journey to heroism and an epic good/evil struggle; root-down it reaches Quest fantasy, now closed at 10 pending sourced split. No sibling leaf fits and pure-parent rule prevents direct Epic placement.
- #686 The Breast -> Atemporal -> Fabulation -> Body myth (2->3). SFE explicitly calls Roth's literal giant-breast transformation Fabulation/Absurdist SF; Penguin calls it fantasy reworking Kafka through body, desire and existential meaninglessness. Transformed body is the novella's whole reality/argument. Official Penguin cover inspected.
- Gate 246 nodes / 680 visible works / refs consistent. Progress next=687, processed=686, added=537.

## 2026-09-21 12:42 CEST - intake 687-688
- #687 The Breath of the Sun HELD at full Quest fantasy. Aqueduct/PW ground a secondary-world mountain pilgrimage and blasphemous summit expedition; SFE calls it equipoisal fabulation/fantasy/self-parodying SF and notes the summit extends into space and technology may reach it. Root-down the invented-world journey and summit goal reach Quest fantasy; no sibling is better, and Quest is closed at 10.
- #688 The Bridge -> Atemporal -> Fabulation -> Inner space -> Psychogeographic fabulation (3->4). Banks grounds a comatose man's vast surreal bridge-world where dream/fantasy, past/future and voices fuse and explicitly credits Lanark; SFE calls the Bridge a matrix of his life. Impossible place externalizes damaged psyche and desire to remain unconscious. Official author-site cover inspected.
- Gate 246 nodes / 681 visible works / refs consistent. Progress next=689, processed=688, added=538.

## 2026-09-21 13:27 CEST - approved Political space opera five-way partition in progress
- the curator ordered Political space opera converted to a pure umbrella with five exhaustive leaves: Interstellar court politics (Teixcalaan, Vorkosigan), Revolutionary space opera (Seven Devils, Sun Chronicles, Empress of Forever), Post-scarcity politics (Culture), Space Succession Opera (Dread Empire's Fall, Imperial Radch), Cosmological politics (Hyperion).
- Revolutionary definition explicitly includes overthrow OR liberation from an imperial order. Record future possible subdivision when capacity/evidence warrants it: pre-collapse/anti-imperial revolts versus pure revolutions.
- Space Succession concerns succession of political orders after imperial collapse/fracture, not dynastic heirs.
- Portrait A/B sheets sent to the curator through main; awaiting five-letter picks before wiring and deployment.

## 2026-09-21 13:38 CEST - Political space opera partition deployed
- the curator selected portrait string ABBBB. Wired 249 Interstellar court A, 250 Revolutionary B, 251 Post-scarcity B, 252 Space Succession B, 253 Cosmological B; all resized 1024x1536 WebP.
- Political space opera is now a pure five-child umbrella; exact partition 2/3/1/2/1 and all nine prior cards preserved exactly once. Commit a8d3109 pushed; public deployment live.
- Fresh independent page loads and actual pixels verified all five portraits, breadcrumbs and leaf titles. Public umbrella: https://gusoder.github.io/sff-taxonomy-browser/#political-space-opera
- Verifier 251 nodes / 681 visible works / refs consistent.

## 2026-09-21 13:41 CEST - intake 689-690
- #689 The Bridge (J. S. Breukelaar) -> Supernatural and dark -> Dark fantasy (6->7). SFE grounds an escaped cult-created Monster/story-mediated horror; Meerkat explicitly calls the contemporary college/cult novel Dark Fantasy, supernatural and paranormal, with Mades, part-witch rescuer and necromancy. Official Meerkat cover inspected.
- #690 The Brilliant Death -> complete two-book duet in Political fantasy -> Court intrigue -> Dynastic intrigues (8->9). PRH grounds five controlling families, poisoned patriarchs, heirs summoned by Vinalia's ruler, palace transformation/infiltration, then allied streghe against the dictatorlike Capo. Magic/gender transformation are deep themes; threats to ruling families and control of Vinalia govern the shared plot. Two official PRH covers inspected.
- Gate 251 nodes / 683 visible works / refs consistent. Progress next=691, processed=690, added=540.
- Drive YAML: The Bridge https://drive.google.com/file/d/16cejTKY19T6n59TK_9la_37bMhQRTxZU/view?usp=drivesdk&authuser=gusoder%40gmail.com ; Brilliant Death https://drive.google.com/file/d/1g3lu5XhjqeSfQ24pWVIYIJagg7ASWglA/view?usp=drivesdk&authuser=gusoder%40gmail.com
- Deployment db641d1 fresh-load pixel verification passed: Dark fantasy visibly 7 fictions; Dynastic intrigues visibly 9 fictions, with covers rendering. Public leaves: https://gusoder.github.io/sff-taxonomy-browser/#dark-fantasy and https://gusoder.github.io/sff-taxonomy-browser/#dynastic-intrigues

## 2026-09-21 14:02 CEST - Quest fantasy split and held-queue release
- Quest fantasy is now a pure umbrella with locked complete partition: Classic quest fantasy 5, Revisionist quest fantasy 3, Fairytalesque quest fantasy 2. Portrait picks AAB installed as images 254-256.
- Released held #661 Tess of the Road -> Revisionist quest fantasy (3->4): feminist/self-recovery road reframes who may be a quest hero and what victory means. Official PRH cover inspected. Drive https://drive.google.com/file/d/161ecv86O3CgwW4GbrFKb9qdxh9nfrrAH/view?usp=drivesdk&authuser=gusoder%40gmail.com
- Released held #685 The Book of Three as complete five-book Chronicles of Prydain -> Classic quest fantasy (5->6): Taran maturation, fellowship, ancient evil, world stakes. Complete series Open Library cover pass. Drive https://drive.google.com/file/d/1oA2pFQqTAOSnY0XZ8OyifhYxFgLUZL-q/view?usp=drivesdk&authuser=gusoder%40gmail.com
- Released held #687 The Breath of the Sun -> Revisionist quest fantasy (4->5): sacred summit pilgrimage interrogates faith, truth, exploration and heroic conquest. Official Aqueduct cover inspected. Drive https://drive.google.com/file/d/11rcW3ahAVy96ln9iy4EmFq4snLLhtWJl/view?usp=drivesdk&authuser=gusoder%40gmail.com
- Gate 254 nodes / 686 visible works / refs consistent. Progress next=691, processed=690, added=543. Commit b740353 pushed; Pages propagation pending fresh pixel closeout.

## 2026-09-21 14:09 CEST - intake 691-692
- #691 The Buried Giant -> Historical fantasy -> Period fantasy -> Celtic fantasy (2->3). SFE/PRH place its memory quest in post-Arthurian Britain amid Britons, Saxons, Gawain, ogres and a dragon-induced amnesia. The Celtic-British legendary-historical stage governs over quest form and memory allegory. Official PRH cover inspected.
- #692 The Butcher Boy EXCLUDED as non-speculative literary fiction. Pan Macmillan, PRH and Booker describe a 1960s small-town Irish stream-of-consciousness descent into madness and murder; the monstrous language and unstable voice are psychological, with no impossible event or speculative world claim. No card.
- Gate 254 nodes / 687 visible works / refs consistent. Progress next=693, processed=692, added=544.
- Deployment 9dcdd86 fresh-load pixel verification passed: Celtic fantasy visibly 3 fictions with correct breadcrumb/portrait and rendered grid. Public leaf https://gusoder.github.io/sff-taxonomy-browser/#celtic-fantasy

## 2026-09-21 14:41 CEST - intake 693-694
- #693 The Cabin at the End of the World EXCLUDED as speculative ambiguity insufficient for this taxonomy. Harper and the agency call it psychological/home-invasion horror; its intruders claim a family sacrifice will stop the apocalypse, but the novel preserves the possibility of delusion and supplies no authoritative supernatural mechanism. Physical disasters on television do not establish causation. No card.
- #694 The Castle -> Atemporal -> Fabulation -> Classic Fabulation (3->4). SFE calls Kafka’s unfinished novel Absurdist SF: K assaults the fog-shrouded workings of the Castle while the world becomes an endless office of transaction. Its inaccessible authority/bureaucracy composes reality itself. Official PRH cover inspected.
- Gate 254 nodes / 688 visible works / refs consistent. Progress next=695, processed=694, added=545.
- Deployment 4dbdddf fresh-load pixel/DOM verification passed: Classic Fabulation visibly 4 fictions; The Castle cover loaded at 293x450, with correct breadcrumb and portrait. Public leaf https://gusoder.github.io/sff-taxonomy-browser/#classic-fabulation

## 2026-09-21 15:17 CEST - intake 695-696 locally complete, deployment blocked on rebuilt GitHub auth
- Recovery: restored exact 989-entry queue from Drive; indices 691-694 matched recent work exactly. Progress rebuilt at next=695/processed=694/added=545, then candidates/progress/provenance committed locally for durability; current repo push awaits fresh device auth.
- #695 The Castle of Iron DEDUPED into existing original Incomplete Enchanter trilogy card in Multiverse fantasy. SFE/Baen establish Harold Shea's symbolic-logic travel among parallel myth/literature worlds; the card already includes Castle. Added its missing cover after one-pass review; visible-work count unchanged.
- #696 The Castle of Otranto -> Ghost story -> Haunted House (9->10). SFE identifies it as the work that introduced Gothic fiction; PRH grounds supernatural omens, ancestral usurpation curse and threatened dynasty inside Otranto. The castle and place-bound family haunting are the engine. Official PRH cover inspected.
- Gate 254 nodes / 689 visible works / refs consistent. Progress next=697, processed=696, added=546. Local only pending GitHub device auth; Haunted House has reached 10 and now requires a sourced complete split proposal before any further additions.

## 2026-09-21 15:42 CEST - intake 697-698 locally complete, deployment blocked on rebuilt GitHub auth
- #697 The Centauri Device -> Classic space opera -> Pulp -> Golden-age space opera (9->10). SFE calls it darkly sardonic/disgruntled Space Opera and Hachette grounds a lowlife captain, vicious space war and sentient doomsday bomb; its 1974 attack on first-wave conventions belongs at that tradition’s late edge, before New Space Opera. Cover inspected.
- #698 The Changeling (Victor LaValle) -> Urban fantasy -> Fae founders (3->4). PRH calls it a dark fairy tale of New York; Time/USA Today ground witches, trolls and changeling folklore remade through parenting, race and internet life. Ancient Faerie child-substitution surviving in modern NYC governs. Official PRH cover inspected.
- Gate 254 nodes / 691 visible works / refs consistent. Progress next=699, processed=698, added=548. Local only pending GitHub device auth. Golden-age space opera reached 10 and now requires a sourced complete partition proposal before another addition.

## 2026-09-21 16:08 CEST - recovered-auth deployment live
- GitHub device authentication completed as GuSoder; pushed queue durability and intake commits through e0d41d2.
- Fresh independent loads and screenshots verified Haunted House at 10 with The Castle of Otranto cover loaded 293x450; Golden Age space opera at 10 with The Centauri Device cover loaded 180x203; Fae Founders at 4 with The Changeling cover loaded 292x450; Multiverse fantasy at 4 and The Incomplete Enchanter detail at 3 books with The Castle of Iron cover loaded 180x243.
- Public leaves: https://gusoder.github.io/sff-taxonomy-browser/#haunted-house ; https://gusoder.github.io/sff-taxonomy-browser/#golden-age-space-opera ; https://gusoder.github.io/sff-taxonomy-browser/#fae-founders ; https://gusoder.github.io/sff-taxonomy-browser/#multiverse-fantasy/the-incomplete-enchanter
- Verifier remains 254 nodes / 691 visible works / refs consistent. Progress next=699, processed=698, added=548.

## 2026-09-21 16:17 CEST - intake 699-700
- #699 The Circus of Dr. Lao HELD at Period fantasy. SFE, Nebraska and Orion ground actual mythical creatures/gods transforming a Depression-era Arizona town. It passes Fantasy -> Real Earth Universe -> Historical fantasy -> Period fantasy, but the existing Weird West leaf is explicitly nineteenth-century and pure-parent rules prevent direct placement. This reinforces the unresolved late-20th-century/modern Period fantasy gap.
- #700 The Citadel of Fear -> Supernatural dark -> Supernatural fiction -> Ancient tormentors -> Elder gods (3->4). Under the curator's 2026-09-19 magic/SF dividing rule, actual gods and dark magic make it Fantasy rather than Lost-world SF. Flame Tree grounds the hidden Aztec city, disturbed ancient gods, nightmare creatures and dark magic unleashed into the modern world; the ancient worshipped being's intrusion drives the horror. Official Flame Tree cover inspected.
- Gate 254 nodes / 692 visible works / refs consistent. Progress next=701, processed=700, added=549.
- Deployment 657d59c fresh-load pixel/DOM verification passed: Elder gods visibly 4 fictions; The Citadel of Fear cover loaded 162x250 with correct breadcrumb/portrait. Public leaf https://gusoder.github.io/sff-taxonomy-browser/#elder-gods

## 2026-09-21 16:35 CEST - Post-Holocaust Survival split AAA
- the curator selected AAA. Converted Post-Holocaust Survival to a pure three-child umbrella: Post-pandemic survival 3 (Earth Abides, I Am Legend, Station Eleven); Post-nuclear survival 2 (Alas, Babylon, Dr. Bloodmoney); Terminal wastelands 5 (Lost Everything, The Road, These Prisoning Hills, In the Country of Last Things, Shelter).
- Terminal wastelands is a flagged taxonomy coinage and condition-based complement: mixed-cause or unspecified collapses whose defining condition is traversing/enduring the devastated landscape rather than one named cause. Recovery may exist, but the wasteland remains governing.
- Installed AAA portraits 257-259, each cropped from the visually inspected left panel and resized 1024x1536 WebP.
- Verifier 257 nodes / 692 visible works / refs consistent. Deployment pending.
- Deployment aa6db24 fresh-load pixel verification passed: pure umbrella visibly has 3 subgenres; Post-pandemic 3, Post-nuclear 2, Terminal wastelands 5. Correct AAA portraits, breadcrumbs and cover grids render on all three leaves. Public umbrella https://gusoder.github.io/sff-taxonomy-browser/#post-holocaust-survival

### 2026-09-23 11:48 CEST - Ambiguous-magic rule (the curator ruling 11:47, verbatim: "If the world is also made up, it's fantasy (like the Baru president). If it's just some real world superstition it's not fiction imo")
- STANDING RULE (apply autonomously): magic left ambiguous (maybe real, maybe not) counts as Fantasy only when the world is also invented (secondary/made-up world, Baru Cormorant precedent). Ambiguous magic in a real-world setting that is only superstition = not speculative fiction; exclude.
- Applied: #969 We Ride Upon Sticks (Quan Barry; real Danvers, Massachusetts, 1989; witchcraft pledged, never confirmed; https://www.penguinrandomhouse.com/books/602077/we-ride-upon-sticks-by-quan-barry/, https://www.npr.org/2020/03/04/809741338/witchcraft-field-hockey-and-1980s-massachusetts-meet-in-we-ride-upon-sticks) -> EXCLUDED.
- Applied: #982 Witch Wood (John Buchan 1927; real 1640s Scottish Borders parish; witch cult, supernatural uncertain; https://en.wikipedia.org/wiki/Witch_Wood) -> EXCLUDED.
- Consistent with earlier #984 Wuthering Heights exclusion (real Yorkshire, ambiguous ghost). No site change.

### 2026-09-23 notes rebuilt after workspace reset (~10:23)
- Machine minds split live f01e346 (Robots 7 / AI 4; Stepford released). Token instinct-sff-taxonomy-push-3 (repo-only, Contents RW, exp 2026-12-22), vault "GitHub PAT (sff-taxonomy push)".
- Anti-colonial fantasy split live 1203c4e (Rebel fantasy 7 / Insurgent fantasy 3; the curator 11:09). Insurgent portrait hand fix v2 live 3c357f6.
- #948 Two Planets -> Historical first contact after full walk (the curator "do the walk" 11:35), adcdd0e. No retrofuture node or doctrine (main retracted its gloss).
- Future possibility (the curator context 11:43, not a ruling): a proto-SF / Early SF node someday; Two Planets and similar very early SF are candidates. No moves until he opens it.
- Still held: Little Brother + Merciful Crow duplicates; Plot Against America + Raven Tower pure-branch breaks; 10 stem forks.

### 2026-09-23 11:52 CEST - No-duplicates rule (the curator ruling 11:51, verbatim: "No duplicates, ever")
- STANDING RULE: one book = one card = one home. Never place a work in two leaves; resolve any straddle to the single best fit by the top-down walk.
- Applied: The Merciful Crow Duology keeps Civil revolution fantasy; Medieval dynastic intrigue card + YAML removed (leaf now 4).
- Applied: Little Brother keeps Technothriller (Modern day gate: recognizable present-day San Francisco, real hacking/crypto drive the thriller); Postcyberpunk card removed (leaf now 5). Card covers aligned to the Tor/Macmillan set; YAML rationale corrected (it wrongly argued Cyberpunk). KNOWN_PARITY exception cleared in verify_local.sh.
- Totals 304 nodes / 891 cards / 1,910 books.

### 2026-09-23 12:05 CEST - Alt Prewar (the curator ruling 12:03, verbatim "Alt Prewar then")
- New leaf Alt Prewar (307) under Period alterations; The Plot Against America moved off the branch (divergence 1940-43, snaps back via ordinary events, not Atemporal). Period alterations now pure; removed from verify KNOWN list. Portrait 307 generated at creation.

- 2026-09-23 12:20 the curator ruled ("Yes") The Raven Tower -> Epic fantasy > Invented Mythology (its core is the invented theology; dynastic plot is scaffolding). Dynastic intrigues is now pure; KNOWN pure-branch exceptions list is empty. Tree: 305 nodes, 891 cards / 1,910 books.

## Standing grant: autonomous leaf creation (the curator 2026-09-23 12:27:10)
the curator's words: "No, don't visibly park them. If the umbrella genre is far down the tree, (like at least 5 steps down right now I feel) and there is space (like 2/3/4 genres only), you see a pattern in naming and can follow it, you are allowed to just make leaves yourself. But preferably I would like to be served leaf suggestions here, in any case a link to the tree for me to inspect"
- Scope: parent umbrella at depth >= 5 (Speculative fiction = 0), currently 2-4 children, and a clear sibling naming pattern to follow -> may create the leaf myself (portrait at creation as usual).
- Preference: still serve leaf suggestions to him first where possible; always give him a tree link to inspect.
- Never visibly park books on stems.

## Standing rule: existing-leaf placements and cover art are autonomous (the curator 2026-09-23 12:33:26)
the curator's words: "9,10,11: you don't need my permission to place books with a genre that fits, c'mon. You got guidelines for pick cover art, I don't have time for that"
- Placing a book in an EXISTING leaf that fits: just do it, report after.
- Cover art: follow the cover guidelines (one-pass, flat art, English title visible); never bring cover choices to him.
- Only new leaves, names and structure go to him (within the 12:27 autonomous-leaf grant above).
- Executed at 12:35: Trail of Lightning (Sixth World, 2 books) -> navajo-myth-fantasy; The Year of the Witching -> isolationist-fantasy; The Sinful Ones (= 1950 "You're All Alone", one card; #870 merged as duplicate) -> absurdist-constructed-realities. added 732 -> 735. Tree: 305 nodes, 894 cards / 1,914 books.
- Still awaiting the curator on 8 new-leaf suggestions (Antebellum fantasy, Hidden creators, Theological space opera, Future insurgency, Noir-era fantasy, Tang fantasy, Patriarchal Dystopias, Psi saga).

## 12:40 - Noir fantasy (308) + Antebellum fantasy (309) under Industrial age fantasy
- the curator 12:37:26 "Oh, you mean Noir fantasy, yes!" -> Noir fantasy leaf, Trouble the Saints first card (Tor cover OL 10288337).
- the curator 12:38:54 "Ok, antebellum is go" -> Antebellum fantasy leaf, The Underground Railroad first card (Doubleday cover isbn 9780385542364).
- Industrial age fantasy children now in era order: Gaslight, Antebellum, Weird West, Tudorbethan, Dust Bowl, Noir, Neon (7).
- BANKED future sibling names (the curator 12:37, do NOT create yet): "Gatsby fantasy", "Deco fantasy".
- Portraits generated at creation (smart 2:3, 1024x1536 webp). added 735 -> 737. Tree: 307 nodes, 896 cards / 1,916 books.
- Remaining suggestions awaiting the curator: Hidden creators, Theological space opera, Future insurgency, Tang fantasy, Patriarchal Dystopias, Psi saga.
- 12:41 the curator VETO on Hidden creators: "No, supernatural is getting crowded without a good plan forward, hold it". Supernatural fantasy (Nocturne) is FROZEN for additions (new leaves and placements) until he has a plan. Jonathan Hoag -> pending-ruling queue.

## 12:55 - Dystopian rebellion (310) under Totalitarian dystopia
- the curator 12:52:19 "Dystopian rebellion is awesome, let's go!"; 12:53:53 "Sure, hang it there" (Totalitarian dystopia, not Social dystopian future, which excludes police states).
- The Wild Boys first card (Grove cover OL 568697). Totalitarian dystopia definition widened to three modes (Huxleyan, Orwellian, Dystopian rebellion). added -> 738.

## 14:05 - Far shores fantasy (311-314) under Fantasy Realms
- the curator 14:02:25 "Go" on the Far shores spec.
- Fantasy Realms > Far shores fantasy (sibling after Gothic) > Chuanqi (Shenmo moved whole from Fairy-tale revision with Master Li + 278 portrait; Xuanhuan new leaf, Under Heaven first card, Penguin cover OL 9946446) and Khayal (new leaf; The Lions of Al-Rassan moved from Andalusian fantasy, which keeps The Bird King).
- BANKED (do NOT create): Xianxia (under Chuanqi), Alf Layla (under Khayal).
- Fairy-tale revision now 3 children (inversion, transplant, expansion). No empty works folders left by the moves.
- added 738 -> 739 (Under Heaven only). Tree: 312 nodes, 898 cards / 1,918 books.

## 15:27 - Historical fold (Proto SF 315, Period SF 316)
- the curator 15:05:52 "Execute". SF > Historical: 8 children -> Proto SF / Period SF / Alternate history.
- Proto SF: Lost world fiction, Scientific adventure, Fantastic voyage, Gothic SF (moved whole). Period SF: Steampunk, Psi noir, Historical first contact (moved whole).
- Two Planets moved Historical first contact -> Scientific adventure (written in its own era).
- Mem (2018, 1920s) NOT moved: no Period SF leaf fits (steam-era / telepathy / aliens). Stays in Mad-science Gothic, flagged to the curator.
- Wild Seed leaf NOT created (pending ruling). Tree: 314 nodes, 898 cards / 1,918 books.
- 15:38 the curator "Can you change it to Period SF?" -> Period Sci-Fi renamed Period SF (id/anchor period-sf, portrait 316-period-sf.webp), harmonizing with Proto SF.

## 16:10 - Deco SF (317) under Period SF; Psi noir retired
- the curator 15:53 "But wait" halted Retro Gothic SF (nothing had been committed). Rule 15:55: direct subgenres under Period umbrellas are named for the era.
- the curator 16:00:59 "Yay, finally a Deco Genre! Execute Deco SF" -> Deco SF leaf (Art Deco interwar, ~1918-1939): Mem (from Mad-science Gothic) + The Listener (from Psi noir). Psi noir left empty -> retired (node, folder, portrait 286 file kept in repo root).
- Period SF children: Steampunk, Deco SF, Historical first contact. Historical first contact (14th c. + prehistory) still breaks the era-naming rule - open question for the curator.
- Tree: 314 nodes, 898 cards / 1,918 books.

## 16:26 - Theological space opera (318) under New space opera; Cosmological politics retired
- the curator 16:15:12 "Ok, execute" (after the drops-to-4 exchange). Theological space opera leaf beside Political space opera: The Hyperion Cantos (moved; SFE Simmons entry grounds pilgrimage/Papacy/Messiah/Transcendence) + The Unreasoning Mask (new card, intake #3 resolved; cover OL 10176146, 1981 paperback).
- Cosmological politics left empty -> retired. Political space opera: 4 subgenres.
- added +1. Tree: 314 nodes, 899 cards / 1,919 books.

## 16:39 - Hidden history SF (319) under Historical; Historical first contact retired
- the curator 16:35:22 "Execute, resolve Historical first contact and place a Hidden history SF next to Alternate history with those books, move in Wild seed". 16:37:53 addendum: Hidden history = unrecorded events; Period SF = period aesthetics, SF elements open or hidden (in both genre.yaml `marker` + definitions).
- Hidden history SF: Eifelheim, The Inheritors (moved), Wild Seed (new card, cover OL 10279447 Grand Central 2020). Psi saga name dropped; pending #8 resolved.
- Historical: Proto SF, Period SF, Alternate history, Hidden history SF. Period SF: Steampunk, Deco SF.
- added +1. Tree: 314 nodes, 900 cards / 1,920 books.

## 2026-09-23 18:01 - Patriarchal Dystopias created; Hoag placed
- New leaf Patriarchal Dystopias under Social dystopia (the curator 17:43:49 "Ok then you can execute Patriarchal dystopia"). Definition: dystopia whose engine is patriarchy, male rule as the organizing principle of the oppression. Portrait 320.
  - The Handmaid's Tale (series card with The Testaments) moved from Childless Dystopias.
  - New card: The Holdfast Chronicles (Charnas; Walk to the End of the World, Motherlines, The Furies, The Conqueror's Child), 1 card / 4 books. Source SFE charnas_suzy_mckee.
  - the curator stated the Childless Dystopias cards are The Handmaid's Tale, Children of Men, Atomised, Greybeard; with Handmaid's moved, Childless holds 3 cards.
- The Unpleasant Profession of Jonathan Hoag (Heinlein 1942) added to Absurdist constructed realities, not Supernatural (the curator 17:47:56: it's fabulation). 5 cards on the leaf.
- Tree: 315 nodes, 902 cards / 1,925 books.

## 2026-09-23 18:26 - Intake counter fix
- #989 Zuleika Dobson (Beerbohm) was already placed in Comic fantasy (in tree since before the 03:42 mirror sync); progress.json was one behind. processed=989/989. The added count was not changed.

## 2026-09-23 21:40 - Gap-intake rulings: Wuxia, The Incandescent
- the curator 21:26 "Execute Wuxia for The Water Outlaws": new leaf Wuxia under Chuanqi (third after Shenmo, Xuanhuan), portrait 321-wuxia.webp; The Water Outlaws (S. L. Huang) first card. Commit 72e1cc3.
- the curator 21:39 "Put it in contemporary for now, keep magic school in mind for later": The Incandescent (Emily Tesh) -> Contemporary fantasy > Magical coming-of-age, next to Harry Potter.
- BANKED future leaf (do NOT create yet): "Magic school". Seed: teacher-POV magic-school books (The Incandescent); Harry Potter and other school-set coming-of-age books are candidates to revisit if it is created.
- the curator 21:48 "Execute": Audition for the Fox (Martin Cahill) -> Epic fantasy > Invented Mythology (3->4). Time-travel-fantasy leaf question now covers only The Everlasting.
- the curator 22:00 "Cool, do the umbrella bundle": new umbrella Epic fantasy > Hard fantasy (EoF term, Westfahl), holding Hard magic (moved, 9 cards) and new leaf Time magic; The Everlasting (Harrow) first Time magic card. Portraits 322-hard-fantasy, 323-time-magic.
- the curator 22:16 "Execute": new leaf Cyberpunk > LitRPG (sibling of Metaverse; term coined 2013, EKSMO). Seed: Dungeon Crawler Carl series card (8 books). Portrait 324-litrpg.
- the curator 22:38 "Execute": Robots split. Robots is now an umbrella over Androids (SFE term: Do Androids Dream, Stepford Wives, Luminous, Caves of Steel, + Annie Bot from the hanging list) and Sentient Robots (I, Robot, Murderbot, Service Model, Neom, + Robots of Gotham by the load-bearing test, vetoable). The Cyberiad moved to Humorous SF (mode over subject). Portraits 325-androids, 326-sentient-robots.
- the curator 22:41 "Ok, unfreeze it": Supernatural fantasy branch UNFROZEN (lifts the 12:41 freeze). Placed held B books: Katabasis -> Surreal afterlife, The Reformatory -> Ghost speakers, Starling House -> Contemporary haunted house. Locus Rec tier 2 still parked.
- the curator 23:01 "execute": Alternate history fantasy split into pure umbrella over Alt Crusade (The Devils), Alt Ming (The Radiant Emperor), Alt Spice Route (Amina al-Sirafi, from hanging list), Alt Flintlock (Alvin Maker, Temeraire, Sorcerer Royal, Angel Mage), Alt Diesel (Dead Djinn, Summerland, Burn, Dominion of the Fallen). Portraits 327-331.
- the curator 23:12: Death of the Author (Okorafor) EXCLUDED as not SFF - literary frame; the inner robot novel doesn't make the book SFF. Dropped from hanging list and intake; recorded in progress.json excluded[]. Do not resurface.
- the curator 23:13: Martin Hench trilogy (Doctorow: Red Team Blues, The Bezzle, Picks and Shovels) EXCLUDED as not SFF - real tech, no speculative premise. Recorded in progress.json excluded[]. Do not resurface.
- the curator 23:14: A Granite Silence (Nina Allan) EXCLUDED as not SFF - historical crime novel, no speculative element. Recorded in progress.json excluded[]. Do not resurface.
- the curator 23:16: Looking Glass Sound (Catriona Ward) EXCLUDED as not SFF - psychological/metafictional thriller, nothing supernatural on the page. Recorded in progress.json excluded[]. Do not resurface.
- the curator 23:22 "Execute": Corey Fah Does Social Mobility (Waidner) is SFF -> Classic Fabulation > Absurdist constructed realities (6->7). Cover: Penguin UK front via Amazon (no OL cover).

## STANDING INTAKE RULE - "Absurd Shit" rule (the curator 2026-09-23 23:29)
Verbatim: "I'm making an 'Absurd Shit'-rule: if it's too absurd to say if it's SF or Fantasy, and it's not even a Fabulation: kill it"
Apply autonomously without asking per case: too absurd to call SF or Fantasy AND no Fabulation node fits -> exclude as not SFF. Always check the Fabulation branch first (a Fabulation fit keeps the book). Log each kill in sweep.log as "-Title (Absurd Shit rule)" and in progress.json excluded[] with the rule named.
- the curator 23:30: The Salt Oracle (Lorraine Wilson) killed under the Absurd Shit rule (first kill). Recorded in progress.json excluded[].
- the curator 23:33 "I agree": Sleeping Worlds Have No Memory (Barsukov) -> SF > Atemporal > New Weird (6->7). Cover: Arc Manor (publisher) product image; OL has none.
- the curator 23:46 "go": new leaf Fantasy > Real Earth > Mythic retelling > Biblical fantasy (Bible retold as fantasy, miracles are real magic). Seed: HIM (Ryman). Portrait PENDING: daily image limit hit at 23:46; generate 332-biblical-fantasy.webp after midnight. Hanging list A closed.
- the curator 23:58 "Sure, go dystopian rebellion": Notes from a Regicide (Fellman) -> Totalitarian dystopia > Dystopian rebellion (1->2).
- 00:04 Biblical fantasy portrait generated (332-biblical-fantasy.webp, 1024x1536) after the daily image cap reset.
- the curator 11:08 "Execute": Once Was Willem (M. R. Carey) -> Supernatural fantasy > Undying (2->3). Cover: Orbit US jacket (Hachette CDN).
- the curator 11:13 "Right, execute": Slow Gods (Claire North) -> Future history in space (4->5). Cover: OL id 15215660.
- the curator 11:39 "Execute with Mythic power struggle": new umbrella Mythological Fantasy under Epic fantasy (Epic's child count unchanged, Invented Mythology moved under it); new sibling leaf Mythic Power Struggle (mythic beings from real tradition - angels, demons, gods, spirits - in personal long-running struggles; war may be offstage). Seeded: The City in Glass (Nghi Vo, 2024) - closes held #77. Portrait 333-mythic-power-struggle.webp generated 11:44. Umbrella portrait NOT made (only one portrait ruled) - header shows placeholder sparkle until the curator commissions one.
- BANKED future leaf (the curator 2026-09-24 ~14:33, do NOT create yet): "Simulated realities" under Cyberpunk next to Metaverse - worlds you're unknowingly inside vs Metaverse's jacked-in avatars. Parked because Cyberpunk's 4-child spread is nice as-is.
- the curator 15:51 "Ok execute" (after naming trail Ebooks in books -> "Scripted books in books?" and approving the yaml definition): new leaf Scripted books in books under Books in Books - reality revealed as authored text (written/narrated/computed from inside). Seeded: The Anomaly (Le Tellier; metafiction through-line, text disintegrates at the end). Closes held #114. Portrait 335-scripted-books-in-books.webp. Live-verified 15:55. Totals: 330 nodes, 1,010 cards / 2,052 books. Held: 3 (Secret Market, Ten Percent Thief, Wings Upon Her Back).
- STANDING RULE (the curator 2026-09-24 16:38, "keep the completeness rule in prompt then for the walk"): every briefing walk must list ALL children of every umbrella on a plausible route, entered or not, with one-line faults. Born from the Wings walk omitting Invented Mythology.
- the curator 16:38 "So hard science fantasy may be executed": Wings Upon Her Back (Mills) -> Hard science fantasy (5->6). His reasoning: 'visitors' speculation opens the SF side; mythology kept light, Invented Mythology + whole mythological branch ruled out ('I read alien'); author fits fantasy elements (wings) into a scientific frame (surgery). Cover: OL 14744077 (Tachyon 2024). HANGING LIST CLEARED: held 0, added 111, totals 330 nodes, 1,013 cards / 2,055 books.
- the curator 18:02 "Go" (verified on his channel, phoneconv 18:02:40): tier-2 chunk 1 (k2 1-20) executed autonomously under existing-leaf rule. PLACED 15: 51->Hidden history SF (3->4); A Half-Built Garden->Near-future first contact (1->2); A Haunting on the Hill->Contemporary haunted house (8->9); A House with Good Bones->Contemporary haunted house (9->10, FREEZES at 10); A Letter to the Luminous Deep->Cozy fantasy (2->3); A Philosophy of Thieves->Postcyberpunk (8->9); A Song of Salvation->Theological space opera (2->3); A Stranger in the Citadel->Lost Knowledge (6->7); A Tempest of Tea->Caper Fantasy (2->3); A Thousand Blues->Sentient Robots (5->6); Acts of God->Humorous science fiction (7->8, flag: possible future Scripted-books claim); After the Forest->Fairy-tale expansion (4->5); Age of Ash->Renaissance dynastic intrigue (4->5); All the Seas of the World->Court spies (4->5); Angel Maker->Steampunk (5->6). HELD 5 (tier2 held, awaiting the curator): #6 A Market of Dreams and Destiny (Folklore in Gaslight frozen), #7 A Midwinter's Tail (Contemporary mythic fantasy frozen), #9 A Song of Legends Lost (no clean leaf), #18 Among Ghosts (Dark Fantasy realms shaky), #19 An Arrow to the Moon (no Chinese-myth leaf). Covers: 12 OL + 3 Amazon (Wilde, Cheon, Bear) - all visually verified; Citadel cover is the Tachyon PRINT edition (OL audiobook cover rejected), After the Forest uses the real Tor cover (OL placeholder rejected). Totals: 330 nodes, 1,028 cards / 2,070 books. tier2 cursor 20/322.
- the curator 18:38 "If so, execute" (verified on his channel 18:38:30, his own three-leaf proposal): frozen Folklore in Gaslight (10) SPLIT into pure branch with 3 sibling leaves under Gaslight fantasy - Faeries in Gaslight (5, incl. tier-2 held #6 A Market of Dreams and Destiny, held now 4), Monsters in Gaslight (5), Circus in Gaslight (1). Portraits 336/337/338 (1024x1536 webp). Totals: 333 nodes, 1,029 cards / 2,071 books.
- STANDING RULE (the curator 2026-09-24 ~19:51): NO dirty branches - a branch holds zero direct cards; every card lives in a leaf. (Folklore in Gaslight split was the first application.)
- the curator 19:56 "Ok, execute the split anyway" (verified 19:56:23; leaf names all his, 19:46-19:49): frozen Contemporary mythic fantasy (10) SPLIT into pure branch with 4 leaves - Modern Albion Myth (7, incl. held #7 A Midwinter's Tail, held now 3), Modern Greek Myth (1), Modern Anansi Myth (1), Modern Orisha Myth (1). NAMING PRINCIPLE (his): distinct cultural myth names over continent-level labels. The Book of Love PARKED in progress.json pending_ruling[] (invented cosmology, not inherited myth; candidates: posthumous-fantasy seed vs revenants). Portraits 339-342. Totals: 337 nodes, 1,029 cards / 2,071 books.

## 2026-09-24 22:07 - Modern invented myth leaf
- modern-invented-myth created under contemporary-fantasy (the curator ruling 22:07); The Book of Love seeded from pending-ruling queue (queue empty). Portrait 343. Next free portrait: 344.

## 2026-09-25 07:49 - Modern Invented Myth moved
- modern-invented-myth now under contemporary-mythic-fantasy (the curator 07:49); label capitalized "Modern Invented Myth"; CMF def updated.

## 2026-09-25 11:21 - Ozymandian tech leaf
- ozymandian-tech created under science-fantasy (the curator ruling 11:21); A Song of Legends Lost seeded from held #9 (held now 2). Portrait 344. Next free portrait: 345.

## 2026-09-25 11:29 - STANDING RULE: no magic on the SF side
- Magic-actual books never land on the science-fiction side; crossing requires ambiguous/revealed tech (Ozymandian tech / HSF pattern). Catch in walks before presenting candidates.
- REVISIT: Invoker Trilogy book 2 publication -> re-examine A Song of Legends Lost (ozymandian-tech): tech confirmed -> hard-science-fantasy; magic confirmed -> fantasy side.

## 2026-09-25 12:36 - Dark realms rename + Among Ghosts
- dark-fantasy-realms renamed dark-realms ("Dark realms"), distinguishing from Real-Earth dark-fantasy; Among Ghosts placed from held #18 (held now 1: #19). Portrait 275 kept.

## 2026-09-25 12:46 - STANDING FIX: seeding rule
- Walks: "def fits, no leaf exists" = always a new-leaf candidate at EVERY def-fitting branch, never a bare fail. Completeness lists children; seeding covers their gaps.
- OPEN: An Arrow to the Moon placement - Modern Chinese Myth under CMF (the curator's 12:43 steer, my updated pick) vs Chinese myth fantasy under Mythic retelling. Awaiting his ruling.

## 2026-09-25 12:47 - Modern Chinese Myth leaf
- modern-chinese-myth created under contemporary-mythic-fantasy (the curator ruling 12:47); An Arrow to the Moon seeded from held #19 - HELD LIST EMPTY. CMF def updated (Chinese added). Portrait 345. Next free portrait: 346. Tier-2 cursor 20/322; chunk 2 (21-40) awaits his go.

## 2026-10-03 19:0x - Wormwood Trilogy duplicate merged
- The two Wormwood cards folded into one: kept The Wormwood Trilogy (3 books) in alien-invasion-fiction, removed the Wormwood trilogy card from near-future-first-contact (index.html, works yaml, genre.yaml). See DUPLICATES.md. Gate OK: 1307 cards.

- REVISIT (curator note phonemsg-01M4G09YH4MDQR3FXJR73B4T8E, 2026-10-09): Space marine corps (under Ground-pounders). If any Warhammer 40K / Black Library title enters the tree, re-examine the leaf; 40K may belong under a new Grimdark shelf, to be decided before readers hit Space marine corps and get confused. No 40K title is in the tree or queue as of 2026-10-09.

## 2026-10-24 15:59 - World-at-war split at ten (4-way, his names)
- Split world-at-war-fantasy (10) into War of humanity (5) / War on humanity (1) / War of immortals (2) / Eldritch invasions (2), curator "Approved" phonemsg-01M5Q31JC8YZZ7MTR9A9Y3NNZ7 on his own names (phonemsg-01M5MGX2D2SX7M222M423QDHD0) + widened immortals scope (phonemsg-01M5MH104DM8ESNC7191S2G92P). Original stays umbrella.
- Main-war rule placed the mixed cases: Malazan + Wake the Dragon + Between Dragons + Ascendant Kingdoms -> War of humanity (soft); Wall of Night alone -> War on humanity; Dark Moon + Echoes -> War of immortals; Gates of Good and Evil + Ascendant Trilogy -> Eldritch invasions.
- Portraits 781-784 (1024x1536 webp): human armies clashing / shadow swarm at the last wall (Gondor-echo tree banner edited out) / two immortals warring above a burning city / eldritch gate pouring horrors.
- Gate OK: 733 nodes, 2429 cards / 5,515 books.

## 2026-10-31 20:22 - Medieval fantasy four-way split (approved)
- Approved split phonemsg-01M69PA8ZZT9AT6DCD6BAPNWE9 of serve phonemsg-01M69P9EW3V3NAC1G363DEV105. Medieval Haunting (Otranto, Once Was Willem, + intake MC04529 The Folly of the World - provisional, ontology deliberately unresolved) / Medieval Fey (The Hood) / Medieval Folklore (Winternight, Wolf and His King, Knight's Wyrd) / Medieval Spiritual (Son of the Morning/Night, Armed in Her Fashion, Lapvona). 3/1/3/3.
- Medieval Mages held out until a book earns it. Spiritual scope (miracles/curses/faith without gods appearing) accepted phonemsg-01M69P8ES3PT64SMMGCHB3CQ8D.
- Medieval definition corrected at same approval: pre-Black-Death cap removed, full medieval cultural stage incl. 15th c.; Plague gate unchanged; no Autumn restoration.
- Portraits 858-haunting (grave-risen boy), 859-fey (leaf-dressed faerie + hooded outlaw), 860-folklore (hearth domovoi), 861-spiritual (demonic shadow over congregation), all 1024x1536, we-judged A/A/A/B. No bows, hands clean, no text.
- Folly cover OL id 10589394 (US Orbit 2012). yaml mirror moved 9 works + new folly yaml; medieval genre.yaml history entry.

## 2026-10-31 20:44 - Intake MC04530 Brothers Grossbart into Medieval Spiritual
- The Sad Tale of the Brothers Grossbart (Bullington, Orbit 2009) -> Medieval Spiritual (3->4). Existing-leaf placement under the 2026-10-30 autonomy ruling (phonemsg-01M66AQB0JEGYRYN8Q7XTWHVDX), no approval needed.
- Basis: Christian supernatural operative on-page (demons possess/walk, plague demon hunted by priest Martyn, Heinrich's soul-sale; publisher "living saints and livelier demons"); approved widened Spiritual scope covers it. Folk menagerie (werewolf, cat-men, witch, sea-monsters, salamander) disclosed as episodic crossover, not the engine. Not Plague: set 1364, pestilence past.
- Cover: US Orbit jacket from author's site, served locally (cover-the-sad-tale-of-the-brothers-grossbart.jpg, 400x600).
- Gate OK: 810 nodes, 2628 cards / 6,055 books. Commit 2dca4e9.

## 2026-10-31 20:48 - MC04531 skipped, MC04532 excluded
- MC04531 An Edge Sharp Enough (Sutanto, Harper Voyager) SKIPPED: forthcoming (publishes 2026-11-17); unpublished-volume exclusion confirmed by main 2026-10-31 20:48, no revisit obligation. Recorded in candidates.tsv.
- MC04532 Brave Like Fireweed (Jesse White) EXCLUDED: 40-page children's picture book (Union Square Kids 2024) - not an SFF novel; slipped the non-novel filter. Recorded in candidates.tsv.

## 2026-10-31 20:52 - MC04533 excluded; MC04534+35 The Lost Queen into Royal enemies romantasy
- MC04533 Bourbon, Sugar, Grace (Reisman) EXCLUDED: Tor.com 2017 novelette, shorter than a novella.
- MC04534+MC04535 collapsed: The Lost Queen trilogy (Jessica Thorne, Bookouture Second Sky 2024; A Touch of Shadows / A Kiss of Flame / A Crown of Darkness, all published) -> Royal enemies romantasy (4->5). Whole-arc: book 1 Crown-outlaw register (hunted shadow-mage vs crown knight), settling on two rival royal houses (Wren = lost queen of Asteroth's daughter; Finn = enemy king's son). Cover: book 1 jacket from publisher CDN, served locally.
- Gate OK: 810 nodes, 2629 cards / 6,058 books.

## 2026-10-31 - MC04537+MC04538 The Hollow King (Jessica Thorne) -> Crown-outlaw romantasy
Complete duology (Mageborn, Nightborn; Bookouture 2020, Hachette reissue 2025). Whole-fiction basis: mageborn collared/bound to the crown of Larelwynn; Grace Marchant = orphan soldier with hidden suppressed magic; beloved Prince Bastien = heir and the crown's own mageborn enforcer (Lord of Thorns). One crown, not two rival houses -> crown-outlaw (6->7), not royal-enemies; not crown-slave (no slavery bondage). Covers: per-volume verified Hachette jackets served locally (cover-mageborn.jpg, cover-nightborn.jpg).

## 2026-10-31 - MC04539+MC04540 Nevermoor (Jessica Townsend) -> Grey Mages
4 published vols (Nevermoor 2017, Wundersmith 2018, Hollowpox 2020, Silverborn 2025; Hachette). Morrigan Crow learns the Wundersmith's craft (wild Wunder, undefined art) in the invented-world Wundrous Society -> mage-hero > grey-mages (8->9), same slot as Earthsea. Not magic-school (real-earth branch; Nevermoor is a wholly invented world). Per-volume AU Hachette covers served locally.

## 2026-10-31 - MC04541+MC04543+MC04546 Consortium Rebellion (Jessie Mihalik) -> Space romance (9->10 FREEZE FLAGGED)
Complete trilogy (Polaris Rising, Aurora Blazing 2019, Chaos Reigning 2020; Harper Voyager). One self-contained von Hasenberg sister romance per volume against the High Houses' alcubium war; romance is the spine in every volume = space-romance def exactly. Leaf hit 10 with this card; freeze-at-10 flagged to parent before the next card (Starlight's Shadow, MC04542+44+45, same leaf, is held pending ruling). Covers: per-volume author-site published jackets served locally.

## 2026-10-31 - CORRECTION 1: Saga of the Skolian Empire (Catherine Asaro) -> Galactic courts (space-romance 10->9)
Ordered by main (21:20:40, split-serve #2 rejection): root gates win - a fiction failing the parent leaf's gate gets MOVED under single-fiction autonomy (phonemsg-01M66AQB0JEGYRYN8Q7XTWHVDX), not accommodated by split design. Whole-fiction evidence: eligible corpus = 8 published vols (Ruby Dice 2008, Diamond Star 2009, Carnelians 2011, Undercity 2014, Bronze Skies 2017, Gold Dust 2023, Vanished Seas 2024, Jigsaw Assassin 2025) - Skolian imperial dynastic politics plus the Bhaajan undercity noir mysteries; romance is not the spine in every volume (Undercity/Gold Dust/Vanished Seas/Jigsaw Assassin are Major Bhaajan noir procedurals). Fails the space-romance whole-fiction gate -> moved to galactic-courts (7->8), where dynastic court politics is the spine. Card + yaml moved; canonical_genre updated; placement_history records the move.

## 2026-10-31 - CORRECTION 2: The Rule of Luck (Catherine Cerveny) corpus fix (space-romance stays 9)
Card claimed "two novels" with wrong years. Grounded bibliography: the Felicia Sevigny series is a TRILOGY - The Rule of Luck (Jan 2016), The Chaos of Luck (Dec 2016), The Game of Luck (Sep/Oct 2018, Orbit/Redhook, ISBN 9780316441667; FictionDB + hachette.co.uk + Locus Oct 2018 new-books). Added The Game of Luck with visually verified jacket served locally (cover-the-game-of-luck.jpg); years fixed to 2016/2016/2018; first_published 2016. Also resolved during split grounding: Imperial Broadcasts eligible corpus = Love Galaxy only (Nebula Rising is forthcoming Apr 2027 per PRH - announced is not published).

## 2026-10-31 - SKOLIAN COMPLETE-CORPUS VERIFICATION + STAGED MOVE (pending Gustav's split ruling)
Complete published shared-universe bibliography verified (FictionDB series page, Wikipedia bibliography, baen.com, simonandschuster, catherineasaro.net series page): 20 novels in 3 publisher series - mainline Saga of the Skolian Empire 14 (Primary Inversion 1995 ... Carnelians 2011; Lightning Strike I/II aka Earthborn/Starborn = expanded re-edition of Catch the Lightning, same story, not separate volumes); Major Bhaajan Mysteries 4 (Undercity 2014, The Bronze Skies 2017, The Vanished Seas 2020, The Jigsaw Assassin 2022); Dust Knights 2 (The Down Deep Jul 2024, Gold Dust Oct 2025 - Gold Dust was misdated 2020 and misgrouped as Bhaajan on the old card). Novellas excluded (City of Cries absorbed into Undercity; Children of the Dust; Pyre of New Day). All 20 jackets downloaded and visually verified in two contact-sheet passes (author/branding confirmed per volume).
Existing-tree walk for the 20-volume fiction (rule 11j kept, one fiction - Gustav's Oct 30 ruling reaffirmed by main 21:38): honest leaf = future-history-in-space (leaf's established reading: Foundation, Alliance-Union, CoDominium, Humanx - multi-series universes as one future-history fiction). galactic-courts FAILS the 6 Undercity vols (throne is client, not arena); galactic-houses fails its throne clause; soap/adventure/military/colonies fail per-volume. No seed needed - but future-history is at 9, so Skolian's arrival triggers a split.
SERVED to main 21:41 (for Gustav "Approve split?"): Future history in space -> umbrella (0 cards) with Chronicle future history (5: Foundation, Alliance-Union, CoDominium, Island Worlds, Humanx Commonwealth - weakest Humanx) / Saga future history (5: Poseidon's Children, Skolian, Terran Republic, Theirs Not to Reason Why, Slow Gods - weakest Skolian/Theirs). Axis: what carries the course - the eras or one continuing line. Rejected: foresight axis 3/7, time-depth blurry, polity/diaspora 7/3. Names proposed, Gustav coins.
STAGED, uncommitted edits: none in repo (index.html/yamls untouched); covers + texts prepared, execute on his word: move saga card (rewritten, 20 vols, year 1995, Primary Inversion cover) to the approved child; galactic-courts back to 7. Skolian card provisionally live in galactic-courts with the old 8-vol list (both other touched leaves are failed gates; no better provisional).
Queue mapping when executed: MC01474/75/80 saga; MC01478/79/81/82 Bhaajan; MC01476 Gold Dust (queue year wrong: 2020, actual 2025) + The Down Deep surfaced.
Split prep (space-romance, preparation only until Gustav rules): Starlight's Shadow = Mihalik trilogy (Hunt the Stars/Eclipse the Moon/Capture the Sun 2022-23, human x Valovian couple per volume - fits the gate, is the tenth card). The Kindred = standalone (ISFDB: Dow's other novels are separate universes). Alien Affairs: Kiera Smith (GEP Bureau agent) x Thor (Buri leader) on Orpheus Two vs Dynatec - human x alien, institution-agent on an outside world.

## 2026-11-02 09:01 CET — Space romance five-way split (curator-approved)
- Approval: curator "Add dangerous love also then, split approved" (phonemsg-01M6DM13NE1BRN2W37SQPZWGG0, 2026-11-02 8:54 AM CET), after his "Forbidden space love" naming (phonemsg-01M6BSVBFV31P3D645DYQ5GW7F) and the Alien/AI/Forbidden/Arranged parallel-name set.
- Space romance -> umbrella (0 cards), children by what the love must cross: Alien space love (2: Alien Affairs, Starlight's Shadow), AI space love (2: Defy the Stars, The Stars Too Fondly), Forbidden space love (3: The Kindred, Consortium Rebellion, Starbound), Dangerous space love (1: The Rule of Luck), Arranged space love (2: Winter's Orbit, The Imperial Broadcasts).
- Starlight's Shadow (Mihalik trilogy: Hunt the Stars 2022, Eclipse the Moon 2022, Capture the Sun 2023) placed as the incoming tenth card in Alien space love; 3 local verified jackets (author site), Honor and Shadows novella excluded. Queue MC04542/44/45 -> in_tree.
- Portraits 862-866 wired (picks: alien A, ai B, forbidden A, dangerous B, arranged A; generated pairs, judged in-house per 2026-10-21 rule).
- Straddles disclosed: The Kindred (imposed bond + forbidden love -> Forbidden by whole-fiction obstacle); The Rule of Luck (illicit/dangerous rather than formally prohibited -> its own Dangerous leaf, which is why Gustav added it); The Imperial Broadcasts (sanctioned TV courtship -> Arranged).
- Fixed parity gap: consortium-rebellion was missing from space-romance genre.yaml works list (present in index.html); now correctly listed under forbidden-space-love.

## 2026-11-02 - MC04547 How to Lose a Goblin in Ten Days (Jessie Sylva) -> Cozy peeps fantasy (4->5)
Standalone debut (Orbit, Jan 20 2026; PW interview + Orbit New Voices 2026 list; author site lists no other Orbit title, no sequel/shared universe found). Halfling Pansy and goblin Ren each believe they inherited the same cottage; bargain to cohabit, first driven out forfeits - forced-proximity opposites-attract gentle romance in a comfort-read register (Orbit copy: "cozy fantasy romance, brimming with warmth"). Walk: Speculative fiction > Fantasy > Fantasy realms > Heart fantasy > Cozy fantasy > Cozy peeps fantasy. Not cozy-place (contested private home, not a house that takes people in); not cozy-craft (no trade holds the story); not romantasy (warm low-intensity register, no co-equal external stakes). Cover: PW CDN publisher jacket, visually verified (correct title/author, English, cottage tagline matches), served locally as cover-how-to-lose-a-goblin-in-ten-days.jpg. Queue MC04547 -> in_tree.

## 2026-11-02 - MC04548 Ninth Ward (Jewell Parker Rhodes) -> Ghost speakers (4->5)
Standalone MG (Little, Brown 2010; no sequel/shared universe). Lanesha, born with a caul, sees and sometimes communicates with spirits (Kirkus); Mama Ya-Ya has the sight; her gift is the defining speculative element of the Katrina survival story (PW: "a mix of magical and gritty realism"). Walk: supernatural-fantasy > Ghost stories (umbrella) > Ghost speakers - gate "living mediums whose defining gift is to speak with, through or for the dead". Not ghosts-and-grief (mother's ghost present, but the engine is her gift and the storm, not elegy); not lessons-beyond-the-grave (the relationship across death is not the engine). No age axis in this branch; MG sits next to adult tenants. Cover: Open Library id 7129231 (CSK Author Honor jacket, matches queue title's honor marker), visually verified, served locally as cover-ninth-ward.jpg; PW CDN image for the ISBN was a reader photo of a physical copy - rejected. Queue MC04548 -> in_tree.

## 2026-11-02 - MC04549 Paradise on Fire (Jewell Parker Rhodes) -> excluded_non_speculative
Realistic MG wildfire-survival novel (2021): Addy, whose parents died in a fire, at a wilderness camp when a wildfire strikes. "Haunted" is metaphorical; no speculative element (author site, SuperSummary, NYT review). New queue status value excluded_non_speculative introduced for non-speculative novels (disclosed to main).

## 2026-11-02 - MC04550-52 Noon Onyx (Jill Archer) -> already in tree (godforsaken-realms); vol 4 surfaced + added
Queue rows collide with the existing Noon Onyx card (placed 2026-10-14 after a setting review: world is Halja, a fictional country with circa-1900s tech, not Earth - hence Godforsaken realms, not urban/end-times). Placement stands; no new contradicting evidence. Bibliography completion: Pocket Full of Tinder (Black Willow 2016, ISFDB Type NOVEL, series #4) was missing from the card - added with verified jacket served locally (cover-pocket-full-of-tinder.jpg). Vol 3 jacket re-verified (PRH print ISBN 9780425257173; OL id 8092549 was an interior title page - rejected). Vols 1-2 jackets unchanged (OL 7492145/7751135, contact-sheet re-verified). Queue MC04550/51/52 -> in_tree.

## 2026-11-02 - MC04553-58 Dresden/Cinder Spires cluster reconciliation (no tree change)
Both universes already carded: The Dresden Files (mage-pi, 17 novels + Twelve Months 2026) and The Cinder Spires (steampunk-realms, 2 vols). MC04553 Brief Cases + MC04554 Side Jobs = short-fiction collections -> excluded_short_fiction (standing rule). MC04555 The Aeronaut's Windlass -> in_tree (Cinder Spires #1, on card). MC04556/57/58 Dresden Files Collection 1-6/13-15/7-12 = omnibus e-bundles of carded novels -> in_tree with omnibus note.

## 2026-11-02 - MC04559 The Olympian Affair + MC04560 Twelve Months -> in_tree (no tree change)
The Olympian Affair = Cinder Spires #2, already on the card (steampunk-realms); queue year 2024 vs card 2023 (Ace pub Nov 2023), card year stands. Twelve Months = Dresden Files #18 (Ace 2026-01-20), already on The Dresden Files card (mage-pi) as book 18 of 18.

## 2026-11-02 - MC04562-64 Janitors of the Post-Apocalypse (Jim C. Hines) -> Comic adventure SF (3->4)
Complete trilogy (Terminal Alliance Nov 2017 [queue said 2018], Terminal Uprising Feb 2019, Terminal Peace Aug 2022; DAW; author's bibliography lists exactly 3). Krakau aliens + feral-human plague Earth; Mops and her spaceship sanitation crew pulled through zombie-plague/conspiracy escapades. Comic-adventure gate exact (comedy runs on adventure; Hitchhiker's sibling); not satirical (joke not aimed at society), not rom-com. Covers: per-volume verified jackets served locally (OL 14524563/10891359 + PRH CDN 9780756412814), contact-sheet checked. Queue MC04562-64 -> in_tree.

## 2026-11-02 - MC04565 Unchosen Ones (Jim C. Hines) -> skipped_forthcoming
Forthcoming June 2027 (DAW) per the author's own bibliography page. No revisit wake per standing rule.

## 2026-11-02 ~09:42 CET - MC04561 Slayers of Old: refined seed serve prep
- Parent chain verified LIVE: Speculative fiction > Fantasy > Real earth fantasy > Contemporary fantasy > Folktale > Earthly comic fantasy (4 subgenres), https://gusoder.github.io/sff-taxonomy-browser/#earthly-comic-fantasy
- NAMES/SEEDS check: Parody realms (under Comic fantasy realms) is the established in-tree trope-parody concept but invented-world only; Earthly comic fantasy has no parody child. Age-based leaf = one-book singleton (illegal narrowness per SEEDS.md carve doctrine). Recommendation: seed "Parody fantasy" as 5th Earthly comic fantasy child.
- Engine evidence: psillustrated ("takes on the trope of the retired Chosen One in an obvious homage to Buffy"; "still has his wit"), booksbonesbuffy ("humor galore", "laugh-out-loud dialog", Buffy nods: Giles-like mentor Felipe, Council, destiny), WSJ via PRH ("Buffy the Vampire Slayer meets Thursday Murder Club and thoroughly enjoyable"). Uncertainty preserved: reviews also call it heart-felt urban fantasy; comedy-engine reading is the proposal's load-bearing judgment.
- Kaiju cover QA swap now LIVE-verified: card serves local cover-the-kaiju-preservation-society.jpg (Tor print jacket).

## 2026-11-02 11:53 CET - MC04561 Slayers of Old -> NEW SEED LEAF Parody fantasy (EXECUTED)
- Approval verified in observations: user +46705084862 "Approved" phonemsg-01M6DXPT3F6ZNZXEKTA0Y72HR6 (11:43:29 CET) on the agent's Approve seed? block phonemsg-01M6DPTVV1QYVD7142SHZ5QTDH. Firewall flag on the repo-carried approval claim resolved against this original.
- Commits a9239f7 (leaf + card + portrait + queue + NAMES/SEEDS) and 905d0f3 (root copies - site resolves covers/portraits root-relative; leaf-dir copies kept per convention). Both pushed; deploy landed ~11:52.
- Live-verified: #earthly-comic-fantasy shows 5 SUBGENRES with the Parody fantasy card + portrait (scrolled screenshot); #parody-fantasy shows 1 FICTION, Slayers of Old DAW jacket (PRH 9780756421274) loading, portrait background rendering, 0 broken images.
- Cover: DAW print jacket, tagline "Retire. Save the world. Again." Queue MC04561 -> in_tree (year corrected 2026->2025). verify_local: 816 nodes, 2637 cards / 6,090 books, refs consistent.
- Wobble fixed mid-flight: first commit put cover+portrait only in the leaf dir; site 404'd them (root-relative resolution) - caught on live verify, fixed in 905d0f3 before closeout.
- Portrait 867 generated per standing self-select rule (bookshop with three retired heroes + trope furniture), full-res at /downloads/parody-fantasy-portrait.png.

## 2026-11-02 11:57 CET - Parody fantasy portrait v2 (main review correction)
- Main rejected v1: read secondary-world (robed wizard, armor, medieval shop). Corrected via image EDIT of the original (commit e30a591): same composition/jokes, contemporary Earth unmistakable (denim/cardigan/flannel+cap, card reader+laptop, to-go coffee, street view with parked car). No oil-style prompt. Full-res /downloads/parody-fantasy-portrait-v2.png sent to main with live screenshot; live-verified 200/0 broken.

## 2026-11-02 12:03 CET - MC04566 excluded_non_novel + MC04567/68 Kirith Kirin -> Far-future planetary romance (7->8)
- MC04566 Weather Wizards Cloud Book: nonfiction (Algonquin 1989 cloud-forecasting humor guide) -> excluded_non_novel (3f4f8d9).
- MC04567+68 = one fiction (rule 11j): Senal/Irion trilogy per SFE (Kirith Kirin 2000 fantasy / The Ordinary 2004 science fantasy / The Last Green Tree 2006 fixup space opera). Kirith Kirin surfaced; card = 3 vols. Walk rejects: hard-science-fantasy (physics bar), ozymandian-tech (real magic not buried tech), classic/lost-colony PR (not Earth-visitor/forgotten-colony), theological space opera (vol 3 tonality only). Commit 0f2d4e7. Live-verified 8 FICTIONS + fiction page 3 BOOKS, 0 broken. Covers: OL 940824 + Macmillan 9780765305282/9780765305305, leaf dir + root copies.
- Mechanics learning: fiction-page deep links (#leaf/work) render the leaf grid after a plain reload; a card tap renders the fiction page. Verify fiction pages by tap.

## 2026-11-02 12:09 CET - MC04569-71 exclusions + MC04572 Realm Universe -> Galactic courts (8->9)
- MC04569 White Widow (Lehrer 1996 mainstream, Kirkus) -> excluded_non_speculative; MC04570/71 HotD light-up collectibles (Running Press Minis) -> excluded_non_novel (7c8aa2e).
- MC04572: ISFDB Realm Universe = Thirteenth Man 2012 + Treasons Cycle (A Choice of Treasons 2014, Of Treasons Born 2016); one fiction (11j), galactic-courts gate (throne + Ducal Council as arena). Covers OL 10469606/8535759/11103648. Commit 926bbf5. Live: 9 FICTIONS, fiction page 3 BOOKS, 0 broken.
- NOTE: galactic-courts at 9 incl. provisionally parked Skolian (staged future-history split still unruled). Next arrival there = split serve, no tenth card.

## 2026-11-02 12:10 CET - CORRECTION (main): Skolian galactic-courts placement is COMPLETED, not staged
Main 12:10: the whole-universe dynastic-center ruling was executed in e1c89b1 (verified in git log: 20-novel bibliography, retained in Galactic courts by rule-39 center of gravity, sidebar disclosure) and delivered Oct 31 21:53 with 20 novels and six Undercity sidebars disclosed. No staged future-history ruling or permission to reopen it exists. The 2026-10-31 "STAGED MOVE (pending ruling)" entry and today's 12:09 "provisionally parked" note are STALE - superseded by e1c89b1. No move or sweep made; records reconciled here only. Galactic courts stands at 9; an incoming tenth card triggers a split proposal before placement, as usual.

## 2026-11-02 12:11 CET - MC04573-75 GROUNDING IN PROGRESS (no placement yet)
Queue rows: MC04573 Shadowkill (1991), MC04574 Shadowplay, MC04575 Shadowspeer = Shadith's Quest trilogy (DAW 1990-91). ISFDB: Shadith's Quest (pe 1517) is a SUB-SERIES of the Diadem Universe -> rule 11j interrogates the WHOLE Diadem Universe as one fiction: Diadem Saga 9 vols (Diadem from the Stars 1977 ... per Wikipedia, list cut at Ghosthunt 1983 + 1 more) + Shadith's Quest 3 + possibly other sub-series (check ISFDB Diadem Universe super-series page for full contents: Dancer/Skeen/Drinker of Souls may be separate universes). Engine per PRH: "a young woman and her companions must stop an opportunistic destroyer of worlds" - space opera adventure. Next run: pull full Diadem Universe contents, then walk (space-adventure vs galactic-* candidates), covers for all volumes, place once.

## 2026-11-02 15:11 CET - MC04573/74/75 The Diadem Universe -> Space hunt (8->9)
- Whole-fiction walk (rule 11j): ISFDB pe 1517 (Shadith's Quest = sub-series of Diadem Universe) + SFE Jo Clayton entry confirm ONE 15-novel sequence: Diadem Saga 9 (1977-86) + Shadith's Quest 3 (1990-91) + Shadowsong 3 (1995-96). Separate universes (Skeen, Dancers, Drinker of Souls, Moongather, Wild Magic) excluded.
- Walk: space-hunt gate exact ("following the trail... clues, maps and the next lead drive the story"): SFE calls the sequence "Space Operas of extended quests"; Aleytys hunted for the diadem then a Hunter herself (Star Hunters/Nowhere Hunt/Ghosthunt); Shadith's Quest hunts Seyirshi, destroyer of worlds (PRH series page); Shadowsong runs the trail out. Rejected: space-adventure parent-line letter (new-space-opera def = 1980s+ revival; but tenant practice - Nightmare Blue 1975, In Fury Born 1992 - already absorbs 1970s-90s adventure), pulp-space-chase (pulp-era tenants 1956/1966), future-history-in-space (episodic quests, not a civilization chronicle; multi-series reading never ratified), psi leaves (contemporary-set / future-of-earth psi-science, not the engine). Wobbles disclosed in rationale: dash-flavored early volumes; era vs new-space-opera umbrella letter.
- Covers: 15 distinct English DAW jackets; rejected 4 interior title-page scans (OL 4734746/9598304/4749164/4749122), German Moewig Nowhere Hunt (14654465), PRH placeholder 9780886773854, damaged IA Shadowplay scan -> clean PRH DAW ebook cover 9780756417758. Local cover-*.jpg in leaf dir + root. Card cover = book 1.
- Queue: MC04573/74/75 -> in_tree; 12 surfaced volumes (surfaced3-surfaced14) recorded. verify_local: 816 nodes, 2640 cards / 6,111 books, refs consistent.

## 2026-11-02 15:17 CET - CORRECTION (main review): Diadem Universe moved space-hunt -> Pulp space chase (3->4)
- Main 15:15 rejected the space-hunt placement: New space opera ancestor gate ("The self-aware revival of space opera from the 1980s on - Banks and his heirs", accepted def) excludes a 1977-96 DAW series; existing tenants (Nightmare Blue 1975, In Fury Born 1992) cannot authorize an ancestor-gate exemption. Root/ancestor boundaries beat lower fit.
- Re-walk with exact ancestor wording: space-opera = "Umbrella for space opera, the large-scale interstellar adventure tradition, divided into Classic space opera and New space opera." classic-space-opera = "the classic space-opera tradition, partitioned by pulp mode and enduring evergreen status." pulp-space-opera = "space opera in the pulp tradition, partitioned into its original wave and deliberate modern throwbacks." None of the classic/pulp ancestor defs carries era language; the only dated gate is New space opera ("1980s on"), which Diadem fails. Mode evidence: SFE compares Clayton's venues to Leigh Brackett - the pulp lineage. Not retro (21st-c deliberate throwback), not evergreen (dated). Golden-age tenant practice spans 1950-1992 (Space Beagle 1950, Heechee Saga 1977, Starliner 1992).
- Leaf: pulp-space-chase gate exact ("pursuit, hunter or hunted: revenge, flight or a race against a doomsday weapon drives the run"). Odyssey boundary test passed (person's journey remains); chase over voyage (pursuit, not journey out, is the engine). Move under single-fiction autonomy + main's correction directive; no gate changed, no tenant sweep.
- Card, 15 covers (leaf dir), queue notes, yaml rationale + placement_history updated. verify_local: 816 nodes, 2640 cards / 6,111 books.

## 2026-11-02 15:24 CET - Diadem placement UNRESOLVED -> boundary decision served to Gustav via main
- Main 15:21: 'original wave' IS era language; recover the user's original Classic/Pulp/Golden age/Retro boundary ruling; no tenant-exception reasoning, no unilateral fit, no intake/structure changes while unresolved.
- RECOVERED ORIGINALS: (1) era-naming family (decision doc 16b): "Pulp = when it was made, Classic or Evergreen = the canon that never stops selling, Retro = modern throwbacks, Revival = the old chassis in new craft", applied to Classic space opera 2026-09-17. (2) Sept 13-14 boundary placements: Stars My Destination 1956/Double Star 1957/Karres 1966/Nova 1968 ("1968 New Wave, so classic not new", phonemsg-01M2EXHXXMC8BZG9B9RF13Q65E)/Shikasta 1979 -> Classic; Startide Rising 1983 (phonemsg-01M2F1644FKY1TGTG62D9X6FCZ)/Fire Upon the Deep 1992 -> New. Classic/New line ~1980. (3) 28a: Retro "made for" the 2024 Principle of Moments (modern throwback). (4) Oct 30: Norstrilia refused Evergreen - "only Dune and Star Wars live up to this" (economic canon). (5) Current tenants confirm the era reading: pulp leaves hold 1950-1970 (Space Beagle 1950 ... Hour of the Horde 1970, Nova 1968 in Pulp space intrigue) with only Heechee 1977 + Starliner 1992 as outliers.
- GAP CONFIRMED: under the originals, Diadem Universe (1977-96, pre-revival DAW adventure, not pulp-era, not canon-evergreen, not a throwback, not the 1980s+ self-aware revival) has NO honest leaf in the Classic branch (Pulp era / Retro throwback / Evergreen canon is the whole partition) and fails the New space opera ancestor gate. Served to Gustav via main with recommendation (widen Golden age "original wave" to the classic adventure wave through ~1980, Diadem -> Pulp space chase beside Karres; alt: named era leaf for the pre-revival decades, his to coin).
- Card stays PROVISIONALLY in pulp-space-chase (unaccepted; least-wrong existing leaf, kin to Karres); 15-novel bibliography intact; no other changes. Intake PAUSED on his ruling.
- 15:25 main rejected option A (gate change to rescue a placement, conflicts with "Pulp = when it was made"). Served ONE seed proposal: "Paperback space opera" leaf under Classic space opera (siblings Pulp space opera / Evergreen space opera; parent URL verified live; no name collision in tree). Gate: classic adventure tradition of the paperback-original decades between the pulp wave and the 1980s+ revival, era as cultural axis (rule 62); Not-lines vs New/Retro/Evergreen. First member Diadem Universe (moves on approval; no other cards swept). Uncertainties disclosed: name is my pick (his to coin/replace), Heechee 1977 + Starliner 1992 are same-era tenants in pulp leaves (no sweep without his order), 80s-90s traditional adventure included by mode.

## 2026-11-02 19:46 CET - Diadem FINAL in Pulp space chase; Paperback seed withdrawn; intake resumed
- Main 19:45 (owning the overcaution): the approval wait was unnecessary - single-fiction placement is standing autonomy (phonemsg-01M66AQB0JEGYRYN8Q7XTWHVDX), and Gustav's actual 15:29 objection ("I don't feel people will understand what pulp is if we put in paperback. Did you not find any place in Pulp Space Opera for this?", phonemsg-01M6EAN04XPSKG3NTQ6W3CA0NE) rejects the Paperback distinction and points the fiction inside Pulp space opera. Paperback seed withdrawn; no gate/def changes; no invented grant.
- Rationale re-grounded on his calibration (no tenant-exemption argument; the 1977-96 run rides with the whole fiction under rule 11j + his 15:29 direction). placement_history final entry appended; index placement_note synced. Card stays in pulp-space-chase (now final, 4 fictions).

## 2026-11-02 19:55 CET - MC04576/77 Numinous World -> Long chronicle fantasy (3->4)
- ISFDB series 35464: Numinous World = Black Ships 2008 + Hand of Isis 2009 + Stealing Fire 2010 + Elza Versfelt sub-series (The General's Mistress 2012, The Emperor's Agent 2013, The Marshal's Lover 2018) + Ravens of Falkenau collection 2011 (EXCLUDED, short fiction). Rule 11j one fiction, 6 novels, 4 surfaced (surfaced15-18).
- Walk: long-chronicle-fantasy gate exact ("one person, family or place followed across several Period fantasy eras... the long span is the point and no single-era leaf is honest; magic-agnostic"): one recurring soul, Bronze Age/Aeneid -> Ptolemaic Egypt -> Alexander's successors -> Napoleonic Elza. Chronicle-family boundary from the accepted Industrial Not-line ("the substantial span begins before the industrial age") includes it (span begins c.1200 BC). Wobble disclosed in yaml: the leaf's own "from the Renaissance to the modern line" phrase vs Vampire Chronicles tenant (antiquity start) + sibling Not-line. Rejected: reincarnation-fiction (SF-rooted; this is fantasy - ISFDB tag historical fantasy, gods/oracles real), classical-antiquity-fantasy (3 of 6 vols only), mythic-retelling (book 1 only), secret-history (no hidden cabal).
- Covers: 6 distinct English jackets; Hand of Isis title-page-style scan rejected for the 2010 Orbit painted jacket; General's Mistress keeps the library-stamped Gallery Books scan (best available, disclosed). Card cover = Black Ships.
- verify_local: 816 nodes, 2641 cards / 6,117 books.
- 19:59 main live-pixel review: OL 8178947 (The General's Mistress) is an interior TITLE PAGE with library stamps, not a stamped jacket. Replaced with the verified Amazon front jacket (1451667213); yaml cover_curation corrected. Cover QA lesson: typographic publisher-imprint pages with a library address block are title pages, not jackets.
- 20:07 MC04578 The Whisperwood Legacy (Jo Schulte, standalone YA debut, Little, Brown Young Readers, 2025-05-27; queue's 2021 wrong) -> unholy-halls (7->8). Walk: invented-fairytales fit on surface but BARRED by fantasy-realms ancestor gate "Imaginary-world fantasy" (book is real-Earth contemporary NC); fairytale-transplant rejected (tales invented in-fiction, not inherited); folktale retired. contemporary-fantasy > dark-fantasy > horror-fantasy > unholy-ground-horror > unholy-halls: menace dwells and waits in the built place (Locus "abandoned theme park... best settings for monster stories"; Kirkus "stories have power - and can hold danger"). Friction disclosed: halls def says "a building"; park = built grounds+attractions, same family as hotels/schools. haunted-wilds/cursed-towns/folk-horror/torment rejected with reasons in work yaml. Cover: Amazon 031657872X real US jacket, verified. Commit next.
- 20:10 MC04579 A Burden Shared (Jo Walton): short story (author site, Tor.com 2017-04-19) -> excluded_short_fiction, standing rule, no title exception. No placement.
- 20:10 MID-WALK MC04580 Everybody's Perfect (Jo Walton, Tor 9781250314055, written 2025, pub date TBC - verify out vs forthcoming). Novel: Serenissima, imaginary shadow-Venice, crossroads of nine worlds; gentle city fantasy, multiple non-recurring POVs, people/connections/plague/power; comps Piranesi (in tree: portal-fantasy/eldritch-doors/uncanny-thresholds/visionary-thresholds) + Swordspoint (Riverside: gothic-realms/fantasy-of-manners/posh-fantasy). NEXT: check pub date (Tor page), walk gothic-realms/fantasy-of-manners gate (gothic tone vs "gentle"), far-shores-fantasy, heart-fantasy; pick honest leaf; Amazon cover 1250314054? (verify ISBN-10) then place/verify/report.
- 20:14 MC04580 Everybody's Perfect (Jo Walton, Tor 2026-06-30, 272pp standalone) -> mythlike-past (7->8). CORRECTION: first pass placed on the invented-mythology UMBRELLA in error (verify_local caught non-leaf card); moved to the correct leaf per the 2026-10-12 curator split axis - no on-page gods, invented myth is the world the human story walks through. Friction kept: mythlike-past wording says inherited PAST/backdrop; this myth is live/unfolding, but the governing axis is gods-on-page vs not (Spear Cuts Through Water precedent). Walk: fantasy-realms (invented world, story lives in it; not portal). Rejected: high/political/heroic/S&S/comic/fairytale, far-shores (ABOUT-NESS test, Venice Western), gothic-realms (no menace register; Pax Britannica manners gate fails - Venetian artisan cast), heart-fantasy (no bond spine). Engine: invented founding myth coming true in a belief-built city at a nine-world crossroads. Friction disclosed: epic-fantasy ancestor lists journeys/wars (absent) but also cosmic systems/invented gods (present); gentle tone, engine over tone. Cover Amazon 1250314054 real Tor jacket. Commit next.
- 20:20 MC04580 positive-fit reconciliation (main 20:19): PW review 2026-03-19 supplies the positive evidence - Serenissima "built on nothing but layers of magical mist and memories and dreams", "believed into being" by Venetians, waterways "maintained by shared belief", PW calls it the story's "inventive backdrop" with a "low-stakes plot... personal and affecting" across nine human POVs; the doge prophecy is a founding legend coming true with "the city itself" pulling people (fate via backdrop, not a god actor). Axis covered: no gods on the page; invented myth is the world the human story walks through. "Inherited past or backdrop" gloss covers the live-myth case via backdrop. Rationale rewritten in work yaml; ruling applied, no wording project, no approval wait.
- 20:21 MC04581 My Real Children (Jo Walton, Tor 2014, Tiptree co-winner) -> alternate-worlds (fabulation). SFE Walton entry grounds the engine: Parallel World topos, two versions of one life, neither replaces the other, meditative. Leaf's own wording fits exactly: literary fabulation destabilizing memory (dementia frame never settles which life is real) and history, no travel mechanism, no historical POD. Rejected: alternate-history (identifiable turning point), parallel-world-fiction/multiverse-mirror (travel/communication mechanism; mirror-on-our-history). Cover Amazon 0765332655 real Tor jacket.
- 20:26 MC04582/83/84 -> ONE fiction "Sulien's World" (rule 11j): The King's Peace (2000), The King's Name (2001), The Prize in the Game (2002 prequel) -> arthur-reimagined (6->7). Author's own series page grounds Earth-rootedness: "a fantasy alternate sixth century Europe... the alternate Britain", same geography, mythically connected to our world -> real-earth gate passes. SFE: "a reworking of Arthurian legends". Woman-warrior narrator reshaping the legend = arthur-reimagined's own wording; peer tenants gwenhwyfar/spear. Rejected warrior-hero (anchor is the inherited story, not the class engine), alt-history-fantasy, mythological-fantasy. Queue years 2007/2004 are reprints. Covers: 3 real Tor jackets via Amazon, contact-sheet verified.
- 20:30 MC04585 Thessaly (2017 omnibus): fiction ALREADY in tree as "The Just City" (greek-god-fantasy, curator-approved 2026-10-05, all 3 novels incl. Philosopher Kings + Necessity). Queue row -> already_in_tree (duplicate). No placement. Note: card's books 2-3 use remote OL cover URLs (accepted 2026-09-22 audit) - left as-is.
- 20:31 MC04586 Tooth and Claw (Jo Walton, Tor 2003, WFA winner) -> courtship-fantasy (5->6). SFE's own classing is the branch name: "Satirical Fantasy of Manners", Trollope dragon world. Gothic-realms gate passes via its explicit manners clause; leaf = the match is the plot (sisters' marriage prospects + inheritance lawsuit, draconic biology working through courtship). Cover Amazon 0765349094 real Tor jacket.
- 20:36 MC04587/88/89 "Cat" (Joan D. Vinge): TENTH-CARD CATCH. Walk landed on psionics (SF, psi as studiable science) but the leaf already holds 9 tenants (Demolished Man, Slan, Ubik, Lathe of Heaven, A Plague of Pythons, Drunkard's Walk, Gabriel's Body, Hauser's Memory, Life During Wartime) - Cat would be the tenth. live_place ran before I counted (my ls filtered out the works dir - process lesson: count works/ before every live_place). Placement REVERTED cleanly (work yaml, genre list, index card, covers; verify_local green 2646/6124). Split serve to main next; rows blocked_split_pending. Meanwhile MC04590+ runnable.

### 2026-11-02 20:44 CET - Psionics 11j consolidation + Cat as 9th
- Tenth-card scare resolved as a counting error: psionics held Hauser's Memory and Gabriel's Body as separate cards, but SFE/ISFDB confirm they are the Dr Patrick Cory series with Donovan's Brain (1942, in mad-science-gothic) - one fiction under rule 11j.
- Consolidated all three Cory books onto one Donovan's Brain series card in psionics (verified in-tree English jackets reused); removed the card from mad-science-gothic (6->5). Single-fiction consolidation autonomy; main confirmed 2026-11-02 20:42. No split, no gate change.
- MC04587-89 Cat (Psion 1982, Catspaw 1988, Dreamfall 1996) placed as psionics' 9th fiction. verify_local green (816 nodes, 2645 cards / 6,127 books).
- Split proposal withdrawn (evidence retained in /tmp/psionics-split.md).

### 2026-11-02 20:58 CET - MC04590-93 The Snow Queen -> Hidden lander romance (3->4)
- One fiction (11j): Snow Queen cycle - The Snow Queen 1980, World's End 1984, The Summer Queen 1991, Tangled Up in Blue 2000 (SFE Vinge); queue years reprints.
- Walk: atemporal SF -> science fantasy -> planetary romance -> lost-colony -> hidden lander: Hegemony strips/bans tech to keep Tiamat a primitive mer farm, Winter Queen suppresses succession = leaders repressing technological recovery. Darkover precedent: active contact OK. Rejected classic-PR (visitor-from-Earth shape; at 9), far-future PR (Earth current), abandoned/broken lander, rebel space opera. Wobble moderate (cyclical cut-off; Gundhalinu offworlder lead in book 4).
- Covers: 4 distinct English jackets localized (288125 Warner Snow Queen, 10121558 Bluejay first World's End, 7024106 Warner first Summer Queen, 183221 Tor Tangled); contact-sheet verified; fiction cover = book 1.

### 2026-11-02 21:06 CET - MC04594-95 The Resurgam Trilogy -> Zombie mystery fiction (1->2)
- One fiction (11j): Dust (Ace 2010), Frail (Ace 2011), Grave (Candlemark & Gleam 2014, surfaced third volume). SFE Turner + publisher page.
- Gate: zombification never explained (dead simply rise, not bite-spread; Reactor/Odd Things Considered). 'Virus'/'bacteria'/'artificial plague' evidence describes the later zombie-KILLING lab plague, not zombification. Raising Stony Mayhall precedent. Wobble mild.
- Covers: Ace print Dust (rejected Penguin audio ed), Ace Frail, Amazon Candlemark Grave (rejected OL library-sticker photo); localized.

### 2026-11-02 21:10 CET - MC04596-97 The Elysium Chronicles -> Planet ecology fiction (5->6)
- One fiction (11j): A Door into Ocean 1986, Daughter of Elysium 1993, The Children Star 1998, Brain Plague 2000 (SFE Slonczewski); two volumes surfaced.
- Walk: futurist -> hard SF (practicing biologist, rigorous biological extrapolation) -> planetary science -> planet ecology (Shora's ocean ecology and Prokaryon's microbial intelligence are the main characters). Rejected terraforming (refused, not enacted), planet expedition, genetic-engineering umbrella. Wobble mild.
- Covers: Orb Door, Avon Daughter (small but real jacket), Tor Children Star, Tor Brain Plague; rejected blank spine + two title-page images; localized.

### 2026-11-02 21:16 CET - MC04598-600 Dragonlord trilogy = already_in_tree
- dynastic-murders 'Dragonlord' card already carries The Last Dragonlord 1998, Dragon and Phoenix 1999, Bard's Oath 2012 (placed 2026-10-04, same queue). Rows MC04598/599/600 marked already_in_tree. ISFDB series 6025 confirms the 3-novel bibliography; short story Dragonlord's Justice (1995) excluded per shorts rule.

### 2026-11-02 21:18 CET - MC04601-03 Harris folklore novellas excluded
- A Pocketful of Crows (2017), Orfeia (2020) = two of Harris's three illustrated folklore novellas (author's own site + RCW agency call them novellas); Maiden, Mother, Crone (2023) = their omnibus collection + 3 shorts (ISFDB Type: COLLECTION). All excluded under the novella/collection rules.

### 2026-11-02 21:19 CET - MC04604-06,608 The Rune Books -> Norse fantasy (2->3)
- One fiction (11j): author's own site lists Runemarks 2007, Runelight 2011, The Gospel of Loki 2014, The Testament of Loki 2018 as the RUNE books.
- Walk: real-earth fantasy -> historical fantasy -> mythic retelling -> norse fantasy: Gospel retells the Eddic myths, Runemarks/Runelight reimagine the Nine Worlds post-Ragnarok, Testament continues the same Loki. Rejected modern-norse-myth (only Testament is modern-set; one fiction can't split). Wobble moderate.
- Covers: 4 English jackets (Doubleday Runemarks, Runelight, Gollancz Gospel/Testament); contact-sheet verified; localized.

### 2026-11-02 21:21 CET - MC04607 The Moonlight Market -> consolidated into Honeycomb fiction (Invented fairytales, 5 cards, now 2 books)
- Author site: 'very much part of my Honeycomb world... a snapshot of it exists in Honeycomb'; Silken Folk + Nine Worlds shared. Card retitled 'The Honeycomb World'; books Honeycomb 2021, The Moonlight Market 2024. Both covers localized + contact-sheet verified.

### 2026-11-02 21:27 CET - Honeycomb World card: ancestor reconciliation added (QA from main)
- placement_rationale now explicitly reconciles the fantasy-root setting split: fiction anchored in the invented Nine Worlds (Honeycomb wholly; Moonlight Market's plot is the Folk's exile/homecoming), fairytale-fantasy ancestor setting-agnostic for invented fairy tales, modern-invented-myth and portal-fantasy alternatives rejected. No gate changed.

### 2026-11-02 21:31 CET - MC04609-16 Jocelynn Drake block
- MC04609/10/11/13 placed as one fiction 'The Dark Days Series' (Nightwalker 2008, Dayhunter 2009, Dawnbreaker 2009, Pray for Dawn 2010, Wait for Dusk 2010, Burn the Night 2011; FictionDB + Fantastic Fiction bibliographies; Nightwalker and Wait for Dusk surfaced) -> oldfangs-fantasy (8->9). Mira = ancient nightwalker, secret Coven enforcer; leaf = inside-the-dynasties vampire world; tenants Night Huntress/Sabina Kane same shape. Rejected fangs-out/newfangs/occult-mystery/publicly-paranormal. Wobble low (naturi share plot).
- Covers: 6 English jackets contact-sheet verified; OL 8292916 (Burn the Night) was a title-page scan -> rejected, replaced with Amazon 0061851825 jacket; Nightwalker/Wait for Dusk/Pray for Dawn via Amazon ISBN-10 (OL had no/small covers). All localized.
- MC04612 Inner Demon, MC04614/15 Asylum Interviews, MC04616 The Dead the Damned and the Forgotten = excluded_novella (FictionDB/bookseries.org form records).

### 2026-11-02 21:39 CET - MC04617 Griffen McCandles -> Paranormal fantasy (6->7)
- One fiction (11j): Dragons Wild 2008 + Dragons Luck 2009 (Asprin solo), Dragons Deal 2010 (Asprin+Nye), Dragons Run 2013 (Nye). SFE Nye entry + jodynye.com bibliography + FictionDB.
- Walk: hidden dragon race in modern New Orleans -> supernatural-fantasy gate ('monsters walking the modern world') -> paranormal-fantasy (tenant shape: hidden supernatural communities; Dr. Greta Helsing etc). Rejected werewolf (wolf-specific), beasts-of-marvel (magic realism), fae-founders (Faerie-specific), occult-mystery. Wobble low-moderate: paranormal-fantasy def still candidate/empty; fit rests on ancestor gate + tenants.
- Covers: 4 English jackets; OL Dragons Luck was a title page -> Amazon 0441016804. Localized.

### 2026-11-02 21:41 CET - MC04618/19 Imperium placement REVERTED pre-push (tenth-card rule)
- comic-space-fiction was already at 9 works (bill-the-galactic-hero existed; my earlier tenant listing was truncated by head -8, so I misread the count as 8). live_place reported 10 after append; placement immediately reverted before any push (commit bef6e6a dropped via reset to 2ac4f7c).
- MC04618/19 marked pending_split: a full split proposal for comic-space-fiction is owed before The Imperium Series can be placed. LESSON: never count tenants from a head-truncated listing; always ls works/ or count live_place's pre-check.

### 2026-11-02 21:45 CET - Tenth-card resolution for comic-space-fiction (no split needed)
- Tenant fit check (main 21:42): The Sol Majestic fails the comic gate - PW/WaPo/LJ/WSJ center coming-of-age + station-community rescue, not comedy governing. MOVED to space-habitat-life (3->4) under single-fiction move autonomy; full source-grounded rationale on card. Comic-space-fiction 9->8.
- MC04618/19 The Imperium Series then placed as the 9th (View 2011 surfaced, Fortunes 2014, Rhythm 2015; SFE 'Military SF laced with Humour'; publisher 'P.G. Wodehouse meets space opera'; leaf def explicitly includes comic military adventures). No structural change; no split proposal required.
- OPEN: Fault Tolerance card (comic-space-fiction) represents only book 3 of Valdes's Chilling Effect series and has an empty books list - 11j completeness fix owed (fiction = Chilling Effect 2019, Prime Deceptions 2020, Fault Tolerance 2022).

### 2026-11-02 21:47 CET - Fault Tolerance 11j completeness fix
- Card expanded from book 3 only (empty books list) to the whole Chilling Effect series: Chilling Effect 2019, Prime Deceptions 2020, Fault Tolerance 2022 (author site lists exactly 3). Retitled 'The Chilling Effect Series'; leaf unchanged (comic-space-fiction, stays 9). 3 English jackets contact-sheet verified, localized.

### 2026-11-02 21:51 CET - tsv bookkeeping fix
- MC04612/14/15/16 novella exclusions had not landed (regex skipped them in the Drake commit); now written. MC04620 Dragons Run = already_in_tree (on the Griffen card).

### 2026-11-02 21:51 CET - MC04623, MC04625-32 already_in_tree/excluded
- MC04623 View from the Imperium = book 1 on the placed Imperium card. MC04625/29/30 Best Served Cold, Red Country (+Booktrack edition) on The First Law card; MC04632 Age of Madness omnibus same; MC04626-28 Shattered Sea on its card (dynastic-wars); MC04631 Sharp Ends = excluded_collection.

## 2026-11-02 Dreamland block (MC04621/04622/04624)
One fiction (11j): "Dreamland" — Waking in Dreamland (Baen May 1998), School of Light (Jun 1999), The Grand Tour (Aug 2000); series membership per jodynye.com/bibliography ("Dreamland I/II/III"), FictionDB series 25604, Goodreads series 61700. Queue years 2000/2012 = reprints. Premise: visitors from the Waking World cross into the shared dream-world Dreamland (sustained by seven Sleepers) on quests (Baen copy; Kliatt compares to Xanth). Placed quest-thresholds 7->8 (active-adventure engine; adult Baen market keeps it out of child-friendly whimsical-doors; satire is texture, not a comic-realms governing mode; portal gate "crossings between Earth and another world" fits the Waking World -> Dreamland crossing). Covers: OL 409630/406704/406770 (Baen print jackets, contact-sheet QA, localized to repo root). Wobble: moderate — threshold is sleep rather than a physical door and tone is brighter than the uncanny umbrella framing, but the quest-thresholds def partitions by engine and is tone-agnostic.

## 2026-11-02 Marsbound block (MC04636/04639/04642) + Haldeman exclusions (MC04634/04638) + MC04633
MC04633 The Heroes: already_in_tree (on The First Law card, book 5 of 9, mud-and-blood-fantasy). MC04634 A Separate War and Other Stories = excluded_collection (ISFDB 146771). MC04638 Future Weapons of War = excluded_collection (Baen anthology ed. Haldeman & Greenberg). Marsbound trilogy one fiction (11j): Marsbound 2008 / Starbound 2010 / Earthbound 2011 (ISFDB series 26405; queue 2009/2012 reprints). Premise grounded via BookPage (Carmen Dula, Mars colony, rescued by another species already on Mars) and Starbound review (starship to Wolf 25 to meet the Others). Placed xenological-expeditions 7->8 (contact with the alien governs; voyage to meet the alien society central). Rejected near-future-first-contact (encounter on Mars/deep space, not Earth), surface-colony-life (colony is launch point). Covers OL 12232745/9473548/12232751 (Ace jackets; rejected OL 9434706 page-scan composite + OL 8003086 title page). Wobble: low-moderate — book 1's contact happens at the colony rather than on a dispatched mission, but the parent alien-expedition gate is "away from Earth" and the trilogy's spine is going out to meet the Others.

## 2026-11-02 Forever Peace (MC04637)
Standalone (SFE: shares only the title with The Forever War, separate universe - per main, omnibus components are bookkeeping, not universe evidence). 2043 Earth: Alliance vs Ngumi guerrilla war fought via cyberlinked remote soldierboys (Kirkus; SFE); resolution: prolonged cyberlinking humanizes soldiers, peace inevitable (SFE). Placed future-war 6->7 (war transformed by technology on near-future Earth). Rejected military-SF-under-spacefaring (Earthbound conflict, ancestor gate fails), techno-fiction (nanoforge/Jupiter threads serve the war story). Cover OL 283721 (1997 Ace jacket). Wobble: low - the posthuman ending is transformative but arrives through the war's own technology, which future-war's def absorbs ("War transformed by technology").

## 2026-11-02 Camouflage (MC04635) + Peace And War omnibus (MC04641)
MC04641 Peace And War = already_in_tree (omnibus: The Forever War + Forever Peace + Forever Free; components on the super-space-soldier and future-war cards). Camouflage standalone 2004 (Nebula): two immortal shapeshifting aliens concealed in human history (changeling sympathetic, chameleon predator) converge on a raised alien artifact (editorsreads synopsis; Wikipedia). Placed hidden-history-sf 5->6 (aliens/events concealed from the record through real history; Wild Seed is the same shelf-shape). Rejected hidden-alien-fiction (invasion ancestor gate fails - residents, not invaders), alien-tokens (artifact is convergence device, not the subject), alien-cosmic-history (not cosmic-scale). Cover OL 284158 (2004 Ace jacket). Wobble: low-moderate - the present-day artifact thread is thriller-shaped, but the fiction's spine is the concealed historical passage. NOTE: live verify owed next run (run limit).

## 2026-11-02 Old Twentieth (MC04640)
Standalone 2005. Immortal humans (Becker-Cendrek Process) on a one-way Beta Hydri expedition; ship VR "time machines" recreate the 20th century; immortals start dying in the tanks, VR system possibly acting independently (sfsite.com/03b/ot220.htm; sffworld.com; worldswithoutend). Placed techno-fiction-in-space 8->9 (VR/AI mystery + posthuman immortals + interstellar voyage; Glasshouse same VR-in-space shape). Rejected generation-starships (single-generation immortal crew), machine-minds (future-of-earth gate fails on starship story), time-travel fiction (VR recreation, not travel). Cover OL 284260 (2005 Ace jacket). Wobble: low-moderate - the AI reveal is the resolution rather than omnipresent, but the VR mystery is the plot engine per all three reviews.

## 2026-11-02 The Accidental Time Machine (MC04643)
Standalone 2007. Matt Fuller accidentally builds a forward-only time machine, exponential jumps through millennia (Strange Horizons review). Atemporal root ruling ("when in sci fi, anything time travel goes Atemporal", curator 2026-09-23) -> overclockian 4->5 (forward-only private device; initially placed into umbrella homebrew-time-machines, moved to the child leaf after verify_local caught the non-leaf card). Cover OL 11957012 (2007 Ace jacket). Wobble: none material.

## 2026-11-02 Work Done for Hire (MC04644)
Standalone 2014. Near-future (c.2030) surveillance thriller: blackmailed ex-sniper vs an employer who sees through the whole grid (Locus/Letson, The Tech). Technothriller -> infowar 8->9. Cover OL 14420921 (2014 Ace jacket, ISBN 9780425256619; rejected 8333459 title page). Wobble: none.

## 2026-11-02 Joe Hill collections excluded (MC04645/46/48)
20th Century Ghosts (short story collection, PS Publishing 2005 - joehill.nl + en.wikipedia), Full Throttle (13 stories, William Morrow 2019 - harpercollins.com), Strange Weather (four novellas, William Morrow 2017 - joehill.nl + headline.co.uk). All excluded_collection per novellas/shorts/collections rule. Novels Horns (MC04647) and The Fireman (MC04649) proceed to walks.

## 2026-11-02 Horns (MC04647)
Standalone 2010. Ig Perrish's devil horns make people confess/act on darkest impulses; God vs Satan through earthly pawns (NYT, Reactor, PopMatters reviews). Contemporary dark fantasy -> torment -> satanic-torment 3->4 (explicit Satan iconography/engine; tenants Rosemary's Baby, Master and Margarita). Rejected demonic-torment (generic demon; this is Satanic), horror-fantasy (no place menace), urban-fantasy. Cover OL 6303181 (2010 Morrow jacket; faint Amazon 'Copyrighted Material' watermark; rejected 10367822 movie tie-in, 9119615 audio). Wobble: none.

## 2026-11-02 The Fireman (MC04649)
Standalone 2016. Dragonscale spore pandemic, origin and transmission uncertain, no treatment (Locus/Langan; Guardian; NYT). Apocalyptic -> pandemic -> mystery-plague 7->8 (inexplicable affliction; tenants Blindness, The Violence). Rejected die-off (progressive burn, not one mass dying), zombie, post-pandemic-survival (in progress not aftermath). Cover OL 7885034 (2016 Gollancz UK jacket, English). Wobble: none.

## 2026-11-02 MC04650 Fortress at the End of Time - TENTH arrival, split proposal
Standalone novel (272p, Tordotcom 2017; PW + Tor page count). Walk: far-future, military listening station Citadel at edge of human space; closed oppressive posting society (corruption, suicide, no escape) is the engine (Verge, PW, Book Smugglers). Honest best fit = space-dystopias (closed, oppressive societies off Earth; tenants incl. Dred prison ship, Unkindness generation ship) but leaf is FULL at 9. Per standing rule: no tenth placement; split proposal served to main. Alternatives rejected: military-sf children (warfare-mode keyed, war long over), colony-life children (outpost not a colony), future-history-in-space, space-opera, techno-fiction-in-space (also FULL, and engine is social not tech).

## 2026-11-03 Space dystopias split EXECUTED + Fortress placed (MC04650)
Gustav Approved the split 2026-11-03 7:06 AM (phonemsg-01M6G08HR34RJ3N23TD9A0TZP6, verified user iMessage in-thread). Split-with-umbrella: space-dystopias -> shipboard-dystopias (Unkindness of Ghosts, Dred Chronicles + incoming) / planetary-dystopias (7), hull-vs-surface axis. New portraits 868/869 (2:3, no text, generated). 818 nodes. Fortress at the End of Time -> shipboard-dystopias 2->3 (272p Tordotcom 2017, cover OL isbn 9780765392800). Wobble: none.
- 2026-11-03 MC04651 Eat the Dark (Schreiber, Del Rey 2007) -> unholy-halls (8->9). One-night supernatural siege in a closing hospital; unholy predator dwells and waits in a building that is no one's home. Cover OL id 2405465 (real 2007 Del Rey jacket, red-lit corridor), QA'd.
- 2026-11-03 MC04652 No Doors, No Windows (Schreiber, Del Rey 2009) -> keys-to-the-haunting (4->5). Scott Mast rents empty Round House; dead bound to the place meet the newcomer tenant. Grounded: Kirkus, Flames Rising, Gumshoe, Shroud, PRH. Cover Google Books zoom3 isbn 9780345510136 (real 2009 Del Rey jacket), QA'd. OL id 8050993 rejected: title-page scan.
## 2026-11-03 Metaverse split EXECUTED + Username series placed (MC04653/54)
Gustav Approved 2026-11-03 8:53 AM (phonemsg-01M6G6BGVG8PQY0B71JGM5W99Z, verified user iMessage after the 7:26 split question). Split-with-umbrella: metaverse -> platform-metaverse (8: Snow Crash, Ready Player One, Omnitopia Dawn, Arena, Otaku, Dark Factory, The Extremes, Alma sequence) / private-metaverse (A Dream of Wessex + incoming), open vs closed access axis. New portraits 870/871 (2:3, no text, generated, QA'd). 820 nodes. Username series (Joe Sugg, 3 books: Evie 2015 OL 10295142, Regenerated 2016 Hachette CDN 918x1250, Uprising 2017 OL 12752510) -> private-metaverse 1->2. Uprising not a queue row: 11j completeness volume. Wobble: first live_place run wrote works yaml before KeyError on stale index.html; partial write cleaned and re-run.
- 2026-11-03 MC04655 The Dragon's Eye = already_in_tree (owning card the-dragons-eye @ breakaway-space-colonies, placed pre-queue with full walk).
- 2026-11-03 MC04656/57/58 Cry Pilot trilogy (Joel Dane, Ace 2019-2020) -> alien-war-grunts (7->8). Javelin squad ground war vs unknown biomech horrors from the terrafixing; criminal-pool cry pilots, squad found-family (author interview paulsemel.com; reviews aislynndmerricksson, firedrake.org). Not marine-corps (corporate military, no Corps tradition), not super-space-soldier (he isn't remade), not mercs. Covers OL 10209005/13493127/14339113 (real Ace jackets), QA'd.
- 2026-11-03 CORRECTION: Cry Pilot trilogy moved alien-war-grunts -> future-war (7->8) after main's Spacefaring ancestor challenge: books 1-2 Earthbound, war originates on Earth; 'Earthbound conflict remains the core' (future-war def). Corporate military (not state) - my earlier counter mis-stated it; the unit is Earth's standing corporate army, not a contract regiment (space-mercs def).
- 2026-11-03: MC04659/60/61 Metzada Mercenary Corps series (Joel Rosenberg; Ties of Blood and Silver completeness vol) -> space-mercs (6->7). Gate: hired regiment, contract and pay drive the story; NFG jacket "killing was their business". ISFDB series 4301 + Wikipedia. Covers: 3x OL + Emile via archive.org scan (1986 Roc). MC04660 title_collision flag wrong (Rosenberg's Hero is Metzada #4).
- 2026-11-03: NEW LEAF alt-swashbuckler-fantasy seeded under alternate-history-fantasy (7th child) on Gustav's Approved (phonemsg-01M6G8P2AJFSSJ6F43W4ETYS1G, 9:33); portrait 872. MC04662/63 Mordred's Heirs duology (Paladins 2004, Paladins II: Knight Moves 2006) -> alt-swashbuckler-fantasy (1). Alt flintlock split proposal withdrawn (incoming failed the powder gate; powder held binding per main).
- 2026-11-03: MC04664 The Dabare Snake Launcher (Joelle Presby, Baen 2022) -> orbital-mechanics (6->7). Space elevator build = orbital engineering w/ real physics (nanofiber tether, anchor rock, debris clearing); TMiaHM precedent for politics-heavy plot. Cover: S&S CDN 2023 tp (same Baen jacket), hi-res. Wobble: social-over-technical emphasis + ambiguous Mami-Wata thread, disclosed.

## 2026-11-03 MC04665 Forged in Fire (John A. Pitts, Tor 2012) — placed (11j completeness)
- Sarah Beauhall series card already at attic-talismans with books 1-2 (MC03996/97). ISFDB series 29561 = 5 novels; added Forged in Fire (2012), Night Terrors (2016, Wordfire), Rainbow Brigade (2020). Card now 5 books; tree book count 6,187 → 6,190.
- Covers QA'd: OL 14605095 (Forged, proper Tor jacket; rejected OL 8105751 title-page scan), OL 8666866 (Night Terrors), OL 11428114 (Rainbow Brigade); localized as cover-forged-in-fire.jpg / cover-night-terrors.jpg / cover-rainbow-brigade.jpg.
- Hand-edit (live_place asserts card must not exist): works yaml books+intake+history, index.html node books array. NOTE: json round-trip regex ate inline JS tail once; restored tail from git HEAD; verify_local green. Commit 7af3ac7.

## 2026-11-03 MC04666 Candle + MC04669 Kaleidoscope Century + MC04674 The Sky So Big and Black (John Barnes)
- All three rows already owned by The Century Next Door series card at rewired-minds (intake line listed all three ids; ISFDB series 714 confirms 4 novels). Queue years are reprints (Candle 2000, KC 1995, SSB&B 2002 first pubs).
- 11j completeness gap found: card was missing book 1, Orbital Resonance (1991). Added to works yaml + index.html node (cover OL 603493, Tor 1992 pb; rejected OL 9793086 photo-of-book and PRH placeholder); first_published 1995 -> 1991. Tree books 6,190 -> 6,191. Leaf stays at 9 cards (existing card, no new placement).
- index.html edit done line-based (prefix + json + preserved tail) after the earlier regex trap; verify_local green.

## 2026-11-03 MC04667 Daybreak Zero + MC04668 Directive 51 + MC04672 The Last President — already_in_tree
- All three owned by the Daybreak trilogy card at chemical-catastrophe; all three ISFDB series-28030 volumes present, no completeness gap. Tsv-only change, no tree change.
- Cursor: MC04670 Mother of Storms (own card at rain-drowned-worlds; verify) and MC04671 The Armies of Memory (Thousand Cultures card at copied-minds lists only Merchants of Souls + Armies of Memory — check ISFDB whether A Million Open Doors / Earth Made of Glass are missing = likely 11j completeness fix).

## 2026-11-03 MC04670 Mother of Storms — already_in_tree
- Standalone (1994), own card at rain-drowned-worlds, intake id MC04670 already on the card; no gap. Tsv-only change.

## 2026-11-03 MC04671 The Armies of Memory — placed (11j completeness)
- Thousand Cultures card at copied-minds had only books 3-4. ISFDB series 750 = 4 novels; added A Million Open Doors (1992, OL 603277) and Earth Made of Glass (1998, OL 182486), first_published 2001 -> 1992. Series shorts (Canso de Fis de Jovent 1991, The Little White Nerves Went Last 2006) excluded per no-shorts rule. Leaf stays 9 cards. Tree books 6,191 -> 6,193. verify_local green.

## 2026-11-03 MC04673 The Merchants of Souls — already_in_tree
- Owned by the Thousand Cultures card at copied-minds (book 3; intake id MC04673 already on the card). Tsv-only change.

## 2026-11-03 MC04675 After America + MC04676 Angels of Vengeance — already_in_tree
- The Disappearance card at alt-present holds all 3 series books (Without Warning 2008/9, After America 2010, Angels of Vengeance 2012; PRH series page + FictionDB confirm 3-book series). No gap. Tsv-only change.

## 2026-11-03 Thousand Cultures moved: copied-minds -> post-scarcity-politics
- Trigger: main's whole-fiction challenge on the MC04671 completeness walk. Grounding: AMOD = springer-contact culture clash on Wilson/Nansen, no mind-copying (Kirkus, Wikipedia, Reactor, finfar.org); EMoG = Briand diplomacy/disaster, no mind-copying (ISFDB flap synopsis); psypyx copied-minds content confined to books 3-4 (TMoS Kirkus + christian-sauve + Prometheus reviews; TAoM per series arc). Future-of-earth ancestor fails for books 1-2 (no Earth at all).
- Whole-fiction governing mode: post-scarcity Council of Humanity intervenes in isolated cultures; moral authority + collective choice (reunion by force, psypyx vote, invasion unity) under material abundance. Tenant parallel: Banks's Culture. Wobble disclosed: social-manners register vs space-opera ancestor.
- copied-minds 9->8 cards, post-scarcity-politics 1->2. Cards 2,669 / books 6,193 unchanged. verify_local green.

## 2026-11-03 Birmingham sweep MC04677-87
- Dave vs. the Monsters (MC04677/79/81): already_in_tree, 3 novels complete at paranormal-aftermath; series shorts (A Protocol for Monsters, Soul Full of Guns) excluded.
- Axis of Time (MC04678/80/86 placed): 11j completeness - added Axis of Time Reloaded novels WW3.1 (2023, Amazon B0CJCJBP96), WW3.2 (2025, B0FQBMVP8K, Dragon finalist per ISFDB), WW3.3 (2026, B0GNLTSBLQ); same time-thrown Multinational Force, Timetribe gate holds. Covers = Amazon ebook jackets, localized. Card 3->6 books; tree 6,193 -> 6,196. Stalin's Hammer novellas + 2017 omnibus excluded (MC04682 excluded_novella).
- The Cruel Stars (MC04683/85 already_in_tree; MC04684 skipped_forthcoming): The Forever Dead publishes 2026-11-24 (PRH 9781984820587); no revisit wake per durable forthcoming restriction (main 2026-11-03); fact preserved on project state only.
- MC04687 Without Warning: already_in_tree (Disappearance card).

## 2026-11-03 MC04688 The Shockwave Rider (John Brunner, Harper & Row 1975) — placed, NEW
- cyberpunk-noir (1->2): alienated fugitive rewriting identities via the net, survival story against corrupt high-tech power; proto-cyberpunk ancestor text. Rejected cyberheist, revolutionary-cyberpunk (ending = coda), huxleyan-dystopia, algorithmic-surveillance-dystopias (present-day branch), remade-minds leaves. Cover: OL 211303 Del Rey print jacket (first edition only available at 250px; rejected OL 11254030 audiobook). Live run before push.

## RULE CORRECTION (main 2026-11-03 10:31): tenth-card rule
- 9 existing fictions in a leaf is NOT a split trigger and NOT a stop. If the honest fit is a 9-work leaf, PLACE the tenth card, THEN propose the required split (at ten) and pause intake for that decision. Do not invent a nine-fiction cap. (Supersedes the earlier "9 + incoming = stop" reading.)

## MC04689/90 banked research — Count to the Eschaton (John C. Wright), NOT YET PLACED
- Series (ISFDB ea.cgi/John_C._Wright + Goodreads series 104450): 6 novels, all published: 1 Count to a Trillion (2011), 2 The Hermetic Millennia (2012), 3 The Judge of Ages (2014), 4 The Architect of Aeons (2015), 5 The Vindication of Man (2016), 6 Count to Infinity (2017). No forthcoming volume.
- Tree status: grep clean — NOT in tree. Existing "the-eschaton-novels" card (techno-fiction-in-space) is Charles Stross Singularity Sky/Iron Sunrise — name collision, different fiction.
- Aboutness so far: Kirkus on bk1 — 23rd-c exhausted Earth, Texas duelist/math genius Menelaus Montrose; robot starship 50 ly out at an antimatter star reports a monument with symbols = gift of advanced knowledge. Kirkus on bk6 — billions of years of deep time, cosmic-scale structure. Goodreads: bk3 year 10,515 AD, Hyades Armada; bk5 innumerable ages. Mode: deep-time far-future future history with intelligence augmentation; verify per-volume.
- TODO next run: per-volume grounding (all 6), root-down walk; if fit is future-history-in-space (9 works) place the tenth per corrected rule, then split proposal + pause.
- Walk pre-assessment: future-history-in-space def "Works tracing a sustained future course of interstellar human civilization" — strong whole-fiction fit (2210 -> billions of years; interstellar to intergalactic human clades/civilizations). Leaf at 9 works; per main's corrected rule: place the tenth, then draft the required split proposal and pause intake. LibraryThing publisher copy calls bk5 "space opera" — check space-opera def before final walk.

## 2026-11-03 MC04689/90 Count to a Trillion / Count to Infinity (John C. Wright, Tor) — placed, NEW 6-book 11j card "Count to the Eschaton"
- future-history-in-space (9->10): def "sustained future course of interstellar human civilization" — Stapledonian deep-time chronicle, 2210 AD to billions of years hence, interstellar to intergalactic. Per-volume grounding: Kirkus bk1/bk6, Strange Horizons bk1, Locus/Di Filippo bk3, publisher copy bk5 (LibraryThing), GearsBlog series. Rejected space-opera umbrella (adventure-first; this is didactic future history) and techno-fiction-in-space (tech as furniture; Stross Eschaton card there = name collision only). TENTH CARD placed per main's corrected rule (10:31) — split proposal for future-history-in-space required next, intake pauses for that decision.
- Covers: 6 distinct verified English Tor print jackets localized (Amazon 0765329271 bk1, OL 11296918 bk2, Amazon 0765329298 bk3 clean (rejected OL 9614573 Davenport Public Library stickered scan), OL 8417259 bk4, OL 8534785 bk5, OL 12707307 bk6; rejected OL 8322750 bk1 title-page scan). Live run before push.

## 2026-11-03 SPLIT PROPOSAL SERVED: future-history-in-space (frozen at 10) — awaiting Gustav
- Axis: what the chronicle turns on — existential test vs outward growth. Children: "The long emergency" (6: Foundation, CoDominium, Theirs Not to Reason Why, Terran Republic, Slow Gods, Count to the Eschaton) / "The widening frontier" (4: Alliance-Union, Island Worlds, Poseidon's Children, Humanx Commonwealth). Hard cases overlap-tested in the proposal. Intake PAUSED (one open decision). On approval: umbrella keeps def, works: []; new leaves numbered after 872, defs as drafted, 2:3 no-text portraits; all 10 cards re-walked with placement_history citing ruling id; fix slow-gods missing books array (Slow Gods 2025, cover OL 15215660); verify_local, push, live verify both leaves with screenshots, report, resume intake at MC04691.

## 2026-11-03 Gate re-check (main ~10:52): TWO MOVES, split dissolved
- Theirs Not to Reason Why Universe: future-history-in-space -> star-stripes (4->5). Fails the future-history gate: subject is Ia's military career and precognitive war-plan (author site + PRH: "A Military Science Fiction Series"), not civilization's course. Star-stripes arc fit: enlistment -> commission -> Hellfire's captain; First Salik War prequels fold under 11j. Wobbles disclosed: Army start, ensemble prequels.
- The Terran Republic (Caine Riordan): future-history-in-space -> far-future-first-contact (8->9). Fails the gate: a ~2105-2125 crisis sequence on one protagonist, not a civilization chronicle. Contact/diplomacy frame governs (elitistbookreviews "a first contact story", bookseriesinorder series focus). Wobble: war-thriller texture mid-series.
- future-history-in-space now 8 — NOT frozen; split proposal WITHDRAWN as moot (no tenth card exists). Intake resumes after this closeout. Queue rows for both fictions still read 'new' in the tsv (pre-cursor; will mark already_in_tree when hit).

## 2026-11-03 RESTRICTION recorded (main 11:03): forthcoming books
- Durable project rule: forthcoming books are excluded (skipped_forthcoming) with NO automatic revisit wakes. The Forever Dead one-shot wake (wakeschedule-01M6GBH7C1YMB30J0VC6A6EE3V, set for 2026-11-25) DELETED per this restriction. The Forever Dead (Cruel Stars 3, Del Rey 9781984820587, pub 2026-11-24) fact stays HERE on project state only - no wake, no scheduled job. Add it to the starbridge Cruel Stars card only if the intake naturally resurfaces it after publication.

## 2026-11-03 Johnson CORRECTION (main 11:05 directive): separation undone, whole-fiction walk
- Recovered original user directive (Oct 30, phonemsg-01M66AQB0JEGYRYN8Q7XTWHVDX): "if it is a shared universe it is one fiction". No superseding later instruction found in project todo or observations. Two-card split REVERTED (git revert cb422c7) - separation was unauthorized; named-series precedent does not override the user directive.
- Full whole-fiction walk of the 8-book universe: military leaves fail (3 diplomatic prequels); first-contact leaves fail (5 war books); future-history-in-space honestly holds the whole - the civilization-level Salik/V'Dan encounter is the through-story from The Terrans to Damnation across one timeline; precedent tenants with mixed contact/war modes: CoDominium, Humanx Commonwealth, Alliance-Union. Wobble disclosed: each era's foreground is single-mode; civilization course judged at whole-fiction level.
- Card (8 books, id theirs-not-to-reason-why-universe) moved star-stripes -> future-history-in-space. Counts: star-stripes 4, future-history-in-space 9 (unfrozen; tenth allowed), far-future-first-contact back to 9 (artificial tenth withdrawn). 2,671 cards / 6,203 books.
- Intake: paused per main 11:05 until this correction is reported with live proof; resumes after closeout per single-fiction autonomy doctrine.

## 2026-11-03 Placed: Chronicles of Chaos -> modern-greek-myth (MC04691/93/98)
- Fiction: Chronicles of Chaos (John C. Wright) - Orphans of Chaos (2005, queue row listed 2007 reprint; first pub Nov 2005 per SFE + ISFDB hc 0-765-31131-3), Fugitives of Chaos (2006), Titans of Chaos (2007). All 3 Tor novels; Orphans = 2005 Nebula nominee (Wikipedia). One fiction (single trilogy), 3 books.
- Walk: SFE aboutness - five schoolchildren at a Welsh boarding school are gods of Greek/Titan blood imprisoned by the Olympian order; fully released each commands a unique alternate cosmos; war in heaven between ultimate Order and Chaos; mode "shifts between heroic fantasy and space opera" (sf-encyclopedia.com/entry/wright_john_c). Fit: modern-greek-myth gate ("powers and bloodlines of Greek myth remain active within ordinary present-day life"); umbrella's Not-Mythic-retelling line respected (original story, not a retold named myth). Wobble disclosed: final volume escalates to cosmic space-opera-vocabulary war; present-day Earth frame holds. Leaf 4->5.
- Covers: 3 distinct verified English Tor print jackets localized (Amazon P-pattern: 0765311313, 0765314967, 076531648X; Titans jacket confirms series name "The fantastic climax of The Chronicles of Chaos"). Visually reviewed all 3.
- 2,672 cards / 6,206 books. Cursor next: MC04692 Null-A Continuum, then MC04694-97 already_in_tree (Eschaton card).

## 2026-11-03 Null-A: singleton REVERTED (main 11:15); whole-fiction fold + deep seed proposal served
- Main 11:15: whole-shared-universe rule applies across authors; Null-A Continuum is a continuation of van Vogt's Null-A sequence - fold, don't close as singleton. Reverted 7e91675; MC04692 back to new.
- Whole fiction = the Null-A sequence, 4 novels, one Gosseyn story (Wikipedia The World of Null-A + SFE): The World of Null-A (serial 1945, book 1948), The Pawns of Null-A (1956), Null-A Three (1984), Null-A Continuum (Wright 2008).
- Rewalk vs era-bound gates: golden-age branch fails the 2008 volume; retro-space-opera fails the 1945-84 volumes; psionics fails honestly (psi is toolset, not governing mode; galactic power struggle is the engine); evergreen ("escaped its era, perpetually current") is a weak fit for famously of-its-era pulp; future-history fails (single-period adventure, not civilization course). NO existing leaf honestly holds the whole 4-novel fiction.
- Deep seed proposal served to main (11:20): seed under pulp-space-opera, one recommended name. INTAKE PAUSED (one open Gustav decision).

## 2026-11-03 EXECUTED Gustav's approval (phonemsg-01M6GH9KVDQT9W738983QDKK1E, 12:04): space-opera def + Red Rising move + split undo
- Space opera umbrella def widened: "the large-scale interplanetary or interstellar adventure tradition" (was "interstellar"; SFE Space Opera: "interplanetary or interstellar conflict"). No child defs touched.
- Red Rising -> insurgent-space-opera (6->7): whole-fiction engine = the Rising from inside the regime (enslaved caste, Sons of Ares cells, Darrow carved into a Gold). Red God excluded as forthcoming. planetary-dystopias 7->6.
- Conditional met and executed: with red-rising out, merged dystopias = 6+3 = 9 < 10 -> the 2026-11-03 morning Space dystopias split (shipboard/planetary, hull vs surface) is UNDONE: space-dystopias restored as a leaf with 9 works (a-time-of-changes, dead-souls, fortress-sol, lies-inc, the-last-contract-of-isako, the-thick-and-the-lean, an-unkindness-of-ghosts, the-dred-chronicles, the-fortress-at-the-end-of-time); child nodes removed; all 9 cards re-walked with placement_history citing the ruling. 819 nodes (-2).
- 2,672 cards / 6,206 books; verify_local green.

## 2026-11-03 Placed: The Null-A Sequence -> pulp-space-intrigue (MC04692; whole-universe fold per main 11:15/11:20 doctrine)
- One fiction across authors: van Vogt's World of Null-A (1948), Pawns of Null-A (1956; Players variant), Null-A Three (1984) + Wright's authorized Null-A Continuum (2008, in-style). Original-wave golden-age fiction; 2008 annex disclosed as wobble, not disqualifying (main: later authorized continuation does not disqualify the whole original-wave fiction by year alone). Leaf: pulp-space-intrigue (schemes/espionage/manhunts, not fleets; rival-power boundary test collapses -> Empire branch). Leaf 4->5.
- Covers: World of Null-A = 1948 S&S first-edition jacket (OL 6709058, worn edges, complete); Pawns = genuine English print jacket of the variant-titled edition 'The Players of Null-A' (OL 5543821, low-res 147x220, disclosed on card); Null-A Three = DAW 1985 pb jacket (OL 5543819); Continuum = Tor Sci Fi Essential jacket (Amazon 0765316293, re-verified). All visually reviewed.
- 2,673 cards / 6,210 books.

## 2026-11-03 Excluded: John Chu rows MC04699-04702 (all Tor.com short fiction, SFE-verified)
- Cost-Benefit Analysis (2014), Beyond the El (2019), Hold-Time Violations (2015), The Water That Falls on You from Nowhere (2013, Hugo Best Short Story 2014) - all stories per SFE Chu entry. excluded_short_fiction.
- SURFACED GAP: Hold-Time Violations was much-expanded into Chu's debut novel The Subtle Art of Folding Space (2026, SFE entry updated 2026-05-04). The novel is in NEITHER the tree NOR the candidates queue (harvest predates/omitted it). Not placed (not a queue row; no unasked sweep). Flagged to main for the list-harvesting layer.

## 2026-11-03 Placed: Einstein's Bridge (MC04703+MC04704, one fiction) -> near-future-first-contact
- SFE cramer_john: Einstein's Bridge (1997, Avon) = near-future hard-SF, messages from another dimension when a particle accelerator operates. Baen pages (baen.com/einstein-s-bridge.html, published 5/2/2023 reprint; baen.com/fermi-s-question.html, published 6/6/2023): Fermi's Question is the explicit sequel ("15 years since the events of Einstein's Bridge", same Griffin/Coulton characters, Iris Foundation, Hive war) -> ONE fiction, 2 books (1997 + 2023).
- Leaf now 8 works (a-half-built-garden, beyond-the-light-horizon, einsteins-bridge, exordia, solar-express, the-blue-beautiful-world, the-burn-zone, voyagers). NOTE: genre.yaml works list had been stale (listed only 4 of 7 pre-existing); live_place regenerated it from the works dir.
- Covers: Baen CDN product-page jackets (9781625799265/9781625799272-med_1.jpg), localized as cover-einsteins-bridge-1/2.jpg. Small (157x240) but publisher-served, distinct, alt-labeled per volume.
- verify_local green (819 nodes, 2674 cards / 6212 books).

## 2026-11-03 Excluded: MC04707 Otherwhens, Otherwheres (Dalmas) = collection
- SFE dalmas_john tags it [coll]: "Otherwhens, Otherwheres: Favorite Tales" (Silver Dragon Books 2002). Queue year 2007 likely reprint. excluded_collection.

## 2026-11-03 STRUCTURAL GAP: MC04706 Fanglith (Dalmas) - no fitting leaf, proposal drafted
- Fiction: Fanglith series = Fanglith (1985) + Return to Fanglith (1987), Baen (queue 2006 = reprint). Baen blurb (baen.com/fanglith.html): political refugees of a galactic tyranny stranded on "the galaxy's most barbaric planet", revealed as 11th-century Earth; kids + ship computer + telepathic wolf must save parents from Thought Police and medieval warriors. SFE: "the planet to which criminals are exiled turns out to be Earth".
- Texture = planetary romance (adventure on an exotic world, fantasy furniture) but the planetary-romance umbrella partitions "by how the hero stands to Earth" into 3 leaves, none fitting: classic = visitor FROM Earth to alien world (inverted here); lost-colony children = descendants of settlers (repression/renunciation/broken tech - none apply; locals are just medieval Earth natives); far-future = natives of a far future where Earth is gone/forgotten (galactic society here is contemporary with 11th-c Earth). hard-science-fantasy fails (FTL present). space-dash weak (chase element yes, engine is survival-adventure on the planet) and at 9 works (would freeze). No umbrella in the tree holds works (verified: 0 nodes have both children and works).
- Proposal drafted for Gustav (new 4th child under planetary-romance); served via main. Intake pauses when served.

## 2026-11-03 Placed: Fanglith (MC04706, one fiction, 2 books) -> space-dash [10TH WORK - LEAF FROZEN]
- Whole-fiction grounding: vol 1 Fanglith (Baen 1985-10-01 per baen.com product page) = refugee family fleeing the Empire of Human Worlds' Thought Police, stranded on the galaxy's most barbaric planet (revealed as 11th-century Earth), children save parents from pursuers (baen.com blurb). Vol 2 Return to Fanglith (Baen, Aug 1987) = imperial fleets reconquer colony planets; Larn and Deneen flee again and establish a rebel base (worldswithoutend.com synopsis). Constant engine across both = prey-side flight/hiding from imperial pursuit -> space-dash def verbatim ("a guarded family on the run, where flight, hiding and the next jump drive the story").
- Root-down walk rejected: planetary-romance cluster (umbrella partitions by hero-Earth relation, none fits; more decisive: whole-fiction engine is pursuit, not world-exploration; vol 2 is flight+rebellion); earthborn/xenanthropology (no observer-frame society study); timestranded (no time travel); hard-science-fantasy (FTL present per Baen chapter sample); rebel-space-opera (covers only vol 2's rebel base; vol 1 has no revolt). new-space-opera ancestor gate: 1985/87 = "from the 1980s on"; SFE documents Dalmas's ironic repurposing of space-opera venues (self-aware use); tenant precedent A Roil of Stars (Baen 1991, same register/profile) already under this ancestor.
- space-dash hits 10 -> FROZEN pending split proposal (intake pauses when served).
- Covers: vol 1 Baen CDN 0671559885-med.jpg (160x240); vol 2 OL covers.openlibrary.org/b/isbn/0671653431-L.jpg (305x500). Localized cover-fanglith-1/2.jpg. Vol 2 ISBN-10 0671653431 via AbeBooks.
- MC04707 excluded_collection committed separately (2f06019). verify_local green (819 nodes, 2675 cards / 6214 books).

## 2026-11-03 Completeness: Tracer added to Outer Earth card (book 1, 16 Jul 2015, Hachette-verified)
- Card previously held Zero-G + Impact only (queue ids MC08100/08101; Tracer never in queue). Jacket: Hachette CDN hbg-title-tracer-6.jpg (795x1250), localized cover-outer-earth-0.jpg. Card now 3 books, first_published 2015.
- PENDING DECISION (reported to main): Outer Earth fails space-dash whole-fiction gate (publisher-copy audit); proposed new leaf under space-colonies for the station/colony thriller mode. Awaiting Gustav ruling via main.

## 2026-11-03 SEED EXECUTED: Space station thrillers (space-station-thrillers) under Space colonies
- Gustav approved (phonemsg-01M6GJVGFYGSCTWGCMS05RZBA4, iMessage "Approved", verified in delegation context). Fourth child of space-colonies by story engine (case / power / daily life / threat).
- Def: fast-moving criminal or terrorist threat is the engine (conspiracies, blackmail, hostage crises, sabotage inside the settlement) vs Space mystery's case engine. Seed tenant: Outer Earth (3 books incl Tracer completeness add).
- space-dash back to 9 works; freeze dissolved; no split needed. verify_local green (820 nodes, 2675 cards / 6215 books).
- DISCLOSED: new leaf has no portrait webp (portrait pipeline outside intake scope); node image="" renders dark background. May want a portrait later.

## 2026-11-03 Portrait: 873-space-station-thrillers.webp shipped
- Two 1024x1536 variants generated (smart tier, 2:3): A = courier chased through crowded concourse (rejected: reads as space-dash chase cousin); B = hooded saboteur planting a blinking device on a reactor conduit, security sweeping from a catwalk, Earth through the viewport (PICKED: sabotage is the distinguishing act vs space-mystery's case-work and space-dash's chase). Content checklist passed: genre legible at a glance, no franchise silhouettes, no bows, gloved hands clean on the device, plausible station scale, no readable text. Root file 873-space-station-thrillers.webp; genre.yaml image+portrait set; index.html node image set. verify_local green.

## 2026-11-03 Router slug collision recorded (no fix now, per main)
- Two cards share the book/fiction slug wolf-in-shadow: Gemmell's Wolf in Shadow (1987), volume 1 inside fiction card stones-of-power (post-apocalyptic-fantasy), and Lambshead's standalone Wolf in Shadow (2013) at magic-counter-ops/works/wolf-in-shadow.yaml. Bare hash #magic-counter-ops/wolf-in-shadow resolves to the stones-of-power card; the magic-counter-ops card is reachable via the #magic-counter-ops leaf page (click book-wolf-in-shadow) and verified live. Any link sent to Gustav must be checked to resolve to the intended card.

## 2026-11-03 Queue anomaly recorded (unresolved intake state, do not process)
- intake-lists/merged-candidates-2026-10/candidates.tsv: 11,681 rows tree_status=new; 4,499 of them sit BEFORE the current cursor (file line 4747), spanning MC00001 (line 2) through MC04530 (line 4531). Statuses for those rows are unresolved, not evidence of absence from the tree. Cursor continues in file order (MC04751 at 4:20 PM).

## 2026-11-03 Widening executed: classic-time-agencies "through the early 1990s" -> "through the 1990s"
- Gustav Approved (phonemsg-01M6GZ55KP7K0ZFT54AHVC8J91, iMessage, verified against the phone channel). Admits Corrupting Dr. Nice (1997, classic institutional comedy sensibility). Thriller register and post-2010 revival unchanged. Commit 07ede1e.

## 2026-11-03 Placed: Dog Days (MC04752/53/54/55, one fiction, 4 books) -> mage-pi [10TH WORK - LEAF FROZEN]
- Whole-fiction grounding: fangfiction.blogspot.com series review + PRH series page. Mason = trained practitioner (mentor Eli), jazz guitarist, freelance enforcement for Victor (Bay Area chief magical enforcer), ifrit familiar Lou. Per-volume engines: v1 missing ifrits / power-hungry practitioner; v2 energy pool lets monsters in; v3 hunting the shape-shifters; v4 hired by a black practitioner to find another and retrieve stolen materials. Case-driven -> occult-mystery > occult-pi > mage-pi (own craft is the working tool). Rejected: occult-cop (no badge), occult-secret-service (community enforcer, not state), monster-pi (human), pi-meets-magic (trained).
- mage-pi hits 10 -> FROZEN pending split proposal (intake pauses when served).
- Covers: OL 2421401 / 7094333 (v1-2); PRH CDN images3/images1.penguinrandomhouse.com/cover/<isbn> (v3-4, 279x450). Rejected OL 8018890 + 10051864 (title pages, Burlingame library stamp). Localized cover-dog-days-1..4.jpg. ISBNs 9780441015535 / ...016563 / ...017980 / ...019649.

## 2026-11-04 SPLIT EXECUTED: Mage PI dissolved into six leaves under Occult PI
- Gustav "Approved" (phonemsg-01M6K1FBZPJ1AF6KPYB2EDXTA4, 11:25 AM, verified on phone channel) + Ballard move ("Ballad move also", phonemsg-01M6K1FRCP7JJ3GMGRME5WD3EA). Dissolve overrides split-with-umbrella default per his "I don't mean split in that way" (phonemsg-01M6H4GH0N5N6RQ2P0H025FT55). Names Evocation/Illusionist/Witchcraft/Shaman PI are his own.
- evocation-pi (the-dresden-files, case-files-of-justis-fearsson) / illusionist-pi (dog-days) / necromancer-pi (felix-castor, eric-carter, nightwise) / psychic-pi (stealing-the-elf-kings-roses, the-broken-hearts-agency) / witchcraft-pi (diana-tregarde-investigations) / shaman-pi (sacred-ground). mage-pi retired to taxonomy/_retired/2026-11-04-mage-pi; redirect mage-pi -> occult-pi in index.html; occult-pi now has 8 children.
- Portraits 874-879 wired (A-variants picked from A/B pairs after full-size review: no bows, no text, clean hands, genre legible).

## 2026-11-04 Placed: Growing Up Weightless (MC04756, 1 book) -> surface-colony-life [10TH WORK - LEAF FROZEN]
- Grounding: Kirkus (1993-10-15 release), reactormag.com reread, Tor/Forge excerpt, worldswithoutend. Settled independent Luna, coming-of-age engine (train trip, growing up, father's water symphony); council politics backdrop only. Philip K. Dick Award winner (Tor Essentials jacket). Cover: OL 12565335 (2022 Tor Essentials reprint jacket, genuine English print jacket; rejected OL 7994189 = Bantam title page). Localized cover-growing-up-weightless.jpg.
- surface-colony-life hits 10 -> FROZEN pending split proposal (intake pauses when served).
- MC04757 excluded_collection (Heat of Fusion and Other Stories, 2004).

## 2026-11-04 Split: Surface colony life (10) -> Prehabited world (4) / Fresh settlerworld (6), umbrella kept
- Gustav coined the names himself: "Prehabited world / Fresh settlerworld" (phonemsg-01M6K96VKMNGQWMXX7FYZKH4WS, 1:40:41 PM CET, verified on phone channel; iterations phonemsg-01M6K8FSE5AGVQYK7YWD1E5BPB, phonemsg-01M6K8NVZ8AEHFW6YGRRCS4HJE, phonemsg-01M6K8T1RGZ48X1V1RSFS22K5W). No Approve block needed - his own naming. Names used exactly as written (singular).
- prehabited-world: hella, remnant-population, planetfall, the-voices-of-heaven (natives can be people, fauna, biosphere or ruins - in def). fresh-settlerworld: desolation-road, the-outposter, destinys-road, the-homecoming-saga, mirabile, growing-up-weightless (def covers young and established lone colonies: Luna 4 generations, Destiny's Road generations old, terraformed Mars).
- Mirabile wording fixed: creatures are mutated Earth-brought life, not natives.
- Portraits 880 (prehabited-world) and 881 (fresh-settlerworld) wired. Umbrella link: https://gusoder.github.io/sff-taxonomy-browser/#surface-colony-life

## 2026-11-04 Placed The Dragon Waiting (MC04758) -> Alt Renaissance fantasy (3)
- 1983 standalone, John M. Ford. Openly alternate Renaissance Europe, magical/vampire machinery sustaining Byzantine expansion; not crusading Christendom, not a horror engine. Sources: Wikipedia, Reactor Jo Walton review, Locus Paul Di Filippo review (URLs in work yaml). English Gollancz Fantasy Masterworks reprint jacket, OL380130, inspected and localized. Next MC04759.

## 2026-11-04 Placed The Last Hot Time (MC04759) -> Big-city fae (9)
- Ford standalone, December 2000 (ISFDB); 2001 queue date is edition. MC04763 2025 reprint marked already_in_tree. Modern Chicago with gangster-era aesthetics, not actual historical setting (WELL author interview); returned Faerie society and exiled elves shape urban institutions. Borderworld wobble disclosed, no many-world/crossing itinerary established. English Tor jacket OL182420 inspected and localized. Sources in yaml. Next MC04760 The Scholars of Night. Big-city fae now on freeze-watch at 9.

## 2026-11-04 Placed The Scholars of Night MC04760 -> Infowar (10, FROZEN)
- 1988 standalone (2021 queue reprint); thin speculative scope admitted by current mundane Technothriller gate. Conflicting reviews surfaced, sources in yaml. English Tor jacket OL10375014 inspected; OL10891155 placeholder and OL12706141 library banner rejected. Infowar at ten, intake paused, split proposal being prepared immediately. process.md reconciled to place tenth then freeze, matching SPLITTING.md and verified September26 original on not delaying to an eleventh.


## 2026-11-04 Placed Web of Angels MC04761 -> Space techno fiction10, FROZEN
- Ford1980 standalone,2024 Tor reprint, Doctorow introduction not coauthor. Intergalactic Web manipulation and control govern; proto-cyberpunk is a substantial texture, but Modern-day ancestor fails. Full sibling walk and four sources in YAML. English publisher2024 paperback jacket inspected/localized324x500. Tenth placed, intake paused, split preparation now. NextMC04762 only after decision/live closeout.
- Planetfall seed declined: "Nah, no new lvl 3 seed just for this" phonemsg-01M6KDBRD4JPSB0RCST9HNZW0V. Retained Surface colony life9 with substantial Earth/ship psychological straddles explicit, no definition change.8e79d371 live QA complete.


## 2026-11-04 Audit The Spare Man -> Comic space fiction10, FROZEN
- Own-call single fiction move on actual author murder-comedy account plus independent reviews. Space techno9 unfreezes; Comic10 frozen. Space PI blocked by its settlement ancestor: all action aboard transient cruise liner. No definition changed. Bill whole-series completeness/time-travel issue uncovered during mandatory split audit, pending source-grounded resolution before serving a forced split.


## 2026-11-04 Bill whole-fiction completeness and explicit exception
The curator kept the entire seven-novel fiction in Comic space fiction as an explicit exception to the any-time-travel rule: "If it’s not until book six I think the time travel browsers will be annoyed by five books of his comic stuff" (phonemsg-01M6KEGWWB8QRRQ7H8MJ0GRZJC), then "keep" (phonemsg-01M6KEHW5PZSP7DCECBYK0HFBC, 2026-11-04 15:14 CET). Proposed Time door widening dropped; no definition changed.
- Expanded1 ->7 novels, six books added, no fiction count change. All7 English jackets inspected/localized. Comic space fiction remains10 FROZEN, next single decision is its actual-content split; noMC04762 before decision/live closeout.


## 2026-11-04 Comic space future rename
Curator phonemsg-01M6KQKEP17D9YX9PE91HR3JTJ supplied name. Label and positive definition updated, no membership or portrait change, Bill exception retained. Stable id comic-space-fiction preserved. Ten fictions frozen; split still unapproved, intake cursor MC04762 paused.


## 2026-11-05 Comic space future split executed
The curator approved the served 3/3/4 split with his own Space gang comedy name (phonemsg-01M6NGYC97EQD2FQA1HECN3N27, 2026-11-05 10:34:21 CET, original Approved read live in its naming exchange). Comic space future stays as umbrella with zero direct fictions.
- Cadet: Bill all7, Rats/Bats both, Wasp. Envoy: Condomnauts, Magnificent Wilf, whole Dilbia. Gang: Chilling Effect all3, Gods of Sagittarius, Spare Man, Imperium all3. All10 fictions and their21 volumes preserved. Bill explicit exception retained on its card, child definition and umbrella.
- Portraits886B/887B/888B selected after full-size A/B review, no bows/text, concealed human hands. Positive definitions and ten updated root-down walks. Local QA then live deployment QA required before resuming MC04762.


## 2026-11-05 Comic split live QA complete; intake resumed
Commit64cc8b38 deployed successfully. Umbrella and all3 leaves pixel-checked, all10 jackets visible in leaf captures, all card payloads preserved except placement notes. Parent closeout delivered10:41. No decision open.

## 2026-11-05 MC04762 duplicate; Starfinder MC04764 placed
MC04762 is Growing Up Weightless2022 reissue of existing MC04756, marked already_in_tree. MC04763 already marked duplicate. Starfinder2009 (queue2010 paperback) -> Steampunk realms5; one published Skylords novel, no invented trilogy completion. Full source-read root-down walk and quest/technology wobble in YAML. English PRH paperback jacket inspected and localized. NextMC04765 Bronze Knight whole-fiction audit.


## 2026-11-05 Bronze Knight whole4 placed -> Champion of Realm6
All4 novels (Eyes of God, Devil's Armor, Sword of Angels, Forever Knight) one fiction; shared world and continuation verified by publisher and detailed reviews of each volume. Continuing protector of Grimhold/Inhumans and war leadership beat exiled opening phase, personal grief, artifact quest and court politics; substantial wobble explicit in source-read walk. First novel2002 per contemporary Locus vs2001 copyright/date in ISFDB title preserved. Four English jackets inspected/localized; blank/placeholder OL3/4 rejected, paperbacks accepted. Next sequentialMC04768 Tyrants and Kings, not yet classified. Starfinder6a90afa4 live QA complete and delivered.


## 2026-11-05 Tyrants and Kings whole3 -> War of humanity7
Jackal1999/Grand Design2000/Saints2001, publisher series complete, contemporary Locus dates checked. Per-volume military/hero/political engine and author theme-shift evidence recorded; substantial political statecraft/Richius hero wobble not hidden. Whole-world ensemble war wins over the first-book-only warrior reading. Three English print jackets inspected/localized. Bronze Knight ba3eed6d live QA complete all4 covers, parent closeout delivered10:49. NextMC04772, MC04771 already on Bronze Knight.


## 2026-11-05 Tristopolis whole6 -> Hard science fantasy8
Primary BSFA author rigorous-physics/solar-system-divergence statement + UK publisher scientific rationale decide disputed root. Detailed per-volume engines, cop-to-PI transition, SF/Fantasy/New weird/alt-history alternatives and substantial unproved-physics caveat recorded. Six English jackets inspected/localized; Dark=Black Blood one novel, not two. Tyrants67b93d56 live QA done3 jackets, parent sent10:53. NextMC04775 A Trip to Venus.


## 2026-11-05 A Trip to Venus1897 -> Scientific adventure8
MC04775 queue2013 reprint, original1897. Root-down historical scientific marvel voyage wins over planetary romance and modern Hard SF. Original English decorated cloth front inspected/localized. NextMC04776 Books of the Shaper whole trilogy.


## 2026-11-05 Books of the Shaper whole3 -> War of immortals4
MC04776/77/78 actual2012/2013/2013. Deathless sorcerers and Old Breed world-war vs personal quest/mage-training/mythology alternatives recorded with substantial wobble. Complete self-contained trilogy verified against author; early io9 four-volume plan rejected. Three English Orbit covers inspected/localized. NextMC04779 Those Who Walk in Darkness.


## 2026-11-05 Soledad O Roark whole2 -> Orwellian statesmanship6
MC04779/80 originals2003/2006, contradictory FF2004 rejected. Near-future gate rules out Superhero under Modern-day; ideological law criminalizes powered people and legal/extralegal police killing binds both novels, substantial noir/superhero wobble explicit. Two English jackets inspected/localized. Shaper042407cf liveQA/parent delivered11:04; Venus also delivered. NextMC04781 A Deeper Blue, check scope/eligibility before deeper research.


## 2026-11-05 Paladin of Shadows whole6 -> Spytech7
MC04781 plus later same fiction rows reconciled MC04781,MC04787,MC04794,MC04802,MC04819,MC04823. Explicit Katya implants+invented super-smallpox primary samples settle SFF eligibility, all6 plots audited. All six Baen images lowres158-160x240 disclosed. NextMC04782 A Hymn Before Battle / Posleen universe. No structural proposal.


## 2026-11-05 active Posleen duplicate/edition reconciliation
MC04782/83 existing whole12 Legacy Aldenata in Warzone Earth, not new fiction. Removed erroneous13th-card2013 revised edition into first-book edition metadata, publisher verified. Same-fiction queue rows reconciled: MC04782,MC04783,MC04786,MC04793,MC04796,MC04797,MC04798,MC04809,MC04811,MC04814,MC04827,MC04829,MC04830. No reclassification/full corpus audit. Totals831/2710/6303. NextMC04784 Against the Tide / Council Wars, inspect existing card first.


## 2026-11-05 FREEZE Future war10 Council Wars whole4 restored/rewalked
ActiveMC04784 entire4 source-read, missing2003 first added, fiction start2003 fixed, all4 covers localized. Whole war across naval/ground/resource struggle beats first book knowledge village; significant final space raid caveat. Moved Lost knowledge keepers7->6 to Future war9->10. INTAKE PAUSED pending cluster audit and split proposal, no proposal served yet. Other9 need independent whole-fiction/root audit; preliminary evidence some may leave, don't force partition. Paladin+Posleen22d141da still deployment/liveQA awaited.

## Future war audit: Ninth City Burning9->Multiverse invasion7
Own Nov3 correction missed explicit interdimensional fronts. Root rewalk now supported by author+publisher+3 reviews. Future war10->9, no split proposal served; audit ongoing, no intake yet.

## Future war audit: Ander Rade whole2 to Cyberpunk noir3
Rogue2024 date fixed and Ghost Cell2025 restored, author confirms covert rather than geopolitical war; explicit2091 blocks Modern-day Spytech. Future war9->8. All English publisher covers localized. Intake still paused for Terminator scope audit.

## Frozen-leaf audit: Terminator whole17 to Time agency thrillers7
Allston2 were only tiny part, root missed psychic communication. Whole17 licensed novels including divergent continuations restored; whole institutional time-displacement assassin/protection thriller wins, Dreams mental mechanism and Salvation war-only substantial wobbles. Future war8->7, no split gate. Continue audit remaining7 before next intake.

## Future war frozen audit COMPLETE, corrected7, split unnecessary
Source-read remaining whole7 including Council, retained all with explicit whole-fiction wobbles: War Girls afterwar/space2, Cry Pilot space3, Forever Peace apocalypse/peace conspiracy. Three false tenants removed: Ninth City Burning multiverse, Ander Rade noir, Terminator time travel. No structural decision served or open. Resume ordered intake after MC04784 once latest deployment/liveQA complete.

## MC04785 TransDimensional Hunter whole4 restored, Future war8
Explicit future blocks Warzone Earth ancestor. Primary particle-perception mechanism does not establish parallel Earths. No false multiverse move. All4 English Baen lowres fronts localized, no new fiction. Next unresolved MC04788 Citadel.

## MC04788 Troy Rising whole3 restored to Starbridge9
Earth resistance4->3, whole interstellar fleet campaign not first premise. Citadel2011 missing restored, bundle2020 and second edition2023 phantom entries removed.2026 authorized anthology noted, Ringo novella/short novel length ambiguity not counted as fourth conventional novel. Next MC04789 Citizens.

## MC04789 Citizens skip, MC04790 Looking Glass whole4 to Patrol spaceship8
Citizens Baen multi-author unrelated veterans anthology skipped. Looking Glass first-book-only Warzone home rejected whole; later3 navy exploration/combat ship. Full primary chapter7 resolves ordinary planetary gates same universe via substrate, Tuffy uncanny cosmology retained. Claws2008 corrected, all4 fronts localized. Warzone Earth5->4. Next MC04791.

## 2026-11-05 MC04795 Post-alien devastation seed
Curator Approved phonemsg-01M6P0SNH05832F272PCXACRGQ15:11:24 to exact served seed, name his. Gunpowder & Embers whole1 from Lost knowledge quest7->6, new1; PHS children3->4. First2020, eARC2019 not extra. No parent gate widened. Alien dominions whole-engine challenge checked/rejected, real cult strand recorded. Next MC04796.

## MC04801 Black Tide Rising whole11 -> Post-pandemic mutants6
Whole shared world11 regular published novels2013-25 restored from6, first2013 fixed; Zombie virus7->6. Living aftermath/reconstruction whole outweighs outbreak portions in Graveyard/Valley/Gannon World, no ancestor edits. All11 English fronts local.4anthologies+2023graphic ancillary, King FlorCubaTamp delayed primary despite2025 catalogues, World We Forge2027 anthology partial/eARC excluded. NextMC04802 already Paladin; check04803.

## MC04806/07 Special Circumstances whole2 retained Demon counter ops3
Episodic volumes form caveat explicit, no internal-story extra cards; faith/damnation operational response strongest despite genuine Old Ones opening/finale and Queen astral rescue. Current secret-service direct Urban route repaired in rationale.2English Baen fronts local. Next new04813 Last Centurion.

## MC04813 Last Centurion whole1 -> Wasteland journeys5
Die-off9->8; simultaneous plague+mini-ice-age,22chapter long company extraction and later reconstruction outweigh first9 catastrophe analysis. Final5 settlement/rebuilding real wobble, no definition stretch. English front local.04824/28 Black Tide anthologies skipped/already ancillary. Next substantive04825 Von Neumanns War.

## MC04825 Von Neumanns War whole1 retained Warzone Earth4
Contemporary open mechanical invasion not conscious imperial motive, significant engineering/hardSF straddle explicit. Mars biosphere-killing assertion removed as unverified. One English front local. Next new04831 After the Coup novella eligibility first;04832 Fuzzy Nation.

## MC04831 short, MC04832 Fuzzy Nation1 retained Planet plunder5
Author explicitly separate reboot continuity not Piper merge; extraction/personhood court conflict whole. CurrentTor2022English front local first2011 unchanged. AfterCoup author2008short-story skipped. Next04833 HeadOn/LockIn universe.

## MC04833/34/59 LockIn2 retained Cyborgs8
Bothnovels independently researched mediated humanembodiment,policeprocedural and Agora/neuralreality straddles explicit. BothEnglishprint fronts localized, LockIn2015reprint(first2014). Unlockednovella not counted. Next04835Metatropolis anthologyskip then04836MonstersOhio.

## MC04835Metatropolis anthology skip, MC04836MonstersofOhio1 SatiricalSF8
PublishedUSNov3UKNov5confirmed author/currentpublisher. Satirehumanpredators/kindmonsters, causaluncertaintyrecorded no inventedalien/Cthulhu/fungus. Tor2026Englishfrontlocal.832/2711/6328. Next04837OldMansWarshareduniverse rewalk.

## MC04837 OldMansWar7 moved Futurehistory valid9 nominal10
Wholecivilizationchronicle not supersoldieronly;all7Englishfrontslocal. SlowGods knowninvalidFuturistroot12secbackwards,nohonestterminalTimeTravelleaf,pendingcuratordiscussion;excludeinvalidtenantfromsplitcount.832/2711/6328unchanged. No nextintake untilSlowdecision.

## SlowGods scopednonintegralblip ruling2026-11-05
Originalphonemsg-01M6P4575KPNQ79ZFW7NV9A5HF permitsignoring12secblip, notglobalrulechange. Rootcaveatremoved,Futurehistoryvalid10freeze,splitrequiredbefore04838.832/2711/6328unchanged.

## Approved Future history in space split2026-11-05
Curator Approved phonemsg-01M6P4XYQJCZ647JS4PF6F0A6D, 2026-11-05 16:23, on final names block phonemsg-01M6P4RCBZS1BJ6H7QZYCJ169W. Original umbrella retained zero direct fictions; actual whole-fiction partition 3/4/3, not per-volume placements.
Star empire chronicles3 / Star alliance chronicles4 / Star diaspora chronicles3. Threepixelinspectedportraits890-892, original38umbrella retained.835nodes/2711fictions/6328books. NextMC04838 afterdeployandliveQA.

## 2026-11-05 MC04838 Redshirts whole1 -> Time door2
Integralplannedpastjourneythroughblackholeandback, not builttimeapparatus; Scripted4->3, TimeDoor1->2. No definition changes.2013Englishprintfrontlocal,2012firstyearretained.835nodes/2711fictions/6328books unchanged. NextMC04839 ShadowWarNightDragons prologuerow, inspectformat.

## 2026-11-05 MC04839/40format skips, MC04841AndroidsDream -> Spaceenvoy4
NightDragonshortstory, MonstersOhioexcerpt skippedsourcegrounded. AndroidsDream1futureinterstellardiplomaticcomedy movedfromModernSatirical8->7 toSpaceEnvoy3->4, no gateedit;2019TorEnglishprintfrontlocal,2006firstyear.835/2711/6328 unchanged. Next04842EndAllThingscomponentrows, alreadywholeOMW7 coversnovels.

## MC04842-57 serialcomponents covered
4EndAllThingsparts+12listedHumanDivisionepisodes sourceverifiedagainstpublisher/ToC. Alreadybooks6/5 withinwholeOMW7 Staralliancechronicles. No extra cards/books. NextsubstantiveMC04858TheInterdependencywhole3 existingGalacticcourts, researchnotmutated.

## MC04858Interdependencywhole3 retainedGalacticcourts9
All3owncausalplotsverified,Flowphysicalstartravel nottime/parallelproof, MemoryRoomdigitalnotancestorvisit. Singlethronecenterdespitemerchanthousesstrongwobble.2018/19/21EnglishTorfrontslocal,first2017/18/20. Not a tenthcard. Next04859LockInalreadywhole2rewalkcomplete,04860PresidentsBrainformat,04861Unlockednovellaalreadyancillary,04862MoonHitsEye.

## MC04860/61format skips, MC04862Moonwhole1 -> Satirical8
PresidentBrainshort2010,Unlockednovella2014 sourceverified. Moonauthorcalls episodicnovel,notcollectionskip. Societalcrisisresponse/comedygoverns,Impact5->4/Satirical7->8; no actualhit, resets. Fantasyrootanddisasterwobblesexplicit,noattestedmagic/time. English2025Torfrontlocal. NextMC04863CrawlersJohnShirley.

## MC04863Crawlerswhole1 -> Technocrisis9
2003firstnot2007ebook. Humanmilitarynanocolony containment/hiveassimilation; noaliens,nogenedesign/medicalnanos/naturalzombiepathogen. StrongCreaturefeature/pulpwobble recorded; explicittechnicalaccount/rationalizedsystemkeepsTechnothriller. English2003DelReyprintfrontlocal.835/2712/6329. NextMC04864Armor.

## MC04864Armorwhole1 -> AlienWarGrunts9
1984firstnot2020reprint. Allfivepartsreviewed, Crowcolony/memorystrandgovernswaraftermath, Enginepsychologicalnotengineeredsoldierbody. StrongSuperSoldier/SpaceCaperwobblesexplicit;spatialTransit/memorynotactualtime. Vampire$authornoteexcludesidentity. English2020DAWprintfrontlocal.835/2713/6330.Next04865Vampires.

## MC04865Vampire$whole1 -> VampireHunt6
1990first=2008Vampiresretitle/reprint. Fullnovelplotnotfilm,literalblessedsilver/Damnedpredators;modernVatican-backedcommercialhunters. Armorcharactersseparatebyexplicitpublicationnote. English2008Acefrontlocal.835/2714/6331.NextMC04866.

## MC04866DaysOfFuturePastwhole3 -> PostApocalypticFantasy8
2016/17trilogynot2022newnovel,notPOI. ActualdivineforwardtimeFantasyrootfirst,wholefutureCaliforniacollapse/questincludingAybem/spacecleanupchecked. Cyborg/Moonfineplotreaderconfidenceexplicit. ThreeEnglishpaperbackfrontsISBNlinked/local.835/2715/6334.NextMC04867SometimesintheFall.

## MC04867/68SeasonsOfChangewhole2 -> RetroSpaceOpera6
SummerEnd2022/Fall2025not2020. Authorcurrentseries2,thirdinprogressJuly2026. WholeDavefreight/family/ventureandBenrescue/Venuswarchecked,HardSFOrbital/Western/Drama wobblesexplicit. EnglishS&S2023MMsummer/2025TPfallfrontslocal.835/2716/6336.NextMC04869.

## MC04869/70Varley
BlueChampagnepublisher8storycollectionskip; wholeThunderLightning4 -> TimeDistortion5. Localblackfieldtime/age/ratesgoverningtemporalpriorityoverstrongRetro. LastinventionFTLreader-sourcednotpublisherphysics. All4Englishprintfrontslocal.835/2717/6340.NextMC04871DemonwholeGaea3.

## MC04871Gaea3 -> ClassicPlanetaryRomance10
Whole3plotsandbiotechrootchecked,HardScienceFantasyknownphysicsnotcertified,BDOlosingfirst-bookroute.1987paperbacklineTitan/Wizardand1984originalDemonprintfrontsactualpixelslocal.835/2718/6343.INTAKEFROZENmandatorysplitat10;proposalresearchnext,noquestionservedyet.

## 2026-11-05 bounded Classic planetary romance repair batch1
NorthwestSmith all-shortstorycollection excluded+preserved exclusionrecord. WholeSpaceTrilogy3->ModernBiblicalMyth3, literalworkingChristianpowers; wholeKane3->DIYrewind9, actualpasttrip + laterprivaterebuild controlswholefiction. BoththreebookfrontsetsEnglishprintlocalized/pixelchecked. Classic10->7; no split warranted. Rhiannon mechanism/sharedBrackettSolarSystem scope still underresearch, no move yet. Intake remains frozen until leaf settled. No definition changes.

## 2026-11-05 bounded Rhiannon shared-fiction repair
Stark and the Star Kings: whole connected BrackettSolarSystem/Stark/Skaith + HamiltonStarKings10novels -> Overclockian6; Classic6. Explicitsameuniverseauthorscrossover, exactprivateownertest, Reaverslinkedmindscoldrationalization verifiedprimary notgoddessreviewshorthand. TenEnglishprintfrontslocalized/pixelchecked, no genrechange. Intake frozen pending remaining Classic integrity closeout.

## 2026-11-05 bounded Classic audit closeout
Well World scope3->10 novels restored, same Classic leaf after full walk. All10 English print fronts local and pixel checked; Ghost StraightGate original text connects Well and colony home, no unsupported alternateEarth or time travel. Author noncanonical-final2 caveat recorded, same shared setting. Classic6; no split warranted. Other survivors checked: Gulliver explicitOldMarsruling, Columbus physicalVenusvoyage, Stonehenge physicalgalaxyworlds notprovenalternateEarth, Arkad Baen/Locushumanvisitorquest, Gaea alreadycomplete. No gate changes. Counts835genres/2717fictions/6360books.

## MC04872 Millennium whole1 -> PostApocalypticFantasy9
1983firstnot1999reprint. Originalfinalcreatorvoice/freewill/evolution/Eden checkedprimary+EBSCO,notmeregodlikeAI;Fantasyrootbeforetimegate. LastAgealreadyfallenEarth/secwarspollution,notbiblicalangel/demonapocalypse.1983investigation/CouncilGateProjectstrongstraddlesrecorded.1999AceEnglishprintfrontlocal.835/2718/6361. Next04873PersistenceVisionformat then04874SlowApocalypse.

## MC04873-78 resolved, SlowApocalypsewhole1->ChemicalCatastrophe4
Persistence1978shortcollectionexcluded;Slow2012oilmaterialfailure->Chemical4 afterwholecitycollapse/caravan/recoverywalk;printAce2012ISBNfrontlocal. Titan/WizardalreadyGaea3notduplicatecards. WiswellDIY2022/MissMyself2024explicitshortsexcludedownauthor/publisher.835/2719/6362. Next04879.

## MC04879-81 resolved: DragonHasSomeComplaintswhole1->CozyPeeps6
PhantomViewexplicit7580wordnoveletteexcluded;ThreeOClockDragonshort18pexcluded. 2026Dragonwhole1 foundcare/rehabbonddespitemajorwar/godclimax;Soldier9stronglosingroute,notunit-as-story. Authorhypotheticalcrossoversnotsharedcontinuity. EnglishDAW2026hcfrontlocal.835/2720/6363. Next04882Chrysalids.

## MC04882Chrysalidswhole1->Mutant5
1955novelReBirthsamework. Primarypublishersglobalnuclearwar;wholemutationpuritypersecutionandFringesrescue,notpsiscienceprogramme. Noactualtimetripfromdream. EnglishNYRB2008paperbackfrontlocal.835/2721/6364. Next04883OutwardUrge.

## MC04883-84: Facewhole1->TermsOfService10, ALL INTAKE FROZEN
OutwardUrgeSFE/ISFDBlinkedshortcollectionexcluded(Wikipediafixupnovelconflictretained). Face2022novelownTor/LocussettlesformvsoneSHnovellalabel. Wholepervasiveranking/surveillance/avatarselfpolicingTerms9->10. Mustresearchcontentofall10wholefictionsandserveApproveSplitbeforemoreintake. Noopenquestionyet. EnglishTorhcfrontlocal.835/2722/6365. Next04885TwiceLivedblockedbysplit.

## Terms10boundedcontentrepairs,nosplitneeded
CompanyTownwhole1->TimeAgencyThrillers8(originalBranchfuturecorporateprototypes/doorwayinfrastructure);Scionwholecurrent1->CyberpunkNoir4(ownfinishedreviewsprotection/identitysyndicateplotnotopeninglegaldayjob). Terms10->8. No definitionschanged,only2individualmoves. BothEnglishprintfrontsreinspected/localized.835/2722/6365unchanged. Other8notrewritten,noformexceptionrevoked. NoApproveserved. Resumeorderedintake04885oncebatchlive.

## MC04885TwiceLivedwhole1->MirrorMultiverseFantasy7
Wholebothfamily/lives/settlingendingreviewed. Fantasy/SFrootconflictdisclosed:YAMLnotesunscientificbodilytransfer,notclinicalengine. No seed.EnglishhcPWfrontlocal.835/2723/6366.Next04886Arabesk3mustresearchEVERYvolumeown.

## MC04886Arabesk3->MachineAgeAlterations8
All3ownpublisherandfinishedreviews,bothEffendicity/politicaltraumaandFelaheenancestry/geneticrevealnotonlyfirstnovel. Explicit1915peacefork100yearsafterlivingcounterfactualorderbeatsnoirFuturistwobble. CancelledAshrafBey2008notfourthagainstSFEselectedlisting.3Englishprintfrontslocal.835/2724/6369. Next04887EndWorldBlues.

## MC04887EndWorldBlueswhole1->TimeAgencyThrillers9
Creatorallowsliteral/timeSFnovelinset/traumareadings,ambiguitypreserved. NarratedmachineHighStrangeoffersspecifictime/placeexile,builtregimeapparatusnotnaturalrip;original58/40/41/49read. English2007printfrontlocal.835/2725/6370. Next04890checkqueue;watchdogactive.

## MC04890StampingButterflieswhole1->MindOverTime7
Originalending1977tippingpoint/changedfutureshipprovesrewrittenhistory,notonlydreammetaphor. Mentalintertemporallinks,LibraryAIinducedstatewobblerecordednotinstitutionalpassengerproject;falsevirtualpeoplebelieffinallyrefuted. English2006SpectraYoullprintfrontlocal.835/2726/6371. Next04891Assassini3ownvolumeresearch.

## MC04891-93Assassiniwhole3->AltRenaissanceFantasy4
EveryownnovelresearchedincludingOutcast/Exiledending,originalcavegodsnotinventedscientificengine. OwncreatorMarcoPolodukes/strongerByzantiummaterialcounterfactualbeatsPeriodVenice. ThreeEnglishUK/USlaterprintfrontslocal,UKOutcastplaceholderrejected.835/2727/6374.Next04894MerzSlaverscheckwholeShadowWarrior.

## MC04894-95ShadowWarriorwhole2->PulpSwordSorcery10FROZEN
Eachnovelownengine/Slaversfinal37read. StatedNehonIgulbookmap/narrative FantasyRealms, earlyNinjaalternateEarth/JapanKoreablurbwobbleexplicit. Slavers2014eARC/2015print. BothEnglishprintfrontslocal.835/2728/6376. STOPnextintake;reinterrogateall10/PulpS&Ssplitbeforeproceeding.

## FrozenPulpS&Sreinterrogation:TowerFear->Tinderbox8
WholeoriginalclimaxopenLivingrebellion/occupiedcityregimechangeconfirmsPolitical/Rebel/Tinderbox,notoldPWlabelonlyS&S. Pulp10->9,noPulpSplitgate. Counts835/2728/6376unchanged. Remainingboundedwhole-fictionbookscoperepairsPulp:BlackCompany/Hanuvar/Imaro/ThievesWorld/Fafhrdformats;noothermoveornewgenreapproved.

## 2026-11-05 Fafhrd scope completion
Added Bailey Swords Against the Shadowland1998,onePulpfictioneightdisplayedbooks,2009EnglishDarkHorseprintjacketinspected/localized. Sixlegacycollectionsleftunchanged:ownerexclusionoriginalnotfound,deletionwithdrawn19:52. Counts835/2728/6377.

## 2026-11-05 Hanuvar whole-fiction completion
Added vols1/3, three published episodic novels, Pulp9 unchanged. Vol4 not released. Corrected old revenge/army rationale using each novel. Counts835/2728/6379. Two added English publisher print jackets inspected and localized.

## 2026-11-05 Black Company thirteen novels
Added SilverSpike1989 andnowreleasedTheyCryNov3,2026. PreserveuserS&ShomeOct4phonemsg-01M4365QDXX624V0Y07SSC1VBA;latearcworldbuildingwobbleexplicit. Counts835/2728/6381. TwoEnglishTorprintfrontsinspected/localized.

## 2026-11-05 Fafhrd current-fiction cover stabilization
Localized all7legacyEnglishprintfronts after intermittentexternalloadfailures. Two poor photographs replaced with cleanpublisherDarkHorseflatprintfronts. Countsunchanged835/2728/6381. All8localEnglishjacketsinspected,noformatdeletion.

## 2026-11-05 Imaro four novels
AddedTrailBohu1985/NaamaWar2009afterwholefourwalk. Pulp9remains,lateepic/hiddenheirwobbleexplicitnotignored. Dossouyeauthor2017separateworldnotmerge. Counts835/2728/6383. TwoaddedEnglishpaperbackfrontsinspected/localized.

Imaro live QA followup: new2visible; old2cardshadnojacketsandheroSFPLsticker. RecoveredcleanNightShadeprintfrontsandlocalizedboth. Awaitlatestdeploybeforecompletion.

## 2026-11-05 Thieves World whole-fiction repair
Abbey-only card completed to11novels including samecontinuitySacredBand; movedPulp8/BorderlandMultiverse6becauseactualEarthcrossingsviaLemuria,homegroundSanctuaryreturns. No standalonebooksplit, no newgenre. Excludednewcollection/novella/uncertaincontinuityrowswithsources. ElevenEnglishprintfrontsinspected/localized. Counts835/2728/6393. Awaitdeploy/liveQA.

## 2026-11-05 Raven/Elves samefiction
Consolidatedalreadyexisting7+3novelcardsunderauthorprimarysameworldevidence. Whole10walkSoldier9unchanged(removeElves/addcombinedRaven),Pulp8->7. Counts835/2727/6393. All10Englishprintfrontsinspected/localized. Awaitdeploy/liveQA.

## 2026-11-05 FinalPulpboundedscopewalks
Anji1publishedretainedPulp,Jan2027sequelnotadded. SwordDancer8allpublisherplotsrecheckedretainedPulp(personalpair/familymagicaladventurenotarmies). Pulpnow7afterTower/Thieves/Ravenmoves;nofrozenleafremains,noquestionopen. AwaitRaven/Elves16c38232deployQAthenresumeMC04896.

## MC04896-98 DragonLordswhole3->Parody9
Eachnovelownpublisher/finishedreviewschecked. Metatextualheroicquestsendupwinswhole3overCaper/latePoliticalGodhood;latehumordisagreementexplicitnotfirstbookshortcut. ThreeEnglishOrbitprintfrontslocal/visuallyinspected. 835/2728/6396. No gate, next04899EmpireStorms3. Deploy/liveQAremaining.

## MC04899-04904 Evil empire seed, wholeSkovron6
Curator Approved phonemsg-01M6PPVJW7A9SR7WZTTXFCJJS9 (2026-11-05 21:36:55 CET) on served seed phonemsg-01M6PPTVYMHK32JQGQ00DV3B87 and explicit axis/parent widening phonemsg-01M6PPTY4TDKTG7YDTQK1AHV08; name supplied by curator phonemsg-01M6PPRMHAN041VVB1M7TVEYCF. Rebel2->3 children;Samizdat6/Tinderbox8unchanged,new1fiction6novels. Local6Englishprintfronts.836nodes/2729fictions/6402books. NextMC04905BarricadeJonWallace. Deploy/liveQAremaining.

Evil empire 1d916bcf live visually verified 21:41; portrait and six loaded jackets inspected, parent informed.

## MC04905-04907 Kenstibec3->Nuked5
Every novel own official/finished-review read. Nuclear ruins/rebuilding communities throughout, mixed-cause/artificial-human identity wobble explicit; no Robot gate widening. Three localized later English Gollancz print fronts inspected.836/2730/6405. NextMC04915FreeBastardswholeLotLands. Deploy/liveQAremaining.

Kenstibec45631bd7live3jacketsverified/reported21:45.

## MC04915-16LotLandswhole3->Pulp8
OwnGrey/True/Freepublisherandfinishedreviews,authorinterviewexplicitpersonal/pulpformevenwarbook;latePolitical/Militarywobblefullyrecordednotfirstbookshortcut.3EnglishPRHprintfrontslocal/inspected,latereditionsoriginal2015/2019/2021years.836/2731/6408. Next04917Howardshortscheck. Deploy/liveQAremaining.


### 2026-11-06 - Freakbusters seed
Curator Approved phonemsg-01M6QP475PE22GXJBJ47QNJGCX (2026-11-06 06:43:24 CET) on served seed phonemsg-01M6QP3KVJ3F0C4BQ5D25N0981. Name proposed by curator phonemsg-01M6QNZWX6H9KH73VZ7QSYBS1B. No existing gate changes. Onefiction33novels, eighthUrbanfantasychild; actualmagicboundary, wholefictionstraddles, containercaptionsandper-volumeQAexplicit.3priorHoward/Deadlandsskiprowsrecoveredexactly.


### 2026-11-06 - Bartimaeus
MC04923-26 four anthology skips; MC04927-29 one fiction/four novels placed in Paranormal bureau5->6. Full whole-fiction walk and4English jacket QA; no structural change. Next MC04930.


### 2026-11-06 - The Wicked Sea
MC04930shortstory/31unpublished2027 skipped;MC04932onepublishednovel -> Magic bond romantasy7->8. ExplicitdifferentworldfromBitten. Fullwalk/tetherbargainvsinnate/EnglishcoverQA; nextMC04933.


### 2026-11-06 - The Great Undead War
MC04936nonfiction skip;37whole3novels -> Alt diesel fantasy8->9;38anthology skip. Allthreeenginesread;2026sameuniversespinoffunexplainedtime-eratransfer/HUDsubstantialstraddle;magicrootfirst. NextWALKMC04939.


## Post-infestation survival (2026-11-06)
Fifth Post-holocaust survival child; native proliferating life rather than disease or aliens defines the living aftermath. One fiction/two novels Invasive Species/Slavemakers, no moves or gate widening. Descriptive sibling-pattern coinage, not established literary term; Post-Infestation alone is an existing C. A. Gleason short-work title, not exact full-name collision or trademark proof. Honest ceiling1; Triffids/Green Brain look-alikes excluded, other leads unverified. Approved phonemsg-01M6QVDV36P8KNNCE3XX2NV0FC08:16:02CET on served seed phonemsg-01M6QS3TTT4Y9KER6AWG0Q8KNW and axis phonemsg-01M6QS3X004KV8DH41RQ2FH9FJ. Portrait895 A selected, two local English flat jackets inspected.
838nodes/2736fictions/6451novels. NextWALKMC04940. Deploy/liveQA pending.


### 2026-11-06 A Strange and Ancient Name
MC04940standalone1 -> Medieval Fey1->2;reverseportalwobblepreserved;primarysample7chaptersread;1993nominalfirsteditionvsDec1992release;2015ebookqueue. English235x375originalfrontinspected. NextMC04941PrinceoftheSidhe2. 838/2737/6452.


### 2026-11-06 Prince of the Sidhe
MC04941/46whole2 -> Celtic6->7;bothownprimarysamples/synopsesread;reverseportal/secondSaxonwarwobbleexplicit.1995/96originalnotqueueebookyears.235x375Englishfrontsvisuallyinspected. 838/2738/6454. NextMC04943Highlandertieinskip then44KingsSon.


### 2026-11-06 Kings Son Magics Son
MC04943Highlandertie skip;44standalone1994 -> Celtic7->8;45BardsTale tie skip;46alreadywholeSidhe2. Balladsource/renamedBritain/romancewobbleexplicit;nooverlappingseed.9chaptersauthorizedsampleinspected,originalEnglish147x240front.838/2739/6455,nextMC04947Echelon/Empyre.


###2026-11-06RyanLaing
MC04947/48whole2(2006/2007)->Cyberpunknoir4->5;ownprimary/revieweach,authorizedsamplesboth,metaverse/cyborg/alienorigin/dystopianwobblesrecorded.EnglishPRHfrontsmatchedpaperbacks,localized302x450.838/2740/6457.NextMC04949IllustratedEric(existingDiscworldcheck),50Dragonsitterwhole.


###2026-11-06Dragonsitter
IllustratedEric49duplicatealreadyDiscworld. Whole10Dragonsitter2012-2019->Mythicfarce5->6,actuallegendarybeingscomicgate,notinheritedfamily/place.10ownpublishersynopses,finishedreviewseach,10Englishprintfrontslocalizedandinspected.838/2741/6467.


###2026-11-06HouseBottomLake
MC04956standalone2016->Feralhouse3->4;inexplicableactivehouseagency,notdeadownerclaim.Romance/MR/portalwobblesexplicit.2021Englishpaperbackjacketlocalized.838/2742/6468,nextMC04957Daphne.


### 2026-11-06 Daphne
MC04957 Daphne (2022) -> Vengeful spirits8->9. Specific returning dead woman hunts thinking victims. Cameo/geography scope and Vengeance torment overlap recorded, no gate change. Official English2023paperback jacket localized.838/2743/6469. NextMC04958Goblin.


### 2026-11-06 Goblin
MC04958 Goblin(2017) -> Cursed towns6->7. One linked novel6novellas plusframe, onebook, wholeplaceengine. Prestoandmundanehorrorwobbles explicit;cameosnotallMalermanmerge. OfficialEnglish2022paperbackfront.838/2744/6470. NextMC04959Inspection.


### 2026-11-06 Inspection
MC04959 Inspection(2019) -> Sociological SF5->6. Pairedcohortconditioningexperiment,primaryauthorrejectssupernatural. RecognizablepresentchosenwithSFENearFuturelabelwobblerecorded. OfficialEnglish2019paperbackfront.838/2745/6471. NextMC04960MaloriewholeBirdBox2.


### 2026-11-06 Bird Box
MC04960 Malorie2021paperback -> wholeBirdBox2014/Malorie2020,Post-apocalypticfantasy9->10. SFalienlabelvssupernaturalrootwobbledisclosed.838/2746/6473. ALLINTAKEFROZENpendingPostapocalypticfantasysplit;nextMC04961notwalked.


### 2026-11-06 approved Post-apocalyptic cause split
Owner Approved phonemsg-01M6R1CA7FDFP5DZYVRHYQC4C3. Original umbrella0, Post Magicalypse6 / Fantasy after Disaster4, two new leaves/portraits896A/897B. Counts840/2746/6473 unchanged cards/books. No scope repairs bundled. Greek/Ancient Greece follows separately before MC04961.


### Whole Sipstrassi / Ancient Greece retirement2026-11-06
Owner Approved phonemsg-01M6R3B5CZRVQVGNWBVEKKB40N, accepting ruinedfuture frame. GreekSeries2 merged into StonesPower4 plus Bloodstone1994 = seven novels/one fiction in Post Magicalypse. AncientGreece retired, oldid redirectsPostMagicalypse; Classicalantiquity retained overRoman only.839nodes/2745fictions/6474books; netcards-1, books+1. Title/idStonesofPower unchanged.

## MC04961 Pearl2026-11-06
Whole1->Creaturefeature2;2019original/2021retitle/2022paperback; no-pretenseanimalintelligence slasher, psi/vengeance/animalfable rivals and datecontradiction recorded in walk-mc04961.md.839nodes/2746fictions/6475books. NextMC04962PicturesofYou.

## MC04962-04964 2026-11-06
PicturesofYou skippurehorror5sourcesread;SpinBlackYarn skipcollection PRHfive novellas. UnburyCarolwhole1original2018->Fairytaledamselinversion4, rootsettingandrescuerole qualifiedinwalk-mc04964.md;WeirdWestremains9/no split.839/2747/6476. NextMC04965WatchingEvilDead.

## MC04965-04966 2026-11-06
WatchingEvilDead skipnonfiction perPRHownlifewritingguide. MorrisBakerwhole2original2022/2023->AltColdWar6; firstandsequelownengines/current2scopefullwalkinwalk-mc04966.md.839nodes/2748fictions/6478books. NextMC04967BurningMagic.

## Shadow Magic trilogy, 2026-11-06
MC04967-04969 whole3 -> Necromancer4. Full per-volume engines and mystery/setting wobbles recorded in walk-mc04967-04969.md. Three English print jackets localized and inspected.839nodes/2749fictions/6481books. NextMC04970.

## Amenkor shared universe, 2026-11-06
MC04970-04971 whole9 -> Channeled hard magic9. Author explicit all3sameworld, each trilogy ownengines grounded. Fullwalk, time/politicalrivals and thinBreathreviewcaveat in walk-mc04970-04971.md. Nine English print fronts localized, currentreprints disclosed.839nodes/2750fictions/6490books. NextMC04972.

## BloodlessQueen, 2026-11-06
MC04972whole1->Perilousfairydoors7, actualanchoredTree/Faerieparentrescue. SFmarketing/lateportalrivalsrecorded.839nodes/2751fictions/6491books. NextMC04973ForeverSeaduology.

## ForeverSea wholeduology, 2026-11-06
MC04973-04974->Revisionistquestfantasy9to10FREEZE. Positiveheroicrevision; ecologicalwobble/depthgateexplicit. NoEcoseed. Splitresearchall10owed, nextMC04975paused.839nodes/2752fictions/6493books.

## White Rat consolidation, 2026-11-06
Confirmed Clocktaur+SaintSteel shareduniverse->oneWhiteRat8novels inexistingDutyBond8to9. Revisionist10to9, Paladin4to3. Invalid10cardtriggercancelled. No newgenre, noEcoseed, nodefschanged. MC04975stillpausedforparentreconciliation.839nodes/2751fictions/6497books. Goredd/AfterWar scopegaps notfixed.

## Intake resumedMC04975-78, 2026-11-06
Main11:13:25resumeafterWhiteRatQA. MC04975editionexistingBabel4. MC04976-77existingHexologists2re-walkCozyCraft4to3->Magitech1to2,firstyear2023fix,third2027unpublished. MC04978pending-scopepicturebookperparent11:15:48,notban. NextMC04979.839/2751/6497unchanged.

## Approved Ancient Greece seed2026-11-06
OriginalownerApprovedphonemsg-01M6R6XHAGWZG1ZSCC0172NF3J read. AncientGreecefantasynewstableidancient-greece-history-fantasy underClassicalantiquity1to2, oldredirectuntouched. ConfirmedAlexander2(Tarr2004/2008), Lord1993disputednotadded. Portrait761reusedafterQA;2localEnglishprintcovers.840nodes/2752fictions/6499books. NextMC04980afterliveQA.

## MC04980 DevilBargain whole2
Altcrusade1to2,sharedscopeconfirmed2002/2003,PrideKingsindependentpercompletedcomparativereviewnotmerged. Bothownenginesread,2localRocEnglishprintjacketsinspected.840nodes/2753fictions/6501books.NextMC04981.

## MC04981 William Conqueror whole2
MedievalFey2to3,2004/2005notebook2007. Bothownenginesread,Otherworldrestoration/landbondpositive;Arthurstraddleexplicit,historicaleventspreserved,nosecret-themepremise.2localEnglishRocfrontsinspected,Ritebordercroponly.840/2754/6503.NextMC04982.

## Frankish myth fantasy (2026-11-06)
Owner Approved phonemsg-01M6RBADZY44A1905AKNNNKVQ2 on served block phonemsg-01M6RB81NF95V4PHRQEPM6KXA9, after choosing name phonemsg-01M6RB7S1H5SS8JZVAT3DRBKQH. Mythic retelling7to8, Kingdom of the Grail2000 one fiction/one novel, no moves/gate changes. Matter of France tradition, not historical Franks in general; Arthur/Grail hybrid wobble explicit. Descriptive sibling-pattern name chosen by owner, not claimed formal genre or trademark clearance. Supersedes proposed Carolingian/Charlemagne labels. Honest ceiling1, Three Hearts stays portal. Portrait898A selected after visual review of two variants.
841nodes/2755fictions/6504novels. NextMC04983 afterliveQA.

## MC04983 Rhiyana5 whole fiction
HoundFalcon3+Alamut2sameworld confirmedpublisher/reviews. MedievalFey3to4, all5ownenginesread;authorpsi-mutantoriginwobbleexplicitagainstactualnarratedfantasy/publicroyalpolitics.5Englishprintfrontsinspected/localized.841/2756/6509.NextMC04984.

## MC04984 Song of Ireland
TimeDistortion5to6. Unequal-rateDanuCities engineeredSF, actualtextending governs. Quartet4mythcyclesthematic, notpositivecontinuity. 2006onebook,2014TorEnglishpaperback.841/2757/6510.NextMC04985.

## MC04985 CaptainNemo whole3
Existing20kcard folds Castaways/Island bypositiveprimarycontinuity. ScientificAdventure8unchanged.3Englishprintfrontsinspected/localized.841/2757/6512.NextMC04986.

## MC04986 Off on a Comet
FORCEDScientificAdventure8to9. NaturalcometvsTechMarvelgatewobble explicit. No shallowseed/widening.1877onebookMint2021jacket.841/2758/6513.NextMC04987.

## MC04987 Paris in the Twentieth Century
FutureSocialSF7to8. Written1863future1960, firstpub1994. Corporateefficiencycrushesartist, Dystopiarivalsfailchildgates.1997DelReyEnglishprintfront.841/2759/6514.NextMC04988.

## MC04988 Baltimore Gun Club whole3
Existing EarthMoon2 folds NorthPole sequel1889. Orbital mechanics7 unchanged. Three distinct English print fronts inspected/localized. Third terrestrial axial-dynamics straddle explicit.841/2759/6515. Next MC04989.

## Irish myth fantasy (2026-11-06)
Approved phonemsg-01M6RCX3V80P0GQAY2C6YDT81Z on served block phonemsg-01M6RCVMYF1DWH36NXS4C36EHS. Mythic retelling8to9, one connected Watson Ulster Cycle fiction/two novels2009/2011. Primary Raven excerpt explicitly reacts to Deirdre flight. No existing moves/gate changes. Descriptive sibling-pattern label, no exact named-property collision shown, not trademark clearance. Portrait899B selected after full-size A/B inspection, two English print fronts localized.842/2760/6517. NextMC04990.

## Duellists whole3 MC04990-92
Caper9to10 FROZEN. Intake PAUSED for immediate split. Every novel own engine researched, clockwork mechanism unverified so no false Steam/Magitech.3localEnglishOrbitjacketsinspected.842/2761/6520. NextMC04993afterapprovedsplitlive.

## Classical and Celtic myth bundle,2026-11-06
OwnerApprovedphonemsg-01M6RFDYE1AG8KVCEN1G519KVK onphonemsg-01M6REYJM5ZZE3NTDVN4MT7FF7. Mythic9to8; ClassicalGreek/Roman, CelticIrish/Welsh. WholeLloydJones3mergedfrom3cards;Caper10to9triggercancelled. Tournament retained empty, no retirementapproval.845nodes/2759fictions/6520books. Intakefrozenforrequestedlong-termMythicstructureproposalafterliveQA. Portrait900A901A902B inspected.

## Mythic growth proposal declined2026-11-06
Ownerphonemsg-01M6RGDGKMRV87X7WJ8Y9E2F35keeps8fornow; Europe/beyondEuropeblock01M6RG5A96CVJZGRHTTN8KAFWAdeclined. Nochange. Classical/Celticdbb22bdliveandQAcomplete42223015125. ResumeMC04993.

## MC04993-96, 2026-11-06
Embodiment unpublished Nov10 skipped current Nov6. Phoenix Hoard whole3 placed LivingCity3to4; every volume own engine, clan legacy/Tokyo straddle explicit,3 English print jackets localized/inspected.845nodes/2760fictions/6523books. NextMC04997.

## MC04997 Boreal Moon whole3,2026-11-06
DynasticMagic9to10FROZEN. ALLintakepausedforimmediatesplitaudit. 2003/2004/2006firstyearsverified,everyownenginewalked,3EnglishVoyagerjacketsinspected/localized.845nodes/2761fictions/6526books. NextMC04998onlyafterapprovedsplitlive.

## Inheritance whole-fiction root correction2026-11-06
Whole3novels+existingnovella moves DynasticMagic10to9 -> InventedGodhood4to5. Splittriggercancelled. FourcoversQAincludingrejectBroken titlepageandHundredARCforfinalpublisherjacket. No structuralchange. ActiveGrishaverse/Artamonscopeauditcontinuesbeforefreshintake.

## Magic politics 2026-11-06
Approved originalphonemsg-01M6RHKZ46K3FRD9QN028GH4RG onphonemsg-01M6RHFMFHDPTM16JZBFTJNXY3. Political3to4children, unchangedparentdef. Artamonwhole7 onefiction, dynastic9to8 martial5to4, duplicateLegacyfolded. Name descriptive not formalattestedgenre; fullwalkandproofartamon-whole-repair.md. Grishaversenotpartapproval.

## Grishaversewhole7normalplacement2026-11-06
Magicpolitics1to2Dynastic8to7. ExistingScarscardexpanded7, allindividualenginesresearched, originalprint7coversQA. Structureunchanged.846/2760/6533. NextMC04998.

## MC04998-05000 Galactic Milieu whole8 -2026-11-06
Classic time agencies8to9. OnecardPliocene4+Intervention+Milieu3;each ownenginechecked. DatesJack1992/Golden1982resolved.8Englishpublisher2013reprintcoversQA. Structureunchanged.846nodes/2761fictions/6541volumes. NextMC05001.

## MC05001-05004 Rampart Worlds whole3 -2026-11-06
Spacehunt8to9;each ownengine/positiveNewancestorchecked.3EnglishprintjacketsQA. BorealrowMC05003foldedalreadyincluded.846/2762/6544. NextMC05005.

## MC05005-05009Purewhole3andshorts2026-11-06
ExistingMutantfictioncardretained,addBurn2014,all3ownengines/rootwalk/EnglishcoversQA.3Torshortsskipped.846/2762/6545. NextMC05010.

## MC05010-05012 Rivelle Realm whole3 2026-11-06
Merge Eva/Alliana cards under author-confirmed Rivelle Realm title. Whole3 ordinary Cozy peeps6->7, not merely firstbook Cozycraft or prequel Fairytaleepilogue. All own primary/completedreviews/rootwalk,3 English print jackets inspected/localized.846/2761/6545. NextMC05013.

## MC05013 Tessa Miyata whole2 2026-11-06
ExistingSlipintomythcard7unchanged,addSoUnlucky2024toNoHero2023. Bothownprimary/completedreviews,firstaccidentaldiscoveryvslaterinvitationwobbleexplicit,2EnglishprintfrontsQA.846/2761/6546. NextMC05014 NightsEdge.

## NightEdge MC05014-05017/05019 whole4 2026-11-06
OrdinaryCozypeeps7->8,4publishednovels2013/14/24/25,DragonWilliamnovellaskip,unpublishedTwistnotadded. All4ownengines/primary/completedreviews/rootwalk/EnglishcoversQA.846/2762/6550. NextMC05018TradePactuniverse.

## Clan Chronicles whole nine, 2026-11-06
Ordinary Hard alien8->9. Three shared-world trilogies; nine first publication years1997/1999/2002/2007/2008/2009/2015/2016/2017. Every volume own primary and completed review; actual root walk; nine English print fronts inspected/localized. No time travel established, dimensional teleportation not era travel.846/2763/6559. Next MC05020 Web Shifters.

## Galactic Center whole6 root repair2026-11-06
Hardalien9->8,Hardtimetravel3->4,missingGreatSkyRiver1987/SailingBrightEternity1995added. All6ownprimary/completedreviews,actualphysicsera-transferbeatsFuturist.846/2763/6561. ScopedrepairbeforeWebShifters,nobroadcorpossweep.

## Web Shifters whole6 2026-11-06
Ordinary Hard alien8->9 after Galactic Center correction. Web Shifters+Library one universe, six novels1998/2000/2003/2018/2020/2021. OnlyThingFear novella skipMC05036.846/2764/6567. NextMC05023.

## Time tangles2026-11-06
Timeslips2->3children, level7 sibling toTimebleeds/Timestrays. WholeKefahuchi3movedHardalien9->8, onefictionceiling1, ownerApprovedphonemsg-01M6RNXAQVSV7X4H28X67WFJQW actualread.847/2764/6567. Newportrait904 inspected, threeEnglishprintcoverslocalized(NovaSwinglowresolution). Noexistinggatechange; nootherfiction. Newcoinage; nearTimeTanglesingularEagar1976/TangledinTimeLaskydisclosed, noexactpluralgenreusageestablished ortrademarkclaim.
