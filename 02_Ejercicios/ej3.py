import threading
import time
import os
import textwrap

path = "/home/paul1213/UCA/SisOp1/02_Ejercicios/ej3_files/"


class BackgroundTask(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True

    def run(self):
        while True:

            #print(os.listdir())

            time.sleep(5)

def mostrar_menu():
    menu = textwrap.dedent("""
        -----------------------------
        |   1. Agregar archivo.     |
        |   2. Eliminar archivo.    |
        |   3. Listar archivos.     |
        |   4. Leer archivo.        |
        |   5. Mostrar directorio.  |
        |   6. Salir.               |
        -----------------------------
    """)
    print(menu)

def listar_archivos():
    for archivo in os.listdir(path):
        print(f"* {archivo} *")
    
def agregar_archivo():
    archivo = input("Ingrese el nombre del archivo a crear: ")
    if os.path.exists(archivo):
        print(f"Ya existe un archivo con el nombre {archivo}.")
    else:
        nuevo_archivo = open(f"{path}/{archivo}", "x")
        nuevo_archivo.close(nuevo_archivo)
        print("Archivo creado con exito.")


def main():
    # Crear una instancia de la clase BackgroundTask
    background_thread = BackgroundTask()

    # Iniciar el hilo demonio
    #background_thread.start()

    mostrar_menu()
    opcion = int(input("Ingrese su opcion: "))
    while opcion != 6:
        if opcion > 6 or opcion < 1:
            print("Opcion no disponible.")
        elif opcion == 1:
            agregar_archivo()
        elif opcion == 3:
            listar_archivos()
        
        mostrar_menu()
        opcion = int(input("Ingrese su opcion: "))

if __name__ == "__main__":
    main()