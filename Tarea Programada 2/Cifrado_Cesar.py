def cifrar_cesar(texto, desplazamiento):
    resultado = []
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nuevo = (ord(char) - base + desplazamiento) % 26 + base
            resultado.append(chr(nuevo))
        else:
            resultado.append(char)
    return ''.join(resultado)


def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento) # Deciframos igual, solo que con desplazamiento inverso
