# Ejemplo ficticio — interpretación de una consulta de diferencial

> Ejemplo didáctico inventado. **No corresponde a un cliente real ni representa una cotización histórica de ECLIGHTING.** Sin datos económicos.

## Pedido recibido
«Diferencial Schneider 2 polos, superinmunizado, 300 mA y selectivo».

## Lo que se debe analizar
- **RCCB / interruptor diferencial**, fabricante Schneider Electric.
- **2 polos**, **IΔn = 300 mA**.
- **SI**: superinmunización, mayor inmunidad frente a disparos intempestivos; no es sinónimo de selectividad.
- **S**: selectividad temporal, propiedad distinta.
- **In** en amperios: no indicada; buscar las distintas opciones del catálogo.
- Verificar ficha de cada modelo para corroborar simultáneamente SI, S y tipo de detección (A/AC/B).

## Comportamiento esperado del agente
1. Interpretar los atributos pedidos.
2. Buscar variantes en Odoo con códigos **reales** y `qty_available` (stock a mano).
3. Informar qué atributos están verificados y cuáles no.
4. No afirmar que hay unidades libres para vender.
5. Solo incluir definición breve de RCCB si el usuario pide «con explicación».

## Aprendizaje
No forzar repregunta sobre In antes de mostrar modelos; distinguir SI de S y validar atributos de fabricante.

## Estado
Ejemplo de entrenamiento — **no es prueba de compatibilidad ni aprobación técnica de un modelo real**.
