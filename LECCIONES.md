# 💡 Guía de Lecciones Aprendidas: UX, Accesibilidad y Carga Cognitiva

Este documento recopila las directrices y lecciones aprendidas durante la sesión de refactorización del proyecto. Debe servir como marco de referencia para futuras investigaciones y desarrollos en plataformas de análisis visual y scrollytelling.

---

## 🧠 1. Reducción de la Carga Cognitiva

### Evitar el "Ruido" de la Gamificación Explícita
- **Lección:** Las mecánicas de gamificación excesivamente explícitas (como carteles de `🔓 LOGRO DESBLOQUEADO (Nivel X/5)`) pueden restar seriedad académica y saturar visualmente al lector en investigaciones de crisis humanitarias o temas complejos.
- **Directriz:** Los logros y el progreso deben ser **implícitos**. El lector debe sentir el avance a través de la narrativa visual y el flujo de scroll, sin necesidad de banners intrusivos de recompensa.

### Minimizar Notas Internas (Meta-labels)
- **Lección:** Etiquetas como `💡 AUTOPREGUNTA DE RETENCIÓN (Active Recall)` actúan como notas internas que interrumpen la inmersión del lector en el contenido.
- **Directriz:** La estructura de interacción (como tarjetas de preguntas y respuestas) debe hablar por sí sola. Basta con presentar la pregunta de forma directa para invitar a la reflexión, reduciendo la fricción conceptual del "cómo debe estudiar" el lector.

---

## 🎨 2. UX/UI Inmersiva y Orientada al Valor

### Claridad en la Propuesta de Valor del Hero
- **Lección:** El subtítulo del Hero no debe enfocarse tanto en la mecánica del desarrollo (*"un análisis metodológico interactivo que..."*), sino en el valor directo y el propósito de la investigación (*"desglosar el espectro de narrativas detrás de la crisis..."*).
- **Directriz:** Comunicar primero el **qué** y el **por qué** (el impacto de la investigación) antes de detallar el **cómo** (la metodología interactiva).

### Limpieza Visual en Tarjetas de Apoyo
- **Lección:** Las tarjetas de interacción (como las de autoevaluación o notas de datos) deben mantener la máxima sobriedad para destacar el contenido textual.
- **Directriz:** Preservar bordes acentuados elegantes (ej. `border-left: 4px solid var(--accent)`) y contrastes sutiles de fondo, pero retirar emojis y subtítulos redundantes en la parte superior del componente.

---

## ♿ 3. Accesibilidad e Internacionalización (a11y & i18n)

### Localización Terminológica y Evitación de Anglicismos
- **Lección:** El uso de anglicismos académicos como *Rent-Seeking* incrementa la fricción y la exclusión para el lector hispanohablante promedio, restando naturalidad al análisis.
- **Directriz:**
  - En las versiones en español, traducir los conceptos a su equivalente natural en nuestro idioma (**"Búsqueda de rentas"**).
  - Si el término técnico en inglés es sumamente específico de la literatura, introducirlo entre paréntesis `(Rent-Seeking)` únicamente en la primera mención o en el marco metodológico.
  - Mantener los términos originales exclusivamente en la versión internacional en inglés (`en`) para el público global.

### Limpieza de Código para Lectores de Pantalla (Screen Readers)
- **Lección:** La acumulación de emojis no semánticos y textos puramente mecánicos en etiquetas de accesibilidad distorsiona la lectura secuencial de los lectores de pantalla.
- **Directriz:** Mantener el marcado HTML limpio y semántico. Si se usan emojis como decoraciones visuales, estos no deben entorpecer el orden de lectura principal o deben ocultarse mediante atributos `aria-hidden="true"`.
