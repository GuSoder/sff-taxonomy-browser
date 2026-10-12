#!/usr/bin/env python3
"""Fold books into an existing card. Usage: fold_books.py card_title leaf-id '[{"title":..,"year":..},..]' [old=>new rationale replacement]"""
import json, sys, re, yaml, glob
title, leaf, books = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
rep = sys.argv[4].split('=>',1) if len(sys.argv)>4 else None
s=open('index.html',encoding='utf-8').read()
m=re.search(r'(const nodes=)(.*)',s)
nodes,end=json.JSONDecoder().raw_decode(m.group(2))
n=next(x for x in nodes if x['id']==leaf); w=next(x for x in n['works'] if x['title']==title)
w.setdefault('books',[{'title':w['title'],'year':w.get('year') or w.get('first_published')}])
for b in books: w['books'].append(b)
for k in ('placement_note',):
    if rep and w.get(k): w[k]=w[k].replace(rep[0],rep[1])
s=s[:m.start(2)]+json.dumps(nodes,ensure_ascii=False,separators=(',',':'))+m.group(2)[end:]+s[m.end(2):]
open('index.html','w',encoding='utf-8').write(s)
f=glob.glob(f'taxonomy/**/{leaf}/works/*.yaml',recursive=True)
for p in f:
    d=yaml.safe_load(open(p))
    if d['title']==title:
        d.setdefault('books',[{'title':d['title'],'year':d.get('first_published')}]); d['books']+=books
        if rep: d['placement_rationale']=d['placement_rationale'].replace(rep[0],rep[1])
        yaml.safe_dump(d,open(p,'w'),sort_keys=False,allow_unicode=True,width=160); print('folded',title,len(books))
