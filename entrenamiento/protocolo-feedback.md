# Del feedback a una lección

## Capturar
- Consulta original (anonimizada).
- Respuesta observada (resumen).
- Corrección que aporta el empleado.
- Tipo: formato / procedimiento / dato técnico / código de catálogo.
- Fuente o evidencia.
- Estado de revisión.
- Qué debería hacer diferente el asistente.
- Pregunta de prueba que impediría repetir el error.

## Aprobar
- Formato/preferencia: basta la instrucción del responsable del asistente.
- Técnico/normativo/seguridad: exige documentación de fabricante, norma aplicable o revisión técnica responsable.
- Código de Odoo: verificación con catálogo actual. No guardar stock como valor estable.
- No difundir datos confidenciales ni de terceros.

## Publicar
Redactar ficha o regla en una rama de GitHub, agregar una prueba, abrir pull request, aprobar y fusionar. Actualizar la configuración de ChatGPT/Tuqui por una vía comprobada. **La fusión del PR no equivale a una actualización automática del agente.**

## Ejemplo 1: INS Schneider 630 A
Error: responder con MCCB NS630 ante la búsqueda de INS630.
Corrección: distinguir interruptor-seccionador INS de interruptor automático NS/NSX. Buscar por referencia real y no sustituir familias sin advertir.

## Ejemplo 2: stock
Preferencia: mostrar solo stock a mano `qty_available`, no stock reservado o pronosticado. Evitar llamadas de inventario adicionales por defecto.

## Ejemplo 3: explicación
Preferencia: solo explicar qué es y para qué se usa si el usuario escribe «con explicación» o equivalente.
