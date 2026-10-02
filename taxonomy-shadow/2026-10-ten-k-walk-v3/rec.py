#!/usr/bin/env python3
# usage: rec.py attrs.txt   lines: idx|form|has_magic|is_real_earth|setting|genre|tags|conf|source|note
# upserts into book-analysis/books-NNNN.yaml (250 ids per file); decision joined from results2.txt/holds3.txt
import sys,json,os,re
q={r['i']:r for r in json.load(open('../queue.json'))}
dec={}
for l in open('../v2/results2.txt'):
    p=l.rstrip('\n').split('|')
    if p[0] in('C','+C'):
        for x in p[2].split(','):
            if x.strip().isdigit(): dec[int(x)]=p[3]
for l in open('holds3.txt'):
    i,r=l.strip().split('|');dec[int(i)]='HOLD:'+r
KEYS=['id','title','author','form','has_magic','is_real_earth','setting','genre','tags','confidence','source','decision','note']
def q_(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"')+'"'
def load(fn):
    d={}
    if os.path.exists(fn):
        cur=None
        for l in open(fn):
            if l.startswith('- id:'): cur={'id':int(l.split(':')[1])};d[cur['id']]=cur
            elif cur is not None and l.startswith('  ') and ':' in l:
                k,v=l.strip().split(':',1);cur[k]=v.strip().strip('"')
    return d
def dump(fn,d):
    with open(fn,'w') as f:
        f.write('# per-book analysis; keys: form has_magic is_real_earth setting genre tags confidence source decision note\n')
        for i in sorted(d):
            r=d[i];f.write(f"- id: {i}\n")
            for k in KEYS[1:]:
                v=r.get(k,'')
                f.write(f"  {k}: {q_(v) if k in('title','author','note','tags') else v}\n")
files={}
for l in open(sys.argv[1]):
    l=l.rstrip('\n')
    if not l.strip() or l.startswith('#'): continue
    p=l.split('|')+['']*10
    idxs=[]
    for s in p[0].split(','):
        if '-' in s: a,b=map(int,s.split('-'));idxs+=range(a,b+1)
        else: idxs.append(int(s))
    for i in idxs:
        fn=f"book-analysis/books-{i//250*250:04d}.yaml"
        if fn not in files: files[fn]=load(fn)
        files[fn][i]={'id':i,'title':q[i]['title'],'author':q[i]['author'],'form':p[1],'has_magic':p[2],'is_real_earth':p[3],'setting':p[4],'genre':p[5],'tags':p[6],'confidence':p[7],'source':p[8],'decision':dec.get(i,'pending'),'note':p[9]}
for fn,d in files.items(): dump(fn,d)
