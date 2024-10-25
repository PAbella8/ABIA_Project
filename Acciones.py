class Actions(object):
    '''
    Clase que representa las acciones posibles.
    '''
    pass

class MovePaquete(Actions):
    '''
    Acción de mover paquete de una oferta a otra.
    '''
    def __init__(self,paquete,oferta_inicial,oferta_final):
        self._paquete=paquete
        self._oferta_inicial=oferta_inicial
        self._oferta_final=oferta_final

class SwapPaquetes(Actions):
    '''
    Acción de intercambiar paquetes entre ofertas.
    '''
    def __init__(self,paquete1,paquete2,oferta_inicial,oferta_final):
        self._paquete1=paquete1
        self._paquete2=paquete2
        self._oferta_inicial=oferta_inicial
        self._oferta_final=oferta_final

class SwapOferta(Actions):
    '''
    Acción de mover todos los paquetes de una oferta a otra.
    '''
    def __init__(self,oferta_inicial,oferta_final):
        self._oferta_inicial=oferta_inicial
        self._oferta_final=oferta_final
