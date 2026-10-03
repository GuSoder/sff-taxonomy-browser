import re,collections
# tree parse
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
byid={n['id']:n for n in nodes}
# confirmed duplicates: new card name -> (new leaf, orig name, orig leaf, origin 'v3'|'v1')
D=[("1632 series","ring-of-fire-and-time-travel","Ring of Fire (1632)","whole-towns-and-lives-displaced","v3")]
res=[l.rstrip('\n').split('|') for l in open('/tmp/shadow/v2/results2.txt')]
out=[];xs=[]
for name,leaf,on,ol,org in D:
    c=[n for n in nodes if n['new'] and name in n['cards'] and (not leaf or n['id']==leaf)]
    assert len(c)==1,(name,[n['id'] for n in c]); leaf=c[0]['id']
    path=[];n=byid[leaf]
    while n and n['new']: path.append(n['id']);n=n['par']
    for p in path: xs.append(f"XS|{p}|{name}")
    if org=='v3':
        hit=[f for f in res if f[0]=='C' and len(f)>4 and f[4]=='v3' and f[1]==name]
        assert len(hit)==1,(name,hit)
        hit[0][0]='+C';hit[0][1]=on;hit[0][3]=ol
        # fold lines already naming this card
        for f in res:
            if f[0]=='+C' and len(f)>4 and f[4]=='v3' and f[1]==name: f[1]=on;f[3]=ol
    else:
        # v1 card: find its result leaf
        for l in open('/tmp/shadow/results.txt'):
            f=l.rstrip('\n').split('|')
            if f[0]=='C' and f[1]==name: xs.append(f"X|{name}|{f[3]}")
open('/tmp/shadow/v2/results2.txt','w').writelines('|'.join(f)+'\n' for f in res)
open('/tmp/shadow/v2/splits2.txt','a').writelines(x+'\n' for x in xs)
print(len(xs),'removal lines')
