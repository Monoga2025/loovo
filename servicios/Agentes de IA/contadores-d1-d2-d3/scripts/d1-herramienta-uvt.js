// Herramienta (Code Tool) del agente D1: UVT + tabla de retencion del Art. 383 ET (calculo determinista, el LLM no hace aritmetica).
// Entrada `query` (texto): "uvt" | "art383:<base en UVT>" | "cop_a_uvt:<pesos>" | "uvt_a_cop:<uvt>"

// >>> VERIFICAR con resolucion DIAN <<<  Valor de la UVT 2026 en pesos (COP por 1 UVT). Dejar null hasta confirmarlo.
const UVT_2026 = null;
const UVT_FUENTE = 'VERIFICAR con resolucion DIAN (resolucion anual de la UVT); no configurada';

// Art. 383 ET: [desde (UVT), hasta (UVT), tarifa marginal, UVT sumadas]
const TABLA_383 = [
  [0, 95, 0, 0],
  [95, 150, 0.19, 0],
  [150, 360, 0.28, 10],
  [360, 640, 0.33, 69],
  [640, 945, 0.35, 162],
  [945, 2300, 0.37, 268],
  [2300, Infinity, 0.39, 770],
];

const redondear = (n, d = 2) => Math.round(n * 10 ** d) / 10 ** d;
const aNumero = (txt) => {
  const s = String(txt ?? '').replace(/[\s$]/g, '');
  const n = /^\d+(\.\d+)?$/.test(s) ? Number(s) : Number(s.replace(/\./g, '').replace(',', '.'));
  return Number.isFinite(n) && n >= 0 ? n : null;
};
const hayUvt = typeof UVT_2026 === 'number' && UVT_2026 > 0;

function retencion383(baseUvt) {
  for (const [desde, hasta, tarifa, suma] of TABLA_383) {
    if (baseUvt > desde && baseUvt <= hasta) {
      return { tarifa_marginal: tarifa, retencion_uvt: redondear(Math.max(0, baseUvt - desde) * tarifa + suma) };
    }
  }
  return { tarifa_marginal: 0, retencion_uvt: 0 };
}

const [orden, arg] = String(query).trim().toLowerCase().split(':');
let salida;
if (orden === 'uvt') {
  salida = { uvt_2026_cop: hayUvt ? UVT_2026 : null, estado: hayUvt ? 'configurada' : UVT_FUENTE };
} else if (orden === 'art383') {
  const base = aNumero(arg);
  if (base === null) salida = { error: 'Usa art383:<base gravable en UVT>, p. ej. art383:200' };
  else {
    const r = retencion383(base);
    salida = {
      articulo: 'Art. 383 ET', base_uvt: base, ...r,
      retencion_cop: hayUvt ? redondear(r.retencion_uvt * UVT_2026, 0) : null,
      aviso_uvt: hayUvt ? null : UVT_FUENTE,
      nota: 'La base debe ser la base gravable en UVT despues de depuracion (Art. 387 ET, rentas exentas y limites). Confirmar con la norma vigente.',
    };
  }
} else if (orden === 'cop_a_uvt' || orden === 'uvt_a_cop') {
  const v = aNumero(arg);
  if (v === null) salida = { error: `Usa ${orden}:<numero>` };
  else if (!hayUvt) salida = { error: 'UVT 2026 no configurada', aviso_uvt: UVT_FUENTE };
  else salida = orden === 'cop_a_uvt' ? { cop: v, uvt: redondear(v / UVT_2026, 2) } : { uvt: v, cop: redondear(v * UVT_2026, 0) };
} else {
  salida = { error: 'Comando no reconocido. Usa: uvt | art383:<uvt> | cop_a_uvt:<pesos> | uvt_a_cop:<uvt>' };
}
return JSON.stringify(salida);
