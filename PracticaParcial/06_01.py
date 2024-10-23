import threading, random, time

class Asiento:
    def __init__(self, nombre:str):
        self.__nombre = nombre
        self.__lock: threading.Lock = threading.Lock()
        self.__disponible = True

    @property
    def nombre(self):
        return self.__nombre

    def reservar_asiento(self):
        self.__lock.acquire()
        try:
            if self.__disponible:
                self.__disponible = False
                reserva_exitosa = True
            else:
                reserva_exitosa = False
        finally:
            self.__lock.release()

        return reserva_exitosa

class Avion:
    def __init__(self, cantidad_asientos:int):
        self.__asientos = [Asiento(f"Asiento {i+1}") for i in range(cantidad_asientos)]

    @property
    def asientos(self):
        return self.__asientos


class Cliente(threading.Thread):
    def __init__(self, nombre:str, semaforo:threading.Semaphore, cant_asientos_a_reservar:int, avion:Avion):
        super().__init__()
        self.__nombre = nombre
        self.__semaforo = semaforo
        self.__cant_asientos_a_reservar = cant_asientos_a_reservar
        self.__avion = avion

    def __reservar_asientos(self):
        intentos = 0
        reservados = 0
        while reservados < self.__cant_asientos_a_reservar and intentos < len(self.__avion.asientos):
            time.sleep(random.uniform(0.2, 1.2))
            if(self.__avion.asientos[intentos].reservar_asiento()):
                print(f"{self.__nombre} reservo el asiento {self.__avion.asientos[intentos].nombre}\n", end="")
                reservados += 1
            intentos += 1
        
        if reservados == 0:
            print(f"{self.__nombre} no encontro asientos disponibles\n", end="")
        elif reservados < self.__cant_asientos_a_reservar:
            print(f"{self.__nombre} reservo {reservados} de {self.__cant_asientos_a_reservar}\n", end="")
            
        print(f"{self.__nombre} termino de hacer reservas\n\n", end="")

    def run(self):
        self.__semaforo.acquire()
        try:
            self.__reservar_asientos()
        finally:
            self.__semaforo.release()

def main():
    avion: Avion = Avion(16)
    semaforo: threading.Semaphore = threading.Semaphore(3)
    clientes: list[Cliente] = [Cliente(f"Cliente {i+1}", semaforo, 5, avion) for i in range(5)]

    for cliente in clientes:
        cliente.start()

    for cliente in clientes:
        cliente.join()

if __name__ == "__main__":
    main()