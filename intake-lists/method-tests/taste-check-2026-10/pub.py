import json,collections,urllib.request,urllib.parse,concurrent.futures as cf,re
m=json.load(open('mentions.json'))
c=collections.defaultdict(set)
for k,u,v in m:
    for t,a in v:c[(t,a)].add((k,u))
# merge case dups
d={}
for (t,a),s in c.items():
    d.setdefault((t.lower(),a),set()).update(s)
items=[(k,s) for k,s in d.items() if len(s)>=2]
def look(k):
    t,a=k
    url='https://openlibrary.org/search.json?'+urllib.parse.urlencode({'title':t,'author':a,'fields':'title,author_name,publisher,first_publish_year','limit':5})
    try:return json.load(urllib.request.urlopen(url,timeout=25))['docs']
    except Exception as e:return None
with cf.ThreadPoolExecutor(8) as ex:
    res=list(ex.map(lambda x:look(x[0]),items))
out=[]
for (k,s),r in zip(items,res):
    out.append(dict(title=k[0],author=k[1],blog=sum(1 for x in s if x[0]=='blog'),yt=sum(1 for x in s if x[0]=='yt'),docs=r))
json.dump(out,open('ol.json','w'))
print(sum(1 for o in out if o['docs']), len(out))
