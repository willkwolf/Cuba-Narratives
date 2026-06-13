# 🔍 NARRATIVAS GLOBALES — Repositorio de Investigación Crítica

> **Misión:** Debunking riguroso de narrativas hegemónicas usando triangulación de fuentes,
> análisis geopolítico y ciencia de datos aplicada a crisis actuales.

---

## ¿Qué es este repositorio?

Este proyecto es un **laboratorio de periodismo de investigación computacional**.
Cada módulo analiza una crisis o narrativa global dominante y la somete a tres preguntas:

1. ¿Quién se beneficia de que esta narrativa sea la oficial?
2. ¿Qué dicen las fuentes con intereses opuestos?
3. ¿Qué predicen los datos cuando se filtran sesgos?

No buscamos "la verdad objetiva" — buscamos **hipótesis falsificables** mejor fundamentadas
que las que circulan en medios masivos o en propaganda de Estado.

---

## 📁 Estructura del repositorio

```
narrativas-globales/
│
├── README.md                   ← Este archivo
│
├── casos/
│   └── cuba-monopolio/
│       ├── cuba-monopolio.html     ← Infografía scrollytelling interactiva
│       ├── datos/
│       │   ├── fmp-encuesta-2024.md    ← Datos FMP (2,703 hogares)
│       │   └── gaesa-balances.md       ← Balances filtrados (elToque 2025)
│       └── fuentes.md              ← Mapa de fuentes con sesgo explícito
│
├── metodologia/
│   └── METODOLOGIA.md          ← Marco de análisis completo
│
└── plantilla/
    └── PLANTILLA-CASO.md       ← Para agregar nuevos casos
```

> **Para agentes IA:** cada carpeta de caso es autónoma.
> Puedes trabajar un caso sin leer los demás.
> El archivo `fuentes.md` dentro de cada caso es tu punto de entrada prioritario.

---

## 🧪 Metodología

### Principio central: Triangulación con sesgo explícito

No descartamos fuentes imperfectas — las usamos sabiendo sus limitaciones.
Una fuente con sesgo conocido es más útil que una fuente de sesgo oculto.

```
SEÑAL CONFIABLE = convergencia entre fuentes con intereses OPUESTOS
RUIDO           = coincidencia entre fuentes con el mismo interés
```

**Ejemplo aplicado (caso Cuba):**
Cuando FMP (crítico del régimen), elToque (economistas independientes en Cuba)
y Havana Consulting Group (exilio técnico) coinciden en que GAESA controla 70%+
de la economía — eso es señal. Ninguno tiene incentivo de inventar el mismo dato.

---

### Pasos del proceso analítico

```
PASO 1 — IDENTIFICAR LA NARRATIVA DOMINANTE
          ¿Cuál es la historia que "todos saben"?
          ¿Quién la repite y quién se beneficia?

          ↓

PASO 2 — MAPEAR ACTORES Y SESGOS
          Tabla de actores: nombre / posición / incentivo / tipo de sesgo
          Clasificar: crítico / régimen / académico / internacional / técnico

          ↓

PASO 3 — LEVANTAR HIPÓTESIS ALTERNATIVA
          Formular en espectro: provocadora → plausible → falsificable
          La versión falsificable debe tener condición de refutación explícita

          ↓

PASO 4 — BUSCAR CONVERGENCIA ENTRE OPUESTOS
          ¿Qué datos aparecen en fuentes que se odian entre sí?
          Eso es el núcleo duro del análisis

          ↓

PASO 5 — CIENCIA DE DATOS / HIPÓTESIS CUANTITATIVA
          Traducir la tesis a predicción medible
          Contrastar con datos disponibles
          Declarar qué evidencia refutaría la hipótesis

          ↓

PASO 6 — PRODUCCIÓN DE ARTEFACTO
          Scrollytelling HTML / infografía / reporte Markdown
          El artefacto debe poder leerse sin conocer el proceso interno
```

---

### Marco teórico por defecto

Este repositorio opera desde el **pluralismo metodológico**:
no tiene ideología fija, pero sí preferencias epistémicas:

| Preferencia | Razón |
|---|---|
| Hipótesis falsificables sobre narrativas infalsificables | Popper: ciencia vs. ideología |
| Actores racionales sobre conspiraciones | Navaja de Occam geopolítica |
| Datos de primer orden sobre metaanálisis | Menos capas de interpretación |
| Escuela Austriaca para economías de precios distorsionados | Mises: cálculo económico; Hayek: conocimiento disperso |
| Búsqueda de Rentas (Rent-Seeking Theory) (Tullock-Krueger) para monopolios políticos | Explica captura sin conspiración |

