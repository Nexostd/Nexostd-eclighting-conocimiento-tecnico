# Flujo de aprendizaje técnico a partir de cotizaciones

**Estado:** procedimiento inicial · 2026-10-28
**Objetivo:** transformar pedidos reales y cotizaciones respondidas en conocimiento técnico verificable, sin precios ni datos de clientes.

## 0. Qué aprende y qué no
El modelo no se reentrena automáticamente. Los casos revisados generan **fichas, reglas, glosario y pruebas** que se guardan en GitHub, y pueden incorporarse al contexto/skill/instrucciones del agente Tuqui en una actualización separada. **Subir una cotización no cambia por sí solo el asistente.**

## 1. Selección — menos carga, mayor valor
En lugar de procesar todas las cotizaciones, elegir inicialmente **3 a 5 casos por semana**, priorizando:
- Material nuevo o descripción difícil.
- Equivalencia o sustitución técnica que hubo que analizar.
- Error o corrección de interpretación detectados.
- Abreviatura de cliente que cuesta interpretar.
- Familia consultada con frecuencia.
- Caso que revela una regla generalizable.

Descartar tareas triviales repetidas, casos sin información suficiente y pedidos cuya documentación no se pueda compartir sin comprometer la confidencialidad.

## 2. Captura mínima — 2 minutos por caso
Crear un caso usando `plantillas/caso-de-cotizacion.md` o el Issue de GitHub:
- Texto del pedido **desidentificado**.
- Respuesta cotizada: código interno, fabricante, modelo y características; **sin precios**.
- Motivo técnico de la elección (si se conoce).
- Dudas o equivalencias pendientes.
- Fuente oficial disponible, si existe.
No copiar en GitHub el correo o PDF original sin desidentificar.

## 3. Limpieza de datos y seguridad
Antes de enviar: quitar **precios, costos, descuentos, márgenes, CUIT, nombres de clientes/personas, email, teléfono, domicilios, obras identificables, cuentas, notas privadas, links internos de oportunidad y condiciones comerciales**. Revisar también metadatos, encabezados, pies y hojas ocultas de Excel.
Preservar únicamente cantidades del pedido que aporten contexto técnico (nunca confundirlas con stock actual).

## 4. Extracción del asistente
Por cada caso, separar:
1. **Lo solicitado:** texto/atributos explícitos.
2. **Lo cotizado:** código Odoo + referencia de fabricante + descripción.
3. **La interpretación:** qué datos inferimos y cuáles faltaban.
4. **La decisión:** por qué se eligió esa referencia.
5. **La evidencia:** fabricante, norma o confirmación responsable.
6. **El aprendizaje generalizable:** sin nombrar cliente, proyecto ni precio.
7. **La prueba:** pregunta similar con respuesta esperada.

## 5. Revisión técnica — controles
Etiquetas:
- **Verificado:** propiedades confirmadas en ficha vigente o por revisión técnica responsable con evidencia documentada.
- **En revisión:** hipótesis, correspondencia probable o dato no comprobado.
- **Rechazado:** error técnico o equivalencia no válida.

**Una cotización enviada NO prueba por sí sola que el producto sea equivalente o cumpla el pliego.** No publicar una regla técnica de seguridad ni una equivalencia como verificada sin soporte.

## 6. Publicación controlada
- Primero registrar el caso desidentificado en `casos/pendientes/` o como Issue privado.
- Una vez validado, actualizar uno o varios destinos:
  - `conocimiento/`: ficha de producto, diferencia técnica o criterio.
  - `catalogo/`: mapeo de descripción–código, señalando fecha/fuente.
  - `agente/`: regla sobre cómo responder o buscar.
  - `pruebas/`: consulta y resultado esperado.
  - `aprendizajes/`: decisión y razón del cambio.
- Usar una pull request para cambios relevantes y pedir aprobación técnica.
- No guardar stock fijo: Odoo lo calcula en vivo.

## 7. Incorporación a Tuqui
Tras aprobar el cambio, revisar si corresponde:
- Actualizar manualmente las instrucciones del agente.
- Publicar/actualizar una skill del workspace.
- Cargar documentación como contexto del agente o base de conocimiento.

**La conexión GitHub de ChatGPT no equivale a sincronización automática GitHub → Tuqui.**
El stock que muestra el agente, cuando se pide un producto, es **solo `qty_available`**. Las preguntas «con explicación» activan una explicación breve opcional.

## 8. Pruebas
Probar al menos:
- Consulta normal y «con explicación».
- Un caso con abreviatura real.
- Un caso de atributo especial (SI, S, A/AC, kA, IRAM, etc.).
- Un caso sin coincidencia.
- Códigos reales sin invenciones.
- Stock **a mano** únicamente, sin decir libre de reservas.

## 9. Rutina propuesta
- Durante el día: marcar casos que realmente aporten algo nuevo; no interrumpir toda la cotización para documentar.
- Dos momentos por semana o una revisión semanal de **20–30 minutos**: seleccionar 3–5 casos y enviarlos desidentificados.
- Área técnica: validar los aprendizajes que afectan prestaciones, normas y equivalencias.
- Una vez aprobados: registrar versión, aplicar a Tuqui cuando corresponda y repetir pruebas.

## 10. Indicadores
Medir mensualmente, con un conjunto fijo de 10–20 consultas:
- % de identificaciones correctas.
- % de códigos verificados.
- % de respuestas que inventan características (meta: 0).
- % de casos resueltos sin repreguntas innecesarias.
- % de respuestas «con explicación» que realmente explican el uso.
- Cantidad de aprendizajes **aprobados**, no solo recibidos.

## Flujo operativo simplificado
`Pedido + cotización desidentificados` → `Extracción` → `Revisión` → `Ficha/regla/prueba` → `GitHub` → `Actualización de Tuqui` → `Evaluación`.

## Responsabilidades
- **Comercial:** marcar caso, borrar datos privados y contar por qué cotizó.
- **Asistente:** estructurar, comparar, detectar dudas, proponer cambios y pruebas.
- **Responsable técnico:** aprobar o corregir interpretación, norma o equivalencia.
- **Administrador Tuqui:** aplicar las versiones aprobadas al agente y verificar su funcionamiento.
