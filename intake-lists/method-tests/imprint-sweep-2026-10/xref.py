import json,re,datetime,collections
h=open('/home/sandbox/sff-taxonomy-browser/index.html').read();m=re.search('const nodes=(.*)',h);ns,e=json.JSONDecoder().raw_decode(m[1])
def norm(s):
    s=s.lower();s=re.sub(r'\(.*?\)','',s);s=re.sub(r'[^a-z0-9 ]',' ',s);s=re.sub(r'^(the|a|an) ','',s.strip());return re.sub(r'\s+',' ',s).strip()
tree=set()
for n in ns:
  for w in n.get('works',[]):
    tree.add(norm(w['title']))
    for b in w.get('books',[]):tree.add(norm(b['title']))
def intree(t):return norm(t) in tree
