# Candidate queue 2026-09-12 (1000-book goal)

`candidates-2026-09-12.json` is the active intake queue for Gustav's 2026-09-12 work order: grow the taxonomy toward 1000 books from published best-of lists.

- 989 unique candidates (updated same day with modern-decade lists), pre-sorted by list frequency (score = number of source lists citing the book).
- Fields: title, author, score, lists (source list ids).
- Normalized on title+author (subtitle-insensitive); deduplicated within the queue; 85 books already on the site (132 works) were weeded out.
- Sources: 24 ranked lists harvested from sfadb.com static pages (Guardian1000, NPR2011, NPR2021, Amazon SF/SFF/Millennium, Pringle 100 Best SF, Pringle Modern Fantasy, Locus 1975/1987/1998/2012 polls incl. 21st-century SF, 501 Must-Read, 1000 Books, 1001 Books, CoreList400) plus Locus Recommended Reading annual lists 2011-2024 (10 years: 2011, 2012, 2015, 2017-2021, 2023, 2024; sections SF/Fantasy/YA/First/Horror novels only; 348 raw entries, 340 new).
- 989 >= the 868 needed for the 1000-book goal, with margin for skips.
- Processing order = file order. The Sep 11 cursor-based pipeline (README.md, coverage.yaml, pending-batch.yaml) predates this queue and is parked; this queue drives intake until exhausted.