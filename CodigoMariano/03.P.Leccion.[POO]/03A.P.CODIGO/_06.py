class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre   # público
        self._edad = edad      # protegido
        self.__edad = edad     # privado
