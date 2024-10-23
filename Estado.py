from Paquetes import Paquetes
from Transporte import Transporte

class Estado(object):
    '''
    Clase que representa el estado del problema.
    '''
    def __init__(self,ofertas) -> None:
        self._asignaciones={oferta:[[],oferta.pesomax] for oferta in ofertas} #[]
    
    def asignar(self,paquete,oferta):
        self._asignaciones[oferta][0].append(paquete)
        self._asignaciones[oferta][1]-=paquete.peso
        paquete.asignar()

    
def estado_inicial(paquetes: Paquetes,transporte: Transporte):
    '''
    Función que genera el estado inicial del problema.
    '''
    estado_ini=Estado(transporte._lista_ofertas)
    while paquetes.paquetes_sin_asignar():
        paquetes.asignar()