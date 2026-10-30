// Nodo Code "Separar archivos" (modo: Run Once for All Items).
// Webhook multipart: campos binarios "extracto" y "auxiliar". CSV/TXT se decodifica a texto; XLSX pasa a Extract From File.
const entrada = $input.first();
const salida = [];
for (const tipo of ['extracto', 'auxiliar']) {
  const bin = entrada.binary && entrada.binary[tipo];
  if (!bin) throw new Error(`Falta el archivo "${tipo}" (multipart/form-data, campo "${tipo}").`);
  const nombre = (bin.fileName || '').toLowerCase();
  const mime = (bin.mimeType || '').toLowerCase();
  const esXlsx = /\.xlsx$/.test(nombre) || mime.includes('spreadsheetml');
  const esXls = /\.xls$/.test(nombre) || mime === 'application/vnd.ms-excel';
  if (esXls) throw new Error(`"${tipo}": el formato .xls antiguo no esta soportado; guardalo como .xlsx o .csv.`);
  if (esXlsx) {
    salida.push({ json: { tipo, es_excel: true }, binary: { data: bin } });
    continue;
  }
  const buf = await this.helpers.getBinaryDataBuffer(0, tipo);
  let texto = buf.toString('utf8');
  if (texto.includes('�')) texto = buf.toString('latin1'); // exportes bancarios en ANSI/Latin-1
  salida.push({ json: { tipo, es_excel: false, texto } });
}
return salida;
