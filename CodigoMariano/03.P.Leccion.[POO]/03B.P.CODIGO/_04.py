class Vehiculo:
    def encender(self):
        print("El vehículo está encendido.")
class Auto(Vehiculo):
    def encender(self):
        print("El auto está encendido.")
       
def iniciar_vehiculo(unVehiculo):
    # .encender() dependerá de la clase del objeto unVehiculo
    unVehiculo.encender() 
def main():
    v = Vehiculo()
    a = Auto()
    iniciar_vehiculo(v)  
    iniciar_vehiculo(a)  
if __name__==main():
    main()
'''SALIDA
El vehículo está encendido.
El auto está encendido.
'''
