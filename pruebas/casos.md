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
