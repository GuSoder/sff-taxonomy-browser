import sys,re
sys.path.insert(0,'/tmp/sweep')
import xref
from collections import defaultdict
ns={n['id']:n for n in xref.ns}
ns['slavic-myth-fantasy']={'id':'slavic-myth-fantasy','label':'Slavic myth fantasy (NEW)','parent':'mythic-retelling','works':[]}
xref.ns.append(ns['slavic-myth-fantasy'])
for l in open('v2/seeds2.txt'):
    f=l.rstrip('\n').split('|')
    if f[0]=='N':
        ns[f[1]]={'id':f[1],'label':f[3]+' (NEW v2)','parent':f[2],'works':[]}
        xref.ns.append(ns[f[1]])
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
for l in list(open('results.txt'))+list(open('v2/results2.txt')):
    f=l.rstrip('\n').split('|')
    if f[0] in('C','+C') and len(f)>=4:
        placed|=set(idx(f[2]))
        if f[0]=='C': newc[f[3]].append(f[1])
        else: folds+=1
    elif f[0]=='H': held|=set(idx(f[1]))
held-=placed
dead=set();rm=defaultdict(set)
for l in list(open('splits.txt')):
    f=l.rstrip('\n').split('|')
    if f[0]=='D' and len(f)>=4:
        for x in f[3].split(';'):
            if x: rm[f[1]].add(x.strip())
        if f[2].startswith('(remove'): pass
splits=defaultdict(list)
for l in list(open('splits.txt'))+list(open('v2/splits2.txt')):
    f=l.rstrip('\n').split('|')
    if f[0]=='S': splits[f[1]].append((f[2],f[3],f[4],f[5].split(';')))
for l in open('v2/splits2.txt'):
    f=l.rstrip('\n').split('|')
    if f[0]=='XS':
        for par,ents in splits.items():
            for e in ents:
                if e[0]==f[1] and f[2] in e[3]: e[3].remove(f[2])
    elif f[0]=='X':
        if f[1] in newc[f[2]]: newc[f[2]].remove(f[1])
def cards(leaf):
    e=[w if isinstance(w,str) else w.get('title') for w in ns[leaf]['works']] if leaf in ns else []
    nn=[c for c in newc[leaf] if c not in rm[leaf]]
    return e+nn
def emit_child(cid,cn,cs,d):
    global nleaf,ncards
    if cid in splits:
        out.append('  '*d+f'[{cid}] {cn} NEW (umbrella, 0 direct cards, split in shadow)')
        for c2,n2,d2,cs2 in splits[cid]: emit_child(c2,n2,cs2,d+1)
        return
    ex=[c for c in newc[cid] if c not in rm[cid]]
    allc=[]
    for c in cs+ex:
        if c not in allc: allc.append(c)
    nleaf+=1;ncards+=len(allc)
    out.append('  '*d+f'[{cid}] {cn} NEW ({len(allc)})')
    for c in allc: out.append('  '*(d+1)+'- '+c)
out=[];nleaf=0;ncards=0
def emit(i,d):
    global nleaf,ncards
    n=ns[i]
    if kids[i]:
        out.append('  '*d+f'[{i}] {n["label"]}')
        if i=='pulp-sword-and-sorcery':
            for w in cards(i): out.append('  '*(d+1)+'- '+w)
            ncards+=len(cards(i))
        for k in kids[i]: emit(k,d+1)
    elif i in splits:
        out.append('  '*d+f'[{i}] {n["label"]}  (umbrella, 0 direct cards, split in shadow)')
        for cid,cn,df,cs in splits[i]:
            emit_child(cid,cn,cs,d+1)
    else:
        cs=cards(i);nleaf+=1;ncards+=len(cs)
        out.append('  '*d+f'[{i}] {n["label"]} ({len(cs)})')
        for c in cs: out.append('  '*(d+1)+'- '+c)
roots=[n['id'] for n in xref.ns if n['parent'] in (None,'','root') or n['parent'] not in ns]
for r in roots: emit(r,0)
# slavic
txt='\n'.join(out)
open('v2/shadow-tree.txt','w').write(txt+'\n')
print('roots',len(roots),'leaves',nleaf,'cards',ncards,'placed works',len(placed),'held',len(held),'newcards',sum(len(v) for v in newc.values()),'folds',folds)
over=[l for l in out if re.search(r'\((1[1-9]|[2-9]\d)\)$',l)]
print('leaves >10:',over[:10])
