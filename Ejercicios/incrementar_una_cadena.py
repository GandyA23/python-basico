# Función que sume 1 al número final de una palabra

# Mi solución
def plus_one_to_end(word: str) -> str:
    i = 0

    while i < len(word) and (not word[i].isdigit() or word[i] == '0'):
        i += 1

    return word[0:i] + str(int('0' + word[i:])+1)   

# Solución de Arturo Sacramento Lopez Gonzalez
def incrementar_cadena (cadena: str):
    cadena_separada = ["", ""]
    for elemento in cadena:
        cadena_separada[1 if elemento.isdigit() else 0] += elemento
    # zfill rellena de 0 si la longitud de la cadena es menor al tamaño original
    cadena_separada[1] = "1" if not cadena_separada[1] else str(int(cadena_separada[1]) + 1).zfill(len(cadena_separada[1]))
    return "".join(cadena_separada)

if __name__ == '__main__':
    str1 = 'hola'
    str2 = 'hola000034'
    str3 = 'hola908'
    str4 = 'hola000'
    str5 = 'hola010'
    str6 = 'hola099'
    str7 = 'hola99'

    print(plus_one_to_end(str1))
    print(plus_one_to_end(str2))
    print(plus_one_to_end(str3))
    print(plus_one_to_end(str4))
    print(plus_one_to_end(str5))
    print(plus_one_to_end(str6))
    print(plus_one_to_end(str7))

    print(incrementar_cadena(str1))
    print(incrementar_cadena(str2))
    print(incrementar_cadena(str3))
    print(incrementar_cadena(str4))
    print(incrementar_cadena(str5))
    print(incrementar_cadena(str6))
    print(incrementar_cadena(str7))