from Problem import Problema
from Estado import estado_inicial
from Paquetes import Paquetes
from Transporte import Transporte
from aima.search import hill_climbing, simulated_annealing

num_paquetes=9
semilla=1111
paquetes=Paquetes(num_paquetes,semilla)

problema=hill_climbing(Problema(estado_inicial(paquetes,Transporte(paquetes._lista_paquetes,1.2,semilla))))
print(problema)