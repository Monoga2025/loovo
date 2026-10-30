"""Genera motion/index.html desde plan/index.tpl.html + plan/beats.json. Fuente de tiempos: plan/edl.json + plan/words_tl.json.
Las palabras de whisper vienen deformadas en algunos tramos: se alinean al texto limpio del EDL (difflib); las no
emparejadas se interpolan por posición de carácter entre anclas. Los beats con sonido los usa también scripts/sfx.py."""
import json, unicodedata, re, difflib
E = json.load(open("plan/edl.json", encoding="utf-8")); WT = {w["id"]: w for w in json.load(open("plan/words_tl.json", encoding="utf-8"))}
edl = {s["id"]: {"start": s["start"], "end": s["end"]} for s in E["segs"]}
S = lambda i: edl[i]["start"]; EN = lambda i: edl[i]["end"]
def norm(w):
    s = "".join(c for c in unicodedata.normalize("NFD", w.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", s)
words = {}
for s in E["segs"]:
    if s["r0"] is None: continue
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
B = {}
# A gancho (bordes medidos en la envolvente: 'pero no vendo nada' = 2,62-3,28)
B["a_yo"] = at("A", "yo"); B["a_mont"] = at("A", "montón"); B["a_pero"] = 2.60; B["a_nada"] = 3.00
B["cut1"] = 3.40
B["mg1"] = 13.50; B["r_dos"] = at("B4", "dos"); B["r_buenos"] = at("B4", "muy")
B["f_in"] = S("C2a") - 0.22
B["f_items"] = [at("C2a", "cliente,"), at("C2a", "información,"), at("C2a", "copy,"), at("C2a", "CRO,"), S("C2c") + 0.03]
B["f_emb"] = at("C2b", "embudo"); B["f_ven"] = at("C2b", "ventas.")
B["v_in"] = S("C3a") - 0.20; B["v_imp"] = at("C3a", "importante"); B["v_ven"] = S("C3b")
B["g_in"] = S("D1") - 0.30; B["g_name"] = at("D1", "Agency"); B["g_tiles"] = at("D2", "agentes"); B["g_cap"] = at("D2", "capacitados")
B["g_vender"] = at("D2", "vender."); B["g_b2b"] = S("D3") + 0.02; B["g_vend"] = at("D3", "vendiendo.")
B["k_in"] = S("D4a") - 0.22; B["k_card"] = S("D4b") - 0.05; B["k_yo"] = EN("D4b") - 0.22
B["o_in"] = S("D5"); B["o_orq"] = at("D5", "orquestador"); B["o_ag"] = at("D5", "agentes.")
B["t_in"] = S("E1") - 0.25; B["t_ent"] = at("E1", "entrenando"); B["t_prompt"] = at("E2", "prompt")
B["t2_in"] = S("E3") - 0.08; B["t_orq"] = at("E3", "orquestador"); B["t_sub"] = at("E3", "subagentes.")
B["pl"] = S("PL")
B = {k: (round(v, 3) if isinstance(v, float) else [round(x, 3) for x in v] if isinstance(v, list) else v) for k, v in B.items()}
json.dump(B, open("plan/beats.json", "w"), indent=0)
json.dump(words, open("plan/words_clean.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
D = dict(edl=edl, words=words, B=B, total=E["total"])
t = open("plan/index.tpl.html", encoding="utf-8").read().replace("__DATA__", json.dumps(D, ensure_ascii=False)).replace("__TOTAL__", str(E["total"]))
open("motion/index.html", "w", encoding="utf-8").write(t)
for k, v in B.items(): print(k, v)
for k, v in words.items(): print(k, " ".join(f"{w}[{x}]" for w, x in v))
