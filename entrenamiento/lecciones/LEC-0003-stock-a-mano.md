# LEC-0003 — Stock a mano solamente

**Tipo:** procedimiento / eficiencia.
**Estado:** aprobada como preferencia de consulta.

## Enseñanza
Mostrar solo `qty_available` («Stock a mano»), junto a código, marca, características y unidad. No consultar automáticamente `free_qty`, `virtual_available`, `stock.quant`, ubicaciones ni reservas. Si es viable, recuperar en la misma lectura de `product.product` todos los campos necesarios.

## Aclaración fundamental
El stock físico a mano **puede estar reservado**. Nunca presentarlo como «disponible para la venta» sin un análisis adicional expresamente solicitado. Si falla el ERP, mostrar «No verificado», no cero.

## Prueba
- Una consulta de productos muestra la columna «Stock a mano».
- No asegura disponibilidad comercial libre de reservas.
