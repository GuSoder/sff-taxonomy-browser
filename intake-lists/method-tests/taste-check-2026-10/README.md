# Taste check, 2026-10 (method test only; no tree changes, no intake)

Question: are the imprints in the imprint sweep the ones taste-makers (bloggers, BookTubers) actually praise?

## Sample
- Bloggers: 140 usable pages (144 URLs) from Fantasy Hive, Grimdark Magazine, Book Riot, Reactor, Fantasy Book Critic, SFFWorld, Nerd's Feather, Fantasy-Literature, Book Smugglers, Locus, Tor.com, Nerd Daily, Fantasy Inn, SF Book. Mostly 2025 year-end and best-of lists, plus some anticipated-2026 lists.
- BookTubers: 68 watch pages, 59 with usable transcripts (9 under 1.5 KB). `srcs.json` lists every URL.
- Fetched page text is in `pages/` (md5 of URL as filename).

## Extraction
1. `ext.py`: regex for "Title by Author" over all pages, about 1,800 noisy candidates (`mentions.json`).
2. `pub.py`: kept titles on 2+ pages (137), looked up Open Library (`ol.json`). It returned nothing for ~50.
3. `tally.py`: 67 real SFF books were hand-cleaned and given a publisher/imprint by hand (dict `M`), using Open Library hints plus own knowledge. Mentions were then counted by searching those titles in all pages. Output in `tally-output.txt`.

## Caveats
- 2025 skew and English-language blogs only.
- 67-book base: top of the ranking is solid, the long tail is not.
- Imprint is a manual assignment; US/UK split titles (Bennett, Tchaikovsky, Fawcett) are judgment calls.
- Transcripts are YouTube auto-captions, so spelling is loose and some titles are missed. yt-dlp was bot-blocked; web_fetch on watch URLs worked. Google Books API gave 429.
- Counts are page-mentions, not readers.
- Books that appear in transcripts without "by Author" are missed.

## Tally (page-mentions of the 67 books)
| Group | Bloggers | YouTube |
|---|---|---|
| Macmillan/Tor | 132 | 30 |
| Hachette (Orbit, Gollancz) | 68 | 34 |
| PRH (Del Rey, DAW, Berkley, Viking) | 57 | 19 |
| HarperCollins (Voyager, Morrow) | 35 | 13 |
| S&S (Saga) | 5 | 1 |

Imprints, bloggers: Tordotcom 67, Tor 52, Orbit 47, Del Rey 33, Harper Voyager 21, Gollancz 15, Morrow 9, DAW 6, Berkley 6.
Imprints, YouTube: Orbit 19, Tordotcom 14, Del Rey 13, Gollancz 12, Tor/Tordotcom 10, Harper Voyager 7, Tor 6.

## Verdict vs sweep
- Validated: Tor/Tordotcom, Orbit, Gollancz, Harper Voyager.
- Not swept but praised: the PRH family (Del Rey, DAW, Berkley), also Saga, Viking, Bloomsbury, FSG. Baen got nothing.
- Reordering: taste ranks Tor > Orbit+Gollancz > PRH/Del Rey > Harper Voyager. Titan, Angry Robot, Solaris and Tachyon barely register, so bulk yield overstates them.
