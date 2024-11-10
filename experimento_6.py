import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from timeit import timeit
import random

from Problem import Problema
from Estado import estado_inicial, estado_inicial_aleatorio
from Paquetes import Paquetes
from Transporte import Transporte
from aima.search import hill_climbing, simulated_annealing

num_paquetes = 50
def ponderaciones(num,semilla):
    tiempos=[]
    costes = []
    for val in range(num):
        
        coste= []
        time=[]
        for _ in range(5):
            paquetes=Paquetes(num_paquetes,semilla)
            transporte=Transporte(paquetes._lista_paquetes,1.2,semilla)
            p = Problema(estado_inicial_aleatorio(paquetes,transporte,val),1,'Ponderado')
            time.append(timeit(lambda: coste.append(hill_climbing(p)._coste),number=1))
        costes.append(sum(coste) / len(coste))
        tiempos.append(sum(time)/len(time))
    return tiempos

semillas=[1814, 6627, 2530, 1718, 5707]
pesos=[]
for j in range(5):
    n=20
    sem = semillas[j]
    precios = ponderaciones(n,sem)
    proporciones = [i for i in range(n)]

    pesos.append(precios) 
    plt.plot(proporciones,precios,label=f'semilla {sem}')
    
    
print(semillas)
print(pesos)

plt.legend()
plt.title('Tiempo de ejecución en función de la ponderación de la felicidad')
plt.savefig('tiempo_ponderaciones.png')