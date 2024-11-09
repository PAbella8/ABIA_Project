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
import timeit

num_paquetes=50
semilla=1234
paquetes=Paquetes(num_paquetes,semilla)
transporte=Transporte(paquetes._lista_paquetes,1.2,semilla)

p=Problema(estado_inicial_aleatorio(paquetes,transporte))
problema,costes=simulated_annealing(p)
#print(timeit.timeit(lambda: hill_climbing(Problema(estado_inicial(paquetes,transporte))), number=10))
print('solución:',problema._asignaciones,problema._coste,problema._felicidad)
print(p.pasos)
print(len(costes))
plt.plot([i for i in range(1000)],costes)
plt.title('Evolución del coste')
plt.savefig('evo_coste3.png')

'''
for oferta in transporte._lista_ofertas:
    print(oferta)
for paquete in range(len(paquetes._lista_paquetes)):
    print(paquete,end=' ')
    print(paquetes._lista_paquetes[paquete])
    '''