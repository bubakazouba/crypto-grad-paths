import json
P=r'C:\Users\slash\crypto-grad-paths\schools.json'
S=json.load(open(P,encoding='utf-8'))
c=json.load(open('coa_csula.json',encoding='utf-8'))['csula']
S=[s for s in S if not s.get('baseline')]
row={
 "school":"California State University, Los Angeles (your current program)","short":"CSULA (current)","csrankings_name":None,
 "city":"Los Angeles","state":"CA","region":"SoCal","baseline":True,"n_professors":0,"professors":[],
 "program":{"name":"M.S. in Mathematics (current program, baseline)","url":"https://www.calstatela.edu/nss/math/masters-degree-mathematics",
  "length":"\"You can finish the program in two years by taking an average of 2.5 courses per semester.\"","years":2,
  "years_note":"years from the official program page","thesis":"yes",
  "total_tuition_usd":17096,"total_tuition_resident_usd":17096,
  "tuition_basis":"2026-27 CA-resident graduate tuition $4,274 per semester (6.1+ units) x 4 semesters. Campus fees ($547.03/semester) are counted in the realistic cost below.",
  "tuition_url":c['tuition_url'],"resident_basis":"$4,274/semester x 4 semesters (resident); campus fees $547.03/semester counted separately.","resident_url":c['tuition_url'],
  "deadline_fall2027":None,"deadline_note":"Already enrolled (started Fall 2026).","deadline_url":None,"gre":None,"app_fee_usd":None,
  "funding_note":None,"priority_iso":None,"deadline_iso":None},
 "cost":{"coa_year":c['coa_year'],"months":9,"living_usd":c['living_usd'],"fees_usd":round(c['fees_usd']),"health_usd":None,"url":c['url'],
  "quote":c['quote'],"basis":c['basis']+" Commuter column instead: living $21,706."},
 "alt_programs":[],"research_fit_note":"Thesis option (MATH 5990, needs a 3.5 program GPA) or comprehensive exams. A thesis with a crypto-adjacent advisor is the cheapest way to a first paper. No crypto faculty listed here; compare every other row against staying put.",
 "notes":"Baseline row added in round 2 so every cost and deadline can be read as 'vs. staying here'.","sources":[c['url'],c['tuition_url'],"https://www.calstatela.edu/nss/math/masters-degree-mathematics"],
 "fit_score":0,"fit_profs":[]}
S.insert(0,row)
json.dump(S,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(S))
