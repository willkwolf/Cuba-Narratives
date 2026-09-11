# 🔍 NARRATIVAS GLOBALES — Repositorio de Investigación Crítica

> **Misión:** Debunking riguroso de narrativas hegemónicas usando triangulación de fuentes,
> análisis geopolítico, ciencia de datos y trazabilidad periodística aplicada a crisis complejas.

---

## ¿Qué es este repositorio?

Este proyecto es un **laboratorio de periodismo de investigación computacional**.
Cada módulo analiza una crisis o narrativa global dominante y la somete a tres preguntas:

1. **¿Quién se beneficia** de que esta narrativa sea la oficial?
2. **¿Qué dicen las fuentes** con intereses opuestos?
3. **¿Qué predicen los datos** cuando se filtran sesgos y se auditan balances primarios?

No buscamos imponer una posición política en un escenario complicado y complejo — buscamos **reducir y simplificar el ruido informativo**, ofreciendo **hipótesis falsificables** respaldadas por una bitácora viva de evidencia.

---

## 📁 Estructura del repositorio

```
Cuba-Narratives/
│
├── README.md                           ← Este archivo
├── Fuentes.md                          ← Mapa de fuentes, sesgos declarados y falsación
├── LECCIONES.md                        ← Directrices de UX, accesibilidad (a11y) y carga cognitiva
│
├── index.html                          ← Infografía scrollytelling interactiva (ES/EN)
├── cuba-monopolio.html                 ← Redirección / archivo histórico
│
├── data/
│   ├── indicadores.json                ← Métricas cuantitativas estructuradas y trianguladas
│   └── bitacora.json                   ← Hitos periodísticos y trazabilidad de evidencia
│
├── scripts/
│   └── audit_claims.py                 ← Linter y auditor automático de claims y consistencia
│
└── .github/workflows/
    ├── deploy.yml                      ← Despliegue continuo a GitHub Pages
    └── audit-pipeline.yml              ← Pipeline de verificación de integridad y datos
```

> **Para agentes IA e investigadores:** Cada caso es autónomo. Los archivos `data/indicadores.json` y `data/bitacora.json` representan la fuente estructurada de verdad, mientras que `Fuentes.md` documenta la justificación epistemológica de cada indicador.

---

## 🧪 Metodología: Triangulación con Sesgo Explícito

No descartamos fuentes imperfectas — las usamos conociendo sus intereses y limitaciones. Una fuente con sesgo conocido es más útil que una fuente de neutralidad simulada.

```
SEÑAL CONFIABLE = convergencia entre fuentes con intereses OPUESTOS
RUIDO           = coincidencia entre fuentes con el mismo interés
```

### Ejemplo aplicado (caso Cuba):
* **El tamaño de GAESA:** La consultora del exilio (Havana Consulting Group) estimaba que GAESA controlaba ">70% de la economía". Sin embargo, la auditoría econométrica de balances internos filtrados (Pavel Vidal / *elTOQUE* / Univ. Columbia) situó sus operaciones en torno al **~40% del PIB**, con un 37% de valor agregado y reservas líquidas por $14,467M USD. El repositorio contrasta ambos datos: descarta el mito del 70% sin diluir la captura institucional real de GAESA.
* **La paradoja hotelera:** Las propias estadísticas del régimen (ONEI) demuestran que los hoteles de GAESA operan a solo **25% – 30% de ocupación**, lo que refuta la idea de un cartel hiper-eficiente y confirma la tesis austriaca de mala asignación masiva de capital (*elefantes blancos*).

---

## 📊 Datos Cuantitativos y Estadísticas Clave (Verificado Septiembre 2026)

