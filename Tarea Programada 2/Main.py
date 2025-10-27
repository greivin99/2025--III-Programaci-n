from Cifrado_Cesar import cifrar_cesar, descifrar_cesar
from Cifrado_Vigenere import cifrar_vigenere, descifrar_vigenere
from other_code import limpiar_texto, solicitar_entrada


def main():
    print("Vamos a cifrar texto!\n")
    texto = input("Ingrese el texto a cifrar: ")
    texto = limpiar_texto(texto)

    algoritmo = solicitar_entrada("En que algoritmo cifrar? cesar o vigenere: ", ["cesar", "vigenere"])
    accion = solicitar_entrada("ACCION: encriptar (1) o desencriptar (2)? Opcion: 1 o 2: ", ["1", "2"])

    if algoritmo == "cesar":
        while True:
            try:
                desplazamiento = int(input("Ingresar el desplazamiento: "))
                break
            except ValueError:
                print("Ingresar un numero válido.")
        if accion == "1":
            resultado = cifrar_cesar(texto, desplazamiento)
        else:
            resultado = descifrar_cesar(texto, desplazamiento)

    else:
        clave = input("Ingresar palabra clave: ").strip().lower()
        if accion == "1":
            resultado = cifrar_vigenere(texto, clave)
        else:
            resultado = descifrar_vigenere(texto, clave)

    print("\n↓↓↓ RESULTADO ↓↓↓")
    print(resultado)


if __name__ == "__main__":
    main()
