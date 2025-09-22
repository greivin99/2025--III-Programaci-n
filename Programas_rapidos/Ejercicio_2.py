"Guardar numeros pares e impares"

lista_pares = []
lista_impares = []

while True:
    num = int(input("Ingresar número (negativo para terminar): "))
    if num < 0:
        break
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print("# pares:", len(lista_pares))
print("# impares:", len(lista_impares))