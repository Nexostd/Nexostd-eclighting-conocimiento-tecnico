# Temario técnico ECLIGHTING – base de conocimiento

Base de preguntas y respuestas técnicas para el asistente técnico y para capacitar a la oficina.
Origen: Temario Técnico v1.0 (73 preguntas, 2026-10-27) + Complemento v1.1 (26 preguntas, 2026-10-28) + Módulo 09 de reglas de cotización del equipo (2026-10-28).
El Módulo 09 no son preguntas: son reglas del equipo que el asistente aplica siempre que la consulta encaje.

**Estado:** BORRADOR pendiente de revisión del área técnica. Ante un dato crítico de seguridad, mandan la ficha del fabricante y el pliego del cliente.

## Módulos

| Archivo | Módulo | Códigos |
|---|---|---|
| `01-fundamentos.md` | Fundamentos eléctricos | F01–F08 |
| `02-protecciones-maniobra.md` | Protecciones, maniobra y control | P01–P17 |
| `03-tableros-accesorios.md` | Tableros y accesorios | T01–T14 |
| `04-canalizaciones.md` | Canalizaciones eléctricas | C01–C15 |
| `05-cables.md` | Cables y conductores | K01–K14 |
| `06-puesta-a-tierra-conexionado.md` | Puesta a tierra y conexionado | PT01–PT10 |
| `07-interpretacion-cotizaciones.md` | Interpretación de cotizaciones | Q01–Q08 + checklist |
| `08-iluminacion.md` | Iluminación | L01–L13 |
| `09-reglas-de-cotizacion.md` | Reglas de cotización ECLIGHTING (cómo interpretamos y qué necesitamos) | I01–I04, jerga, FA01–FA03, datos por familia |

## Formato de cada entrada

```
### CÓDIGO · Pregunta
Respuesta.
- **Para cotizar:** datos que hay que pedir.
- **Palabras clave:** cómo lo pide el mostrador (jerga, abreviaturas, sinónimos).
```

- Cada entrada se entiende sola: el asistente puede recuperar una sin leer el resto del módulo.
- Las **palabras clave** sirven para que la búsqueda encuentre la entrada aunque la consulta venga con jerga.
- Para agregar una pregunta: siguiente código libre del módulo, mismo formato, y anotarla en `aprendizajes/registro.md`.
- Una entrada validada por el área técnica se marca agregando `- **Validado:** nombre, fecha` al final.
- No incluir precios, stock ni datos de clientes.
