# Revisión de las prácticas originales

Los archivos de `practicas/originales/` se conservaron sin cambios. Las correcciones se reflejan en ejemplos nuevos; no sustituyen la evidencia original.

## Práctica 1

Se requiere NumPy y cuatro entradas: nombre, edad, opción del 1 al 3 y día del 1 al 7. Una entrada no numérica donde se usa `int(input(...))` puede provocar ValueError. Es una mejora futura para la captura de datos, no un impedimento para estudiar listas y bucles.

El comentario «Switch (Case)» describe una selección simulada con `if/elif/else`.

## Práctica 2

Hay dos archivos con numeración 2. Se conservaron ambos para no eliminar evidencia ni inventar su orden cronológico.

La variante con atributos privados define las clases pero no incluye un recorrido final que cree objetos y pruebe sus métodos. Puede terminar sin imprimir nada y eso no significa que el archivo tenga un error.

En la variante con atributos de clase, cambiar `Estudiante.estado` afecta la consulta del atributo compartido de sus instancias mientras no tengan un atributo de instancia con ese mismo nombre. Para SIGHA, la disponibilidad y los datos individuales deben mantenerse por objeto.

## Práctica 3

| Hallazgo | Consecuencia | Criterio aplicado en la integración |
| --- | --- | --- |
| Aula, Persona, Docente y Estudiante se definen varias veces | El nombre global termina apuntando a la última definición; se mezclan ejemplos distintos | Una sola definición base por entidad |
| `def mostar(...)` aparece dentro de `__init__` | Se crea una función local, no un método accesible por el objeto | Métodos al mismo nivel de indentación que `__init__` |
| Estudiante hereda de Docente en una sección | La relación no representa el dominio de SIGHA | Docente y Estudiante heredan de Persona |
| El constructor de esa Estudiante omite disponibilidad al llamar a la clase base | Esa versión fallaría al instanciarse | Ajustar la jerarquía y pasar los argumentos requeridos |
| Asistente usa un único `super().__init__` con argumentos de ambos padres, pero Docente no acepta todos ellos | La creación de Asistente falla con TypeError | No forzar herencia múltiple; si se mantiene como ejercicio, diseñar constructores cooperativos compatibles con el MRO |
| Inscripcion incluye calificación y asistencia | Amplía el sistema fuera del alcance del informe | Mantenerlo como ejercicio académico; usar asociación estudiante–curso en SIGHA |

Un archivo puede pasar la revisión sintáctica y aun así fallar en ejecución. Aquí el error del constructor de Asistente es de ejecución, no de sintaxis.

## Práctica 4

El ejercicio ilustra una abstracción y dos implementaciones concretas. Para SIGHA se adaptó ese patrón a la consulta por recursos, sin añadir pagos.

## UML y modelo integrado

El UML recibido conserva las entidades del informe, incluido Periodo, y se guarda junto con su fuente drawio. El modelo integrado reutiliza esos conceptos y propone Persona como base abstracta de Docente y Estudiante.

Esta propuesta de herencia debe reflejarse en una futura revisión del UML si el grupo decide adoptarla. El PDF original no se modificó ni se presenta como si ya incluyera ese cambio.

El archivo drawio contiene un elemento cuyo texto incluye XML; conviene abrirlo y revisar su apariencia antes de actualizar el diagrama. No se ha declarado una validación visual de ese archivo.
