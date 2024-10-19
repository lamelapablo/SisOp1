class Vehiculo:
    def encender(self):
        print("El vehículo está encendido.")

class Motocicleta(Vehiculo):
    def encender(self):  
        # Sobreescritura del método encender
        print("La motocicleta está encendida.")

def main():
    miMoto=Motocicleta()
    miMoto.encender()     # Ejecuta Método sobreescrito
if __name__==main():
    main()
'''SALIDA
La motocicleta está encendida.
'''
