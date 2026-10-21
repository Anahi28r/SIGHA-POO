# SIGHA · Informe UML y aportes del equipo

Nuestro proyecto busca apoyar la organización de horarios académicos y reducir los cruces de docentes, aulas y cursos. El avance que hemos construido en conjunto está formado por la definición del proyecto y el diagrama UML inicial.

## Avance actual

- Definición de la problemática, alcance y funcionalidades en el informe.
- Identificación de entidades y relaciones en el UML inicial.
- Propuestas para aplicar los temas de clase al desarrollo del sistema.

Este paquete se concentra en esos documentos y en las cinco ideas. El desarrollo de las propuestas corresponde a la siguiente etapa del proyecto.

## Propuesta de distribución de los aportes

El trabajo previo se ha realizado en conjunto. Para organizar las contribuciones individuales, proponemos el siguiente reparto de ideas. Este reparto no atribuye una implementación que ya haya realizado cada integrante.

| Integrante | Propuesta | Documento |
| --- | --- | --- |
| Ian Rafael Avila Delgado | Organización del horario semanal | [Leer aporte](aportes/01_ian_avila.md) |
| Jeremy Jair Eduarte Lopez | Definición de los recursos académicos como objetos | [Leer aporte](aportes/02_jeremy_eduarte.md) |
| Jose Gabriel Intriago Cedeño | Validación de las asignaciones y detección de cruces | [Leer aporte](aportes/03_jose_intriago.md) |
| Anahi Carolina Robayo Tuarez | Reutilización de los datos comunes mediante herencia | [Leer aporte](aportes/04_anahi_robayo.md) |
| Heiko Marcelo Vera Ponce | Consultas de horarios con abstracción y polimorfismo | [Leer aporte](aportes/05_heiko_vera.md) |

Cada documento está redactado en primera persona y expresa una propuesta de desarrollo. Cada integrante podrá revisarla, adaptarla y subir su contribución desde su propia cuenta.

## Aplicación de las prácticas

### Fundamentos de Python

En las primeras prácticas trabajamos tipos de datos, entrada por teclado, listas, matrices, arrays, funciones, condicionales y bucles. Para SIGHA proponemos utilizar estas bases para organizar días y periodos, recorrer asignaciones y preparar consultas. No es necesario trasladar todas las herramientas al proyecto: las listas pueden ser suficientes para una representación inicial.

### Clases objetos y encapsulamiento

Las prácticas de clases permiten representar los elementos del proyecto mediante atributos, constructores y métodos. En el diseño de SIGHA identificamos docentes, estudiantes, asignaturas, aulas y cursos. A partir del encapsulamiento, proponemos controlar sus actualizaciones con operaciones que revisen los datos antes de modificarlos, diferenciando atributos individuales de los compartidos por una clase.

### Herencia y reutilización

Estudiamos cómo una clase hija puede reutilizar datos y métodos de una base y ampliar su comportamiento. Para SIGHA proponemos revisar los elementos comunes de Docente y Estudiante y considerar Persona como base. Esta mejora se incorporaría a nuestro UML cuando revisemos la estructura de esas clases.

### Abstracción y polimorfismo

Estudiamos bases abstractas, métodos requeridos e implementaciones distintas utilizadas mediante una operación común. Para SIGHA proponemos aplicar esa estructura a las consultas de horarios. El ejercicio de pagos sirve para comprender la estructura de programación; no amplía el alcance del proyecto con una función de pagos.

## Documentos

- [Informe de SIGHA](docs/INFORME_SIGHA.pdf).
- [UML inicial](docs/UML_SIGHA.pdf).

Los dos PDF originales conservan su contenido y la carátula del grupo. 

## Próximos pasos

Revisaremos el reparto de ideas, ajustaremos el UML según las decisiones que adoptemos y desarrollaremos las propuestas de forma gradual. Cada avance deberá indicar qué se implementó y cómo se comprobó. Pagos, calificaciones, asistencia y matrícula administrativa permanecen fuera del alcance definido.
