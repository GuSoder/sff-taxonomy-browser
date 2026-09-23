#!/usr/bin/env python3
"""Build the 2022+ gap intake queue (Gustav 2026-09-23 "set up that sweep").
Sources (cached raw HTML in intake-lists/gap-2022/sources/, refetch with --fetch):
  sfadb.com award pages, novel categories, winners + shortlists:
    Hugo (Novel), Nebula (Novel), Arthur C. Clarke (Winner + Shortlist),
    World Fantasy (Novel), Locus Awards (Sf Novel, Fantasy Novel), BSFA (Novel)
  locusmag.com Recommended Reading lists 2022-2025, novel sections
    (SF, Fantasy, Horror, YA, First, Translated), same sections as the first intake.
Keeps books with publication (eligibility) year >= 2022. Dedupes internally, against
every book in the live tree (index.html) and against all 989 first-intake candidates
(which covers the 245 not added). Output: intake-lists/gap-2022/candidates.json,
sorted by score (number of source lists) desc, then title. Deterministic."""
import re, html, json, os, sys, glob, unicodedata, subprocess
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(R, 'intake-lists/gap-2022'); S = os.path.join(D, 'sources')
AWARDS = {'Hugo_Awards': ['Novel'], 'Nebula_Awards': ['Novel'], 'Arthur_C_Clarke_Award': ['Winner', 'Shortlist'],
          'World_Fantasy_Awards': ['Novel'], 'Locus_Awards': ['Sf Novel', 'Fantasy Novel'], 'British_SF_Association_Awards': ['Novel']}
SHORT = {'Hugo_Awards': 'Hugo', 'Nebula_Awards': 'Nebula', 'Arthur_C_Clarke_Award': 'Clarke', 'World_Fantasy_Awards': 'WFA',
         'Locus_Awards': 'LocusAward', 'British_SF_Association_Awards': 'BSFA'}
LR_URLS = {2022: 'https://locusmag.com/feature/2022-recommended-reading-list/', 2023: 'https://locusmag.com/2024/02/2023-recommended-reading-list/',
           2024: 'https://locusmag.com/2025/02/2024-recommended-reading-list/', 2025: 'https://locusmag.com/2026/02/2025-recommended-reading/'}
LR_SECTIONS = {'NOVELS – SCIENCE FICTION': 'SF', 'NOVELS – FANTASY': 'Fantasy', 'NOVELS – HORROR': 'Horror', 'YOUNG ADULT NOVELS': 'YA',
               'FIRST NOVELS': 'First', 'SCIENCE FICTION NOVELS': 'SF', 'FANTASY NOVELS': 'Fantasy', 'HORROR NOVELS': 'Horror', 'TRANSLATED NOVELS': 'Translated'}
YEARS = range(2022, 2027); MIN_PUB = 2022
def fetch():
    for a in AWARDS:
        for y in YEARS: subprocess.run(['curl', '-sL', '-A', 'Mozilla/5.0', '-o', f'{S}/{a}-{y}.html', f'https://www.sfadb.com/{a}_{y}'], check=True)
    for y, u in LR_URLS.items(): subprocess.run(['curl', '-sL', '-A', 'Mozilla/5.0', '-o', f'{S}/Locus_Recommended-{y}.html', u], check=True)
def norm(s):
    s = unicodedata.normalize('NFKD', html.unescape(s or '')).encode('ascii', 'ignore').decode().lower()
    s = re.split(r'[:(]', s)[0]; s = re.sub(r'[^a-z0-9 ]', ' ', s.replace('&', 'and')); s = re.sub(r'^(the|a|an) ', '', s.strip())
    return re.sub(r'\s+', ' ', s).strip()
def surnames(authors): return {norm(a).split()[-1] for a in authors if norm(a)}
entries = []  # (title, [authors], pub_year, source_id, winner)
def awards():
    for a, cats in AWARDS.items():
        for y in YEARS:
            f = f'{S}/{a}-{y}.html'
            if not os.path.exists(f): continue
            t = open(f, encoding='utf-8', errors='replace').read()
            m = re.search(r'Eligibility Year</b>\s*:\s*(\d{4})|Eligibility Year\s*:?\s*</?[^>]*>?\s*:?\s*(\d{4})', t)
            ey = re.search(r'Eligibility Year.{0,80}?(\d{4})', re.sub(r'<[^>]+>', ' ', t), re.S)
            pub = int(ey.group(1)) if ey else y - 1
            for blk in re.findall(r'<div class="categoryblock">(.*?)</div> <!-- categoryblock', t, re.S):
                cm = re.search(r'<div class="category">(.*?)</div>', blk, re.S)
                cat = re.sub(r'<[^>]+>', '', cm.group(1)).strip() if cm else ''
                if cat not in cats: continue
                for li in re.findall(r'<li[^>]*>(.*?)</li>', blk, re.S):
                    tm = re.search(r'<b>(.*?)</b>', li, re.S)
                    if not tm: continue
                    au = [html.unescape(x) for x in re.findall(r'<a href="[^"]*">([^<]+)</a>', li.split('</b>', 1)[1].split('(')[0])]
                    win = 'winner' in li or cat == 'Winner'
                    entries.append((html.unescape(re.sub(r'<[^>]+>', '', tm.group(1))).strip(), au, pub, f'{SHORT[a]}{y}', win))
