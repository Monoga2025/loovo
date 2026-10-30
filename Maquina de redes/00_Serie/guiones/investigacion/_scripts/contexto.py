import sys,re
sys.stdout.reconfigure(encoding="utf-8")
import importlib.util,os
spec=importlib.util.spec_from_file_location('a',os.path.join(os.path.dirname(__file__),'analiza_largo.py'));
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
p,pat=sys.argv[1],sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 6
r=a.words_by_time(a.parse(p))
words=[(t,w) for t,ws in r for w in ws]
txt=' '.join(w for _,w in words)
idx=[];pos=0
cum=[];c=0
for i,(t,w) in enumerate(words): cum.append(c); c+=len(w)+1
import bisect
for m in list(re.finditer(pat,txt,re.I))[:n]:
    i=bisect.bisect_right(cum,m.start())-1
    s=max(0,i-35);e=min(len(words),i+45)
    print(f"[{int(words[i][0]//60)}:{int(words[i][0]%60):02d}]",' '.join(w for _,w in words[s:e]));print()
