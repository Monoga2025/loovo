from pathlib import Path
import sys, subprocess, os
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'herramientas'))
import puente_codex as bridge
DEST=Path(__file__).resolve().parent
if '--worker' in sys.argv:
    subject="destacada Sin humo: reglas, no IA. Un emblema abstracto de tres bloques sólidos encajados como un mecanismo de reglas con un único punto lima. Formas SÓLIDAS y GRUESAS de azul eléctrico #2F5BFF con volumen 3D y bordes redondeados, como objetos escultóricos, NO filigrana ni alambre ni contornos. Grosor mínimo de cualquier parte estructural: 6% del diámetro total de la figura, preferible 12%. UN solo punto lima #C6FF3D. Fondo carbón #0B0B0F completamente liso. Sin texto, números, personas, líneas finas, retículas ni filigrana. Figura centrada ocupando cerca del 60% del ALTO del lienzo; esta instrucción de alto prevalece sobre la frase genérica posterior de diámetro del ancho. Silueta compacta reconocible a 64 px, materiales 3D como las otras portadas. Genera exactamente UNA imagen, sin variantes ni regeneraciones"
    # Keep bridge method; preserve historical register even on its failure branch.
    register=ROOT/'borradores/REGISTRO.md'
    previous=register.read_bytes()
    try:
        ok=bridge.run('destacada_05b',subject,(1080,1920))
    finally:
        if register.read_bytes()!=previous: register.write_bytes(previous)
    sys.exit(0 if ok else 2)
p=subprocess.Popen([sys.executable,str(Path(__file__).resolve()),'--worker'])
try: code=p.wait(timeout=540)
except subprocess.TimeoutExpired:
    subprocess.run(['taskkill','/PID',str(p.pid),'/T','/F'],capture_output=True)
    (DEST/'ERROR.txt').write_text('Límite local de 540 segundos excedido; puente detenido sin alternativa.',encoding='utf-8')
    code=124
(DEST/'estado.txt').write_text(str(code),encoding='utf-8')
bridge.progress('Sin humo 05b: generación en segundo plano finalizada; código '+str(code)+'. Ver borradores/destacada_05b/.')
