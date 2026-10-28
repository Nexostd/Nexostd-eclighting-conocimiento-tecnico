# Aprendizajes y decisiones del proyecto

**2026-10-28 — Cambio de enfoque:** el buscador estático basado en fichas y filtros no satisface la necesidad. El producto principal es un **asistente técnico conversacional**.

**2026-10-28 — Uso principal:** explicar, identificar, comparar e interpretar materiales eléctricos con contexto de comercialización en Argentina.

**2026-10-28 — Ejecución inicial:** agente nativo de Tuqui, con sus instrucciones, skill y contexto técnico opcional. El intérprete de cotizaciones e historial de clientes queda como proyecto distinto.

**2026-10-28 — Códigos reales:** cuando una consulta menciona marca o material concreto, buscar proactivamente en Odoo, no pedir que el usuario solicite códigos de forma separada.

**2026-10-28 — Formato:** identificación y atributos claros, breve diferenciación, tabla de modelos de Odoo y stock.

**2026-10-28 — «Con explicación»:** la explicación de qué es/para qué se usa debe ser **opcional y activada por frase explícita**, no obligatoria en todos los resultados.

**2026-10-28 — Eficiencia:** consultar exclusivamente stock **a mano** (`qty_available`) y recuperar sus valores junto con los demás campos en la menor cantidad de lecturas posible; no reservar o cruzar movimientos automáticamente.

**2026-10-28 — Cautela:** stock a mano no es necesariamente libre para venta. No prometer entrega basada únicamente en ese campo.

**2026-10-28 — Calidad:** marcas, modelos y prestaciones no se deben inferir únicamente de una descripción abreviada de Odoo. Para atributos críticos, consultar documentación técnica oficial.

**2026-10-28 — Ejemplo didáctico:** diferencias entre selectividad S y superinmunidad SI en diferenciales Schneider. La clase A/AC/B es otra propiedad independiente.

**2026-10-28 — Gestión del conocimiento:** GitHub privado almacena reglas, fichas, evidencia y correcciones validadas. Odoo mantiene códigos/stock actuales. El temario formativo permanece como borrador hasta revisión del área técnica.

**2026-10-28 — Abreviaturas cortas:** SI, S o A sueltas traen ruido en la búsqueda (SIMPLE, SIN). Combinarlas con otra palabra clave del producto o con la marca en el código.

**2026-10-28 — Pulgadas y milímetros:** los pedidos suelen venir en pulgadas y los productos PVC figuran en mm. Aplicar la equivalencia comercial y aclararla; pendiente de validación técnica.

**2026-10-28 — Unidad de venta:** el cliente pide en barras, rollos o unidades; Odoo puede manejar metros o estuches. Verificar y avisar la diferencia.

**2026-10-28 — Listas de materiales:** responder por rubro en tablas, priorizar accesorios del mismo sistema, marcar ⚠️ cuando el stock a mano no alcanza y cerrar con lo que hay que confirmar con el cliente.

**2026-10-28 — Odoo solo lectura:** el asistente nunca modifica registros de Odoo, tampoco para corregir datos que detecte.

**2026-10-28 — Pendiente:** definir cómo mostrar los productos con sufijo `/BORRAR` en el código.

**2026-10-28 — Temario como base de conocimiento:** el Temario Técnico v1.0 (73 preguntas) y el Complemento v1.1 (26 preguntas, incluye módulo de Iluminación) quedan en `conocimiento/temario/`, un archivo por módulo, con palabras clave de mostrador por entrada. Estado: borrador hasta revisión del área técnica.

**2026-10-28 — Instrucciones v3:** se incorporan estados de validación (Confirmado, Condicional, Alternativa, No verificado, No compatible), tabla de equivalencias atributo por atributo, auditoría de cotizaciones (Crítico, Revisar, Validado), separación del pedido en atributos y más distinciones técnicas. Se crean `equivalencias-aprobadas.md` y `referencias-validadas.md`.

**2026-10-28 — Alcance de gestión pendiente:** se mantiene solo stock a mano, sin precios ni costos, hasta que se decida si se amplía a reservado, libre, entrante y proveedores.

**2026-10-28 — Alcance de gestión (opción 2):** además del stock a mano, en consultas de disponibilidad el asistente muestra reservado (`qty_available` − `free_qty`), libre (`free_qty`), entrante (`incoming_qty`) y previsto (`virtual_available`). Precios, costos y proveedores quedan fuera. Campos verificados en Odoo el 2026-10-28.

**2026-10-28 — Unidad de medida en Odoo:** hay cables cargados con unidad «Unidades» aunque el stock se lleva en metros. El asistente no debe asumir la unidad por el campo `uom_id`.
