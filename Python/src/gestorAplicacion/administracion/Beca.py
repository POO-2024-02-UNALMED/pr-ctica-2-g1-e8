class Beca:
    _becas=[]

    def _init_(
        self,
        cupos,
        convenio,
        promedioRequerido,
        estratoMinimo,
        avanceRequerido,
        ayudaEconomica,
        creditosInscritosRequeridos,
    ):
        self._cupos=cupos
        self._convenio=convenio
        self._promedioRequerido=promedioRequerido
        self._estratoMinimo=estratoMinimo
        self._avanceRequerido=avanceRequerido
        self._ayudaEconomica=ayudaEconomica
        self._creditosInscritosRequeridos=creditosInscritosRequeridos
        Beca._becas.append(self)

    @staticmethod
    def buscandoBeca(becaSel):
        beca=None
        for becas in Beca._becas:
            if becas.getConvenio()==becaSel:
                beca=becas
        return beca
    
    @classmethod
    def eliminarBeca(cls, beca):
        cls._becas.remove(beca)

    @staticmethod
    def listaBecas():
        lista=[]
        for beca in Beca._becas:
            lista.append(beca.getConvenio())
        return lista
    
    def getConvenio(self):
        return self._convenio
