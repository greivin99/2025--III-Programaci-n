from Movimiento import Movimiento

class Cuenta:

    def __init__(self, numero, saldo, tipo, tasa):
        self.__numero = numero
        self.__saldo = saldo
        self.__tipo = tipo
        self.__tasa = tasa
        self.__movimientos = [Movimiento(saldo, credito)]
        # la relacion entre movimiento y cuenta es de COMPOSICION. 
        # porque los movimientos no pueden existir sin una cuenta 
        # ni fuera de ella. 
        #cuando hay una composicion los objetos no se pueden crear fuera del 
        #contenedor

    def __str__(str):
        return f"cuenta {self.__numero}, {self.__tipo}."

    def credito(self, amount):
        self.__saldo = self.__saldo + amount
        self.__movimientos.append(Movimiento(amount, "credito"))


    def debito(self, amount):
        if amount > self.__saldo:
            return False
        else: 
            self.__saldo = self.__saldo - amount
            self.__movimientos.append(Movimiento(amount, "debito"))
            return True