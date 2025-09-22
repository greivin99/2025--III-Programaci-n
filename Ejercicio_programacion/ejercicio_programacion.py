def choque_asteroides(lista):
    res = [0] * len(lista)

    for i in range(len(lista)):
        if i < len(lista) - 1 and lista[i] > 0 and lista[i+1] < 0:
            choque = lista[i] + lista[i+1]
            if abs(lista[i]) >= abs(lista[i+1]):
                res[i] = choque
            else:
                res[i+1] = choque
        elif res[i] == 0:
            res[i] = lista[i]

    return res

print(choque_asteroides([5,1,10,-5]))
print(choque_asteroides([3,-2,52,87]))
print(choque_asteroides([3,2,9,-5]))
print(choque_asteroides([10,-28,15,1]))
print(choque_asteroides([11,55,9,-5,210]))
print(choque_asteroides([7,9,-4,-15,10]))