| Dato / Indicador | Descripción Empírica | Fuente Primaria y Metodología |
|---|---|---|
| **96%** | Pérdida de capacidad de compra de alimentos esenciales por parte de la población | Food Monitor Program (FMP) - Encuesta 2,703 hogares |
| **67%** | Desplome de la producción agrícola nacional en el último lustro | FMP / Infobae (Mayo 2026) |
| **80%** | Porcentaje de alimentos consumidos en la isla de origen importado | FMP / Martí Noticias / ONEI 2026 |
| **40% vs. >70%** | Peso de GAESA: ~40% del PIB según balances contables reales filtrados (Pavel Vidal / elTOQUE) vs. >70% estimado por el exilio | Balances filtrados GAESA (2023-2024) / Havana Consulting Group |
| **$14,467M USD** | Reservas líquidas y depósitos retenidos por GAESA en el Banco Financiero Internacional | Balances internos filtrados (Marzo 2024) / elTOQUE |
| **3.2×** | Multiplicador de ingresos consolidados de GAESA frente al presupuesto tributario estatal | elTOQUE (Balances contables filtrados 2025) |
| **25% – 30%** | Tasa promedio de ocupación hotelera en instalaciones de GAESA (Gaviota) | ONEI / Pedro Monreal (2024-2026) |
| **92.68%** | Porcentaje de remesas familiares que ingresan por canales informales | Cuba Siglo 21 (Febrero 2025) |
| **33.9%** | Porcentaje de hogares donde al menos un miembro durmió con hambre por falta de ingresos | FMP 2024 (Sergio Ángel Baquero) |
| **29%** | Porcentaje de hogares que consume solo dos comidas al día | Diario de Cuba / FMP 2026 |
| **43%** | Caída interanual en el volumen total de remesas familiares en 2024 (-70% vs. 2019) | Cuba Siglo 21 (Febrero 2025) |

---

## 🗓️ Bitácora de Evidencia: Reduciendo el Ruido

La nueva sección interactiva **"Bitácora de Evidencia"** en `index.html` permite al lector auditar cómo los hitos de la realidad ajustan nuestras hipótesis:

1. **Septiembre 2026:** Sanciones del Secretario de Estado Marco Rubio al Banco Exterior de Cuba (BEC) y a Fidel Ernesto Castro Calis (O.E. 14404).
2. **Mayo 2026:** Encuesta nacional FMP ante relatores especiales de la ONU sobre el derecho a la alimentación.
3. **Noviembre 2025:** Filtración de balances internos de GAESA y auditoría econométrica de Pavel Vidal.
4. **Diciembre 2025:** Interrupción de crudo venezolano y colapso del Sistema Electroenergético Nacional (SEN).
5. **Febrero 2025:** Colapso del canal oficial de remesas y migración al mercado paralelo.
6. **2024–2026:** Informe ONEI / Pedro Monreal sobre desinversión agrícola y ocupación hotelera estancada en 25-30%.

---

## 🚀 Plan de Superación SWOT (Horizonte 6 Meses)

* **Fase 1 (Mes 1–2): Desacoplamiento de Datos e Interfaz:** Datasets estructurados en `data/`, nuevo componente de Bitácora en `index.html`, sincronización y limpieza.
* **Fase 2 (Mes 3–4): Pipeline Automatizado y Fact-Checking Agéntico:** Integración de `scripts/audit_claims.py` con GitHub Actions para monitorear fuentes y auditar la consistencia de cifras.
* **Fase 3 (Mes 5–6): Escalabilidad Multicaso:** Estandarización de la plantilla modular para aplicar la misma triangulación a otros contextos geopolíticos.

---

## ⚠️ Descargo de responsabilidad

Este repositorio produce **investigación analítica e intelectual**, no propaganda partidaria.
Las tesis presentadas son **hipótesis académicas** formuladas para ser refutadas mediante condiciones explícitas de falsación. Las fuentes se identifican con su sesgo para empoderar al lector en su propia evaluación crítica.

---

## 📄 Licencia

**Creative Commons Atribución – NoComercial – CompartirIgual 4.0 Internacional** (`CC BY-NC-SA 4.0`).

---

*Última actualización: Septiembre 10, 2026 — Investigación activa en desarrollo continuo*
