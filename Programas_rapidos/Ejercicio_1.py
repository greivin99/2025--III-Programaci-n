"Suma de # pares"

suma = 0
while True:
    num = int(input("Ingrese un número (-1 para terminar): "))
    if num == -1:
        break
    if num % 2 == 0:
        suma += num
print("# pares total suma:", suma)