class Docente:
    status = "En proceso"
    def __init__(self, nombre, identificacion, disponibilidad):
        print(f"Creando docentes {nombre}, {identificacion}, {disponibilidad}")

        self.nombre = nombre
        self.identificacion = identificacion
        self.disponibilidad = disponibilidad
        

class Estudiante:
    estado = "Activo"
    def __init__(self, nombre_e, identificacion_e, matricula):
        print(f"Creando Estudiante {nombre_e}, {identificacion_e}, {matricula}")

        self.nombre_e = nombre_e
        self.identificacion_e = identificacion_e
        self.matricula = matricula

class Asignatura:
    tipo = "Academico"
    def __init__(self, codigo, nombre_a, horas_semanal):
        print(f"Creando Asignatura {codigo}, {nombre_a}, {horas_semanal}")

        self.codigo = codigo
        self.nombre_a = nombre_a
        self.horas_semanal = horas_semanal

class Curso:
    nivel = "3 nivel"
    def __init__(self, nombre_p, paralelo, semestre):
        print(f"Creando Curso {nombre_p}, {paralelo}, {semestre}")

        self.nombre_p = nombre_p
        self.paralelo = paralelo
        self.semestre = semestre

class Aula:
    estado_general = "Disponible"
    def __init__(self, numero, capacidad, tipo):
        print(f"Creando Aula {numero}, {capacidad}, {tipo}")

        self.numero = numero
        self.capacidad = capacidad
        self.tipo = tipo

class Horario:
    modalidad = "Presencial"
    def __init__(self, dia, hora_inicio, hora_fin):
        print(f"Creando Horario {dia}, {hora_inicio}, {hora_fin}")

        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

class Inscripcion:
    periodo = "2026-2027"
    def __init__(self, fecha, calificacion_final, asistencia):
        print(f"Creando Inscripcion {fecha}, {calificacion_final}, {asistencia}")

        self.fecha = fecha
        self.calificacion_final = calificacion_final
        self.asistencia = asistencia

class Persona:
    especie = "Humano"
    def __init__(self, nombre_ps, identificacion):
        print(f"Creando Persona {nombre_ps}, {identificacion}")

        self.nombre_ps = nombre_ps
        self.identificacion = identificacion

# HERENCIA SIMPLE
class Aula:
    estado_general = "Disponible"
    def __init__(self, numero, capacidad, tipo):
        print(f"Creando Aula {numero}, {capacidad}, {tipo}")

        self.numero = numero
        self.capacidad = capacidad
        self.tipo = tipo

class LaboratorioTI(Aula): 
    tipo = "General"
    
    def __init__(self, numero, capacidad, tipo, equipos, TI):
        super().__init__(numero, capacidad, tipo)
        print(f"Equipar Laboratorio con equipos {equipos} de {TI}")
        self.equipos = equipos
        self.TI = TI


# HERENCIA DE HERENCIA 
class Persona:
    def __init__(self, nombre_ps, identificacion):

        self.nombre_ps = nombre_ps
        self.identificacion = identificacion

        def mostar(self):
            print(self.nombre_ps)

class Docente(Persona):
    def __init__(self, nombre, identificacion, disponibilidad, ):
        super().__init__(nombre, identificacion)
        self.disponibilidad = disponibilidad

        def mostar(self):
            print(self.nombre)

class Estudiante(Docente):
    def __init__(self, nombre_e, identificacion_e, matricula):
        super().__init__(nombre_e, identificacion_e)  
        self.matricula = matricula

        def mostar(self):
            print(self.nombre_e)

# HERENCIA MULTIPLE
class Docente:
    status = "En proceso"
    def __init__(self, nombre, identificacion, disponibilidad):
        print(f"Creando Docente {nombre}, {identificacion}, {disponibilidad}")

        self.nombre = nombre
        self.identificacion = identificacion
        self.disponibilidad = disponibilidad

class Estudiante:
    estado = "Activo"
    def __init__(self, nombre_e, identificacion_e, matricula):
        print(f"Creando Estudiante {nombre_e}, {identificacion_e}, {matricula}")

        self.nombre_e = nombre_e
        self.identificacion_e = identificacion_e
        self.matricula = matricula

class Asistente(Docente, Estudiante):
    rol = "Asistente"
    def __init__(self, nombre, identificacion, disponibilidad, nombre_e, identificacion_e, matricula, porcentaje_asis):
        super().__init__(nombre, identificacion, disponibilidad, nombre_e, identificacion_e, matricula)  
        print(f"El porcentaje de asistencia del estudiante {nombre_e} es de {porcentaje_asis}")
        self.porcentaje_asis = porcentaje_asis


lab = LaboratorioTI(202, 30, "Computación", 25, "Cisco")
est = Estudiante("Ana Gómez", "1301234567", "M2026")
asis = Asistente("Carlos", "1309876543", "Parcial", "Carlos", "1309876543", "M2025", "95%")

print("Bases de LaboratorioTI:", LaboratorioTI.__bases__)
print("Bases de Asistente:", Asistente.__bases__)

print("Subclases de Aula:", Aula.__subclasses__())
print("Subclases de Persona:", Persona.__subclasses__())

print("MRO de LaboratorioTI:", LaboratorioTI.__mro__)
print("MRO de Asistente:", Asistente.__mro__)
      
    