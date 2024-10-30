# Estructuras de control de flujo
# Tema de importación de librerías
# Importación básica
# ¿Qué librerías vienen incluidas en python?

# Ejemplo importación básica
#import math
#resultado = math.sqrt(16)
#print(resultado)

# Condicionales if, elif, else
# Elif = else if
# Revisar palabras RESERVADAS DE PYTHON
# ¿Cómo se convierte un bloque de código en comentario? ctrl+k+c y para quitar comentario ctrl+k+u

age = 18
country = 'USA'

if age >= 21 and country == 'USA':
    print('You can buy alcohol')
elif age >= 18 and country == 'COL':
     print('You can buy alcohol')
else:
     print('You can\'t alcohol')

for i in range(10):
    print(i)
# While cuando no tenemos claro el número de veces a ejecutar. Buscar qué es +=