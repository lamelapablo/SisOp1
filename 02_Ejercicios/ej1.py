"""
Enunciado
Escribe un programa en python que cree tres hilos utilizando la clase threading.Thread. Cada hilo debe generar una lista de numeros al cuadrado de una cantidad dada y luego guardar esos numeros en un archivo de texto. Los hilos deben ejecutarse de manera sincrona, es decir, un hilo debe esperar a que el anterior termine antes de comenzar.
"""

import threading
import os

path = "/home/paul1213/UCA/SisOp1/02_Ejercicios"
filePath = f"{path}/ej1.txt"
cantidadNums = 10

def deleteFile(file):
    try:
        os.remove(file)
    except FileNotFoundError:
        print("El archivo no existe")
        

class MyThread(threading.Thread):
    def __init__(self,numthread,cantNum):
        super(MyThread, self).__init__()
        self.name=f"Thread-{numthread}"
        self.cantNum = cantNum

    def run(self):
        self.saveListToFile(self.generateList())

    def generateList(self):
        ls = [i*i for i in range(self.cantNum)]
        return ls

    def saveListToFile(self, ls):
        with open(filePath, "a") as file:
            for num in ls:
                file.write(f'{num}\n')


def main():

    deleteFile(filePath) # primero elimino el archivo

    print("-"*20)
    print("INICIO del Proceso\n",end="")
    print("....................")

    t0 = MyThread(0, cantidadNums)
    t1 = MyThread(1, cantidadNums)
    t2 = MyThread(2, cantidadNums)

    t0.start()
    t1.start()
    t2.start()

    t0.join()
    t1.join()
    t2.join()

    print("....................")
    print("FIN del Proceso\n",end="-"*20)

if __name__ == "__main__":
    main()