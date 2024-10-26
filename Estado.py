from Paquetes import Paquetes
from Transporte import Transporte
from Acciones import*
from copy import*

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
        ofertas_usadas=self._asignaciones.keys()

        for i in range(len(ofertas_usadas)):
            peso_ocupado=lista_peso_ocupado[i]
            oferta1=ofertas_usadas[i]
            prioridad1=(oferta1[0]+1)//2
            total_ofertas=self._transporte.ofertas_prioridad(prioridad1)
            for oferta2 in total_ofertas:
                if (oferta in ofertas_usadas and peso_ocupado<=lista_peso_libre[ofertas_usadas.index(oferta)]) or (oferta not in ofertas_usadas and peso_ocupado<=self._transporte.pesomax(oferta)):
                    yield SwapOferta(oferta1,oferta2)

            for paquete in ofertas_usadas[i]:
                peso_paquete,prioridad_paquete=self._paquetes.primer_paquete(paquete)
                ofertas_prioridad=self._transporte.ofertas_prioridad(prioridad_paquete)
                for oferta in ofertas_prioridad:
                    if oferta in ofertas_usadas:
                        if peso_paquete<=lista_peso_libre[ofertas_usadas.index(oferta)]:
                            yield MovePaquete(paquete,oferta1,oferta)
                        for paquete2 in self._asignaciones[oferta]:
                            peso_paquete2,prioridad_paquete2=self._paquetes.primer_paquete(paquete2)
                            if peso_paquete>=peso_paquete2:
                                if lista_peso_libre[ofertas_usadas.index(oferta)]+peso_paquete2>=peso_paquete:
                                    if prioridad_paquete<=prioridad_paquete2:
                                        if (oferta[0]+1)//2<=prioridad_paquete2:
                                            yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                                    else:
                                        if prioridad1<=prioridad_paquete:
                                            yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                            else:
                                if lista_peso_libre[ofertas_usadas.index(oferta1)]+peso_paquete>=peso_paquete2:
                                    if prioridad_paquete<=prioridad_paquete2:
                                        if (oferta[0]+1)//2<=prioridad_paquete2:
                                            yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                                    else:
                                        if prioridad1<=prioridad_paquete:
                                            yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                    elif peso_paquete<=self._transporte.pesomax(oferta):
                        yield MovePaquete(paquete,oferta1,oferta)

    def aplicar_accion(self,accion):
        asignaciones=copy.deepcopy(self._asignaciones)
        coste=self._coste
        felicidad=self._felicidad
        if isinstance(accion,SwapOferta):
            oferta_inicial=accion._oferta_inicial
            oferta_final=accion._oferta_final
            peso_ocupado_inicial=0
            paquetes_prioridad=[0,0]
            dia_inicial=oferta_inicial[0]
            dia_final=oferta_final[0]
            paquetes=asignaciones[oferta_inicial]
            for paquete in paquetes:
                peso_paquete,prioridad_paquete=self._paquetes.primer_paquete(paquete)
                peso_ocupado_inicial+=peso_paquete
                paquetes_prioridad[prioridad_paquete-1]+=1 if prioridad_paquete>0 else 0

            if oferta_final not in asignaciones.keys():
                asignaciones[oferta_final]=[]
            
            asignaciones[oferta_final]+=asignaciones[oferta_inicial]
            del asignaciones[oferta_inicial]
            coste-=self._transporte.coste(oferta_inicial)
            coste_inicial=peso_ocupado_inicial*0.25*(2 if dia_inicial==4 else 1) if dia_inicial>=2 else 0
            coste_final=peso_ocupado_inicial*0.25*(2 if dia_final==4 else 1) if dia_final>=2 else 0
            coste=coste-coste_inicial+coste_final
            felicidad_inicial=paquetes_prioridad[0]*max(0,(1-dia_inicial))+paquetes_prioridad[1]*max(0,(3-dia_inicial))
            felicidad_final=paquetes_prioridad[0]*max(0,(1-dia_final))+paquetes_prioridad[1]*max(0,(3-dia_final))
            felicidad=felicidad-felicidad_inicial+felicidad_final

        if isinstance()
            
            
        





    
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