import json,os,sys
P=r'C:\Users\slash\crypto-grad-paths\schools.json'
S=json.load(open(P,encoding='utf-8'))
base=[s for s in S if s.get('baseline')]
S=[s for s in S if not s.get('baseline')]
assert len(S)==59
def load(f):
    return json.load(open(f,encoding='utf-8')) if os.path.exists(f) else {}
PH={};[PH.update(load(f)) for f in ['phd_1.json','phd_2.json']]
CO={};[CO.update(load(f)) for f in ['parts/p0.json','parts/p1.json','parts/p3.json','parts/p4.json','coa_rest.json','coa_s.json','coa_t.json','coa_u.json']]
nph=nco=nev=0
for i,s in enumerate(S):
    k=str(i)
    v=PH.get(k)
    if v is not None:
        ph=v.get('phd')
        if ph and ph.get('deadline_iso'):
            s['phd']={kk:ph.get(kk) for kk in ('deadline_iso','priority_iso','url','quote','note')};nph+=1
            s.pop('phd_null_note',None)
        else:
            s['phd']=None;s['phd_null_note']=v.get('phd_null_note') or (ph or {}).get('note') or 'PhD deadline not found on an official page.'
        mp=v.get('ms_phd') or {}
        ev={kk:vv for kk,vv in mp.items() if isinstance(vv,dict) and vv.get('value') not in (None,'')}
        s['ms_phd']=ev
        if ev: nev+=1
    elif s.get('phd_direct') and s['phd_direct'].get('deadline_iso'):
        pd=s['phd_direct'];s['phd']={'deadline_iso':pd['deadline_iso'],'priority_iso':pd.get('priority_iso'),'url':pd['url'],'note':pd.get('note')};nph+=1
    c=CO.get(k)
    if c is not None:
        if c.get('living_usd') is not None:
            s['cost']={kk:c.get(kk) for kk in ('coa_year','months','living_usd','fees_usd','health_usd','url','quote','basis','note','fees_included_in_tuition')};nco+=1
        else:
            s['cost']={'living_usd':None,'note':c.get('note') or 'No official graduate cost-of-attendance figure found.','url':c.get('url')}
for s in S:
    if s['short']=='Texas A&M University':
        s['program']['years']=1.5
        if s.get('cost'):
            s['cost']['fees_usd']=0
            s['cost']['basis']=(s['cost'].get('basis') or '')+' Round 2: the Engineering Program Fee is already inside the tuition total above, so fees here are 0 to avoid double counting.'
json.dump(base+S,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('phd',nph,'cost',nco,'evidence',nev,'of',len(S))
print('no phd:',[s['short'] for s in S if not s.get('phd')])
print('no cost:',[s['short'] for s in S if not (s.get('cost') or {}).get('living_usd')])
