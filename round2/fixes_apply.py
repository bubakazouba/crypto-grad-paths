import json
P=r'C:\Users\slash\crypto-grad-paths\schools.json'
S=json.load(open(P,encoding='utf-8'))
by={s['short']:s for s in S}
def g(n): return by[n]
# 1 UMass: non-thesis
s=g('University of Massachusetts Amherst');p=s['program']
p['thesis']='no';p['name']="MS in Computer Science - On Campus (non-thesis; optional 6-credit Master's Project)"
p['thesis_source']='https://cics.umass.edu/academics/academic-policies/graduate-programs-policies/ms-degree-requirements'
p['thesis_quote']="\"The Master's in Computer Science degree is a non-thesis degree\"; \"the MS program offers a Master's Project 6 credit research opportunity.\""
s['notes']=s['notes'].replace("thesis set to 'yes' only because of the 6-credit research Master's Project; there is no formal thesis.","Thesis corrected to 'no' (round-2 review): the CICS MS requirements page says it is a non-thesis degree; the 6-credit Master's Project is the research option.")
# 7 Columbia wording
s=g('Columbia University');p=s['program']
p['name']='M.S. in Computer Science - MS Thesis pathway (you arrange a CS faculty thesis advisor)'
s['research_fit_note']=s['research_fit_note'].replace('it needs a CS faculty member to agree to advise (faculty invite)','you must arrange a CS faculty member who agrees to advise ("You are required to arrange for a Computer Science Faculty member who agrees to advise the thesis"); it is not invitation-only')
# 6 Oregon State fee
s=g('Oregon State University');p=s['program']
p['app_fee_usd']=85;p['app_fee_url']='https://graduate.oregonstate.edu/admissions/process'
s['notes']=s['notes'].replace("app_fee_usd is null: no OSU page fetched states the amount (old fee pages redirect to the Graduate Admissions homepage); search snippets suggest $85 but this was not confirmed on a fetched official page.","App fee $85 (domestic and international degree-seeking) per the OSU Graduate School application-process page (graduate.oregonstate.edu/admissions/process), read through its search-index copy on 2026-11-06 because the live URL now redirects.")
# 8 TAMU program fee
s=g('Texas A&M University');p=s['program']
p['total_tuition_usd']=33642
p['tuition_basis']='Fall 2026/Spring 2027 graduate non-resident tuition $836.40/SCH x 30 hours = $25,092, PLUS the Engineering Program Fee from the same rate sheet ($2,565 per semester at 9+ hours; $285/SCH below 9): 3 semesters at 9 hrs = $7,695, plus 3 hrs x $285 = $855, so $8,550. Total $33,642. Other required fees (Engineering fees row $431-$1,985/semester) still excluded. Round-2 review: the earlier $25,092 omitted the program fee.'
# 9 Princeton closed
s=g('Princeton University');s['program']['closed_fall2027']=True
for n in ['Yale University','Cornell University']: g(n)['funded_ms']=True
s=g('University of Chicago');s['program']['thesis']='research track'
# USC faculty labels
s=g('University of Southern California')
for pr in s['professors']:
    if pr['name']=='Jiapeng Zhang':
        pr['role_note']='crypto-adjacent theorist, not a core cryptographer';pr['crypto_core']='adjacent';pr['affiliation_source']='https://viterbi.usc.edu/directory/faculty/Zhang/Jiapeng';pr['title']='Assistant Professor of Computer Science'
    if pr['name']=='Mengyuan Li':
        pr['role_note']='systems/TEE security, not cryptography';pr['crypto_core']='not-crypto';pr['affiliation_source']='https://viterbi.usc.edu/directory/faculty/Li/Mengyuan';pr['title']='Assistant Professor of CS and ECE ("Trusted Execution Environments, confidential computing, ... micro-architectural security")'
if 'No core cryptographer' not in s['research_fit_note']:
    s['research_fit_note']='No core cryptographer found at USC CS (round-2 review): Jiapeng Zhang is a crypto-adjacent theory professor; Mengyuan Li works on systems/TEE security; Muhammad Naveed is not in the current USC CS faculty directory. '+s['research_fit_note']
s['extra_events']=[{'iso':'2027-01-15','kind':'Deferral','label':'Deadline','title':'USC MS CS: defer your admission to Fall 2027 (updated materials due)','url':'https://viterbigradadmission.usc.edu/faq/','note':'USC Viterbi FAQ: you may request to defer "within one (1) year of your original application semester" (a Fall 2026 admit can move to Spring 2027 or Fall 2027); "All updated application materials need to be received by the application deadline for the new semester to which you are applying"; "The application deadline for Fall admission is January 15". No separate date is printed for the Deferral Request Form itself. "Admission is not guaranteed."'}]
# UCR
s=g('University of California, Riverside')
for pr in s['professors']:
    if pr['name']=='Amey Bhangale':
        pr['role_note']='not a cryptographer (PCPs, hardness of approximation)';pr['crypto_core']='not-crypto';pr['affiliation_source']='https://theoryofcomputing.org/articles/v016a016/'
if 'no confirmed cryptography' not in s.get('research_fit_note',''):
    s['research_fit_note']='UC Riverside has no confirmed cryptography faculty (round-2 review): the only listed person, Amey Bhangale, works on PCPs and hardness of approximation, and his dblp record mixes in unrelated papers. '+s.get('research_fit_note','')
# NYU
s=g('New York University')
for pr in s['professors']:
    if pr['name']=='Joseph Bonneau': pr['role_note']='not on the NYU theory-group page; current NYU status unverified'
names={x['name'] for x in s['professors']}
src='https://cs.nyu.edu/theory-group/'
if 'Oded Regev' not in names:
    s['professors'].append({'name':'Oded Regev','dblp':'https://dblp.org/pid/r/OdedRegev','title':'Faculty, NYU Courant ("Lattice-based crypto, quantum, mathematical aspects of TCS")','affiliation_source':src,'source':'NYU theory-group page (added round 2)'})
if 'Tony Metger' not in names:
    s['professors'].append({'name':'Tony Metger','dblp':'https://dblp.org/pid/224/0245','title':'Faculty, NYU Courant ("Quantum computation, cryptography, and information theory")','affiliation_source':src,'source':'NYU theory-group page (added round 2)'})
s=g('Massachusetts Institute of Technology')
if 'Round-2 check' not in s['notes']:
    s['notes']+=' Round-2 check: the CIS group page (https://toc.csail.mit.edu/cis) names founders Goldwasser, Micali and Rivest and says the group "is currently led by Professors Yael Kalai and Vinod Vaikuntanathan"; whether Rivest or Micali take new PhD students was not verified, so they are not added.'
for s in S: s['n_professors']=len(s['professors'])
json.dump(S,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
