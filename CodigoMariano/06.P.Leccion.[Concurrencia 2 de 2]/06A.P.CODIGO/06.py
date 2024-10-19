'''
Barrier

La clase Worker extiende threading.Thread y recibe un objeto Barrier y un identificador de
trabajador (worker_id). Cada trabajador realiza una tarea simulada (primera etapa) y luego
espera en la barrera usando self.barrier.wait(). Todos los hilos deben llegar a este punto
antes de que cualquiera de ellos pueda continuar.

Método barrier.wait():
    self.barrier.wait() es el punto donde cada hilo espera hasta que todos los demás hilos
    lleguen a la barrera. 
    
Sincronización con la Barrera:
    Después de que todos los hilos pasan la barrera, cada uno realiza una segunda tarea simulada;
    es decir solo cuando todos los hilos han llamado a wait(), todos pueden
    continuar a la siguiente etapa.

Creación de la Barrera:
    En main(), se crea una barrera (barrier = threading.Barrier(num_workers)) que espera que
    los 5 hilos lleguen al punto de sincronización.

Finalización:
    Se espera que todos los hilos terminen, usando join(),y luego se imprime un mensaje
    indicando que todos han terminado.
    
Métodos de la clase threading.Barrier(num_workers)
    num_workers-> se pasa por parmetro la cantidad de thread que se necesitan para descativar la barrera
    .wait():      Cuando se dispara el método, mantiene bloquedo hasta que se desactiva cuando se llega
                  a la cantidad de thread 'num_worker' 


'''

import threading
import time
import random

class Worker(threading.Thread):
    def __init__(self, barrier, worker_id):
        super().__init__()
        self.barrier = barrier
        self.worker_id = worker_id

    def run(self):
        print(f"Trabajador {self.worker_id} está realizando la primera tarea.\n",end="")
        time.sleep(random.uniform(1, 3))     # Simula tiempo de trabajo
        print(f"Trabajador {self.worker_id} ha terminado la primera tarea y está esperando en la barrera.\n",end="")

        self.barrier.wait()                  # Espera a que todos los hilos lleguen a la BARRERA

        print(f"Trabajador {self.worker_id} ha pasado la barrera y está realizando la segunda tarea.\n",end="")
        time.sleep(random.uniform(1, 3))     # Simula tiempo de trabajo
        print(f"Trabajador {self.worker_id} ha terminado la segunda tarea.\n",end="")

def main():
    num_workers = 5                          # Cantidad de thread que deben llegra  a la barreraa par que se desactive
    barrier = threading.Barrier(num_workers) # intancia de la barrera

    workers = []                             # lista para almacenar los threads
    for i in range(num_workers):
        worker = Worker(barrier, i)          # instancia de cada thread
        workers.append(worker)               # agregar el thread a la lista 

    # Inicia todos los hilos
    for worker in workers:                   # recorrer la lista de threads
        worker.start()                       # arrancar el thread

    # Espera a que todos los hilos terminen
    for worker in workers:
        worker.join()                        

    
    

if __name__ == "__main__":
    main()