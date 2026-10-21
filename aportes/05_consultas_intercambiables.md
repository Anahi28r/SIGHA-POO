# Propuesta 5: consultas intercambiables de horarios

**Autor:** por acordar con el grupo.  
**Usuario de GitHub:** por completar.  
**Fecha real del aporte:** por completar.  
**Estado de esta ficha:** propuesta inicial; ejemplo de apoyo preparado.

## Idea

Consultar la planificación por docente o por curso mediante la misma operación `consultar()`, con una implementación distinta para cada criterio.

## De dónde surge

La práctica 4 utiliza una base abstracta PasarelaDePago, implementaciones distintas y un servicio que recibe una pasarela. Para SIGHA se reutiliza la estructura, sin incorporar pagos.

El repaso de examen también distinguió clases abstractas, métodos abstractos, herencia y polimorfismo.

## Aplicación al proyecto

En [practica_04.py](../aplicaciones/practica_04.py), ConsultaHorario declara un método abstracto y ConsultaPorDocente y ConsultaPorCurso lo implementan. ServicioConsulta recibe uno de esos objetos y lo utiliza sin decidir internamente cómo filtrar.

## Qué puede aportar el integrante

Explicar el contrato común y preparar casos para ambas consultas. Como ampliación opcional, puede implementar ConsultaPorAula reutilizando la función de consulta por aula del proyecto. Esa ampliación no se marca como implementada en esta ficha.

## Cómo comprobarlo

Desde la raíz: `python -m aplicaciones.practica_04`.

Las dos consultas deben ejecutarse por medio de ServicioConsulta y devolver las asignaciones que correspondan al recurso indicado. Con un docente o curso sin clases, el resultado debe estar vacío.

**Resultado observado por el autor:** por completar después de ejecutar.

## Para explicarlo en clase

- `ABC` y `@abstractmethod` permiten declarar una base y una operación requerida.
- Una clase con métodos abstractos pendientes no puede instanciarse.
- El polimorfismo permite usar la misma operación con comportamientos distintos.
- La composición aparece cuando ServicioConsulta guarda y utiliza un objeto de consulta.
- `pass` no convierte por sí mismo un método en abstracto.
