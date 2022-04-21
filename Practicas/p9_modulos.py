# Módulos
# Es necesario que en el archivo que estás importando no tendrás sentencias fuera de su archivo main, en caso de ser así, 
# estas sentencias serán ejecutadas, ver el archivo 8_funciones.py para ver un ejemplo. 

# Es posible importar métodos o variables globales
# Ejemplo de importación de un método de otro módulo
from p8_funciones import multiplicar, compararnumeros

# Ejemplo de importación de un método de una variable
from p8_funciones import variable_global

print(multiplicar(8, 9))
print(compararnumeros(8, 9))
print(variable_global)