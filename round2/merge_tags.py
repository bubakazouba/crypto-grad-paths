import json
P=r'C:\Users\slash\crypto-grad-paths\schools.json'
S=json.load(open(P,encoding='utf-8'))
T={}
for i in range(4): T.update(json.load(open(f'tags_{i}.json',encoding='utf-8')))
import os
if os.path.exists('tags_extra.json'): T.update(json.load(open('tags_extra.json',encoding='utf-8')))
MY=['lower bounds','memory checking','ORAM','PIR','garbling','oblivious algorithms','lattices/PQC']
YEARS={0:1.5,1:1.5,2:1.5,3:2,4:2,5:2,6:1.5,7:2,8:2,9:1.5,10:2,11:2,12:2,13:1.5,14:2,15:1.5,16:2,17:2,18:2,19:2,20:2,22:5/3,23:2,24:2,25:2,26:2,27:2,28:2,29:1.5,30:1.5,31:2,32:2,33:1.5,34:2,36:2,37:1,38:1.5,39:2,40:5/3,41:2,42:2,43:1.5,44:2,45:2,46:2,47:2,48:1.5,49:2,50:2,51:2,52:2,53:1.5,54:2,55:2,56:1.5,57:1.25,58:1}
ASSUMED={5,18,24,31,34,41}
miss=[]
for i,s in enumerate(S):
    if s.get('baseline'): continue
    if i in YEARS and 'years' not in s['program']:
        s['program']['years']=round(YEARS[i],2)
        s['program']['years_note']=('years assumed (no official length; matches the tuition total\'s term count)' if i in ASSUMED else 'years = the term count used in the tuition total')
    for p in s['professors']:
        k=s['short']+'|'+p['name']
        t=T.get(k)
        if not t: miss.append(k); continue
        p['research_tags']=t['research_tags']
        p['tag_evidence']=t.get('evidence',{})
        if p.get('crypto_core')!='not-crypto': p['crypto_core']=t.get('crypto_core')
        if t.get('dblp_suspect'): p['dblp_suspect']=t.get('suspect_reason') or True
        p['tags_source']='dblp titles 2021-2026 via sparql.dblp.org, classified against a fixed vocabulary'
    fp=[p['name'] for p in s['professors'] if set(p.get('research_tags',[]))&set(MY) and p.get('crypto_core')!='not-crypto']
    s['fit_score']=len(fp); s['fit_profs']=fp
json.dump(S,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('missing',miss)
