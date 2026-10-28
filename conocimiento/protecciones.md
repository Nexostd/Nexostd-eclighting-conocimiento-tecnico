# Protecciones eléctricas — guía inicial

> Material de apoyo a validar por el responsable técnico. Las características de una referencia concreta se confirman en la ficha del fabricante.

## Interruptor termomagnético (MCB)
Protege contra **sobrecargas y cortocircuitos**. Características de identificación: In (A), número de polos, curva de disparo (B/C/D), poder de corte (kA), tensión, normativa y serie de fabricante.

## Interruptor diferencial (RCCB)
Detecta corriente residual y desconecta cuando se cumplen sus condiciones de disparo. No reemplaza una protección contra sobrecarga/cortocircuito salvo cuando integra esa función (RCBO). Características: polos, In (A), sensibilidad diferencial IΔn (mA), tipo AC/A/B, selectividad S, comportamiento ante perturbaciones (SI), tensión y normas.

- **Tipo A:** detección de corriente residual alterna senoidal y pulsante continua, dentro de las condiciones de la norma correspondiente.
- **Tipo AC:** detecta corriente residual alterna senoidal; no suponer idoneidad frente a componentes continuas.
- **Tipo S/selectivo:** retardo intencional pensado para coordinación con diferenciales aguas abajo, sujeto a las condiciones del diseño.
- **SI/superinmunizado:** mejor inmunidad frente a perturbaciones que pueden provocar disparos intempestivos. **No equivale a selectivo**.
- **300 mA**: sensibilidad residual distinta de 30 mA. No sustituir una por otra cuando el diseño requiere protección adicional de personas.

## Interruptor automático de caja moldeada (MCCB)
Generalmente se emplea para circuitos de mayor corriente y capacidades de corte. Parámetros: corriente nominal, número de polos, unidad de disparo (térmico-magnética o electrónica), Icu/Ics, tensiones de empleo, montaje y accesorios.

## Interruptor-seccionador
Su misión principal es la maniobra/seccionamiento conforme a su categoría y especificación; **no suponer protección automática contra sobrecargas o cortocircuitos**. Es importante para diferenciar familias Schneider INS/INV de NS/NSX.

## Poder de corte (kA)
Representa la capacidad del dispositivo para interrumpir una corriente de cortocircuito bajo condiciones normalizadas. No se debe elegir sin evaluar la corriente de cortocircuito prevista y la norma/dispositivo.

## Para cotizar
Recuperar polos, corriente nominal, curva o unidad de disparo, poder de corte si corresponde, sensibilidad/tipo en diferenciales, tensión, modelo/marca y accesorios requeridos.
