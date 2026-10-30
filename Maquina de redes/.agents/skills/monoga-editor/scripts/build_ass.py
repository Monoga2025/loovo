# FILE: build_ass.py
# Uso: python3 build_ass.py words_out.json captions.ass [fuente]
# Subtítulos de 1-3 palabras con palabra activa resaltada (amarillo) en 1080x1920.
import json, sys

words = json.load(open(sys.argv[1], encoding="utf-8"))
out = sys.argv[2]
font = sys.argv[3] if len(sys.argv) > 3 else "Montserrat"
W, H, SIZE, CAPTION_BOTTOM = 1080, 1920, 84, 1380
margin_v = H - CAPTION_BOTTOM
HEADER = (
    "[Script Info]\nScriptType: v4.00+\n"
    f"PlayResX: {W}\nPlayResY: {H}\nWrapStyle: 2\n\n"
    "[V4+ Styles]\n"
    "Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,"
    "BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,"
    "BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n"
    f"Style: Cap,{font},{SIZE},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,"
    f"-1,0,0,0,100,100,0,0,1,6,2,2,120,140,{margin_v},1\n\n"
    "[Events]\n"
    "Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n"
)
YELLOW, WHITE = "&H00E5FF&", "&HFFFFFF&"


def ts(x):
    h, m, s = int(x // 3600), int(x % 3600 // 60), x % 60
    return f"{h}:{m:02d}:{s:05.2f}"


groups, cur = [], []
for w in words:
    cur.append(w)
    if len(cur) == 3 or w["w"].endswith((".", ",", "?", "!", "…")):
        groups.append(cur)
        cur = []
if cur:
    groups.append(cur)

lines = []
for g in groups:
    for i, w in enumerate(g):
        end = g[i + 1]["s"] if i + 1 < len(g) else w["e"]
        parts = []
        for j, x in enumerate(g):
            t = x["w"].upper()
            parts.append("{\\c" + YELLOW + "}" + t + "{\\c" + WHITE + "}" if j == i else t)
        lines.append(f"Dialogue: 0,{ts(w['s'])},{ts(end)},Cap,,0,0,0,,{' '.join(parts)}")
open(out, "w", encoding="utf-8").write(HEADER + "\n".join(lines) + "\n")
print(f"{len(lines)} eventos -> {out}")
