from abia_azamon import *
from Acciones import *
class Paquetes(object):
    '''
    Clase que representa todos los paquetes del problema con 3 atributos: la lista desordenada deç
    paquetes, la lista de paquetes que utilizaremos (clasificada o no) y la lista de paquetes sin asignar.
    '''
    def __init__(self,num_paquetes: int, semilla: int):
        self._lista_desordenada=random_paquetes(num_paquetes,semilla) #lista de paquetes inicial
        self._lista_paquetes=self._lista_desordenada #utilizamos los paquetes desordenados para el estado inicial aleatorio, y los clasificados para el otro
        self._num_paquetes_sin_asignar = len(self._lista_paquetes) #número de paquetes que nos quedan por asignar
    def ordenar(self):  
        '''
        Método para clasificar los paquetes por prioridad.
        '''
        self._por_prioridad=[[],[],[]]       
        for paquete in self._lista_desordenada:
            self._por_prioridad[paquete.prioridad].append(paquete)
        self._lista_paquetes=sum(self._por_prioridad,[])
      
    def paquetes_sin_asignar(self):
        '''
        Método que comprueba que todavía quedan paquetes para asignar.
        '''
        return self._num_paquetes_sin_asignar > 0 
    
    def asignar(self):
        '''
        Quando asignamos un paquete restamos 1 al número de paquetes que quedan por asignar.
        '''
        self._num_paquetes_sin_asignar -= 1

    def primer_paquete(self,num_paquete):
        '''
        A partir del identificador del paquete (su posición en la lista) obtenemos su peso y su prioridad.
        '''
        return self._lista_paquetes[num_paquete].peso, self._lista_paquetes[num_paquete].prioridad
    
    def peso(self,paquete):
        '''
        A partir del identificador del paquete (su posición en la lista) obtenemos su peso.
        '''
        return self._lista_paquetes[paquete].peso
