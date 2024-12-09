#Ejercicios Intermedios
#Clase `Banco`: Implementa una clase `Banco` con: Atributo de clase `tasa_interes`. 
# Método de clase `actualizar_tasa(nueva_tasa)`.  
# Método `calcular_interes(monto)` que calcule el interés sobre un monto basado en la tasa actual.

class Banco:
    tasa_interes = 0.05 # tasa interes inicial 5%

    @classmethod
    def actualizar_tasa(cls, nueva_tasa):
        cls.tasa_interes = nueva_tasa

    def calcular_intereses(self, monto):
        return monto * self.tasa_interes
    
banco1 = Banco()
print(banco1.calcular_intereses(1000))

banco1.actualizar_tasa(0.1)
print(banco1.calcular_intereses(1000))
