import subprocess,re,json,collections,glob,os,time
root=os.path.expanduser('~/oeisdata'); hard=set()
for path in glob.iglob(root+'/seq/A*/*.seq'):
 with open(path,encoding='utf8',errors='replace') as f:
  for line in f:
   if line.startswith('%K ') and 'hard' in line[11:].strip().split(','):
    hard.add(os.path.basename(path)[:7]);break
print('hard',len(hard),flush=True)
res={a:{'commits':0,'commits_since_2024':0,'commits_2026':0,'last_stu_change':'','last_growth':''} for a in hard}
p=subprocess.Popen(['git','-C',root,'log','--no-renames','--format=COMMIT %H %cs','-p','--','seq/'],stdout=subprocess.PIPE,encoding='utf8',errors='replace',bufsize=1024*1024)
a=None; date=''; added=removed=0; changed=False; new=False; commits=0

def flush():
 global a,added,removed,changed,new
 if a:
  r=res[a];r['commits']+=1;r['commits_since_2024']+=date>='2024-01-01';r['commits_2026']+=date>='2026-01-01'
  if changed and not new and not r['last_stu_change']:r['last_stu_change']=date
  if changed and not new and added>removed and not r['last_growth']:r['last_growth']=date
 a=None;added=removed=0;changed=new=False
for line in p.stdout:
 if line.startswith('COMMIT '):
  flush(); date=line.rstrip().split()[-1];commits+=1
 elif line.startswith('diff --git '):
  flush();m=re.match(r'diff --git a/seq/A\d+/(A\d{6})\.seq ',line)
  if m and m[1] in hard:a=m[1]
 elif a and line.startswith('new file mode '):new=True
 elif a and re.match(r'^[+-]%[STU] ',line):
  vals=line[11:].strip().strip(',').split(',');n=sum(bool(x.strip()) for x in vals)
  if line[0]=='+':added+=n
  else:removed+=n
  changed=True
flush(); rc=p.wait();print('commits',commits,'rc',rc,flush=True)
if rc:raise SystemExit(rc)
open('ranking/history.json','w').write(json.dumps(res))
