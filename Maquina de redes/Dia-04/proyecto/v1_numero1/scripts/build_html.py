"""Genera motion/index.html desde plan/index.tpl.html + bloque entreno02 (plan/e02.*), y plan/beats.json + plan/sfx_cues.json.
Una sola fuente de tiempos: EDL (plan/edl.json) + palabras (plan/words_tl.json). Los 'beats' que llevan sonido se calculan aquí
y los usa tanto la composición (D.B) como scripts/sfx.py."""
import json, unicodedata, re
E = json.load(open("plan/edl.json", encoding="utf-8")); W = json.load(open("plan/words_tl.json", encoding="utf-8"))
F = 1 / 30
edl = {s["id"]: {"start": s["start"], "end": s["end"]} for s in E["segs"]}
S = lambda i: edl[i]["start"]; EN = lambda i: edl[i]["end"]
def norm(w):
    s = "".join(c for c in unicodedata.normalize("NFD", w.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", s)
words = {seg["id"]: [[norm(x["w"]), round(max(seg["start"], x["on"]), 3), x["w"]] for x in seg["words"]] for seg in W}
# palabras que whisper dejó fuera del tramo (empiezan justo en el borde): se ubican en el primer sonido
words["D3"].insert(0, ["hasta", round(S("D3") + 0.06, 3), "hasta"])
words["F0b"].insert(0, ["en", round(S("F0b") + 0.02, 3), "en"])
words["F1b"].insert(0, ["con", round(S("F1b") + 0.02, 3), "con"])
def at(i, w, n=0):
    hits = [x[1] for x in words[i] if x[0] == norm(w)]
    if len(hits) <= n: raise SystemExit(f"no encuentro '{w}' #{n} en {i}: {[x[0] for x in words[i]]}")
    return hits[n]
B = {}
B["a_no1"] = at("H1", "número"); B["a_w1"] = S("H2") - 0.10; B["a_box"] = at("H2", "mejor"); B["a_w2"] = S("H3") - 0.08
B["a_stamp"] = at("H3", "sido") + 0.08; B["a_push"] = at("H3", "no") - 0.40; B["p_h3"] = at("H3", "no") - 0.12
B["e02"] = S("C1")
B["c_in"] = EN("CP"); B["c_land"] = at("C3b", "mejores") - 0.10; B["c_sw"] = at("C4", "es") - 0.12; B["c_box"] = at("C4", "se")
B["d_in"] = EN("C4"); B["d_grid"] = at("D2", "creerme") - 0.10; B["d_flip0"] = at("D2", "número"); B["d_flip1"] = at("D2", "todo") + 0.30
B["cut1"] = round(S("D3") * 30) / 30
B["f_in"] = EN("D3"); B["f_big"] = at("F0b", "fracasos") - 0.08; B["f_list"] = S("F1a") - 0.06
B["f_cards"] = [at("F1a", "agencia"), at("F1b", "empresa"), at("F1c", "reparación"), at("F1c", "diseño"), at("F1c", "edición"), at("F1d", "las")]
B["f_frac"] = [at("F1a", "fracasé", 0), at("F1a", "fracasé", 1), at("F1c", "fracasé", 0), at("F1c", "fracasé", 1), at("F1c", "fracasé", 2), at("F1d", "fracasé")]
B["f_all"] = EN("F1d") - 0.30
B["p_in"] = S("P1"); B["p_no1"] = at("P1", "número"); B["p_crack"] = EN("P1") + 0.30
B["r1_in"] = EN("P2"); B["r1_org1"] = at("R1", "organizando", 0) - 0.05; B["r1_org2"] = at("R1", "organizando", 1) - 0.05; B["r2_in"] = S("R2")
B["r3_in"] = EN("R2"); B["r3_nodes"] = at("R3", "distintas") - 0.05; B["r3_lines"] = at("R3", "habilidades"); B["r3_chart"] = at("R3", "yo") - 0.05
B["r3_fruto"] = at("R3", "fruto")
B["r4_in"] = at("R4a", "algún") - 0.12; B["r4_tags"] = at("R4a", "todo"); B["r4_big"] = at("R4a", "suerte", 0); B["r4_no"] = at("R4a", "no")
B["r4_drop"] = at("R4a", "suerte", 1) + 0.12
B["r5_in"] = EN("R4a") + 0.06; B["r5_rows"] = [at("R4b", "esfuerzo"), at("R4b", "constancia"), at("R4b", "años", 0)]
B["r5_lay"] = at("R4b", "yo", 0) - 0.10
B["cut2"] = round((S("R4b") + (167.10 - 160.20)) * 30) / 30
B["z_in"] = round((at("R4b", "yo", 2) - 0.45) * 30) / 30; B["z_days"] = at("R4b", "días"); B["z_five"] = at("R4b", "nuevo") - 0.12
B["pl"] = S("PL")
B = {k: (round(v, 3) if isinstance(v, float) else [round(x, 3) for x in v] if isinstance(v, list) else v) for k, v in B.items()}
json.dump(B, open("plan/beats.json", "w"), indent=0)
D = dict(edl=edl, words={k: [[a, b] for a, b, _ in v] for k, v in words.items()}, B=B, total=E["total"])
t = open("plan/index.tpl.html", encoding="utf-8").read()
t = t.replace("/*E02CSS*/", open("plan/e02.css", encoding="utf-8").read())
t = t.replace("<!--E02HTML-->", open("plan/e02.html", encoding="utf-8").read())
t = t.replace("//E02JS", open("plan/e02.js", encoding="utf-8").read())
t = t.replace("__DATA__", json.dumps(D, ensure_ascii=False)).replace("__TOTAL__", str(E["total"]))
open("motion/index.html", "w", encoding="utf-8").write(t)
for k, v in B.items(): print(k, v)
