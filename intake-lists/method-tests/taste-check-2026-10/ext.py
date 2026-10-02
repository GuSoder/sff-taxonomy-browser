import json,hashlib,os,re,collections
o=json.load(open('/tmp/taste/srcs.json'))
def rd(u):
    fn='/tmp/taste/pg/'+hashlib.md5(u.encode()).hexdigest()+'.txt';return open(fn).read() if os.path.exists(fn) else ''
NAME=r"[A-Z][a-zA-Z'’\-\.]+(?: (?:[A-Z][a-zA-Z'’\-]+|[A-Z]\.|de|van|von|le|la|St\.)){1,3}"
TW=r"(?:[A-Z0-9][\w'’:\-\!\?\.&]*)(?:(?: |, )(?:[A-Za-z0-9][\w'’:\-\!\?\.&]*)){0,9}"
pat=re.compile(r"(?:\*\*|\*|_|\"|“|‘)?(%s)(?:\*\*|\*|_|\"|”|’)?,? by (%s)"%(TW,NAME))
STOP=set('the a an and of in to is it for on with as by at from this that these those i you we they he she was were are be been my your our their his her its if or but so not no yes one two three first second third new best top book books novel read'.split())
def mentions(text):
    res=set()
    for m in pat.finditer(text):
        t,a=m[1].strip(' *_"“”.,'),m[2].strip()
        # trim leading lowercase-start fragments / long lead-ins
        words=t.split()
        # strip leading words until a plausible title start (capitalized, not stopword at pos0 unless 'The/A')
        while words and words[0].lower() in ('and','but','so','from','with','also','plus','then','in','is','was','by','of','as','at','for','on','or','if','that','this','it','my','i','we','book','novel','titled','called','read','reading','fantasy','sci-fi') :words=words[1:]
        if not words or len(words)>9:continue
        t=' '.join(words)
        if len(t)<3:continue
        res.add((t,a))
    return res
if __name__=='__main__':
    src={}
    for k in('blog','yt'):
        for u,t,d in o[k]:
            if k=='yt' and 'watch?v=' not in u:continue
            tx=rd(u)
            if len(tx)<1500:continue
            src[(k,u)]=mentions(tx)
    json.dump([[k,u,sorted(v)] for (k,u),v in src.items()],open('/tmp/taste/mentions.json','w'))
    for k in('blog','yt'):
        n=[len(v) for (kk,u),v in src.items() if kk==k];print(k,len(n),sum(n))
