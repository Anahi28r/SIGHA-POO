"""Herencia simple y sobrescritura. Extensión opcional del modelo de ocho clases."""
from sigha.modelos import Aula, Docente, Estudiante


class LaboratorioTI(Aula):
    def __init__(self, numero, capacidad, equipos):
        if type(equipos) is not int or equipos < 0:
            raise ValueError("Los equipos deben ser un entero no negativo.")
        super().__init__(numero, capacidad, "Laboratorio TI")
        self.equipos = equipos

    def mostrar(self):
        return super().mostrar() + f", {self.equipos} equipos"


def main():
    laboratorio = LaboratorioTI("LAB-1", 25, 25)
    print(laboratorio.mostrar())
    personas = [Docente("Ana Ejemplo", "D01", "Mañana"),
                Estudiante("Luis Ejemplo", "E01", "estudiante@example.com")]
    for persona in personas:
        print(persona.realizar_actividad())
    print("Docente y Estudiante heredan de Persona; Estudiante no hereda de Docente.")
    print("No se requiere herencia múltiple para estas relaciones de SIGHA.")


if __name__ == "__main__":
    main()
