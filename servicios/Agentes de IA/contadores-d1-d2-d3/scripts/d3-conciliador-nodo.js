// ===== Nodo Code D3: conciliacion bancaria DETERMINISTA (sin IA) =====
// Modo: "Run Once for All Items". Entrada: items {tipo:'extracto'|'auxiliar', texto} (CSV)
// o filas de Excel {tipo, ...columnas}. Salida: 1 item con la conciliacion.
// Convencion de signo (ambos lados): ingreso al banco = positivo, egreso = negativo.
//   Extracto: credito (abono) = +, debito (cargo) = -.   Auxiliar de Bancos: debito = +, credito = -.

const VENTANA_DEFECTO = 3;

const sinTildes = (s) => String(s ?? '').normalize('NFD').replace(/[̀-ͯ]/g, '');
const norm = (s) => sinTildes(s).toLowerCase().trim();

function detectarDelimitador(linea) {
  const cand = [';', ',', '\t', '|'];
  let mejor = ',', max = -1;
  for (const d of cand) {
    const n = linea.split(d).length - 1;
    if (n > max) { max = n; mejor = d; }
  }
  return mejor;
}

function parseCSV(texto) {
  const t = String(texto ?? '').replace(/^﻿/, '');
  const primera = t.split(/\r?\n/).find((l) => l.trim() !== '') || '';
  const delim = detectarDelimitador(primera);
  const filas = [];
  let fila = [], campo = '', comillas = false;
  for (let i = 0; i < t.length; i++) {
    const c = t[i];
    if (comillas) {
      if (c === '"' && t[i + 1] === '"') { campo += '"'; i++; }
      else if (c === '"') comillas = false;
      else campo += c;
    } else if (c === '"') comillas = true;
    else if (c === delim) { fila.push(campo); campo = ''; }
    else if (c === '\n' || c === '\r') {
      if (c === '\r' && t[i + 1] === '\n') i++;
      fila.push(campo); campo = '';
      if (fila.some((x) => x.trim() !== '')) filas.push(fila);
      fila = [];
    } else campo += c;
  }
  fila.push(campo);
  if (fila.some((x) => x.trim() !== '')) filas.push(fila);
  return filas;
}

// Convierte a objetos usando la fila de encabezado (la primera con "fecha" y algun campo de valor)
function filasAObjetos(matriz) {
  const idx = matriz.findIndex((f, i) => i < 20 &&
    f.some((c) => norm(c).includes('fecha')) &&
    f.some((c) => /valor|monto|importe|debito|credito/.test(norm(c))));
  if (idx < 0) throw new Error('No se encontro la fila de encabezados (se espera una columna "Fecha" y "Valor" o "Debito/Credito").');
  const enc = matriz[idx].map((c) => c.trim());
  return matriz.slice(idx + 1).map((f) => {
    const o = {};
    enc.forEach((h, j) => { o[h] = (f[j] ?? '').trim(); });
    return o;
  });
}

// Devuelve centavos (entero) o null. Acepta 1.234.567,89 | 1,234,567.89 | -50.000 | (50.000) | $ 1.000
function parseMonto(v) {
  if (typeof v === 'number') return Math.round(v * 100);
  let s = String(v ?? '').trim();
  if (s === '') return null;
  let neg = false;
  if (/^\(.*\)$/.test(s)) { neg = true; s = s.slice(1, -1); }
  s = s.replace(/[$\s]|COP/gi, '');
  if (s.startsWith('-')) { neg = !neg; s = s.slice(1); }
  if (s.endsWith('-')) { neg = !neg; s = s.slice(0, -1); }
  if (s.startsWith('+')) s = s.slice(1);
  const p = s.lastIndexOf('.'), c = s.lastIndexOf(',');
  if (p >= 0 && c >= 0) {
    const dec = p > c ? '.' : ',';
    s = dec === '.' ? s.replace(/,/g, '') : s.replace(/\./g, '').replace(',', '.');
  } else if (p >= 0 || c >= 0) {
    const sep = p >= 0 ? '.' : ',';
    const partes = s.split(sep);
    const esMiles = partes.length > 2 || (partes.length === 2 && partes[1].length === 3 && partes[0] !== '0');
    s = esMiles ? partes.join('') : partes.join('.');
  }
  if (!/^\d+(\.\d+)?$/.test(s)) return null;
  const n = Math.round(parseFloat(s) * 100);
  return neg ? -n : n;
}

