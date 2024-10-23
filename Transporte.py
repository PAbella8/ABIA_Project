from abia_azamon import *
class Transporte(object):
    def __init__(self, lista_paquetes: list, prop: float, semilla: int):
        self._lista_ofertas = random_ofertas(lista_paquetes,prop,semilla)