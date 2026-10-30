import json
W = json.load(open("../plan/words_on.json", encoding="utf-8")); E = json.load(open("../plan/edl.json"))
D = dict(words=[[w["w"], w["on"], w["e"]] for w in W], total=E["total"])
p = open("../index.tpl.html", encoding="utf-8").read().replace("__DATA__", json.dumps(D, ensure_ascii=False)).replace("__TOTAL__", str(E["total"]))
open("index.html", "w", encoding="utf-8").write(p); print("ok", E["total"])
