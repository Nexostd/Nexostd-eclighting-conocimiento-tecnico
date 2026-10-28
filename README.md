# ECLIGHTING · Conocimiento técnico

Repositorio privado de conocimiento técnico, reglas del Asistente Técnico Informativo y aprendizajes del equipo de ECLIGHTING / Electricidad Canning.

> **Estado:** borrador de trabajo. Las fichas y el temario requieren validación del área técnica. GitHub conserva instrucciones y conocimiento; Odoo permanece como fuente de códigos y stock en vivo.

## Objetivo
Transformar preguntas, errores, aclaraciones y aprendizajes del trabajo diario en documentación verificable, revisable y reutilizable por el equipo.

## Reglas principales
- **Consulta normal:** identificar productos, mostrar características, códigos reales de Odoo y stock **a mano** (`qty_available`).
- **«Con explicación»:** además de la consulta normal, explicar brevemente qué es y para qué sirve el material.
- Consultar Odoo cuando se mencionen materiales y marcas concretas; no hacerlo para conceptos puros.
- Recuperar `default_code`, `name`, `product_brand_id`, `qty_available` y `uom_id` juntos, de ser posible.
- No consultar reservas, `free_qty`, `virtual_available`, ubicaciones ni movimientos, salvo instrucción expresa.
- Nunca inventar códigos, características técnicas ni existencias.
- Verificar con fichas de fabricantes las propiedades que no consten en la descripción del ERP.
- **Stock a mano** no significa stock libre para vender; no afirmarlo.
- No subir credenciales, información personal ni documentación confidencial de clientes.

## Estructura prevista
- `agente/`: instrucciones y versiones de skills.
- `conocimiento/`: fichas de materiales y familias.
- `formacion/`: temario de 73 preguntas, pendiente de aprobación.
- `aprendizajes/`: decisiones y correcciones.
- `catalogo/`: ejemplos documentados; nunca datos de stock fijos.
- `pruebas/`: casos de control del asistente.

## Uso y mantenimiento
Cada nueva enseñanza se propone como cambio en el repositorio y pasa por revisión técnica cuando involucre normas, seguridad o características de producto.
