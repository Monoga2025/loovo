// Pruebas locales (Node) del JavaScript de D1 (herramienta UVT, articulos) y D2 (preparar Vision, validar).
// NO prueba n8n ni llama a OpenAI: la extraccion por vision se simula con una respuesta fija.
const fs = require('fs');
const path = require('path');
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const leer = (f) => fs.readFileSync(path.join(__dirname, f), 'utf8');
let fallos = 0;
function igual(nombre, esperado, obtenido) {
  const ok = JSON.stringify(esperado) === JSON.stringify(obtenido);
  if (!ok) fallos++;
  console.log(`${ok ? 'OK  ' : 'FALLA'} ${nombre}${ok ? '' : `\n       esperado: ${JSON.stringify(esperado)}\n       obtenido: ${JSON.stringify(obtenido)}`}`);
}

// ---------- D1: herramienta
const herr = new Function('query', leer('d1-herramienta-uvt.js'));
const t = (q) => JSON.parse(herr(q));
console.log('--- D1: calcular_uvt_y_retencion ---');
igual('UVT sin configurar', [null, true], [t('uvt').uvt_2026_cop, /VERIFICAR con resolucion DIAN/.test(t('uvt').estado)]);
igual('art383 base 50 UVT -> 0', 0, t('art383:50').retencion_uvt);
igual('art383 base 100 UVT -> (100-95)*19% = 0.95', 0.95, t('art383:100').retencion_uvt);
igual('art383 base 200 UVT -> (200-150)*28%+10 = 24', 24, t('art383:200').retencion_uvt);
igual('art383 base 500 UVT -> (500-360)*33%+69 = 115.2', 115.2, t('art383:500').retencion_uvt);
igual('art383 base 700 UVT -> (700-640)*35%+162 = 183', 183, t('art383:700').retencion_uvt);
igual('art383 base 1000 UVT -> (1000-945)*37%+268 = 288.35', 288.35, t('art383:1000').retencion_uvt);
igual('art383 base 2500 UVT -> (2500-2300)*39%+770 = 848', 848, t('art383:2500').retencion_uvt);
igual('art383 sin UVT: retencion_cop null y aviso', [null, true], [t('art383:200').retencion_cop, /VERIFICAR/.test(t('art383:200').aviso_uvt)]);
igual('cop_a_uvt sin UVT no inventa valor', 'UVT 2026 no configurada', t('cop_a_uvt:1500000').error);
igual('comando invalido', true, /no reconocido/.test(t('hola').error));
// Con UVT de PRUEBA (valor ficticio SOLO para probar la aritmetica, no es la UVT real)
const herrConUvt = new Function('query', leer('d1-herramienta-uvt.js').replace('const UVT_2026 = null;', 'const UVT_2026 = 1000;'));
igual('con UVT ficticia 1000: art383:200 -> 24.000 COP; uvt_a_cop:95 -> 95.000', [24000, 95000], [JSON.parse(herrConUvt('art383:200')).retencion_cop, JSON.parse(herrConUvt('uvt_a_cop:95')).cop]);

console.log('--- D1: articulos ET (ingesta) ---');
const arts = new Function(leer('d1-articulos-et.js'))().map((x) => x.json);
igual('cantidad de articulos', 25, arts.length);
igual('Art. 383 y Art. 868 presentes', [true, true], ['Art. 383', 'Art. 868'].map((s) => arts.some((a) => a.section === s)));
igual('ningun valor en pesos de UVT en el texto (patron $ + digitos)', 0, arts.filter((a) => /\$\s?\d/.test(a.content)).length);
igual('Art. 868 marca la UVT 2026 como VERIFICAR', true, /VERIFICAR con resolucion DIAN/.test(arts.find((a) => a.section === 'Art. 868').content));

