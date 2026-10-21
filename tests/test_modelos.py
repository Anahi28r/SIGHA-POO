import unittest
from sigha.demo import datos_ejemplo
from sigha.modelos import Persona, Docente, Estudiante, Aula, Curso, Horario, Periodo
from sigha.planificacion import agregar_horario, consultar_por_docente, consultar_por_aula
from aplicaciones.practica_03 import LaboratorioTI
from aplicaciones.practica_04 import ConsultaHorario, ConsultaPorCurso, ConsultaPorDocente


class TestIntegracion(unittest.TestCase):
    def setUp(self):
        self.docente, self.estudiante, self.asignatura, self.aula, self.curso = datos_ejemplo()
        self.base = self.crear()

    def crear(self, **cambios):
        datos = dict(dia="Lunes", periodo=Periodo(1, "08:00", "10:00"),
                     asignatura=self.asignatura, docente=self.docente,
                     aula=self.aula, curso=self.curso)
        datos.update(cambios)
        return Horario(**datos)

    def test_clases_abstractas_no_se_instancian(self):
        with self.assertRaises(TypeError):
            Persona("Persona", "P01")
        with self.assertRaises(TypeError):
            ConsultaHorario()

    def test_polimorfismo(self):
        self.assertIn("imparte", self.docente.realizar_actividad())
        self.assertIn("consulta", self.estudiante.realizar_actividad())

    def test_encapsulamiento_rechaza_capacidad_invalida(self):
        with self.assertRaises(ValueError):
            self.aula.actualizar_capacidad(-1)
        self.assertEqual(self.aula.consultar_capacidad(), 30)
        with self.assertRaises(AttributeError):
            self.docente.nombre = "Cambio directo"

    def test_relacion_estudiante_curso(self):
        self.assertEqual(len(self.curso.estudiantes), 1)
        with self.assertRaises(ValueError):
            self.curso.agregar_estudiante(self.estudiante)
        with self.assertRaises(TypeError):
            self.curso.agregar_estudiante(self.docente)

    def test_super_reutiliza_datos_del_aula(self):
        lab = LaboratorioTI("LAB1", 20, 18)
        self.assertEqual(lab.consultar_capacidad(), 20)
        self.assertIn("18 equipos", lab.mostrar())

    def test_estado_de_clase_compartido(self):
        anterior = Docente.estado_general
        try:
            Docente.cambiar_estado_general("Revisión")
            self.assertEqual(self.docente.estado_general, "Revisión")
            self.assertEqual(Docente("Otro", "D02", "Tarde").estado_general, "Revisión")
        finally:
            Docente.cambiar_estado_general(anterior)

    def test_cruces_independientes_de_docente_aula_curso(self):
        for campo in ("docente", "aula", "curso"):
            with self.subTest(campo=campo):
                recursos = dict(docente=Docente("Otro", "D02", "Mañana"),
                                aula=Aula("102", 25, "Teórica"), curso=Curso("TI", "B", 2))
                recursos[campo] = getattr(self, campo)
                otro = self.crear(**recursos)
                self.assertEqual(self.base.detectar_conflicto(otro), (campo,))

    def test_misma_identificacion_representa_mismo_docente(self):
        otro = self.crear(docente=Docente("Ana", self.docente.identificacion, "Mañana"),
                          aula=Aula("102", 25, "Teórica"), curso=Curso("TI", "B", 2))
        self.assertEqual(self.base.detectar_conflicto(otro), ("docente",))

    def test_periodos_consecutivos_permitidos(self):
        self.assertEqual(self.base.detectar_conflicto(
            self.crear(periodo=Periodo(2, "10:00", "12:00"))), ())

    def test_superposicion_parcial_y_envolvente(self):
        for inicio, fin in [("09:00", "11:00"), ("07:00", "11:00")]:
            with self.subTest(inicio=inicio):
                self.assertTrue(self.base.detectar_conflicto(
                    self.crear(periodo=Periodo(2, inicio, fin))))

    def test_dia_distinto_permitido(self):
        self.assertEqual(self.base.detectar_conflicto(self.crear(dia="Martes")), ())

    def test_periodos_invalidos(self):
        for inicio, fin in [("10:00", "09:00"), ("09:00", "09:00"), ("25:00", "26:00")]:
            with self.subTest(inicio=inicio):
                with self.assertRaises(ValueError):
                    Periodo(1, inicio, fin)

    def test_rechazo_no_modifica_planificacion(self):
        horarios = [self.base]
        with self.assertRaises(ValueError):
            agregar_horario(horarios, self.crear())
        self.assertEqual(horarios, [self.base])

    def test_consultas_por_recurso(self):
        horarios = [self.base]
        self.assertEqual(self.curso.consultar_horario(horarios), horarios)
        self.assertEqual(consultar_por_docente(horarios, self.docente.identificacion), horarios)
        self.assertEqual(consultar_por_aula(horarios, self.aula.numero), horarios)
        self.assertEqual(consultar_por_docente(horarios, "inexistente"), [])
        for consulta in (ConsultaPorCurso(self.curso), ConsultaPorDocente(self.docente.identificacion)):
            self.assertEqual(consulta.consultar(horarios), horarios)


if __name__ == "__main__":
    unittest.main()
