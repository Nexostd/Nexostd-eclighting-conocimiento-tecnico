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
