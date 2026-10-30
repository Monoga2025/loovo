// Nodo Code "Armar respuesta". Si la IA fallo (onError: continue), la conciliacion igual se entrega.
const conciliacion = $('Conciliar (determinista)').first().json;
const ia = $input.first().json;
const texto = ia && ia.choices && ia.choices[0] && ia.choices[0].message ? ia.choices[0].message.content : null;
return [{
  json: {
    resumen_ejecutivo_ia: texto || null,
    aviso_ia: texto ? 'Resumen redactado por IA a partir de cifras calculadas por codigo; la IA no concilia.' : 'No se pudo generar el resumen con IA; la conciliacion es valida.',
    conciliacion,
  },
}];
