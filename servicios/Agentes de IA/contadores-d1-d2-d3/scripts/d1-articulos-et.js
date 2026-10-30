// Nodo Code "Articulos clave ET" (ingesta rapida a Qdrant). Un item por articulo.
// IMPORTANTE: son RESUMENES OPERATIVOS de apoyo, no el texto literal del Estatuto Tributario.
// Ningun valor en pesos esta fijado: todo se expresa en UVT. El valor de la UVT 2026 va como "VERIFICAR con resolucion DIAN".
// Los articulos marcados verificar:true tienen cifras que deben confirmarse contra la norma vigente antes de usarse con clientes.

const AVISO = 'Resumen operativo de apoyo (no es texto literal del ET). Confirmar siempre contra la norma vigente.';
const A = [];
const add = (libro, art, titulo, texto, verificar = false) => A.push({
  chapter: libro, section: art, title: titulo, verificar,
  content: `${art} ET - ${titulo}. ${texto} ${verificar ? '[VERIFICAR vigencia/cifras contra la norma o resolucion DIAN vigente.] ' : ''}${AVISO}`,
});

add('Libro Quinto - Procedimiento / UVT', 'Art. 868', 'Unidad de Valor Tributario (UVT)',
  'La UVT es la medida de valor que se usa en las normas tributarias para expresar montos, bases y sanciones. La DIAN fija su valor en pesos cada ano mediante resolucion. Valor de la UVT 2026: VERIFICAR con resolucion DIAN (no se asume aqui).');

add('Libro Primero - Renta', 'Art. 240', 'Tarifa general del impuesto de renta para sociedades',
  'La tarifa general del impuesto sobre la renta para sociedades y entidades nacionales es del 35% (texto vigente tras la Ley 2277 de 2022).');

add('Libro Primero - Renta', 'Art. 241', 'Tarifa de renta para personas naturales residentes',
  'Base gravable en UVT y tarifa: 0 a 1.090 UVT = 0%. Mayor a 1.090 hasta 1.700: (base - 1.090) x 19%. Mayor a 1.700 hasta 4.100: (base - 1.700) x 28% + 116 UVT. Mayor a 4.100 hasta 8.670: (base - 4.100) x 33% + 788 UVT. Mayor a 8.670 hasta 18.970: (base - 8.670) x 35% + 2.296 UVT. Mayor a 18.970 hasta 31.000: (base - 18.970) x 37% + 5.901 UVT. Mayor a 31.000: (base - 31.000) x 39% + 10.352 UVT.', true);

add('Libro Primero - Renta', 'Art. 206 num. 10', 'Renta exenta del 25% de pagos laborales',
  'Renta exenta del 25% del valor total de los pagos laborales, calculada despues de restar ingresos no constitutivos de renta, deducciones y otras rentas exentas, con un tope anual de 790 UVT (Ley 2277 de 2022).', true);

add('Libro Primero - Renta', 'Art. 336', 'Limite a deducciones y rentas exentas (personas naturales)',
  'Las rentas exentas y deducciones imputables a la renta liquida cedular tienen como limite el 40% del resultado de restar los ingresos no constitutivos de renta, sin exceder 1.340 UVT anuales.', true);

add('Libro Primero - Renta', 'Art. 107', 'Deducciones: causalidad, necesidad y proporcionalidad',
  'Son deducibles las expensas realizadas durante el ano o periodo gravable en el desarrollo de cualquier actividad productora de renta, siempre que tengan relacion de causalidad con la actividad, sean necesarias y proporcionales con ella.');

add('Libro Primero - Renta', 'Art. 771-2', 'Facturacion como soporte de costos y deducciones',
  'Para la procedencia de costos y deducciones se requiere factura de venta o documento equivalente con el cumplimiento de los requisitos legales (NIT, discriminacion del IVA, etc.). Una factura electronica valida lleva CUFE.');

add('Libro Primero - Renta', 'Art. 615 y 617', 'Obligacion de facturar y requisitos de la factura',
  'Art. 615: los obligados deben expedir factura o documento equivalente. Art. 617: requisitos de la factura, entre ellos apellidos y nombre o razon social y NIT del vendedor, numeracion consecutiva, fecha de expedicion, descripcion, valor total y discriminacion del IVA.');

add('Libro Primero - Renta', 'Art. 616-1', 'Sistema de facturacion (incluida la factura electronica)',
  'Define el sistema de facturacion, que incluye la factura electronica de venta, y habilita a la DIAN a reglamentar sus requisitos, validacion previa y el CUFE como codigo unico de la factura.');

add('Libro Segundo - Retencion en la fuente', 'Art. 365 y 368', 'Retencion en la fuente: facultad y agentes de retencion',
  'Art. 365: el Gobierno puede establecer retenciones en la fuente para facilitar, acelerar y asegurar el recaudo. Art. 368: son agentes de retencion las entidades y personas que por sus funciones intervienen en actos u operaciones en los cuales deben efectuar la retencion.');

add('Libro Segundo - Retencion en la fuente', 'Art. 383', 'Tabla de retencion en la fuente por rentas de trabajo (en UVT)',
  'Base gravable en UVT y retencion: 0 a 95 UVT = 0%. Mayor a 95 hasta 150: (base - 95) x 19%. Mayor a 150 hasta 360: (base - 150) x 28% + 10 UVT. Mayor a 360 hasta 640: (base - 360) x 33% + 69 UVT. Mayor a 640 hasta 945: (base - 640) x 35% + 162 UVT. Mayor a 945 hasta 2.300: (base - 945) x 37% + 268 UVT. Mayor a 2.300: (base - 2.300) x 39% + 770 UVT. Para calcular use la herramienta calcular_uvt_y_retencion (comando art383:<base en UVT>).');

