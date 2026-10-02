import re,json,urllib.request,concurrent.futures as cf,html,sys
H={'User-Agent':'Mozilla/5.0 Chrome/124'}
def get(u):
    for _ in range(3):
        try:return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30).read().decode('utf8','ignore')
        except Exception as e:pass
    return ''
def parse(t):
    out=[]
    for a in re.findall(r'<article[^>]*>.*?</article>',t,re.S):
        m=re.search(r'/titles/([a-z0-9-]+)/([a-z0-9-]+)/(\d{13})/',a)
        if not m:continue
        ti=re.search(r'<h\d[^>]*>(.*?)</h\d>',a,re.S);ti=html.unescape(re.sub('<[^>]+>','',ti[1])).strip() if ti else m[2]
        co=re.search(r'Contributors\s*(.*?)\s*(Series:|Price)',re.sub(r'<[^>]+>',' ',a),re.S);co=re.sub(r'\s+',' ',co[1]).strip() if co else m[1]
        out.append((m[3],ti,co))
    return out
def harvest(q,maxp=80):
    first=get(f'https://www.hachettebookgroup.com/?s={q}&post_type=title')
    n=re.search(r'([\d,]+) results',first);n=int(n[1].replace(',','')) if n else 0
    pages=min(maxp,(n+23)//24)
    res=parse(first)
    def f(p):return parse(get(f'https://www.hachettebookgroup.com/page/{p}/?s={q}&post_type=title'))
    with cf.ThreadPoolExecutor(6) as ex:
        for r in ex.map(f,range(2,pages+1)):res+=r
    return n,res
if __name__=='__main__':
    allr={}
    for q in sys.argv[1:]:
        n,r=harvest(q);print(q,n,len(r),flush=True)
        for x in r:allr[x[0]]=x
    old=json.load(open('hbg_all.json')) if __import__('os').path.exists('hbg_all.json') else {}
    old.update(allr);json.dump(old,open('hbg_all.json','w'));print(len(old))
