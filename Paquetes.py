from abia_azamon import *
from Acciones import *
class Paquetes(object):
    def __init__(self,num_paquetes: int, semilla: int):
        self._lista_paquestes = random_paquetes(num_paquetes,semilla)
        self._num_paquetes_sin_asignar = len(self._lista_paquestes)
    
    def paquetes_sin_asignar(self):
        return True if self._num_paquetes_sin_asignar > 1 else False
    
    def asignar(self):
        self._num_paquetes_sin_asignar -= 1