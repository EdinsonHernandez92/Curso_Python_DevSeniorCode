# Clase `Persona`: Diseña una clase `Persona` con los atributos: Nombre y Edad. Incluye un método `es_mayor_de_edad` que retorne `True` si la edad es 18 o mayor, de lo contrario, `False`.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
persona1 = Persona("Victor", 32)
persona2 = Persona("Angel", 10)

print(persona2.es_mayor_de_edad())