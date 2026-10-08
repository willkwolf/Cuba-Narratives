# CUBA NARRATIVAS — Repositorio de Investigación Crítica

Investigación interactiva y base de datos verificable sobre la crisis institucional, el monopolio corporativo militar y el colapso material en Cuba.

Sitio web en producción: [https://willkwolf.github.io/Cuba-Narratives/](https://willkwolf.github.io/Cuba-Narratives/)

---

## 1. Misión y Alcance

Este proyecto es un laboratorio abierto de periodismo computacional y análisis institucional. Su objetivo es reducir el ruido informativo y desarmar la polarización ideológica que suele dominar el debate sobre Cuba, sometiendo cada narrativa a estándares de verificación cruzada, balances documentales primarios y condiciones formales de falsación.

Para lograrlo, la investigación aborda tres interrogantes estructurales:
1. Incentivos: ¿Quién se beneficia políticamente de que una narrativa específica sea aceptada como la oficial?
2. Contraste empírico: ¿Qué revelan los datos de actores con intereses opuestos cuando se confrontan de manera directa?
3. Falsación científica: ¿Qué condiciones materiales concretas refutarían cada hipótesis formulada?

---

## 2. Metodología de Investigación y Fact-Checking

Esta sección detalla el marco metodológico para auditores académicos, periodistas de investigación y agencias de verificación de datos (fact-checkers como AFP, EFE o unidades independientes).

### A. Triangulación de Fuentes con Sesgo Declarado
El proyecto parte de una premisa epistemológica: en contextos de censura y polarización geopolítica no existen fuentes neutras. La neutralidad simulada suele ser más opaca que el sesgo declarado. Por ende, no se descartan fuentes por su alineación política; se clasifican según sus incentivos y se busca la convergencia empírica:

* Señal confiable: Convergencia en el dato entre fuentes con intereses o incentivos ideológicos opuestos.
* Ruido o propaganda: Coincidencia entre fuentes con el mismo incentivo que no aportan contraste documental independiente.

Espectro de fuentes auditadas:
* Fuentes oficiales del Estado cubano (ONEI, MINREX, discursos de la Asamblea Nacional): Monitoreo de balances de comercio exterior, asignación sectorial de inversiones y turismo. Su sesgo es oficialista, pero sus propios anuarios estadísticos permiten evidenciar contradicciones internas (como la inversión récord en hoteles con ocupación del 25% frente a la caída agrícola).
* Fuentes del exilio técnico y centros de pensamiento (Havana Consulting Group, Cuba Siglo 21): Estimaciones sobre flujos de remesas y control militar. Se someten a contraste crítico para evitar la sobrestimación retórica (por ejemplo, corrigiendo el mito de que GAESA controla más del 70% del PIB a su cifra auditada real del ~40%).
* Fuentes técnicas independientes y periodismo econométrico (elTOQUE, análisis de balances filtrados por Pavel Vidal, Pedro Monreal, Carmelo Mesa-Lago): Auditorías basadas en libros contables directos, tasas representativas del mercado informal y modelos econométricos independientes.
* Organizaciones de derechos humanos e investigaciones de campo (Food Monitor Program, Casa Palanca en alianza con Cubadata): Encuestas presenciales y probabilísticas a miles de hogares cubanos en toda la isla (seguridad alimentaria, colapso de la gratuidad médica y corrupción hospitalaria).
* Organismos internacionales (Relatorías de Naciones Unidas, agencias multilaterales): Evaluaciones formales sobre el impacto del embargo estadounidense (Alena Douhan) contrastadas con denuncias de inseguridad alimentaria y privación material (Relatoría del Derecho a la Alimentación).

### B. Arquitectura de Datos Desacoplada
Para evitar la manipulación de cifras en la interfaz y garantizar la reproducibilidad de los datos:
* Capa de datos estructurada: Los indicadores cuantitativos se almacenan de forma independiente en `data/indicadores.json`. Cada registro incluye su identificador, valor nominal, valor numérico, unidad, fuente primaria, referencia metodológica, fecha y grado de convergencia.
* Bitácora cronológica: Los hitos de la realidad se registran en `data/bitacora.json`, documentando fecha, categoría, fuentes primarias, contraste y su impacto directo sobre las hipótesis de la investigación.
* Capa de presentación: La interfaz web en `index.html` consume y refleja estos datos sin introducir métricas aisladas o desvinculadas de la base de verificación.

### C. Pipeline Automatizado de Auditoría Continua (CI/CD)
El repositorio incorpora un script de auditoría (`scripts/audit_claims.py`) integrado a los flujos de trabajo de GitHub Actions (`.github/workflows/audit-pipeline.yml`):
* Valida la sintaxis y los esquemas JSON de los datasets.
* Comprueba que cada afirmación numérica y cada hito contenga los metadatos de trazabilidad obligatorios.
* Audita la integridad textual y cruzada en el frontend para evitar discrepancias entre los datos certificados y la narrativa pública.

### D. Criterios Popperianos de Falsación (Falsifiability)
Toda hipótesis dentro del proyecto debe ser refutable. No se formulan dogmas cerrados:
* Hipótesis del Monopolio Militar y Captura de Rentas: Si se desmantelara el holding corporativo GAESA (desregulando el comercio exterior de insumos, permitiendo una banca comercial autónoma y liberando el tipo de cambio) y, aun así, la crisis de abasto y la escasez persistieran bajo libre iniciativa ciudadana, la hipótesis de la captura monopólica quedaría falsada.
* Hipótesis del Bloqueo Externo como Causa Exclusiva: Si el embargo y las sanciones de Estados Unidos fueran levantados en su totalidad y, sin embargo, la cúpula estatal mantuviera la asimetría interna de inversión (priorización de resorts vacíos frente a salud y agricultura, y prohibición del comercio exterior autónomo a campesinos), la tesis del bloqueo externo como causa única quedaría falsada.

---

## 3. Bitácora de Evidencia: Trazabilidad contra el Ruido Informativo

El proyecto no oculta los eventos que matizan sus premisas iniciales; los incorpora como hitos fechados en su bitácora viva:

1. Septiembre 2026: Sanciones del Departamento de Estado de EE. UU. (Marco Rubio / OFAC) contra el Banco Exterior de Cuba y la cúpula militar bajo la Orden Ejecutiva 14404. Intensifica el cerco financiero externo, aunque el régimen la utiliza para ocultar su desinversión interna.
2. Mayo 2026: Informe del Food Monitor Program ante la Relatoría Especial de la ONU sobre Alimentación (encuesta nacional de 2,703 hogares): 96% de pérdida de capacidad de compra y privación calórica severa.
3. Noviembre 2025: Filtración de balances internos de GAESA y auditoría de Pavel Vidal (elTOQUE / Columbia): Se corrige el peso de GAESA del mito del >70% al ~40% del PIB, verificando activos por $17,894M USD y depósitos bancarios retenidos por $14,467M USD.
4. Diciembre 2025: Interrupción de suministros petroleros de Venezuela y colapso del Sistema Electroenergético Nacional (SEN). Evidencia que factores físicos externos interactúan con la desinversión secular interna.
5. Febrero 2025: Cuba Siglo 21 y elTOQUE reportan que el 92.68% de las remesas ingresan por canales informales ante las tasas cambiarias oficiales distorsionadas.
6. 2024–2026: Anuarios de la ONEI analizados por Pedro Monreal demuestran que los hoteles de GAESA operan al 25%–30% de ocupación pese a recibir hasta 14 veces más inversión que la agricultura nacional.
7. 2025–2026: Investigación de Casa Palanca y Cubadata (La privatización silenciosa): Encuesta a 2,141 personas en toda la isla revela que el 74.3% paga por atención médica o fármacos formalmente gratuitos, el 78% recurre a influencias personales (palancas) y el 52.2% desiste de tratarse por falta de recursos económicos.

---

## 4. Datos Cuantitativos y Métricas Clave

| Indicador | Magnitud | Fuente Primaria y Metodología | Nivel de Convergencia |
|---|---|---|---|
| Pérdida de capacidad de compra de alimentos esenciales | 96% | Food Monitor Program (Encuesta a 2,703 hogares) | Alta |
| Desplome de producción agrícola nacional (último lustro) | 67% | FMP / Infobae (Mayo 2026) | Media-Alta (convergencia con acopio ONEI) |
| Dependencia de alimentos importados sobre el consumo nacional | 80% | FMP / Martí Noticias / ONEI 2026 | Máxima (reconocido oficialmente) |
| Peso macroeconómico real de GAESA (balances auditados vs. exilio) | 40% vs. >70% | Balances filtrados GAESA (Pavel Vidal / elTOQUE) vs. Havana Consulting | Señal crítica contrastada |
| Reservas líquidas y depósitos en el Banco Financiero Internacional | $14,467M USD | Balances internos de GAESA (Marzo 2024) / elTOQUE | Alta (evidencia contable primaria) |
| Ingresos de GAESA frente al presupuesto tributario del Estado | 3.2x | Balances contables de GAESA / elTOQUE (Noviembre 2025) | Alta |
| Tasa promedio de ocupación hotelera en instalaciones de GAESA | 25% – 30% | ONEI / Análisis de Pedro Monreal (2024-2026) | Máxima (estadística oficial comprobada) |
| Remesas familiares desviadas al mercado cambiario informal | 92.68% | Cuba Siglo 21 / elTOQUE (Febrero 2025) | Máxima (brecha cambiaria abierta) |
| Población que paga por salud o fármacos formalmente gratuitos | 74.3% | Casa Palanca / Cubadata (Encuesta a 2,141 ciudadanos) | Alta (metodología probabilística) |
| Ciudadanos que desisten de recibir atención médica por falta de recursos | 52.2% | Casa Palanca / Cubadata (2025-2026) | Alta (ruptura de universalidad) |
| Hogares donde al menos un miembro se acuesta con hambre | 33.9% | Food Monitor Program (2024-2026) | Alta |
| Caída del volumen total de remesas en 2024 (-70% frente a 2019) | 43% | Cuba Siglo 21 (Febrero 2025) | Alta |

---

## 5. Estructura del Repositorio

```
Cuba-Narratives/
|
|-- README.md                    Documentacion metodologica, fuentes y guia de auditoria
|-- Fuentes.md                   Matriz exhaustiva de sesgos declarados y marco epistemologico
|-- LECCIONES.md                 Directrices de UX, accesibilidad (a11y) y carga cognitiva
|
|-- index.html                   Infografia interactiva bilingue (ES/EN)
|-- cuba-monopolio.html          Archivo historico y redireccion
|
|-- data/
|   |-- indicadores.json         Metricas cuantitativas estructuradas y trazables
|   `-- bitacora.json            Registro cronologico de hitos y ajustes de hipotesis
|
|-- scripts/
|   `-- audit_claims.py          Auditor automatico de consistencia de datos y textos
|
`-- .github/workflows/
    |-- deploy.yml               Despliegue continuo en GitHub Pages
    `-- audit-pipeline.yml       Pipeline de verificacion y prueba de esquemas JSON
```

---

## 6. Estado del Proyecto y Hoja de Ruta

El proyecto opera como un sistema continuo y modular:

* Estado actual: Desacoplamiento de datos completado (`data/`), integración de auditoría CI/CD funcional, módulo interactivo de bitácora desplegado y trazabilidad de indicadores verificada.
* Siguiente fase: Automatización de alertas para nuevas filtraciones contables y reportes de organismos internacionales, y estandarización del pipeline para investigaciones comparadas multicaso en la región.

---

## 7. Declaración de Independencia y Licencia

Este repositorio produce investigación periodística, económica e intelectual. No representa a ningún partido, gobierno o grupo de interés. Todas las fuentes se identifican de forma abierta para que auditores externos puedan replicar, refutar o matizar las conclusiones.

Licencia: Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0).
