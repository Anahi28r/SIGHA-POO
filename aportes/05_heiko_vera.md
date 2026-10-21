# Aporte propuesto de Heiko Marcelo Vera Ponce

## Consultas de horarios con abstracción y polimorfismo

Esta propuesta forma parte de la distribución de ideas para el equipo. Su implementación corresponde a una etapa posterior al informe y al UML inicial.

### Mi propuesta

Propongo organizar las consultas de horarios mediante una operación común que pueda trabajar con distintos criterios. Mi idea es consultar por docente o por curso sin tener que repetir toda la lógica que presenta los resultados.

### Relación con lo aprendido en clase

La práctica de una base abstracta con distintas implementaciones y el repaso del examen permiten plantear un contrato de consulta. El polimorfismo haría posible utilizar la misma operación con comportamientos distintos, mientras un servicio recibiría el objeto de consulta que debe emplear.

### Relación con nuestro informe y UML

Nuestro informe contempla consultar horarios por curso, docente o aula, y el UML incluye consultarHorario() en Curso y Estudiante. Propongo desarrollar esa funcionalidad con una abstracción para las consultas, como una ampliación del diseño actual.

### Desarrollo que planteo

Planteo una clase abstracta ConsultaHorario con un método consultar(), y variantes concretas para docente y curso. Un servicio utilizaría cualquiera de esas variantes. La consulta por aula podría incorporarse siguiendo el mismo criterio. Del ejercicio de pagos aprovecharíamos la estructura de programación, sin añadir pagos a SIGHA.

### Cómo comprobaré la propuesta

La propuesta se podrá comprobar utilizando datos de distintos cursos y docentes. Cada consulta deberá devolver únicamente las asignaciones del recurso seleccionado; si no tiene clases, el resultado deberá estar vacío.

### Beneficio para SIGHA

Mi aporte busca organizar la consulta y facilitar su ampliación sin duplicar el código que muestra la planificación.
