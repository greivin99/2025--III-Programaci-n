from datetime import datetime

class Persona:

    def __init__(self, nombre, apellido1, apellido2, direccion, fechaNac):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.direccion = direccion
        self.fecha_nacimiento = fechaNac
        
    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2} from {self.direccion}, nacio {self.fecha_nacimiento}"
    
    def __eq__(self,other): 
        if not isinstance(other, Persona):
            return false
        return self.nombre == other.nombre and self.apellido1 == other.apellido1 \
                and self.apellido2 == other.apellido2 and self.direccion == other.direccion \
                and self.fecha_nacimiento == other.fecha_nacimiento
                
    def __lt__(self, other): #si el self es menor que other. 
        if not isinstance(other, Persona):
            return false
        date1 = datetime.strptime(self.fecha_nacimiento, "%d-%m-%Y").date()
        date2 = datetime.strptime(other.fecha_nacimiento, "%d-%m-%Y").date()
        return date1 < date2