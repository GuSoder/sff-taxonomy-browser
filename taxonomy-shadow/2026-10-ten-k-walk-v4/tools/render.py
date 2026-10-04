import yaml,glob,os,sys
from collections import defaultdict
here=os.path.dirname(os.path.abspath(__file__))+'/..'
gs={}
for f in glob.glob(here+'/genres/*.yaml'):
    g=yaml.safe_load(open(f)); gs[g['id']]=g
kids=defaultdict(list)
for g in gs.values(): kids[g['parent']].append(g['id'])
out=[];nl=nc=0
def emit(i,d):
    global nl,nc
    g=gs[i];k=kids[i];n=len(g['cards'])
    tag='' if g['origin']=='original' else ' NEW'
    if k:
        out.append('  '*d+f"[{i}] {g['label']}{tag}"+(f" (umbrella, {n} direct cards)" if n else ''))
    else:
        out.append('  '*d+f"[{i}] {g['label']}{tag} ({n})");nl+=1
    nc+=n
    for c in g['cards']: out.append('  '*(d+1)+'- '+c['name'])
    for x in k: emit(x,d+1)
for r in kids[None]: emit(r,0)
open(here+'/tree.txt','w').write('\n'.join(out)+'\n')
print('genres',len(gs),'leaves',nl,'cards',nc)
