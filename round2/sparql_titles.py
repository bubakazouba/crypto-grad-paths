import json,sys,time,urllib.request,urllib.parse,os
S=json.load(open(r'C:\Users\slash\crypto-grad-paths\schools.json',encoding='utf-8'))
extra=json.load(open(sys.argv[1],encoding='utf-8')) if len(sys.argv)>1 else []
out=json.load(open('titles.json',encoding='utf-8')) if os.path.exists('titles.json') else {}
todo=[(r['short'],p['name'],p['dblp']) for r in S for p in r['professors'] if p.get('dblp')]+[tuple(e) for e in extra]
Q='''PREFIX dblp: <https://dblp.org/rdf/schema#>
SELECT ?p ?t ?y ?v WHERE { ?p dblp:authoredBy <%s> ; dblp:title ?t ; dblp:yearOfPublication ?y .
OPTIONAL { ?p dblp:publishedIn ?v } FILTER(?y >= "2021"^^<http://www.w3.org/2001/XMLSchema#gYear>) }'''
for sch,name,url in todo:
    key=sch+'|'+name
    if key in out and 'titles' in out[key]: continue
    pid=url.rstrip('/').split('/pid/')[-1]
    q=Q%('https://dblp.org/pid/'+pid)
    u='https://sparql.dblp.org/sparql?'+urllib.parse.urlencode({'query':q})
    for a in range(4):
        try:
            x=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'Accept':'application/sparql-results+json','User-Agent':'crypto-grad-paths'}),timeout=90).read());break
        except Exception as e:
            print('retry',name,e,flush=True);time.sleep(5*(a+1))
    else:
        out[key]={'error':'fetch failed','dblp':url};continue
    T={}
    for b in x['results']['bindings']:
        y=int(b['y']['value'][:4])
        if y>2026: continue
        k=b['p']['value']
        T.setdefault(k,{'y':y,'t':b['t']['value'],'v':set()})
        if 'v' in b: T[k]['v'].add(b['v']['value'])
    L=[{'y':v['y'],'t':v['t'],'v':', '.join(sorted(v['v'])),'uri':k} for k,v in T.items()]
    L.sort(key=lambda z:-z['y'])
    out[key]={'dblp':url,'pid':pid,'titles':L}
    print(name,len(L),flush=True)
    json.dump(out,open('titles.json','w',encoding='utf-8'),ensure_ascii=False)
    time.sleep(0.5)
json.dump(out,open('titles.json','w',encoding='utf-8'),ensure_ascii=False)
print('DONE',len(out))
