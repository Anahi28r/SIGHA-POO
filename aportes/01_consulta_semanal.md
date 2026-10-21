# Propuesta 1: consulta semanal por días y periodos

**Autor:** por acordar con el grupo.  
**Usuario de GitHub:** por completar.  
**Fecha real del aporte:** por completar.  
**Estado de esta ficha:** propuesta inicial; ejemplo de apoyo preparado.

## Idea

Organizar la consulta de SIGHA como una tabla: cada columna representa un día y cada fila un periodo. Así se puede observar qué bloques tienen clase y cuáles están libres.

## De dónde surge

La práctica 1 trabajó cadenas, números, booleanos, entrada de datos, listas, matrices, funciones y bucles. Una lista de listas permite representar la semana sin introducir todavía herramientas adicionales.

## Aplicación al proyecto

En [practica_01.py](../aplicaciones/practica_01.py), `crear_semana()` construye una matriz de bloques libres. El ejemplo asigna dos materias y recorre las filas con un bucle.

El código es una demostración inicial. La matriz ilustrativa no sustituye los objetos Horario ni aplica por sí sola la validación de cruces del modelo.

## Qué puede aportar el integrante

Adaptar la salida para que muestre encabezados de días y horas; explicar los índices de fila y columna; comprobar que la cantidad de días y periodos sea correcta. Registrar en esta ficha qué modificación realizó realmente.

## Cómo comprobarlo

Desde la raíz: `python -m aplicaciones.practica_01`.

Se esperan tres filas de periodos, cinco columnas de días y las materias de ejemplo en sus posiciones. Al cambiar una celda, las demás filas deben conservar sus valores.

**Resultado observado por el autor:** por completar después de ejecutar.

## Para explicarlo en clase

- Una lista guarda una secuencia; una matriz puede representarse con listas de listas.
- Un `for` permite recorrer periodos y días.
- Una función permite reutilizar la construcción de la semana.
- NumPy se vio en el original, pero no es obligatorio usarlo en esta idea si bastan listas.
