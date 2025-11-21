from Animal import Animal
from Gato import Gato
from Perro import Perro

un_perro = Perro("Zapote", 4 , "Chihuahua")
un_gato = Gato("Caliche", 10, "Naranja")
cualquiera = Animal("?", 3)

#isinstance verifica OBJETOS en el arbol de herencia
print(isinstance(cualquiera, Animal))
print(isinstance(un_perro, Animal))
print(isinstance(un_gato, Animal))

#issubclass verifica clases en el arbol de herencia
print(issubclass(Perro, Animal))
print(issubclass(Gato, Animal))
