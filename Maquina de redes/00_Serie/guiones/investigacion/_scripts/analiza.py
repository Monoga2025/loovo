import re,sys,glob,os
d=sys.argv[1]
def ts(s):
    h,m,x=s.split(':');return int(h)*3600+int(m)*60+float(x)
seen={}
for f in sorted(glob.glob(os.path.join(d,'*-orig.vtt'))+[g for g in glob.glob(os.path.join(d,'*.vtt')) if '-orig' not in g and not os.path.exists(g.replace('.en.vtt','.en-orig.vtt').replace('.es.vtt','.es-orig.vtt'))]):
    t=open(f,encoding='utf8',errors='replace').read().split('\n')
    cues=[];i=0
    while i<len(t):
        m=re.match(r'(\d+:\d+:\d+\.\d+) --> (\d+:\d+:\d+\.\d+)',t[i])
        if m:
            s,e=ts(m[1]),ts(m[2]);i+=1;lines=[]
            while i<len(t) and t[i].strip():
                lines.append(re.sub(r'<[^>]+>','',t[i]).strip());i+=1
            cues.append((s,e,lines))
        i+=1
    words=[];last=''
    out=[]  # (start, text)
    prev=[]
    for s,e,lines in cues:
        for l in lines:
            if l and l not in prev and l!=last:
                out.append((s,l));last=l
        prev=lines
    txt=' '.join(l for _,l in out)
    w=txt.split();n=len(w);dur=max(e for _,e,_ in cues)
    name=os.path.basename(f)
    print('###',name,'| palabras',n,'| fin subt %.1fs'%dur,'| p/s %.2f'%(n/dur if dur else 0))
    # segments each ~8s
    seg={}
    for s,l in out: seg.setdefault(int(s//8)*8,[]).append(l)
    for k in sorted(seg): print('  [%02ds] %s'%(k,' '.join(seg[k])))
