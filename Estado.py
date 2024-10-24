from Paquetes import Paquetes
from Transporte import Transporte

class Estado(object):
    '''
    Clase que representa el estado del problema.
    '''
    def __init__(self,asignaciones,transporte,paquetes,coste,felicidad) -> None:
        self._asignaciones=asignaciones
        self._coste=coste
        self._felicidad=felicidad
    
    def asignar(self,paquete,oferta):
        self._asignaciones[oferta][0].append(paquete)
        self._asignaciones[oferta][1]-=paquete.peso
        paquete.asignar()
    
    
def estado_inicial(paquetes: Paquetes,transporte: Transporte):
    '''
    Función que genera el estado inicial del problema.
    '''
    diccionario={}
    cont=0
    peso_libre=0
    coste=0
    while paquetes.paquetes_sin_asignar():
        peso,prioridad=paquetes.primer_paquete(cont)
        dia= 3 if prioridad==2 else prioridad
        if peso_libre<peso or dia>oferta[0]:
            oferta,peso_libre,coste_oferta=transporte.get_oferta(dia)
            diccionario[oferta]=[cont]
            coste+=coste_oferta
        else:
            diccionario[oferta].append(cont)
        cont+=1
        paquetes.asignar()
        coste+=peso*0.25*(2 if dia==4 else 1) if dia>=2 else 0
    return Estado(diccionario,transporte,paquetes,coste,felicidad)