from datetime import datetime
import statistics

class Experimento:
    # funcion de inicializacion = metodo constructor
    def __init__(self, nombreExperimento, fecha, tipoExperimento, resultado):
        self.nombreExperimento = nombreExperimento
        self.fecha = fecha
        self.tipoExperimento = tipoExperimento
        self.resultado = resultado

# funcion para agregar una tarea
def agregarExperimento(listaExperimentos):
    nombreExperimento = input("Ingrese el nombre del experimento: ")
    fecha_str = input("Ingrese la fecha de realizacion del experimento (DD/MM/YYYY): ")
    try:
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        print("Fecha no valida")
        return
    tipoExperimento = input("Ingrese el tipo de experimento (Quimica, Biologia, Fisica): ")
    resultado_str = input("Ingrese los resultados obtenidos, separados en comas ej 3,4,5: ")
    try:
        resultado = list(map(float, resultado_str.split(",")))
    except ValueError:
        print("Resultados no validos")
        return
    
    # crear un objeto y lo agrega a la lista de experimentos
    experimento = Experimento(nombreExperimento, fecha, tipoExperimento, resultado)
    listaExperimentos.append(experimento)
    print("Experimento agregado con exito")

def visualizarExperimento(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados")
        return
    
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}")
        print(f"Nombre Experimento: {experimento.nombreExperimento}")
        print(f"Fecha de realizacion: {experimento.fecha.strftime('%d/%m/%Y')}")
        print(f"Tipo de experimento: {experimento.tipoExperimento}")
        print(f"Resultados obtenidos: {experimento.resultado}")

def calcularExperimento(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados")
        return
    
    for experimento in listaExperimentos:
        promedio = round(statistics.mean(experimento.resultado), 2)
        maximo = round(max(experimento.resultado), 2)
        minimo = round(min(experimento.resultado), 2)
        print(f"\nCalculo de estadisticas de {experimento.nombreExperimento}")
        print(f"Promedio de resultados: {promedio}")
        print(f"Maximo de resultados: {maximo}")
        print(f"Minimo de resultados: {minimo}")

def compararExperimentoSeleccionados(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados")
        return
    
    print("Experimentos disponibles: ")
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"{i}.{experimento.nombreExperimento}")
    
    seleccion = input("\nIngrese los numeros de los experimentos que desea comparar (separados por comas ej 1,3,5): ")
    try:
        indices = list(map(int, seleccion.split(",")))
        experimentosSeleccionados = [listaExperimentos[i - 1] for i in indices if 1 <= i <= len(listaExperimentos)]

        if not experimentosSeleccionados:
            print("No selecciono experimentos validos")
            return
        
        # Comparar entre las seleccionadas
        mejorExperimento = max(experimentosSeleccionados, key=lambda experimento: statistics.mean(experimento.resultado))
        peorExperimento = min(experimentosSeleccionados, key=lambda experimento: statistics.mean(experimento.resultado))

        print(f"\nEntre los experimentos seleccionados: ")
        print(f"El experimento con mejor promedio es '{mejorExperimento.nombreExperimento}' con '{statistics.mean(mejorExperimento.resultado)}'")
        print(f"El experimento con peor promedio es '{peorExperimento.nombreExperimento}' con '{statistics.mean(peorExperimento.resultado)}'")
    except (ValueError, IndexError):
        print("Entrada no valida. Asegurese de ingresar numeros validos y separados por comas")

# Funcion para generar informes
def generarInforme(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados")
        return
    
    with open("Informe_experimentos.txt", "w") as archivo:
        for experimento in listaExperimentos:
            archivo.write(f"Nombre Experimento: {experimento.nombreExperimento}\n")
            archivo.write(f"Fecha de realizacion: {experimento.fecha.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Tipo de experimento: {experimento.tipoExperimento}\n")
            archivo.write(f"Resultados obtenidos: {experimento.resultado}\n")
            archivo.write("\n")
    print("Informe generado como 'Informe_experimentos.txt'")

# Menu
def menu():
    listaExperimentos=[]
    while True:
        print("\nMenu de opciones: ")
        print("1. Agregar Experimento: ")
        print("2. Visualizar Experimentos: ")
        print("3. Calculos basicos de resultados obtenidos: ")
        print("4. Comparacion de resultados obtenidos: ")
        print("5. Generar informe: ")
        print("6. Salir: ")

        try:
            opcion = int(input("Selecciones una opcion: "))
        except ValueError:
            print("Por favor, ingrese un numero valido")
            continue

        if opcion == 1:
            agregarExperimento(listaExperimentos)
        elif opcion == 2:
            visualizarExperimento(listaExperimentos)
        elif opcion == 3:
            calcularExperimento(listaExperimentos)
        elif opcion == 4:
            compararExperimentoSeleccionados(listaExperimentos)
        elif opcion == 5:
            generarInforme(listaExperimentos)
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida. Por favor intente nuevamente")
        
if __name__ == "__main__":
    menu()