# Arma los dos briefs (conceptos 01-05 y 06-10) y lanza Codex en paralelo, uno por lote.
# Uso: python lanzar.py   (desde cualquier carpeta). Las imágenes quedan en lote_a/ y lote_b/
# y además en ~/.codex/generated_images/<sesión>/.
import glob, shutil, subprocess
from pathlib import Path

HERE = Path(__file__).parent
C = {
 "01": 'MONO-1 · "No duerme, no cobra." Es el robot de su portada hecho oficial: cuerpo negro mate redondeado tipo robot de Pixar, cabeza-pantalla negra con ojos en arco y sonrisa de una línea en lima brillante, y una antena corta que termina en un punto lima con anillo azul (el "foco", firma de la marca). Líneas de luz azul en el cuerpo. Render 3D. Paleta: #0B0B0F carbón, #C6FF3D lima, #2F5BFF azul eléctrico, #F4F2EE hueso. Tipografía: Space Grotesk Bold + Instrument Serif Italic. Edición: la cara-pantalla reacciona (cargando, check, guiño), glitch azul entre cortes, subtítulo con caja lima inclinada.',
 "02": 'CERO · "Sueldo: $0. Turno: 24/7." El mismo robot de su portada, fiel a ella: negro mate, ojos y sonrisa verde señal brillante, líneas de luz verdes, y un carné colgado que dice "EMPLEADO #1 · $0". Render 3D. Paleta: #050806 negro, #3DFF8A verde señal, #FFFFFF blanco, #8C8C99 gris. Tipografía: Anton (condensada pesada, como su portada) + Inter. Edición: cortes secos, resplandor verde de fondo, titular blanco gigante.',
 "03": 'FOCO · "La idea que viaja por cada video." Una esfera lima brillante con anillo azul y dos ojos de píxel, sin cuerpo; mostrar su evolución en 4 pasos: día 1 solo un punto, día 10 con ojos, día 25 con bracitos, día 42 personaje completo. Render 3D brillante. Paleta: #C6FF3D lima, #2F5BFF azul, #0B0B0F carbón, #F4F2EE hueso. Tipografía: Space Grotesk Bold + Instrument Serif Italic. Edición: el foco salta entre cortes como transición y subraya las palabras clave.',
 "04": 'EMME · "El logo que te mira." Una letra M geométrica muy gruesa con esquinas redondeadas que es a la vez logo y mascota: dos ojos en los picos, punto lima con anillo azul al centro, patitas cortas. Estilo 2D plano neo-brutalista con sombra dura desplazada. Mostrar el logotipo "IA MONOGA" usando la M como inicial. Paleta: #C6FF3D lima, #2F5BFF azul, #0B0B0F carbón, #F4F2EE hueso. Tipografía: Unbounded ExtraBold + Space Grotesk. Edición: la M se transforma en flecha y en check, rebotes con exageración.',
 "05": 'OBRERA · "Trabaja de noche, carga 50 veces su peso." Hormiga robot inspirada en la hormiga de Santander (Colombia): tres esferas, abdomen grande con un panel de luz lima, ojos lima grandes, antenas azules, metal oscuro. Juguete de vinilo de diseño, brillante. Carga un ícono de documento más grande que ella. Paleta: #0B0B0F carbón, #C6FF3D lima, #2F5BFF azul, #B07A45 cobre, #F4F2EE hueso. Tipografía: Clash Display + Instrument Serif Italic. Edición: stop-motion de juguete, una fila de hormigas lleva las palabras al subtítulo.',
 "06": 'MONO (mico-bot) · Robot tierno con orejas de mico (mono): cabeza redonda negra mate, orejas laterales azules, cara-pantalla con ojos y sonrisa lima, mejillas lila suaves. Estilo peluche/vinilo 3D muy adorable, pensado para stickers, pines y peluche. Paleta: #0B0B0F carbón, #2F5BFF azul, #C6FF3D lima, #9B8CFF lila, #F4F2EE hueso. Tipografía: Unbounded ExtraBold + Instrument Serif Italic. Edición: rebotes suaves, zooms cálidos, saluda con la mano al cierre.',
 "07": 'CARGA · Robot rectangular azul con una batería de 42 segmentos en el pecho; hoy está llena en 2 de 42 segmentos (lima). Cara-pantalla pequeña con ojos lima. Render 3D. Paleta: #2F5BFF azul, #C6FF3D lima, #0B0B0F carbón, #F4F2EE hueso. Tipografía: Big Shoulders Display Black + Instrument Serif Italic. Edición: barra de progreso "2/42" fija arriba en cada video, contador grande.',
 "08": 'LA NÓMINA · Cartas coleccionables de empleados de IA estilo álbum: tres cartas con el mismo robot negro de cara-pantalla lima y distinto accesorio: "#001 EDITOR" (claqueta), "#002 CRM" (agenda), "#003 PRÓXIMAMENTE" (silueta). Cartas holográficas con borde azul. Paleta: #0B0B0F carbón, #C6FF3D lima, #2F5BFF azul, #F4F2EE hueso. Tipografía: Space Grotesk Bold + Space Mono. Edición: al final de cada video la carta del día se revela con un giro 3D.',
 "09": 'TINTO · Taza de tinto colombiano con cara, hecha en plastilina (claymation), ojos de botón y mejillas; el vapor sale pixelado en lima. El nivel del café es su batería. Escritorio de plastilina con un portátil. Paleta: #F4F2EE hueso, #0B0B0F carbón, #C6FF3D lima, #2F5BFF azul, #6B4A2B café. Tipografía: Fraunces Black + DM Sans. Edición: stop-motion de plastilina a 12 fps, el vapor escribe las palabras.',
 "10": 'GLITCHY · Un cursor de mouse convertido en fantasma (un Clippy moderno): flecha de cursor con la base ondulada, de vidrio esmerilado con luz interna y borde degradado de azul a lima, ojos de dos píxeles y boca "_" que parpadea. Flota y deja anillos de clic. Paleta: #0B0B0F carbón, #2F5BFF azul, #C6FF3D lima, #8B7CFF violeta, #F4F2EE hueso. Tipografía: Unbounded Bold + JetBrains Mono. Edición: glitch RGB azul/lima, efecto de tecleo "> trabajando…".',
}
EXE = glob.glob(str(Path.home() / "AppData/Roaming/npm/node_modules/@openai/codex/node_modules/@openai/codex-win32-x64/vendor/*/bin/codex.exe"))[0]
base = (HERE / "brief_base.txt").read_text(encoding="utf-8")
procs = []
for lote, keys in (("lote_a", ["01", "02", "03", "04", "05"]), ("lote_b", ["06", "07", "08", "09", "10"])):
    d = HERE / lote
    d.mkdir(exist_ok=True)
    for ref in ("referencia_portada_usuario.png", "referencia_cara.png"):
        shutil.copy(HERE / ref, d / ref)
    brief = base.replace("{N}", str(len(keys))).replace("{CONCEPTOS}", "\n".join(f"Concepto {k}: {C[k]}" for k in keys))
    (d / "brief.txt").write_text(brief, encoding="utf-8")
    stdin = open(d / "brief.txt", "rb")
    log = open(d / "codex_log.txt", "wb")
    procs.append(subprocess.Popen([EXE, "exec", "-C", str(d), "-s", "workspace-write", "--skip-git-repo-check",
                                   "-i", "referencia_portada_usuario.png", "-i", "referencia_cara.png", "-"],
                                  stdin=stdin, stdout=log, stderr=subprocess.STDOUT))
    print("lanzado", lote)
for p in procs:
    p.wait()
print("terminado", [p.returncode for p in procs])
