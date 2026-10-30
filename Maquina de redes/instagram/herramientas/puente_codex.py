"""Reutiliza la invocación y descubrimiento de portada.py, sin ejecutarlo ni tocar días."""
from pathlib import Path
import subprocess,glob,shutil,re,json,sys
OUT=Path(__file__).resolve().parents[1]
GENERATED=Path.home()/'.codex/generated_images'

def progress(s):
 with (OUT/'PROGRESS.md').open('a',encoding='utf-8') as f:f.write('\n- '+s+'\n')
def run(name,subject,size):
 dest=OUT/'borradores'/name;dest.mkdir(parents=True,exist_ok=True)
 brief=f'''Genera UNA imagen real con la herramienta integrada image_generation de Codex (no código, no SVG, no base64 manual, no otro proveedor). No delegues, no publiques, no inicies sesión ni navegues cuentas. Es una ilustración abstracta para Monoga/Loovo, no evidencia de productos ni resultados.\nMarca Eléctrico: carbón #0B0B0F, azul #2F5BFF, un único foco lima #C6FF3D y hueso #F4F2EE. NADA rojo. Sin personas, rostros, manos, logos, pantallas, facturas, números, letras, texto, marcas de agua ni tipografía.\nTema: {subject}.\nFormato final solicitado {size[0]}x{size[1]}. Si el generador entrega otro tamaño, conserva original; el padre lo ajusta después con Pillow. Composición limpia, editorial, mucho vacío. Si es destacada, icono/objeto abstracto enteramente dentro del círculo centrado en el lienzo (50%,50%), diámetro 60% del ancho.\nUsa exclusivamente image_generation. Si no está disponible o falla, informa el error exacto y detente; no simules imágenes con código ni uses servicios alternativos. Los archivos generados quedan en ~/.codex/generated_images/<session-id>/. Puedes copiar la imagen final a fondo.png dentro de esta carpeta de trabajo. No escribas fuera de esta carpeta salvo el almacenamiento automático de generated_images. No instales nada, no leas datos del usuario ni credenciales.\n'''
 (dest/'prompt.txt').write_text(brief,encoding='utf-8')
 pattern=str(Path.home()/'AppData/Roaming/npm/node_modules/@openai/codex/node_modules/@openai/codex-win32-x64/vendor/*/bin/codex.exe')
 found=glob.glob(pattern);exe=found[0] if found else shutil.which('codex')
 if not exe:raise RuntimeError('No encuentro codex.exe. No se inició sesión ni se instaló nada.')
 cmd=[exe,'exec','-C',str(dest),'-s','workspace-write','--skip-git-repo-check','-']
 (dest/'invocacion.json').write_text(json.dumps(cmd,ensure_ascii=False),encoding='utf-8')
 progress('Paso 5: invocando '+name+' mediante codex exec; prompt y log en borradores/'+name+'. No hay tarea en segundo plano.')
 with (dest/'prompt.txt').open('rb') as stdin,(dest/'codex_log.txt').open('wb') as stdout:
  try:r=subprocess.run(cmd,stdin=stdin,stdout=stdout,stderr=subprocess.STDOUT,timeout=25*60)
  except subprocess.TimeoutExpired:raise RuntimeError('Codex tardo mas de 25 minutos. Revisa codex_log.txt.')
 text=(dest/'codex_log.txt').read_text(encoding='utf-8',errors='replace')
 match=re.search(r'session id:\s*(\S+)',text)
 originals=[]
 if match and (GENERATED/match.group(1)).exists():
  originals=sorted((GENERATED/match.group(1)).glob('*.png'),key=lambda f:f.stat().st_mtime)
  for i,p in enumerate(originals,1):shutil.copy(p,dest/f'original_{i:02d}.png')
 # A generated image is mandatory; a caller-created placeholder is never success.
 if not originals:
  error=f'Codex exit code {r.returncode}; sin PNG generado en generated_images para la sesión '+(match.group(1) if match else 'no identificada')+'\n'+text[-7000:]
  (dest/'ERROR.txt').write_text(error,encoding='utf-8')
  (OUT/'borradores/REGISTRO.md').write_text('# Registro de imágenes\n\n## '+name+' · FALLÓ\n- Prompt completo: `'+name+'/prompt.txt`.\n- Formato previsto: '+str(size[0])+'×'+str(size[1])+'. Sin texto IA.\n- Invocación idéntica al método de portada.py, sin referencia porque no hay personas.\n- Imágenes generadas: 0. Sin composición, sin hoja de contactos y sin lote.\n- Error exacto y salida: `'+name+'/ERROR.txt` y `'+name+'/codex_log.txt`.\n- Revisión visual y de dimensiones: no aplicable (no se generó imagen).\n\n```text\n'+error+'\n```\n',encoding='utf-8')
  progress('DETENIDO en paso 5(a): falló '+name+'. Error exacto en borradores/'+name+'/ERROR.txt. No ejecutar lote, composición ni hoja. Pasos 5(b–d) pendientes; no usar otro método.')
  print(error);return False
 shutil.copy(originals[-1],dest/'seleccion.png')
 progress('Puente '+name+' generó '+str(len(originals))+' PNG; selección copiada. Pendiente revisar imagen antes del lote.')
 print(str(dest/'seleccion.png'));return True
if __name__=='__main__':
 ok=run('prueba','anillo azul con una pequeña chispa lima como icono central; fondo carbón, sin ningún texto',(1080,1920))
 sys.exit(0 if ok else 2)
