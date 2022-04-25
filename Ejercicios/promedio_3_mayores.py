# Una función que reciba una lista de 4 números y se debe ejecutar el promedio de los 3 mayores

# Mi solución
def avg_three_greater (nums: list) -> float:
    # Ordena la lista
    nums.sort()
    greaters = nums[-3:]
    return sum(greaters) / len(greaters)


# Solución de Arturo Sacramento Lopez Gonzalez
def promedio_mayores(lista: list):
    lista.sort()
    ultimos_tres = lista[-3:]
    return sum(ultimos_tres) / len(ultimos_tres)

if __name__ == '__main__':
    l1 = [1, 2, 3, 4]
    l2 = [4, 3, 2, 5]
    l3 = [7, 5, 7, 7]
    l4 = [8, 5, 7, 11, 99]

    print(avg_three_greater(l1))
    print(avg_three_greater(l2))
    print(avg_three_greater(l3))
    print(avg_three_greater(l4))

    print(promedio_mayores(l1))
    print(promedio_mayores(l2))
    print(promedio_mayores(l3))
    print(promedio_mayores(l4))