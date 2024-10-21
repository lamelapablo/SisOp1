import threading
import random
import time

class Producer(threading.Thread):
    def __init__(self, mensajes, condition, max_items):
        super().__init__()
        self.__mensajes: list[str] = mensajes
        self.__condition: threading.Condition = condition
        self.__max_items: int = max_items

    def run(self):
        for i in range(self.__max_items):
            time.sleep(random.uniform(0.5, 1.5))
            mensaje = f"Mensaje {i}"
            with self.__condition:
                self.__mensajes.append(mensaje)
                print(f"Productor envio mensaje -> {mensaje}\n", end="")
                self.__condition.notify()

class Consumer(threading.Thread):
    def __init__(self, mensajes, condition, max_items):
        super().__init__()
        self.__mensajes: list[str] = mensajes
        self.__condition: threading.Condition = condition
        self.__max_items = max_items

    def run(self):
        for _ in range(self.__max_items):
            with self.__condition:
                while not self.__mensajes:
                    self.__condition.wait()
                mensaje = self.__mensajes.pop(0)
                print(f"Consumidor recibio mensaje <- {mensaje}\n", end="")
            time.sleep(random.uniform(0.5, 1.5))

def main():
    semaphore = threading.Condition()
    mensajes: list[str] = []
    max_items = 5
    
    producer: Producer = Producer(mensajes, semaphore, max_items)
    consumer: Consumer = Consumer(mensajes, semaphore, max_items)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()