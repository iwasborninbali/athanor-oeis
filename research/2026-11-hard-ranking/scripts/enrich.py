import csv,json,re,collections,math
from pathlib import Path
P=Path('ranking'); root=Path.home()/'oeisdata'; a_re=re.compile(r'(?<![A-Za-z0-9])A\d{6}(?!\d)')
wiki={}
for lang in ('ru','de'):
 d=collections.defaultdict(set)
 for line in (P/f'wiki_{lang}.jsonl').open():
  x=json.loads(line)
  for a in a_re.findall(x['url']):d[a].add(x['pageid'])
 wiki[lang]=d
rows=list(csv.DictReader((P/'hard_metrics.csv').open()))
for r in rows:
 a=r['id'];
 for lang in wiki:r[f'wikipedia_{lang}_pages']=len(wiki[lang][a])
 r['wikipedia_all_pages']=int(r['wikipedia_en_pages'])+sum(len(wiki[k][a]) for k in wiki)
 r['watch_score']=round(3*math.log10(1+int(r['incoming_all']))+2*math.log10(1+r['wikipedia_all_pages'])+math.log10(1+int(r['references_D'])+int(r['links_H']))+('core' in r['keywords'].split(','))+.5*('nice' in r['keywords'].split(',')),3)
 path=P/'sources/formal-conjectures/FormalConjectures/OEIS'/f'{int(a[1:])}.lean'
 t=path.read_text() if path.exists() else ''
 for category in ('open','solved','test'):
  r[f'formal_category_{category}']=len(re.findall(r'@\[category\s+(?:research\s+)?'+category+r'\b',t))
 p=root/'seq'/a[:4]/(a+'.seq'); lines=p.read_text(encoding='utf8',errors='replace').splitlines(); patterns=re.compile(r'\b(proved|proven|disproved|refuted|false|counterexample|this is true|solved)\b',re.I)
 marked=[]
 for i,line in enumerate(lines):
  if line.startswith(('%C ','%F ')) and re.search('conjectur',line,re.I):
   near=line+' '+(lines[i+1][11:] if i+1<len(lines) and lines[i+1].startswith(('%C ','%F ')) and re.search(r'\b(above|this|that|the) conjecture\b',lines[i+1],re.I) else '')
   if patterns.search(near):marked.append(near[11:])
 r['conjecture_resolution_contexts']=len(marked)
 r['conjecture_proved_contexts']=sum(bool(re.search(r'\b(proved|proven)\b',m,re.I)) for m in marked)
with (P/'hard_metrics.csv').open('w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print('enriched',len(rows),'wiki',*(sum(int(r[f'wikipedia_{lang}_pages'])>0 for r in rows) for lang in ('en','ru','de')))
