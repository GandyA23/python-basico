# Listas  
# Definición de una lista
lista = [1, 2, 3, 4, 10]

print(lista[0])

# Es posible realizar una modificación a los elementos en específico de la lista
lista[0] = 2

# Imprime todos los valores de la lista
print(lista)
print(type(lista))  # <class 'list'>

# Imprime la longitud de la lista
print(len(lista))

# Imprime el valor más alto de la lista
print(max(lista))

# Imprime el valor más bajo de la lista
print(min(lista))

# Una vez que ya esta definida la lista, es posible agregar un elemento nuevo al final de la lista
# NOTA: No es necesario que el elemento agregado tenga el mismo tipo que los elementos de la lista
lista.append(12)
lista.append("Hola")

print(lista)

# Aunque esto va a ser que no sea posible ejecutar métodos como min o max, debido a que no hay una manera de comparar los elementos
# print(min(lista))   # Genera un error

# En este caso si es posible
lista = ['h', 'o', 'l', 'a']
print(max(lista))

# Ordena todos los elementos de la lista de menor a mayor
lista.sort()

print(lista)

# Tuplas
# Las tuplas son muy similares a las listas, pero tienen la característica de que las tuplas son inmutables (no es posible modificarlas)

# Definición de una tupla
tupla = (1, 'hola', 7, 'adios')

print(type(tupla))  # <class 'tuple'>
print(tupla)

# Si se trata de hacer una modificación, entonces se generara un error
# Genera un error
# tupla[0] = 2  
# tupla.append(3)

# Sets
# Los sets son muy similares a las listas, pero tienen la característica de que los sets si son mutables, y no aceptan valores repetidos

# Definición de un set
set_ = {1, 'hola', 'mundo', 3}

print(type(set_))

# Es posible añadir y descartar elementos, peor en caso de añadir uno existente, este será descartado.
set_.add(1)
set_.add('hola')
set_.add(5)         # Solo se añade el elemento 5

set_.discard('hola')

print(set_)

# Si se trata de hacer una modificación, entonces se generara un error
# Genera un error
# set_[0] = 2  
