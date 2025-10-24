from persona import Persona

unaPersona = Persona("greivin","perez","conejo","Alajuela", "02-01-1997")
otraPersona = Persona("Maria", "Solis", "Rojas", "San Jose", "03-01-2000")
elClon = Persona("greivin","perez","conejo","Alajuela", "02-01-1997")
print(unaPersona)
print(otraPersona)
print(elClon)
otroClon = unaPersona
print(otroClon)

if unaPersona == elClon:
    print("Son lo mismo")
else:
    print("Son lo mismo")



