# Funciones

# Variable global para ser importada
variable_global = 10

# Ejemplo de definición
# No es necesario indicar que tipo de dato es en cada parámetro de la lista
def multiplicar (a, b):
    print("Estas ejecutando la función multiplicación")
    return a * b

# Es posible asignarle un tipo de dato a los valores que recibes en la función
# Aunque Python seguirá recibiendo cualquier tipo de dato en n1 o n2, es más como una recomendación o documentación para el programador
def compararnumeros (n1: int, n2: int) -> str:
    """
    # Es posible atrapar el error de la siguiente manera con excepciones:
    if type(n1) is not int or type(n2) is not int:
        raise Exception("No son dos enteros")
    """

    if n1 > n2:
        return "El número uno es menor al segundo"
    elif n1 < n2:
        return "El número uno es menor al segundo"
    else:
        return "Los números son iguales"

# Es parecido a una función main en otros lenguajes
if __name__ == '__main__':
    # Para ejecutar el bloque de código de una función, esta debe de ser llamada
    print(multiplicar(3, 3))

    print(compararnumeros(1, 2))
    print(compararnumeros(2, 1))
    print(compararnumeros(2, 2))
