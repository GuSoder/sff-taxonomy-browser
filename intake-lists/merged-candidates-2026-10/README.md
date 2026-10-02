# Merged candidate list, 2026-10 (analysis only; no intake, no tree changes)

`candidates.tsv`: one row per candidate book not already in the tree. 11,969 rows: **10,069 non-Titan** plus 2,029 Titan-only rows flagged `low_conf_genre=1` (Titan is mixed genre; roughly half is SFF).
Columns: id, title, author, year (earliest known, many sources have none), imprints, sources (provenance, every source that listed it), n_sources, genre_tags, series, tree_status, low_conf_genre, notes.

## Sources (provenance)
- Macmillan/Tor: Macmillan Algolia backend, Fantasy/SF category, 1990-2026 (`imprint-sweep-2026-10/tor_new.json`).
- Hachette site search, 12 keywords (`hbg_all.json`); keyword search, so not genre-pure.
- Gollancz: store.gollancz.co.uk/products.json re-harvested for tags; rows kept only with BISAC FIC009/FIC028 or Fantasy/SF tags.
- Harper Voyager: harpercollins.com collection JSON.
- PRH: Del Rey, Ace, DAW, Spectra via randomhousebooks.com list-title API (`prh-baen-probe-2026-10`).
- Baen: category pages (`prh-baen-probe-2026-10`).
- Titan: `imprint-catalogs-2026-10`, flagged low confidence.
Not included: Random House Worlds, Berkley, Ballantine, Bantam, Tachyon, Angry Robot, Rebellion (small or mixed).

## Dedupe and tree match (method)
- Title cleaned (edition words, eARC suffix, parentheticals), normalized (lowercase, no punctuation, leading article dropped). Author normalized to surname plus first initial of the first credited person.
- Dedupe across sources on title+author surname. Rows with no author (Gollancz or Harper where the author could not be derived) merge into an authored row with the same title when one exists.
- Tree match: title in the tree (any card or book) AND author surname among that card's authors = `in_tree`, removed from the list. Same title with a different author stays in the list as `title_collision_diff_author` (75 rows). Cards with no author data count as matches.
- Dropped as non-novels: 389 rows (box sets, bundles, calendars, omnibus, volumes, art books and similar title patterns).

## Caveats
- Gollancz authors come from product tags: a tag is accepted only if its surname appears elsewhere (other sources or the tree); else flagged `UNVERIFIED`. Harper authors come from URL slugs. 198 rows have no author.
- Hachette, Harper and Gollancz carry no first-publication year. Many Baen rows are eARC or free-library items; some non-SFF and kids' books remain (Hachette keyword search, Titan).
- Series installments are separate rows, the tree holds series as multi-book cards, so row count is not comparable to the tree's book count without series collapse.
- Anthologies and media tie-ins are included unless matched by the non-novel patterns.
