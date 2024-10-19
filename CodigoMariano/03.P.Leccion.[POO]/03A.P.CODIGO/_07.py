class Persona:
    def __init__(self, nombre):
        self._nombre = nombre  # protegido

    # Getter
    def get_nombre(self):
        return self._nombre

    # Setter
    def set_nombre(self, nombre):
        self._nombre = nombre

persona = Persona("Ana")
print(persona.get_nombre())    # Salida: Ana
persona.set_nombre("Carlos")
print(persona.get_nombre())    # Salida: Carlos