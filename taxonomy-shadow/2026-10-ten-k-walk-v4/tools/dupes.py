import yaml,glob,re,os
from collections import defaultdict
here=os.path.dirname(os.path.abspath(__file__))+'/..'
def norm(s):
    s=s.lower();s=re.sub(r'\(.*?\)','',s);s=re.sub(r'[^a-z0-9 ]',' ',s);s=re.sub(r'^(the|a|an) ','',s.strip());return re.sub(r'\s+',' ',s).strip()
bt=defaultdict(set);cn=defaultdict(set)
for f in glob.glob(here+'/genres/*.yaml'):
    g=yaml.safe_load(open(f))
    for c in g['cards']:
        cn[norm(c['name'])].add((g['id'],c['name']))
        for b in c['books']:
            bt[(norm(b['title']),norm(b.get('author','') or ''))].add((g['id'],c['name']))
bd={k:v for k,v in bt.items() if len({x[1] for x in v})>1 or len({x[0] for x in v})>1}
cd={k:v for k,v in cn.items() if len(v)>1}
print('books in >1 card/leaf:',len(bd)); print('card names repeated:',len(cd))
for k,v in sorted(bd.items())[:60]: print('BOOK',k,sorted(v))
for k,v in sorted(cd.items())[:40]: print('CARD',k,sorted(v))
