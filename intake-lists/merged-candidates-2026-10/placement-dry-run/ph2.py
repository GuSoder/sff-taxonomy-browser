import sys,json,collections,re,csv;sys.path.insert(0,'/tmp/sweep')
exec(open('merge.py').read().split("rows=[]")[0])
kids=collections.Counter(n.get('parent') for n in ns)
byid={n['id']:n for n in ns}
def anc(i):
    p=[]
    while i:p.append(i);i=byid[i].get('parent') if i in byid else None
    return p
def label(i):return byid[i]['label'] if i in byid else i
al=collections.defaultdict(collections.Counter)
leafworks=collections.Counter()
treeseries={}  # norm title -> leaf (works titles)
for n in ns:
    leafworks[n['id']]=len(n.get('works',[]))
    for w in n.get('works',[]):
        for a in (w.get('authors') or []):al[surn(a)][n['id']]+=1
        treeseries[norm(w['title'])]=n['id']
M={ # author -> node (branch or leaf), my knowledge of what the author is mainly known for
'brian jacques':'animal-fantasy','mercedes lackey':'epic-fantasy','david weber':'military-science-fiction','david drake':'military-science-fiction','john ringo':'military-science-fiction','ian douglas':'military-science-fiction','mike shepherd':'military-science-fiction','tom kratman':'military-science-fiction','michael z. williamson':'military-science-fiction','steven l. kent':'military-science-fiction','travis s. taylor':'military-science-fiction',
'eric flint':'alternate-history','ben bova':'hard-sf','charles sheffield':'hard-sf','james p. hogan':'hard-sf','sharon lee':'new-space-opera','peter f. hamilton':'new-space-opera','catherine asaro':'new-space-opera','brian herbert':'spacefaring-fiction','charles e. gannon':'spacefaring-fiction','jack mcdevitt':'spacefaring-fiction','edmond hamilton':'pulp-space-opera','julie e. czerneda':'alien-fiction',
'patricia briggs':'urban-fantasy','faith hunter':'urban-fantasy','kim harrison':'urban-fantasy','lilith saintcrow':'urban-fantasy','charles de lint':'urban-fantasy','chloe neill':'vampire-fantasy','ilona andrews':'urban-fantasy','kevin hearne':'urban-fantasy','benedict jacka':'urban-fantasy','diana rowland':'urban-fantasy','rob thurman':'urban-fantasy','lynsay sands':'vampire-fantasy','barb hendee':'vampire-fantasy','charlaine harris':'vampire-fantasy','nalini singh':'nocturne-fantasy',
'katharine kerr':'epic-fantasy','david dalglish':'epic-fantasy','sara douglass':'epic-fantasy','mark lawrence':'epic-fantasy','michelle west':'epic-fantasy','melanie rawn':'political-fantasy','miles cameron':'epic-fantasy','anthony ryan':'epic-fantasy','jennifer fallon':'epic-fantasy','dave duncan':'epic-fantasy','django wexler':'epic-fantasy','brent weeks':'epic-fantasy','trudi canavan':'epic-fantasy','james barclay':'epic-fantasy','dennis l. mckiernan':'classic-quest-fantasy','ian c. esslemont':'epic-fantasy','john gwynne':'epic-fantasy','sam sykes':'epic-fantasy','kristen britain':'epic-fantasy','elizabeth haydon':'epic-fantasy','ken scholes':'epic-fantasy','bradley p. beaulieu':'epic-fantasy','rj barker':'epic-fantasy','lynn flewelling':'epic-fantasy','margaret weis':'classic-quest-fantasy','tracy hickman':'classic-quest-fantasy','jennifer roberson':'fantasy-realms',
'gail carriger':'gaslight-fantasy','robert rankin':'earthly-comic-fantasy','carissa broadbent':'romantasy','steven brust':'fantasy-realms'}
Mk={tuple(k.split()[-1:])+(k[0],) :v for k,v in M.items()}  # (surname,first initial)
def key(a):return surn(a)
MK={}
for a,v in M.items():MK[surn(a)]=v
cands=json.load(open('cands.json'))
TIE=re.compile(r"\b(star wars|star trek|warhammer|forgotten realms|dragonlance|halo|doctor who|warcraft|starcraft|world of warcraft|marvel|dc comics|dungeons|battletech|mass effect|assassin'?s creed|alien:|aliens:|terminator|stargate|supernatural|buffy|the witcher)\b",re.I)
ANTH=re.compile(r"(year'?s best|best of the year|best new|anthology|the best (science|fantasy|horror)|treasury|\bstories\b|\btales\b|megapack|\bbaen free)",re.I)
EDITORS={'dozois','hartwell','davis','miller','datlow','strahan','windling'}
acount=collections.Counter(surn(o['author']) for o in cands if not o['low_conf_genre'])
res=[];reasons=collections.Counter()
for o in cands:
    if o['low_conf_genre']:o['node']='';o['level']='';o['basis']='titan low-confidence genre, not placed';res.append(o);continue
    a=o['author'];k=surn(a);c=al.get(k)
    o['tier']=''
    o['node']='';o['level']='';o['basis']=''
    # leaf by series
    ser=o['series'];
    if ANTH.search(o['title']) or k[0] in EDITORS and acount[k]>=3:
        o['basis']='unmatched: anthology/collection (editor or title pattern)';res.append(o);continue
    if ser and norm(ser) in treeseries:
        o['node']=treeseries[norm(ser)];o['level']='leaf';o['basis']='series matches tree card';o['tier']='T1'
    elif c:
        if len(c)==1:
            o['node']=next(iter(c));o['level']='leaf';o['tier']='T1' if acount[k]<=4 else 'T2';o['basis']='author in tree, all cards in one leaf (%d); %d candidates by author'%(sum(c.values()),acount[k])
        else:
            ps=[anc(l) for l in c]
            common=[x for x in ps[0] if all(x in p for p in ps)]
            o['node']=common[0] if common else 'speculative-fiction';o['level']='branch';o['tier']='B';o['basis']='author in tree across %d leaves; common ancestor'%len(c)
    elif k in MK:
        o['node']=MK[k];o['level']='leaf' if MK[k] in kids and False else ('branch' if MK[k] in kids else 'leaf');o['tier']='M';o['basis']='author knowledge (curated map)'
    if not o['node']:
        if TIE.search(o['title']) or TIE.search(o['series'] or ''):reasons['media tie-in']+=1;o['basis']='unmatched: media tie-in'
        elif not a:reasons['no author']+=1;o['basis']='unmatched: no author'
        else:o['basis']='unmatched: author/series unknown to tree and map'
    res.append(o)
json.dump(res,open('placed.json','w'))
lv=[o for o in res if o['level']=='leaf'];br=[o for o in res if o['level']=='branch'];un=[o for o in res if not o['node'] and not o['low_conf_genre']]
print('non-titan',sum(1 for o in res if not o['low_conf_genre']),'leaf',len(lv),'branch',len(br),'unmatched',len(un))
print(collections.Counter(o['basis'].split(' (')[0] for o in res if not o['low_conf_genre']))
