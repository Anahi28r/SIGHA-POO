# SIGHA · Aprendizaje de Programación Orientada a Objetos

Repositorio académico para reunir las prácticas de Python, documentar lo aprendido y aplicar sus conceptos al **Sistema de Gestión de Horarios Académicos (SIGHA)**.

**Estado:** definición del proyecto, UML inicial, prácticas originales y una integración inicial revisada. No es el sistema terminado.

## ¿Qué problema resuelve SIGHA?

La planificación manual puede asignar el mismo docente o aula a dos clases simultáneas, o superponer asignaturas de un mismo curso. SIGHA propone organizar los recursos, elaborar horarios y detectar esos conflictos antes de aceptar una asignación.

El alcance del informe incluye estudiantes, docentes, asignaturas, aulas, cursos y horarios. Matrícula administrativa, calificaciones, asistencia y pagos quedan fuera del proyecto.

## Aportes de los cinco integrantes

El repositorio también debe mostrar las ideas individuales del equipo. Se prepararon [cinco propuestas para repartir y revisar](aportes/README.md), con su relación con las prácticas, aplicación en SIGHA y comprobación sugerida.

Cada integrante debe completar su autoría, adaptar la idea y registrar lo que realmente hizo. Las fichas son propuestas; todavía no acreditan una entrega individual de cinco personas. Para el examen se incluye un [repaso desde los fundamentos hasta abstracción y polimorfismo](aportes/REPASO_APORTES.md).

## Del ejercicio de clase al proyecto

| Práctica | Evidencia existente | Aprendizaje | Aplicación preparada para SIGHA |
| --- | --- | --- | --- |
| 1 | Datos primitivos, entrada, listas, matrices, NumPy, funciones y bucles | Organizar y recorrer información | Representar una semana como periodos y días |
| 2 · clases | Docente, Estudiante, Asignatura, Curso y Aula; métodos de instancia, clase y estáticos | Diferenciar `self`, `cls` y operaciones independientes | Crear recursos académicos y consultar sus datos |
| 2 · encapsulamiento | Atributos con doble guion bajo y métodos de consulta y actualización | Controlar cambios de estado | Rechazar una capacidad de aula inválida mediante un método |
| 3 | Herencia simple, multinivel y múltiple; `super()` | Reutilizar atributos y revisar relaciones «es un» | Persona → Docente / Estudiante; Aula → LaboratorioTI como extensión opcional |
| 4 | PasarelaDePago, Paypal, Stripe y ServicioDeCaja | Abstracción, sobrescritura, polimorfismo y composición | Consultas intercambiables por curso y docente, sin agregar pagos al proyecto |

La explicación detallada está en [Relación entre prácticas y SIGHA](docs/RELACION_PRACTICAS_SIGHA.md).

## Organización

```text
SIGHA-POO/
├── README.md
├── practicas/originales/       # Archivos de clase conservados sin cambios
│   ├── 01/
│   ├── 02/                    # Dos variantes de la práctica 2
│   ├── 03/
│   └── 04/
├── aportes/                   # Cinco propuestas individuales y plantilla
├── aplicaciones/              # Aplicación explicada de cada práctica a SIGHA
├── sigha/                     # Modelo inicial en Python y demostración
├── prototipo-web/             # Interfaz HTML/JS independiente
├── docs/
│   ├── documentos/            # Informe, UML, guías y carátula recibidos
│   ├── RELACION_PRACTICAS_SIGHA.md
│   ├── REVISION_CODIGO.md
│   ├── BITACORA.md
│   └── COMO_SUBIR_A_GITHUB.md
└── tests/                     # Verificación del modelo integrado
```

## Ejecutar la integración

Requiere **Python 3.10 o posterior**, sin paquetes externos. Abre una terminal dentro de esta carpeta:

```console
python -m sigha.demo
```

La demostración crea objetos de ejemplo, relaciona un estudiante con un curso, registra una clase, rechaza una asignación que produce cruces y acepta una corrección con un bloque consecutivo.

Ejecutar las aplicaciones de cada práctica:

```console
python -m aplicaciones.practica_01
python -m aplicaciones.practica_02
python -m aplicaciones.practica_03
python -m aplicaciones.practica_04
```

Pruebas:

```console
python -m unittest discover -s tests -v
```

La práctica 1 **original** utiliza NumPy y pide datos por teclado; sus requisitos están en `requirements-originales.txt`. Los ejemplos nuevos no necesitan NumPy.

## Conceptos visibles en el código

- **Abstracción:** `Persona` define `realizar_actividad()` como método abstracto.
- **Encapsulamiento:** nombre, identificación, capacidad y límites de periodo se consultan o actualizan mediante métodos y propiedades.
- **Herencia:** `Docente` y `Estudiante` heredan de `Persona` y reutilizan su constructor con `super()`.
- **Polimorfismo:** el mismo método `realizar_actividad()` tiene respuestas diferentes; las consultas usan una operación común.
- **Relaciones entre objetos:** `Horario` relaciona `Periodo`, `Asignatura`, `Docente`, `Aula` y `Curso`.
- **Reglas del dominio:** hay cruce si coinciden el día, intervalos superpuestos y al menos un recurso: docente, aula o curso.

El modelo base contiene ocho clases: Persona, Docente, Estudiante, Asignatura, Aula, Curso, Periodo y Horario. La aplicación 3 añade LaboratorioTI como extensión y la aplicación 4 introduce las clases de consulta; esas extensiones no forman parte de la cuenta de ocho.

## Qué funciona y qué está pendiente

| Parte | Estado |
| --- | --- |
| Prácticas originales | Conservadas; la práctica 3 tiene errores documentados |
| Integración Python | Ejemplo en memoria, con clases y detección de conflictos |
| Relación estudiante–curso | Ejemplo en memoria, sin matrícula administrativa |
| Interfaz web | Prototipo independiente con su propio almacenamiento local |
| Conexión web–Python | Pendiente |
| Base de datos compartida, cuentas y permisos | Pendiente |
| Disponibilidad docente, carga semanal y capacidad frente al tamaño del curso | Pendiente |

Para abrir la interfaz, haz doble clic en [prototipo-web/index.html](prototipo-web/index.html) desde la carpeta descargada. No es necesario publicar una web para documentar las prácticas en GitHub.

## Evidencias y autoría

Los cinco archivos Python originales y los documentos de clase se conservan con sus nombres y contenido. Sus rutas y huellas están en [el inventario](docs/inventario_originales.json). Las prácticas identifican a Anahí Robayo en sus nombres; los integrantes del proyecto figuran en la carátula del informe.

Las carpetas `sigha/`, `aplicaciones/`, `tests/` y esta documentación contienen una **integración y revisión nueva preparada con asistencia de IA** a partir del material recibido. No deben presentarse como archivos históricos de clase sin cambios. Revisa y comprende cada ejemplo antes de incorporarlo a la entrega.

No se han inventado fechas de clases, aportes de integrantes ni un historial de commits. Completa [la bitácora](docs/BITACORA.md) con las fechas y evidencias reales del grupo.

## Crear el repositorio en GitHub

Sigue [la guía paso a paso](docs/COMO_SUBIR_A_GITHUB.md). Nombre sugerido: **SIGHA-POO**.

El repositorio reúne el proceso de aprendizaje; el informe es uno de sus documentos. La consigna adicional de relacionar prácticas y proyecto se incorpora según lo explicado por la estudiante en esta conversación.
