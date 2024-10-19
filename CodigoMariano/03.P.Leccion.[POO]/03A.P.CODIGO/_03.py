class Auto:    
    ruedas = 4                 # atributo de clase
    # Constructor
    def __init__(self, marca, modelo, anio, color):
        self._marca = marca    # atributo de instancia
        self._modelo = modelo  # atributo de instancia
        self._anio = anio      # atributo de instancia
        self._color = color    # atributo de instancia
        self._velocidad = 0    # atributo de instancia