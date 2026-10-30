# Genera subtítulos del Día 2: make_caps + minúsculas (salvo siglas) + recorte a la duración
import json, re, subprocess, sys
KEYS = "pago,mañana,evento,agencia,inteligencia,artificial,exploto,durmiendo,sobreexplotó,trabaja,crm,real,integrada,nacido,esclavizar,empleado"
SKIP = "3.10-5.05,10.55-13.45,14.45-16.8,34.1-37.1,38.65-41.45,41.5-46.25,53.55-55.75,55.9-57.4"
p = sys.argv[1] if len(sys.argv) > 1 else "motion/compositions/graphics.html"
KEYS = sys.argv[2] if len(sys.argv) > 2 else KEYS
subprocess.run([sys.executable, "scripts/make_caps.py", "build/words_out.json", p, "--keys", KEYS, "--skip", SKIP, "--max", "3"], check=True)
t = open(p, encoding="utf-8").read()
m = re.search(r"const CAPS = \[(.*?)\];", t, re.S)
caps = json.loads("[" + m.group(1).strip().rstrip(",") + "]")
KEEP = {"CRM", "CRMs", "DIAN", "Loovo"}
for c in caps:
    c["b"] = round(min(c["b"], 63.100000), 2)
    for w in c["w"]:
        if w[0] not in KEEP:
            w[0] = w[0][0].lower() + w[0][1:]
js = "const CAPS = [\n" + ",\n".join("        " + json.dumps(c, ensure_ascii=False) for c in caps) + ",\n      ];"
open(p, "w", encoding="utf-8").write(t[:m.start()] + js + t[m.end():])
