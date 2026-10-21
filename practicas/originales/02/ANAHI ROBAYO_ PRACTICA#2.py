class Docente:
    status = "En proceso"

    def __init__(self, nombre, identificacion, disponibilidad):
        self.nombre = nombre
        self.identificacion = identificacion
        self.disponibilidad = disponibilidad

    def mostrar(self):
        print(self.nombre)

    @classmethod
    def estado(cls):
        print(cls.status)

    @staticmethod
    def mensaje():
        print("Docente registrado")


class Estudiante:
    estado = "Activo"

    def __init__(self, nombre, identificacion, matricula):
        self.nombre = nombre
        self.identificacion = identificacion
        self.matricula = matricula

    def mostrar(self):
        print(self.nombre)

    @classmethod
    def ver_estado(cls):
        print(cls.estado)

    @staticmethod
    def mensaje():
        print("Estudiante registrado")


class Asignatura:
    tipo = "Academico"

    def __init__(self, codigo, nombre, horas):
        self.codigo = codigo
        self.nombre = nombre
        self.horas = horas

    def mostrar(self):
        print(self.nombre)

    @classmethod
    def ver_tipo(cls):
        print(cls.tipo)

    @staticmethod
    def mensaje():
        print("Asignatura registrada")


class Curso:
    nivel = "3 Nivel"

    def __init__(self, nombre, paralelo, semestre):
        self.nombre = nombre
        self.paralelo = paralelo
        self.semestre = semestre

    def mostrar(self):
        print(self.nombre)

    @classmethod
    def ver_nivel(cls):
        print(cls.nivel)

    @staticmethod
    def mensaje():
        print("Curso registrado")


class Aula:
    estado = "Disponible"

    def __init__(self, numero, capacidad, tipo):
        self.numero = numero
        self.capacidad = capacidad
        self.tipo = tipo

    def mostrar(self):
        print(self.numero)

    @classmethod
    def ver_estado(cls):
        print(cls.estado)

    @staticmethod
    def mensaje():
        print("Aula registrada")


d1 = Docente("Carlos", "D01", "08:00")
e1 = Estudiante("Jose", "E01", "Matriculado")
a1 = Asignatura("POO01", "POO", 4)
c1 = Curso("Software", "A", 3)
au1 = Aula(101, 30, "Laboratorio")

d1.mostrar()
e1.mostrar()
a1.mostrar()
c1.mostrar()
au1.mostrar()


e2 = Estudiante("Juan", "E02", "Matriculado")

print(e1.estado)
print(e2.estado)

Estudiante.estado = "Inactivo"

print(e1.estado)
print(e2.estado)