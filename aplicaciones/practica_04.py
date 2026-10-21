"""Adapta la abstracción y composición del ejemplo de pagos a consultas de horarios."""
from abc import ABC, abstractmethod
from sigha.demo import datos_ejemplo
from sigha.modelos import Horario, Periodo
from sigha.planificacion import consultar_por_docente


class ConsultaHorario(ABC):
    @abstractmethod
    def consultar(self, horarios):
        pass


class ConsultaPorDocente(ConsultaHorario):
    def __init__(self, identificacion):
        self.identificacion = identificacion

    def consultar(self, horarios):
        return consultar_por_docente(horarios, self.identificacion)


class ConsultaPorCurso(ConsultaHorario):
    def __init__(self, curso):
        self.curso = curso

    def consultar(self, horarios):
        return self.curso.consultar_horario(horarios)


class ServicioConsulta:
    def __init__(self, consulta):
        self.consulta = consulta

    def mostrar(self, horarios):
        for horario in self.consulta.consultar(horarios):
            print(horario.consultar_detalle())


def main():
    docente, _, asignatura, aula, curso = datos_ejemplo()
    horarios = [Horario("Lunes", Periodo(1, "08:00", "10:00"),
                        asignatura, docente, aula, curso)]
    for consulta in (ConsultaPorDocente(docente.identificacion), ConsultaPorCurso(curso)):
        print(type(consulta).__name__)
        ServicioConsulta(consulta).mostrar(horarios)
    print("Una misma operación, distintas consultas. No se implementan pagos.")


if __name__ == "__main__":
    main()
