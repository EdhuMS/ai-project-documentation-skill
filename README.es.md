# AI Project Documentation Skill

**Documentación portable de proyectos de software y continuidad verificable entre agentes de IA.**

[![Versión](https://img.shields.io/badge/versión-v0.1.0-blue)](https://github.com/EdhuMS/ai-project-documentation-skill/releases)
[![Licencia MIT](https://img.shields.io/badge/licencia-MIT-green)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/formato-Agent%20Skills-blueviolet)](https://agentskills.io/specification)

**Idiomas:** [English](README.md) | **Español**

> **Estado:** versión pública inicial (v0.1.0). Incluye instrucciones de skill, plantillas, herramienta local en Python y pruebas unitarias. No se ha comprobado su funcionamiento en todos los agentes ni en todas las plataformas de almacenamiento.

## ¿Qué es?

AI Project Documentation Skill es una **skill de código abierto** para ayudar a desarrolladores y agentes de IA a mantener documentación técnica, conservar decisiones y continuar proyectos después de cambiar de sesión, conversación o agente.

En lugar de depender de un resumen que podría estar desactualizado, propone registrar **qué se desarrolló, qué se verificó, qué decisiones se tomaron y cuál es el siguiente paso**. Antes de continuar, el nuevo agente debe contrastar la información con el código y las evidencias disponibles.

### ¿Qué problema resuelve?

En proyectos que duran semanas o meses, un agente puede perder el contexto original. Eso puede provocar trabajo repetido, decisiones contradictorias o que una tarea se dé por terminada sin pruebas. Esta skill establece un protocolo de continuidad para reducir esos riesgos; **no garantiza que el agente recuerde automáticamente sesiones anteriores**.

## Funcionalidades

- **Continuidad entre agentes:** handoffs (entregas de contexto) con estado, decisiones, pruebas, bloqueos y próxima acción.
- **Independencia del proveedor:** documentación en archivos Markdown/JSON, sin obligar al usuario a utilizar Google Drive, GitHub ni ningún servicio de nube.
- **Tres niveles documentales:** ligero, profesional y crítico, según el tamaño y riesgo del proyecto.
- **Trazabilidad basada en evidencias:** distingue información verificada, reportada, inferida y desconocida.
- **Plantillas:** estado del proyecto, decisiones arquitectónicas (ADR) y handoffs.
- **Seguridad:** lectura como punto de partida cuando el permiso es incierto; las publicaciones, fusiones, eliminaciones y otras operaciones sensibles requieren autorización.
- **CLI local:** comandos básicos para inicializar documentación y validar el archivo de estado utilizando Python.

## Requisitos

Para utilizar las instrucciones necesitas un asistente capaz de leer archivos Markdown o compatible con el formato [Agent Skills](https://agentskills.io/specification).

**Python 3.9 o superior** es opcional y solamente se necesita para ejecutar la herramienta local. No se requieren dependencias de Python de terceros.

## Instalación

### Opción 1. Agentes compatibles con Agent Skills

1. Descarga el código desde [GitHub](https://github.com/EdhuMS/ai-project-documentation-skill) o clona el repositorio:

   ```bash
   git clone https://github.com/EdhuMS/ai-project-documentation-skill.git
   ```

2. Copia la **carpeta completa** del repositorio al directorio de skills que admita tu agente. Deben conservarse `SKILL.md`, `references/` y `templates/`.
3. Actualiza o reinicia el descubrimiento de skills, si tu aplicación lo requiere.
4. Comprueba que el agente puede acceder a las instrucciones y solicita su uso.

> La ruta de instalación cambia según el agente y el entorno. Esta versión no incorpora un instalador universal ni garantiza la activación automática en ChatGPT, Codex, Claude, Gemini u otros productos.

### Opción 2. Uso manual

Si tu asistente no admite instalación de skills, abre `SKILL.md`, comparte sus instrucciones con el agente y proporciona los documentos pertinentes de `references/`. La herramienta solo podrá leer o modificar archivos para los que realmente tenga acceso y permisos.

### Opción 3. Documentación local sin servicios externos

Desde la carpeta descargada del repositorio, abre una terminal y ejecuta:

```bash
python scripts/pdc.py init /ruta/a/mi-proyecto --project-id mi-proyecto
```

El comando crea la documentación ligera en `/ruta/a/mi-proyecto/docs/continuity/` y evita sobrescribir una carpeta de documentación que ya contenga archivos.

Valida el estado del proyecto mediante:

```bash
python scripts/pdc.py validate /ruta/a/mi-proyecto/docs/continuity/PROJECT-STATE.json
```

En Windows puedes utilizar `py` en lugar de `python` cuando esa sea la configuración de tu equipo. Sustituye la ruta de ejemplo por la de tu proyecto real.

## ¿Cómo usar la skill?

### Caso 1. Retomar un proyecto

> Usa AI Project Documentation Skill en modo lectura. Revisa el código, la documentación y el último handoff. Comprueba la rama, los commits y las pruebas disponibles. Identifica el último hito real y el siguiente paso sin modificar archivos.

### Caso 2. Documentar avances

> Usa AI Project Documentation Skill con nivel profesional. Documenta el trabajo realizado, las decisiones, las pruebas ejecutadas y el siguiente hito. Solo puedes escribir en la carpeta de documentación que te autoricé.

### Caso 3. Transferir el proyecto a otro agente

> Prepara un handoff verificable con los cambios completados, su evidencia, las pruebas aprobadas, fallidas u omitidas, los riesgos y la próxima acción exacta. No inventes commits ni declares una versión finalizada sin comprobarla.

### Caso 4. Utilizar otra plataforma de almacenamiento

> Quiero almacenar mi documentación en [plataforma o carpeta]. Usa la skill, verifica si tienes acceso de lectura y escritura, define el lugar canónico de cada documento y propón los cambios antes de guardarlos.

## Niveles documentales

| Nivel | Recomendado para | Documentos habituales |
| --- | --- | --- |
| **Ligero** | Proyectos personales y prototipos | README, estado del proyecto y handoff |
| **Profesional** | Aplicaciones mantenidas y trabajo en equipo | Nivel ligero + requisitos, arquitectura, ADR, pruebas y changelog |
| **Crítico** | Sistemas con riesgos elevados o requisitos regulatorios | Nivel profesional + riesgos, trazabilidad, seguridad y evidencias de recuperación |

Los niveles son recomendaciones adaptables y no constituyen certificaciones de calidad o seguridad.

## Almacenamiento independiente

Los documentos se guardan en formatos abiertos **Markdown y JSON**. Cada documento debe tener una ubicación canónica; las copias adicionales pueden existir en otras plataformas, pero no deben sobrescribir silenciosamente versiones divergentes.

Puedes utilizar archivos locales, repositorios Git o servicios como Google Drive, OneDrive, Notion o GitLab **si tu agente dispone de las herramientas y los permisos correspondientes**.

**Limitación de v0.1.0:** todavía no existen adaptadores automáticos para sincronizar datos entre esas plataformas.

## Estructura del repositorio

```text
ai-project-documentation-skill/
├── README.md
├── README.es.md
├── SKILL.md
├── LICENSE
├── CHANGELOG.md
├── references/
├── templates/
├── examples/
├── docs/
│   ├── decisions/
│   └── releases/
├── scripts/
│   └── pdc.py
└── tests/
    └── test_pdc.py
```

## Pruebas y validación

Desde la raíz del repositorio:

```bash
python -m unittest discover -s tests -v
python scripts/pdc.py validate templates/PROJECT-STATE.json
```

Estas pruebas comprueban la herramienta local; **no validan automáticamente la calidad de todos los documentos ni la compatibilidad universal entre agentes**.

## Versiones y lanzamientos (Releases)

Las versiones oficiales se consultan en [GitHub Releases](https://github.com/EdhuMS/ai-project-documentation-skill/releases).

| Versión | Contenido |
| --- | --- |
| [v0.1.0](https://github.com/EdhuMS/ai-project-documentation-skill/releases/tag/v0.1.0) | Primera versión pública: protocolos portables, plantillas, handoffs verificables, CLI local y pruebas |

Puedes consultar los cambios en [CHANGELOG.md](CHANGELOG.md) y las [notas de la primera versión](docs/releases/v0.1.0.md).

> **Nota:** los archivos publicados después de crear el tag `v0.1.0`, incluida esta traducción, están disponibles en `main` y podrían no formar parte del archivo histórico de la release. No debe reescribirse silenciosamente un lanzamiento anterior.

## Límites y consideraciones de seguridad

- Una skill de instrucciones no reemplaza las políticas de seguridad y permisos del sistema anfitrión.
- El agente debe verificar las afirmaciones de otros agentes y documentos anteriores.
- No publiques contraseñas, información confidencial, datos de clientes ni expedientes privados.
- No des por ejecutadas pruebas que solo aparezcan descritas en un documento.
- La herramienta local no realiza despliegues, sincronización cloud ni operaciones de Git remotas.

## Colaboraciones

Se aceptan *issues* y *pull requests* con propuestas de mejora, errores reproducibles, nuevas traducciones y ejemplos genéricos. Evita compartir documentación privada o información real de clientes.

## Licencia y referencias

Las instrucciones, plantillas y el CLI mantenidos por este proyecto se distribuyen bajo la [licencia MIT](LICENSE). © 2026 EdhuMS. Esta licencia no concede derechos sobre marcas de terceros, documentación externa ni servicios enlazados. Tampoco implica certificaciones de seguridad o compatibilidad universal.

Referencias metodológicas: [Agent Skills](https://agentskills.io/specification), [Architecture Decision Records](https://adr.github.io/madr/), [Diátaxis](https://diataxis.fr/) y [Keep a Changelog](https://keepachangelog.com/).
