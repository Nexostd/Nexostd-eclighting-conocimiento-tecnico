# Interpretación de pedidos técnicos

## Método
1. Leer el pedido literalmente e identificar producto/familia.
2. Separar condiciones obligatorias de preferencias, marcas de referencia y datos faltantes.
3. Interpretar abreviaturas y medidas sin inventar especificaciones.
4. Localizar candidatos del fabricante o de Odoo.
5. Confirmar los atributos críticos contra documentación técnica.
6. Identificar alternativas y equivalencias solo si cumplen todas las exigencias relevantes.

## Ejemplo: «INT. DIF. SCHNEIDER 2P 300MA SI SELECTIVO»
- Familia: interruptor diferencial RCCB.
- Fabricante: Schneider Electric.
- Polos: 2.
- Sensibilidad: 300 mA.
- SI: inmunidad mejorada a perturbaciones.
- S: selectividad temporal.
- Falta: corriente nominal; mostrar varias corrientes presentes en catálogo sin interrumpir consulta.

## Ejemplo: «Bandeja escalera cincada en caliente»
No sustituir por bandeja perforada cincada electrolíticamente; verificar espesor, ancho, altura de ala, tratamiento, longitud y accesorios.

## Jerga del mostrador → nombre técnico
Estado: BORRADOR, pendiente de validación técnica.

| Cómo lo pide el cliente | Producto | Cómo puede figurar en Odoo |
|---|---|---|
| disyuntor / diyuntor / disyuntor diferencial | Interruptor diferencial (RCCB) | INT. DIFERENCIAL, INT.DIF, IID, ID, F202/F204 (ABB), Vigi (bloque acoplable) |
| térmica / llave térmica | Interruptor termomagnético (MCB) | INT. TERMOMAGNETICO, TERMOMAGNETICA, SH201/SH202 (ABB) |
| superinmunizado / super inmunizado | Diferencial de inmunidad reforzada | SI, A-SI, A-SUP INMU; en ABB aparece AP-R (verificar en ficha) |
| selectivo | Diferencial con retardo, va aguas arriba | S, SELEC, SELECTI |
| caja 5x10 | Caja rectangular de embutir | RECTANGULAR |
| caja 5x5 | Caja mignon | MIGNON |
| caño corrugado | Tubo corrugado en rollo | TUBO CORRUGADO |
| caño rígido PVC | Tubo rígido | TUBO RÍGIDO |
| tarugo / taco | Taco de expansión | TARUGO, TACO, S6 / S8 / S10 |
| unipolar 2,5 | Cable unipolar 1x2,5 mm² | CABLE UNIP. 1X2.50 |

## Medidas en pulgadas → milímetros (caños y accesorios PVC)
Estado: equivalencia de uso comercial, **no verificada en ficha**. Aplicarla y aclararla para que se confirme con el cliente.

| Pulgadas | Milímetros |
|---|---|
| 5/8" | 16 mm |
| 3/4" | 20 mm |
| 7/8" | 22 mm |
| 1" | 25 mm |
| 1 1/4" | 32 mm |
| 1 1/2" | 40 mm |
| 2" | 50 mm |

## Unidad de venta
- Caño rígido PVC: puede venderse por metro. «X caños» del cliente suele significar barras; confirmar el largo de la barra.
- Caño corrugado: rollos de 25 m o 50 m según el código; el stock puede estar expresado en metros.
- Cable: stock en metros.
- Tarugos y tornillos: por estuche o caja; verificar cantidad por envase.

## Datos que suelen faltar en una lista de materiales
- Diferencial: polos (2P/4P), sensibilidad (30/300 mA), clase (AC / A / B) y si es SI o selectivo.
- Termomagnética: polos (1P/2P/3P/4P), curva (B/C/D), poder de corte (kA).
- Caja octogonal: chica o grande.
- Caño rígido y corrugado: clase mecánica según dónde se instala (pared, losa, contrapiso).
- Tornillos: diámetro y largo.
- Cable: si el cliente exige norma o aislación LS0H.
- Proporción de diferenciales y termomagnéticas: si es poco habitual, preguntar el esquema del tablero.

## Advertencias de interpretación
- «Semipesado» es una denominación de caño de acero. Si el cliente pide PVC, elegir la clase del fabricante; el significado de las clases SD / ED / HD / HDX de Genrod está **pendiente de verificar en ficha**.
- Un diferencial clase B no equivale a uno SI ni a uno clase A común.
- Priorizar que cajas, caños y accesorios sean del mismo sistema.

## Ejemplo: lista de materiales de obra (caso C11)
Pedido con cajas, caños PVC en pulgadas, corrugado en rollos, accesorios, fijación, cable unipolar y tablero ABB.
- Explícito: cantidades, medidas en pulgadas, PVC, colores y secciones de cable, marca ABB, amperajes.
- Supuesto: 3/4" = 20 mm y 1" = 25 mm; cajas PVC del mismo sistema; diferencial 2P 30 mA.
- Faltante: clase de caño y corrugado, octogonal chica o grande, polos de térmicas, clase del diferencial, medida de tornillos, largo de barra.
