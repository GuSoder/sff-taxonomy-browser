#!/usr/bin/env python3
"""usage: olcover.py 'Title' 'Author'  -> OL search candidates with cover ids"""
import sys,json,urllib.request,urllib.parse
t,a=sys.argv[1],sys.argv[2]
u='https://openlibrary.org/search.json?'+urllib.parse.urlencode({'title':t,'author':a,'limit':6,'fields':'key,title,author_name,first_publish_year,cover_i,edition_count,isbn'})
d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'sff-taxonomy/1.0'}),timeout=30))
for x in d['docs']:
    print(x.get('title'),'|',x.get('author_name'),'|',x.get('first_publish_year'),'| cover_i',x.get('cover_i'),'| editions',x.get('edition_count'))
