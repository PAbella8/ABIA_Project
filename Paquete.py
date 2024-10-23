class Paquete(object):
    """
    Clase que representa un paquete con dos atributos,
    su peso y su prioridad
    """

    def __init__(self, peso: float, prioridad: int):
        """
        Constructora: genera un paquete con un peso y una prioridad
        :param peso: Peso de un paquete
        :param prioridad: Prioridad de un paquete
        (valor 0 ⇾ Paquetes de prioridad 1 = entrega en un día,
         valor 1 ⇾ Paquetes de prioridad 2 = entrega entre 2 y 3 días,
         valor 2 ⇾ Paquetes de prioridad 3 = entrega entre 4 y 5 días)
        """
        self.peso = peso
        self.prioridad = prioridad

    def __str__(self):
        return f"#Paquete# peso({self.peso})" \
               f" prioridad({self.prioridad})"