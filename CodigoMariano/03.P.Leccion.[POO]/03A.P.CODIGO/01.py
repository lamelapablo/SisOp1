class Auto:     
    __ruedas = 4                      # atributo de clase privado
    # Constructor
    def __init__(self, marca, modelo, anio, color):
        self.__marca = marca        # atributo de instancia privado
        self.__modelo = modelo      # atributo de instancia privado
        self.__anio = anio          # atributo de instancia privado
        self.__color = color        # atributo de instancia privado
        self.__velocidad = 0        # atributo de instancia privado
    
    # Métodos para acceder a los atributos de clase privados
    @classmethod
    def ruedas(cls):
        return cls.__ruedas
    
    # Métodos para acceder a los atributos de instancia privados
    @property
    def marca(self):                # getter
        return self.__marca
    
    @property
    def modelo(self):               # getter
        return self.__modelo
    
    @property
    def anio(self):                 # getter
        return self.__anio
    
    @property
    def color(self):                # getter
        return self.__color

    @property
    def velocidad(self):            # getter
        return self.__velocidad
    
    # Métodos para modificar a los atributos de instancia privados
    @color.setter
    def color(self, nuevo_color):   # setter
        self.__color = nuevo_color

    # Métodos públicos para interactuar con el auto
    def acelerar(self, cantidad):
        self.__velocidad += cantidad
        self.__mostrar_estado()

    def frenar(self, cantidad):
        self.__velocidad -= cantidad
        if self.__velocidad < 0:
            self.__velocidad = 0
        self.__mostrar_estado()

    # Método privado para mostrar el estado del auto
    def __mostrar_estado(self):
        salida=f"El auto {self.__marca} {self.__modelo} "
        salida+=f"con {self.ruedas()} ruedas ({self.__anio}) "
        salida+=f"está a {self.__velocidad} km/h."
        print(salida)
        
def main():
    print()
    a1=Auto("Chevrolet","Bel Air",1957,"Celeste")
    a1.acelerar(30)
    print(". . . . . .")
    a1.frenar(20)
    print(". . . . . .")
    a1.frenar(10)
    print()
    
if __name__==main():
    main()
    
