// Prueba local (Node) de la logica del nodo Code de D3 contra datos-prueba/.
// Uso: node scripts/probar-d3.js     (NO prueba n8n: solo el JavaScript del nodo)
const fs = require('fs');
const path = require('path');

const raiz = path.join(__dirname, '..');
const src = fs.readFileSync(path.join(__dirname, 'd3-conciliador-nodo.js'), 'utf8');
const extracto = fs.readFileSync(path.join(raiz, 'datos-prueba', 'extracto-bancolombia-ejemplo.csv'), 'utf8');
const auxiliar = fs.readFileSync(path.join(raiz, 'datos-prueba', 'libro-auxiliar-bancos-ejemplo.csv'), 'utf8');

function ejecutar(items, ventanaWebhook) {
  const mock$ = (nombre) => {
    if (nombre !== 'Webhook D3' || ventanaWebhook === undefined) throw new Error('nodo no disponible');
    return { first: () => ({ json: { query: { ventana: String(ventanaWebhook) } } }) };
  };
  const fn = new Function('$input', '$', src);
  return fn({ all: () => items }, mock$)[0].json;
}

let fallos = 0;
function igual(nombre, esperado, obtenido) {
  const ok = JSON.stringify(esperado) === JSON.stringify(obtenido);
  if (!ok) fallos++;
  console.log(`${ok ? 'OK  ' : 'FALLA'} ${nombre}\n       esperado: ${JSON.stringify(esperado)}\n       obtenido: ${JSON.stringify(obtenido)}`);
}

const items = [{ json: { tipo: 'extracto', texto: extracto } }, { json: { tipo: 'auxiliar', texto: auxiliar } }];
const r = ejecutar(items);
const desc = (arr, f) => arr.map(f);

console.log('--- Escenario 1: ventana por defecto (3 dias) ---');
igual('conciliadas / exactas / en ventana', [7, 4, 3], [r.resumen.conciliadas, r.resumen.conciliadas_exactas, r.resumen.conciliadas_en_ventana]);
igual('pares conciliados (banco->libro, tipo, dif dias)',
  [['REF0001', 'RC-0101', 'exacto', 0], ['REF0002', 'CE-0201', 'exacto', 0], ['REF0003', 'RC-0102', 'ventana', 2], ['REF0004', 'CE-0202', 'ventana', 3],
   ['REF0005', 'CE-0203', 'exacto', 0], ['REF0006', 'RC-0103', 'exacto', 0], ['REF0007', 'RC-0104', 'ventana', 1]]
    .sort(),
  desc(r.partidas_conciliadas, (c) => [c.banco.ref, c.libro.ref, c.tipo_match, c.diferencia_dias]).sort());
igual('solo en bancos: cantidad (17 movimientos - 7 conciliados)', 10, r.en_bancos_no_libros.length);
igual('solo en bancos: por categoria', { 'GMF 4x1000': 4, 'Cuota de manejo': 1, 'IVA comision': 2, 'Comision ACH': 1, 'Sin contabilizar': 2 },
  r.en_bancos_no_libros.reduce((a, e) => ((a[e.categoria] = (a[e.categoria] || 0) + 1), a), {}));
igual('partidas sin contabilizar (no cargos)', [-380000, 750000], r.en_bancos_no_libros.filter((e) => e.categoria === 'Sin contabilizar').map((e) => e.monto).sort((a, b) => a - b));
igual('cargos por categoria (cantidad, total)',
  Object.fromEntries(Object.entries({ 'GMF 4x1000': [4, -35720], 'IVA comision': [2, -4066], 'Cuota de manejo': [1, -18900], 'Comision ACH': [1, -2500] }).sort()),
  Object.fromEntries(Object.entries(r.cargos_bancarios_por_categoria).map(([k, v]) => [k, [v.cantidad, v.total]]).sort()));
igual('solo en libros (montos)', [-600000, -380000, 1100000], r.en_libros_no_bancos.map((e) => e.monto).sort((a, b) => a - b));
igual('fila TOTALES del libro marcada invalida', 1, r.filas_invalidas.length);
igual('total banco / total libros / diferencia', [158814, -30000, 188814], [r.resumen.total_banco, r.resumen.total_libros, r.resumen.diferencia_banco_menos_libros]);
igual('neto solo banco / neto solo libros / cuadra', [308814, 120000, true], [r.resumen.neto_solo_banco, r.resumen.neto_solo_libros, r.resumen.cuadra]);
igual('GMF registrado vs teorico 4x1000', [35720, 35720], [r.verificaciones_informativas.gmf_registrado, r.verificaciones_informativas.gmf_teorico_4x1000_sobre_egresos]);
igual('IVA registrado vs 19% teorico', [4066, 4066], [r.verificaciones_informativas.iva_registrado_en_comisiones, r.verificaciones_informativas.iva_19pct_teorico_sobre_comisiones]);

console.log('--- Escenario 2: ventana = 1 (query ?ventana=1) ---');
const r1 = ejecutar(items, 1);
igual('conciliadas / en ventana / solo banco / solo libros', [5, 1, 12, 5], [r1.resumen.conciliadas, r1.resumen.conciliadas_en_ventana, r1.resumen.solo_banco, r1.resumen.solo_libros]);
igual('cuadra con ventana 1', true, r1.resumen.cuadra);

console.log('--- Escenario 3: ventana = 0 (solo exactas) ---');
const r0 = ejecutar(items, 0);
igual('conciliadas / en ventana', [4, 0], [r0.resumen.conciliadas, r0.resumen.conciliadas_en_ventana]);

console.log('--- Escenario 4: filas tipo Excel (objetos, fecha serial y numeros) ---');
const rx = ejecutar([
  { json: { tipo: 'extracto', Fecha: '2026-10-01T00:00:00.000Z', Descripcion: 'GMF 4X1000', Valor: -400 } },
  { json: { tipo: 'extracto', Fecha: 46296, Descripcion: 'Abono', Valor: 1000000 } }, // 46296 = 2026-10-01 (serial Excel)
  { json: { tipo: 'auxiliar', Fecha: '2026-10-02', Detalle: 'Recaudo', Debito: 1000000, Credito: 0 } },
]);
igual('Excel: conciliada en ventana 1 dia + GMF solo banco', [1, 'ventana', 1, 'GMF 4x1000'],
  [rx.resumen.conciliadas, rx.partidas_conciliadas[0] && rx.partidas_conciliadas[0].tipo_match, rx.en_bancos_no_libros.length, rx.en_bancos_no_libros[0] && rx.en_bancos_no_libros[0].categoria]);

console.log('--- Escenario 5: errores esperados ---');
let msg = '';
try { ejecutar([{ json: { tipo: 'extracto', texto: extracto } }]); } catch (e) { msg = e.message; }
igual('sin auxiliar lanza error claro', true, /Faltan datos/.test(msg));
msg = '';
try { ejecutar([{ json: { Fecha: '2026-10-01', Valor: 5 } }]); } catch (e) { msg = e.message; }
igual('item sin tipo lanza error claro', true, /tipo = extracto/.test(msg));

console.log(fallos === 0 ? '\nRESULTADO: todas las comprobaciones pasaron' : `\nRESULTADO: ${fallos} comprobacion(es) FALLARON`);
process.exit(fallos === 0 ? 0 : 1);
