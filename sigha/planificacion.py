"""Operaciones iniciales de planificación en memoria."""
from .modelos import Horario


def agregar_horario(horarios, nuevo):
    if not isinstance(nuevo, Horario):
        raise TypeError("Se necesita un objeto Horario.")
    for existente in horarios:
        conflictos = nuevo.detectar_conflicto(existente)
        if conflictos:
            raise ValueError("Cruce de " + ", ".join(conflictos) + ": "
                             + existente.consultar_detalle())
    horarios.append(nuevo)


def consultar_por_docente(horarios, identificacion):
    return [h for h in horarios if h.docente.identificacion == identificacion]


def consultar_por_aula(horarios, numero):
    return [h for h in horarios if h.aula.numero == str(numero)]