> **Para agentes IA:** el marco teórico es una caja de herramientas, no un dogma.
> Si un caso requiere otro marco, documéntalo en `fuentes.md` del caso.

---

## 📚 Consulta de fuentes — Caso inaugural: Cuba (Línea de Partida)

### 📊 Datos Cuantitativos y Estadísticas Clave (Verificado Junio 2026)

| Dato / Indicador | Descripción Empírica | Fuente Primaria |
|---|---|---|
| **96%** | Pérdida de capacidad de compra para adquirir alimentos esenciales por parte de la población en años recientes. | Food Monitor Program (FMP) - Encuesta Seguridad Alimentaria 2024 |
| **67%** | Desplome de la producción agrícola nacional durante los últimos 5 años, coincidiendo con la redirección de recursos militares. | FMP / Infobae (Mayo 2026) |
| **80%** | Porcentaje de alimentos consumidos en la isla que son de origen importado. | FMP / Martí Noticias 2026 |
| **>70%** | Porcentaje de la economía cubana bajo control directo o indirecto del conglomerado militar GAESA. | Havana Consulting Group / ASCE 2025 |
| **95%** | Porcentaje de los flujos financieros controlados por GAESA en transacciones nacionales. | Havana Consulting Group / ASCE 2025 |
| **33.9%** | Porcentaje de hogares donde al menos un miembro se ha ido a dormir con hambre por falta de recursos financieros. | FMP 2024 (Sergio Ángel Baquero) |
| **29%** | Porcentaje de hogares que se alimenta **solo dos veces** al día bajo la crisis actual. | Diario de Cuba / FMP 2026 |
| **43%** | Caída interanual en el volumen total de remesas familiares recibidas en la isla durante 2024 (-70% comparado con 2019). | Cuba Siglo 21 (Febrero 2025) |
| **92.68%** | Porcentaje de las remesas totales entrantes que ingresan al país por canales informales. | Cuba Siglo 21 (Febrero 2025) |
| **3.2x** | Proporción en la que los ingresos consolidados estimados de GAESA superan el presupuesto tributario estatal de Cuba. | elToque (Noviembre 2025 - balances filtrados) |

### 🔍 Clasificación de Fuentes y Sesgos Documentados

Para contrarrestar la polarización de las narrativas tradicionales, las fuentes se clasifican explícitamente según su sesgo e incentivos de procedencia:

#### A. Fuentes Críticas / Exilio (Sesgo Anti-Régimen Pro-Mercado)
* **Food Monitor Program (FMP):** Observatorio independiente de seguridad alimentaria. Provee datos sobre desnutrición recogidos de forma presencial en 2,703 hogares en Cuba (Director: Sergio Ángel Baquero).
* **Havana Consulting Group:** Consultora basada en Miami. Analiza transacciones financieras de GAESA y balances de remesas (Director: Emilio Morales).
* **14ymedio / Diario de Cuba:** Medios independientes cubanos. Reportajes en terreno sobre decomisos estatales a agricultores y mercados informales.

#### B. Fuentes Técnicas Independientes (Sesgo Bajo / Metodología de Mercado)
* **elToque:** Portal independiente de economía. Publica el índice diario del tipo de cambio informal de divisas y balances corporativos filtrados de GAESA.
* **Cuba Siglo 21:** Asociación civil. Informes institucionales sobre el poder corporativo de GAESA, MIPYMES post-2021 y manipulación cambiaria.

#### C. Fuentes Oficiales / Régimen (Sesgo Pro-Régimen)
* **Gobierno Cubano / ONEI (Oficina Nacional de Estadística e Información):** Anuario Estadístico oficial. Útil para contrastar asimetrías de inversión (hoteles de lujo vs. agricultura).
* **Relatora ONU sobre Sanciones (Alena Douhan):** Relatoría especial de Naciones Unidas. Foco prioritario en el impacto estructural negativo del embargo estadounidense.

#### D. Fuentes Internacionales Neutras (Sesgo Bajo / Foco en Derechos)
* **Relatoría ONU sobre la Alimentación:** Relatoría especial. Evaluaciones del derecho a la alimentación, alertas nutricionales y recomendaciones al gobierno cubano.

---

### Cómo usar este mapa de fuentes

```
✅ Usar para tesis:     Datos que aparecen en convergencia entre fuentes con intereses OPUESTOS
⚠️ Usar con reserva:   Datos que solo aparecen en fuentes de un solo lado
❌ No usar como prueba: Datos de fuente única sin posibilidad de corroboración
```