function parseFecha(v) {
  if (v === null || v === undefined || v === '') return null;
  let y, m, d;
  if (typeof v === 'number' && v > 20000 && v < 90000) { // serial de Excel
    const dt = new Date(Math.round((v - 25569) * 86400000));
    y = dt.getUTCFullYear(); m = dt.getUTCMonth() + 1; d = dt.getUTCDate();
  } else {
    const s = String(v).trim();
    let r;
    if ((r = s.match(/^(\d{4})[-\/.](\d{1,2})[-\/.](\d{1,2})/))) { y = +r[1]; m = +r[2]; d = +r[3]; }
    else if ((r = s.match(/^(\d{1,2})[-\/.](\d{1,2})[-\/.](\d{4})/))) { d = +r[1]; m = +r[2]; y = +r[3]; } // formato Colombia DD/MM/AAAA
    else return null;
  }
  const ms = Date.UTC(y, m - 1, d);
  const chk = new Date(ms);
  if (chk.getUTCFullYear() !== y || chk.getUTCMonth() !== m - 1 || chk.getUTCDate() !== d) return null;
  return { iso: chk.toISOString().slice(0, 10), dias: Math.round(ms / 86400000) };
}

function normalizarFilas(objetos, tipo) {
  const out = [];
  const esBanco = tipo === 'extracto';
  objetos.forEach((o, n) => {
    const claves = Object.keys(o);
    const k = (re) => claves.find((c) => re.test(norm(c)));
    const kFecha = k(/fecha/), kVal = k(/^(valor|monto|importe|valor total)$/);
    const kDeb = k(/debito/), kCre = k(/credito/);
    const kTipo = k(/^(tipo|naturaleza|transaccion|tipo transaccion)$/);
    const kRef = k(/^(referencia|ref|documento|comprobante|cheque|numero)/);
    const textos = claves.filter((c) => /descrip|detalle|concepto|tercero|nombre/.test(norm(c))).map((c) => String(o[c] ?? '').trim()).filter(Boolean);
    const f = parseFecha(o[kFecha]);
    let monto = null;
    if (kDeb || kCre) {
      const deb = parseMonto(o[kDeb]) ?? 0, cre = parseMonto(o[kCre]) ?? 0;
      monto = esBanco ? (cre - deb) : (deb - cre);
    }
    if ((monto === null || monto === 0) && kVal) {
      const v = parseMonto(o[kVal]);
      if (v !== null) {
        monto = v;
        const t = kTipo ? norm(o[kTipo]) : '';
        if (t && v > 0 && /^(d|debito)/.test(t)) monto = esBanco ? -v : v;
        else if (t && v > 0 && /^(c|credito)/.test(t)) monto = esBanco ? v : -v;
      }
    }
    if (!f || monto === null || monto === 0) {
      const tieneDatos = claves.some((c) => String(o[c] ?? '').trim() !== '');
      if (tieneDatos && (f || monto !== null)) {
        out.push({ _invalida: true, fila: n + 1, motivo: !f ? 'fecha no interpretable' : 'monto cero o no interpretable' });
      }
      return; // filas vacias se ignoran
    }
    out.push({
      fila: n + 1, fecha: f.iso, dias: f.dias, monto,
      descripcion: textos.join(' | '), ref: kRef ? String(o[kRef] ?? '').trim() : '',
    });
  });
  return out;
}

