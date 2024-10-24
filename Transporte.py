from abia_azamon import *
class Transporte(object):
    def __init__(self, lista_paquetes: list, prop: float, semilla: int):
        self._lista_ofertas = random_ofertas(lista_paquetes,prop,semilla)
        self._ofertas_ordenadas=[[],[],[],[],[]]
        for oferta in self._lista_ofertas:
            self._ofertas_ordenadas[oferta.dias-1].append(oferta)
        self._ofertas_no_asignadas=[len(lista) for lista in self._ofertas_ordenadas]


        self._pesos = {oferta:oferta.pesomax for oferta in self._lista_ofertas}

    def get_oferta(self,dia):
        if self._ofertas_no_asignadas[dia]==0:
            dia=dia+1
        self._ofertas_no_asignadas[dia]-=1
        pos_2=len(self._ofertas_ordenadas[dia])-self._ofertas_no_asignadas[dia]
        oferta=self._ofertas_ordenadas[dia][pos_2]
        return (dia,pos_2),oferta.pesomax, oferta.precio
    
    def coste(self,oferta):
        return self._ofertas_ordenadas[oferta[0]][oferta[1]].precio
