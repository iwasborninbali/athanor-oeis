import os,re,glob,json,csv,collections,math,subprocess,html
from pathlib import Path
P=Path('ranking'); root=Path.home()/'oeisdata'; refs=collections.Counter(); yrefs=collections.Counter(); rows={}; ar=re.compile(r'(?<![A-Za-z0-9])A\d{6}(?!\d)'); yrs=re.compile(r'\b(?:19\d\d|20[012]\d)\b'); proof=re.compile(r'\b(proved|proven|disproved|refuted|false|counterexample)\b',re.I)
for path in glob.iglob(str(root/'seq/A*/*.seq')):
 a=Path(path).stem
 try: lines=Path(path).read_text(encoding='utf-8',errors='replace').splitlines()
 except OSError: continue
 allref=set(); yref=set(); fields=collections.defaultdict(list)
 for l in lines:
  if len(l)<11 or l[0]!='%':continue
  typ=l[1]; content=l[11:]; fields[typ].append(content)
  found=set(ar.findall(content)); allref.update(found)
  if typ=='Y':yref.update(found)
 allref.discard(a);yref.discard(a);refs.update(allref);yrefs.update(yref)
 keys=set(','.join(fields['K']).split(','))
 if 'hard' not in keys:continue
 data=''.join(fields[t] for t in []) if False else ','.join(x for t in 'STU' for x in fields[t]); terms=[x.strip() for x in data.split(',') if x.strip()]
 cl=[s for k in 'CF' for s in fields[k] if re.search('conjecture',s,re.I)]
 texts='\n'.join(lines); lit=fields['D']+fields['H']; recent=[int(y) for l in lit for y in yrs.findall(l) if int(y)<=2026]
 rows[a]={'id':a,'name':fields['N'][0] if fields['N'] else '', 'keywords':','.join(sorted(keys)), 'references_D':len(fields['D']), 'links_H':len(fields['H']), 'arxiv_link_lines':sum(bool(re.search(r'arxiv\.org|arxiv:',l,re.I)) for l in fields['H']), 'doi_link_lines':sum(bool(re.search(r'doi\.org|\bdoi:',l,re.I)) for l in fields['H']), 'latest_literature_year':max(recent,default=''), 'term_count_inline':len(terms),'last_term_digits':len(re.sub(r'\D','',terms[-1])) if terms else '', 'conjecture_lines':len(cl),'conjecture_proof_marked_lines':sum(bool(proof.search(s)) for s in cl), 'conjecture_unmarked_lines':sum(not proof.search(s) for s in cl), 'conjecture_example':next((s for s in cl if not proof.search(s)),''), 'erdosproblems_link':int('erdosproblems.com' in texts.lower())}
print('parsed',len(rows),'corpus',sum(1 for _ in glob.iglob(str(root/'seq/A*/*.seq'))),flush=True)
wiki=collections.defaultdict(set)
for line in (P/'wiki_en.jsonl').open():
 d=json.loads(line)
 for a in ar.findall(d['url']):wiki[a].add(d['pageid'])
open_data=[json.loads(l) for l in (P/'sources/LeanOpenProblems/apn/data/oeis/samples.jsonl').open()]; openids=collections.defaultdict(list)
for d in open_data:openids[d['oeis_id']].append(d['id'])
formal={f'A{int(p.stem):06d}' for p in (P/'sources/formal-conjectures/FormalConjectures/OEIS').glob('*.lean') if p.stem.isdigit()}
resroot=P/'sources/LeanOpenProblems-results'; solved=collections.defaultdict(set); attempted=collections.defaultdict(set); count=0
for p in resroot.glob('runs/oeis*/*/scores.json'):
 try:
  s=json.loads(p.read_text()); name=p.parent.name
  if name in {x['id'] for x in open_data}:
   attempted[name].add(p.parts[-3]);count+=1
   if s.get('proof_scorer',{}).get('value')=='C':solved[name].add(p.parts[-3])
 except (ValueError,AttributeError):pass
print('score files',count,'solved samples',len(solved),'formal',len(formal),flush=True)
history=json.loads((P/'history.json').read_text())
for a,r in rows.items():
 h=history[a];r.update(h);r['incoming_all']=refs[a];r['incoming_Y']=yrefs[a];r['wikipedia_en_pages']=len(wiki[a]);r['oeis_open_samples']=len(openids[a]);r['oeis_open_solved_samples']=sum(x in solved for x in openids[a]);r['oeis_open_attempted_samples']=sum(x in attempted for x in openids[a]);r['oeis_open_sample_ids']=';'.join(openids[a]);r['oeis_open_solved_ids']=';'.join(x for x in openids[a] if x in solved);r['formal_conjectures_oeis']=int(a in formal)
 # A transparent score; bounded log axes, no activity, conjecture or AI term.
 r['watch_score']=round(3*math.log10(1+refs[a])+2*math.log10(1+len(wiki[a]))+math.log10(1+r['references_D']+r['links_H'])+1*('core' in r['keywords'].split(','))+0.5*('nice' in r['keywords'].split(',')),3)

with (P/'hard_metrics.csv').open('w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=list(next(iter(rows.values())).keys()));w.writeheader();w.writerows(sorted(rows.values(),key=lambda r:r['id']))
print('metrics written',len(rows),flush=True)

