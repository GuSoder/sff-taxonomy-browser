import json,re,collections,csv
exec(open('merge.py').read().split("rows=[]")[0])  # reuse helpers+tree
rows=json.load(open('rows_raw.json'))
NON=re.compile(r"\b(box(ed)? set|bundle|calendar|coloring|colouring|journal|sampler|cookbook|planner|notebook|trilogy collection|complete collection|collection of|\d+-book|\d+ book|omnibus|boxset|tarot|sketchbook|art of|official guide|roleplaying|rpg|screenplay|manga|graphic novel|volume \d+|vol\. ?\d+|writing prompts|poster|coloring)\b",re.I)
groups=collections.OrderedDict()
for r in rows:
    nt=norm(r['title']);sn,ini=surn(r['author'])
    r['nt']=nt;r['sn']=sn
    k=(nt,sn)
    groups.setdefault(k,[]).append(r)
# merge authorless into authored with same title
byt=collections.defaultdict(list)
for (nt,sn),g in groups.items():byt[nt].append((sn,g))
final=[]
for (nt,sn),g in groups.items():
    if sn=='' and any(s!='' for s,_ in byt[nt]):continue
    final.append(g)
out=[];dropped=collections.Counter()
for g in final:
    r0=sorted(g,key=lambda r:(r['author']=='',r['year'] is None))[0]
    title=r0['title'];
    if NON.search(title):dropped['non-novel/box/bundle']+=1;continue
    srcs=sorted({r['source'] for r in g});imps=sorted({r['imprint'] for r in g})
    ys=[r['year'] for r in g if r['year']]
    ts=tree.get(r0['nt'])
    status='new'
    if ts is not None:
        if '?' in ts or r0['sn']=='' or r0['sn'] in ts:status='in_tree';
        else:status='title_collision_diff_author'
    tags=sorted({r['genre_tag'] for r in g if r['genre_tag']})
    out.append(dict(title=title,author=r0['author'],year=min(ys) if ys else '',sources='; '.join(srcs),imprints='; '.join(imps),genre_tags=', '.join(tags),series=next((r['series'] for r in g if r['series']),''),notes='; '.join(sorted({r['extra'] for r in g if r['extra']})),tree_status=status,low_conf_genre=int(srcs==['Titan (low-confidence genre)']),n_sources=len(srcs)))
print(len(final),len(out),dropped)
print(collections.Counter(o['tree_status'] for o in out))
new=[o for o in out if o['tree_status']!='in_tree']
print('candidates',len(new),'excl titan-only',sum(1 for o in new if not o['low_conf_genre']),'multi-src',sum(o['n_sources']>1 for o in new),'noauthor',sum(1 for o in new if not o['author']))
json.dump(out,open('merged_all.json','w'))
