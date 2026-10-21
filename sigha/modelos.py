"""Modelo académico inicial. Biblioteca estándar de Python 3.10 o posterior.

Integra conceptos de las prácticas; no es una transcripción de los originales.
Las ocho clases incluyen a Persona, que es abstracta.
"""
from abc import ABC, abstractmethod
from datetime import time


def texto_valido(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} debe ser un texto no vacío.")
    return valor.strip()


class Persona(ABC):
    institucion = "SIGHA - ejemplo académico"

    def __init__(self, nombre, identificacion):
        self.__nombre = texto_valido(nombre, "Nombre")
        self.__identificacion = texto_valido(identificacion, "Identificación")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def identificacion(self):
        return self.__identificacion

    def actualizar_nombre(self, nuevo_nombre):
        self.__nombre = texto_valido(nuevo_nombre, "Nombre")

    def mostrar(self):
        return f"{self.nombre} ({self.identificacion})"

    @abstractmethod
    def realizar_actividad(self):
        """Cada tipo de persona implementa su comportamiento."""
        pass


class Docente(Persona):
    estado_general = "Activo"  # Compartido por la clase; no indica disponibilidad horaria.

    def __init__(self, nombre, identificacion, disponibilidad):
        super().__init__(nombre, identificacion)
        self.__disponibilidad = texto_valido(disponibilidad, "Disponibilidad")

    def consultar_disponibilidad(self):
        return self.__disponibilidad

    @classmethod
    def cambiar_estado_general(cls, estado):
        cls.estado_general = texto_valido(estado, "Estado")

    @staticmethod
    def identificacion_valida(valor):
        # Solo revisa que exista texto: no valida una cédula ecuatoriana.
        return isinstance(valor, str) and bool(valor.strip())

    def realizar_actividad(self):
        return f"El docente {self.nombre} imparte clases."


class Estudiante(Persona):
    def __init__(self, nombre, identificacion, correo):
        super().__init__(nombre, identificacion)
        self.__correo = texto_valido(correo, "Correo")

    @property
    def correo(self):
        return self.__correo

    def realizar_actividad(self):
        return f"El estudiante {self.nombre} consulta su horario."


class Asignatura:
    def __init__(self, nombre, codigo, horas_semanales):
        self.nombre = texto_valido(nombre, "Asignatura")
        self.codigo = texto_valido(codigo, "Código")
        if type(horas_semanales) is not int or horas_semanales <= 0:
            raise ValueError("Las horas semanales deben ser un entero positivo.")
        self.horas_semanales = horas_semanales


class Aula:
    def __init__(self, numero, capacidad, tipo):
        self.numero = texto_valido(str(numero), "Número de aula")
        self.__capacidad = self.validar_capacidad(capacidad)
        self.tipo = texto_valido(tipo, "Tipo de aula")

    @staticmethod
    def validar_capacidad(capacidad):
        if type(capacidad) is not int or capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero positivo.")
        return capacidad

    def actualizar_capacidad(self, capacidad):
        self.__capacidad = self.validar_capacidad(capacidad)

    def consultar_capacidad(self):
        return self.__capacidad

    def mostrar(self):
        return f"Aula {self.numero}: {self.tipo}, {self.consultar_capacidad()} plazas"


class Curso:
    def __init__(self, nombre, paralelo, semestre):
        self.nombre = texto_valido(nombre, "Curso")
        self.paralelo = texto_valido(paralelo, "Paralelo")
        if type(semestre) is not int or semestre <= 0:
            raise ValueError("El semestre debe ser un entero positivo.")
        self.semestre = semestre
        self.__estudiantes = []

    @property
    def clave(self):
        return (self.nombre, self.paralelo, self.semestre)

    @property
    def estudiantes(self):
        return tuple(self.__estudiantes)

    def agregar_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise TypeError("El curso recibe objetos Estudiante.")
        if any(e.identificacion == estudiante.identificacion for e in self.__estudiantes):
            raise ValueError("El estudiante ya pertenece a este curso.")
        self.__estudiantes.append(estudiante)

    def consultar_horario(self, horarios):
        return [h for h in horarios if h.curso.clave == self.clave]


class Periodo:
    def __init__(self, numero, hora_inicio, hora_fin):
        if type(numero) is not int or numero <= 0:
            raise ValueError("El número de periodo debe ser positivo.")
        inicio, fin = time.fromisoformat(hora_inicio), time.fromisoformat(hora_fin)
        if inicio >= fin:
            raise ValueError("La hora de fin debe ser posterior al inicio, en el mismo día.")
        self.numero = numero
        self.__inicio, self.__fin = inicio, fin

    @property
    def hora_inicio(self):
        return self.__inicio

    @property
    def hora_fin(self):
        return self.__fin

    def se_superpone_con(self, otro):
        return self.hora_inicio < otro.hora_fin and otro.hora_inicio < self.hora_fin

    def mostrar(self):
        return f"{self.hora_inicio:%H:%M}-{self.hora_fin:%H:%M}"


class Horario:
    dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")

    def __init__(self, dia, periodo, asignatura, docente, aula, curso):
        if dia not in self.dias:
            raise ValueError("Selecciona un día académico de lunes a viernes.")
        for valor, clase in [(periodo, Periodo), (asignatura, Asignatura),
                             (docente, Docente), (aula, Aula), (curso, Curso)]:
            if not isinstance(valor, clase):
                raise TypeError(f"Se necesita un objeto {clase.__name__}.")
        self.dia, self.periodo = dia, periodo
        self.asignatura, self.docente, self.aula, self.curso = asignatura, docente, aula, curso

    def detectar_conflicto(self, otro):
        if self.dia != otro.dia or not self.periodo.se_superpone_con(otro.periodo):
            return ()
        recursos = []
        if self.docente.identificacion == otro.docente.identificacion:
            recursos.append("docente")
        if self.aula.numero == otro.aula.numero:
            recursos.append("aula")
        if self.curso.clave == otro.curso.clave:
            recursos.append("curso")
        return tuple(recursos)

    def consultar_detalle(self):
        return (f"{self.dia} {self.periodo.mostrar()} | {self.asignatura.nombre} | "
                f"{self.docente.nombre} | Aula {self.aula.numero} | "
                f"{self.curso.nombre} {self.curso.paralelo}")
