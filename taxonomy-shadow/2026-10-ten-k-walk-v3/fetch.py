import json,sys,urllib.request,urllib.parse,concurrent.futures as cf,os,time
q=json.load(open('../queue.json'));held=json.load(open('../held2.json'))
ids=sorted(set(map(int,held)))
out='ol.jsonl'
done=set()
if os.path.exists(out):
    for l in open(out): done.add(json.loads(l)['i'])
todo=[i for i in ids if i not in done]
def get(u):
    for t in range(3):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'sff-taxonomy/1.0'}),timeout=20))
        except Exception as e: time.sleep(1+t)
    return None
def work(i):
    r=next(x for x in q if x['i']==i) if False else Q[i]
    t=r['title'].split('(')[0].strip();a=r['author']
    d=get('https://openlibrary.org/search.json?'+urllib.parse.urlencode({'title':t,'author':a,'limit':1,'fields':'key,title,subject,first_sentence'}))
    res={'i':i,'subj':[],'desc':''}
    if d and d.get('docs'):
        x=d['docs'][0];res['subj']=x.get('subject',[])[:12];res['ot']=x.get('title')
        w=get('https://openlibrary.org'+x['key']+'.json')
        if w:
            ds=w.get('description','')
            if isinstance(ds,dict): ds=ds.get('value','')
            res['desc']=ds[:400]
    return res
Q={r['i']:r for r in q}
lim=int(sys.argv[1]) if len(sys.argv)>1 else len(todo)
with open(out,'a') as f, cf.ThreadPoolExecutor(16) as ex:
    for r in ex.map(work,todo[:lim]): f.write(json.dumps(r)+'\n'); f.flush()
