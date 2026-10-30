# FILE: add_hook.py
# Uso: python3 add_hook.py captions.ass salida.ass "LÍNEA 1|LÍNEA 2|..." [segundos] [fuente]
# Añade el gancho en texto (arriba, dentro de la zona segura) con un pop de
# entrada y fade de salida. Palabras entre *asteriscos* van en amarillo.
import re, sys

src, out, text = sys.argv[1], sys.argv[2], sys.argv[3]
dur = float(sys.argv[4]) if len(sys.argv) > 4 else 3.3
font = sys.argv[5] if len(sys.argv) > 5 else "Impact"
SIZE, TOP = 116, 300  # zona segura superior: 270 px
YELLOW, WHITE = "&H00E5FF&", "&HFFFFFF&"

ass = open(src, encoding="utf-8").read()
style = (f"Style: Hook,{font},{SIZE},&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,"
         f"0,0,0,0,100,100,1,0,1,8,4,8,65,120,{TOP},1\n")
ass = ass.replace("\n\n[Events]", "\n" + style + "\n[Events]", 1)

body = "\\N".join(text.split("|"))
body = re.sub(r"\*(.+?)\*", lambda m: "{\\c" + YELLOW + "}" + m.group(1) + "{\\c" + WHITE + "}", body)
anim = "{\\fscx70\\fscy70\\t(0,170,\\fscx106\\fscy106)\\t(170,260,\\fscx100\\fscy100)\\fad(0,250)}"
h, m, s = 0, int(dur // 60), dur % 60
event = f"Dialogue: 1,0:00:00.00,{h}:{m:02d}:{s:05.2f},Hook,,0,0,0,,{anim}{body}\n"
open(out, "w", encoding="utf-8").write(ass.rstrip("\n") + "\n" + event)
print(f"gancho 0-{dur}s -> {out}")
