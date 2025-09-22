"Leer 5 numeros y luego imprimir el mas grande y el mas pequeño"

numeros = [int(input("Ingresar un numero: ")) for _ in range(5)]
print("Numero mayor:", max(numeros))
print("Numero menor:", min(numeros))
