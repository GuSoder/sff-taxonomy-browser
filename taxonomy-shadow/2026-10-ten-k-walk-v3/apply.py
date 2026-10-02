import sys,re,json
# batch file lines: leaf|card name|idx,idx...   or  H:REASON|idx,idx..  (ranges a-b ok)
q={r['i']:r for r in json.load(open('../queue.json'))}
def ex(s):
    o=[]
    for p in s.split(','):
        p=p.strip()
        if '-' in p: a,b=map(int,p.split('-'));o+=range(a,b+1)
        elif p: o.append(int(p))
    return o
f=sys.argv[1]
res=open('../v2/results2.txt','a');dec=open('decided.txt','a');holds=open('holds3.txt','a')
for l in open(f):
    l=l.rstrip('\n')
    if not l.strip() or l.startswith('#'): continue
    p=l.split('|')
    if p[0].startswith('H:'):
        for i in ex(p[1]): holds.write(f"{i}|{p[0][2:]}\n");dec.write(f"{i}\n")
    else:
        ids=ex(p[2])
        res.write(f"C|{p[1]}|{','.join(map(str,ids))}|{p[0]}|v3\n")
        for i in ids: dec.write(f"{i}\n")
