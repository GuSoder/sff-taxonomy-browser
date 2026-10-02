import json,urllib.request,urllib.parse,time
def q(params,idx='macmillan-us_products'):
    body=json.dumps({"params":urllib.parse.urlencode(params)}).encode()
    r=urllib.request.Request(f"https://34C0LL333A-dsn.algolia.net/1/indexes/{idx}/query",data=body,headers={'X-Algolia-Application-Id':'34C0LL333A','X-Algolia-API-Key':'<public search key embedded in us.macmillan.com page source, redacted>'})
    return json.load(urllib.request.urlopen(r,timeout=40))
