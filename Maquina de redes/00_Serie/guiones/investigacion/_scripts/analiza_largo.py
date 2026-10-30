import sys; sys.stdout.reconfigure(encoding="utf-8")
import re, sys, glob, os
def ts(s):
    h,m,r=s.split(':'); return int(h)*3600+int(m)*60+float(r)
def parse(path):
    txt=open(path,encoding='utf-8',errors='replace').read()
    out=[];last=''
    for blk in re.split(r'\n\n+',txt):
        m=re.search(r'(\d+:\d\d:\d\d\.\d+) --> (\d+:\d\d:\d\d\.\d+)',blk)
        if not m: continue
        lines=blk.split('\n')[1:]
        t=' '.join(re.sub(r'<[^>]+>','',l).strip() for l in lines if '-->' not in l).strip()
        if t and t!=last and not last.endswith(t):
            out.append((ts(m.group(1)),t)); last=t
    return out
def words_by_time(segs):
    # dedupe rolling captions: keep text only when new words
    res=[];prev=[]
    for t,s in segs:
        w=s.split()
        k=0
        for n in range(min(len(prev),len(w)),0,-1):
            if prev[-n:]==w[:n]: k=n;break
        new=w[k:]
        if new: res.append((t,new))
        prev=w
    return res
def main(p, dur):
    r=words_by_time(parse(p))
    tot=sum(len(w) for _,w in r)
    first=[ (t,w) for t,w in r if t<60]
    print('FILE',os.path.basename(p))
    print('palabras',tot,'wpm medio',round(tot/(dur/60)))
    # wpm por tramos
    buckets={}
    for t,w in r: buckets[int(t//300)]=buckets.get(int(t//300),0)+len(w)
    print('wpm por 5min',[round(v/5) for k,v in sorted(buckets.items())])
    print('PRIMEROS 60s:',' '.join(' '.join(w) for _,w in first)[:1500])
    txt=' '.join(' '.join(w) for _,w in r).lower()
    for kw in ['didn\'t work','doesn\'t work','error','mistake','let\'s see','let me','so now','i think','why','por qué','no funcion','error','a ver','vamos a','ahora','bueno','entonces','spoiler','subscribe','suscr','next video','siguiente video','en el próximo','al final']:
        print(' ',kw,txt.count(kw))
    print('ÚLTIMOS 40s:',' '.join(' '.join(w) for t,w in r if t>dur-40)[:900])
if __name__=='__main__':
    main(sys.argv[1], float(sys.argv[2]))
