import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SCRIPTS = Path(__file__).resolve().parent
EDITOR = ROOT / ".claude" / "skills" / "monoga-editor" / "scripts"
PENDING = "Pendiente"


def field(text, name):
    m = re.search(rf"\*\*{re.escape(name)}:\*\*[ \t]*(.*)", text)
    return m.group(1).strip() if m else ""


def read(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


def checks(day):
    brief = read(day / "brief.md")
    guion = read(day / "guion.md")
    caption = read(day / "caption.md")
    resultados = read(day / "resultados.md")
    entregables = day / "entregables"
    videos = sorted(entregables.glob("*.mp4")) if entregables.exists() else []
    portadas = sorted(p for p in entregables.glob("*.png") if "portada" in p.name.lower()) if entregables.exists() else []
    views = re.search(r"\|\s*Vistas\s*\|([^\n]*)", resultados)
    return [
        ("brief", bool(field(brief, "Gancho (primeras palabras)")) or bool(field(brief, "Tema")), "Completa brief.md (tema, gancho, dato real, portada)."),
        ("crudo", any((day / "crudo").glob("*.mp4")), f"Deja tu video grabado en {day.name}/crudo/."),
        ("transcripcion", (day / "proyecto" / "transcript" / "words.json").exists(), "Pide la transcripción (monoga-editor, transcribe.py)."),
        ("guion", PENDING not in guion[:300] and len(guion) > 120, "Pide 'guion': revisión contra hechos.md y tu voz."),
        ("video", bool(videos), "Pide 'editar': monoga-editor, con las reglas de audio del Día 1."),
        ("portada", bool(portadas), f"Corre: python {SCRIPTS.name}/dia.py portada {day.name[-2:].lstrip('0') or '0'}"),
        ("caption", PENDING not in caption[:300] and len(caption) > 200, "Pide 'caption'."),
        ("publicado", bool(re.search(r"\*\*Publicado:\*\*\s*s[ií]", resultados, re.I)), "Publica y marca 'Publicado: sí' en resultados.md."),
        ("resultados", bool(views and re.search(r"\d", views.group(1))), "A las 24 h, pega las cifras y pide 'resultados'."),
    ]


def update_marcador(n, last):
    marcador = ROOT / "00_Serie" / "marcador.md"
    lines = marcador.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"| {n} |"):
            cells = line.split("|")
            cells[4] = f" {last} "
            lines[i] = "|".join(cells)
            break
    marcador.write_text("\n".join(lines) + "\n", encoding="utf-8")


def estado(n):
    day = ROOT / f"Dia-{n:02d}"
    if not day.exists():
        print(f"{day.name} no existe. Corre: python {SCRIPTS.name}/new_day.py {n}")
        return None
    rows = checks(day)
    print(f"== {day.name} ==")
    nxt = None
    last = "creado"
    for name, ok, hint in rows:
        print(f"{'[x]' if ok else '[ ]'} {name}")
        if ok:
            last = name
        elif nxt is None:
            nxt = (name, hint)
    update_marcador(n, last)
    print(f"Siguiente: {nxt[0]} -> {nxt[1]}" if nxt else "Todo completo.")
    return day, rows, nxt


def portada(n, force=False):
    day = ROOT / f"Dia-{n:02d}"
    brief = read(day / "brief.md")
    titular = field(brief, "Portada titular")
    if not titular:
        print("brief.md no tiene 'Portada titular'. Complétalo (ej. 42 DÍAS) y repite.")
        return 1
    existing = [p for p in (day / "entregables").glob("*.png") if "portada" in p.name.lower()]
    if existing and not force:
        print(f"Ya hay portada: {existing[0].name}. Usa --force para generar otra.")
        return 0
    args = [sys.executable, "-X", "utf8", str(SCRIPTS / "portada.py"), str(n), "--titular", titular]
    for flag, key in (("--secundario", "Portada secundario"), ("--etiqueta", "Portada etiqueta")):
        value = field(brief, key)
        if value:
            args += [flag, value]
    frame = field(brief, "Portada fotograma")
    if frame:
        args += ["--frame", frame]
    return subprocess.run(args).returncode


def main():
    if len(sys.argv) < 3 or not sys.argv[2].isdigit():
        print("Uso: dia.py estado|portada|todo <N> [--force]")
        return 2
    command, n = sys.argv[1], int(sys.argv[2])
    force = "--force" in sys.argv
    if command == "estado":
        return 0 if estado(n) else 1
    if command == "portada":
        code = portada(n, force)
        estado(n)
        return code
    if command == "todo":
        result = estado(n)
        if not result:
            return 1
        day, rows, nxt = result
        done = {name for name, ok, _ in rows if ok}
        if "crudo" in done and "portada" not in done:
            portada(n, force)
            estado(n)
        return 0
    print("Comando desconocido.")
    return 2


sys.exit(main())
