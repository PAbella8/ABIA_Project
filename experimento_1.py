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
def generar_random(num=1):
    semilla = random.randint(1000,9999)
    paquetes=Paquetes(num_paquetes,semilla)
    transporte=Transporte(paquetes._lista_paquetes,1.2,semilla)
    p=Problema(estado_inicial_aleatorio(paquetes,transporte,num))
    return p

semillas = [random.randint(1000,9999) for _ in range(10)]
time_no_so=[]
pasos_no_so=[]
time_so=[]
pasos_so=[]
costes_no_so=[]
costes_so=[]
print(semillas)
for semilla in semillas:
    num = 1
    paquetes=Paquetes(num_paquetes,semilla)
    transporte=Transporte(paquetes._lista_paquetes,1.2,semilla)
    p=Problema(estado_inicial(paquetes,transporte),num)
    time = []
    paso = []
    coste = []
    for _ in range(10):
        #sol = hill_climbing(p)
        time.append(timeit(lambda: coste.append(hill_climbing(p)._coste),number=1))
        #coste.append(sol._coste)        
        paso.append(p.pasos)
        
    time_no_so.append(sum(time) / len(time))
    pasos_no_so.append(sum(paso) / len(paso))
    costes_no_so.append(sum(coste) / len(coste))
    print(semilla)
    
for semilla in semillas:
    num = 1
    paquetes=Paquetes(num_paquetes,semilla)
    transporte=Transporte(paquetes._lista_paquetes,1.2,semilla)
    p=Problema(estado_inicial_aleatorio(paquetes,transporte),num)
    time = []
    paso = []
    coste = []
    for _ in range(10):
        #sol = hill_climbing(p)
        #coste.append(sol._coste)
        time.append(timeit(lambda: coste.append(hill_climbing(p)._coste),number=1))
        paso.append(p.pasos)
    time_so.append(sum(time) / len(time))
    pasos_so.append(sum(paso) / len(paso))
    
    costes_so.append(sum(coste) / len(coste))
    print(semilla)


print(time_no_so)
print(time_so)
data_time = [time_no_so,time_so]
labels_time = ['Estado inicial por días', 'Estado inicial aleatorio']
plt.boxplot(data_time,tick_labels=labels_time)
plt.ylabel('Tiempo de ejecución en segundos')
plt.title('Comparativa tiempo según el generador del estado inicial con Boxplots')
plt.savefig('test_time_ei.png')
plt.clf()

print(pasos_no_so)
print(pasos_so)
data_pasos = [pasos_no_so,pasos_so]
labels_pasos = ['Estado inicial por días', 'Estado inicial aleatorio']
plt.boxplot(data_pasos,tick_labels=labels_pasos)
plt.ylabel('Pasos de ejecución en segundos')
plt.title('Comparativa pasos según el generador del estado inicial con Boxplots')
plt.savefig('test_pasos_ei.png')
plt.clf()


print(costes_no_so)
print(costes_so)
data_costes = [costes_no_so,costes_so]
labels_costes = ['Estado inicial por días', 'Estado inicial aleatorio']
plt.boxplot(data_costes,tick_labels=labels_costes)
plt.ylabel('Costes de la solución final en euros')
plt.title('Comparativa costes según el generador del estado inicial con Boxplots')
plt.savefig('test_costes_ei.png')