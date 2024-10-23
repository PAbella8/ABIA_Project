class Oferta(object):
    """
    Clase que representa una oferta de transporte con tres atributos,
    el peso máximo que se puede transportar, el precio por kilogramo
    y el número de días en los que se entregara.
    """

    def __init__(self, pesomax: float, precio: float, dias: int):
        """
        Constructora: asigna valores a una oferta de transporte
        :param pesomax: Peso máximo que se puede transportar
        :param precio: Precio por kilogramo
        :param dias: Días hasta que se haga la entrega
        """
        self.pesomax = pesomax
        self.precio = precio
        self.dias = dias

    def __str__(self):
        return f"#Oferta# pesomax ({self.pesomax}) kg" \
               f" precio({self.precio})" \
               f" dias ({self.dias})"