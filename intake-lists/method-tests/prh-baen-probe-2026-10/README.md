# PRH family and Baen catalog probe, 2026-10 (method test only; no tree changes, no intake)

## Result: both are scriptable. No browser needed for data.
### Penguin Random House (Del Rey, Ace, DAW, Random House Worlds, Spectra, Ballantine, Bantam, Berkley, Inklore)
- penguinrandomhouse.com is JS-rendered, but the sister site randomhousebooks.com (PRH's own consumer site, linked from penguinrandomhouse.com/imprints/) exposes a public WordPress REST API that its own pages call: `POST https://randomhousebooks.com/wp-json/dwt/v2/list-title` with JSON `{"imprintCode":"DR","rows":100,"start":0}`. It pages at 100 rows and returns recordCount, title, subtitle, author(s), onsale date, series, ISBN. No key needed; plain curl/Python works.
- Imprint codes were found by scanning 2-char and 100-299 codes and resolving each through `single-title` (codes.json, 673 non-empty). Used: DR Del Rey, A0/A8/A9 Ace (family Berkley), 161 DAW, 142 Random House Worlds, 1R Spectra, 181 Inklore, BB/R2 Ballantine, 1A Bantam, AA/B0/CZ/AQ Berkley. Roc has no standalone code; Roc-labelled titles appear under Ace/Berkley (and "Roc Lit 101" is a tiny YA imprint). Other Berkley codes (AK, AV, X3, CJ) and Dell, Penguin, Putnam, Viking, Harmony were not harvested.
- Harvested 17,223 rows, 16,637 unique title+first author (prh_titles.json, prh_unique.json).
### Baen
- baen.com/allbooks renders in JS, but the category page is server-rendered and pages by `?page=N`: `https://www.baen.com/allbooks/category/index/id/1972/options/available?page=N`, 20 books a page, 80 real pages, then it wraps. Fields: title, author, release date, URL. 1,964 raw rows, 1,524 unique URLs, 1,514 unique titles (baen_titles.json). Includes eARC duplicates, bundles and some non-novel items.

## Numbers (unique title+author, NEW = title not in tree, title-only matching)
| Imprint | Unique | New vs tree | By authors already in tree | Years |
|---|---|---|---|---|
| Del Rey | 994 | 826 | 517 (52%) | 1979-2027; <2000: 161, 2000-17: 505, 2018+: 328 |
| Ace (3 codes) | 1,271 | 1,166 | 285 (22%) | 1985-2027; 63 / 911 / 297 |
| DAW | 766 | 697 | 168 (21%) | 1982-2027; 90 / 362 / 314 |
| Random House Worlds | 698 | 692 | 137 (19%) | 1986-2027; 34 / 264 / 400 |
| Spectra | 247 | 229 | 81 (32%) | 1961-2015; 69 / 178 / 0 |
| Inklore | 85 | 85 | 0 | 2007-2027, almost all 2018+ |
| Baen | 1,514 | 1,483 | 222 (15%) | 1991-2026; <2000: 21, 2000-17: 1,153, 2018+: 340 |
| Ballantine (mixed) | 3,224 | 3,186 | 93 (3%) | 1978-2027 |
| Bantam (mixed) | 2,102 | 2,077 | 40 (2%) | 1957-2027 |
| Berkley (mixed, romance/thriller) | 7,250 | 7,179 | 85 (1%) | 1950-2027 |

SFF-pure imprints (Del Rey, Ace, DAW, Spectra, Baen): about 4,200 new titles before cleanup. Ballantine, Bantam and Berkley are mostly non-SFF.

## Caveats
- No genre field is exposed by the PRH or Baen listings (categories come back null), so genre purity is by imprint nature plus a proxy: share of titles whose first author already appears in the tree (865 authors). The proxy underestimates purity, since the tree is small.
- Title-only matching. Series installments, audiobook and ebook reissues and box sets count separately. Del Rey/Ace include licensed and media tie-ins.
- The browser was only used to find endpoints; the data came from plain HTTP.
- randomhousebooks.com was flagged once by an automated check as a "domain mismatch" with penguinrandomhouse.com; it is PRH's own site (linked from PRH's imprints page). The API was used only for read-only catalog lookups.
