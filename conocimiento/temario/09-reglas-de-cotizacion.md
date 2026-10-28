# Módulo 09 – Reglas de cotización ECLIGHTING
Cómo interpretamos un pedido y qué necesitamos cuando nos piden un producto o una familia.
Este documento describe cómo cotiza el equipo de ECLIGHTING: cómo leemos un pedido y, cuando alguien pide un producto o una familia, qué entendemos que necesita.
El asistente aplica estas reglas SIEMPRE que la consulta encaje, aunque el usuario no las repita. Sin precios ni stock.
Estado de cada regla: **Vigente** (definida o confirmada por el equipo) o **Propuesta** (aplicar con aviso hasta que se confirme).

---

## 1. Cómo leemos un pedido

### I01 · Separar el pedido en atributos (Vigente)
Antes de buscar, cada ítem se descompone en: familia, marca, medidas, datos eléctricos (polos, A, mA, kA, curva, clase), material, norma y accesorios. Los valores del cliente no se cambian.
Se separa siempre: **lo que el cliente dijo**, **lo que suponemos** y **lo que falta preguntar**.

### I02 · Pulgadas a milímetros en PVC (Vigente)
El cliente pide en pulgadas; las líneas de PVC están en mm. Equivalencia comercial: 5/8" = 16 mm · 3/4" = 20 mm · 7/8" = 22 mm · 1" = 25 mm · 1 1/4" = 32 mm · 1 1/2" = 40 mm · 2" = 50 mm. Se aplica y se aclara para que el cliente la confirme.

### I03 · Unidad en que pide el cliente vs. unidad de venta (Vigente)
- "X caños" = barras: confirmar largo de barra; Odoo puede manejar metros.
- Corrugado: se pide en rollos (25 o 50 m según código); el stock está en metros.
- Cable: se pide en metros o rollos; una fila por color, nunca sumar colores.
- Tarugos y tornillos: por estuche o caja; confirmar cantidad por envase.
- La unidad que muestra Odoo puede no ser la real (hay cables cargados en "Unidades").

### I04 · Términos de acero aplicados a PVC (Vigente)
"Semipesado", "liviano" y "pesado" vienen del caño de acero. Si el pedido dice PVC, se elige la clase equivalente del fabricante de PVC y se aclara.

---

## 2. Qué entendemos cuando nos piden… (jerga del mostrador)

| Cuando el cliente dice | Entendemos | Cómo puede figurar en Odoo |
|---|---|---|
| disyuntor / diyuntor / disy | Interruptor diferencial | INT. DIFERENCIAL, INT.DIF, IID, ID, F202/F204, FH202 (ABB), Vigi (bloque acoplable) |
| térmica / llave térmica | Interruptor termomagnético | INT. TERMOMAGNETICO, TERMOMAGNETICA, SH201/SH202 (ABB) |
| superinmunizado | Diferencial de inmunidad reforzada | SI, A-SI, A-SUP INMU; ABB: AP-R |
| selectivo | Diferencial con retardo, va aguas arriba | S, SELEC, SELECTI |
| caja 5x10 | Caja rectangular de embutir | RECTANGULAR |
| caja 5x5 | Caja mignon | MIGNON |
| caja octogonal | Caja octogonal chica o grande (preguntar cuál) | OCTOGONAL CHICA / GRANDE |
| caño corrugado | Tubo corrugado en rollo | TUBO CORRUGADO |
| caño PVC / caño rígido | Tubo rígido de PVC | TUBO RÍGIDO |
| tarugo / taco | Taco de expansión | TARUGO, TACO, S6 / S8 / S10 |
| unipolar 2,5 | Cable unipolar 1x2,5 mm² | CABLE UNIP. 1X2.50 |
| bornes / borneras Zoloda | Familia Zoloda para tablero completa (ver FA01) | BPN, BSLKN, D-BPN, JSSB, EKN1, SE1 |

