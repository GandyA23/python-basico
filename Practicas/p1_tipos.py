"""
El tipo de dato de cada variable depende del valor asignado a cada variable. 
"""

# Datos básicos
entero = 1
booleano = True
flotante = 3.1415

cadena = "Hola Mundo!"

# También es posible declararlo con comillas simples
cadena = 'Hola Mundo!'

print(type(entero))     # <class 'int'>
print(type(booleano))   # <class 'bool'>
print(type(flotante))   # <class 'float'>

# Python cuenta con la capacidad de trabajar con números complejos
complejo1 = 2 + 4j
complejo2 = 2 + 7j
resultadoComplejo = complejo1 + complejo2

print(resultadoComplejo)    # (4+11j)

# Es posible hacer la suma de variables que son diferentes tipos
print(entero + flotante)    # (4.141500000000001)

# Aunque no es posible en todos los casos
# print(cadena + entero)    # Genera un error

# Para esto, es posible realizar un casteo para realizar la suma, o en este caso en específico, la concatenación. 
print(cadena + ' ' + str(entero))
