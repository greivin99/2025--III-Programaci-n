class Producto:
    def __init__(self, nombre, categoria, precio, proveedor):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__proveedor = proveedor

    def __str__(self):
        return f"{self.__id if hasattr(self, '_Producto__id') else '?'} - {self.__nombre} ({self.__categoria}), Precio: {self.__precio}, Proveedor: {self.__proveedor}"

    @property
    def nombre(self):
        return self.__nombre

    @property
    def categoria(self):
        return self.__categoria

    @property
    def precio(self):
        return self.__precio

    @property
    def proveedor(self):
        return self.__proveedor

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @proveedor.setter
    def proveedor(self, nuevo_proveedor):
        self.__proveedor = nuevo_proveedor

    def set_id(self, pid):
        self.__id = pid
