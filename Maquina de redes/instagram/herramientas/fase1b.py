from pathlib import Path
import re, json
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
SERIE=ROOT.parent/'00_Serie'
def progress(s):
    with (ROOT/'PROGRESS.md').open('a',encoding='utf-8') as f: f.write('\n- Fase 1b: '+s+'\n')

def captions():
    p=ROOT/'cola.md'; text=p.read_text(encoding='utf-8')
    notes=[
        'Base: `../Dia-01/caption.md`, copiada casi literal. «hoy está» → «estaba» y «Faltan 42 días» → «El reto empezó el 7 de octubre»: contexto histórico, no cuenta regresiva vigente. Se retiró el MARCADOR completo: «Servicios lanzados: 0» no está confirmado en hechos.md y no se conservaron cifras sin respaldo. «Mañana, día 2: [te presento a mi primer empleado]» → «Día 2: te presento a mi primer empleado», respaldado por el editor ✅. Nombre del evento, rol de Monoga y aprobación de esa línea: **pendiente de Monoga**, como pide el original; no se da por resuelto su pendiente editorial.',
        'Base: `../Dia-02/caption.md`, copiada casi literal. Se eliminó la primera línea (contratación, pago y trabajo hasta las 3 a. m. no están confirmados ✅). «Hoy es el día» → «Día»; «Faltan 40 días» → «El reto empezó el 7 de octubre», por republicación histórica. Se retiró el MARCADOR completo: «Empleados con IA: 2» sigue sin confirmación y no se da por operativo al agente del CRM. Se eliminó la promesa «Mañana… conectamos el CRM a la DIAN»: integración no existente ⏳ y fecha vencida. Se conserva el aviso original de que el CRM está en pruebas, no como resultado confirmado. Número de empleados, nombre del evento y rol de Monoga: **pendiente de Monoga**.',
        'Base: `../Dia-03/caption.md`, leído completo: solo dice «Pendiente.». Se retiró el caption inventado por el agente anterior. No hay caption publicable ni hashtags que validar: **pendiente de Monoga**. No se inventó texto para completar la cola.'
    ]
    sources=[]
    for n in range(1,4):
        original=(ROOT.parent/f'Dia-{n:02d}'/'caption.md').read_text(encoding='utf-8')
        if n==3: cap=None
        else:
            cap=re.search(r'```\s*\n(.*?)\n```',original,re.S).group(1)
            if n==1:
                cap=cap.replace('Loovo hoy está','Loovo estaba').replace('Faltan 42 días.','El reto empezó el 7 de octubre.')
                cap=re.sub(r'MARCADOR DEL DÍA 1\n.*?\n\n','',cap,flags=re.S)
                cap=cap.replace('Mañana, día 2: [te presento a mi primer empleado].','Día 2: te presento a mi primer empleado.')
            else:
                cap=cap.split('\n',1)[1].replace('Hoy es el día 2','Día 2').replace('Faltan 40 días.','El reto empezó el 7 de octubre.')
                cap=re.sub(r'MARCADOR DEL DÍA 2\n.*?\n\n','',cap,flags=re.S)
                cap=cap.replace('Mañana, día 3: conectamos el CRM a la DIAN para hacer facturas electrónicas.\n\n','')
            assert len(cap)<900 and len(re.findall(r'#\w+',cap))<=5 and '#42DiasLoovo' in cap
            assert '[' not in cap and 'sin métricas' not in cap
        start=text.index(f'## Día {n}\n'); end=text.find('\n## ',start+1)
        if end<0: end=len(text)
        section=text[start:end]; section=section[:section.index('- Caption propuesto')]
        section+=(f'- Caption basado en el original ({len(cap)} caracteres):\n\n```text\n{cap}\n```\n' if cap else '- Caption: **pendiente de Monoga** (el original solo dice «Pendiente.»).\n')
        section+='\n- Cambios respecto del original y motivo: '+notes[n-1]+'\n'
        text=text[:start]+section+text[end:]
        sources.append({'dia':n,'caption':cap,'caracteres':len(cap) if cap else None,'cambios':notes[n-1]})
    text+='\n### Publicación por API · fuente oficial aportada por el padre\n- Solo imágenes **JPEG** por API.\n- Carruseles: hasta **20 elementos**.\n- Límite: **100 publicaciones por 24 h**.\nFuente: Meta, consulta del **2026-10-23**, https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/content-publishing/ . Verificación aportada por el padre; no se volvió a consultar desde esta sesión. Son condiciones de la API, no límites equivalentes de la app. Los PNG finales son archivos de composición, no archivos listos para enviar a la API. Los cinco datos de la tabla anterior continúan **no verificados**.\n'
    p.write_text(text,encoding='utf-8')
    (ROOT/'borradores/captions_verificacion.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2),encoding='utf-8')
    progress('paso 1 terminado: captions Día 1/2 recuperados de los originales, cambios anotados y <900 caracteres/5 hashtags; Día 3 pendiente (no tiene caption original). Datos API de Meta aportados por el padre registrados, cinco límites restantes no verificados.')
    print([(x['dia'],x['caracteres']) for x in sources])

def fonts():
    target=ROOT/'herramientas/fuentes'; target.mkdir(exist_ok=True)
    sample='Á É Í Ó Ú Ñ á é í ó ú ñ ¿ ¡ → ·'
    sheet=Image.new('RGB',(1600,450),'#0B0B0F'); d=ImageDraw.Draw(sheet)
    report=[]
    for i,name in enumerate(['space-grotesk-latin-700-normal','space-grotesk-latin-500-normal','instrument-serif-latin-400-italic']):
        font=TTFont(SERIE/'marca/fonts'/f'{name}.woff2'); font.flavor=None; dest=target/f'{name}.ttf'; font.save(dest)
        cmap=font.getBestCmap(); missing=[c for c in sample if c!=' ' and (ord(c) not in cmap or cmap.get(ord(c))=='.notdef')]
        added=[]
        if missing==['→']:
            # Derivado local: la WOFF2 latin original no incluye U+2192.
            from fontTools.pens.ttGlyphPen import TTGlyphPen
            u=font['head'].unitsPerEm
            pen=TTGlyphPen(None)
            points=[(.08,.29),(.65,.29),(.48,.46),(.55,.53),(.84,.24),(.55,-.05),(.48,.02),(.65,.19),(.08,.19)]
            pen.moveTo((round(points[0][0]*u),round(points[0][1]*u)))
            for x,y in points[1:]: pen.lineTo((round(x*u),round(y*u)))
            pen.closePath()
            order=font.getGlyphOrder(); order.append('arrowright.local'); font.setGlyphOrder(order)
            font['glyf']['arrowright.local']=pen.glyph(); font['hmtx']['arrowright.local']=(round(.92*u),round(.08*u))
            for table in font['cmap'].tables:
                if table.isUnicode(): table.cmap[0x2192]='arrowright.local'
            font.save(dest); added=['→']; cmap=font.getBestCmap()
            missing=[c for c in sample if c!=' ' and ord(c) not in cmap]
        assert not missing,(name,missing)
        pil=ImageFont.truetype(str(dest),56)
        for c in sample.replace(' ',''): assert pil.getmask(c).getbbox(),(name,c)
        d.text((30,10+i*145),name,font=ImageFont.truetype(str(dest),24),fill='#F4F2EE')
        d.text((30,50+i*145),sample,font=pil,fill='#F4F2EE')
        report.append({'fuente':name,'pillow':True,'muestra':sample,'glifos_faltantes':missing,'glifos_locales_agregados':added})
    sheet.save(ROOT/'borradores/prueba_fuentes.png')
    (target/'verificacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    progress('paso 2 terminado: tres WOFF2 convertidas a TTF sin instalar; Pillow abre las tres y cmap/máscaras verifican todos los glifos Á É Í Ó Ú Ñ á é í ó ú ñ ¿ ¡ → ·. La flecha U+2192 ausente se agrega como contorno geométrico en las TTF derivadas (originales intactos); detalle en herramientas/fuentes/verificacion.json. Prueba visual: borradores/prueba_fuentes.png.')
    print('3 TTF: Pillow y cobertura OK')
if __name__=='__main__':
    import sys
    {'captions':captions,'fonts':fonts}[sys.argv[1]]()
