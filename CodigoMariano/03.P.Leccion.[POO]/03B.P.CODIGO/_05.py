class Telefono:   # Clase base Telefono
    def hacer_llamada(self):
        print("Llamando...")
class Reloj:      # Clase base Reloj
    def mostrar_hora(self):
        print("Mostrando la hora...")
class DispositivoInteligente(Telefono, Reloj): 
                  # Clase DERIVADA MÚLTIPLE
    def usar_asistente_virtual(self):
        print("Usando el asistente virtual...")
def main(): # Ejemplo de uso
    dispositivo = DispositivoInteligente()
    dispositivo.hacer_llamada()           # Heredado de Teléfono
    dispositivo.mostrar_hora()            # Heredado de Reloj
    dispositivo.usar_asistente_virtual()  # Método propio
if __name__ == "__main__":
    main()
'''SALIDA
Llamando...
Mostrando la hora...
Usando el asistente virtual...  '''
