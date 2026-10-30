"""Escribe el _edl.md del entregable: tabla de tramos desde plan/edl.json + plan/notas.md + licencias. Uso: edl_md.py "Título" salida.md"""
import sys, json
E = json.load(open("plan/edl.json", encoding="utf-8")); B = json.load(open("plan/beats.json"))
K = {"mg": "motion", "scr": "pantalla (B-roll 2.5D)", "cam": "persona (mira a cámara)", "pl": "placa"}
o = [f"# {sys.argv[1]} · EDL", "",
     "Crudo (solo lectura, no se movió): C:/Users/you/Desktop/VID_20261013_110529.mp4 (celular, rotación -90 → 1080x1920, 30 fps).",
     f"Línea final {E['total']:.2f} s, 9:16 1080x1920, 30 fps, H.264 CRF 18 + AAC 320k 48 kHz.",
     "Audio: solo el del celular (ese día no hubo mic del PC): HPF 70 Hz + afftdn 6 dB + compresor 2:1, fundidos 12 ms; voz a -17,6 LUFS; música bajo la voz con ducking.",
     "", "| Tramo | Línea final (s) | Crudo (s) | Imagen | Texto |", "|---|---|---|---|---|"]
for s in E["segs"]:
    cr = f"{s['a']:.2f}–{s['b']:.2f}" if s.get("a") is not None else "—"
    img = K[s["kind"]]
    if s["kind"] in ("scr", "cam") and s.get("view"): img += f" · imagen desde {s['view']['src']:.2f}"
    o.append(f"| {s['id']} | {s['start']:.2f}–{s['end']:.2f} | {cr} | {img} | {s['texto']} |")
cuts = [f"{v:.2f} s" for k, v in B.items() if k.startswith("cut")]
o += ["", f"Invert flash + glitch Mixkit 1022 en: {', '.join(cuts)}.", ""]
bl = E.get("blur", [])
o += ["## Desenfoques de privacidad"] + ([f"- Crudo {b['t0']:.1f}–{b['t1']:.1f} s, zona {b['r']} (px del crudo 1080x1920): {b.get('nota', '')}. Pixelado 1/28 + gauss 18 px." for b in bl] or ["- Ninguno necesario en los planos usados (ver notas)."])
o += ["", open("plan/notas.md", encoding="utf-8").read().strip(), "",
      "## Licencias",
      "- Música: \"Sci-Fi Score\" (Mixkit 464, Arulo), Mixkit Stock Music Free License: redes sociales y YouTube, uso comercial, sin atribución; prohíbe TV/radio, CD/DVD, videojuegos, remezclarla o registrarla en Content ID. Texto en LICENCIA_musica.txt.",
      "- Glitch: Mixkit SFX 1022, Mixkit Sound Effects Free License (heredado del Día 4; la página individual no abrió: verificar en el listado antes de publicar).",
      "- Resto de SFX: sintetizados por código. Íconos: Phosphor (MIT). Fuentes: Montserrat y Playfair Display (OFL). Pantallas: grabadas por el usuario en el crudo."]
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(o) + "\n"); print("ok", sys.argv[2])
