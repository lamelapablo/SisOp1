'''
RLOCK
El ejemplo trata de 3 thread. Realizan una llamada a una función recursiva.
Una vez que un thread (en la primer llamada) toma y bloquea a la función recursiva ,
en la segunda llamada recursiva vuelve a ejecutar la función (previamente bloqueada por él),
por tanto la puede ejecutar sólo él gracias al tipo de bloqueo Rlock. Una vez que terminan
la funciones y sale de cada recursiva, se ejecuta el finally liberando el bloqueo de cada llamada.

Métodos de threading.Rlock() - 
     .acquire() : Se utiliza para adquirir un  Rlock  (el bloqueo)
     .release() : Se utiliza para liberar el Rlock  (un bloqueo) que un hilo adquirió
                  previamente utilizando .acquire()
'''
import threading
import time

class RecursiveTask(threading.Thread):
    def __init__(self, rlock, depth):
        super().__init__()
        self.rlock = rlock             # Recibe el objeto de bloqueo
        self.depth = depth

    def run(self):
        self.perform_task(self.depth)

    def perform_task(self, depth):
        
        try:
            self.rlock.acquire()           # Adquiere el RLock
            print(f"{threading.current_thread().name} ha adquirido el RLock a profundidad {depth}")
            if depth > 0:
                # Realiza un trabajo simulado
                time.sleep(1)
                # Llama recursivamente
                self.perform_task(depth - 1)
        finally:
            print(f"{threading.current_thread().name} está liberando el RLock a profundidad {depth}")
            self.rlock.release()           # Libera el RLock

def main():
    # instancia el objeto para hacer el rlock
    rlock = threading.RLock()
    
    # Crea varios hilos con diferentes profundidades
    threads = [
        RecursiveTask(rlock, 3),
        RecursiveTask(rlock, 2),
        RecursiveTask(rlock, 1)
    ]
    
    # Inicia los hilos
    for thread in threads:
        thread.start()
    
    # Espera a que todos los hilos terminen
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
