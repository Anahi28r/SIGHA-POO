# Propuesta 2: recursos académicos como objetos

**Autor:** por acordar con el grupo.  
**Usuario de GitHub:** por completar.  
**Fecha real del aporte:** por completar.  
**Estado de esta ficha:** propuesta inicial; ejemplo de apoyo preparado.

## Idea

Representar docentes, estudiantes, asignaturas, aulas y cursos mediante objetos, para reunir sus datos y sus operaciones en una estructura organizada.

## De dónde surge

Las dos variantes de la práctica 2 trabajan clases académicas, atributos, constructores y métodos. Una de ellas también muestra un método estático y la diferencia entre atributos de clase y de instancia.

## Aplicación al proyecto

El [modelo](../sigha/modelos.py) define las entidades y la [aplicación 2](../aplicaciones/practica_02.py) crea docentes y un aula. Un docente tiene nombre, identificación y disponibilidad, en lugar de guardar esos datos en variables aisladas.

## Qué puede aportar el integrante

Crear y explicar dos recursos ficticios diferentes; mostrar qué atributos pertenecen a cada objeto; añadir o mejorar una operación útil de consulta. Indicar en esta ficha el cambio real, sin atribuirse automáticamente todo el modelo existente.

## Cómo comprobarlo

Desde la raíz: `python -m aplicaciones.practica_02`.

El nombre actualizado de un docente no debe cambiar el del otro. El atributo de clase de estado general sí se consulta de forma compartida, mientras no se oculte con uno de instancia. El ejemplo restablece el estado original al terminar.

**Resultado observado por el autor:** por completar después de ejecutar.

## Para explicarlo en clase

- Una clase es el modelo; un objeto es una instancia de ese modelo.
- `__init__` inicializa el objeto y `self` se refiere a la instancia.
- Un método de instancia recibe `self`; un método de clase recibe `cls`.
- Un método estático no recibe automáticamente ni `self` ni `cls`.
- La disponibilidad de cada docente es individual y no debe confundirse con un estado general compartido.
