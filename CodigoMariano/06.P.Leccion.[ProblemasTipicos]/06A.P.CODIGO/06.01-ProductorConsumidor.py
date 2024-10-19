import threading
import time
import random

class Buffer:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.buffer = []
        self.espacios = threading.Semaphore(capacidad)  # Semáforo para controlar espacios disponibles
        self.elementos = threading.Semaphore(0)         # Semáforo para controlar elementos disponibles

    def agregar(self, item):
        self.espacios.acquire()  # Espera por un espacio disponible
        self.buffer.append(item)
        self.elementos.release()  # Señala la disponibilidad de un nuevo elemento

    def retirar(self):
        self.elementos.acquire()  # Espera por un elemento disponible
        item = self.buffer.pop(0)
        self.espacios.release()   # Señala la disponibilidad de un nuevo espacio
        return item

class Productor(threading.Thread):
    def __init__(self, buffer):
        super().__init__()
        self.buffer = buffer

    def run(self):
        while True:
            item = random.randint(1, 100)
            self.buffer.agregar(item)
            print(f"Producido {item}\n",end="")
            time.sleep(random.random())

class Consumidor(threading.Thread):
    def __init__(self, buffer):
        super().__init__()
        self.buffer = buffer

    def run(self):
        while True:
            item = self.buffer.retirar()
            print(f"Consumido {item}\n",end="")
            time.sleep(random.random())

# Uso de las clases
buf = Buffer(10)
p = Productor(buf)
c = Consumidor(buf)
p.start()
c.start()


'''

Explicación General del Código
El código define un sistema donde los productores generan datos aleatorios y los consumidores los procesan. Estos roles están modelados como hilos que interactúan con un buffer común. La clave para manejar la concurrencia en este escenario es el uso de semáforos, que son variables especiales que se utilizan para controlar el acceso a recursos comunes.

Clase Buffer
La clase Buffer gestiona un buffer con capacidad limitada. Los métodos agregar y retirar permiten a los productores añadir datos y a los consumidores retirarlos, respectivamente.

Atributos:
capacidad: El número máximo de elementos que el buffer puede contener.
buffer: Una lista que actúa como el almacenamiento real de datos.
espacios: Un semáforo que cuenta los espacios vacíos disponibles en el buffer.
elementos: Un semáforo que cuenta los elementos disponibles en el buffer para ser consumidos.
Uso de Semáforos
Los semáforos espacios y elementos juegan un papel crucial en la coordinación entre productores y consumidores.

Semáforo espacios
Inicialización: Se inicializa con el valor de la capacidad del buffer, lo que significa que al principio, el buffer tiene capacidad espacios vacíos disponibles para que los productores coloquen elementos.
Función en agregar: Cada vez que un productor quiere añadir un elemento al buffer, primero debe "adquirir" (decrementar) un espacio del semáforo espacios. Si no hay espacios disponibles (el semáforo espacios es 0), el productor se bloqueará hasta que un consumidor "libere" un espacio al consumir un elemento.
Semáforo elementos
Inicialización: Se inicializa a 0, indicando que inicialmente no hay elementos en el buffer para consumir.
Función en retirar: Antes de que un consumidor pueda retirar un elemento, debe "adquirir" (decrementar) el semáforo elementos. Si no hay elementos disponibles, el consumidor se bloqueará hasta que un productor agregue un elemento y "libere" (incremente) este semáforo.
Clases Productor y Consumidor
Ambas clases heredan de threading.Thread, lo que les permite operar en hilos separados. Utilizan el buffer para agregar y retirar elementos, respectivamente.

Productores: Continuamente generan nuevos elementos y los añaden al buffer.
Consumidores: Continuamente retiran elementos del buffer para procesarlos.
Conclusión
El uso de semáforos aquí es fundamental para garantizar que el buffer no se sobrecargue ni se vacíe completamente, lo que podría causar que los hilos se bloqueen indefinidamente o que se acceda a datos no válidos. Los semáforos proporcionan una manera elegante y efectiva de manejar la sincronización necesaria en este problema clásico de la programación concurrente.

'''
