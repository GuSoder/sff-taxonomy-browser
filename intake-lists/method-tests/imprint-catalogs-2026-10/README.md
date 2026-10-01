# Imprint-catalog sourcing method test (2026-10-02)

Owner-commissioned test (spec: compile SF/fantasy books 1990-today from big SFF imprints' own catalog pages, fields title/author/year only, no per-book lookups, no gap-filling from other sources; cross-reference the tree; report how long the new list is).

## What the file is
`titan_candidates_not_in_tree.tsv` - 2,195 rows (title, author, year), sorted by year descending. These are CANDIDATES, not confirmed new SFF books.

- Source: titanbooks.com/catalog, pages 1-295 ("3,537 results"). 3,444 rows parsed; ~90 listed results not parsed.
- Mixed genre: Titan also publishes crime, horror, comics, games and film/TV books. The catalog has no genre field and none was looked up.
- Year is the release date of the listed edition. For reprints, tie-ins and reissues it may not be the first publication year.
- Rows dated 2027+ (65) were dropped as announcements. Window kept: 1990-2026.
- 695 unique rows were dropped by title keyword as non-fiction/tie-ins (Art of, Making of, Official, Guide, etc.). That filter is crude; some rows left may still be non-fiction and some dropped may be fiction.
- Cross-reference with the tree (index.html as of commit f9c19a3, 2,370 books) was by normalized TITLE ONLY (lowercase, no punctuation, leading article and parentheticals removed). Author was not compared, so a same-title different book could hide a real new row (false match) and edition-title differences could leave a row listed as new that is already in the tree.
- Numbers: 3,376 rows in window, 2,965 unique title+author, 76 in tree, 2,889 not in tree, 2,195 after the keyword drop. Decades of the 2,195: 1990s 2, 2000s 179, 2010s 1,244, 2020-26 770. The catalog barely reaches before 2010.

## Per-imprint usability (plain web fetch, no browser)
Test criterion: title, author and year directly on the imprint's own catalog pages.

- Titan: usable. Titles, authors, format, release date on listing pages, 295 pages.
- Baen (/allbooks): titles and authors, no year; page parameter ignored (same first page for p=2, p=60); mostly eARCs.
- Angry Robot (/books): 14 pages, titles and authors, no year.
- Gollancz (store.gollancz.co.uk/collections/all): titles and prices, no author or year in the listing; Masterworks collection URL not found.
- Tachyon (/shop/books): titles and authors, no year (year appears only in image upload paths, not a catalog field).
- Orbit (hachettebookgroup.com/imprint/orbit): recent titles only, no authors/years, pagination returned a similar page.
- Harper Voyager (harpercollins.com collection): blurb page only.
- Solaris: social-media feed, no catalog.
- Tor/Tor.com (Macmillan): search page returned empty (JS-rendered).
- Del Rey, Ace (PRH), DAW (dawbooks.com), Saga (S&S): URLs tried returned not found or timed out. Not tried with a browser, so "unreachable by plain fetch", not proven unusable.

Per-imprint yield (candidates / in tree / new): Titan 3,376 / 76 / 2,889 (2,195 after keyword drop); all others 0.

No book research, intake, or tree changes were done from this list.
