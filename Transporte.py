from abia_azamon import *
class Transporte(object):
    def __init__(self, lista_paquetes: list, prop: float, semilla: int):
        self._lista_ofertas = random_ofertas(lista_paquetes,prop,semilla)
        self._pesos = {oferta:oferta.pesomax for oferta in self._lista_ofertas}