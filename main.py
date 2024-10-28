from Problem import Problema
from Estado import estado_inicial
from Paquetes import Paquetes
from Transporte import Transporte
from aima.search import hill_climbing, simulated_annealing

num_paquetes=20
semilla=1235
paquetes=Paquetes(num_paquetes,semilla)
transporte=Transporte(paquetes._lista_paquetes,1.2,semilla)

problema=simulated_annealing(Problema(estado_inicial(paquetes,transporte)))
print('solución:',problema._asignaciones,problema._coste,problema._felicidad)
for oferta in transporte._lista_ofertas:
    print(oferta)
for paquete in paquetes._lista_paquetes:
    print(paquete)