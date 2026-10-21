# Propuesta 3: validar antes de aceptar una asignación

**Autor:** por acordar con el grupo.  
**Usuario de GitHub:** por completar.  
**Fecha real del aporte:** por completar.  
**Estado de esta ficha:** propuesta inicial; ejemplo de apoyo preparado.

## Idea

Evitar que SIGHA acepte una clase con horas inválidas o con un cruce de docente, aula o curso. Las comprobaciones deben ocurrir antes de modificar la planificación.

## De dónde surge

La práctica 1 usa condicionales; la práctica 2 introduce atributos encapsulados y métodos de consulta y actualización. La aplicación combina esas ideas con las relaciones Horario–Periodo del proyecto.

## Aplicación al proyecto

[Periodo](../sigha/modelos.py) valida que el fin sea posterior al inicio y expone las horas mediante propiedades. `Horario.detectar_conflicto()` comprueba coincidencias. [agregar_horario()](../sigha/planificacion.py) rechaza la nueva asignación antes de añadirla a la lista.

## Qué puede aportar el integrante

Documentar los tres tipos de cruce y preparar un caso para cada uno. Explicar qué dato se controla mediante métodos o propiedades y verificar que una asignación rechazada no se guarda.

## Cómo comprobarlo

Desde la raíz: `python -m sigha.demo`.

Con una clase el lunes de 08:00 a 10:00:

- Una clase de 09:00 a 11:00 con el mismo docente, aula o curso debe rechazarse.
- Una clase de 10:00 a 12:00 puede usar esos recursos porque es consecutiva.
- Una clase en otro día no produce un cruce temporal con la del lunes.

**Resultado observado por el autor:** por completar después de ejecutar.

## Para explicarlo en clase

- Encapsular consiste en organizar el acceso y las operaciones sobre los datos, no solo en escribir guiones bajos.
- Una propiedad sin setter evita la asignación directa a esa propiedad desde el uso habitual del objeto.
- Un error de validación se comunica aquí con `ValueError` y se muestra sin guardar el dato inválido.
- El doble guion bajo de Python no es una barrera absoluta de seguridad.
