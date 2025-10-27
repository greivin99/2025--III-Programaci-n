def limpiar_texto(texto):
    return ' '.join(texto.strip().lower().split())


def solicitar_entrada(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion in opciones_validas:
            return opcion
        print(f"Opcion no valida. Debe elegir entre opcion: {', '.join(opciones_validas)}")
