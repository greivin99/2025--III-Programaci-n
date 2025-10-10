def main():
    asteroides = leer_lista()
    procesar_lista(asteroides)
    
def leer_lista():
    str_lista = input("ingrese la lista de numeros enteros, separados por coma: ")
    return str_lista.split(',')

def procesar_lista(lista_asteroides):
    temp = []
    for indice in range(0, len(lista_asteroides)-1):
        temp.append(process_pair(int(lista_asteroides[indice]), int(lista_asteroides[indice+1])))
    result = []
    for pair in temp:
        if len(result) == 0:
            result.append(pair[0])
            result.append(pair[1])
        else:
            if pair[0] == pair[1] == 0:
                result.append(0)
            else:
                result.pop()
                result.append(pair[0])
                result.append(pair[1])
    print(result)

def process_pair(first, second):
    if first > 0 and second < 0:
        return [first - second, 0]
    elif first < 0 and second > 0:
        return [0, second - first]
    elif first > 0 and second > 0:
        return [0,0]
    elif first < 0 and second < 0:
        return [0,0]
    else: 
        return [0,0]


main()
