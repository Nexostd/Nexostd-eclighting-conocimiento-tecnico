# Arquitectura

**GitHub** = documentación técnica versionada, instrucciones, casos de prueba y decisiones.

**Tuqui** = interfaz conversacional del equipo que interpreta la consulta, presenta resultados y utiliza sus fuentes.

**Odoo** = fuente en vivo de referencias de catálogo y cantidades a mano. El agente usa `product.product` con `default_code`, `name`, `product_brand_id`, `qty_available`, `uom_id` al investigar productos.

**Fichas de fabricantes y documentación aprobada** = fuente para confirmar parámetros técnicos críticos y equivalencias.

No existe sincronización automática GitHub→Tuqui por el hecho de subir archivos. Las actualizaciones de instrucciones/skills/contexto deben publicarse o enlazarse mediante un flujo aprobado y verificado.
