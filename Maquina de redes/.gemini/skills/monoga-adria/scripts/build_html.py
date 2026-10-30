"""Genera motion/index.html desde plan/index.tpl.html con los tiempos de plan/edl.json, plan/words_tl.json y plan/scene25d.json"""
import json
E = json.load(open("plan/edl.json", encoding="utf-8")); W = json.load(open("plan/words_tl.json", encoding="utf-8"))
C = json.load(open("plan/scene25d.json"))
edl = {s["id"]: {"start": s["start"], "end": s["end"]} for s in E["segs"]}
words = {}
for seg in W:
    st = edl[seg["id"]]["start"]
    words[seg["id"]] = [round(max(st, x["on"]), 3) for x in seg["words"]]
lib0 = C["start"]; libA = C["A"]["dur"]; libB = C["B"]["dur"]; libB0 = lib0 + libA - C["xfade"]
D = dict(edl=edl, words=words, total=E["total"], lib0=lib0, libA=libA, libB0=round(libB0, 3), libB=libB)
t = open("plan/index.tpl.html", encoding="utf-8").read()
t = t.replace("__DATA__", json.dumps(D, ensure_ascii=False)).replace("__TOTAL__", str(E["total"]))
t = t.replace("__LIB0__", str(lib0)).replace("__LIBD__", str(round(libA + libB - C["xfade"], 3)))
open("motion/index.html", "w", encoding="utf-8").write(t)
print("ok", E["total"], lib0, libA, libB, libB0)
