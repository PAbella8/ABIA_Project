from Paquetes import Paquetes
from Transporte import Transporte

class Estado(object):
    '''
    Clase que representa el estado del problema.
    '''
    def __init__(self) -> None:
        pass
    
def estado_inicial(paquetes: Paquetes,transporte: Transporte):
    '''
    Función que genera el estado inicial del problema.
    '''
    while paquetes.paquetes_sin_asignar():
        paquetes.asignar()