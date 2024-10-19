from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau ..Guau..")

def main(): # Ejemplo de uso
    # Error: No se puede instanciar un clase abstracta
    # a = Animal()     # <- Error, Animal() es ABSTRACTA
    p = Perro()
    p.hacer_sonido()  # Salida
if __name__ == "__main__":
    main()
'''SALIDA
Guau ..Guau..'''
