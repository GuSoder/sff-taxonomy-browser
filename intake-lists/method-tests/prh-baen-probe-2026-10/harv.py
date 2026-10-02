import json,urllib.request,concurrent.futures as cf
H={'User-Agent':'Mozilla/5.0 Chrome/124','Content-Type':'application/json'}
def post(p,d):
    r=urllib.request.Request('https://randomhousebooks.com/wp-json/dwt/v2/'+p,json.dumps(d).encode(),H);return json.load(urllib.request.urlopen(r,timeout=40))
codes={'DR':'Del Rey','A0':'Ace','A8':'Ace','A9':'Ace','161':'DAW','142':'Random House Worlds','1R':'Spectra','181':'Inklore','BB':'Ballantine','R2':'Ballantine','1A':'Bantam','AA':'Berkley','B0':'Berkley','CZ':'Berkley','AQ':'Berkley'}
def page(a):
    c,s=a
    for _ in range(3):
        try:
            d=post('list-title',{'imprintCode':c,'rows':100,'start':s});return c,d['data']['works']
        except Exception:pass
    return c,[]
jobs=[]
for c in codes:
    n=post('list-title',{'imprintCode':c,'rows':1})['recordCount']
    jobs+=[(c,s) for s in range(0,n,100)]
out=[]
with cf.ThreadPoolExecutor(6) as ex:
    for c,ws in ex.map(page,jobs):
        for w in ws:out.append(dict(imprint=codes[c],code=c,title=w['title'],sub=w['subtitle'],onsale=w['onsale'],author=[a['authorDisplay'] for a in w['author'] if a['roleCode']=='A'][:2],series=(w['series'] or {}).get('seriesName'),isbn=w['isbn'],url=w['seoFriendlyUrl']))
json.dump(out,open('prh_titles.json','w'));print(len(out))
