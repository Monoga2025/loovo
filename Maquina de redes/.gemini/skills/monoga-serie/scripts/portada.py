import argparse
import glob
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILL = ROOT / ".claude" / "skills" / "monoga-serie"
GENERATED = Path.home() / ".codex" / "generated_images"
LETTERS = "ABCDEF"
WAIT_SECONDS = 25 * 60


def codex_exe():
    pattern = str(Path.home() / "AppData" / "Roaming" / "npm" / "node_modules" / "@openai" / "codex" / "node_modules" / "@openai" / "codex-win32-x64" / "vendor" / "*" / "bin" / "codex.exe")
    found = glob.glob(pattern)
    if found:
        return found[0]
    return shutil.which("codex")


def reference(day, frame, dest):
    if frame and Path(frame).exists():
        shutil.copy(frame, dest)
        return
    sources = [day / "proyecto" / "build" / "cut.mp4"] + sorted((day / "crudo").glob("*.mp4"))
    source = next((s for s in sources if s.exists()), None)
    if source is None:
        sys.exit("No hay video en proyecto/build/cut.mp4 ni en crudo/. Pasa --frame con una imagen.")
    second = frame or "2.2"
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", str(second), "-i", str(source), "-frames:v", "1", str(dest)], check=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("dia", type=int)
    p.add_argument("--titular", required=True)
    p.add_argument("--secundario", default="")
    p.add_argument("--etiqueta", default="")
    p.add_argument("--contexto", default="El creador tiene 42 dias para transformar su empresa antes de un evento con mas de 2.000 empresarios.")
    p.add_argument("--frame", default="")
    p.add_argument("--variantes", type=int, default=2)
    p.add_argument("--ancho", type=int, default=1080)
    p.add_argument("--alto", type=int, default=1440)
    a = p.parse_args()

    day = ROOT / f"Dia-{a.dia:02d}"
    if not day.exists():
        sys.exit(f"{day.name} no existe. Corre new_day.py primero.")
    out = day / "portada"
    out.mkdir(exist_ok=True)
    reference(day, a.frame, out / "referencia.png")

    lines = [f'- Titular principal: "{a.titular}"']
    if a.secundario:
        lines.append(f'- Linea secundaria: "{a.secundario}"')
    if a.etiqueta:
        lines.append(f'- Etiqueta pequena: "{a.etiqueta}"')
    names = ", ".join(f"portada_final_{LETTERS[i]}.png" for i in range(a.variantes))
    brief = (SKILL / "templates" / "portada_brief.md").read_text(encoding="utf-8")
    for key, value in {
        "{{DIA}}": str(a.dia),
        "{{CONTEXTO}}": a.contexto,
        "{{TEXTOS}}": "\n".join(lines),
        "{{ANCHO}}": str(a.ancho),
        "{{ALTO}}": str(a.alto),
        "{{VARIANTES}}": str(a.variantes),
        "{{NOMBRES}}": names,
    }.items():
        brief = brief.replace(key, value)
    (out / "brief_codex.txt").write_text(brief, encoding="utf-8")

    exe = codex_exe()
    if not exe:
        sys.exit("No encuentro codex.exe. Instala la CLI de Codex e inicia sesion con codex login.")
    log = out / "codex_log.txt"
    with open(out / "brief_codex.txt", "rb") as stdin, open(log, "wb") as stdout:
        try:
            subprocess.run([exe, "exec", "-C", str(out), "-s", "workspace-write", "--skip-git-repo-check", "-i", "referencia.png", "-"], stdin=stdin, stdout=stdout, stderr=subprocess.STDOUT, timeout=WAIT_SECONDS)
        except subprocess.TimeoutExpired:
            print("Codex tardo mas de 25 minutos. Revisa codex_log.txt.")

    text = log.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"session id:\s*(\S+)", text)
    saved = sorted(out.glob("portada_final_*.png"))
    if match and GENERATED.joinpath(match.group(1)).exists():
        originals = sorted(GENERATED.joinpath(match.group(1)).glob("*.png"), key=lambda f: f.stat().st_mtime)
        for i, f in enumerate(originals, 1):
            shutil.copy(f, out / f"intento_{i:02d}.png")
        print(f"Codex genero {len(originals)} imagenes (sesion {match.group(1)}). Copias en portada/intento_NN.png")
    if saved:
        print("Finales guardadas por Codex:", ", ".join(s.name for s in saved))
    else:
        print("Codex no guardo los finales. Usa la ultima de cada variante en portada/intento_NN.png.")
    final = text.split("\ncodex\n")[-1].strip()
    print("--- Reporte de Codex ---")
    print(final[-900:])
    pick = re.search(r"[Rr]ecomiendo\s+(?:la\s+)?(?:variante\s+)?\**\s*([A-F])\b", final)
    letter = pick.group(1) if pick else "A"
    chosen = out / f"portada_final_{letter}.png"
    if chosen.exists():
        target = day / "entregables" / f"Dia{a.dia}_portada_TikTok_3x4.png"
        target.parent.mkdir(exist_ok=True)
        shutil.copy(chosen, target)
        print(f"Propuesta copiada a {target.relative_to(ROOT)} (variante {letter}). El usuario decide cuál queda.")


main()
