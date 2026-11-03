#!/usr/bin/env python3
"""Move one existing card between leaves. Usage: live_move.py work-id old-leaf new-leaf 'reason'"""
import re,json,yaml,os,glob,sys,shutil
R=os.path.expanduser('~/sff-taxonomy-browser'); os.chdir(R)
wid,old,new,reason=sys.argv[1:5]
gdir={os.path.basename(os.path.dirname(f)):os.path.dirname(f) for f in glob.glob('taxonomy/speculative-fiction/**/genre.yaml',recursive=True)}
od,nd=gdir[old],gdir[new]
# works yaml
p=f'{od}/works/{wid}.yaml'
wy=yaml.safe_load(open(p,encoding='utf-8'))
assert wy['canonical_genre']==old, wy['canonical_genre']
wy['canonical_genre']=new
wy.setdefault('placement_history',[]).append(dict(date='2026-11-03',**{'from':old,'to':new,'reason':reason}))
yaml.safe_dump(wy,open(p,'w',encoding='utf-8'),allow_unicode=True,sort_keys=False,width=120)
os.makedirs(f'{nd}/works',exist_ok=True); shutil.move(p,f'{nd}/works/{wid}.yaml')
# genre.yaml works lists
for d,drop in ((od,True),(nd,False)):
    fp=f'{d}/genre.yaml'; g=open(fp,encoding='utf-8').read()
    if drop:
        g=re.sub(rf'^- {re.escape(wid)}\n','',g,count=1,flags=re.M)
    else:
        if re.search(r'^works: \[\]$',g,re.M): g=re.sub(r'^works: \[\]$',f'works:\n- {wid}',g,flags=re.M)
        else:
            mm=re.search(r'^works:\n((?:- .*\n)+)',g,re.M); assert mm, fp
            g=g[:mm.end()]+f'- {wid}\n'+g[mm.end():]
    open(fp,'w',encoding='utf-8').write(g)
# index.html
s=open('index.html',encoding='utf-8').read()
m=re.search(r'const nodes=(.*)\n',s); nodes,end=json.JSONDecoder().raw_decode(m.group(1)); by={n['id']:n for n in nodes}
works=by[old]['works']; i=[k for k,w in enumerate(works) if (w.get('id') or '')==wid or (w.get('title') and re.sub(r'-+','-',re.sub(r'[^a-z0-9]+','-',w['title'].lower().replace("'",''))).strip('-')==wid)]
assert i, 'work not found in old leaf node'
w=works.pop(i[0]); by[new]['works'].append(w)
s=s[:m.start(1)]+json.dumps(nodes,ensure_ascii=False,separators=(',',':'))+m.group(1)[end:]+s[m.end(1):]
open('index.html','w',encoding='utf-8').write(s)
print('moved',wid,old,'->',new,'| counts:',len(by[old]['works']),'->',len(by[new]['works']))
