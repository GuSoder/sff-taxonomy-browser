import sys,json,re,collections,csv,unicodedata
sys.path.insert(0,'/tmp/sweep')
R='/home/sandbox/sff-taxonomy-browser/intake-lists/method-tests/'
from xref import ns
def asc(s):return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
EDN=r"\b(collector'?s|collectors|special|deluxe|illustrated|anniversary|signed|limited|exclusive|standard|hardcover|paperback|tie-?in|movie|film|gift|10th|20th|25th|30th|40th|50th|reissue|new|revised|expanded|unabridged|large print|export|trade)\b[^()]*\bedition\b"
def clean_title(t):
    t=asc(t).replace('’',"'").replace('\r',' ')
    t=re.sub(r'\s*[-–:]\s*eARC.*$','',t,flags=re.I)
    t=re.sub(r'\((?:[^()]*)(?:edition|unabridged|ebook|book \d+|\#\d+)[^()]*\)','',t,flags=re.I)
    t=re.sub(r'[:,-]?\s*(?:a|the)? ?novel$','',t,flags=re.I) if False else t
    t=re.sub(EDN,'',t,flags=re.I)
    t=re.sub(r'\s*[:\-–]\s*$','',t.strip())
    return re.sub(r'\s+',' ',t).strip()
def norm(s):
    s=asc(s).lower();s=re.sub(r'\(.*?\)','',s);s=re.sub(r'[^a-z0-9 ]',' ',s);s=re.sub(r'^(the|a|an) ','',s.strip());return re.sub(r'\s+',' ',s).strip()
def surn(a):
    a=asc(a)
    a=re.sub(r'(?i)^(edited by|ed\.|by|introduction by|illustrated by|with)\s+','',a.strip())
    a=re.split(r'(?i)\s+(?:writing as|and|with|&|\+)\s+|,|\+',a)[0].strip()
    a=re.sub(r'\s*\(.*?\)','',a)
    toks=[x for x in re.sub(r'[^A-Za-z\' -]','',a).split() if x]
    if not toks:return '',''
    return toks[-1].lower().strip("'"),toks[0][0].lower()
def first_author(a):
    a=asc(a or '')
    a=re.sub(r'(?i)^(edited by|edited|ed\.)\s*','',a.strip())
    a=re.split(r'(?i)\s+writing as\s+|\s+and\s+|\s*,\s*|\s*&\s*|\s*\+\s*|\s+with\s+',a)[0].strip()
    return a
# tree
tree=collections.defaultdict(set)  # normtitle -> author surnames (empty set -> unknown)
treeauth=collections.defaultdict(list)  # surname -> [(leafid)]
node={n['id']:n for n in ns}
for n in ns:
    for w in n.get('works',[]):
        au=set(surn(a)[0] for a in (w.get('authors') or []))
        for t in [w['title']]+[b['title'] for b in w.get('books',[])]:
            tree[norm(t)]|=au if au else {'?'}
rows=[]
def add(src,imp,title,author,year=None,cat=None,series=None,extra=None):
    t=clean_title(title)
    if not t or len(t)<2:return
    rows.append(dict(title=t,author=first_author(author),year=year,source=src,imprint=imp,genre_tag=cat,series=series,extra=extra))
# Tor
for r in json.load(open(R+'imprint-sweep-2026-10/tor_new.json')):add('Macmillan/Tor',r['imp'],r['title'],r['author'],r['y'],r['cat'])
# Hachette
for k,v in json.load(open(R+'imprint-sweep-2026-10/hbg_all.json')).items():add('Hachette site search','Hachette group (Orbit/Redhook/other)',v[1],v[2],None,None)
# Gollancz
GEN=set()
gl=json.load(open('gol_full.json'));tc=collections.Counter()
for p in gl:
    for t in eval(p['tags']) if isinstance(p['tags'],str) else p['tags']:tc[t]+=1
BAD=re.compile(r'fantasy|fiction|series|romance|thriller|horror|science|epic|sword|space|action|adventure|general|gollancz|paperback|hardback|edition|masterworks|essentials|tiktok|shopify|thema|bisac|children|teen|juvenile|modern|contemporary|urban|paranormal|dystopi|alien|time travel|myth|legend|fairy|folk|magical|historical|crime|mystery|literary|classic|gothic|comic|humor|fantastic|ebook|audio|book|tax-rate|v1\.|stories|cyber|punk|dark|post|apocal|war|military|steampunk|western|detective|vampire|witch|dragon|magic|superhero|short|collection|anthology|novel|saga|hard|soft|first contact|robot|biograph|history|young|adult|award|prize|wars?$',re.I)
def gl_author(tags):
    c=[t for t in tags if re.match(r"^[A-Z][A-Za-z.'\-]+( [A-Za-z.'\-]+){1,3}$",t) and not BAD.search(t) and tc[t]<=80 and not re.search(r'\d',t)]
    return c
# Harper
for p in json.load(open(R+'imprint-sweep-2026-10/harper_voyager_titles.json')):
    h=p['handle'];ts=re.sub(r'[^a-z0-9]+','-',asc(clean_title(p['title'])).lower()).strip('-')
    a=''
    if h.startswith(ts+'-'):a=h[len(ts)+1:].replace('-',' ').title()
    elif True:
        # fall back: last two slug tokens
        a=''
    add('HarperCollins Voyager collection','Harper Voyager',p['title'],a,None,None,extra=('author from URL slug' if a else 'author missing'))
# PRH
for r in json.load(open('/tmp/prh/prh_unique.json')):
    if r['imprint'] in('Del Rey','Ace','DAW','Spectra'):
        y=int(r['onsale'][:4]) if r.get('onsale') else None
        add('PRH randomhousebooks.com API',r['imprint'],r['title'],(r['author'] or [''])[0],y,None,r.get('series'))
for r in json.load(open('/tmp/prh/baen_titles.json')):
    a=r['author'].split('\n')[-1]
    add('Baen category pages','Baen',r['title'],a,int(r['date'][:4]) if r['date'] else None,None)
# Titan (flag)
import csv as c2
for r in c2.DictReader(open(R+'imprint-catalogs-2026-10/titan_candidates_not_in_tree.tsv'),delimiter='\t'):
    add('Titan (low-confidence genre)','Titan',r['title'],r['author'],int(r['year']) if r['year'].isdigit() else None,None)

KNOWN=set(surn(r['author'])[0] for r in rows)|set(x for v in tree.values() for x in v)
for p in gl:
    tags=eval(p['tags']) if isinstance(p['tags'],str) else p['tags']
    bis=[t for t in tags if t.startswith('BISAC:')]
    sf=any(b.startswith(('BISAC:FIC009','BISAC:FIC028')) for b in bis) or 'Fantasy' in tags or 'Science Fiction' in tags
    if not sf:continue
    ca=gl_author(tags)
    if p['product_type'] in ('Gift','Merchandise'):continue
    cat='Fantasy' if ('Fantasy' in tags or any(b.startswith('BISAC:FIC009') for b in bis)) and 'Science Fiction' not in tags else ('Science Fiction' if 'Science Fiction' in tags else 'SFF')
    kn=[c for c in ca if surn(c)[0] in KNOWN]
    pick=kn[0] if kn else (ca[0] if ca else '')
    add('Gollancz store','Gollancz',p['title'],pick,None,cat,extra=('author from tags (matches author seen elsewhere)' if kn else ('author from tags, UNVERIFIED' if ca else 'author missing')))
print(len(rows),collections.Counter(r['source'] for r in rows))
json.dump(rows,open('rows_raw.json','w'))
