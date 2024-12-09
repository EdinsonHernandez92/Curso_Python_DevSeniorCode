#2. Herencia: Clase `Vehiculo` y `Moto`: Crea una clase base `Vehiculo` con los atributos: Tipo y Marca. Crea una subclase `Moto` que herede de `Vehiculo` y tenga un método `hacer_wheelie` que imprima:  `"¡La moto [Marca] está haciendo un wheelie!"`

class Vehiculo():
    def __init__(self, tipo, marca):
        self.tipo = tipo
        self.marca = marca

class Moto(Vehiculo):
    def __init__(self, marca):
        super().__init__('Moto', marca)
    
    def hacer_wheelie(self):
        print(f"¡La moto {self.marca} está haciendo un wheelie")

moto1 = Moto("Suzuki")
moto1.hacer_wheelie()