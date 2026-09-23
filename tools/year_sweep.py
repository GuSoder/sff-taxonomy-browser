#!/usr/bin/env python3
"""Publication-year sweep over the live tree (index.html `const nodes=`), the same
source verify_local.sh counts. One year per book: series cards use each books[] year,
single-book cards use the card year. A book seen with conflicting years keeps the latest.
Writes data/publication_years.csv (node, card, book, year) and prints a summary.
Usage: python3 tools/year_sweep.py"""
import json, csv, os, collections
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
line = next(l for l in open(os.path.join(root, 'index.html')).read().split('\n') if l.startswith('const nodes='))
nodes, _ = json.JSONDecoder().raw_decode(line.split('const nodes=', 1)[1])
def yr(v):
    try: return int(str(v)[:4])
    except (TypeError, ValueError): return None
years = {}
for n in nodes:
    for w in n.get('works') or []:
        books = w.get('books') or [{'title': w.get('title'), 'year': w.get('year')}]
        for b in books:
            k = (n['id'], str(w.get('title')), str(b.get('title')))
            y = yr(b.get('year'))
            if k not in years or (y is not None and (years[k] is None or y > years[k])): years[k] = y
os.makedirs(os.path.join(root, 'data'), exist_ok=True)
with open(os.path.join(root, 'data/publication_years.csv'), 'w', newline='') as o:
    wr = csv.writer(o); wr.writerow(['node', 'card', 'book', 'year'])
    for k in sorted(years): wr.writerow([*k, '' if years[k] is None else years[k]])
ys = [y for y in years.values() if y is not None]; mx = max(ys); cnt = collections.Counter(ys)
print(f'books: {len(years)}  with year: {len(ys)}  without year: {len(years)-len(ys)}')
print(f'min year: {min(ys)}  max year: {mx}')
print('max-year books:', '; '.join(f'{b} [{c}]' for (n, c, b), y in years.items() if y == mx))
print('per year 2010+:', ', '.join(f'{y}:{cnt[y]}' for y in range(2010, mx + 1)))
dec = collections.Counter((y // 10) * 10 for y in ys)
print('by decade:', ', '.join(f'{d}s:{dec[d]}' for d in sorted(dec) if d >= 1900), f'| pre-1900:{sum(v for d,v in dec.items() if d<1900)}')
miss = [f'{b} [{c}]' for (n, c, b), y in years.items() if y is None]
if miss: print('no year:', '; '.join(miss))
