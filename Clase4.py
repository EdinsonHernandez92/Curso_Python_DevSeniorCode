# Caso Gestión Droguería
# Consultar Codificación Camel Case
# 1.5 es float....35 es int....edinson es str

ventasTotales = 0.0

# solicitar el número de productos
numProductos = int(input('Ingrese el número de productos a gestionar: '))

# listas para almacenar la información
nombres = []
precios = []
cantidades = []

print('Ingreso inicial de productos a la tienda: ')
for i in range(numProductos):
    print(f'Producto {i+1}: ')
    nombre = input('Ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    precio = float(input('Digite el precio del producto: '))
    precios.append(precio)
    cantidad = int(input('Digite la cantidad del producto: '))
    cantidades.append(cantidad)

# Para crear un menú lo mejor es crear un ciclo principal menú
# averiguar para qué sirve \n
while True:
    print('\n ---MENU DE GESION DE DROGUERIA---')
    print('1. Vender Producto')
    print('2. Mostrar Inventario')
    print('3. Mostrar Ventas Totales')
    print('4. Salir')

    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        print('\nVender Producto')
        nombreVenta = input('Ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('Ingrese la cantidad a vender: '))
        productoEncontrado = False

        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    print(f'Venta realizada. Total de esta venta ${totalVenta:.2f}')
                    print(f'Quedan {cantidades[i]} unidades de {nombres[i]} en el inventario')
                else:
                    print(f'Cantidad insuficiente en inventario, ya que en stock solo tenemos {cantidades[i]}')
                    break
        if not productoEncontrado:
            print('Producto no encontrado en el inventario')
    elif opcion == 2:
        print('\nInventario de Productos')
        for i in range(len(nombre)):
            print(f'Producto {i+1}: {nombres[i].capitalize()}, Precio: ${precios[i]:.2f}, Cantidad: {cantidades[i]}')

    elif opcion == 3:
        print(f'\nVentas totales acumuladas: ${ventasTotales:.2f}')

    elif opcion == 4:
        print('Gracias por usar el sistema de gestion drogueria Dev Senior')
        break

    else:
        print('opcion invalida. ingresar entre (1-4)')

# Tarea no dejar ingresar cantidad de productos negativos