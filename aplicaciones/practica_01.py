"""Listas, matrices, funciones y bucles aplicados al horario."""
from sigha.modelos import Horario


def crear_semana(periodos):
    return [["Libre" for _ in Horario.dias] for _ in range(periodos)]


def main():
    semana = crear_semana(3)
    semana[0][0] = "POO"
    semana[1][1] = "Base de Datos"
    for numero, fila in enumerate(semana, start=1):
        print(f"Periodo {numero}: {fila}")
    for indice, dia in enumerate(Horario.dias, start=1):
        print(indice, dia)
    print("La lista de listas representa filas de periodos y columnas de días.")
    print("NumPy se estudia en el original; este ejemplo no lo necesita.")


if __name__ == "__main__":
    main()
