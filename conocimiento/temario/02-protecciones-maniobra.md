# Módulo 02 – Protecciones, maniobra y control
Qué protege, qué maniobra y qué parámetros cambian la selección. Estado: borrador.

### P01 · ¿Qué es una térmica y cómo protege?
El **interruptor termomagnético** abre un circuito por **sobrecarga** (disparo térmico) o **cortocircuito** (disparo magnético). Su calibre debe coordinarse con la capacidad del conductor y las condiciones de instalación. **No reemplaza al diferencial.**
- **Para cotizar:** polos, In (A), curva, poder de corte (kA), tensión, norma y línea.
- **Palabras clave:** térmica, termica, llave térmica, termomagnética, MCB, automático, 2x20, 1x16.

### P02 · ¿Qué significan las curvas B, C y D?
Definen el umbral de actuación **magnética instantánea**. Como referencia, IEC 60898-1: **B ≈ 3–5 × In, C ≈ 5–10 × In y D ≈ 10–20 × In**. B favorece circuitos de baja corriente de arranque; C es habitual en uso general; D admite picos elevados, sujeto a cálculo.
- **Para cotizar:** no sustituir una curva por otra por disponibilidad: verificar corriente de arranque y condiciones de desconexión.
- **Palabras clave:** curva C, curva B, curva D, C16, C20, disparo magnético.

### P03 · ¿Qué es un diferencial? ¿Qué significan 30 mA y 300 mA?
El **interruptor diferencial** detecta el desequilibrio entre corrientes de ida y retorno (corriente residual). **30 mA** se usa habitualmente como protección adicional de personas; **300 mA** suele asociarse a otros objetivos de protección o coordinación. Esos mA son **sensibilidad**, no amperaje de carga.
- **Para cotizar:** polos, corriente nominal (A), sensibilidad IΔn (mA), tipo, selectividad o inmunidad, tensión y norma.
- **Palabras clave:** disyuntor, diyuntor, disy, diferencial, ID, IID, RCCB, 30mA, 300mA, salta por humedad.

### P04 · ¿En qué se diferencian los diferenciales AC, A, F, B, SI y S?
**AC:** fugas alternas sinusoidales. **A:** también continuas pulsantes. **F:** contempla ciertas frecuencias de equipos con variación electrónica. **B:** además detecta corriente continua lisa. **SI** indica alta inmunidad frente a disparos molestos. **S** indica retardo selectivo. **SI y S no significan lo mismo.**
- **Para cotizar:** elegir tipo según la carga y los requisitos del proyecto; no cambiar A por AC ni S por SI.
- **Palabras clave:** superinmunizado, super inmunizado, SI, A-SI, selectivo, clase A, clase B, AP-R, cargador auto eléctrico, variador.

### P05 · ¿Qué es un interruptor de caja moldeada (MCCB)?
Un **MCCB** es un interruptor automático para protección y maniobra de circuitos, habitualmente de corrientes mayores o con funciones ajustables. Frente a una térmica modular puede ofrecer **regulaciones** y poderes de corte superiores, según la gama. No todos los MCCB son regulables.
- **Para cotizar:** polos, corriente nominal o bastidor, unidad de disparo, poder de corte a la tensión indicada, accesorios.
- **Palabras clave:** caja moldeada, MCCB, compact, NSX, Tmax, interruptor regulable, 4x250, 3x160.

### P06 · ¿Qué significan Icu, Ics, In, Ir e Im?
**In:** corriente asignada. **Ir:** ajuste de protección de sobrecarga. **Im:** umbral magnético o instantáneo en determinadas unidades. **Icu:** capacidad última de corte. **Ics:** capacidad de corte en servicio; ambas a una tensión especificada. No asumir que Ics = Icu.
- **Para cotizar:** ejemplo: "4P, 250 A, 36 kA" requiere conocer tensión, unidad de disparo y regulación; confirmar Icu/Ics.
- **Palabras clave:** Icu, Ics, Ir, Im, regulación, ajuste, 36 kA, 50 kA.

### P07 · ¿Qué es un contactor de potencia?
El **contactor** es un interruptor accionado eléctricamente mediante una **bobina**; conecta y desconecta cargas repetidamente. Tiene contactos de **potencia** y, según modelo, **auxiliares**. Por sí solo no sustituye la protección de sobrecarga y cortocircuito.
- **Para cotizar:** cantidad de polos, corriente o categoría de empleo, tensión y frecuencia de bobina, auxiliares, potencia del motor.
- **Palabras clave:** contactor, contactora, bobina 220, bobina 24, LC1, AF, arranque motor.

### P08 · ¿Qué significan AC-1 y AC-3?
Son **categorías de utilización**. **AC-1** corresponde a cargas no inductivas o poco inductivas, como calefacción; **AC-3** a arranque y parada normal de motores de jaula de ardilla. Un contactor puede admitir **corrientes distintas** para AC-1 y AC-3.
- **Para cotizar:** para motor, consultar corriente o potencia y tensión de empleo en AC-3; no guiarse solo por los A de AC-1.
- **Palabras clave:** AC1, AC3, categoría de empleo, motor, resistiva.

