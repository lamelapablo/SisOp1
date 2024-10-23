import threading, random, time

class Semaforo:
    def __init__(self):
        self.__event: threading.Event = threading.Event()

    def verde(self):
        print("El semaforo esta en verde")
        self.__event.set()

    def rojo(self):
        print("El semaforo esta en rojo")
        self.__event.clear()
    
    def esperar_verde(self):
        self.__event.wait()
        
class Vehiculo(threading.Thread):
    def __init__(self, nombre:str, interseccion_lock: threading.Lock, semaforo: Semaforo):
        super().__init__()
        self.__nombre = nombre
        self.__interseccion_lock = interseccion_lock
        self.__semaforo = semaforo

    def __cruzar_interseccion(self):
        self.__interseccion_lock.acquire()
        try:
            self.__semaforo.esperar_verde()
            print(f"{self.__nombre} esta cruzando la interseccion...\n", end="")
            time.sleep(random.uniform(0.5, 1.5))
            print(f"{self.__nombre} cruzo la interseccion\n", end="")
        finally:
            self.__interseccion_lock.release()

    def run(self):
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{self.__nombre} llego a la interseccion")
        self.__cruzar_interseccion()

def controlar_semaforo(semaforo: Semaforo):
    while True:
        semaforo.rojo()
        time.sleep(1.5)
        semaforo.verde()
        time.sleep(1.5)

def main():
    semaforo: Semaforo = Semaforo()
    lock: threading.Lock = threading.Lock()
    vehiculos: list[Vehiculo] = [Vehiculo(f"Vehiculo {i+1}", lock, semaforo) for i in range(5)]

    hilo_semaforo = threading.Thread(target=controlar_semaforo, args=(semaforo,))
    hilo_semaforo.daemon = True
    hilo_semaforo.start()

    for vehiculo in vehiculos:
        vehiculo.start()

    for vehiculo in vehiculos:
        vehiculo.join()

if __name__ == "__main__":
    main()

