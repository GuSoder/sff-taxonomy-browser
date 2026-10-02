import json,sys
q={r['i']:r for r in json.load(open('../queue.json'))}
h=sorted(map(int,json.load(open('../held2.json'))))
import os
dec=set()
if os.path.exists('decided.txt'): dec=set(int(x) for x in open('decided.txt').read().split())
rem=[i for i in h if i not in dec]
n=int(sys.argv[1]);print(len(rem),'remaining')
for i in rem[:n]: print(i,q[i]['author'][:18],'|',q[i]['title'][:44])
