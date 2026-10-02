import re,json,urllib.request,concurrent.futures as cf,html
U='https://www.baen.com/allbooks/category/index/id/1972/options/available?page=%d'
def pg(p):
    for _ in range(3):
        try:
            h=urllib.request.urlopen(urllib.request.Request(U%p,headers={'User-Agent':'Mozilla/5.0 Chrome/124'}),timeout=30).read().decode()
            break
        except Exception:h=''
    out=[]
    for m in re.finditer(r'<div class="book-card[^"]*"[^>]*?data-release-date="([^"]*)"(.*?)(?=<div class="book-card |$)',h,re.S):
        b=m.group(2)
        n=re.search(r'slider-book-name">([^<]+)',b);a=re.search(r'slider-book-description">([^<]*)',b);u=re.search(r'href="(https://www.baen.com/[^"]+\.html)"',b)
        if n:out.append(dict(title=html.unescape(n[1]).strip(),author=html.unescape(a[1]).replace('by ','',1).strip() if a else '',date=m[1],url=u[1] if u else '',page=p))
    return p,out
res=[]
with cf.ThreadPoolExecutor(6) as ex:
    for p,o in ex.map(pg,range(1,100)):res+=o
json.dump(res,open('baen_titles.json','w'));print(len(res),max(r['page'] for r in res))
