from abia_azamon import *
class Transporte(object):
    def __init__(self, lista_paquetes: list, prop: float, semilla: int):
        self._lista_ofertas = random_ofertas(lista_paquetes,prop,semilla)
        self._ofertas_ordenadas=[[],[],[],[],[]]
        for oferta in self._lista_ofertas:
            self._ofertas_ordenadas[oferta.dias-1].append(oferta)


        self._pesos = {oferta:oferta.pesomax for oferta in self._lista_ofertas}