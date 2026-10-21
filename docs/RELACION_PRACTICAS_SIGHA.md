# De cada práctica a una idea aplicable en SIGHA

Este documento relaciona evidencia existente con una aplicación nueva, revisada y ejecutable. El orden sigue la numeración de los archivos, no supone fechas de clase.

## Práctica 1: fundamentos de Python

**Evidencia:** `practicas/originales/01/PRACTICA #1 - ANAHI ROBAYO.py`.

**Qué contiene:** enteros, cadenas, decimales, booleanos, entrada con `input`, conversiones con `int`, listas, listas de listas, arrays NumPy, funciones y bucles. La sección titulada «Switch (Case)» utiliza realmente `if/elif/else`; no utiliza `match/case`.

**Idea para el proyecto:** representar los días y periodos de una semana en una lista de listas, y recorrerla para mostrar asignaturas o bloques libres. No es necesario trasladar todas las herramientas de un ejercicio al proyecto: para esta representación inicial bastan listas de Python.

**Aplicación:** [practica_01.py](../aplicaciones/practica_01.py).

**Cómo demostrarla:** ejecuta `python -m aplicaciones.practica_01`. Explica qué representa cada fila y cada columna. Esta matriz es ilustrativa: el modelo integrado utiliza objetos Horario para las asignaciones reales del ejemplo.

## Práctica 2: clases, atributos y métodos

**Evidencias:**

- `practicas/originales/02/ANAHI ROBAYO_ PRACTICA#2.py`.
- `practicas/originales/02/PRACTICA2_ANAHI ROBAYO.py`.

Ambos archivos están nombrados como práctica 2. Se conservan juntos; no se presupone cuál se entregó primero.

**Qué contienen:** clases Docente, Estudiante, Asignatura, Aula y Curso; constructores; atributos de clase e instancia; métodos de instancia, `@classmethod` y, en una de las variantes, `@staticmethod`. La variante `PRACTICA2_...` emplea atributos con doble guion bajo y métodos para consultar o actualizar datos.

**Idea para el proyecto:** crear objetos que representen recursos académicos y controlar sus actualizaciones. Por ejemplo, cambiar la capacidad de un aula solo si el nuevo valor es positivo.

**Aplicación:** [practica_02.py](../aplicaciones/practica_02.py) y [modelos.py](../sigha/modelos.py).

**Cómo demostrarla:** ejecuta `python -m aplicaciones.practica_02`. Muestra un método de instancia para cambiar el nombre, uno de clase para el estado general y uno estático para una comprobación sencilla. La disponibilidad de un docente sigue siendo un dato individual: no debe confundirse con un estado compartido de clase.

**Precisión sobre encapsulamiento:** en Python el prefijo `__` activa una transformación del nombre para reducir accesos y colisiones accidentales. No hace que los datos sean inaccesibles de forma absoluta. Lo que aporta valor es exponer operaciones claras y validar cambios.

## Práctica 3: herencia y reutilización

**Evidencia:** `practicas/originales/03/PRACTICA#3_ROBAYO ANAHI.py`.

**Qué contiene:** varias clases del ámbito académico y ejemplos de herencia simple, multinivel y múltiple, junto con `super()`, `__bases__`, `__subclasses__` y `__mro__`.

**Hallazgos:** el archivo redefine clases con el mismo nombre y contiene llamadas incompatibles a `super()`. No conviene trasladarlo completo al proyecto sin revisarlo. Los detalles están en [la revisión](REVISION_CODIGO.md).

**Idea para el proyecto:** Docente y Estudiante son tipos de Persona; ambos pueden reutilizar nombre e identificación. Un LaboratorioTI puede ser un tipo de Aula y añadir cantidad de equipos. Un estudiante no es un tipo de docente: para SIGHA, esa relación no debe modelarse mediante herencia.

**Aplicación:** [practica_03.py](../aplicaciones/practica_03.py) y la jerarquía Persona del [modelo](../sigha/modelos.py).

**Cómo demostrarla:** ejecuta `python -m aplicaciones.practica_03`. Explica cómo `super().__init__()` inicializa los datos comunes y cómo el laboratorio amplía `mostrar()` usando `super().mostrar()`.

**Decisión de diseño:** la herencia múltiple se conserva como aprendizaje del ejercicio original. No se fuerza en el proyecto si las relaciones se expresan mejor con asociación entre objetos.

## Práctica 4: abstracción, polimorfismo y composición

**Evidencia:** `practicas/originales/04/PRACTICA#4  ANAHI ROBAYO.py`.

**Qué contiene:** una clase abstracta PasarelaDePago, implementaciones Paypal y Stripe y un ServicioDeCaja que utiliza una pasarela. Es una simulación por consola: no conecta con servicios de pago ni realiza transacciones.

**Idea para el proyecto:** conservar la estructura de una operación común con implementaciones distintas. En SIGHA la operación puede ser `consultar()`: una consulta filtra por curso y otra por docente. Un servicio recibe la consulta que debe utilizar, igual que el servicio de caja recibía una pasarela.

**Aplicación:** [practica_04.py](../aplicaciones/practica_04.py).

**Cómo demostrarla:** ejecuta `python -m aplicaciones.practica_04`. El mismo ServicioConsulta trabaja con ConsultaPorDocente y ConsultaPorCurso. Cambia el objeto recibido, mientras se mantiene la llamada común.

**Límite del alcance:** los pagos no se incorporan a SIGHA. La práctica aporta conceptos, no la obligación de copiar su funcionalidad comercial.

## Repaso que se conecta con las prácticas

En el chat «Preparar examen de POO» se repasaron `pass`, `super()`, sobrescritura y clases abstractas. Los PDF de estudio de esta carpeta también incluyen ejemplos de esas ideas.

- `pass` no hace nada por sí mismo y no vuelve abstracto un método.
- `@abstractmethod` declara una operación que debe implementarse para instanciar una clase concreta.
- `super()` permite continuar la resolución de métodos según la jerarquía; no ejecuta automáticamente todos los constructores con cualquier conjunto de argumentos.
- Una clase hija que sobrescribe un método usa su propia versión. Si necesita reutilizar la versión de la base, debe llamarla explícitamente.
- `None` es un valor que representa ausencia de resultado; `SyntaxError` y `TypeError` son errores distintos. No son conceptos equivalentes.

El ejemplo de estudio con Inscripcion, calificación y asistencia se conserva como material de repaso. Esos atributos no se trasladaron al modelo de SIGHA porque el informe excluye calificaciones y control de asistencia.

## Ejemplo integrado

`python -m sigha.demo` une los conceptos en un recorrido: crea objetos, relaciona un estudiante con un curso, registra una clase, detecta un cruce y acepta una corrección. La integración es nueva; se entrega como un punto de partida para que el equipo la comprenda y la continúe.
