"Guardar palabras y luego traer la posicion elegida"


rango = int(input("Palabras que quedemos ingresar: "))
palabras = tuple(input("Ingresar palabras: ") for _ in range(rango))

pos = int(input("Posicion de la palabra a traer (0 a {}): ".format(rango-1)))
print("Palabra en la posicion", pos, ":", palabras[pos])
