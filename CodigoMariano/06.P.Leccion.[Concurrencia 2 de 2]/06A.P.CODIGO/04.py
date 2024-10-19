'''
EVENT
En este ejemplo, varios hilos esperarán a que un evento se
establezca para poder continuar o ejecutar. Podemos pensar en el inicio de una carrera
donde luego de una señal los corredores comienzan a correr.
    Sincronización de Hilos:
    Todos los hilos inician al mismo tiempo después de que el evento es establecido,
    lo que simula un escenario en el que varias tareas necesitan esperar
    una señal para comenzar.

- - - - -  - - - -  
La clase Worker extiende threading.Thread y recibe un objeto Event y un identificador de trabajador
(worker_id). El método run() hace que cada hilo espere a que el evento sea establecido
usando self.event.wait() antes de continuar con su tarea.

Método event.wait():
event.wait() bloquea el hilo hasta que el evento esté en estado "establecido"
(es decir, hasta que se llame a event.set() y el evento esté en True).

Método event.set():
Coloca el evento en True
    Comentarios: En la función main(), se simula un tiempo de preparación antes de establecer
    el evento con event.set(), lo que permite que todos los hilos que estaban
    esperando comiencen a trabajar.

Métodos de la clase threading.Event()
    set():  establece el evento (quedan todos lo thread que estaban en wait habilitados
            para continuar).
    wait(): queda en espera el thread cuando hasta que se establezca el evento. 

'''
import threading
import time
import random

class Worker(threading.Thread):
    def __init__(self, event, worker_id):
        super().__init__()
        self.event = event
        self.worker_id = worker_id

    def run(self):
        print(f"Trabajador {self.worker_id} está esperando el evento para empezar.\n",end="")
        self.event.wait()                    # ESPERA a que el evento se establezca
        print(f"Trabajador {self.worker_id} ha comenzado a trabajar.\n",end="")
        time.sleep(random.uniform(1, 3))     # Simula el tiempo de ejecución
        print(f"Trabajador {self.worker_id} ha terminado el trabajo.\n",end="")

def main():
    event = threading.Event()                # Se CREA una intancia del EVENTO

    # Crea una lista de trabajadores (hilos)
    workers = []                             # Lista de workers
    for i in range(5):
        worker = Worker(event, i)            # Instancia thread      
        workers.append(worker)               # Agregar instancias a la lista de workers

    # Inicia todos los hilos (estarán esperando el evento)
    for worker in workers:                   # recorre la lista con los objetos thread
        worker.start()                       # Ejecuta thread

    print("Preparando todo...\n",end="")
    time.sleep(2)                            # Simula preparación antes de iniciar el evento

    print("¡Listo! Iniciando evento.\n",end="")
    event.set()                              # ESTABLECE EL EVENTO, permitiendo que los hilos continúen

    # Espera a que todos los hilos terminen
    for worker in workers:
        worker.join()

    print("Todos los trabajadores han terminado.")

if __name__ == "__main__":
    main()
    