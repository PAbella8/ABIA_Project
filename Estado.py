from Paquetes import Paquetes
from Transporte import Transporte
from Acciones import*
import copy

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
        ofertas_usadas=list(self._asignaciones.keys())

        for i in range(len(ofertas_usadas)):
            peso_ocupado=lista_peso_ocupado[i]
            oferta1=ofertas_usadas[i]
            prioridad1=(oferta1[0]+1)//2
            total_ofertas=self._transporte.ofertas_prioridad(prioridad1)
            for oferta2 in total_ofertas:
                if oferta2!=oferta1 and ((oferta2 in ofertas_usadas and peso_ocupado<=lista_peso_libre[ofertas_usadas.index(oferta2)]) or (oferta2 not in ofertas_usadas and peso_ocupado<=self._transporte.pesomax(oferta2))):
                    yield SwapOferta(oferta1,oferta2)

            for paquete in self._asignaciones[ofertas_usadas[i]]:
                peso_paquete,prioridad_paquete=self._paquetes.primer_paquete(paquete)
                ofertas_prioridad=self._transporte.ofertas_prioridad(prioridad_paquete)
                ofertas_prioridad.remove(oferta1)
                for oferta in ofertas_prioridad:
                    if oferta in ofertas_usadas:
                        if peso_paquete<=lista_peso_libre[ofertas_usadas.index(oferta)]:
                            yield MovePaquete(paquete,oferta1,oferta)
                        for paquete2 in self._asignaciones[oferta]:
                            peso_paquete2,prioridad_paquete2=self._paquetes.primer_paquete(paquete2)
                            if peso_paquete>=peso_paquete2:
                                if lista_peso_libre[ofertas_usadas.index(oferta)]+peso_paquete2>=peso_paquete:
                                    if prioridad_paquete<=prioridad_paquete2:
                                        if (oferta[0]+1)//2<=prioridad_paquete:
                                            yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                                    else:
                                        if prioridad1<=prioridad_paquete2:
                                            yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                            else:
                                if lista_peso_libre[ofertas_usadas.index(oferta1)]+peso_paquete>=peso_paquete2:
                                    if prioridad_paquete<=prioridad_paquete2:
                                        if (oferta[0]+1)//2<=prioridad_paquete:
                                            yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                                    else:
                                        if prioridad1<=prioridad_paquete2:
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
            print('swap ofertas', oferta_inicial, oferta_final)
            for paquete in paquetes:
                peso_paquete,prioridad_paquete=self._paquetes.primer_paquete(paquete)
                peso_ocupado_inicial+=peso_paquete
                paquetes_prioridad[prioridad_paquete-1]+=1 if prioridad_paquete>0 else 0

            if oferta_final not in asignaciones.keys():
                asignaciones[oferta_final]=[]
                coste+=self._transporte.coste(oferta_final) 
            asignaciones[oferta_final]+=asignaciones[oferta_inicial]
            del asignaciones[oferta_inicial]
            coste-=self._transporte.coste(oferta_inicial)
            coste_inicial=peso_ocupado_inicial*0.25*(2 if dia_inicial==4 else 1) if dia_inicial>=2 else 0
            coste_inicial+= (1.5*(1+ ((oferta_inicial[0]+1)//2)%2)*len(paquetes) if ((oferta_inicial[0]+1)//2)>0 else 5)
            coste_final=peso_ocupado_inicial*0.25*(2 if dia_final==4 else 1) if dia_final>=2 else 0
            coste_final+=(1.5*(1+ ((oferta_final[0]+1)//2)%2)*len(paquetes) if ((oferta_final[0]+1)//2)>0 else 5)
            coste=coste-coste_inicial+coste_final
            felicidad_inicial=paquetes_prioridad[0]*max(0,(1-dia_inicial))+paquetes_prioridad[1]*max(0,(3-dia_inicial))
            felicidad_final=paquetes_prioridad[0]*max(0,(1-dia_final))+paquetes_prioridad[1]*max(0,(3-dia_final))
            felicidad=felicidad-felicidad_inicial+felicidad_final

        elif isinstance(accion,MovePaquete):
            paquete=accion._paquete
            peso_paquete,prioridad_paquete=self._paquetes.primer_paquete(paquete)
            oferta_inicial=accion._oferta_inicial
            oferta_final=accion._oferta_final
            dia_inicial=oferta_inicial[0]
            dia_final=oferta_final[0]
            asignaciones[oferta_inicial].remove(paquete)
            print('Move paquete',paquete, 'from',oferta_inicial,'to',oferta_final)
            if asignaciones[oferta_inicial]==[]:
                del asignaciones[oferta_inicial]
                coste-=self._transporte.coste(oferta_inicial)
            if oferta_final not in asignaciones:
                asignaciones[oferta_final]=[]
                coste+=self._transporte.coste(oferta_final)
            asignaciones[oferta_final].append(paquete)
            coste_inicial=peso_paquete*0.25*(2 if dia_inicial==4 else 1) if dia_inicial>=2 else 0
            coste_inicial+= (1.5*(1+ ((oferta_inicial[0]+1)//2)%2) if ((oferta_inicial[0]+1)//2)>0 else 5)
            coste_final=peso_paquete*0.25*(2 if dia_final==4 else 1) if dia_final>=2 else 0
            coste_final+=(1.5*(1+ ((oferta_final[0]+1)//2)%2) if ((oferta_final[0]+1)//2)>0 else 5)
            coste=coste-coste_inicial+coste_final
            dia_paquete=3 if prioridad_paquete==2 else prioridad_paquete
            felicidad_inicial=max(0,dia_paquete-dia_inicial)
            felicidad_final=max(0,dia_paquete-dia_final)
            felicidad=felicidad-felicidad_inicial+felicidad_final
        
        elif isinstance(accion,SwapPaquetes):
            paquete1=accion._paquete1
            paquete2=accion._paquete2
            peso1,prioridad1=self._paquetes.primer_paquete(paquete1)
            peso2,prioridad2=self._paquetes.primer_paquete(paquete2)
            oferta1=accion._oferta_inicial
            oferta2=accion._oferta_final
            print('Swap paquetes',oferta1,paquete1,oferta2,paquete2)
            dia1=oferta1[0]
            dia2=oferta2[0]
            asignaciones[oferta1].remove(paquete1)
            asignaciones[oferta1].append(paquete2)
            asignaciones[oferta2].remove(paquete2)
            asignaciones[oferta2].append(paquete1)
            coste_inicial=(peso1*0.25*(2 if dia1==4 else 1) if dia1>=2 else 0) + (peso2*0.25*(2 if dia2==4 else 1) if dia2>=2 else 0)
            coste_final=(peso2*0.25*(2 if dia1==4 else 1) if dia1>=2 else 0) + (peso1*0.25*(2 if dia2==4 else 1) if dia2>=2 else 0)
            coste=coste-coste_inicial+coste_final
            dia_paquete1=3 if prioridad1==2 else prioridad1
            dia_paquete2=3 if prioridad2==2 else prioridad2
            felicidad_inicial=max(0,dia_paquete1-dia1)+max(0,dia_paquete2-dia2)
            felicidad_final=max(0,dia_paquete1-dia2)+max(0,dia_paquete2-dia1)
            felicidad=felicidad-felicidad_inicial+felicidad_final
        print(asignaciones)
        print(coste)
        print(felicidad)
        print(self)
        return Estado(asignaciones,self._transporte,self._paquetes,coste,felicidad)

    def __repr__(self):
        return f"ESTADO: {self._coste} {self._felicidad}"

    def heuristic(self):
        return float(self._felicidad)/self._coste

    
def estado_inicial(paquetes: Paquetes,transporte: Transporte):
    '''
    Función que genera el estado inicial del problema.
    '''
    diccionario={}
    cont=0
    peso_libre=0
    coste=0
    oferta=(-1,-1)
    while paquetes.paquetes_sin_asignar():
        peso,prioridad=paquetes.primer_paquete(cont)
        dia= 3 if prioridad==2 else prioridad
        if dia>oferta[0] or peso_libre<peso:
            oferta,peso_libre,coste_oferta=transporte.get_oferta(dia)
            diccionario[oferta]=[cont]
            coste+=coste_oferta
        else:
            diccionario[oferta].append(cont)
        peso_libre-=peso
        cont+=1
        paquetes.asignar()
        coste+=peso*0.25*(2 if oferta[0]==4 else 1) if oferta[0]>=2 else 0
        coste += 1.5*(1+ ((oferta[0]+1)//2)%2) if ((oferta[0]+1)//2)>0 else 5
        print(coste)
    return Estado(diccionario,transporte,paquetes,coste,0)

