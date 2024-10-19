'''
SEMAPHORE
El ejemplo trata de una simulación de personas que intentan entrar a una sala.
La sala tiene una restrición que es que sólo pueden haber tres personas a la vez.
La simulación corresponde a 10 personas en total. Cada persona se podrá quedar
en la sala entre 1 a 3 segundos (determiado de forma aleatoria).

Se crea un Semaphore con un número máximo de permisos (maxpers),  que representa
la capacidad máxima de personas en la sala.

Se crean varios hilos (instancias de Persona). Cada hilo intentará entrar en la sala,
respetando el límite del semáforo.
enter_room: es la función para entrar a la sala.

Métodos de threading.Semaphore() -

    .acquire():  solicitar un permiso del semáforo antes de acceder a un recurso compartido.
                 Cuando accede (bloquea) se descuenta en uno el valor de la cantidad de
                 acceso disponible.
    .release():  linera el recurso. cuando libera (desbloquea) e incrementa en uno el valor
                 de la cantidad de acceso disponible.
    ._value:     retorna el valor de la cantidad de acceso disponible. 


'''

import threading
import time
import random

class Person(threading.Thread):
    def __init__(self, semaphore, person_id, maxpers):
        super().__init__()
        self.semaphore = semaphore
        self.person_id = person_id
        self.maxpers = maxpers

    def run(self):
        self.enter_room()

    def enter_room(self):
        print(f"Persona {self.person_id} está esperando para entrar (    hay {self.maxpers-self.semaphore._value} en sala.)\n",end="")
        self.semaphore.acquire()              # Intenta adquirir el semáforo
        
        try:
            print(f"Persona {self.person_id} ha entrado en la sala.     ( >> hay {self.maxpers-self.semaphore._value} en sala.)\n",end="")
            time.sleep(random.uniform(1, 3))  # Simula tiempo dentro de la sala
        finally:
            print(f"Persona {self.person_id} está saliendo de la sala.  ( << hay {self.maxpers-self.semaphore._value -1} en sala.)\n",end="")
            self.semaphore.release()          # Libera el semáforo

def main():
    maxpers = 3  # Número máximo de personas en la sala al mismo tiempo
    semaphore = threading.Semaphore(maxpers)  # intancia del semáforo
    
    # Crea una lista vacía para los hilos
    people = []
    # crear y añadir los hilos a la lista
    for i in range(10):                       # Es decir se simularán 10 personas
        person = Person(semaphore, i, maxpers)
        people.append(person)
    
    # Inicia todos los hilos
    for person in people:
        person.start()
    
    # Espera a que todos los hilos terminen
    for person in people:
        person.join()

if __name__ == "__main__":
    main()