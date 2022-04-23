# Crear una función que esconda todos los números de la tarjeta excepto los últimos dígitos.

# Mi solución
def hidelastfournumbers (cc):
    hidecc = ''

    if len(cc) > 4:
        hidecc += '#'*(len(cc)-4)
    
    hidecc += cc[-4:]

    return hidecc

# Solución de Arturo Sacramento Lopez Gonzalez
# Primera solución
def tarjeta_credito1 (numero_tarjeta):
    valor_escondido = ''
    for index in range(0, len(numero_tarjeta)-4):
        valor_escondido += '#'

    valor_escondido = valor_escondido + numero_tarjeta[-4:]
    return valor_escondido

# Segunda solución
def tarjeta_credito2 (numero_tarjeta):
    # Si el resultado de la longitud de la cadena menos 4 es negativo, entonces no imprime los gatitos
    return '#'*(len(numero_tarjeta) - 4) + numero_tarjeta[-4:]

if __name__ == '__main__':
    cc1 = '4556364607935616'
    cc2 = '64607935616'
    cc3 = '1'
    cc4 = '54321'

    print(hidelastfournumbers(cc1))
    print(hidelastfournumbers(cc2))
    print(hidelastfournumbers(cc3))
    print(hidelastfournumbers(cc4))
    
    print(tarjeta_credito1(cc1))
    print(tarjeta_credito1(cc2))
    print(tarjeta_credito1(cc3))
    print(tarjeta_credito1(cc4))
    
    print(tarjeta_credito2(cc1))
    print(tarjeta_credito2(cc2))
    print(tarjeta_credito2(cc3))
    print(tarjeta_credito2(cc4))

    