// ---------- D2: preparar Vision + validar
console.log('--- D2: preparar solicitud Vision (PDF de datos-prueba) ---');
const pdfPath = path.join(__dirname, '..', 'datos-prueba', 'factura-ejemplo-FICTICIA.pdf');
const pdf = fs.readFileSync(pdfPath);
const ctx = { helpers: { getBinaryDataBuffer: async () => pdf } };
(async () => {
  const prep = await new AsyncFunction('$input', leer('d2-preparar-vision.js')).call(ctx, { first: () => ({ json: {}, binary: { file: { mimeType: 'application/pdf', fileName: 'factura-ejemplo-FICTICIA.pdf' } } }) });
  const p = prep[0].json.payload;
  igual('payload: modelo, schema estricto y parte PDF base64', ['gpt-4o-mini', true, 'file', true],
    [p.model, p.response_format.json_schema.strict, p.messages[1].content[1].type, p.messages[1].content[1].file.file_data.startsWith('data:application/pdf;base64,JVBERi0')]);
  let msg = '';
  try { await new AsyncFunction('$input', leer('d2-preparar-vision.js')).call(ctx, { first: () => ({ json: {}, binary: { file: { mimeType: 'text/plain' } } }) }); } catch (e) { msg = e.message; }
  igual('tipo no soportado lanza error claro', true, /no soportado/.test(msg));

  console.log('--- D2: validar y normalizar (respuesta del modelo SIMULADA) ---');
  const validar = (contenido) => new Function('$input', '$', leer('d2-validar-factura.js'))(
    { first: () => ({ json: { choices: [{ message: { content: JSON.stringify(contenido) }, finish_reason: 'stop' }] } }) },
    () => { throw new Error('sin webhook'); })[0].json;
  const bueno = { fecha: '2026-10-05', nit_emisor: '901234567-' + (() => { const P = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]; const s = '901234567'.split('').reverse().reduce((a, x, i) => a + +x * P[i], 0); const r = s % 11; return r > 1 ? 11 - r : r; })(),
    razon_social: 'SERVICIOS CONTABLES DEMO S.A.S.', cufe: 'ab12cd34'.repeat(12), numero_factura: 'FE-1001', subtotal: 1000000, iva: 190000, retefuente: 110000, reteica: 9660, total: 1190000, categoria_puc_sugerida: '5110 Honorarios', notas: null };
  const ok = validar(bueno);
  igual('factura de prueba -> Validacion OK', 'OK', ok['Validación']);
  igual('columnas de salida', ['Fecha', 'NIT Emisor', 'Razón Social', 'CUFE / Número Factura', 'Subtotal', 'IVA', 'Retefuente', 'ReteICA', 'Total', 'Categoría PUC sugerida', 'Validación', 'Canal', 'Procesado'], Object.keys(ok));
  igual('valores clave', ['901234567-' + bueno.nit_emisor.split('-')[1], 1000000, 190000, 110000, 9660, 1190000, '5110 Honorarios'],
    [ok['NIT Emisor'], ok['Subtotal'], ok['IVA'], ok['Retefuente'], ok['ReteICA'], ok['Total'], ok['Categoría PUC sugerida']]);
  const dvMal = validar({ ...bueno, nit_emisor: '901234567-0' });
  igual('DV incorrecto -> REVISAR', true, /REVISAR/.test(dvMal['Validación']) && /digito de verificacion/.test(dvMal['Validación']));
  igual('Subtotal+IVA != Total -> REVISAR', true, /Subtotal \+ IVA/.test(validar({ ...bueno, total: 1200000 })['Validación']));
  igual('CUFE mal formado -> REVISAR', true, /CUFE/.test(validar({ ...bueno, cufe: 'xyz' })['Validación']));
  igual('retenciones null -> 0 (no inventa)', [0, 0], (() => { const r = validar({ ...bueno, retefuente: null, reteica: null }); return [r['Retefuente'], r['ReteICA']]; })());

  console.log(fallos === 0 ? '\nRESULTADO: todas las comprobaciones pasaron' : `\nRESULTADO: ${fallos} comprobacion(es) FALLARON`);
  process.exit(fallos === 0 ? 0 : 1);
})();
