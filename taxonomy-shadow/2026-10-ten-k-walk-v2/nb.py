import json,sys,os
q=json.load(open('/tmp/shadow/queue.json'))
done=set()
if os.path.exists('/tmp/shadow/results.txt'):
    for l in open('/tmp/shadow/results.txt'):
        p=l.rstrip('\n').split('|')
        if p[0] in('C','H','+C'):
            for x in p[2 if p[0]!='H' else 1].split(','):
                x=x.strip()
                if x.isdigit():done.add(int(x))
                elif '-' in x:
                    a,b=x.split('-');done.update(range(int(a),int(b)+1))
import sys as _s;_s.path.insert(0,'/tmp/sweep')
from xref import ns
import collections,re
ex=collections.defaultdict(list)
def sn(a):
    t=re.sub(r"[^A-Za-z' -]",'',a).split();return t[-1].lower() if t else ''
for n in ns:
    for w in n.get('works',[]):
        for a in (w.get('authors') or []):ex[sn(a)].append((w['title'],n['id']))
n=int(sys.argv[1]);k=0;shown=[]
imp={'Gollancz':'Gol','Harper Voyager':'HV','Tor Books':'Tor','Tordotcom':'Tdc','Del Rey':'DR','Ace':'Ace','DAW':'DAW','Baen':'Baen','Spectra':'Spec','Orb Books':'Orb','Tor Science Fiction':'TorSF','Tor Fantasy':'TorF','Forge Books':'Forge','Tor Nightfire':'Night','Bramble':'Bram'}
for r in q:
    if r['i'] in done:continue
    im=r['imprints'].split('; ')[0];im=imp.get(im,im[:6])
    print(f"{r['i']}|{r['author'][:24]}|{r['title'][:60]}|{r['year']}|{im}|{r['genre_tags'][:3]}")
    k+=1;shown.append(r)
    if k>=n:break
seen=set()
for r in shown:
    s_=sn(r['author'])
    if s_ in seen or s_ not in ex:continue
    seen.add(s_);print('TREE',s_,':',' ; '.join(f'{t[:30]}@{l}' for t,l in ex[s_][:8]))
print('done',len(done),'of',len(q))
