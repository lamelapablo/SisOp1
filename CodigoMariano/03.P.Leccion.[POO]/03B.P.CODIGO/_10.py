class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
    def agregar_a_curso(self, curso):
        print(f"Estudiante: {self.nombre} está inscribiéndose a {curso.nombre}.")
        curso.agregar_estudiante(self)

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
    def agregar_estudiante(self, estudiante):
        print(f"Curso: ha sido agregado/a {estudiante.nombre} al curso de {self.nombre}.")

def main():
    # Ejemplo de uso
    estudiante1 = Estudiante("Alice")
    curso1 = Curso("Matemáticas")

    estudiante1.agregar_a_curso(curso1)
if __name__ == "__main__":
    main() 
'''SALIDA
Estudiante: Alice está inscribiéndose a Matemáticas.
Curso: ha sido agregado/a Alice al curso de Matemáticas. '''
