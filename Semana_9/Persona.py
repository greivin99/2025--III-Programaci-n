from datetime import datetime 

class Persona:

    def __init__(self, nombre,apellido1,apellido2,direccion, fecha_nacimiento):
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__direccion = direccion
        self.__fecha_nacimiento = fecha_nacimiento
        self.__apodo = ""

    def __str__(self):
        return f"{self.__nombre} {self.__apellido1} {self.__apellido2},{self.__direccion}, nacido {self.__fecha_nacimiento}"

    # esto seria como un "getter"
    @property 
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        fecha_persona = datetime.strptime(self.__fecha_nacimiento, "%Y-%m-%d").date()
        hoy = datetime.today().date()
        edad = hoy.year - fecha_persona.year
        if (hoy.month, hoy.day) < (fecha_persona.month, fecha_persona.day):
            edad = edad - 1
        return edad

    @property 
    def apodo(self):
        return self.__apodo

    @apodo.setter
    def apodo(self, apodo):
        self.__apodo = apodo

    @property
    def direccion(self):
        return self.__direccion
    
    @property
    def primer_apellido(self):
        return self.__apellido1
    
    @property
    def segundo_apellido(self):
        return self.__apellido2
    
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento