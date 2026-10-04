import sys,re,json,os,yaml
sys.path.insert(0,'/tmp/sweep')
import xref
from collections import defaultdict
q={x['i']:x for x in json.load(open('queue.json'))}
ns={n['id']:n for n in xref.ns}
ns['slavic-myth-fantasy']={'id':'slavic-myth-fantasy','label':'Slavic myth fantasy','parent':'mythic-retelling','works':[]}
xref.ns.append(ns['slavic-myth-fantasy'])
newlabel={}
for l in open('v2/seeds2.txt'):
    f=l.rstrip('\n').split('|')
    if f[0]=='N':
        ns[f[1]]={'id':f[1],'label':f[3],'parent':f[2],'works':[],'v2':True}
        xref.ns.append(ns[f[1]])
kids=defaultdict(list)
for n in xref.ns: kids[n['parent']].append(n['id'])
def idx(s):
    o=[]
    for p in s.split(','):
        p=p.strip()
        if not p: continue
        if '-' in p:
            a,b=p.split('-');o+=range(int(a),int(b)+1)
        else:o.append(int(p))
    return o
newc=defaultdict(list); rows=defaultdict(set)
for l in list(open('results.txt'))+list(open('v2/results2.txt')):
    f=l.rstrip('\n').split('|')
    if f[0] in('C','+C') and len(f)>=4:
        rows[f[1]]|=set(idx(f[2]))
        if f[0]=='C': newc[f[3]].append(f[1])
rm=defaultdict(set)
for l in open('splits.txt'):
    f=l.rstrip('\n').split('|')
    if f[0]=='D' and len(f)>=4:
        for x in f[3].split(';'):
            if x: rm[f[1]].add(x.strip())
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
orig={}
for n in xref.ns:
    for w in n.get('works',[]):
        t=w if isinstance(w,str) else w.get('title')
        orig.setdefault(t,w)
def card(name):
    if name in rows and rows[name]:
        bs=[]
        for i in sorted(rows[name]):
            x=q.get(i)
            if x: bs.append({'title':x['title'],'author':x['author']})
        return {'name':name,'origin':'v3','books':bs}
    w=orig.get(name)
    if isinstance(w,dict):
        bs=[{'title':b['title'],'author':', '.join(w.get('authors',[]) or [])} for b in w.get('books',[])] or [{'title':name}]
        return {'name':name,'origin':'original','books':bs}
    return {'name':name,'origin':'original','books':[{'title':name}]}
genres={}
def addg(gid,label,parent,defn,names,origin):
    g={'id':gid,'label':label,'parent':parent,'origin':origin,'definition':defn or '', 'cards':[]}
    seen=[]
    for c in names:
        if c and c not in seen: seen.append(c)
    g['cards']=[card(c) for c in seen]
    genres[gid]=g
def cards(leaf):
    e=[w if isinstance(w,str) else w.get('title') for w in ns[leaf]['works']] if leaf in ns else []
    return e+[c for c in newc[leaf] if c not in rm[leaf]]
def emit_child(cid,cn,df,cs,parent):
    if cid in splits:
        addg(cid,cn,parent,df,[],'shadow-v3')
        for c2,n2,d2,cs2 in splits[cid]: emit_child(c2,n2,d2,cs2,cid)
        return
    ex=[c for c in newc[cid] if c not in rm[cid]]
    addg(cid,cn,parent,df,cs+ex,'shadow-v3')
def emit(i):
    n=ns[i]
    org='shadow-v2' if n.get('v2') else 'original'
    if kids[i]:
        addg(i,n['label'],n['parent'] if n['parent'] in ns else None,n.get('definition',''),cards(i) if i=='pulp-sword-and-sorcery' else [],org)
        for k in kids[i]: emit(k)
    elif i in splits:
        addg(i,n['label'],n['parent'],n.get('definition',''),[],org)
        for cid,cn,df,cs in splits[i]: emit_child(cid,cn,df,cs,i)
    else:
        addg(i,n['label'],n['parent'],n.get('definition',''),cards(i),org)
roots=[n['id'] for n in xref.ns if n['parent'] in (None,'','root') or n['parent'] not in ns]
for r in roots: emit(r)
out='/home/sandbox/sff-taxonomy-browser/taxonomy-shadow/2026-10-ten-k-walk-v4/genres'
os.makedirs(out,exist_ok=True)
for g in genres.values():
    open(f"{out}/{g['id']}.yaml",'w').write(yaml.safe_dump(g,sort_keys=False,allow_unicode=True,width=100))
nc=sum(len(g['cards']) for g in genres.values()); nb=sum(len(c['books']) for g in genres.values() for c in g['cards'])
print('genres',len(genres),'cards',nc,'books',nb)
