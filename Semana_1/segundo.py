leido1 = input("Escriba un numero entre 1 y 5 ")
leido2 = input("Escriba su nombre ")

#y podemos darle formato a la salida
print("Escribio el numero " + leido1 + " y el nombre " + leido2)


#variante
leido1 = int(input("Escriba un numero entre 1 y 5 "))
leido2 = input("Escriba su nombre ")

#y podemos darle formato a la salida ... pero esto falla porque leido1 es un int
#print("Escribio el numero " + leido1 + " y el nombre " + leido2)

#para arreglarlo usamos la funcion str()
print("Escribio el numero " + str(leido1) + " y el nombre " + leido2)