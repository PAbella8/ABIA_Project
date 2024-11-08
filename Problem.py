from aima.search import Problem
from Estado import Estado
from Acciones import Actions

class Problema(Problem):
    '''
    Clase que  implementa el problema. Hereda de Problem (AIMA), lo que la permite usar
    los algoritmos de búsqueda.
    '''
    def __init__(self, initial,extendido=1):
        self.pasos=0
        self.extendido=extendido
        super().__init__(initial)
    
    def actions(self,estado):
        return estado.acciones(self.extendido)
    
    def result(self,estado,accion):
        #print(estado._asignaciones)
        return estado.aplicar_accion(accion)
    
    def value(self,estado):
        self.pasos+=1
        #print(estado._asignaciones)
        return estado.heuristic_basico()
    
    def goal_test(self, state):
        return False