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

    @staticmethod
    def buscarMateria(nombre, codigo):

        for i in range(len(Materia.materiasTotales)):
            if (
                Materia.materiasTotales[i].getNombre() == nombre
                and Materia.materiasTotales[i].getCodigo() == codigo
            ):
                return i
        return -1
    
    @staticmethod
    def encontrarMateria(nombre):
        mater = None
        for materia in Materia.getMateriasTotales():
            if materia.getNombre() == nombre:
                mater = materia
        return mater

    @staticmethod
    def mostrarMaterias():
        retorno = ""
        i = 1
        for materia in Materia.materiasTotales:
            retorno += f"{i}. {materia.nombre}.\n"
            i += 1
        return retorno
    
    @staticmethod
    def listaNombresMaterias():
        retorno = []
        for materia in Materia.materiasTotales:
            retorno.append(materia.getNombre())
        return retorno

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCodigo(self):
        return self.codigo
    
    @classmethod
    def getMateriasTotales(cls):
        return cls.materiasTotales

    @classmethod
    def setMateriasTotales(cls, materias):
        cls.materiasTotales = materias
