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
D=[("Beautiful Creatures","vampire-courts","Beautiful Creatures","suburban-gothic","v3"),
("Incarnations of Immortality","possessed-and-tormented","Incarnations of Immortality","modern-invented-myth","v3"),
("Locked Tomb","ghost-roads-and-hauntings","The Locked Tomb","technomancy","v3"),
("Noble Dead Saga","riders-and-wolfwalkers","Noble Dead Saga","vampire-hunt","v3"),
("Renshai","renshai-and-kingkillers","Renshai","norse-fantasy","v3"),
("Kingkiller Chronicle","renshai-and-kingkillers","The Kingkiller Chronicle","bard-hero","v3"),
("Emberverse","stackpole-and-throne-cycles","Emberverse","wild-ruins","v3"),
("Radiant Emperor","emperors-and-erebus","The Radiant Emperor","alt-ming-fantasy","v3"),
("Belisarius","empires-that-never-fell","Belisarius","hidden-history-sf","v3"),
("Clockwork Dagger","clockwork-london","The Clockwork Dagger","technomancy","v3"),
("School of Shards","altered-selves","School of Shards","magic-school","v3"),
("Liaden Universe","venus-and-far-systems","Liaden Universe","interstellar-court-politics","v3"),
("Seven Devils","sea-rogues","Seven Devils","revolutionary-space-opera","v3"),
("Gap Cycle","empire-and-frontier-wars","The Gap Cycle","space-dystopias","v3"),
("Sun Eater","norton-and-standalone-colonies","Sun Eater","space-succession-opera","v3"),
("Kane of Old Mars","moon-bases-and-neighbour-worlds","Kane of Old Mars","old-mars","v3"),
("Troy Rising","great-ships-and-troy","Troy Rising","near-future-first-contact","v3"),
("Fall Revolution","war-and-memory-states","Fall Revolution","post-scarcity-politics","v3"),
("The Books of Babel","wonder-machines","The Books of Babel","absurdist-constructed-realities","v1"),
("I Am Legend","classic-last-people","I Am Legend","die-off","v1"),
("The Expanse","expanse-and-grand-tours","The Expanse","hard-alien","v1"),
("Vorkosigan Saga","long-series-fixers","The Vorkosigan Saga","interstellar-court-politics","v1"),
("Lilith's Brood","encounters-with-big-visitors","Lilith's Brood","xenanthropology","v1")]
res=[l.rstrip('\n').split('|') for l in open('/tmp/shadow/v2/results2.txt')]
out=[];xs=[]
for name,leaf,on,ol,org in D:
    c=[n for n in nodes if n['new'] and name in n['cards']]
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
