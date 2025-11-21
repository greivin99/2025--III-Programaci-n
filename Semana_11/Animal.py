class Animal:
    
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    @property
    def nombre(self):
        return self._nombre.title()
    
    @property
    def edad(self):
        return self._edad
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
        
    @edad.setter
    def edad(self, nuevo_valor):
        if nuevo_valor <0:
            print(f"Error: Edad no puede ser <0")
            self._edad = None
        else:
            self._edad = nuevo_valor
            
    def hacer_sonido(self):
        return "(cualquier sonido)"
    
    def __str__(self):
        return f'{self._nombre} tiene {self._edad} años'
    