def locus_rec():
    for y in LR_URLS:
        f = f'{S}/Locus_Recommended-{y}.html'
        t = re.sub(r'</?(li|p|br|h\d|div|ul|ol|tr|td)[^>]*>', '\n', open(f, encoding='utf-8').read())
        L = [l.strip() for l in html.unescape(re.sub(r'<[^>]+>', '', t)).split('\n') if l.strip()]
        sec = None
        for l in L:
            if l.isupper() and 3 < len(l) < 50: sec = LR_SECTIONS.get(l); continue
            if not sec: continue
            l = re.sub(r'\s*amazon\s*/\s*bookshop\s*$', '', l.replace('\xa0', ' '))
            l = re.sub(r'\s*\[\w+\]$', '', l)
            m = re.match(r'^(.+?), ([^,()]+?(?: and [^,()]+)?)(?:, tr\. [^()]+)? \((.+)\)$', l)
            if not m: continue
            au = [x.strip() for x in re.split(r' and |&', m.group(2))]
            entries.append((m.group(1).strip(), au, y, f'LocusRec{y}-{sec}', False))
def tree_keys():
    line = next(l for l in open(os.path.join(R, 'index.html'), encoding='utf-8').read().split('\n') if l.startswith('const nodes='))
    nodes, _ = json.JSONDecoder().raw_decode(line.split('const nodes=', 1)[1]); keys = {}
    for n in nodes:
        for w in n.get('works') or []:
            for b in (w.get('books') or [w]) + [w]: keys.setdefault(norm(b.get('title')), []).append((surnames(w.get('authors') or []), n['id'], w.get('title')))
    return keys
if __name__ == '__main__':
    if '--fetch' in sys.argv: fetch()
    awards(); locus_rec()
    raw = len(entries); tk = tree_keys()
    first = {}
    for c in json.load(open(os.path.join(R, 'intake-lists/candidates.json'))): first.setdefault(norm(c['title']), []).append(surnames([c['author']]))
    q = {}
    for t, au, pub, src, win in entries:
        if pub < MIN_PUB: continue
        k = norm(t); sn = surnames(au)
        key = next((kk for kk in q if kk[0] == k and (q[kk]['_sn'] & sn or not sn)), None) or (k, tuple(sorted(sn)))
        e = q.setdefault(key, {'title': t, 'author': ' & '.join(au), 'year': pub, 'lists': [], 'winner_of': [], '_sn': set(sn)})
        e['_sn'] |= sn; e['year'] = min(e['year'], pub)
        if src not in e['lists']: e['lists'].append(src)
        if win and src not in e['winner_of']: e['winner_of'].append(src)
    out, in_tree, in_first, review = [], [], [], []
    for (k, _), e in q.items():
        sn = e.pop('_sn'); hit = [x for x in tk.get(k, []) if x[0] & sn]
        if hit: in_tree.append(f"{e['title']} -> {hit[0][1]}/{hit[0][2]}"); continue
        if any(s & sn for s in first.get(k, [])): in_first.append(e['title']); continue
        if k in tk: e['review'] = f'title matches tree card {tk[k][0][2]} ({tk[k][0][1]}) with different author'
        e['score'] = len(e['lists']); out.append(e)
    out.sort(key=lambda e: (-e['score'], -len(e['winner_of']), e['title'].lower()))
    for i, e in enumerate(out, 1): e['n'] = i
    json.dump(out, open(os.path.join(D, 'candidates.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump({'raw_entries': raw, 'unique_2022plus': len(q), 'already_in_tree': sorted(in_tree), 'in_first_intake': sorted(in_first)},
              open(os.path.join(D, 'dedupe-report.json'), 'w'), ensure_ascii=False, indent=1)
    pf = os.path.join(D, 'progress.json')
    if not os.path.exists(pf): json.dump({'next': 1, 'processed': 0, 'added': 0, 'held': []}, open(pf, 'w'), indent=1)
    print(f'raw entries {raw}; unique 2022+ {len(q)}; already in tree {len(in_tree)}; in first intake {len(in_first)}; queue {len(out)}')
