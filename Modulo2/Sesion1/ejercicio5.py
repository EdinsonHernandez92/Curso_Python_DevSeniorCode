#5. Clase `Calculadora`: Diseña una clase `Calculadora` con un método estático `suma` que reciba dos números y devuelva la suma de ellos.
  #Ejemplo:  
  #print(Calculadora.suma(3, 4))  # Salida: 7

class Calculadora:
    @staticmethod
    def suma(a,b):
        return a + b

print(Calculadora.suma(5,9))