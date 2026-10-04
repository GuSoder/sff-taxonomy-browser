import yaml,os,re,sys
here=os.path.dirname(os.path.abspath(__file__))+'/..'
def norm(s):
    s=s.lower();s=re.sub(r'\(.*?\)','',s);s=re.sub(r'[^a-z0-9 ]',' ',s);s=re.sub(r'^(the|a|an) ','',s.strip());return re.sub(r'\s+',' ',s).strip()
def load(g): return yaml.safe_load(open(f'{here}/genres/{g}.yaml'))
def save(g): open(f"{here}/genres/{g['id']}.yaml",'w').write(yaml.safe_dump(g,sort_keys=False,allow_unicode=True,width=100))
def fold(rl,rc,kl,kc,batch=False):
    """Fold card rc@rl into kc@kl. batch=True: only drop overlapping books, keep the rest on rc."""
    r=load(rl); k=load(kl) if kl!=rl else r
    rcard=next(c for c in r['cards'] if c['name']==rc); kcard=next(c for c in k['cards'] if c['name']==kc)
    have={norm(b['title']) for b in kcard['books']}
    moved=0
    left=[]
    for b in rcard['books']:
        if norm(b['title']) in have: continue
        if batch: left.append(b)
        else: kcard['books'].append(b); have.add(norm(b['title'])); moved+=1
    if batch and left: rcard['books']=left
    else: r['cards']=[c for c in r['cards'] if c is not rcard]
    save(r)
    if k is not r: save(k)
    return moved,len(left)
if __name__=='__main__':
    log=[]
    for line in open(sys.argv[1]):
        line=line.strip()
        if not line or line.startswith('#'): continue
        f=[x.strip() for x in line.split('|')]
        m,l=fold(f[0],f[1],f[2],f[3],len(f)>4 and f[4]=='batch')
        print('folded',f,'moved',m,'left',l)
