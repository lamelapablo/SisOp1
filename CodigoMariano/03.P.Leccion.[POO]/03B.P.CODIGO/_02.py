class Vehiculo:
    def __init__(self, marca):
        self._marca = marca
        # Si tiene "__" (oculto), entonces no se hereda
class Auto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.__modelo = modelo
    def info(self):
        print(f"Marca: {self._marca}, Modelo: {self.__modelo}")
def main():
    miAuto=Auto("Toyota","Corolla")
    miAuto.info()
if __name__==main():
    main()
'''SALIDA
Marca: Toyota, ModeloCorolla
'''
