from abia_azamon import *
from Acciones import *
class Paquetes(object):
    def __init__(self,num_paquetes: int, semilla: int):
        self._lista_paquestes_inicial = random_paquetes(num_paquetes,semilla)
        self._num_paquetes_sin_asignar = len(self._lista_paquestes)
        self._paquetes=[[],[],[]] #paquetes agrupados por prioridad
        for paquete in self._lista_paquestes_inicial:
            self._paquetes[paquete.prioridad].append(paquete)

    
    def paquetes_sin_asignar(self):
        return self._num_paquetes_sin_asignar > 0 
    
    def asignar(self):
        self._num_paquetes_sin_asignar -= 1