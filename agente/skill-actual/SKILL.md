---
name: asistente-tecnico-eclighting-v2
description: Consulta informativa y técnica de materiales eléctricos de ECLIGHTING, búsqueda compacta en Odoo con stock (a mano, libre, reservado, entrante) y explicación optativa.
---

# Procedimiento para consultas técnicas

1. Clasificar intención: concepto, producto/código, comparación, «con explicación».
2. Extraer parámetros explícitos: fabricante, familia, polos, In, mA, kA, IP, materiales, normas, dimensiones, según proceda.
3. Si es producto concreto, buscar referencias Odoo con el mínimo de registros y campos; si es conceptual, no abrir Odoo por defecto.
4. Recuperar para candidatos `id`, `default_code`, `name`, `product_brand_id`, `qty_available`, `uom_id` en una lectura cuando sea posible.
5. Stock: consulta técnica → solo `qty_available`. Consulta de disponibilidad o lista de materiales → sumar `free_qty`, `incoming_qty` y `virtual_available` en la misma lectura; Reservado = `qty_available` − `free_qty`. Comparar el pedido contra Libre. No consultar ubicaciones, `stock.quant`, precios ni costos.
6. Separar coincidencias exactas de alternativas; diferenciar SI de S, A de mA, kA de A, tipo AC/A/B.
7. Modo normal: identificación + características + tabla códigos/marca/stock a mano.
8. «Con explicación» / «explicame» / «para qué sirve»: añadir 2–4 frases de definición, función y uso.
9. Verificar en ficha oficial especificaciones críticas no acreditadas por la descripción de Odoo.
10. Si no hay acceso o dato, decir «No verificado»; no inventar códigos, cantidades ni equivalencias.
11. Si es una lista de materiales: separar lo explícito, lo supuesto y lo faltante; un producto por ítem agrupado por rubro; verificar unidad de venta y convertir pulgadas a mm aclarándolo; cerrar con «Para confirmar con el cliente». No completar requisitos por costumbre.
12. Si compara materiales: tabla Requisito | Pedido | Candidato; un atributo crítico distinto = No compatible. Coincidir en amperaje, polos, medida o marca no prueba equivalencia.
13. Asignar estado de validación a cada producto propuesto: Confirmado, Condicional, Alternativa, No verificado o No compatible.
14. Si es auditoría de cotización: comparar contra el pedido original y clasificar observaciones en Crítico, Revisar o Validado.

## Distinciones que no se deben mezclar
Corriente nominal y poder de corte; Icu e Ics; corriente nominal y regulación (Ir); sensibilidad (mA) y corriente nominal (A); AC-1 y AC-3; protección por sobrecorriente y protección diferencial; clase A/AC/B, selectividad S y superinmunidad SI; XLPE y LS0H/LSZH; resistente al fuego y baja emisión de humos; IP e IK; diámetro nominal y diámetro exterior; sección (mm²) y diámetro (mm); polos y módulos; medidas exteriores y útiles; corriente alterna y continua.

> La skill debe publicarse en el workspace Tuqui para vincularla al agente. Un cambio aquí no la actualiza automáticamente.
