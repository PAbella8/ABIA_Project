from abia_azamon import *
class Transporte(object):
    '''
    Clase que representa todas las ofertas del problema con 3 atributos: 
    las ofertas desordenadas, las ofertas clasificadas, y las ofertas no asignadas.
    '''
    def __init__(self, lista_paquetes: list, prop: float, semilla: int):
        self._lista_ofertas = random_ofertas(lista_paquetes,prop,semilla) #lista inicial de ofertas
        self._ofertas_ordenadas=[[],[],[],[],[]] #clasificamos las ofertas por dia
        for oferta in self._lista_ofertas:
            self._ofertas_ordenadas[oferta.dias-1].append(oferta)
        self._ofertas_no_asignadas=[len(lista) for lista in self._ofertas_ordenadas] #número de ofertas no asignadas por dia

    def get_oferta(self,dia):
        '''
        Método que retorna una oferta de un dia determinado.
        '''
        if self._ofertas_no_asignadas[dia]==0:
            dia=dia+1
        pos_2=len(self._ofertas_ordenadas[dia])-self._ofertas_no_asignadas[dia]
        self._ofertas_no_asignadas[dia]-=1
        oferta=self._ofertas_ordenadas[dia][pos_2]
        return (dia,pos_2),oferta.pesomax, oferta.precio
    
    def coste(self,oferta):
        '''
        A partir del identificador de la oferta (su posición en la lista) obtenemos su coste.
        '''
        return self._ofertas_ordenadas[oferta[0]][oferta[1]].precio

    def pesomax(self,oferta):
        '''
        A partir del identificador de la oferta (su posición en la lista) obtenemos su pso máximo.
        '''
        return self._ofertas_ordenadas[oferta[0]][oferta[1]].pesomax
    
    def ofertas_prioridad(self,prioridad):
        '''
        Método que retorna una lista con los identificadores de todas las ofertas que
        cumplen con una determinada prioridad (incluye aquellos de prioridad inferior)
        '''
        dia=prioridad*2
        ofertas=[]
        for i in range(dia+1):
            ofertas+=[(i,j) for j in range(len(self._ofertas_ordenadas[i]))]
        return ofertas
    
    def ofertas_prioridad_estricta(self,prioridad):
        '''
        Método que retorna una lista con los identificadores de todas las ofertas
        que tienen una determinada prioridad (no incluye aquellos de prioridad inferior)
        '''
        dia=prioridad*2
        ofertas=[]
        for i in range(max(0,dia-1),dia+1):
            ofertas+=[(i,j) for j in range(len(self._ofertas_ordenadas[i]))]
        return ofertas
