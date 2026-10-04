#!/usr/bin/env python3
"""v5 intake into the ORIGINAL tree (overlay; live tree untouched).
  intake.py next [n]            show next n unprocessed books
  intake.py place ID leaf [card]  add book ID to card (new card or existing) in leaf
  intake.py hold ID reason      hold a book
  intake.py count               leaf counts incl. overlay
Progress: intake/_done.txt (ids), cards in intake/<leaf>.yaml, holds in intake/_holds.yaml"""
import json,sys,os,yaml,re,glob
sys.path.insert(0,os.path.dirname(__file__)); import otree
H=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IN=H+'/intake'
Q=json.load(open('/tmp/shadow/queue.json'))
byid={x['id']:x for x in Q}
RES={}
for p in ['/tmp/shadow/v3/research.jsonl']:
    for l in open(p):
        r=json.loads(l); RES[r['i']]=r
def done():
    p=IN+'/_done.txt'
    return set(open(p).read().split()) if os.path.exists(p) else set()
def mark(i): open(IN+'/_done.txt','a').write(i+'\n')
def norm(s): return re.sub(r'[^a-z0-9 ]','',s.lower())
def orig_titles():
    t={}
    for f in glob.glob(otree.R+'/**/works/*.yaml',recursive=True):
        w=yaml.safe_load(open(f)) or {}
        for x in [w.get('title')]+(w.get('included_titles') or []):
            if x: t.setdefault(norm(x),[]).append((w.get('title'),f.split('speculative-fiction/')[1].split('/works')[0]))
    return t
def orig_by_author():
    a={}
    for f in glob.glob(otree.R+'/**/works/*.yaml',recursive=True):
        w=yaml.safe_load(open(f)) or {}
        for au in w.get('authors') or []:
            a.setdefault(norm(str(au)),[]).append((w.get('id'),w.get('title'),f.split('speculative-fiction/')[1].split('/works')[0].split('/')[-1],(w.get('included_titles') or [])))
    return a
def apply_edits(n):
    p=IN+'/_edits.yaml'
    if not os.path.exists(p): return n
    e=yaml.safe_load(open(p)) or {}
    for g in e.get('new_genres',[]):
        n[g['id']]={'id':g['id'],'label':g['label'],'parent':g['parent'],'definition':g['definition'],'children':[],'nworks':0,'dir':None}
        n[g['parent']].setdefault('children',[]) 
        if n[g['parent']]['children'] is None: n[g['parent']]['children']=[]
        n[g['parent']]['children'].append(g['id'])
    for leaf,ws in (e.get('moved_out') or {}).items(): n[leaf]['nworks']-=len(ws)
    return n
def load_leaf(l):
    p=f'{IN}/{l}.yaml'
    return yaml.safe_load(open(p)) if os.path.exists(p) else {'id':l,'cards':[]}
def save_leaf(g): yaml.safe_dump(g,open(f"{IN}/{g['id']}.yaml",'w'),sort_keys=False,allow_unicode=True,width=100)
def ncards(n,l): return n[l]['nworks']+len(load_leaf(l)['cards'])
if __name__=='__main__':
    c=sys.argv[1]; n=apply_edits(otree.load())
    if c=='next':
        k=int(sys.argv[2]) if len(sys.argv)>2 else 5; d=done(); ot=orig_titles(); oa=orig_by_author(); s=0
        for x in Q:
            if x['id'] in d: continue
            r=RES.get(x['i']); t=(r or {}).get('t','')
            print(f"\n## {x['id']} | {x['title']} | {x['author']} | {x['year']} | series={x['series']} | {x['genre_tags']} | {x['tree_status']}")
            hit=ot.get(norm(x['title']))
            if hit: print('  !! TITLE IN ORIGINAL TREE:',hit)
            for w in oa.get(norm(re.sub(r' \d+$','',x['author'])),[]): print('  ~ orig work by author:',w[0],'|',w[1],'| leaf',w[2],'| incl',w[3][:6])
            print('  BLURB:',t[:700].replace('\n',' ') if t else '(none in cache)')
            s+=1
            if s>=k: break
    elif c=='place':
        i,l=sys.argv[2],sys.argv[3]; card=sys.argv[4] if len(sys.argv)>4 else None
        x=byid[i]; assert l in n, 'unknown leaf'
        assert not n[l].get('children'), 'leaf has children (umbrella)'
        g=load_leaf(l); card=card or x['title']
        for cd in g['cards']:
            if cd['name']==card: cd['books'].append({'id':i,'title':x['title'],'author':x['author']}); break
        else: g['cards'].append({'name':card,'why':os.environ.get('WHY',''),'books':[{'id':i,'title':x['title'],'author':x['author']}]})
        save_leaf(g); mark(i); k=ncards(n,l)
        print(f"placed {x['title']} -> {l} ({k} cards)"+('  *** TRIGGER: leaf at >=10, split owed ***' if k>=10 else ''))
    elif c=='fold':
        i,wid=sys.argv[2],sys.argv[3]; p=IN+'/_folds.yaml'
        h=yaml.safe_load(open(p)) if os.path.exists(p) else []
        h.append({'id':i,'title':byid[i]['title'],'author':byid[i]['author'],'onto_original_work':wid}); yaml.safe_dump(h,open(p,'w'),sort_keys=False,allow_unicode=True); mark(i); print('folded onto',wid)
    elif c=='hold':
        i,why=sys.argv[2],sys.argv[3]; p=IN+'/_holds.yaml'
        h=yaml.safe_load(open(p)) if os.path.exists(p) else []
        h.append({'id':i,'title':byid[i]['title'],'author':byid[i]['author'],'reason':why}); yaml.safe_dump(h,open(p,'w'),sort_keys=False,allow_unicode=True); mark(i); print('held')
    elif c=='count':
        for i,g in n.items():
            k=ncards(n,i)
            if k>=int(sys.argv[2] if len(sys.argv)>2 else 9): print(k,i)
