# Propuesta 4: reutilizar los datos comunes mediante Persona

**Autor:** por acordar con el grupo.  
**Usuario de GitHub:** por completar.  
**Fecha real del aporte:** por completar.  
**Estado de esta ficha:** propuesta inicial; ejemplo de apoyo preparado.

## Idea

Crear una base Persona para el nombre y la identificación que comparten Docente y Estudiante. Cada clase hija añade sus datos y su comportamiento, sin tratar al estudiante como un tipo de docente.

## De dónde surge

La práctica 3 aborda herencia y `super()`. En el repaso para el examen se trabajaron la reutilización del constructor y la sobrescritura de métodos.

## Aplicación al proyecto

En [modelos.py](../sigha/modelos.py), Docente y Estudiante heredan de Persona y llaman a `super().__init__()`. El [ejemplo de la práctica 3](../aplicaciones/practica_03.py) muestra sus comportamientos y una extensión Aula–LaboratorioTI.

La propuesta principal de esta ficha es la jerarquía Persona. LaboratorioTI es un segundo ejemplo didáctico de herencia, no una función obligatoria adicional de este aporte.

## Qué puede aportar el integrante

Explicar los atributos comunes y los específicos, comprobar la inicialización y proponer la actualización de esa jerarquía en el UML. Solo marcar la actualización del UML como terminada cuando se haya modificado y revisado realmente.

## Cómo comprobarlo

Desde la raíz: `python -m aplicaciones.practica_03`.

Docente y Estudiante deben conservar su nombre e identificación y responder de forma distinta a `realizar_actividad()`. El laboratorio debe conservar la capacidad inicializada por Aula y añadir su cantidad de equipos.

**Resultado observado por el autor:** por completar después de ejecutar.

## Para explicarlo en clase

- La herencia expresa una relación «es un»: un docente es una persona.
- `super()` no elimina la necesidad de pasar los argumentos requeridos.
- Sobrescribir un método permite que una hija tenga su propia versión.
- Si esa versión solo contiene `pass`, no imprime nada ni llama automáticamente a la base.
- La herencia múltiple se estudió, pero no debe introducirse si no representa una relación útil del dominio.