### P09 · ¿Qué diferencia hay entre contactor de potencia, auxiliar y modular?
El **de potencia** maniobra cargas principales; el **auxiliar** multiplica señales de control con contactos NA/NC; el **modular** está pensado para montaje DIN y usos específicos (por ejemplo iluminación). Que sea modular no garantiza aptitud AC-3 para motores.
- **Para cotizar:** indicar función, categoría de empleo, bobina, polos y cantidad y tipo de contactos.
- **Palabras clave:** contactor auxiliar, contactor modular, contactor DIN, silencioso, iluminación.

### P10 · ¿Qué tipos de relés se usan en tableros?
Un **relé** cambia el estado de contactos al cumplirse una condición. Puede ser **auxiliar** (señal), **temporizador** (tiempo), **térmico** (sobrecarga de motor), **control de fase o tensión**, entre otros. El nombre genérico "relé" no alcanza para elegir uno.
- **Para cotizar:** identificar función, alimentación o bobina, rango de ajuste, contactos, zócalo y montaje.
- **Palabras clave:** relé, rele, relay, temporizador, timer, interfase, relé de interfaz.

### P11 · ¿Qué diferencia hay entre relé térmico y guardamotor?
El **relé térmico** detecta sobrecargas del motor y normalmente ordena abrir un contactor; no suele cortar él mismo la potencia. El **guardamotor** combina maniobra manual y protecciones específicas del motor, incluidas sobrecargas y cortocircuitos según modelo.
- **Para cotizar:** corriente nominal del motor, rango ajustable, poder de corte y coordinación con contactor.
- **Palabras clave:** guardamotor, guarda motor, GV2, MS116, relevo térmico, térmico de motor, TA25, TF42.

### P12 · ¿Qué diferencia hay entre seccionadora y conmutadora?
La **llave seccionadora** permite aislar un circuito; algunas están habilitadas para cortar carga según su **categoría de empleo**. La **conmutadora** selecciona entre fuentes o circuitos, por ejemplo I–0–II. Ninguna se considera protección automática salvo función especificada.
- **Para cotizar:** polos, A, V, categorías AC-21/22/23, posiciones, transición, montaje y posibilidad de enclavamiento.
- **Palabras clave:** llave conmutadora, conmutadora rotativa, seccionador, corte general, I-0-II, red-grupo, INS.

### P13 · ¿Qué son los descargadores de sobretensión (DPS)?
Un **DPS** limita sobretensiones transitorias desviando su energía. **Tipo 1:** capaz de conducir corrientes parciales de rayo. **Tipo 2:** protección principal ante transitorios en tableros. **Tipo 3:** protección complementaria cerca de equipos sensibles. **No sustituye** térmicas ni diferenciales.
- **Para cotizar:** tipo, configuración de red, Uc, Up, In, Imax/Iimp, polos y coordinación con protecciones.
- **Palabras clave:** descargador, DPS, SPD, protector de sobretensión, rayos, pararrayos de tablero.

### P14 · ¿Qué es una selectora de fases?
Una **selectora manual** permite elegir qué fase alimenta una carga monofásica, respetando el esquema del tablero. Una **selectora automática** monitorea fases y conmuta mediante un sistema diseñado para ello. No se deben unir fases entre sí. Distinto del **relé control de fase**, que vigila la red y desconecta la carga (ver P10).
- **Para cotizar:** manual o automática, número de posiciones, corriente, tensión, esquema, neutro e interbloqueo.
- **Palabras clave:** selector de fase, selectora de fases, conmutador de fase, control de fase, falta de fase.

### P15 · ¿Qué es un seccionador portafusibles?
Combina **seccionamiento** con alojamiento de **fusibles**, para protección y aislamiento según diseño. Hay variantes para **cilíndricos** y **NH** (por ejemplo NH00, NH1, NH2, NH3). Tamaño físico del fusible y amperaje **son parámetros diferentes**.
- **Para cotizar:** cantidad de polos, formato o tamaño de fusible, corriente, tensión, categoría de empleo y si incluye fusibles.
- **Palabras clave:** seccionador fusible, portafusible, base NH, seccionador bajo carga, fusiblera.

### P16 · ¿Qué formatos de fusible existen?
Los más comunes son: **NH** (cuchilla), en tamaños 000, 00, 1, 2 y 3, para potencia y tableros generales; **cilíndricos**, en medidas como 10x38, 14x51 y 22x58 mm, para tableros y control; y **tipo tapón** (Diazed o Neozed), a rosca, en instalaciones más antiguas. **El tamaño físico y la corriente nominal son datos distintos**: un mismo tamaño NH se fabrica en varios amperajes.
- **Para cotizar:** formato y tamaño, corriente nominal (A), tensión, clase de uso y base o seccionador compatible.
- **Palabras clave:** fusible, NH, NH00, cuchilla, cilíndrico, 10x38, tapón, Diazed, Neozed.

### P17 · ¿Qué significan gG, aM y aR?
Indican la **clase de uso** del fusible. **gG:** uso general; protege cables contra sobrecarga y cortocircuito. **aM:** acompañamiento de motor; soporta el pico de arranque y protege solo contra cortocircuito, por eso se usa junto a un relé térmico o guardamotor. **aR / gR:** ultrarrápidos para proteger semiconductores (variadores, rectificadores). **No son intercambiables.**
- **Para cotizar:** clase exigida, carga a proteger y corriente nominal.
- **Palabras clave:** gG, gL, aM, aR, gR, ultrarrápido, fusible de motor.
