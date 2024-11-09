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
    
    costes = []
    for val in range(num+1):
        peso = val/num
        
        coste= []
        for _ in range(3):
            paquetes=Paquetes(num_paquetes,semilla)
            transporte=Transporte(paquetes._lista_paquetes,1.2,semilla)
            p = Problema(estado_inicial_aleatorio(paquetes,transporte,peso),1,'Ponderado')
            coste.append(hill_climbing(p)._coste)
        costes.append(sum(coste) / len(coste))
    return costes

semillas=[]
pesos=[]
for j in range(5):
    n=10
    sem = random.randint(1000,9999)
    precios = ponderaciones(n,sem)
    proporciones = [k/n for k in range(n+1)]
    semillas.append(sem) 
    plt.plot(proporciones,precios,label=f'semilla {sem}')
    
    
print(semillas)
print(pesos)

plt.legend()
plt.title('Costes en función de la ponderación de la felicidad')
plt.savefig('costes_ponderaciones.png')