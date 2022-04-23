# Crear una función que nos retorne los elementos diferentes de dos listas

# Mi solución
def getdiffencesinlists (l1, l2):   
    for b in l2:
        while b in l1:
            l1.remove(b)
    return l1

# Solución de Arturo Sacramento Lopez Gonzalez
# Primera solución
def diferencias_listas1(lista_origen, lista_resta):
    for elemento_b in lista_resta:
        while elemento_b in lista_origen:
            lista_origen.remove(elemento_b)
    return lista_origen

# Segunda solución
def diferencias_listas2(lista_origen, lista_resta):
    lista_return = []
    for elemento in lista_origen:
        if elemento not in lista_resta:
            lista_return.append(elemento)
    return lista_return

# Tercera solución
def diferencias_listas3(lista_origen, lista_resta):
    return [x for x in lista_origen if x not in lista_resta]


if __name__ == '__main__':
    list11 = [1, 2] 
    list12 = [1]

    list21 = [1, 2, 3, 4, 5] 
    list22 = [1, 2, 3, 4]
    
    list31 = [1, 2, 3] 
    list32 = [4, 5, 6]

    print(getdiffencesinlists(list11, list12))
    print(getdiffencesinlists(list21, list22))
    print(getdiffencesinlists(list31, list32))

    print(diferencias_listas1(list11, list12))
    print(diferencias_listas1(list21, list22))
    print(diferencias_listas1(list31, list32))

    print(diferencias_listas2(list11, list12))
    print(diferencias_listas2(list21, list22))
    print(diferencias_listas2(list31, list32))

    print(diferencias_listas3(list11, list12))
    print(diferencias_listas3(list21, list22))
    print(diferencias_listas3(list31, list32))