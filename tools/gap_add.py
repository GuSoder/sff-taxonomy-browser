#!/usr/bin/env python3
"""Apply one batch of gap-intake decisions (awards tier). Usage: gap_add.py batch.json
Each item: {"k":int,"title":str,"action":"add"|"merge"|"skip"|"hold", ...}
 add:   leaf, card{title,authors,year,cover_url,books?,note,sources}
 merge: leaf, into (existing card title), books[{title,year,cover_url}], note
 skip/hold: reason
Updates index.html, taxonomy yamls, gap progress.json and sweep.log (one terse line per item)."""
import json, yaml, sys, os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(R)
G = 'intake-lists/gap-2022'; TOTAL = {1: 125, 2: 322}
def slug(t): return re.sub(r'[^a-z0-9]+', '-', t.lower().replace("'", '')).strip('-')
def dump(p, o): yaml.safe_dump(o, open(p, 'w'), sort_keys=False, allow_unicode=True, width=160)
h = open('index.html').read(); lines = h.split('\n'); li = next(i for i, x in enumerate(lines) if x.startswith('const nodes='))
rest = lines[li].split('const nodes=', 1)[1]; nodes, end = json.JSONDecoder().raw_decode(rest); N = {n['id']: n for n in nodes}
def path(i):
    q = []
    while i: q.append(i); i = N[i].get('parent')
    return 'taxonomy/' + '/'.join(reversed(q))
def norm(t): return re.sub(r'[^a-z0-9]', '', (t or '').lower())
have = {norm(b.get('title')): (n['id'], w['title']) for n in nodes for w in n.get('works') or [] for b in (w.get('books') or [w])}
prog = json.load(open(G + '/progress.json')); log = open(G + '/sweep.log', 'a')
for it in json.load(open(sys.argv[1])):
    k, a, tier = it['k'], it['action'], it.get('tier', 1)
    cur = 'awards_processed' if tier == 1 else 'tier2_processed'
    prog.setdefault(cur, 0)
    if a == 'add':
        c = it['card']; leaf = N[it['leaf']]
        assert not leaf.get('children'), f'not a leaf {leaf["id"]}'
        assert len(leaf['works']) < 10, f'leaf frozen at 10: {leaf["id"]}'
        for b in c.get('books') or [c]: assert norm(b['title']) not in have or norm(b['title']) in map(norm, it.get('twin_ok', [])), f'duplicate {b["title"]} in {have.get(norm(b["title"]))}'
        w = {'title': c['title'], 'cover_url': c['cover_url'], 'shows_english_title': True, 'authors': c['authors'], 'year': c['year'], 'placement_note': c['note']}
        if c.get('books'): w['books'] = [{'title': b['title'], 'year': b['year'], 'cover_url': b['cover_url']} for b in c['books']]
        leaf['works'].append(w); cid = slug(c['title']); d = path(leaf['id']); os.makedirs(d + '/works', exist_ok=True)
        y = {'id': cid, 'title': c['title'], 'authors': c['authors'], 'first_published': c['year'], 'canonical_genre': leaf['id'], 'placement_status': 'accepted',
             'placement_rationale': c['note'], 'classification_sources': c['sources'], 'intake': f'gap-2022 awards tier #{k} ({", ".join(it.get("lists", []))})'}
        if c.get('books'): y['books'] = w['books']
        y['cover_curation'] = {'status': 'complete', 'source': c.get('cover_source', 'Open Library'), 'selected_url': c['cover_url'], 'visually_reviewed_on': '2026-09-25', 'review_method': 'contact-sheet one-pass'}
        dump(f'{d}/works/{cid}.yaml', y); g = yaml.safe_load(open(d + '/genre.yaml')); g.setdefault('works', []).append(cid); dump(d + '/genre.yaml', g)
        for b in c.get('books') or [c]: have[norm(b['title'])] = (leaf['id'], c['title'])
        prog['added'] += 1; log.write(f'{"T2 " if tier==2 else ""}{k}/{TOTAL[tier]} +{c["title"]} → {leaf["label"]}\n')
    elif a == 'merge':
        leaf = N[it['leaf']]; w = next(x for x in leaf['works'] if x['title'] == it['into'])
        if not w.get('books'): w['books'] = [{'title': w['title'], 'year': w['year'], 'cover_url': w['cover_url']}]
        for b in it['books']:
            assert norm(b['title']) not in have, f'duplicate {b["title"]}'
            w['books'].append({'title': b['title'], 'year': b['year'], 'cover_url': b['cover_url']}); have[norm(b['title'])] = (leaf['id'], w['title'])
        d = path(leaf['id']); f = next(p for p in [f'{d}/works/{slug(w["title"])}.yaml'] + [os.path.join(d, 'works', x) for x in os.listdir(d + '/works')]
                                     if os.path.exists(p) and (yaml.safe_load(open(p)) or {}).get('title') == w['title'])
        y = yaml.safe_load(open(f)); y['books'] = w['books']; y.setdefault('placement_history', []).append({'date': '2026-09-24', 'change': it['note']}); dump(f, y)
        log.write(f'{"T2 " if tier==2 else ""}{k}/{TOTAL[tier]} +{it["title"]} → {leaf["label"]} (series: {w["title"]})\n')
    else:
        log.write(f'{"T2 " if tier==2 else ""}{k}/{TOTAL[tier]} {"-" if a == "skip" else "?"}{it["title"]} ({it["reason"].split(":")[0]})\n')
        if a == 'hold': prog.setdefault('held', []).append({'tier': tier, 'k': k, 'title': it['title'], 'reason': it['reason']})
    ruling = any(x['k'] == k and x.get('tier', 1) == tier for x in prog.get('held', []))
    if ruling and a != 'hold': prog['held'] = [x for x in prog.get('held', []) if not (x['k'] == k and x.get('tier', 1) == tier)]
    else: prog[cur] = max(prog.get(cur, 0), k); prog['processed'] = prog.get('processed', 0) + 1
lines[li] = 'const nodes=' + json.dumps(nodes, ensure_ascii=False, separators=(',', ':')) + rest[end:]
open('index.html', 'w').write('\n'.join(lines)); json.dump(prog, open(G + '/progress.json', 'w'), indent=1); log.close()
print(f'awards {prog["awards_processed"]}/125, tier2 {prog.get("tier2_processed", 0)}/322, added {prog["added"]}, held {len(prog.get("held", []))}')
