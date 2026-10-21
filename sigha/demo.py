"""Ejecutar desde la raíz del repositorio: python -m sigha.demo."""
from .modelos import Docente, Estudiante, Asignatura, Aula, Curso, Periodo, Horario
from .planificacion import agregar_horario, consultar_por_docente


def datos_ejemplo():
    docente = Docente("Ana Ejemplo", "DOC-DEMO-01", "Jornada de mañana")
    estudiante = Estudiante("Luis Ejemplo", "EST-DEMO-01", "estudiante@example.com")
    asignatura = Asignatura("Programación Orientada a Objetos", "POO-201", 4)
    aula = Aula("101", 30, "Teórica")
    curso = Curso("TI", "A", 2)
    curso.agregar_estudiante(estudiante)
    return docente, estudiante, asignatura, aula, curso


def main():
    docente, estudiante, asignatura, aula, curso = datos_ejemplo()
    horarios = []
    print("SIGHA - INTEGRACIÓN INICIAL EN PYTHON\n")
    for persona in (docente, estudiante):
        print(persona.realizar_actividad())
    primero = Horario("Lunes", Periodo(1, "08:00", "10:00"),
                      asignatura, docente, aula, curso)
    agregar_horario(horarios, primero)
    print("\nClase registrada:", primero.consultar_detalle())
    propuesta = Horario("Lunes", Periodo(2, "09:00", "11:00"),
                        asignatura, docente, aula, curso)
    try:
        agregar_horario(horarios, propuesta)
    except ValueError as error:
        print("\nAsignación rechazada:", error)
    corregido = Horario("Lunes", Periodo(3, "10:00", "12:00"),
                        asignatura, docente, aula, curso)
    agregar_horario(horarios, corregido)
    print("\nCorrección guardada:", corregido.consultar_detalle())
    print("\nConsulta del curso:")
    for horario in curso.consultar_horario(horarios):
        print("-", horario.consultar_detalle())
    print("\nClases del docente:", len(consultar_por_docente(horarios, docente.identificacion)))
    print("Estudiantes asociados al curso:", len(curso.estudiantes))
    print("\nDatos ficticios. Sin base de datos ni conexión con la interfaz web.")


if __name__ == "__main__":
    main()
