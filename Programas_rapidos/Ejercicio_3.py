"Ingresar # de palabras y guardarlas"

rango = int(input("Numero de palabras que queremos ingresar: "))
palabras = set()

for contador in range(rango):
    palabra = input("Ingresar palabra: ")
    palabras.add(palabra)

print("Palabras guardadas:", palabras)