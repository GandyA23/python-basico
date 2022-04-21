# Diccionarios

# Definición de un diccionario
# { clave: valor }
# Son separados por comas
diccionario = {
    "elemento1": 1,
    "elemento2": 7,
    "elemento10": "cadena"
}

# Modificación de un elemento dentro del diccionario
diccionario['elemento1'] = 10
diccionario[10] = "Cadena modificada"

# Eliminación de elementos de un diccionario
del(diccionario['elemento2'])

print(diccionario)

# Imprime en una lista las claves del diccionario
print(diccionario.keys())

# Imprime en una lista los valores del diccionario
print(diccionario.values())