// Orden importa: IVA primero (una descripcion "IVA COMISION ACH" no debe caer en Comision ACH).
const REGLAS_CARGOS = [
  { categoria: 'IVA comision', re: /\bIVA\b/i, cuenta_sugerida: '2408 IVA descontable (VERIFICAR con contador)' },
  { categoria: 'GMF 4x1000', re: /\bGMF\b|4\s*[xX*]\s*1000|GRAVAMEN.*(MOV|FINANC)/i, cuenta_sugerida: '5115 Impuestos - GMF (VERIFICAR subcuenta)' },
  { categoria: 'Cuota de manejo', re: /CUOTA\s+(DE\s+)?MANEJO/i, cuenta_sugerida: '5305 Gastos financieros (VERIFICAR subcuenta)' },
  { categoria: 'Comision ACH', re: /COMIS\w*.*\bACH\b|\bACH\b.*COMIS\w*/i, cuenta_sugerida: '5305 Gastos financieros - comisiones (VERIFICAR subcuenta)' },
];
function clasificarCargo(descripcion, monto) {
  if (monto >= 0) return null; // los cargos bancarios son egresos
  const d = sinTildes(descripcion);
  for (const r of REGLAS_CARGOS) if (r.re.test(d)) return r;
  return null;
}

function conciliar(extracto, auxiliar, ventana) {
  const banco = extracto.filter((x) => !x._invalida).map((x) => ({ ...x, cargo: clasificarCargo(x.descripcion, x.monto) }));
  const libros = auxiliar.filter((x) => !x._invalida).map((x) => ({ ...x }));
  const usadoL = new Set();
  const conciliadas = [];
  const emparejar = (b, maxDias, tipo) => {
    let mejor = null;
    for (const l of libros) {
      if (usadoL.has(l.id) || l.monto !== b.monto) continue;
      const dif = Math.abs(l.dias - b.dias);
      if (dif > maxDias) continue;
      if (!mejor || dif < mejor.dif) mejor = { l, dif };
    }
    if (mejor) {
      usadoL.add(mejor.l.id); b._par = true;
      conciliadas.push({ banco: b, libro: mejor.l, tipo_match: tipo, diferencia_dias: mejor.dif });
    }
  };
  const orden = (a, b) => (a.dias - b.dias) || (a.fila - b.fila);
  const normales = banco.filter((b) => !b.cargo).sort(orden);
  const cargos = banco.filter((b) => b.cargo).sort(orden);
  // Pasada 1: mismo dia y mismo monto. Pasada 2: ventana +-N dias, el mas cercano primero.
  // Las partidas normales se emparejan antes que los cargos bancarios.
  for (const grupo of [normales, cargos]) for (const b of grupo) if (!b._par) emparejar(b, 0, 'exacto');
  for (const grupo of [normales, cargos]) for (const b of grupo) if (!b._par) emparejar(b, ventana, 'ventana');

  const limpio = (x) => ({ id: x.id, fila: x.fila, fecha: x.fecha, monto: x.monto / 100, descripcion: x.descripcion, ref: x.ref });
  const enBancos = banco.filter((b) => !b._par).sort(orden).map((b) => ({
    ...limpio(b), categoria: b.cargo ? b.cargo.categoria : 'Sin contabilizar',
    cuenta_sugerida: b.cargo ? b.cargo.cuenta_sugerida : null,
  }));
  const enLibros = libros.filter((l) => !usadoL.has(l.id)).sort(orden).map(limpio);
  const conc = conciliadas.sort((a, b) => (a.banco.dias - b.banco.dias) || (a.banco.fila - b.banco.fila)).map((c) => ({
    banco: limpio(c.banco), libro: limpio(c.libro), tipo_match: c.tipo_match, diferencia_dias: c.diferencia_dias,
  }));

  const cents = (arr) => arr.reduce((s, x) => s + Math.round(x.monto * 100), 0);
  const cargosPorCategoria = {};
  for (const e of enBancos) {
    if (e.categoria === 'Sin contabilizar') continue;
    const c = (cargosPorCategoria[e.categoria] ||= { cantidad: 0, total_centavos: 0, cuenta_sugerida: e.cuenta_sugerida });
    c.cantidad++; c.total_centavos += Math.round(e.monto * 100);
  }
  for (const c of Object.values(cargosPorCategoria)) { c.total = c.total_centavos / 100; delete c.total_centavos; }

  const totalBanco = banco.reduce((s, x) => s + x.monto, 0);
  const totalLibros = libros.reduce((s, x) => s + x.monto, 0);
  const netoBanco = cents(enBancos), netoLibros = cents(enLibros);
  const egresosNormales = banco.filter((b) => !b.cargo && b.monto < 0).reduce((s, b) => s + b.monto, 0);
  const sumaCat = (cats) => banco.filter((b) => b.cargo && cats.includes(b.cargo.categoria)).reduce((s, b) => s + b.monto, 0);
  const r2 = (n) => Math.round(n) / 100;
  return {
    parametros: { ventana_dias: ventana },
    partidas_conciliadas: conc,
    en_bancos_no_libros: enBancos,
    en_libros_no_bancos: enLibros,
    cargos_bancarios_por_categoria: cargosPorCategoria,
    filas_invalidas: [...extracto, ...auxiliar].filter((x) => x._invalida).map((x) => ({ fila: x.fila, motivo: x.motivo })),
    resumen: {
      movimientos_banco: banco.length, movimientos_libros: libros.length,
      conciliadas: conc.length,
      conciliadas_exactas: conc.filter((c) => c.tipo_match === 'exacto').length,
      conciliadas_en_ventana: conc.filter((c) => c.tipo_match === 'ventana').length,
      solo_banco: enBancos.length, solo_libros: enLibros.length,
      total_banco: r2(totalBanco), total_libros: r2(totalLibros),
      diferencia_banco_menos_libros: r2(totalBanco - totalLibros),
      neto_solo_banco: r2(netoBanco), neto_solo_libros: r2(netoLibros),
      cuadra: (totalBanco - totalLibros) === (netoBanco - netoLibros),
    },
    verificaciones_informativas: {
      gmf_registrado: r2(Math.abs(sumaCat(['GMF 4x1000']))),
      gmf_teorico_4x1000_sobre_egresos: r2(Math.abs(egresosNormales) * 0.004),
      iva_registrado_en_comisiones: r2(Math.abs(sumaCat(['IVA comision']))),
      iva_19pct_teorico_sobre_comisiones: r2(Math.abs(sumaCat(['Cuota de manejo', 'Comision ACH'])) * 0.19),
      nota: 'Informativo: el GMF puede tener exenciones (cuenta de ahorro exenta) y no todo cargo lleva IVA. Valida contra el extracto.',
    },
  };
}

