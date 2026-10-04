#!/usr/bin/env python3
"""Original tree loader + printer. usage: otree.py [maxdepth] [rootid] [--defs]"""
import yaml,glob,os,sys
R=os.path.expanduser('~/sff-taxonomy-browser/taxonomy/speculative-fiction')
def load():
    n={}
    for f in glob.glob(R+'/**/genre.yaml',recursive=True):
        g=yaml.safe_load(open(f)); d=os.path.dirname(f)
        g['dir']=d; g['nworks']=len(glob.glob(d+'/works/*.yaml')); n[g['id']]=g
    return n
def pr(n,i,depth,maxd,defs,ind=0):
    g=n[i]
    print('  '*ind+f"{g['label']} [{i}] L{depth} w={g['nworks']}"+(f" :: {g.get('definition','')}" if defs else ''))
    if depth<maxd:
        for c in g.get('children') or []: pr(n,c,depth+1,maxd,defs,ind+1)
if __name__=='__main__':
    a=[x for x in sys.argv[1:] if not x.startswith('--')]
    n=load(); md=int(a[0]) if a else 2; root=a[1] if len(a)>1 else 'speculative-fiction'
    def dep(i):
        d=0
        while n[i].get('parent'): i=n[i]['parent']; d+=1
        return d
    pr(n,root,dep(root),md,'--defs' in sys.argv)
