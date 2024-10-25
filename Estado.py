from Paquetes import Paquetes
from Transporte import Transporte
from Acciones import*

class Estado(object):
    '''
    Clase que representa el estado del problema.
    '''
    def __init__(self,asignaciones,transporte,paquetes,coste,felicidad) -> None:
        self._asignaciones=asignaciones
        self._coste=coste
        self._felicidad=felicidad
        self._transporte=transporte
        self._paquetes=paquetes
    
    def acciones(self):
        lista_peso_libre=[]
        lista_peso_ocupado=[]
        for oferta,lista_paquetes in self._asignaciones.items():
            pesomax=self._transporte.pesomax(oferta)
            peso_libre=pesomax
            for paquete in lista_paquetes:
                peso_libre-=self._paquetes.peso(paquete)
            lista_peso_libre.append(peso_libre)
            lista_peso_ocupado.append(pesomax-peso_libre)
        ofertas=self._asignaciones.keys()
        for i in range(len(ofertas)):
            peso_ocupado=lista_peso_ocupado[i]
            oferta1=ofertas[i]
            prioridad1=(oferta1[0]+1)//2
            for j in range(len(lista_peso_libre)):
                oferta2=ofertas[j]
                prioridad2=(oferta2[0]+1)//2
                if peso_ocupado<=lista_peso_libre[j] and prioridad1>=prioridad2:
                    yield SwapOferta(oferta1,oferta2)
            
            
        





    
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
    return Estado(diccionario,transporte,paquetes,coste,0)