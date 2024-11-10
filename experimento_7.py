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
            p = Problema(estado_inicial_aleatorio(paquetes,transporte,val),1,'Ponderado',True)
            time.append(timeit(lambda: coste.append(simulated_annealing(p)._felicidad),number=1))
        costes.append(sum(coste) / len(coste))
        tiempos.append(sum(time)/len(time))
    return costes

n=20
semillas=[4925,1068,2850,1976,1735]
pesos=[]
times=[]
proporciones = [i for i in range(n)]
for j in range(5):
    sem = semillas[j]
    #semillas.append(sem)
    precios = ponderaciones(n,sem)    
    #times.append(tiempo)
    pesos.append(precios) 
    plt.plot(proporciones,precios,label=f'semilla {sem}')
    
    
print(semillas)
print(pesos)

plt.legend()
plt.title('Felicidad en función de la ponderación de la felicidad')
plt.savefig('felicidad_sim_ann.png')
'''
plt.clf()
for i in range(len(pesos)):
    plt.plot(proporciones,times[i],label=f'semilla {semillas[i]}')

plt.title('Tiempo de ejecución en función de la ponderación de la felicidad')
plt.savefig('tiempos_sim_ann.png')
'''