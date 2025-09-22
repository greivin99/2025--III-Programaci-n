"Pedir palabras y luego imprimir la mas larga"

rango = int(input("Numero de palabras que queremos ingresar: "))
palabras = [input("Ingresar palabra: ") for _ in range(rango)]

print("La palabra mas larga es:", max(palabras, key=len))
