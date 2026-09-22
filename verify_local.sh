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
print(f'OK: script parses, {len(nodes)} nodes, {cards} cards / {books:,} books, refs consistent')
PY
