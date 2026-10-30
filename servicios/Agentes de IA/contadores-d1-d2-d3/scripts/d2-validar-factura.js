// Nodo Code "Validar y normalizar" (modo: Run Once for All Items).
// Valida con reglas deterministas lo que el modelo extrajo: digito de verificacion del NIT, formato CUFE, Subtotal + IVA = Total.
const PESOS_NIT = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71];
function digitoVerificacion(nit) { // algoritmo modulo 11 de la DIAN
  const d = String(nit).replace(/\D/g, '').split('').reverse();
  if (!d.length || d.length > 15) return null;
  const s = d.reduce((acc, x, i) => acc + Number(x) * PESOS_NIT[i], 0);
  const r = s % 11;
  return r > 1 ? 11 - r : r;
}

const resp = $input.first().json;
const crudo = resp && resp.choices && resp.choices[0] && resp.choices[0].message;
if (!crudo || !crudo.content) {
  throw new Error(`El modelo no devolvio contenido (${(resp && resp.choices && resp.choices[0] && resp.choices[0].finish_reason) || 'sin respuesta'}${crudo && crudo.refusal ? ': ' + crudo.refusal : ''}).`);
}
let d;
try { d = JSON.parse(crudo.content); } catch (e) { throw new Error('La respuesta del modelo no es JSON valido.'); }

let meta = {};
try { meta = $('Webhook D2').first().json.body || {}; } catch (e) { /* pruebas locales */ }

const num = (x) => (typeof x === 'number' && Number.isFinite(x) ? x : null);
const subtotal = num(d.subtotal), iva = num(d.iva), total = num(d.total);
const retefuente = num(d.retefuente) ?? 0, reteica = num(d.reteica) ?? 0;
const problemas = [];

if (!d.fecha || !/^\d{4}-\d{2}-\d{2}$/.test(d.fecha) || Number.isNaN(Date.parse(d.fecha))) problemas.push('fecha ausente o invalida');

let nit = d.nit_emisor ? String(d.nit_emisor).trim() : null;
if (!nit) problemas.push('NIT del emisor ausente');
else {
  const m = nit.replace(/[.\s]/g, '').match(/^(\d{5,15})-?(\d)?$/);
  if (!m) problemas.push('NIT con formato no reconocido');
  else {
    const dv = digitoVerificacion(m[1]);
    if (m[2] === undefined) { problemas.push('NIT sin digito de verificacion'); nit = m[1]; }
    else {
      nit = `${m[1]}-${m[2]}`;
      if (Number(m[2]) !== dv) problemas.push(`digito de verificacion del NIT no coincide (esperado ${dv})`);
    }
  }
}

const cufe = d.cufe ? String(d.cufe).replace(/\s/g, '').toLowerCase() : null;
if (cufe && !/^[0-9a-f]{96}$/.test(cufe)) problemas.push('CUFE no tiene 96 caracteres hexadecimales');
if (!cufe && !d.numero_factura) problemas.push('sin CUFE ni numero de factura');

if (subtotal === null || iva === null || total === null) problemas.push('falta subtotal, IVA o total');
else {
  if (Math.abs(subtotal + iva - total) > 1) problemas.push('Subtotal + IVA no es igual al Total');
  if (subtotal > 0) {
    const tarifa = iva / subtotal;
    if (![0, 0.05, 0.19].some((t) => Math.abs(tarifa - t) < 0.005)) problemas.push(`IVA/Subtotal = ${(tarifa * 100).toFixed(2)}% (no es 0%, 5% ni 19%)`);
  }
}
if (d.notas) problemas.push(`nota del modelo: ${d.notas}`);

const fila = {
  'Fecha': d.fecha ?? '',
  'NIT Emisor': nit ?? '',
  'Razón Social': d.razon_social ?? '',
  'CUFE / Número Factura': cufe || d.numero_factura || '',
  'Subtotal': subtotal ?? '',
  'IVA': iva ?? '',
  'Retefuente': retefuente,
  'ReteICA': reteica,
  'Total': total ?? '',
  'Categoría PUC sugerida': d.categoria_puc_sugerida ?? '',
  'Validación': problemas.length ? `REVISAR: ${problemas.join('; ')}` : 'OK',
  'Canal': meta.canal || 'webhook',
  'Procesado': new Date().toISOString(),
};
return [{ json: fila }];
