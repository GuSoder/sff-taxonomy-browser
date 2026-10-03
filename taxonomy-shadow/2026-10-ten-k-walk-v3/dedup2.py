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
D=[("Riftwar","riftwar-cycle","The Riftwar Saga","destiny-quest-fantasy","v3"),
("Black Company","gods-and-black-companies","The Black Company","pulp-sword-and-sorcery","v3"),
("Iron Druid","druids-and-inheritors","Iron Druid Chronicles","modern-pantheon-myth","v3"),
("Deryni","deryni-and-kay-courts","Deryni Rising","paladin-hero","v3"),
("Takeshi Kovacs and Morgan","rebuilt-bodies-and-agents","Takeshi Kovacs","techno-fiction-in-space","v3"),
("Greta Helsing","pet-and-preternatural-sleuths","Dr. Greta Helsing","paranormal-fantasy","v3"),
("Amina al-Sirafi","tricksters-thieves-and-blades","The Adventures of Amina al-Sirafi","alt-spice-route-fantasy","v3"),
("Sirens of Titan","cobra-vor-and-titan-sirens","The Sirens of Titan","humorous-science-fiction","v3"),
("Charles de Lint Newford","newford-and-lost-boys","Newford","paranormal-bricks","v3"),
("Nightfall Reichert","gentleman-and-guild-thieves","Nightfall Saga","dark-quest-fantasy","v3"),
("Belisarius Tide of Victory","ark-dreamers-and-girls","Belisarius","hidden-history-sf","v3"),
("Sword of Truth","truth-and-flame-swords","The Sword of Truth","destiny-quest-fantasy","v1"),
("Riftwar Saga","classic-apprentices","The Riftwar Saga","destiny-quest-fantasy","v1"),
("The Divine Cities","ring-and-law-intrigue","Divine Cities","insurgent-fantasy","v1"),
("Rook and Rose","gentleman-and-guild-thieves","Rook & Rose Trilogy","court-spies","v1"),
("World of the Five Gods (Penric)","scholar-mages-and-saints","World of the Five Gods","cleric-hero","v1"),
("Semiosis","first-settlers","Semiosis","alien-expedition","v1"),
("Naamah's (Kushiel's Legacy)","","Kushiel's Legacy","renaissance-dynastic-intrigue","v1")]
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
