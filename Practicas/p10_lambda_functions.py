# Lambda funcitons
# Las funciones lambda son como funciones anónimas


# Definición de la función multiplicación pero en lambda
# El resultado de a*b será el valor de retorno
multiplicacion = lambda a,b: a*b

# Suma al valor mandado 10
suma_10 = lambda a: a + 10


# Es posible mandarle una función lambda para ordenar una lista
# Ordenar los nombres solo considerando los apellidos
lista_nombres = ["Gandy Ávila", "Regina García", "Brian Medrano", "Chuck Tableros", "Jair Vazques", "Alexis Loya"]
lista_nombres.sort(key = lambda nombre: nombre.split(" ")[-1])

print(multiplicacion(5, 5))
print(suma_10(10))
print(lista_nombres)

