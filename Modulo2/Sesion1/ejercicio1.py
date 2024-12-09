# Clase Libro: Crea una clase llamada Libro que tenga los atributos: Título y Autor.
# Implementa un método descripcion que devuelva un texto como: "El libro [Título] fue escrito por [Autor]."

class Libro:

    #Iniciailiza un libro con titulo y autor como atributos
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    #Método solicitado
    def descripcion(self):
        return f"El libro {self.titulo} fue escrito por {self.autor}"

libro1 = Libro("Habitos atomicos","James Clear")
libro2 = Libro("Tus zonas erroneas", "Wayne Dyer")

print(libro1.descripcion())