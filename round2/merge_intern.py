import json
P=r'C:\Users\slash\crypto-grad-paths\internships.json'
I=json.load(open(P,encoding='utf-8'))
G={}
for f in ['part_A.json','part_B.json','part_C.json','part_D.json']: G.update(json.load(open(f,encoding='utf-8')))
for k,v in G.items():
    x=I[int(k)]
    x['gates']=v.get('gates',[])
    for f in ('letter_value','letter_value_reason','letter_value_url','event_type'):
        if v.get(f) is not None: x[f]=v[f]
    if v.get('corrections'): x['review2_corrections']=v['corrections']
def idx(org,prog):
    for i,x in enumerate(I):
        if x['org'].startswith(org) and prog in x['program_name']: return i
    raise KeyError(org+prog)
# structured corrections
i=idx('Cloudflare','Research'); x=I[i]
x['url']='https://job-boards.greenhouse.io/cloudflare'; x['status']='not yet posted'
x['notes']=(x.get('notes') or '')+' Round 2: the old link was a builtin.com copy of the Summer 2026 posting (removed May 2026). As of 2026-11-06 Cloudflare\'s Greenhouse board lists no 2027 Research intern role (only Software Engineer Intern (2027), Product Manager Intern (2027) and a People Team intern), so the URL now points to the board.'
i=idx('IAS / Park City','PCMI'); I[i]['ms_students_eligible']='yes'
i=idx('SLMath','Summer Graduate'); x=I[i]
x['eligibility']='"Graduate students from MSRI Academic Sponsoring Institutions or from the mathematics department of any U.S. institution are eligible to be nominated by their Director of Graduate Studies. Admission is on a first-come, first-served basis up to the limits of the capacity of the school. Early nominations are not accepted." So the CSULA math graduate director must submit the nomination as soon as nominations open.'
x['eligibility_source']='https://legacy.slmath.org/web/msri/education/for-graduate-students'
x['prestige_tier']='Good'; x['prestige_justification']='Well-run two-week math graduate school, but lectures rather than crypto research; demoted from Top in round 2 (letter value for a theory-crypto PhD app is low).'
i=idx('IAS / Park City','PCMI'); x=I[i]
x['prestige_tier']='Good'; x['prestige_justification']='Prestigious IAS math school, but a lecture-based graduate summer school, not crypto research; demoted from Top in round 2.'
for x in I:
    if x['org'].startswith('U.S. Department of Defense') and 'SMART' in x['program_name']:
        x['letters_required']='yes (2-3 references)'
        x['letters_required_reason']='"At least two completed references are required. Applicants may enter up to three references." (SMART knowledge base)'
        x['letters_required_source']='https://www.smartscholarship.org/smart/en?id=kb_article&sys_id=84f05b02db5ac3006bb8f4b40f9619cc'
        x['category_note']='Scholarship-for-service, not an internship: "Accept a one-for-one post graduation service commitment as a civilian employee of the Department of War".'
    if x['org'].startswith('IDA Center for Communications Research, Princeton'):
        x['url']='https://www.mathjobs.org/jobs/IDA/CCRPSCAMP'
    if x['org'].startswith('IDA Center for Communications Research, La Jolla'):
        x['letters_of_recommendation']='Three references who can speak to your research, OR letters; letters optional. "Provide three references who can speak knowledgeably about your research contributions or letters of recommendation. Note that you are not required to submit letters of recommendation."'
# re-rank picks: value of the letter to a theory-crypto PhD application first
LV={'high':0,'medium':1,'low':2}
R={'Reachable':0,'Moderate':1,'Hard':2,'Very hard':3}
T={'theory':0,'applied-research':1}
def blocked(x): return any(g.get('risk_for_him')=='blocks' for g in x.get('gates',[]))
for x in I: x.pop('top_pick',None); x.pop('rank_reason',None)
C=[x for x in I if x.get('track') in T and x.get('ms_students_eligible')!='no' and not blocked(x) and x.get('status')!='closed' and x.get('letter_value') in ('high','medium')]
C.sort(key=lambda x:(LV[x['letter_value']],T[x['track']],R.get(x.get('difficulty_for_sahmoud'),9)))
for n,x in enumerate(C[:10],1):
    x['top_pick']=n
    risks=[g['label'] for g in x.get('gates',[]) if g.get('risk_for_him')=='risk']
    x['rank_reason']=f"Ranked by the value of the likely letter to a theory-crypto PhD application ({x['letter_value']}), then theory before applied, then reachability ({x.get('difficulty_for_sahmoud')})."+(f" Watch: {'; '.join(risks)}." if risks else '')+" Rows that are PhD-only, closed, or blocked by a hard gate are not ranked. A self-arranged summer RA with a professor on your topics (Other routes tab) is likely worth more than any of these."
json.dump(I,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
for x in C[:10]: print(x['top_pick'],x['org'][:45],'|',x['letter_value'],x['track'],x.get('difficulty_for_sahmoud'))
