"""Métodos de instancia, clase y estáticos; encapsulamiento."""
from sigha.modelos import Docente, Aula


def main():
    docente = Docente("Ana Ejemplo", "DOC-DEMO-01", "Mañana")
    otro = Docente("Carlos Ejemplo", "DOC-DEMO-02", "Tarde")
    docente.actualizar_nombre("Ana Ejemplo Actualizada")  # Instancia: self.
    print(docente.mostrar(), docente.consultar_disponibilidad())
    anterior = Docente.estado_general
    try:
        Docente.cambiar_estado_general("En revisión")  # Clase: cls.
        print("Estado compartido:", docente.estado_general, otro.estado_general)
    finally:
        Docente.cambiar_estado_general(anterior)
    print("ID de muestra válido:", Docente.identificacion_valida("DOC-DEMO-01"))
    aula = Aula("101", 30, "Teórica")
    try:
        aula.actualizar_capacidad(-1)
    except ValueError as error:
        print("Dato rechazado:", error)
    print("Capacidad conservada:", aula.consultar_capacidad())


if __name__ == "__main__":
    main()
