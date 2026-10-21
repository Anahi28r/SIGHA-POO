# Aporte propuesto de Jeremy Jair Eduarte Lopez

## Definición de los recursos académicos como objetos

Esta propuesta forma parte de la distribución de ideas para el equipo. Su implementación corresponde a una etapa posterior al informe y al UML inicial.

### Mi propuesta

Propongo detallar las clases que representan los recursos de SIGHA y precisar qué información y operaciones corresponde a cada una. Mi idea es que los datos de docentes, estudiantes, asignaturas, aulas y cursos mantengan una estructura coherente.

### Relación con lo aprendido en clase

Las prácticas de clases y objetos permiten pasar de una descripción general a un modelo con atributos y métodos. El constructor inicializaría cada recurso y self permitiría trabajar con los datos de una instancia concreta. También debemos diferenciar los datos individuales de los que realmente corresponden a la clase.

### Relación con nuestro informe y UML

Nuestro informe y el UML ya identifican Docente, Estudiante, Asignatura, Aula y Curso. Sobre esa base, propongo revisar los tipos de sus atributos y los parámetros de sus métodos, como actualizarDatos(), consultarCapacidad() y consultarHorasSemanales().

### Desarrollo que planteo

Planteo preparar ejemplos de objetos con datos ficticios y definir operaciones para consultar o actualizar cada recurso. Evitaría usar atributos compartidos para datos que cambian entre docentes, estudiantes o aulas.

### Cómo comprobaré la propuesta

La propuesta se podrá comprobar creando dos objetos de una misma clase y verificando que conservan datos distintos. Actualizar un recurso no deberá cambiar los atributos individuales de otro.

### Beneficio para SIGHA

Mi aporte busca que el modelo de SIGHA sea claro y que sus recursos se puedan relacionar sin duplicar información innecesaria.
