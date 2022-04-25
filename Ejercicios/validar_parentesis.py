# Validar si unos parentesis fueron abiertos y cerrados correctamente

# Mi solución
def validateparentheses(parentheses: str) -> bool:
    stack_p = []
    for p in parentheses:
        if p == '(':
            stack_p.append(p)
        elif p == ')' and len(stack_p):
            stack_p.pop()
        else:
            return False
    return not len(stack_p)

# Solución de Arturo Sacramento Lopez Gonzalez
def validar_parentesis(cadena: str) -> bool:
    parentesis_counter = 0
    for elemento in cadena:
        if elemento == '(':
            parentesis_counter += 1
        if elemento == ')':
            parentesis_counter -= 1
        if parentesis_counter < 0:
            return False
    return not parentesis_counter


if __name__ == '__main__':
    p1 = '('
    p2 = '()'
    p3 = ')(()))'
    p4 = '(())((()())())'
    p5 = '(c(b(a)))(d)'

    print(validateparentheses(p1))
    print(validateparentheses(p2))
    print(validateparentheses(p3))
    print(validateparentheses(p4))
    print(validateparentheses(p5))

    print(validar_parentesis(p1))
    print(validar_parentesis(p2))
    print(validar_parentesis(p3))
    print(validar_parentesis(p4))
    print(validar_parentesis(p5))
