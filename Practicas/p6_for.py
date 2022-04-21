# For
# En Python, los ciclos for no son usados para iterar una variable (dependiendo la condición, me detengo), en Python son más usados para realizar iteraciones sobre tipos de datos iterables.(listas, cadenas)

cadena = "Hola Mundo!"

# Ejemplo de un for navegando en una cadena
for c in cadena:
    print(c)

# Ejemplo de un for navegando en una lista
lista = ['hola', 'mundo', '!']
for l in lista:
    print(l)

# Iteración anidada
for l in lista:
    print(l)
    for c in l:
        print(c)

# Imprimir la cadena al revez
for c in reversed(cadena):
    print(c)

# For normal parecido a los otros lenguajes
i = 0
n = 20
step = 2
for i in range(i, n, step):
    print(i)