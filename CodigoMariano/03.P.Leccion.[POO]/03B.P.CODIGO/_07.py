class Direccion: # Clase Dirección
    def __init__(self, calle, ciudad):
        self._calle = calle
        self._ciudad = ciudad
    def mostrar_direccion(self):
        print(f"Dirección: {self._calle}, {self._ciudad}")

class Persona: # Clase Persona
    def __init__(self, nombre, direccion):
        self._nombre = nombre
        # Composición: la persona tiene una dirección
        self._direccion = direccion  
    def mostrar_informacion(self):
        print(f"Nombre: {self._nombre}")
        self._direccion.mostrar_direccion()

def main(): # Ejemplo de uso
    direccion = Direccion("Las totoras 123", "San Ignacio") # AGREGACIÓN
    persona = Persona("Juan", direccion)
    persona.mostrar_informacion()

if __name__ == "__main__":
    main()
'''SALIDA
Nombre: Juan
Dirección: Las totoras 123, San Ignacio'''
