import threading, time, random

class Estacion(threading.Thread):
    def __init__(self, id, event_mi_inicio, event_inicio_proxima):
        super().__init__()
        self.__id = id
        self.__event_mi_inicio: threading.Event = event_mi_inicio
        self.__event_inicio_proxima: threading.Event = event_inicio_proxima

    def run(self):
        if self.__event_mi_inicio:
            print(f"Estacion {self.__id} esta esperando la finalizacion de la estacion anterior...\n", end="")
            self.__event_mi_inicio.wait()

        print(f"Estacion {self.__id} esta trabajando...\n", end="")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Estacion {self.__id} ha completado su tarea")
        if self.__event_inicio_proxima:
            self.__event_inicio_proxima.set()

def main():
    cant_estaciones = 5
    estaciones: list[Estacion] = []
    eventos: list[threading.Event] = []
    for i in range(cant_estaciones):
        eventos.append(threading.Event())

    for i in range(cant_estaciones):
        if i == 0:
            estaciones.append(Estacion(i+1, None, eventos[i]))
        else:
            estaciones.append(Estacion(i+1, eventos[i-1], eventos[i]))

    for estacion in estaciones:
        estacion.start()

    for estacion in estaciones:
        estacion.join()

if __name__ == "__main__":
    main()