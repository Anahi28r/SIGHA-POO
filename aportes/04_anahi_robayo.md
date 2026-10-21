# Aporte propuesto de Anahi Carolina Robayo Tuarez

## Reutilización de los datos comunes mediante herencia

Esta propuesta forma parte de la distribución de ideas para el equipo. Su implementación corresponde a una etapa posterior al informe y al UML inicial.

### Mi propuesta

Propongo incorporar Persona como una clase base para Docente y Estudiante. Mi idea es reunir el nombre y la identificación que ambos comparten, y mantener en cada clase hija los datos que le corresponden.

### Relación con lo aprendido en clase

Las prácticas de herencia y el repaso de super() permiten reutilizar una inicialización común sin repetirla en cada clase. Una hija puede añadir atributos y definir su propia versión de un método cuando necesite un comportamiento diferente.

### Relación con nuestro informe y UML

En nuestro UML actual, Docente y Estudiante aparecen como clases independientes y comparten nombre e identificación. Persona sería una mejora propuesta al diseño, por lo que necesitaríamos actualizar el diagrama si el grupo adopta esta estructura.

### Desarrollo que planteo

Planteo ubicar los atributos comunes en Persona, hacer que Docente y Estudiante hereden de ella y reutilizar su constructor mediante super().__init__(). La disponibilidad permanecería en Docente y el correo y la relación con su curso se definirían para Estudiante.

### Cómo comprobaré la propuesta

La propuesta se podrá comprobar creando un docente y un estudiante, consultando los datos heredados y verificando sus datos específicos. No usaríamos una relación de herencia entre Estudiante y Docente, porque no representa el dominio.

### Beneficio para SIGHA

Mi aporte busca reducir la repetición del código y mantener una organización más clara de las clases del proyecto.
