"""Reubica las palabras (tiempo de crudo) en la línea final según plan/edl.json -> plan/words_tl.json"""
import json
E=json.load(open("plan/edl.json",encoding="utf-8"))["segs"]
W=json.load(open("plan/words_src.json",encoding="utf-8"))
allw=[w for seg in W for w in seg["words"]]
out=[]
for s in E:
    if not s["cam"]: continue
    ws=[dict(w=w["w"],src=w["src"],on=round(s["start"]+w["src"]-s["t0"],3)) for w in allw if w["cam"]==s["cam"] and s["t0"]-0.02<=w["src"]<s["t1"]]
    out.append(dict(id=s["id"],start=s["start"],end=s["end"],words=ws))
json.dump(out,open("plan/words_tl.json","w",encoding="utf-8"),ensure_ascii=False,indent=0)
for o in out: print(o["id"],o["start"],o["end"]," ".join(f"{i}:{w['w']}[{w['on']:.2f}]" for i,w in enumerate(o["words"])))