---

## ⚙️ Para agentes IA — Instrucciones de reforma

Si eres un agente de IA trabajando en este repositorio, lee esto antes de hacer cambios:

### Reglas de edición

```yaml
NUNCA:
  - Eliminar la sección de sesgo declarado en las fuentes
  - Presentar una tesis sin su condición de falsificación
  - Agregar datos sin fuente explícita
  - Reemplazar el espectro de tesis por una sola posición

SIEMPRE:
  - Documentar el sesgo de toda fuente nueva que agregues
  - Mantener la separación entre "señal" y "ruido"
  - Si cambias la tesis principal, explicar por qué en un comentario
  - Actualizar la fecha de los datos cuando haya nuevas fuentes
```

### Cómo agregar un nuevo caso

1. Copiar `plantilla/PLANTILLA-CASO.md`
2. Crear carpeta `casos/nombre-del-caso/`
3. Completar: narrativa dominante → actores → tesis en espectro → datos → fuentes
4. Producir artefacto visual en HTML (scrollytelling) o Markdown
5. Agregar entrada en este README bajo "Casos activos"

### Variables de contexto que los agentes deben conocer

```
CASO ACTUAL:    Cuba — Desabastecimiento y monopolio GAESA
FECHA DATOS:    Junio 2026 (crisis activa, datos en evolución)
MARCO TEÓRICO:  Contraste: Lente CEPAL vs. Economía Institucional y Búsqueda de Rentas (Rent-Seeking)
HIPÓTESIS:      GAESA = monopolio capitalista con retórica socialista
FALSIFICACIÓN:  Si GAESA se disuelve y el desabasto persiste → tesis incompleta
FUENTE SEED:    Food Monitor Program (FMP) — informe ONU mayo 2026
```

---

## 📋 Casos activos

| # | Caso | Narrativa debunkeada | Estado | Artefacto |
|---|---|---|---|---|
| 01 | **Cuba: Capitalismo Capturado** | "El desabasto es culpa del bloqueo" | ✅ Publicado | `cuba-monopolio.html` |
| 02 | *(próximo)* | — | 🔲 Pendiente | — |

---

## ⚠️ Descargo de responsabilidad

Este repositorio produce **investigación analítica e intelectual**, no propaganda.

- Las tesis presentadas son **hipótesis académicas** formuladas para ser refutadas, no verdades establecidas.
- El análisis no representa la posición política de ningún gobierno, partido, institución ni financiador.
- Las fuentes están identificadas con su sesgo explícito. El lector es responsable de su propia evaluación.
- Los datos numéricos provienen de fuentes citadas. En casos de datos estimados o filtrados, se indica explícitamente.
- Este repositorio no tiene afiliación con ninguno de los actores analizados, incluyendo el gobierno cubano, el gobierno de Estados Unidos, GAESA, Food Monitor Program ni organismos de la ONU.
- El análisis geopolítico puede contener errores de interpretación. Se invita a la corrección pública mediante Issues o Pull Requests documentados.
- **Este material no debe usarse como insumo único para decisiones de política pública, periodismo publicado o litigios legales** sin verificación independiente adicional.

> Las hipótesis provocadoras son herramientas de pensamiento, no acusaciones formales.

---

## 📄 Licencia

**Creative Commons Atribución – NoComercial – CompartirIgual 4.0 Internacional**
`CC BY-NC-SA 4.0`

```
Eres libre de:
  ✅ Compartir  — copiar y redistribuir el material en cualquier medio o formato
  ✅ Adaptar    — remezclar, transformar y construir a partir del material

Bajo las siguientes condiciones:
  📌 Atribución       — Debes dar crédito apropiado al repositorio original
  🚫 NoComercial      — No puedes usar el material con fines comerciales
  🔄 CompartirIgual   — Si remezclas el material, debes distribuirlo bajo la misma licencia

Los datos de terceros (FMP, Havana Consulting Group, elToque, etc.) conservan
sus propias licencias y derechos. Esta licencia aplica solo al trabajo
analítico, estructural y visual producido en este repositorio.
```

Texto completo: [creativecommons.org/licenses/by-nc-sa/4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es)

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas bajo estas condiciones:

- Toda fuente nueva debe incluir sesgo declarado
- Toda tesis nueva debe incluir condición de falsificación
- Los cambios a datos existentes requieren fuente actualizada en el commit
- El tono es analítico, no panfletario — en ninguna dirección ideológica

---

*Última actualización: junio 2026 — Crisis de Cuba en desarrollo activo*
