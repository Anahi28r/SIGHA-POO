# SIGHA — primera versión de la aplicación

## Abrir

Extrae el ZIP completo y abre `index.html` con Chrome, Edge o Firefox. Funciona sin instalar programas y sin internet.

## Qué tiene esta versión

- Panel general con cantidades reales de clases, docentes, aulas y cursos.
- Resumen de asignaciones y distribución de horas por día.
- Pantallas para registrar, buscar, editar y eliminar docentes, asignaturas, aulas y cursos.
- Formulario para programar y editar clases.
- Horario semanal filtrado por curso, docente o aula.
- Validación de cruces antes de guardar: mismo docente, aula o curso en intervalos que se superponen.
- Restricción para eliminar un recurso que tenga clases asignadas.
- Guardado local en el navegador, cuando esté disponible.
- Exportación de la planificación a un archivo JSON. Esta versión exporta; todavía no permite importar.

El usuario mostrado en la cabecera representa el rol de planificación. No es una cuenta autenticada ni una sesión de acceso.

## Cómo mostrarla mañana

1. Abre el panel general y explica qué representan sus cantidades.
2. En Docentes, registra un docente de ejemplo con un código que no exista. Observa que aparece en la lista. También puedes editarlo o buscarlo.
3. En Horarios, pulsa «Programar clase». Verás al nuevo docente entre las opciones.
4. Para comprobar la validación con los datos iniciales, selecciona Programación Orientada a Objetos, Ana Mendoza, TI · 2.º A, Aula 101, Lunes, de 08:00 a 09:00. Al guardar, aparecerá un cruce: ya hay una clase con esa docente y ese curso el lunes de 08:00 a 10:00. No se añade la asignación inválida.
5. Cambia el horario de esa propuesta al lunes de 10:00 a 11:00. Con los datos iniciales ese bloque está libre y se puede guardar.
6. Revisa la nueva clase en la consulta del curso TI · 2.º A. Haz clic sobre ella para editarla o eliminarla.
7. Regresa al panel para mostrar que se actualizó la cantidad de clases.
8. En «Acerca de esta versión» puedes explicar las próximas etapas.

El recorrido depende de que esos bloques sigan libres. Si ya creaste otras clases, elige un bloque libre o elimina únicamente tus asignaciones de ensayo.

## Cómo explicarla con honestidad

«Este es el avance funcional de SIGHA. Ya podemos organizar recursos, programar clases y consultar el horario. El sistema valida los cruces antes de guardar. Actualmente trabaja con datos de muestra y almacenamiento en este navegador. En las próximas etapas completaremos la gestión de estudiantes, las reglas de disponibilidad docente y carga semanal, y la conexión con una base de datos compartida».

Las funciones de esta aplicación son un nuevo avance preparado a partir de la propuesta. Antes de presentarlas, tu equipo debe revisarlas y comprenderlas. No significan que todas las funcionalidades del informe estuvieran implementadas anteriormente.

## Qué queda pendiente

- Registro de estudiantes y su relación con cursos.
- Disponibilidad de cada docente y carga semanal por asignatura.
- Comprobación de capacidad de aulas contra cantidad de estudiantes.
- Base de datos compartida y acceso desde varios equipos.
- Autenticación y permisos de usuarios.
- Diagrama de clases completo y entidades independientes para los catálogos.

La asignación de horarios es manual. No se genera un horario automáticamente. No incluye matrícula, notas, pagos ni asistencia.

## Programación orientada a objetos

En el código del archivo hay dos clases:

- `Horario`: representa una asignación y protege su información con el campo privado `#datos`. Expone los métodos `datos()` y `coincideCon()`.
- `GestorHorarios`: administra objetos Horario con el campo privado `#items` y los métodos `listar()`, `guardar()` y `eliminar()`. Comprueba los conflictos antes de modificar la colección.

Las asignaturas, docentes, aulas y cursos tienen identificadores y se relacionan con las asignaciones. Sus catálogos todavía son objetos de datos, no clases de dominio independientes; pueden convertirse en esas clases al refinar el modelo.

La interfaz utiliza HTML, CSS y JavaScript. Si el docente exige otro lenguaje o una estructura específica, será necesario adaptar esta implementación.

## Datos y verificación

Los datos iniciales son ficticios. No hay conexión con los sistemas de una universidad.

El almacenamiento depende del navegador: no se comparte entre equipos ni entre navegadores, y puede perderse si borras sus datos o cambias la ubicación del archivo. El pie de página avisa si no se puede guardar. «Exportar datos» descarga una copia legible de los registros.

La sintaxis del código y 14 comprobaciones de la lógica de horarios pasaron, incluyendo los tres tipos de cruce, límites de horas, clases consecutivas, edición y eliminación. El archivo también se sirvió correctamente mediante HTTP (respuesta 200).

La política de seguridad del navegador de esta sesión impidió inspeccionar la vista previa. Por eso no se ha completado una comprobación visual ni de todos los formularios en un navegador. Ensaya el recorrido anterior en el equipo que utilizarás para exponer.
