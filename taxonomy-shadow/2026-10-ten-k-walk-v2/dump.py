import sys,re
sys.path.insert(0,'/tmp/sweep')
import xref
ns={n['id']:n for n in xref.ns}
leaf=sys.argv[1]
n=ns[leaf]
print('LEAF',leaf,'|parent',n['parent'],'|',(n['definition'] or '')[:300])
for w in n['works']:
    print('  E|',w if isinstance(w,str) else (w.get('title'),w.get('author')))
for l in open('results.txt'):
    f=l.rstrip('\n').split('|')
    if f[0]=='C' and len(f)>=4 and f[3]==leaf: print('  N|',f[1],'|',f[4][:50] if len(f)>4 else '')
