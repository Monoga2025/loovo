"""motion/index.html desde plan/index.tpl.html + _comun/lib.css + _comun/lib.js + plan/edl.json + plan/words_tl.json + plan/beats.py.
Palabras de whisper alineadas al texto limpio del EDL (difflib); las no emparejadas se interpolan por posición de carácter.
plan/beats.py define B (dict) con at(id, palabra, n), S(id), EN(id); los mismos beats los usa sfx.py. Ejecutar en el proyecto."""
import json, unicodedata, re, difflib, os
C = os.path.dirname(os.path.abspath(__file__))
E = json.load(open("plan/edl.json", encoding="utf-8")); WT = {w["id"]: w for w in json.load(open("plan/words_tl.json", encoding="utf-8"))}
edl = {s["id"]: {"start": s["start"], "end": s["end"], "kind": s["kind"]} for s in E["segs"]}
S = lambda i: edl[i]["start"]; EN = lambda i: edl[i]["end"]
def norm(w):
    s = "".join(c for c in unicodedata.normalize("NFD", w.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", s)
words = {}
for s in E["segs"]:
    if s.get("a") is None: continue
    toks = [t for t in s["texto"].split() if norm(t)]; wh = WT[s["id"]]["words"]
    a = [norm(t) for t in toks]; b = [norm(w["w"]) for w in wh]
    tm = [None] * len(toks)
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size): tm[blk.a + k] = wh[blk.b + k]["on"]
    tm[0] = wh[0]["on"] if wh else s["start"]
    pos = [0]; [pos.append(pos[-1] + len(t) + 1) for t in toks]
    end = s["end"] - 0.15; L = pos[len(toks)]
    anc = [(pos[i], tm[i]) for i in range(len(toks)) if tm[i] is not None] + [(L, end)]
    for i in range(len(toks)):
        if tm[i] is None:
            p0, t0 = max((x for x in anc if x[0] <= pos[i]), key=lambda x: x[0]); p1, t1 = min((x for x in anc if x[0] > pos[i]), key=lambda x: x[0])
            tm[i] = t0 + (t1 - t0) * (pos[i] - p0) / (p1 - p0)
    for i in range(1, len(tm)): tm[i] = max(tm[i], tm[i - 1] + 0.06)
    words[s["id"]] = [[norm(t), round(min(x, s["end"] - 0.05), 3)] for t, x in zip(toks, tm)]
def at(i, w, n=0):
    h = [x[1] for x in words[i] if x[0] == norm(w)]
    if len(h) <= n: raise SystemExit(f"no encuentro '{w}' en {i}: {words[i]}")
    return h[n]
G = dict(at=at, S=S, EN=EN, B={}); exec(open("plan/beats.py", encoding="utf-8").read(), G); B = G["B"]
B = {k: (round(v, 3) if isinstance(v, float) else [round(x, 3) for x in v] if isinstance(v, list) else v) for k, v in B.items()}
json.dump(B, open("plan/beats.json", "w"), indent=0)
json.dump(words, open("plan/words_clean.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
D = dict(edl=edl, words=words, B=B, total=E["total"])
t = open("plan/index.tpl.html", encoding="utf-8").read()
t = t.replace("/*__CSS__*/", open(os.path.join(C, "lib.css"), encoding="utf-8").read()).replace("//__LIB__", open(os.path.join(C, "lib.js"), encoding="utf-8").read())
t = t.replace("__DATA__", json.dumps(D, ensure_ascii=False)).replace("__TOTAL__", str(E["total"]))
open("motion/index.html", "w", encoding="utf-8").write(t)
for k, v in B.items(): print(k, v)
for k, v in words.items(): print(k, " ".join(f"{w}[{x}]" for w, x in v))
