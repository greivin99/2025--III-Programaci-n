class Cliente:

    def __init__(self,id, nombre,categoria):
        self.__id = id
        self.__nombre = nombre
        self.__categoria = categoria
        self.__cuentas = [] 
        #LA RELACION cliente - cuentas seria una 
        #agregación. el cliente no necesita
        #cuentas para existir. y la cuenta 
        #aunque esta ligada al cliente es bastante 
        #independiente: usted no tiene que editar al cliente
        #para modificar la cuenta. 

    def __str__(self):
        return f"cliente #{self.__id}, {self.__nombre}. Cat: {self.__categoria}"
    
    def agregarCuenta(self, nuevaCuenta):
        self.__cuentas.append(nuevaCuenta)