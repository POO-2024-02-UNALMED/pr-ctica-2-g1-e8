from gestorAplicacion.administracion.Grupo import Grupo
from gestorAplicacion.usuario.Usuario import Usuario
from gestorAplicacion.administracion.Horario import Horario

class Estudiante(Usuario):
    _estudiantes = []
    def __init__(
        self,
        id,
        nombre,
        programa,
        semestre,
        facultad,
        estrato,
        sueldo,
        materias=None,
        gruposVistos=None,
    ):
        

        super().__init__(id, nombre, facultad)
        super().setTipo("Estudiante")
        self._programa = programa
        self._semestre = semestre
        self._creditos = 0
        self._materias = materias or []  # no se que tan bien este esto
        self._grupos = []
        self._estrato = estrato
        self._sueldo = sueldo
        self._valorMatricula = 1234567 * estrato
        self._matriculaPagada = False
        self._promedio = 0
        self._avance = 0
        self._CREDITOS_PARA_GRADURASE = 120
        self._beca = None
        self._notas = None
        self._gruposVistos = gruposVistos or []
        self._horario = Horario()  # Revisar
        Estudiante._estudiantes.append(self)    
    def getPrograma(self):
        return self._programa

    def setPrograma(self, programa):
        self._programa = programa

    def getSemestre(self):
        return self._semestre

    def setSemestre(self, semestre):
        self._semestre = semestre

    def getCreditos(self):
        return self._creditos

    def setCreditos(self, creditos):
        self._creditos = creditos

    def getMaterias(self):
        return self._materias

    def setMaterias(self, materias):
        self._materias = materias

    def getGrupos(self):
        return self._grupos

    def setGrupos(self, grupos):
        self._grupos = grupos

    def getHorario(self):
        return self._horario

    def setHorario(self, horario):
        self._horario = horario
    @classmethod
    def getEstudiantes(cls):
        return cls._estudiantes

    @classmethod
    def setEstudiantes(cls, estudiantes):
        cls._estudiantes = estudiantes

    def getEstrato(self):
        return self._estrato

    def setEstrato(self, estrato):
        self._estrato = estrato

    def getSueldo(self):
        return self._sueldo

    def setSueldo(self, sueldo):
        self._sueldo = sueldo

    def getValorMatricula(self):
        return self._valorMatricula

    def isMatriculaPagada(self):
        return self._matriculaPagada

    def getPromedio(self):
        return self._promedio

    def setPromedio(self, promedio):
        self._promedio = promedio

    def getAvance(self):
        return self._avance

    def setAvance(self, avance):
        self._avance = avance

    def getCreditosParaGraduarse(self):
        return self._CREDITOS_PARA_GRADURASE

    def getBeca(self):
        return self._beca

    def setBeca(self, beca):
        self._beca = beca

    def getNotas(self):
        return self._notas

    def setNotas(self, notas):
        self._notas = notas


    def getGruposVistos(self):
        return self._gruposVistos


    def setGruposVistos(self, gruposVistos):
        self._gruposVistos = gruposVistos