---

## 3. Cuando nos piden una familia, necesitamos…

### FA01 · Familia Zoloda para tablero (borneras) – Vigente (definida por Nicolás, 2026-10-28)
**Cuándo aplica:** piden "bornes Zoloda", "borneras Zoloda", "familia Zoloda para tablero", "accesorios BPN" o un tablero con borneras Zoloda.
**Qué necesitamos:** siempre el juego completo, no solo el borne:

| Pieza | Qué es | Cómo figura en Odoo |
|---|---|---|
| BPN | Borne de paso a tornillo | BPN-2,5 / -04 / -06 / -10 / -16 / -35 / -50 (colores: -AZ, -VE, -RO, etc.) |
| BSLKN | Borne de puesta a tierra | BSLKN-04 / -06 / -10 / -16 / -35 |
| D-BPN | Tapa final para BPN | D-BPN-2,5/10 (BPN-2,5, 04, 06, 10) · D-BPN-16/35 (BPN-16, 35) |
| JSSB | Puente fijo para BPN | JSSB-10-05/BPN → BPN-2,5 · JSSB-10-06/BPN → BPN-04 · JSSB-10-08/BPN → BPN-06 · JSSB-10-10/BPN → BPN-10 · JSSB-10-12/BPN → BPN-16 · JSSB-10-16/BPN → BPN-35 · JSSB-03-20/BPN → BPN-50 |
| EKN1 | Extremo / tope para riel DIN 35 | EKN1 |
| SE1 | Separador 64×52 mm | SE1 (2 mm) · SE1-D (1 mm amarillo) · SE1-D-GR (1 mm gris) |

**Cómo elegir:** la sección del cable define el BPN, y el BPN define la tapa D-BPN y el puente JSSB. Tierra: BSLKN de la misma sección. Los JSSB-xx/BKF son para bornes a resorte BKF: no van con BPN. Si no dicen sección, mostrar la familia por sección y preguntar solo ese dato.

### FA02 · Cañería de PVC – Propuesta
**Cuándo aplica:** piden caño rígido de PVC.
**Qué necesitamos:** además del caño, de la misma línea y medida: conectores, curvas, uniones y grampas. Si no los pidieron, se ofrecen como "sugerido".
**Cómo elegir:** la medida (pulgadas → mm, ver I02) y la clase del caño definen todos los accesorios.

### FA03 · Cajas de embutir – Propuesta
**Cuándo aplica:** piden cajas de embutir.
**Qué necesitamos:** mismo sistema que la cañería (PVC con PVC, chapa con chapa). Si son cajas de paso, tapas ciegas.
**Cómo elegir:** forma (5x10, 5x5, 10x10, octogonal) y, en octogonales, chica o grande.

---

## 4. Lo que siempre hay que definir antes de cerrar un ítem

| Familia | Datos que definen el producto |
|---|---|
| Diferencial | Polos, corriente (A), sensibilidad (mA), clase (AC / A / B), SI o selectivo |
| Termomagnética | Polos, corriente (A), curva (B/C/D), poder de corte (kA) |
| Caja moldeada | Polos, corriente, poder de corte a la tensión, unidad de disparo |
| Contactor | Corriente o potencia en AC-3, tensión de bobina, contactos auxiliares |
| Cable | Formación y sección, color, aislación, tensión, norma si la exigen |
| Caño y corrugado | Medida, material, clase, unidad (barra, metro, rollo) |
| Caja octogonal | Chica o grande |
| Tornillos | Diámetro y largo |
| Gabinete | Medidas, material, IP, montaje, placa y contrafrente |

Si falta uno de estos datos, se muestran las variantes posibles y se pregunta solo ese dato.

---

## Pendientes de definir con el equipo
- Qué hacer con los códigos con sufijo `/BORRAR` (ocultar, mostrar marcados o mostrar solo si tienen stock).
- Confirmar FA02 y FA03.
