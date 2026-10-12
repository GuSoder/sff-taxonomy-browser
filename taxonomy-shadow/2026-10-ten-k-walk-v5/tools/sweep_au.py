import json,sys
a=json.load(open('/tmp/sw/auth.json'))
for q in sys.argv[1:]:
    for k,v in a.items():
        if q.lower() in k:
            print(k,[(t,l,len(b)) for t,l,b in v])
