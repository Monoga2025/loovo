import json
W = json.load(open("../plan/words_on.json", encoding="utf-8"))
E = json.load(open("../plan/edl.json"))
ws = []
for w in W:
    t = w["w"]
    if t.lower().startswith("code"): t = "Code" + t[4:]
    ws.append([t, w["on"], w["e"]])
p = open("../index.tpl.html", encoding="utf-8").read().replace("__WORDS__", json.dumps(ws, ensure_ascii=False)).replace("__DUR__", str(E["total"]))
open("index.html", "w", encoding="utf-8").write(p); print("ok", E["total"])
