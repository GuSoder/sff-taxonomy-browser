import sys,re
sys.path.insert(0,'/tmp/sweep')
import xref
from collections import defaultdict
ns={n['id']:n for n in xref.ns}
ns['slavic-myth-fantasy']={'id':'slavic-myth-fantasy','label':'Slavic myth fantasy (NEW)','parent':'mythic-retelling','works':[]}
xref.ns.append(ns['slavic-myth-fantasy'])
kids=defaultdict(list)
for n in xref.ns: kids[n['parent']].append(n['id'])
newc=defaultdict(list); 
def idx(s):
    o=[]
    for p in s.split(','):
        p=p.strip()
        if not p: continue
        if '-' in p:
            a,b=p.split('-');o+=range(int(a),int(b)+1)
        else:o.append(int(p))
    return o
placed=set();held=set();folds=0
for l in open('results.txt'):
    f=l.rstrip('\n').split('|')
    if f[0] in('C','+C') and len(f)>=4:
        placed|=set(idx(f[2]))
        if f[0]=='C': newc[f[3]].append(f[1])
        else: folds+=1
    elif f[0]=='H': held|=set(idx(f[1]))
held-=placed
dead=set();rm=defaultdict(set)
for l in open('splits.txt'):
    f=l.rstrip('\n').split('|')
    if f[0]=='D' and len(f)>=4:
        for x in f[3].split(';'):
            if x: rm[f[1]].add(x.strip())
        if f[2].startswith('(remove'): pass
splits=defaultdict(list)
for l in open('splits.txt'):
    f=l.rstrip('\n').split('|')
    if f[0]=='S': splits[f[1]].append((f[2],f[3],f[4],f[5].split(';')))
def cards(leaf):
    e=[w if isinstance(w,str) else w.get('title') for w in ns[leaf]['works']] if leaf in ns else []
    nn=[c for c in newc[leaf] if c not in rm[leaf]]
    return e+nn
out=[];nleaf=0;ncards=0
def emit(i,d):
    global nleaf,ncards
    n=ns[i]
    if kids[i]:
        out.append('  '*d+f'[{i}] {n["label"]}')
        for k in kids[i]: emit(k,d+1)
    elif i in splits:
        out.append('  '*d+f'[{i}] {n["label"]}  (umbrella, 0 direct cards, split in shadow)')
        for cid,cn,df,cs in splits[i]:
            out.append('  '*(d+1)+f'[{cid}] {cn} NEW ({len(cs)})')
            nleaf+=1;ncards+=len(cs)
            for c in cs: out.append('  '*(d+2)+'- '+c)
    else:
        cs=cards(i);nleaf+=1;ncards+=len(cs)
        out.append('  '*d+f'[{i}] {n["label"]} ({len(cs)})')
        for c in cs: out.append('  '*(d+1)+'- '+c)
roots=[n['id'] for n in xref.ns if n['parent'] in (None,'','root') or n['parent'] not in ns]
for r in roots: emit(r,0)
# slavic
txt='\n'.join(out)
open('shadow-tree.txt','w').write(txt+'\n')
print('roots',len(roots),'leaves',nleaf,'cards',ncards,'placed works',len(placed),'held',len(held),'newcards',sum(len(v) for v in newc.values()),'folds',folds)
over=[l for l in out if re.search(r'\((1[1-9]|[2-9]\d)\)$',l)]
print('leaves >10:',over[:10])
