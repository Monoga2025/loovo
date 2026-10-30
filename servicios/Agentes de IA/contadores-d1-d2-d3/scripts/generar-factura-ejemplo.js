// Genera datos-prueba/factura-ejemplo-FICTICIA.pdf (PDF de texto minimo, sin dependencias). Datos 100% inventados.
const fs = require('fs');
const path = require('path');

const PESOS = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71];
const dv = (nit) => { const s = String(nit).split('').reverse().reduce((a, x, i) => a + Number(x) * PESOS[i], 0); const r = s % 11; return r > 1 ? 11 - r : r; };
const NIT = '901234567';
const NIT_DV = `${NIT}-${dv(NIT)}`;
const CUFE = 'ab12cd34'.repeat(12); // 96 hex, obviamente ficticio

const lineas = [
  [16, 'FACTURA ELECTRONICA DE VENTA - EJEMPLO FICTICIO'],
  [10, '*** DOCUMENTO DE PRUEBA: DATOS INVENTADOS, SIN VALIDEZ FISCAL ***'],
  [10, ''],
  [11, 'No. FE-1001                               Fecha de emision: 2026-10-05'],
  [11, 'Emisor: SERVICIOS CONTABLES DEMO S.A.S. (ficticia)'],
  [11, `NIT: ${NIT_DV}`],
  [11, 'Direccion: Calle 0 No. 0-00, Ciudad Ejemplo, Colombia'],
  [10, ''],
  [11, 'Adquirente: CLIENTE DE PRUEBA LTDA (ficticia)   NIT: 900000000-0'],
  [10, ''],
  [11, 'Descripcion                                         Cantidad      Valor'],
  [11, 'Honorarios por asesoria contable (octubre)            1       1.000.000'],
  [10, ''],
  [11, 'Subtotal                                                        1.000.000'],
  [11, 'IVA 19%                                                           190.000'],
  [11, 'Total factura                                                    1.190.000'],
  [10, ''],
  [11, 'Retefuente (ejemplo 11%)                                           110.000'],
  [11, 'ReteICA (ejemplo)                                                    9.660'],
  [10, ''],
  [9, `CUFE: ${CUFE}`],
  [9, 'Valores y retenciones de ejemplo; no corresponden a ninguna operacion real.'],
];

const esc = (s) => s.replace(/\\/g, '\\\\').replace(/\(/g, '\\(').replace(/\)/g, '\\)');
let y = 790;
let contenido = 'BT\n';
for (const [size, texto] of lineas) {
  contenido += `/F1 ${size} Tf 1 0 0 1 40 ${y} Tm (${esc(texto)}) Tj\n`;
  y -= size + 8;
}
contenido += 'ET\n';
// El texto de la factura usa Courier para alinear columnas
const objs = [
  '<< /Type /Catalog /Pages 2 0 R >>',
  '<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
  '<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>',
  `<< /Length ${Buffer.byteLength(contenido, 'latin1')} >>\nstream\n${contenido}endstream`,
  '<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>',
];
let pdf = '%PDF-1.4\n';
const offsets = [];
objs.forEach((o, i) => { offsets.push(Buffer.byteLength(pdf, 'latin1')); pdf += `${i + 1} 0 obj\n${o}\nendobj\n`; });
const xref = Buffer.byteLength(pdf, 'latin1');
pdf += `xref\n0 ${objs.length + 1}\n0000000000 65535 f \n` + offsets.map((o) => `${String(o).padStart(10, '0')} 00000 n \n`).join('');
pdf += `trailer\n<< /Size ${objs.length + 1} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`;
const salida = path.join(__dirname, '..', 'datos-prueba', 'factura-ejemplo-FICTICIA.pdf');
fs.writeFileSync(salida, Buffer.from(pdf, 'latin1'));
console.log('PDF generado:', salida, '| NIT con DV:', NIT_DV, '| CUFE ficticio:', CUFE.length, 'caracteres');
