# Función que regresa un hashtag de una frase o palabra

def generador_hashtag (cadena: str):
    if not cadena:
        return False

    lista_palabras = cadena.split()
    return_cadena = ''
    for palabra in lista_palabras:
        return_cadena += palabra.capitalize()
    return '#' + return_cadena
    
if __name__ == '__main__':
    str1 = 'Curso de Python'
    str2 = 'a s l g'

    print(generador_hashtag(str1))
    print(generador_hashtag(str2))