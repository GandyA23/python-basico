# Es posible crear cadenas con comillas dobles o simples, siempre es el mismo resultado.
cadena = "Hola Mundo!"
simple = 'Adios mundo!'

# Es posible acceder a posiciones específicas de cadenas como si fuera un arreglo de carácteres
print(cadena[0])

# Toma desde la posición 0 y después, toma 5 caracteres
print(cadena[0:5])

# Desde la posición incial, toma 5 carácteres
print(cadena[:5])

# Desde la posición 5, hasta que la cadena se termine.
print(cadena[5:])

# Es posible también manejar posiciones negativas, las posiciones negativas quieren decir 
# que vas a tomar las últimas posiciones del arreglo

# Toma la posición final e imprímelas
print(cadena[-1:])

# Toma las últimas 4 posiciones de la cadena e imprímelas
print(cadena[-4:])

# Excluye las últimas 4 posiciones de la cadena.
print(cadena[-4:])

# Concatenación de las cadena
print(cadena + " " + simple)

# Raw Inputs (Cadenas crudas): ayudan a evitar el escapado de caracteres, usado demasiado en expresiones regulares 
# Se coloca la r antes de la cadena
ruta = r"C:\Documentos"

# Tamaño de una cadena
print(len(cadena))

# Métodos de una cadena
# Convierte todos los caracteres a minúsculas. 
print(cadena.lower())

# Convierte todos los caracteres a mayúsculas.
print(cadena.upper())