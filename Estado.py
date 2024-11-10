from Paquetes import Paquetes
from Transporte import Transporte
from Acciones import*
import copy
import math
import random

class Estado(object):
    '''
    Clase que representa el estado del problema.
    '''

    def __init__(self,asignaciones,transporte,paquetes,coste,felicidad,k=1) -> None:
        self._asignaciones=asignaciones #Diccionario que representa todas las asignaciones. Las claves son los identificadores de cada oferta y los valores son una lista con los paquetes asignados a esa oferta
        self._coste=coste #Coste total del estado
        self._felicidad=felicidad #Felicidad total del estado
        self._transporte=transporte #Instancia de la classe transporte
        self._paquetes=paquetes #Instancia de la classe paquetes
        self.k= k #ponderación de la felicidad (valor en € de cada dia de felicidad)
        self.e=1 #ponderación de la entropia
    def acciones(self,extendido,simulated_annealing=False):
        '''
        Método generador de todas las acciones posibles para un estado determinado.
        '''
        lista_peso_libre=[]
        lista_peso_ocupado=[]
        list_acciones = []
        for oferta,lista_paquetes in self._asignaciones.items(): #calculamos el peso libre y ocupado de cada oferta
            pesomax=self._transporte.pesomax(oferta)
            peso_libre=pesomax
            for paquete in lista_paquetes:
                peso_libre-=self._paquetes.peso(paquete)
            lista_peso_libre.append(peso_libre)
            lista_peso_ocupado.append(pesomax-peso_libre)
        ofertas_usadas=list(self._asignaciones.keys())

        for i in range(len(ofertas_usadas)): #iteramos sobre las ofertas usadas
            peso_ocupado=lista_peso_ocupado[i]
            oferta1=ofertas_usadas[i]
            prioridad1=(oferta1[0]+1)//2
            total_ofertas=self._transporte.ofertas_prioridad(prioridad1)
            if extendido:
                for oferta2 in total_ofertas:
                    if oferta2!=oferta1 and ((oferta2 in ofertas_usadas and peso_ocupado<=lista_peso_libre[ofertas_usadas.index(oferta2)]) or (oferta2 not in ofertas_usadas and peso_ocupado<=self._transporte.pesomax(oferta2))):
                        #Si podemos meter todos los paquetes de una oferta en otra (usada o nueva) hace SwapOferta (si caben y cumplen la prioridad)
                        if not simulated_annealing:
                            yield SwapOferta(oferta1,oferta2)
                        else:
                            list_acciones.append(SwapOferta(oferta1,oferta2))

            for paquete in self._asignaciones[ofertas_usadas[i]]: #Iteramos sobre los paquetes de la oferta
                peso_paquete,prioridad_paquete=self._paquetes.primer_paquete(paquete)
                ofertas_prioridad=self._transporte.ofertas_prioridad(prioridad_paquete)
                ofertas_prioridad.remove(oferta1)
                for oferta in ofertas_prioridad: #Iteramos sobre todas las ofertas que cumplen con la prioridad del paquete
                    if oferta in ofertas_usadas:
                        if peso_paquete<=lista_peso_libre[ofertas_usadas.index(oferta)]:
                            if not simulated_annealing:
                                yield MovePaquete(paquete,oferta1,oferta) #Si podemos meter un paquete en otra oferta (usada o nueva) hace MovePaquete (si cabe y cumple la prioridad)
                            else:
                                list_acciones.append(MovePaquete(paquete,oferta1,oferta))
                        for paquete2 in self._asignaciones[oferta]: #Iteramos sobre los paquetes de la segunda oferta
                            peso_paquete2,prioridad_paquete2=self._paquetes.primer_paquete(paquete2)
                            if peso_paquete>=peso_paquete2:
                                if lista_peso_libre[ofertas_usadas.index(oferta)]+peso_paquete2>=peso_paquete:
                                    if prioridad_paquete<=prioridad_paquete2:
                                        if (oferta[0]+1)//2<=prioridad_paquete:
                                            #Si el paquete más grande cabe en la otra oferta y el paquete de menor prioridad puede ir a la otra oferta hace SwapPaquete
                                            if not simulated_annealing:
                                                yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                                            else:
                                                list_acciones.append(SwapPaquetes(paquete,paquete2,oferta1,oferta))
                                    else:
                                        if prioridad1<=prioridad_paquete2:
                                            if not simulated_annealing:
                                                yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                                            else:
                                                list_acciones.append(SwapPaquetes(paquete,paquete2,oferta1,oferta))
                            else:
                                if lista_peso_libre[ofertas_usadas.index(oferta1)]+peso_paquete>=peso_paquete2:
                                    if prioridad_paquete<=prioridad_paquete2:
                                        if (oferta[0]+1)//2<=prioridad_paquete:
                                            if not simulated_annealing:
                                                yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                                            else:
                                                list_acciones.append(SwapPaquetes(paquete,paquete2,oferta1,oferta))
                                    else:
                                        if prioridad1<=prioridad_paquete2:
                                            if not simulated_annealing:
                                                yield SwapPaquetes(paquete,paquete2,oferta1,oferta)
                                            else:
                                                list_acciones.append(SwapPaquetes(paquete,paquete2,oferta1,oferta))
                    elif peso_paquete<=self._transporte.pesomax(oferta):
                        #Si no estamos usando la oferta seguro que cabe y hacemos MovePaquete
                        if not simulated_annealing:
                            yield MovePaquete(paquete,oferta1,oferta)
                        else:
                            list_acciones.append(MovePaquete(paquete,oferta1,oferta))
        if simulated_annealing:
            yield random.choice(list_acciones)

    def aplicar_accion(self,accion):
        '''
        Método que, a partir de un estado y de una acción, devuelve una instancia del estado resultante al aplicar la acción.
        '''
        asignaciones=copy.deepcopy(self._asignaciones) #Copiamos tots los parámetros del estado original y otros que necesitamos
        coste=self._coste
        felicidad=self._felicidad
        oferta_inicial=accion._oferta_inicial
        oferta_final=accion._oferta_final
        coste_oferta_inicial=self._transporte.coste(oferta_inicial)
        coste_oferta_final=self._transporte.coste(oferta_final)
        if isinstance(accion,SwapOferta):
            '''
            Metemos todos los paquetes de una oferta a otra (usada o nueva).
            '''
            peso_ocupado_inicial=0
            paquetes_prioridad=[0,0]
            dia_inicial=oferta_inicial[0]
            dia_final=oferta_final[0]
            paquetes=asignaciones[oferta_inicial]
            for paquete in paquetes: #calculamos el peso ocupado de la oferta y el número de paquetes de la prioridad 1 y 2
                peso_paquete,prioridad_paquete=self._paquetes.primer_paquete(paquete)
                peso_ocupado_inicial+=peso_paquete
                paquetes_prioridad[prioridad_paquete-1]+=1 if prioridad_paquete>0 else 0

            if oferta_final not in asignaciones.keys(): #Si es una oferta nueva creamos la clave en el diccionario
                asignaciones[oferta_final]=[]
            asignaciones[oferta_final]+=asignaciones[oferta_inicial] #Metemos los paquetes a la oferta y eliminamos la primera del diccionario
            del asignaciones[oferta_inicial]
            coste-=coste_oferta_inicial*peso_ocupado_inicial #Restamos el coste de la primera oferta 
            coste-=peso_ocupado_inicial*0.25*(2 if dia_inicial==4 else 1) if dia_inicial>=2 else 0 #Restamos el coste inicial de almacén
            coste-= (1.5*(1+ ((oferta_inicial[0]+1)//2)%2)*len(paquetes) if oferta_inicial[0]!=0 else 5*len(paquetes)) #Restamos el coste inicial de envío
            coste+=peso_ocupado_inicial*0.25*(2 if dia_final==4 else 1) if dia_final>=2 else 0 #Sumamos el coste final de almacén
            coste+=(1.5*(1+ ((oferta_final[0]+1)//2)%2)*len(paquetes) if oferta_final[0]!=0 else 5*len(paquetes)) #Sumamos el coste final de envío
            coste+=peso_ocupado_inicial*coste_oferta_final #Sumamos el coste de la segunda oferta
            felicidad-=paquetes_prioridad[0]*max(0,(1-dia_inicial))+paquetes_prioridad[1]*max(0,(3-dia_inicial)) #Restamos la feliciad causada por la oferta inicial
            felicidad+=paquetes_prioridad[0]*max(0,(1-dia_final))+paquetes_prioridad[1]*max(0,(3-dia_final)) #Sumamos la felicidad causada por la oferta final

        elif isinstance(accion,MovePaquete):
            '''
            Movemos un paquete de una oferta a otra (usada o nueva).
            '''
            paquete=accion._paquete
            peso_paquete,prioridad_paquete=self._paquetes.primer_paquete(paquete)
            
            dia_inicial=oferta_inicial[0]
            dia_final=oferta_final[0]
            asignaciones[oferta_inicial].remove(paquete) #Eliminamos el paquete de la oferta inicial
            if asignaciones[oferta_inicial]==[]: #Si ésta queda vacía la eliminamos del diccionario
                del asignaciones[oferta_inicial]
            if oferta_final not in asignaciones: #Si la segunda oferta es nueva creamos su clave en el diccionario
                asignaciones[oferta_final]=[]
            asignaciones[oferta_final].append(paquete) #Metemos el paquete en la seguna oferta
            coste-=peso_paquete*coste_oferta_inicial #Restamos el coste de la primera oferta
            coste-=peso_paquete*0.25*(2 if dia_inicial==4 else 1) if dia_inicial>=2 else 0 #Restamos el coste inicial de almacén
            coste-= (1.5*(1+ ((dia_inicial+1)//2)%2) if dia_inicial!=0 else 5) #Restamos el coste inicial de envío
            coste+=peso_paquete*0.25*(2 if dia_final==4 else 1) if dia_final>=2 else 0 #Sumamos el coste final de almacén
            coste+=(1.5*(1+ ((dia_final+1)//2)%2) if dia_final!=0 else 5) #Sumamos el coste final de envío
            coste+= coste_oferta_final*peso_paquete #Sumamos el coste de la segunda oferta
            dia_paquete=3 if prioridad_paquete==2 else prioridad_paquete
            felicidad-=max(0,dia_paquete-dia_inicial) #Restamos la felicidad del paquete en la primera oferta
            felicidad+=max(0,dia_paquete-dia_final) #Sumamos la felicidad del paquete en la segunda oferta
        
        elif isinstance(accion,SwapPaquetes):
            '''
            Cambiamos 2 paquetes de oferta
            '''
            paquete1=accion._paquete1
            paquete2=accion._paquete2
            peso1,prioridad1=self._paquetes.primer_paquete(paquete1)
            peso2,prioridad2=self._paquetes.primer_paquete(paquete2)

            dia1=oferta_inicial[0]
            dia2=oferta_final[0]
            asignaciones[oferta_inicial].remove(paquete1) #Cambiamos los paquetes de oferta
            asignaciones[oferta_inicial].append(paquete2)
            asignaciones[oferta_final].remove(paquete2)
            asignaciones[oferta_final].append(paquete1)
            coste-=coste_oferta_inicial*peso1 + coste_oferta_final*peso2 #Restamos los costes originales de las ofertas
            coste-=(peso1*0.25*(2 if dia1==4 else 1) if dia1>=2 else 0) + (peso2*0.25*(2 if dia2==4 else 1) if dia2>=2 else 0) #Restamos el coste de almacén del estado inicial
            coste+=(peso2*0.25*(2 if dia1==4 else 1) if dia1>=2 else 0) + (peso1*0.25*(2 if dia2==4 else 1) if dia2>=2 else 0) #Sumamos el coste de almacén del estado resultante
            coste+=coste_oferta_final*peso1 + coste_oferta_inicial*peso2 #Sumamos los costes resultantes de las ofertas 
            dia_paquete1=3 if prioridad1==2 else prioridad1
            dia_paquete2=3 if prioridad2==2 else prioridad2
            felicidad-=max(0,dia_paquete1-dia1)+max(0,dia_paquete2-dia2) #Restamos la felicidad del estado inicial
            felicidad+=max(0,dia_paquete1-dia2)+max(0,dia_paquete2-dia1) #Sumamos la felicidad del estado resultante

        return Estado(asignaciones,self._transporte,self._paquetes,coste,felicidad,self.k) #Retornamos una instancia de Estado con los atributos resultantes

    def __repr__(self):
        return f"ESTADO: {self._coste} {self._felicidad}"

    def heuristic_basico(self):
        '''
        Función heurística que busca minimizar el coste y augmentar la felicidad sin ponderación
        '''
        return -self._coste
    
    def heuristic_ponderado(self):
        '''
        Función heurística que busca minimizar el coste y augmentar la felicidad teniendo 
        en cuenta la ponderación
        '''
        return self.k*float(self._felicidad)-self._coste
    
    def heuristic_entropia(self):
        '''
        Función heurística que busca minimizar el coste y la entropía y augmentar la 
        felicidad teniendo en cuenta la ponderación
        '''
        total_entropy=0
        for oferta,lista_paquetes in self._asignaciones.items():
            pesomax=self._transporte.pesomax(oferta)
            peso_libre=pesomax
            for paquete in lista_paquetes:
                peso_libre-=self._paquetes.peso(paquete)
            occupancy=peso_libre/pesomax
            total_entropy = total_entropy + (occupancy * math.log(occupancy))
        return  self.k*float(self._felicidad)-self._coste - self.e*total_entropy
    
def estado_inicial(paquetes: Paquetes,transporte: Transporte,k=1):
    '''
    Función que genera el estado inicial del problema ordenando los paquetes por prioridad 
    y las ofertas por dia. Crea un estado inicial que cumple todas las prioridades y que tiene felicidad=0
    '''
    paquetes.ordenar()
    diccionario={}
    cont=0
    peso_libre=0
    coste=0
    oferta=(-1,-1)
    while paquetes.paquetes_sin_asignar(): #Vamos asignando paquetes haste que no queden más
        peso,prioridad=paquetes.primer_paquete(cont)
        dia= 3 if prioridad==2 else prioridad
        if dia>oferta[0] or peso_libre<peso: #Cuando cambia la prioridad del paquede o se llena la oferta cambiamos de oferta
            oferta,peso_libre,coste_oferta=transporte.get_oferta(dia)
            diccionario[oferta]=[cont]
            
        else:
            diccionario[oferta].append(cont)
        coste+=coste_oferta*peso #Sumamos el coste de la oferta
        peso_libre-=peso
        cont+=1
        paquetes.asignar()
        coste+=peso*0.25*(2 if oferta[0]==4 else 1) if oferta[0]>=2 else 0 #Sumamos el coste de almacén
        coste += 1.5*(1+ ((oferta[0]+1)//2)%2) if ((oferta[0]+1)//2)>0 else 5 #Sumamos el coste de envío

    return Estado(diccionario,transporte,paquetes,coste,0,k)

def estado_inicial_aleatorio(paquetes: Paquetes,transporte: Transporte,k=1):
    '''
    Función que genera el estado inicial del problema asignando una oferta aleatoria de la prioridad 
    de cada paquete. Crea un estado inicial que cumple todas las prioridades y que tiene felicidad=0
    '''
    diccionario={}
    cont=0
    coste=0
    oferta=(-1,-1)
    prioridad_ofertas=[transporte.ofertas_prioridad_estricta(0),transporte.ofertas_prioridad_estricta(1),transporte.ofertas_prioridad_estricta(2)]
    
    pesos_libres_oferta=[[50 for _ in range(len(transporte._ofertas_ordenadas[i]))] for i in range(5)]

    while paquetes.paquetes_sin_asignar(): #Vamos asignando paquetes haste que no queden más
        peso,prioridad=paquetes.primer_paquete(cont)
        no_cabe=True
        while no_cabe: #Buscamos una oferta random hasta que encontremos una donde quepa
            oferta=random.choice(prioridad_ofertas[prioridad])
            if peso<=pesos_libres_oferta[oferta[0]][oferta[1]]:
                no_cabe=False
                
        if oferta not in diccionario: #Si es una oferta nueva
            diccionario[oferta]=[cont]
            pesos_libres_oferta[oferta[0]][oferta[1]]=transporte.pesomax(oferta)-peso
        
        else:
            diccionario[oferta].append(cont) #Si es una oferta que ya usamos
            pesos_libres_oferta[oferta[0]][oferta[1]]-=peso   

        coste+=transporte.coste(oferta)*peso #Sumamos el coste de la oferta
        cont+=1
        paquetes.asignar()
        coste+=peso*0.25*(2 if oferta[0]==4 else 1) if oferta[0]>=2 else 0 #Sumamos el coste del almacén
        coste += 1.5*(1+ ((oferta[0]+1)//2)%2) if ((oferta[0]+1)//2)>0 else 5 #Sumamos el coste de envío

    return Estado(diccionario,transporte,paquetes,coste,0,k)