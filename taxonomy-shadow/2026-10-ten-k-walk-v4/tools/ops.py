import yaml,os,re,sys,glob
here=os.path.dirname(os.path.abspath(__file__))+'/..'
def P(g): return f'{here}/genres/{g}.yaml'
def load(g): return yaml.safe_load(open(P(g)))
def save(g): open(P(g['id']),'w').write(yaml.safe_dump(g,sort_keys=False,allow_unicode=True,width=100))
def find(leaf,name):
    g=load(leaf)
    for c in g['cards']:
        if c['name']==name: return g,c
    raise SystemExit(f'NOT FOUND card {name!r} in {leaf}')
def run(line):
    f=[x.strip() for x in line.split('|')]; op=f[0]
    if op=='move':   # move|card|from|to
        g,c=find(f[2],f[1]); t=load(f[3])
        g['cards']=[x for x in g['cards'] if x is not c]; t['cards'].append(c); save(g); save(t)
    elif op=='new':  # new|id|label|parent|definition
        assert not os.path.exists(P(f[1])), 'exists '+f[1]
        save({'id':f[1],'label':f[2],'parent':f[3],'origin':'shadow-v4','definition':f[4],'cards':[]})
    elif op=='rename': # rename|id|label|definition
        g=load(f[1]); g['label']=f[2]
        if len(f)>3 and f[3]: g['definition']=f[3]
        save(g)
    elif op=='reparent': # reparent|id|newparent
        g=load(f[1]); g['parent']=f[2]; save(g)
    elif op=='rm':   # rm|id  (empty, no children)
        g=load(f[1]); assert not g['cards'], f'{f[1]} not empty'
        for p in glob.glob(here+'/genres/*.yaml'):
            assert yaml.safe_load(open(p))['parent']!=f[1], f'{f[1]} has children'
        os.remove(P(f[1]))
    elif op=='breakout': # breakout|leaf|card|newcard|title;title|target  - pull named books out of a batch card into a new card
        g,c=find(f[1],f[2]); ts={t.strip() for t in f[4].split(';')}
        out=[b for b in c['books'] if b['title'] in ts]; assert len(out)==len(ts), f'titles not all found: {ts-{b["title"] for b in out}}'
        c['books']=[b for b in c['books'] if b['title'] not in ts]
        t=load(f[5]); t['cards'].append({'name':f[3],'origin':'v3','books':out})
        if not c['books']: g['cards']=[x for x in g['cards'] if x is not c]
        if f[5]==f[1]: g=t if False else g
        save(g); 
        if f[5]!=f[1]: save(t)
    elif op=='hold': # hold|card|from|reason  - card has no honest leaf yet; goes to holds.yaml, never to a slush bucket
        g,c=find(f[2],f[1]); g['cards']=[x for x in g['cards'] if x is not c]; save(g)
        hp=here+'/holds.yaml'; h=yaml.safe_load(open(hp)) if os.path.exists(hp) else []
        c['held_from']=f[2]; c['reason']=f[3]; h.append(c)
        open(hp,'w').write(yaml.safe_dump(h,sort_keys=False,allow_unicode=True,width=100))
    else: raise SystemExit('bad op '+line)
if __name__=='__main__':
    for l in open(sys.argv[1]):
        l=l.rstrip('\n')
        if l.strip() and not l.startswith('#'): run(l)
    print('ok')
