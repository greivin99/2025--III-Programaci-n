from Cuenta import Cuenta
from Cliente import Cliente
class Tarjeta:

    def __init__(self, numero, cliente: Cliente, cuenta: Cuenta):
        self.__numero = numero
        self.__cuenta = cuenta
        self.__cliente = cliente

    def __str__(self):
        return f"Tarjeta: {self.__numero}, de {self.__cliente}, asociada a: {self.__cuenta}"

    def cargoTarjeta(self, amount):
        return self.__cuenta.debito(amount)