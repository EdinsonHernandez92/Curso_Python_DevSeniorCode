# Solicitamos al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realizamos las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Mostramos los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# Ejercicio 2
# Solicitamos al usuario que ingrese la medida en metros
medida_metros=float(input("Ingresa la medida a convertir:"))

# Se realiza la operación
centimetros = medida_metros * 100
milimetros = medida_metros * 1000

# Se muestran resultados
print(f"Centímetros: {centimetros}")
print(f"Milímetros: {milimetros}")

# Ejercicio 3
# Solicitamos al usuario que ingrese dos números
numero_1 = float(input("Ingresa el primer número:"))
numero_2 = float(input("Ingresa el segundo número:"))

if numero_1 > numero_2:
    print(f"El número mayor es: {numero_1} y el número menor es: {numero_2}")

if numero_2 > numero_1:
    print(f"El número mayor es: {numero_2} y el número menor es: {numero_1}")

if numero_1 == numero_2:
    print(f"Son el mismo número")

# Ejercicio 4 Verificación Edad
edad = int(input("Ingresa tu edad:"))

if edad >= 18:
    print(f"Puedes votar")
if edad < 18:
    print(f"No puedes votar")