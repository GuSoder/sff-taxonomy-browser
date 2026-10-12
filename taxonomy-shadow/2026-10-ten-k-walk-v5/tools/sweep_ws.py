import sys,subprocess,json,concurrent.futures as cf
items=[l.strip().split('|',1) for l in sys.stdin if l.strip()]
def f(it):
    i,q=it
    try:
        o=subprocess.run(['tools','web_search','--query',q,'--limit','2','--json'],capture_output=True,text=True,timeout=60).stdout
        d=json.loads(o)
        return i,' // '.join(x['domain']+': '+' '.join(x['highlights'])[:330].replace('\n',' ') for x in d[:2])
    except Exception as e: return i,'ERR'
with cf.ThreadPoolExecutor(6) as ex:
    for i,o in ex.map(f,items): print(i,'=>',o,'\n')
