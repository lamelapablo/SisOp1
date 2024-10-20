import threading
import time
import random

class CajaDeAhorro:
    def __init__(self, saldo=0):
        self.__saldo = saldo
        self.__lock = threading.Lock()

    def depositar(self, monto):
        try:
            self.__lock.acquire()
            #time.sleep(random.uniform(1,3))
            print(f"Depositando {monto} al saldo\n", end="")
            self.__saldo += monto
            print(f"Saldo actualizado ({monto}): {self.__saldo}\n", end="")
        finally:
            self.__lock.release()

class Usuario(threading.Thread):
    def __init__(self, nombre, caja_de_ahorro, monto):
        super().__init__()
        self.__nombre = nombre
        self.__caja_de_ahorro = caja_de_ahorro
        self.__monto = monto
    
    def __depositar_dinero(self):
        print(f"{self.__nombre} intenta depositar {self.__monto}\n", end="")
        self.__caja_de_ahorro.depositar(self.__monto)

    def run(self):
        self.__depositar_dinero()


def main():
    caja_compartida = CajaDeAhorro()
    usuarios = []
    for i in range(5):
        usuarios.append(Usuario(f"Usuario {i+1}", caja_compartida, 100*(i+1)))

    for usuario in usuarios:
        usuario.start()

    for usuario in usuarios:
        usuario.join()

if __name__ == "__main__":
    main()