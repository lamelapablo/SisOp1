import threading, random, time

class Asiento:
    def __init__(self, id:int):
        self.__id = id
        self.__disponible = True
        self.__lock: threading.Lock = threading.Lock()

    @property
    def nombre(self):
        return self.__id

    def reservar(self):
        self.__lock.acquire_lock()
        try:
            if self.__disponible:
                self.__disponible = False
                res = True
            else:
                res = False
        finally:
            self.__lock.release_lock()

        return res

class Avion:
    def __init__(self, cant_asientos):
        self.__asientos: list[Asiento] = []
        for i in range(cant_asientos):
            self.__asientos.append(Asiento(i+1))
    
    @property
    def asientos(self):
        return self.__asientos

class Cliente(threading.Thread):
    def __init__(self, nombre: int, avion: Avion, cant_a_reservar: int, semaforo: threading.Semaphore):
        super().__init__()
        self.__nombre = nombre
        self.__avion = avion
        self.__cant_a_reservar = cant_a_reservar
        self.__semaforo = semaforo
    
    def __reservar_asientos(self):
        reservas_realizadas = 0
        intentos = 0
        while reservas_realizadas < self.__cant_a_reservar and intentos < len(self.__avion.asientos):
            time.sleep(random.uniform(0.4, 1.2))
            if self.__avion.asientos[intentos].reservar():
                print(f"{self.__nombre} reservo el asiento {self.__avion.asientos[intentos].nombre}\n", end="")
                reservas_realizadas += 1

            intentos += 1

        if reservas_realizadas == 0:
            print(f"{self.__nombre} no encontro asientos disponibles\n", end="")

        print(f"{self.__nombre} ha terminado de reservar")

    def run(self):
        self.__semaforo.acquire()
        try:
            self.__reservar_asientos()
        finally:
            self.__semaforo.release()

def main():
    semaforo = threading.Semaphore(3)

    avion: Avion = Avion(30)
    clientes: list[Cliente] = []
    for i in range(5):
        clientes.append(Cliente(f"Cliente {i+1}", avion, i+10, semaforo))
    
    for cliente in clientes:
        cliente.start()

    for cliente in clientes:
        cliente.join()

if __name__ == "__main__":
    main()