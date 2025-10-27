def generar_clave(texto, clave):
    clave = clave.lower()
    clave_completa = ""
    indice = 0
    for char in texto:
        if char.isalpha():
            clave_completa += clave[indice % len(clave)]
            indice += 1
        else:
            clave_completa += char
    return clave_completa


def cifrar_vigenere(texto, clave):
    texto = texto.lower()
    clave_completa = generar_clave(texto, clave)
    resultado = []

    for t, k in zip(texto, clave_completa):
        if t.isalpha():
            desplazamiento = (ord(k) - ord('a')) % 26
            nuevo = chr((ord(t) - ord('a') + desplazamiento) % 26 + ord('a'))
            resultado.append(nuevo)
        else:
            resultado.append(t)

    return ''.join(resultado)


def descifrar_vigenere(texto, clave):
    texto = texto.lower()
    clave_completa = generar_clave(texto, clave)
    resultado = []

    for t, k in zip(texto, clave_completa):
        if t.isalpha():
            desplazamiento = (ord(k) - ord('a')) % 26
            nuevo = chr((ord(t) - ord('a') - desplazamiento) % 26 + ord('a'))
            resultado.append(nuevo)
        else:
            resultado.append(t)

    return ''.join(resultado)
