# Dependiendo la receta, crear una función que nos diga cuantos pasteles puedo hacer

# Mi solución
def how_cakes(ingredients_required: dict, ingredients: dict) -> int:
    prop = {}

    for key in ingredients_required.keys():
        if not ingredients.get(key) or ingredients_required[key] > ingredients[key]:
            return 0
        # Trunca el valor decimal
        prop[key] = ingredients[key] // ingredients_required[key]
    return min(prop.values())

# Solución de Arturo Sacramento Lopez Gonzalez
def pasteles(receta: dict, disponibles: dict) -> int:
    return min(disponibles.get(llave, 0) // receta[llave] for llave in receta)

if __name__ == '__main__':
    receta = {
        'harina': 500,
        'azucar': 200,
        'huevos': 1
    }

    disponibles = {
        'harina': 1200,
        'azucar': 1200,
        'huevos': 5,
        'leche': 200
    }

    print("Cantidad de pasteles que se pueden hacer: " + str(how_cakes(receta, disponibles)))