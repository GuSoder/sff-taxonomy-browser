import sys
V='/home/sandbox/sff-taxonomy-browser/taxonomy-shadow/2026-10-ten-k-walk-v5/sweep/verdicts-pass1.tsv'
upd={}
for l in sys.stdin:
    l=l.rstrip('\n')
    if not l: continue
    i,v,n=(l.split('|',2)+['',''])[:3]; upd[i.strip()]=(v.strip(),n.strip())
rows=[l.rstrip('\n').split('\t') for l in open(V,encoding='utf-8')]
c=0
out=[]
for r in rows:
    if r[0] in upd:
        while len(r)<6:r.append('')
        r[4],r[5]=upd[r[0]];c+=1
    out.append('\t'.join(r))
open(V,'w',encoding='utf-8').write('\n'.join(out)+'\n'); print('updated',c,'of',len(upd))
