from gestorAplicacion.administracion.Grupo import Grupo
from excepciones.ErrorManejo import *



class Materia:
    materiasTotales = []

    def __init__(
        self,
        nombre,
        codigo,
        descripcion,
        creditos,
        facultad,
        prerrequisitos=None,
        grupos=None,
    ):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        self.creditos = creditos
        self.facultad = facultad
        self.prerrequisitos = prerrequisitos or []
        self.grupos =[]
        self.hacerAbreviatura(nombre)
        Materia.materiasTotales.append(self)