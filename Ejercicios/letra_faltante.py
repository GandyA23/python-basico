# Mencionar que letra hace falta en una lista de letras

# Mi solución
def missingletters (letters):
    if not len(letters):
        return 

    letters.sort()
    indice = 0
    missing_letters = []
    first_letter = letters[indice]

    while indice < len(letters):
        while first_letter != letters[indice]:
            missing_letters.append(first_letter)
            # Convert to ASCII value (int) and then convert again in char
            first_letter = chr(ord(first_letter)+1)
            
        first_letter = chr(ord(first_letter)+1)
        indice += 1
        
    return missing_letters

# Solución de Arturo Sacramento Lopez Gonzalez
def letra_faltante(lista_letras):
    indice = 0
    while ord(lista_letras[indice])+1 == ord(lista_letras[indice+1]):
        indice += 1

    return chr(ord(lista_letras[indice]) + 1)

if __name__ == '__main__':
    letters1 = ['a', 'c']
    letters2 = ['E', 'I', 'O']

    print(missingletters(letters1))
    print(missingletters(letters2))

