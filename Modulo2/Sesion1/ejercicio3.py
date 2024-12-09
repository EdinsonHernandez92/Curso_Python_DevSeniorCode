#Clase `Rectangulo`: Crea una clase `Rectangulo` con: Atributos: `largo`, `ancho`. Métodos: `area` (calcula el área del rectángulo).  
#Ejemplo:  
#rect = Rectangulo(5, 4)
 #print(rect.area())  # Salida: 20

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

rectangulo1 = Rectangulo(5,6)
rectangulo2 = Rectangulo(3,5)

print(rectangulo2.area())