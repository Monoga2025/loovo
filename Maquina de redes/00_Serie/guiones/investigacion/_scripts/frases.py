import sys,os,re,collections,importlib.util
sys.stdout.reconfigure(encoding="utf-8")
spec=importlib.util.spec_from_file_location('a',os.path.join(os.path.dirname(__file__),'analiza_largo.py'))
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
r=a.words_by_time(a.parse(sys.argv[1]))
w=[x.lower().strip('.,¿?¡!') for _,ws in r for x in ws]
c=collections.Counter(' '.join(w[i:i+3]) for i in range(len(w)-2))
print([ (k,v) for k,v in c.most_common(60) if v>=6][:30])