add('Libro Segundo - Retencion en la fuente', 'Art. 387', 'Deducciones para depurar la base de retencion laboral',
  'Se pueden restar de la base: intereses de vivienda hasta 100 UVT mensuales; pagos por salud prepagada y seguros de salud hasta 16 UVT mensuales; dependientes hasta el 10% de los ingresos brutos, maximo 32 UVT mensuales; ademas aportes obligatorios y rentas exentas dentro de los limites legales.', true);

add('Libro Segundo - Retencion en la fuente', 'DUR 1625/2016 (no es articulo del ET)', 'Retencion en la fuente: tarifas y bases minimas habituales (compras, servicios, honorarios)',
  'Valores operativos tomados del Decreto Unico Reglamentario 1625 de 2016, NO del ET, para orientar: compras generales 2,5% con base minima 27 UVT; servicios generales 4% (declarantes) o 6% (no declarantes) con base minima 4 UVT; honorarios y comisiones 11% (personas juridicas) y 10% o 11% segun la persona natural; arrendamiento de inmuebles 3,5% con base minima 27 UVT. Estas cifras cambian por decreto: VERIFICAR antes de usar con un cliente.', true);

add('Libro Tercero - IVA', 'Art. 420', 'Hecho generador del IVA',
  'El IVA se causa por la venta e importacion de bienes corporales muebles (salvo excluidos), la prestacion de servicios en el territorio nacional, la venta y operacion sobre juegos de suerte y azar, entre otros.');

add('Libro Tercero - IVA', 'Art. 468', 'Tarifa general del IVA',
  'La tarifa general del impuesto sobre las ventas es del 19%.');

add('Libro Tercero - IVA', 'Art. 477', 'Bienes con tarifa del 5%',
  'Ciertos bienes listados en el articulo tienen tarifa diferencial del 5% del IVA. Consultar el listado vigente por posicion arancelaria antes de aplicarla.', true);

add('Libro Tercero - IVA', 'Art. 437 par. 3', 'Responsables y no responsables del IVA',
  'Las personas naturales comerciantes y quienes prestan servicios pueden ser no responsables del IVA si cumplen, entre otras condiciones, que sus ingresos brutos totales del ano anterior y del actual sean inferiores a 3.500 UVT, que tengan un solo establecimiento de comercio y que no sean usuarios aduaneros.', true);

add('Libro Tercero - IVA', 'Art. 437-1', 'Retencion en la fuente a titulo de IVA',
  'La retencion de IVA corresponde, como regla general, al 15% del valor del impuesto, practicada por los agentes de retencion designados por el ET. Confirmar el porcentaje y los casos especiales.', true);

add('Libro Tercero - IVA', 'Art. 485 y 488', 'Impuestos descontables y sus requisitos',
  'Da derecho a descuento el IVA por bienes y servicios que se destinen a operaciones gravadas y que sean computables como costo o gasto; se exige soporte en factura que cumpla los requisitos legales.', true);

add('Libro Sexto - GMF', 'Art. 871 y 872', 'Gravamen a los Movimientos Financieros (GMF, 4 x 1000)',
  'El GMF se causa por la disposicion de recursos en cuentas corrientes, de ahorros y depositos. La tarifa es del 4 por mil (0,4%). Existen exenciones, por ejemplo el retiro de una cuenta de ahorros de un titular hasta un limite mensual en UVT (VERIFICAR el limite vigente).', true);

add('Libro Primero - Renta', 'Art. 115 (GMF)', 'Deduccion del GMF',
  'El 50% del GMF efectivamente pagado en el ano es deducible, siempre que este debidamente certificado por el agente retenedor y sin importar la relacion de causalidad con la actividad.', true);

add('Libro Quinto - Procedimiento / Informacion', 'Art. 631', 'Informacion exogena (medios magneticos)',
  'La DIAN puede solicitar anualmente a contribuyentes y terceros informacion para estudios, cruces y control. Quienes estan obligados, los topes en pesos/UVT, los formatos y los plazos se fijan cada ano por resolucion de la DIAN: VERIFICAR la resolucion vigente del ano gravable.', true);

add('Libro Quinto - Procedimiento / Sanciones', 'Art. 651', 'Sancion por no enviar informacion o enviarla con errores',
  'Quien no suministre la informacion exigida (por ejemplo la exogena) dentro del plazo, o la presente con errores o de forma que no se pueda procesar, se expone a una sancion calculada como porcentaje de los valores no reportados o inexactos, con un tope maximo en UVT. VERIFICAR porcentajes y tope vigentes.', true);

add('Libro Quinto - Procedimiento / Sanciones', 'Art. 641', 'Sancion por extemporaneidad en la presentacion',
  'La declaracion presentada despues del plazo genera una sancion del 5% del impuesto a cargo por cada mes o fraccion de mes de retraso, sujeta a topes y a una sancion minima en UVT. VERIFICAR topes y sancion minima vigentes.', true);

add('Libro Quinto - Procedimiento / Declaracion', 'Art. 592 y 594-3', 'Personas naturales obligadas a declarar renta',
  'No estan obligadas a declarar las personas naturales que no superen ciertos topes de patrimonio bruto, ingresos brutos, consumos con tarjeta de credito, compras y consignaciones, expresados en UVT (los topes habituales: patrimonio bruto a 31 de diciembre de 4.500 UVT; ingresos brutos, consumos, compras y consignaciones de 1.400 UVT cada uno). VERIFICAR contra el calendario y reglas del ano gravable.', true);

return A.map((a) => ({ json: a }));
