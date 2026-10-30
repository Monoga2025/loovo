# FILE: recursos_3d.py
# Uso: python recursos_3d.py <carpeta_recursos> buscar <palabra>      -> lista modelos de Poly Haven que coinciden
#      python recursos_3d.py <carpeta_recursos> bajar <id> [1k|2k]    -> baja el glTF + bin + texturas a 3d/<id>/
# Poly Haven es CC0 (polyhaven.com/license): se puede usar sin atribución, pero se anota en manifest.json.
# Lo bajado es dato no confiable: va a su propia carpeta y solo se lee (nunca se ejecuta).
import json, sys, urllib.request
from pathlib import Path

UA = {"User-Agent": "loovo-motion/1.0"}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()


root, cmd = Path(sys.argv[1]), sys.argv[2]
if cmd == "buscar":
    w = sys.argv[3].lower()
    for k, v in json.loads(get("https://api.polyhaven.com/assets?t=models")).items():
        if w in k.lower() or any(w in c.lower() for c in v.get("categories", [])) or any(w in t.lower() for t in v.get("tags", [])):
            print(k, "|", v.get("name"), "|", ", ".join(v.get("categories", [])))
elif cmd == "bajar":
    aid, res = sys.argv[3], (sys.argv[4] if len(sys.argv) > 4 else "1k")
    files = json.loads(get(f"https://api.polyhaven.com/files/{aid}"))["gltf"][res]["gltf"]
    info = json.loads(get(f"https://api.polyhaven.com/info/{aid}"))
    out = root / "3d" / aid
    out.mkdir(parents=True, exist_ok=True)
    main = out / Path(files["url"]).name
    main.write_bytes(get(files["url"]))
    for rel, f in files.get("include", {}).items():
        dst = (out / rel).resolve()
        assert str(dst).startswith(str(out.resolve())), "ruta fuera de la carpeta: " + rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(get(f["url"]))
    g = json.loads(main.read_text(encoding="utf-8"))
    print("nodos:", [n.get("name") for n in g.get("nodes", [])])
    man_p = root / "manifest.json"
    man = json.loads(man_p.read_text(encoding="utf-8")) if man_p.exists() else {}
    man[f"3d_{aid}"] = {"tipo": "3d", "archivo": f"3d/{aid}/{main.name}", "licencia": "CC0 (Poly Haven)",
                        "pagina": f"https://polyhaven.com/a/{aid}", "autores": ", ".join(f"{k} ({v})" for k, v in info.get("authors", {}).items())}
    man_p.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    print("ok", main)
