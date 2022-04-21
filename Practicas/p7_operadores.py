# Operadores

# Operadores aritméticos
var = 3
print("Suma: " + str(var + 2))
print("Resta: " + str(var - 2))
print("Multiplicación: " + str(var * 2))
print("División: " + str(var / 2))
print("Módulo: " + str(var % 2))
print("Exponente: " + str(var ** 2))
print("Floor div: " + str(var // 2))    # Trunca el valor, no muestra los decimales

# Operadores binarios
# 3 = 11
# 2 = 10
print("and: " + str(var & 2))
print("or: " + str(var | 2))
print("not: " + str(~var))      # Todos los 1 son 0 y viceversa
print("xor: " + str(var ^ 2))   # Regresa 1 en todos los bits que son distintos
print("corrimiento izq: " + str(var << 1))  # Recorre un bit hacia la izquierda 11 << 1 = 110 es igual a 6   
print("corrimiento der: " + str(var >> 1))  # Recorre un bit hacia la derecha 11 >> 1 = 1 es igual a 1

# Operadores de comparación
# Retornan un valor booleano
print("Mayor (>): " + str(var > 2))
print("Menor (<): " + str(var < 2))
print("Igual (==): " + str(var == 2))
print("Mayor o igual (>=): " + str(var >= 2))
print("Menor o igual (<=): " + str(var <= 2))
print("Distinto (!=): " + str(var != 2))

# Operadores de membresía
# Utilizados para saber si existe un contenido específico
# Retornan un valor booleano
cadena = "hola"
lista = [cadena, 'mundo!']
print("Contiene un carácter o: " + str('o' in cadena))
print("Contiene un carácter k: " + str('k' in cadena))
print("Contiene hola en la lista: " + str(cadena in lista))
print("Contiene hola y mario en la lista: " + str(cadena in lista and 'mario' in lista))
print("Contiene hola o mario en la lista: " + str(cadena in lista or 'mario' in lista))
print("No contiene hola en la lista: " + str(cadena not in lista))