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
def incrementar_peso_transportable(n,semilla):
    #semilla = random.randint(1000,9999)
    
    #tiempos = []
    costes = []
    for i in range(n):
        
        #tiempo= []
        coste = []
        for _ in range(10):
            paquetes=Paquetes(num_paquetes,semilla)
            transporte=Transporte(paquetes._lista_paquetes,1.2+i*0.2,semilla)
            p = Problema(estado_inicial_aleatorio(paquetes,transporte),1)
            coste.append(hill_climbing(p)._coste)
            #tiempo.append(timeit(lambda: hill_climbing(p),number=1))
        #tiempos.append(sum(tiempo) / len(tiempo))
        costes.append(sum(coste)/len(coste))
    #print(tiempos)
    return costes# semilla, costes

def incrementar_paquetes(l):
    semilla = random.randint(1000,9999)
    
    tiempos = []
    for i in range(l):
        
        tiempo= []
        for _ in range(10):
            paquetes=Paquetes(num_paquetes+10*i,semilla)
            transporte=Transporte(paquetes._lista_paquetes,1.2,semilla)
            p = Problema(estado_inicial_aleatorio(paquetes,transporte),1)
            tiempo.append(timeit(lambda: hill_climbing(p),number=1))
        tiempos.append(sum(tiempo) / len(tiempo))
    print(tiempos)
    return semilla, tiempos

semillas = [3962,2781,2037,7852,5759]
tendencias = []

for j in range(5):
    num = 10
    sem = semillas[j]
    tendencia = incrementar_peso_transportable(num,sem)
    semillas.append(sem)
    tendencias.append(tendencia)
    proporciones = [1.2+k*0.2 for k in range(num)]
    plt.plot(proporciones,tendencia,label=f'semilla {sem}')

print(semillas)
print(tendencias)

plt.legend()
plt.title('Costes de ejecución en función de la proporción del peso transportable')
plt.savefig('tendencia_proporcion_costes.png')