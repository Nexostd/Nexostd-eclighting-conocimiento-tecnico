# Ejemplos de respuesta esperada

## Pedido normal
**Usuario:** «INS Schneider 630A»

**Respuesta esperada:** identificación de la familia, diferencias de 3P/4P y versión, tabla de coincidencias Odoo (código, marca, características, **stock a mano**). **No** dar una clase teórica ni inventar códigos.

## Pedido con explicación
**Usuario:** «Interruptores Schneider 630A con explicación»

**Respuesta esperada:** además de la tabla normal, agregar: «Un interruptor automático de caja moldeada protege circuitos de alta corriente contra sobrecargas y cortocircuitos. Se usa en tableros generales, distribución de potencia e instalaciones industriales». Solo si la identificación corresponde a una MCCB; una referencia INS puede ser un **interruptor-seccionador** y no debe presentarse erróneamente como MCCB.

## Diferenciales
**Usuario:** «Diferenciales Schneider bipolares SI, 300 mA, selectivos»

**Respuesta esperada:** separar:
- 2 polos; sensibilidad diferencial 300 mA; superinmunización SI; selectividad S; tipo A/AC según ficha.
- Mostrar varios códigos Odoo coincidentes y `qty_available` por unidad.
- No confundir «SI» con «S» ni inferir que dos modelos sean equivalentes.

## Regla general
«Con explicación» es optativo. Sin esa frase, responder prioritariamente con identificación y variantes de catálogo.
