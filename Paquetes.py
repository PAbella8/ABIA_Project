from abia_azamon import *
from Acciones import *
class Paquetes(object):
    def __init__(self,num_paquetes: int, semilla: int):
        self._lista_desordenada=random_paquetes(num_paquetes,semilla)
        self._lista_paquetes=self._lista_desordenada
        self._num_paquetes_sin_asignar = len(self._lista_paquetes)
    def ordenar(self): 
        self._por_prioridad=[[],[],[]]       
        for paquete in self._lista_desordenada:
            self._por_prioridad[paquete.prioridad].append(paquete)
        self._lista_paquetes=sum(self._por_prioridad,[])
      
    def paquetes_sin_asignar(self):
        return self._num_paquetes_sin_asignar > 0 
    
    def asignar(self):
        self._num_paquetes_sin_asignar -= 1

    def primer_paquete(self,num_paquete):
        return self._lista_paquetes[num_paquete].peso, self._lista_paquetes[num_paquete].prioridad
    
    def peso(self,paquete):
        return self._lista_paquetes[paquete].peso
