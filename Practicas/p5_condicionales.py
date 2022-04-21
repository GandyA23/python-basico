# Ejemplo muy sencillo de if
var = 10

if var:
    print("La expresión es verdadera")
else:
    print("La expresión es falsa")

# Las condicionales son parecidas a C
# Cualquier valor diferente a 0 es verdadero
if 0:
    # Nunca entra aquí
    print("La condición siempre es falsa")

# Ejemplo de if - else if
if var == 1:
    print("La variable vale 1")
elif var == 2:
    print("La variable vale 2")
elif var == 3: 
    print("La variable vale 3")
else:
    print("La varible vale 10")

# Comparación de tipos de datos
cadena1 = 'hola'
cadena2 = 'hola'

if cadena1 == cadena2:
    print("Son cadenas iguales")
else:
    print("Son cadenas distintas")

# While
# Se ejecuta el bloque de código siempre y cuando la condición se cumpla
while var: 
    print("El valor de la variable es: " + str(var))
    var -= 1

print("El ciclo se rompio")