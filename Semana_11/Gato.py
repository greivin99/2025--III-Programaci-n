from Animal import Animal

class Gato(Animal):
    
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color
    
    def hacer_sonido(self):
        return "miaaaaaaaau"
    
    def ronronear(self):
        return f"{self.nombre} esta haciendo BRRRRRR"
    
        