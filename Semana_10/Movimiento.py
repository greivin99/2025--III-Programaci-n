from datetime import datetime

class Movimiento:

    def __init__(self, tipo, monto):
        self.__tipo = tipo
        self.__monto = monto
        self.__datetime = datetime.now().isoformat()

    def __str__(self):
        return f"{self.__tipo}, {self.__monto} at {self.__datetime}"