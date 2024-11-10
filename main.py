from Problem import Problema
from Estado import estado_inicial, estado_inicial_aleatorio
from Paquetes import Paquetes
from Transporte import Transporte
from aima.search import hill_climbing, simulated_annealing

num_paquetes=50
semilla=1234
paquetes=Paquetes(num_paquetes,semilla)
transporte=Transporte(paquetes._lista_paquetes,1.2,semilla)

p=Problema(estado_inicial_aleatorio(paquetes,transporte),simulated_annealing=True)
problema=simulated_annealing(p)
print('solución:',problema._asignaciones,'\n Coste:',problema._coste,'\n Felicidad:',problema._felicidad)
