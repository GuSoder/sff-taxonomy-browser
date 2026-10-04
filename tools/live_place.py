#!/usr/bin/env python3
"""Place one card in the live tree. Usage: live_place.py spec.json
spec: {leaf,title,authors,why,books:[{id,title,year,cover}],cover}"""
import re,json,yaml,os,glob,sys
R=os.path.expanduser('~/sff-taxonomy-browser'); os.chdir(R)
MSG='phonemsg-01M43MYMGAMQTNA3CY402KK7FB'
sp=json.load(open(sys.argv[1]))
slug=lambda s: re.sub(r'-+','-',re.sub(r'[^a-z0-9]+','-',s.lower().replace("'",''))).strip('-')
gdir={os.path.basename(os.path.dirname(f)):os.path.dirname(f) for f in glob.glob('taxonomy/speculative-fiction/**/genre.yaml',recursive=True)}
leaf=sp['leaf']; title=sp['title']; wid=slug(title)
assert not glob.glob(f'taxonomy/speculative-fiction/**/works/{wid}.yaml',recursive=True),'exists'
bl=sorted(sp['books'],key=lambda b:b.get('year') or 9999)
books=[]
for b in bl:
    e=dict(title=b['title'])
    if b.get('year'): e['year']=b['year']
    if b.get('cover'): e['cover_url']=b['cover']
    books.append(e)
fy=min([b['year'] for b in bl if b.get('year')],default=None)
cover=sp['cover']
wy=dict(id=wid,title=title,authors=sp['authors'],first_published=fy,canonical_genre=leaf,placement_status='accepted',placement_rationale=sp['why'],
 books=books,cover_curation=dict(status='complete',source='Open Library / publisher',selected_url=cover,visually_reviewed_on='2026-10-04',review_method='contact-sheet one-pass'),
 intake='ten-k walk v5 (queue ids '+', '.join(b['id'] for b in bl)+')',
 placement_history=[dict(date='2026-10-04',to=leaf,reason=f'Intake from the 10k list: placed by a root-down walk (curator commission {MSG}).')])
if fy is None: wy.pop('first_published')
d=gdir[leaf]; os.makedirs(d+'/works',exist_ok=True)
yaml.safe_dump(wy,open(f'{d}/works/{wid}.yaml','w',encoding='utf-8'),allow_unicode=True,sort_keys=False,width=120)
g=open(d+'/genre.yaml',encoding='utf-8').read()
if re.search(r'^works: \[\]$',g,re.M): g=re.sub(r'^works: \[\]$',f'works:\n- {wid}',g,flags=re.M)
else:
    mm=re.search(r'^works:\n((?:- .*\n)+)',g,re.M); assert mm
    g=g[:mm.end()]+f'- {wid}\n'+g[mm.end():]
open(d+'/genre.yaml','w',encoding='utf-8').write(g)
s=open('index.html',encoding='utf-8').read()
m=re.search(r'const nodes=(.*)\n',s); nodes,end=json.JSONDecoder().raw_decode(m.group(1)); by={n['id']:n for n in nodes}
nw=dict(title=title,cover_url=cover,shows_english_title=True,authors=sp['authors'],year=fy,books=books,placement_note=sp['why'])
if fy is None: nw.pop('year')
by[leaf]['works'].append(nw)
s=s[:m.start(1)]+json.dumps(nodes,ensure_ascii=False,separators=(',',':'))+m.group(1)[end:]+s[m.end(1):]
open('index.html','w',encoding='utf-8').write(s)
open('taxonomy-shadow/2026-10-ten-k-walk-v5/intake/_done.txt','a').write('\n'.join(b['id'] for b in bl)+'\n')
print('placed',title,'->',leaf,len(by[leaf]['works']))
