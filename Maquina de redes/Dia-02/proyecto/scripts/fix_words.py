# Palabras del corte (faster-whisper sobre cut.wav) con correcciones de vocabulario -> build/words_out.json
import json, re
w = json.load(open("transcript/cut_words.json", encoding="utf-8"))
fix = {"CDRM": "CRM", "CDRMs": "CRMs", "Dian": "DIAN", "trabajo": "trabaja", "paso": "pasó", "etapa": "etapas", "sobre": "sobreexplotó"}
out = []
for x in w:
    t = x["w"]; core = re.sub(r"[.,;:!?]+$", "", t); p = t[len(core):]
    out.append({"w": fix.get(core, core) + p, "s": x["s"], "e": x["e"]})
r = []
for k, x in enumerate(out):
    if x["w"] == "sobreexplotó" and k + 1 < len(out) and out[k + 1]["w"].startswith("exploto"):
        r.append({"w": "sobreexplotó,", "s": x["s"], "e": out[k + 1]["e"]}); out[k + 1]["w"] = None
    elif x["w"] is not None:
        r.append(x)
out = [x for x in r if x["w"]]
a = [k for k, x in enumerate(out) if x["w"] == "es" and out[k + 1]["w"] == "que" and out[k + 2]["w"] == "este"][0]
for i, t in enumerate(["a", "este", "sí", "lo", "exploto"]): out[a + i]["w"] = t
json.dump(out, open("build/words_out.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "palabras")
