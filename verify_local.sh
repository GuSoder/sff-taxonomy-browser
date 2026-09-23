#!/bin/bash
# Pre-push gate: index.html must pass before any git push.
# 1) Full inline <script> body must parse as valid JS (catches truncated lines).
# 2) const nodes array must JSON-decode and report fiction-card and individual-book counts.
set -e
cd "$(dirname "$0")"
python3 - <<'PY'
import json,re,sys,subprocess,tempfile,os
html=open('index.html').read()
m=re.search(r'<script>(.*)</script>',html,re.S)
if not m:
    sys.exit('FAIL: no inline script block found')
js=m.group(1)
with tempfile.NamedTemporaryFile('w',suffix='.js',delete=False) as f:
    f.write(js); path=f.name
r=subprocess.run(['node','--check',path],capture_output=True,text=True)
os.unlink(path)
if r.returncode!=0:
    print(r.stderr); sys.exit('FAIL: inline script does not parse')
line=[l for l in html.split('\n') if l.startswith('const nodes=')][0]
nodes,end=json.JSONDecoder().raw_decode(line.split('const nodes=',1)[1])
tail=line.split('const nodes=',1)[1][end:]
if not tail.startswith(', by='):
    sys.exit('FAIL: inline JS tail after nodes array missing/truncated')
cards=sum(len(n.get('works',[])) for n in nodes)
books=sum(len(w.get('books',[])) if w.get('books') else 1 for n in nodes for w in n.get('works',[]))
ids=[n['id'] for n in nodes]
assert len(ids)==len(set(ids)), 'FAIL: duplicate node ids'
byid={n['id']:n for n in nodes}
for n in nodes:
    for c in n.get('children',[]):
        assert c in byid, f'FAIL: dangling child {c} on {n["id"]}'
    p=n.get('parent')
    assert p is None or p in byid, f'FAIL: dangling parent on {n["id"]}'
KNOWN={'dynastic-intrigues'}  # pre-existing, surfaced to Gustav 2026-09-23 02:59
haskids={n.get('parent') for n in nodes}
bad=[n['id'] for n in nodes if n.get('works') and n['id'] in haskids]
new=[b for b in bad if b not in KNOWN]
assert not new, f'FAIL: cards on non-leaf nodes {new}'
if bad: print('WARN: known pure-branch violations pending decision:',bad)
import glob as _g, yaml as _y
def _p(i):
    q=[]
    while i: q.append(i); i=byid[i].get('parent')
    return 'taxonomy/'+'/'.join(reversed(q))
_miss=[]
for n in nodes:
    wd=_p(n['id'])+'/works/'
    if not __import__('os').path.exists(_p(n['id'])+'/genre.yaml'): _miss.append(('genre',n['id']))
    have=set()
    for f in _g.glob(wd+'*.yaml'):
        try:
            _d=_y.safe_load(open(f)) or {}; have.add(_d.get('title')); have.add(('id',_d.get('id')))
        except Exception: _miss.append(('unparseable',f))
    for w in n.get('works',[]):
        if w['title'] not in have and ('id',w.get('id') or __import__('re').sub(r'[^a-z0-9]+','-',w['title'].lower()).strip('-')) not in have: _miss.append(('work',n['id'],w['title']))
KNOWN_PARITY=set()
_new=[m for m in _miss if m not in KNOWN_PARITY]
assert not _new, f'FAIL: YAML mirror parity {len(_new)}: {_new[:5]}'
if _miss: print('WARN: known parity gaps pending decision:',_miss)
print(f'OK: script parses, {len(nodes)} nodes, {cards} cards / {books:,} books, refs consistent')
PY
