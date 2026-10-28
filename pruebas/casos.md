# Casos iniciales de prueba

## C01: INS Schneider 630 A
- Consulta: «INS de Schneider de 630 A».
- Debe reconocer que INS es una gama de interruptores-seccionadores y evitar asumir que son MCCB NS/NSX.
- Mostrar referencias reales de la gama solicitada (cuando existan en Odoo), variante, características y stock a mano. Si no hay coincidencias, decirlo.

## C02: INS con explicación
- Consulta: «INS de Schneider de 630 A con explicación».
- Incluir descripción en 2–4 oraciones sobre interruptor-seccionador y aplicaciones, más las referencias.

## C03: Schneider diferencial superinmunizado
- Consulta: «Disyuntores superinmunizados Schneider bipolares».
- Mostrar el tipo de producto, la marca, SI, polos y catálogo; no preguntar amperaje antes de presentar variantes.

## C04: 300 mA selectivo
- Consulta: «Diferenciales Schneider 2P 300mA selectivos».
- Identificar sensibilidad, selectividad, tipo A/AC y SI como atributos distintos.

## C05: Stock
- Ante un producto concreto, mostrar **stock a mano** `qty_available` junto a la unidad; no indicar libre de reservas.

## C06: Consulta conceptual
- «¿Qué diferencia hay entre kA y A?» — responder conceptualmente sin consultar todo Odoo.

## C07: Abreviaturas
- Aceptar «termica 2x20 sch», «disy SI», «morsetos PAT» sin exigir redacción perfecta.

## C08: Datos faltantes
- «Gabinete Schneider metálico» — señalar medidas, IP, placa, montaje, contrafrente cuando proceda.

## C09: Norma
- «¿IRAM 2178-1 significa XLPE?» — diferenciar designación de norma del material de aislación; verificar alcance.

## C10: Sin coincidencia
- Si Odoo no tiene coincidencias fiables, explicar qué se buscó, no crear código ficticio.

## C11: Lista de materiales de obra
- Consulta: pedido completo con cajas (5x10, octogonales, 5x5, 10x10), caño rígido PVC 3/4", corrugado 3/4" y 1" en rollos, conectores, grampas, curvas, uniones, tarugos, tornillos, cable unipolar 1,5 y 2,5 por colores, y tablero ABB (disyuntores 25 A, térmicas 16 A y 10 A).
- Debe proponer un producto por ítem, agrupado por rubro, priorizando el mismo sistema para cajas, caños y accesorios.
- Debe convertir pulgadas a mm y aclararlo; verificar unidad de venta (metro, barra, rollo, estuche); marcar ⚠️ cuando el stock a mano no alcanza.
- Debe cerrar con «Para confirmar con el cliente» (clase de caño, octogonal chica o grande, polos, clase del diferencial, medida de tornillos).
- Resultado 2026-10-28: correcto con v2.

## C12: Abreviaturas cortas
- Consulta: «disyuntor super inmunizado schneider».
- Debe encontrar SI, A-SI y A-SUP INMU sin traer ruido de palabras como SIMPLE o SIN (combinar la abreviatura con DIF/IID o con la marca en el código).
- Resultado 2026-10-28: correcto tras agregar la regla de abreviaturas cortas.

## Banco de pruebas objetivo (30 casos)
Distribución: interpretación de pedidos 8 · identificación de códigos 8 · equivalencias 6 · consultas a Odoo 4 · auditoría de cotizaciones 4.
En cada prueba registrar: resultado esperado, producto identificado, fuentes usadas, errores técnicos y consultas innecesarias. Preferir pedidos reales ya cotizados (anonimizados).

## C13: Caja moldeada con datos faltantes
- Consulta: «Interruptor caja moldeada Schneider 4x160A 36kA».
- Debe identificar familia MCCB, 4 polos, 160 A, 36 kA; estado **Condicional**: faltan tensión y unidad de disparo. No inventar código.

## C14: Equivalencia que no cumple
- Consulta: pedido de diferencial 4x40 A 300 mA clase A selectivo; candidato 4x40 A 30 mA clase AC no selectivo.
- Debe mostrar tabla Requisito | Pedido | Candidato y concluir **No compatible**, aunque coincidan polos y amperaje.

## C15: Gabinete con accesorios
- Consulta: «Gabinete metálico IP65 1000×800×300 con placa de montaje, contrafrente ciego abisagrado y zócalo».
- Debe separar atributos, buscar primero el gabinete y luego indicar si placa, contrafrente y zócalo vienen incluidos o llevan código aparte.

## C16: Seccionador portafusibles
- Consulta: «Seccionadora NH3 630 A».
- Debe distinguir tamaño de fusible (NH3) de corriente (630 A), preguntar polos y si es bajo carga, y no confundir con seccionador sin fusibles.

## C17: Auditoría de cotización
- Consulta: revisar una cotización contra el pedido del cliente.
- Debe clasificar observaciones en Crítico / Revisar / Validado. Si no tiene el pedido original, debe decir que no puede confirmar la coincidencia completa.

## C18: Stock libre
- Consulta: «¿Cuánto unipolar 2,5 rojo Trefi tengo libre? Necesito 200 m».
- Debe leer en una sola consulta `qty_available`, `free_qty`, `incoming_qty` y `virtual_available`, mostrar A mano / Reservado / Libre / Entrante por artículo y comparar los 200 m contra **Libre**.
- No debe sumar colores distintos ni mostrar precios. Si la unidad de Odoo no coincide con metros, aclararlo.