function leerEntradas(items) {
  const grupos = { extracto: [], auxiliar: [] };
  for (const it of items) {
    const j = it.json ?? it;
    const tipo = j.tipo;
    if (tipo !== 'extracto' && tipo !== 'auxiliar') {
      throw new Error('Cada item debe traer tipo = extracto|auxiliar (con Excel, activa "Keep Source: JSON" en Extract From File).');
    }
    if (typeof j.texto === 'string') {
      grupos[tipo].push(...normalizarFilas(filasAObjetos(parseCSV(j.texto)), tipo));
    } else {
      const { tipo: _t, ruta: _r, ...fila } = j;
      grupos[tipo].push(...normalizarFilas([fila], tipo));
    }
  }
  for (const t of ['extracto', 'auxiliar']) { // ids y numero de fila consecutivos por archivo
    let n = 0;
    grupos[t].forEach((x, i) => { x.fila = i + 1; if (!x._invalida) x.id = `${t === 'extracto' ? 'B' : 'L'}${++n}`; });
  }
  if (!grupos.extracto.some((x) => !x._invalida) || !grupos.auxiliar.some((x) => !x._invalida)) {
    throw new Error('Faltan datos: se necesita al menos un movimiento valido en el extracto y en el auxiliar.');
  }
  return grupos;
}

let ventana = VENTANA_DEFECTO;
try {
  const q = $('Webhook D3').first().json.query || {};
  const v = parseInt(q.ventana, 10);
  if (Number.isInteger(v) && v >= 0 && v <= 31) ventana = v;
} catch (e) { /* sin webhook (pruebas locales): ventana por defecto */ }

const g = leerEntradas($input.all());
return [{ json: conciliar(g.extracto, g.auxiliar, ventana) }];
