class Pagina: # Clase Pagina
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido
    def mostrar_pagina(self):
        print(f"Página {self.numero}: {self.contenido}")
class Libro: # Clase Libro
    def __init__(self, titulo):
        self.titulo = titulo
        self.paginas = []  # Lista para almacenar las páginas del libro
    def agregar_pagina(self, numero, contenido):
        pagina = Pagina(numero, contenido)   # COMPOSICION
        self.paginas.append(pagina)
    def mostrar_contenido(self):
        print(f"Libro: {self.titulo}")
        for pagina in self.paginas:
            pagina.mostrar_pagina()
def main(): # Ejemplo de uso
    libro = Libro("Python Básico")
    libro.agregar_pagina(1, "Introducción a Python")
    libro.agregar_pagina(2, "Variables y Tipos de Datos")
    libro.mostrar_contenido()
if __name__ == "__main__":
    main()

'''SALIDA
Libro: Python Básico
Página 1: Introducción a Python
Página 2: Variables y Tipos de Datos'''
