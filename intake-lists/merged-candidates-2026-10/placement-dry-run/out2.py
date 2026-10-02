import json,collections,csv,sys,os;sys.path.insert(0,'/tmp/sweep')
from xref import ns
byid={n['id']:n for n in ns}
kids=collections.defaultdict(list)
for n in ns:kids[n.get('parent')].append(n['id'])
def path(i):
    p=[]
    while i:p.append(byid[i]['label']);i=byid[i].get('parent')
    return ' > '.join(reversed(p))
def leaves_under(i):
    return [i] if not kids.get(i) else [l for c in kids[i] for l in leaves_under(c)]
res=json.load(open('placed.json'));D='/home/sandbox/sff-taxonomy-browser/intake-lists/merged-candidates-2026-10/placement-dry-run/';os.makedirs(D,exist_ok=True)
nt=[o for o in res if not o['low_conf_genre']]
# placements
with open(D+'placements.tsv','w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['title','author','year','imprints','level','tier','node_id','node_path','basis'])
    for o in nt:w.writerow([o['title'],o['author'],o['year'],o['imprints'],o['level'],o['tier'],o['node'],path(o['node']) if o['node'] else '',o['basis']])
lf=collections.defaultdict(collections.Counter)
for o in nt:
    if o['level']=='leaf':lf[o['node']][o['tier']]+=1
rows=[]
for l in [n['id'] for n in ns if not kids.get(n['id'])]:
    ex=len(byid[l].get('works',[]));c=lf.get(l,collections.Counter())
    t1=c['T1']+c['M'];t2=c['T2']
    rows.append(dict(leaf=l,path=path(l),existing=ex,easy_T1=t1,cluster_T2=t2,total_easy_plus_cluster=ex+t1+t2,overflow_strict=max(0,ex+t1-10),overflow_with_cluster=max(0,ex+t1+t2-10)))
rows.sort(key=lambda r:-r['overflow_with_cluster'])
with open(D+'leaf-projection.tsv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
br=collections.defaultdict(collections.Counter)
for o in nt:
    if o['level']=='branch':br[o['node']][o['tier']]+=1
brr=[]
for i,c in br.items():
    ls=leaves_under(i);brr.append(dict(branch=i,path=path(i),projected=sum(c.values()),from_multi_leaf_authors=c['B'],from_curated_author_map=c['M'],leaves_under=len(ls),existing_cards_under=sum(len(byid[l].get('works',[])) for l in ls),capacity_at_10_per_leaf=10*len(ls)))
brr.sort(key=lambda r:-r['projected'])
with open(D+'branch-projection.tsv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(brr[0]),delimiter='\t');w.writeheader();w.writerows(brr)
un=[o for o in nt if not o['node']]
ac=collections.Counter(o['author'] for o in un)
with open(D+'unmatched-top-authors.tsv','w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['author','unmatched_candidates']);[w.writerow(x) for x in ac.most_common(300)]
print('placed leaf',sum(1 for o in nt if o['level']=='leaf'),'branch',sum(1 for o in nt if o['level']=='branch'),'unmatched',len(un))
ov=[r for r in rows if r['overflow_strict']>0];ov2=[r for r in rows if r['overflow_with_cluster']>0]
print('leaves strict overflow',len(ov),sum(r['overflow_strict'] for r in ov),'| with cluster',len(ov2),sum(r['overflow_with_cluster'] for r in ov2))
print('leaves receiving any',sum(1 for r in rows if r['easy_T1']+r['cluster_T2']>0))
for r in rows[:25]:print(r['leaf'],r['existing'],r['easy_T1'],r['cluster_T2'],r['overflow_with_cluster'])
print('--branch');
for r in brr[:20]:print(r['branch'],r['projected'],'leaves',r['leaves_under'],'cap',r['capacity_at_10_per_leaf'],'existing',r['existing_cards_under'])
print('unmatched split by genre tag',collections.Counter(o['genre_tags'] or '(none)' for o in un).most_common(6))
print(collections.Counter(o['basis'] for o in un))
print(ac.most_common(15))
