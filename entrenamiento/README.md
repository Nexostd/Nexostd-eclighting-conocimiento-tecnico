# Entrenamiento supervisado ECLIGHTING

Este repositorio no modifica los pesos de GPT. Es una **base de conocimiento y comportamiento versionada**, consultable desde ChatGPT (conector GitHub) y reutilizable en Tuqui mediante publicación de instrucciones, skills y contexto.

## Cuatro tipos de aprendizaje

1. **Regla de respuesta:** por ejemplo, «con explicación» opcional, tabla breve, lenguaje argentino, ahorro de consultas.
2. **Conocimiento técnico:** qué es un dispositivo, para qué sirve, parámetros, diferencias, normas, compatibilidad. Necesita fuente oficial o aprobación técnica para considerarse validado.
3. **Lenguaje interno:** abreviaturas, denominaciones y forma de buscar en Odoo. Verificar nombres de marca/familia y códigos del ERP.
4. **Corrección:** guardar la pregunta, el error, la respuesta correcta y una prueba de regresión.

## Flujo

Consulta real → respuesta → corrección del equipo → propuesta de aprendizaje → verificación → caso de prueba → revisión de GitHub → aprobación → publicación en las instrucciones/skill/contexto de ChatGPT y Tuqui.

## Comandos conversacionales

- «**Aprendé esto:** …» → redactar y clasificar una lección.
- «**Guardá esta corrección**» → registrar el aprendizaje versionado en GitHub, si los permisos lo permiten.
- «**Validá este dato**» → comprobar en fuente oficial y anotar evidencia.
- «**Con explicación**» → definición, función y aplicación en 2–4 oraciones.
- «**Buscá códigos**» → consultar Odoo en vivo y devolver código, características, marca y `qty_available`.

## Niveles de confianza

- `propuesta`: enseñanza no revisada; no afirmar como hecho técnico.
- `verificada`: confirmada con ficha oficial, norma aplicable o ERP.
- `aprobada`: validada por el responsable técnico o de negocio que corresponda.
- `obsoleta`: reemplazada por una especificación nueva.

## Privacidad y datos dinámicos

No publicar información de clientes, presupuestos confidenciales, contactos, credenciales, capturas privadas, precios negociados ni existencias históricas como stock vigente. Un repo privado tampoco debe usarse como almacén irrestricto de información empresarial.

**Importante:** una actualización en GitHub no reconfigura automáticamente Tuqui ni ChatGPT. El sistema debe recuperar los archivos al responder y publicar los cambios aprobados mediante un proceso explícito.
