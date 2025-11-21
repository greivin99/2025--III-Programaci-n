from Animal import Animal

class Perro(Animal):
    
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza
        
    def __str__(self):
        return f"Perro {self._raza}, nombre: {self._nombre}, edad: {self._edad}"
    
    def hacer_sonido(self):
        return "GUAU GUAU"
        
    