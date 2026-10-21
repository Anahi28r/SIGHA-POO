class Docente:
    # Atributo de clase
    rol = "Docente"

    # Atributos de instancia
    def __init__(self, nombre, identificacion, disponible):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__disponible = disponible

    # Método de instancia
    def actualizarDatos(self, nombre):
        self.__nombre = nombre

    # Método de instancia
    def consultarDisponibilidad(self):
        return self.__disponible

    # Método de clase
    @classmethod
    def cambiarRol(cls, nuevoRol):
        cls.rol = nuevoRol


class Asignatura:
    # Atributo de clase
    categoria = "Académica"

    # Atributos de instancia
    def __init__(self, nombre, codigo, horasSemanales):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__horasSemanales = horasSemanales

    # Método de instancia
    def actualizarDatos(self, nombre):
        self.__nombre = nombre

    # Método de instancia
    def consultarHorasSemanales(self):
        return self.__horasSemanales

    # Método de clase
    @classmethod
    def cambiarCategoria(cls, nuevaCategoria):
        cls.categoria = nuevaCategoria


class Aula:
    # Atributo de clase
    uso = "Educativo"

    # Atributos de instancia
    def __init__(self, numero, capacidad, tipo):
        self.__numero = numero
        self.__capacidad = capacidad
        self.__tipo = tipo

    # Método de instancia
    def actualizarDatos(self, capacidad):
        self.__capacidad = capacidad

    # Método de instancia
    def consultarCapacidad(self):
        return self.__capacidad

    # Método de clase
    @classmethod
    def cambiarUso(cls, nuevoUso):
        cls.uso = nuevoUso


class Estudiante:
    # Atributo de clase
    rol = "Estudiante"

    # 3 atributos de instancia
    def __init__(self, nombre, identificacion, correo):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__correo = correo

    # Método de instancia
    def actualizarDatos(self, correo):
        self.__correo = correo

    # Método de instancia
    def consultarCorreo(self):
        return self.__correo

    # Método de clase
    @classmethod
    def cambiarRol(cls, nuevoRol):
        cls.rol = nuevoRol


class Curso:
    # Atributo de clase
    categoria = "Académico"

    # 3 atributos de instancia
    def __init__(self, nombre, paralelo, semestre):
        self.__nombre = nombre
        self.__paralelo = paralelo
        self.__semestre = semestre

    # Método de instancia
    def actualizarDatos(self, paralelo):
        self.__paralelo = paralelo

    # Método de instancia
    def consultarSemestre(self):
        return self.__semestre

    # Método de clase
    @classmethod
    def cambiarCategoria(cls, nuevaCategoria):
        cls.categoria = nuevaCategoria