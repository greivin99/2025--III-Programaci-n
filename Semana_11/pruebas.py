from Animal import Animal
from Perro import Perro
from Gato import Gato

mi_animal = Animal("yoyo",15)
print(mi_animal)
print(mi_animal.hacer_sonido())

mi_perro = Perro("capita", 7, "Pastor")
print(mi_perro)
mi_perro.nombre = "caspita"
print(mi_perro)
print(mi_perro.hacer_sonido())

gato_volador = Gato("Felix", 10, "naranjoso")
print(gato_volador)
print(gato_volador.ronronear())
print(gato_volador.hacer_sonido())