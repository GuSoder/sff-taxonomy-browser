# Imprint sweep for the 10K goal (2026-10-02)

Method test, owner-commissioned: which publisher/imprint catalogs can supply names of works (title only matters) to reach 10K books. No per-book research, no intake, no tree changes. Cross-reference was against index.html at commit b6836b4 (2,370 books).

## Files
- `tor_raw.json` - Tor Publishing Group rows from Macmillan US search backend (7,332 format-level rows, 1981-2027; fields title, contributorByLine, publicationDate epoch, hierarchicalCategories, format, imprint, isbn13, series).
- `tor_new.json` - Fantasy + Science Fiction titles (1990-2026, audio dropped, deduped by title+author) not in the tree: 2,578.
- `hbg_all.json` - Hachette site-search harvest: 1,922 unique titles keyed by ISBN-13 as [isbn, title, contributors]; 12 keywords (orbit, fantasy, science fiction, epic fantasy, space opera, dystopian, urban fantasy, dragon, wizard, time travel, alien, post-apocalyptic).
- `gol_titles.json` - 1,404 Gollancz product titles (store.gollancz.co.uk/products.json).
- `harper_voyager_titles.json` - 795 products from harpercollins.com collection harper-voyager (title, vendor, handle).
- `hbg.py` (Hachette harvester), `alg.py` (Macmillan query helper), `xref.py` (tree matcher).
- Titan results from the earlier test: ../imprint-catalogs-2026-10/.

## Numbers (new unique title strings vs tree, before genre cleanup)
Tor ~2,550; Hachette ~1,750; Harper Voyager ~680; Gollancz ~1,100 (960 not overlapping the others). Union of these four ~5,930. Titan adds ~2,170 but is mixed genre.

## Caveats
- Matching is by normalized TITLE ONLY (lowercase, no punctuation, leading article/parentheticals dropped). Author is not compared: same-title different books are false matches; edition-title variants stay "new".
- Series installments count as separate titles; the tree holds series as multi-book cards, so "10K" in title strings is not the same unit as the tree's book count.
- Edition/duplicate rows remain (special/collector/deluxe editions partly stripped by title pattern for Harper). Tor rows are per format, deduped by title+author using the earliest publication date.
- Years: only Tor has a publication date. Hachette, Harper, Gollancz (published_at is the web listing date, not the book year), Tachyon, Angry Robot and Titan edition dates give no reliable first-publication year. 1990-2017 reach cannot be verified for those sources.
- Genre: only Tor (category field) and Gollancz (BISAC/genre tags) carry a genre field. Hachette results are keyword search over the whole group (about 80% adult SFF in a 28-title sample; kids, romance, celebrity titles mixed in). Harper collection is Voyager-only but includes special editions.
- Tor: 856 rows have no genre category; they were left out of the Fantasy+SF count.
- Macmillan embedded key: us.macmillan.com's own search page embeds a public search-only key for its search backend (Algolia) and its front-end calls it directly. I called that same backend from a script at low volume (about 30 queries), not through a browser. The key is deliberately not stored in this repo. alg.py has the key redacted (it is in the us.macmillan.com page source as supafolioSettings); decide whether a full harvest should keep using it.

## Per-imprint access notes
Plain fetch via script: Tor (Macmillan backend), Hachette (/?s=kw&post_type=title, /page/N/), Harper Voyager (Shopify collection JSON), Gollancz (Shopify JSON), Tachyon (WooCommerce store API, 240 products), Titan (HTML pages).
web-fetch tool only (direct HTTP 403): Angry Robot (14 pages, title+author, no year).
Partial: Baen (/allbooks first page only, paging ignored); Rebellion/Solaris (shop.rebellion.com JSON, vendor "publishing" about 300, mixed with comics).
Browser-only, not harvested: Penguin Random House family (Del Rey, Ace, DAW, Roc, Berkley), search page renders in JS, no imprint filter or year.
Unusable: Subterranean, Small Beer, PS Publishing (no catalog listing found), Prometheus/Pyr, Head of Zeus, Black Library (blocked/Cloudflare), Pan Macmillan Tor UK (URL 404, one URL tried), Jo Fletcher Books (domain serves unrelated gambling site).
