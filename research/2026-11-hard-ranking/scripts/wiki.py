import urllib.request,urllib.parse,json,time,sys
from pathlib import Path
lang=sys.argv[1] if len(sys.argv)>1 else 'en'; out=Path(f'ranking/wiki_{lang}.jsonl'); meta=Path(f'ranking/wiki_{lang}_status.json')
base=f'https://{lang}.wikipedia.org/w/api.php'; params={'action':'query','list':'exturlusage','euquery':'oeis.org/A','eunamespace':'0','eulimit':'max','format':'json'}
n=0; pages=0; start=time.time(); err=None
with out.open('w') as f:
 while True:
  try:
   req=urllib.request.Request(base+'?'+urllib.parse.urlencode(params),headers={'User-Agent':'OEIS-hard-research/1.0 (aggregate link study; local research)'})
   with urllib.request.urlopen(req,timeout=45) as response: d=json.load(response)
   if 'error' in d: raise ValueError(d['error'])
   for row in d['query']['exturlusage']: f.write(json.dumps(row,ensure_ascii=False)+'\n'); n+=1
   f.flush(); pages+=1
   meta.write_text(json.dumps({'requests':pages,'rows':n,'complete':'continue' not in d,'continuation':d.get('continue'),'error':None}))
   if 'continue' not in d: break
   params.update(d['continue']); time.sleep(1.05)
  except Exception as e:
   err=repr(e); break
meta.write_text(json.dumps({'requests':pages,'rows':n,'complete':err is None,'continuation':d.get('continue') if 'd' in locals() else None,'error':err,'seconds':round(time.time()-start)}))
print(meta.read_text())
