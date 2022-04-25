 # Crear una función que me diga en que cuarto del años estoy

# solución 1
def cuarto1(mes: int) -> int:
    if mes >= 1 and mes <= 3:
        return 1
    if mes >= 4 and mes <= 6:
        return 2
    if mes >= 7 and mes <= 9:
        return 3
    if mes >= 10 and mes <= 12:
        return 4

# solución 2
def cuarto2(mes: int) -> int:
    if mes in range(1, 4):
        return 1
    if mes in range(4, 7):
        return 2
    if mes in range(7, 10):
        return 3
    if mes in range(10, 13):
        return 4

# solución 3
def cuarto3(mes: int) -> int:
    primero = [1, 2, 3]
    segundo = [4, 5, 6]
    tercero = [7, 8, 9]
    cuarto = [10, 11, 12]

    if mes in primero:
        return 1
    if mes in segundo:
        return 2
    if mes in tercero:
        return 3
    if mes in cuarto:
        return 4

# solución 4
def cuarto4(mes: int) -> int:
    return (mes + 2) // 3

if __name__ == '__main__':
    print(cuarto4(1))
    print(cuarto4(3))
    print(cuarto4(6))
    print(cuarto4(8))
    print(cuarto4(11))
    print(cuarto4(12))