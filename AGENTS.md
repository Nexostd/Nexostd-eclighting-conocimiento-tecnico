# Guía para asistentes de IA y Codex

Objetivo: mejorar de manera incremental el conocimiento técnico de ECLIGHTING, sin inventar códigos ni convertir ejemplos históricos en datos actuales.

Antes de cambiar una regla, revisar `agente/INSTRUCCIONES_TUQUI.md` y `aprendizajes/registro.md`.

Cada corrección sobre una característica técnica debe identificar fuente (ficha de fabricante, norma o revisión responsable). No reemplazar una indicación del cliente con una equivalencia no verificada.

El asistente tiene modo normal (códigos y `qty_available`) y «con explicación» (añade para qué sirve). En consultas de disponibilidad muestra también reservado (`qty_available` − `free_qty`), libre (`free_qty`) y entrante (`incoming_qty`). El stock a mano puede estar reservado; para prometer disponibilidad se usa el libre. Nunca precios ni costos.

No subir credenciales, datos personales, ofertas de clientes, listados sensibles ni stock vivo. No hacer cambios sobre Odoo desde este repositorio.
