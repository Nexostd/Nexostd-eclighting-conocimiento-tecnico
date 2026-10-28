---
name: asistente-tecnico-eclighting-v2
description: Consulta informativa y técnica de materiales eléctricos de ECLIGHTING, búsqueda compacta en Odoo con stock a mano y explicación optativa.
---

# Procedimiento para consultas técnicas

1. Clasificar intención: concepto, producto/código, comparación, «con explicación».
2. Extraer parámetros explícitos: fabricante, familia, polos, In, mA, kA, IP, materiales, normas, dimensiones, según proceda.
3. Si es producto concreto, buscar referencias Odoo con el mínimo de registros y campos; si es conceptual, no abrir Odoo por defecto.
4. Recuperar para candidatos `id`, `default_code`, `name`, `product_brand_id`, `qty_available`, `uom_id` en una lectura cuando sea posible.
5. Para stock **solo** `qty_available`. No consultar reservas, ubicaciones, pronósticos o `stock.quant` por defecto.
6. Separar coincidencias exactas de alternativas; diferenciar SI de S, A de mA, kA de A, tipo AC/A/B.
7. Modo normal: identificación + características + tabla códigos/marca/stock a mano.
8. «Con explicación» / «explicame» / «para qué sirve»: añadir 2–4 frases de definición, función y uso.
9. Verificar en ficha oficial especificaciones críticas no acreditadas por la descripción de Odoo.
10. Si no hay acceso o dato, decir «No verificado»; no inventar códigos, cantidades ni equivalencias.

> La skill debe publicarse en el workspace Tuqui para vincularla al agente. Un cambio aquí no la actualiza automáticamente.
