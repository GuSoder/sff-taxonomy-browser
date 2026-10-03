import re,json,collections,sys
APPLY=len(sys.argv)>1
q=json.load(open('/tmp/shadow/queue.json'))
nodes=[];cur=None
for l in open('/tmp/shadow/v2/shadow-tree.txt'):
    s=l.strip();d=(len(l)-len(l.lstrip()))//2
    m=re.match(r'\[([a-z0-9-]+)\]\s*(.*)',s)
    if m: cur={'d':d,'id':m[1],'new':'NEW' in m[2],'cards':[],'par':None};nodes.append(cur)
    elif s.startswith('- ') and cur: cur['cards'].append(s[2:].strip())
st=[]
for n in nodes:
    while st and st[-1]['d']>=n['d']: st.pop()
    n['par']=st[-1] if st else None; st.append(n)
cnt=collections.Counter(c for n in nodes if n['new'] for c in set(n['cards']))
dupn={c for c,v in cnt.items() if v>1}
# also same-leaf double
def idx(s): return [int(x) for x in s.split(',') if x.strip().isdigit()]
lines=[]
for fn,tag in (('/tmp/shadow/results.txt','v1'),('/tmp/shadow/v2/results2.txt','v3')):
    for i,l in enumerate(open(fn)):
        f=l.rstrip('\n').split('|')
        if f[0]=='C' and len(f)>3 and f[1] in dupn: lines.append((tag,i,f[1],idx(f[2]),f[3]))
by=collections.defaultdict(list)
for x in lines: by[x[2]].append(x)
res=[l.rstrip('\n').split('|') for l in open('/tmp/shadow/v2/results2.txt')]
xs=[];plan=[]
for name,L in by.items():
    if len(L)<2: 
        plan.append((name,'single C line; render dup from split lists',[x[4] for x in L])); continue
    au=[set(q[i]['author'] for i in x[3][:4] if i<len(q)) for x in L]
    same=all(a&au[0] for a in au)
    if not same: plan.append((name,'DIFFERENT authors',[(x[4],sorted(a)[:2]) for x,a in zip(L,au)]));continue
    keep=max(L,key=lambda x:len(x[3]))
    plan.append((name,'MERGE keep '+keep[0]+':'+keep[4],[(x[0],x[4],len(x[3])) for x in L if x is not keep]))
    if APPLY:
        for x in L:
            if x is keep: continue
            if x[0]=='v3':
                f=res[x[1]]; f[0]='+C'; f[3]=keep[4]
            else: print('v1 non-keeper skipped',name)
for p in plan: print(p)
if APPLY:
    open('/tmp/shadow/v2/results2.txt','w').writelines('|'.join(f)+'\n' for f in res)

if APPLY:
    kids=collections.defaultdict(list)
    for n in nodes:
        if n['par']: kids[n['par']['id']].append(n)
    def desc(n):
        o=[n]
        for k in kids[n['id']]: o+=desc(k)
        return o
    byid={n['id']:n for n in nodes}
    out=[]
    for name,why,info in plan:
        if name=='Damsel' or why=='DIFFERENT authors': continue
        if why.startswith('MERGE'): kleaf=why.split(':')[1]
        else: kleaf=info[0]
        has=[n for n in nodes if n['new'] and name in n['cards']]
        kn=set(id(x) for x in desc(byid[kleaf])) if kleaf in byid else set()
        keepn=[n for n in has if id(n) in kn]
        if len(has)>1 and len(keepn)>=1:
            for n in has:
                if id(n) not in kn: out.append(f"XS|{n['id']}|{name}")
        else: print('no keeper node',name,kleaf,[n['id'] for n in has])
    open('/tmp/shadow/v2/splits2.txt','a').writelines(x+'\n' for x in out)
    print(len(out),'XS lines')
