import json
W = json.load(open("../plan/words_on.json", encoding="utf-8"))
E = json.load(open("../plan/edl.json", encoding="utf-8"))
ws = [[w["w"].lstrip("-"), w["on"], w["e"]] for w in W]
p = open("../plan/index.tpl.html", encoding="utf-8").read().replace("__WORDS__", json.dumps(ws, ensure_ascii=False)).replace("__DUR__", str(E["total"]))
open("index.html", "w", encoding="utf-8").write(p); print("ok", E["total"])
