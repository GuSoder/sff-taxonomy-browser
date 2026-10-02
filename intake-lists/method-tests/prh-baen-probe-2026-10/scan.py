import json,urllib.request,itertools,string,concurrent.futures as cf
H={'User-Agent':'Mozilla/5.0 Chrome/124','Content-Type':'application/json'}
B='https://randomhousebooks.com/wp-json/dwt/v2/'
def post(p,d):
    r=urllib.request.Request(B+p,json.dumps(d).encode(),H)
    return json.load(urllib.request.urlopen(r,timeout=30))
def code(c):
    try:
        d=post('list-title',{'imprintCode':c,'rows':1})
        n=d['recordCount']
        if not n:return None
        i=d['data']['works'][0]['isbnStr']
        s=post('single-title',{'isbn':i})['data']['frontlistiestTitle']['imprint']
        return (c,n,s['name'],s.get('family'))
    except Exception as e:return None
cs=[''.join(x) for x in itertools.product(string.ascii_uppercase+string.digits,repeat=2)]+[str(i) for i in range(100,300)]
with cf.ThreadPoolExecutor(8) as ex:
    res=[r for r in ex.map(code,cs) if r]
json.dump(res,open('codes.json','w'))
for r in sorted(res,key=lambda x:x[2]):print(r)
