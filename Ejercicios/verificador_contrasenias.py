# Función que verifique las contraseñas,
# Actividad 1: Verifica solo letras y números
# Actividad 2: Verifica solo letras, números y caracteres especiales
# Actividad 3: Todo lo anterior más verificar que mínimo tenga una mayúscula, minúscula

def verifypassword1(pwd: str) -> bool:
    # isalnum = es alfanumerico
    return pwd.isalnum()

def verifypassword2(pwd: str) -> bool:
    if not pwd:
        return False
    for char in pwd:
        char = ord(char)
        if not(32 <= char <= 126):
            return False
    return pwd.isalnum()

def verifypassword3(pwd: str) -> bool:
    flag_spec = flag_num = flag_min = flag_may = False
    
    if not pwd:
        return False
    
    for char in pwd:
        flag_spec |= 32 <= ord(char) <= 126
        flag_num |= char.isdigit()
        flag_min |= char.islower()
        flag_may |= char.isupper()

    return flag_spec and flag_num and flag_min and flag_may

if __name__ == '__main__':
    print(verifypassword1("hello world_"))
    print(verifypassword1("PassW0rd"))
    print(verifypassword1("     "))
    print(verifypassword1("__*__"))
    print(verifypassword1("&)))((("))
    print(verifypassword1("43534h56jnTHHF3k"))
    print(verifypassword1(""))

    print()

    print(verifypassword2("hello world_"))
    print(verifypassword2("PassW0rd"))
    print(verifypassword2("     "))
    print(verifypassword2("__*__"))
    print(verifypassword2("&)))((("))
    print(verifypassword2("43534h56jnTHHF3k"))
    print(verifypassword2(""))

    print()

    print(verifypassword3("hello world_"))
    print(verifypassword3("PassW0rd"))
    print(verifypassword3("     "))
    print(verifypassword3("__*__"))
    print(verifypassword3("&)))((("))
    print(verifypassword3("43534h56jnTHHF3k*!"))
    print(verifypassword3(""))

    print()
