# Aporte propuesto de Jose Gabriel Intriago Cedeño

## Validación de las asignaciones y detección de cruces

Esta propuesta forma parte de la distribución de ideas para el equipo. Su implementación corresponde a una etapa posterior al informe y al UML inicial.

### Mi propuesta

Propongo definir las reglas que deben cumplirse antes de aceptar una asignación de horario. Mi idea es impedir que un docente, aula o curso se utilice en dos clases que se superpongan, y que se registren periodos con horas incoherentes.

### Relación con lo aprendido en clase

El encapsulamiento nos ayuda a organizar las operaciones que consultan o modifican los datos. En lugar de cambiar una asignación sin control, planteo utilizar métodos que primero revisen sus condiciones. Los condicionales permitirían decidir si una propuesta se acepta o se rechaza.

### Relación con nuestro informe y UML

El UML ya propone detectarConflicto(otro: Horario) en Horario y seSuperponeCon(otro: Periodo) en Periodo. Mi aporte se centra en explicar y desarrollar esas responsabilidades, relacionando el día, las horas y los recursos de cada clase.

### Desarrollo que planteo

Planteo comprobar primero que la hora final sea posterior a la inicial. Después se compararía la nueva asignación con las existentes: habría conflicto cuando coincidieran el día, un intervalo superpuesto y el mismo docente, aula o curso. La validación se haría antes de guardar.

### Cómo comprobaré la propuesta

Con una clase el lunes de 08:00 a 10:00, otra de 09:00 a 11:00 con un recurso compartido deberá rechazarse. Una clase de 10:00 a 12:00 será consecutiva y podrá aceptarse. Una propuesta rechazada no deberá alterar la planificación.

### Beneficio para SIGHA

Mi aporte busca reducir errores y evitar cruces antes de establecer un horario definitivo.
