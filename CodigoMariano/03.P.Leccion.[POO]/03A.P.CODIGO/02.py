class Libro:
    __total_libros = 0  # Atributo de clase privado para contar los libros

    def __init__(self, titulo, autor, anio, genero):
        self.__titulo = titulo     # Atributo de instancia privado
        self.__autor = autor       # Atributo de instancia privado
        self.__anio = anio         # Atributo de instancia privado
        self.__genero = genero     # Atributo de instancia privado
        Libro.__total_libros += 1  # Incrementa el contador de libros al crear un nuevo libro

    # Método de clase para acceder al atributo de clase privado
    @classmethod
    def total_libros(cls):
        return cls.__total_libros

    # Getters para los atributos de instancia privados
    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def anio(self):
        return self.__anio

    @property
    def genero(self):
        return self.__genero

    # Setter para modificar el atributo de instancia privado
    @genero.setter
    def genero(self, nuevo_genero):
        self.__genero = nuevo_genero

    # Método público para mostrar información del libro
    def mostrar_info(self):
        print(f"Título: {self.__titulo}, Autor: {self.__autor}, Año: {self.__anio}, Género: {self.__genero}")

def main():
    print()
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "Realismo Mágico")
    libro2 = Libro("1984", "George Orwell", 1949, "Distopía")

    libro1.mostrar_info()
    libro2.mostrar_info()

    print(". . . . . .")
    print(f"Total de libros en la biblioteca: {Libro.total_libros()}")
    print(". . . . . .")
    
    # Cambiar el género de un libro
    libro2.genero = "Ciencia Ficción"
    libro2.mostrar_info()
    print()

if __name__ == "__main__":
    main()