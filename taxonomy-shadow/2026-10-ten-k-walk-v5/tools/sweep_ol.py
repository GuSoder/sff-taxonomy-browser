import sys,json,urllib.parse,urllib.request,concurrent.futures as cf
V='/home/sandbox/sff-taxonomy-browser/taxonomy-shadow/2026-10-ten-k-walk-v5/sweep/verdicts-pass1.tsv'
a,b=int(sys.argv[1]),int(sys.argv[2])
rows=[l.rstrip('\n').split('\t') for l in open(V,encoding='utf-8')]
rows=[r for r in rows if len(r)>4 and r[4]=='WALK' and a<=int(r[0][2:])<=b]
def q(r):
    t=r[1]; au=r[2]
    u='https://openlibrary.org/search.json?limit=3&fields=title,author_name,first_publish_year,subject&title='+urllib.parse.quote(t)+('&author='+urllib.parse.quote(au) if au else '')
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'sff-sweep/1'}),timeout=12))['docs']
    except Exception as e: return r,'ERR'
    out=[]
    for x in d[:2]:
        sub=[s for s in x.get('subject',[]) if any(k in s.lower() for k in ['fiction','fantasy','science','anthology','short','horror','vampire','dragon','magic','alien','space'])][:4]
        out.append(f"{x.get('title')}|{','.join(x.get('author_name',[])[:2])}|{x.get('first_publish_year')}|{';'.join(sub)}")
    return r,' // '.join(out)
with cf.ThreadPoolExecutor(8) as ex:
    for r,o in ex.map(q,rows): print(r[0],'|',r[1],'|',r[2],r[3],'=>',o[:230])
