import threading
import time
import random

class Producer(threading.Thread):
    def __init__(self, data, semaphore, max_items):
        super().__init__()
        self.__data: list[int] = data
        self.__semaphore = semaphore
        self.__max_items: int = max_items

    def run(self):
        for _ in range(self.__max_items):
            #time.sleep(random.uniform(0.5, 1.5))
            item = random.randint(0, 100)
            self.__data.append(item)
            print(f"Productor produjo {item}\n", end="")
            self.__semaphore.release()

class Consumer(threading.Thread):
    def __init__(self, data, semaphore, max_items):
        super().__init__()
        self.__data: list[int] = data
        self.__semaphore = semaphore
        self.__max_items = max_items

    def run(self):
        for _ in range(self.__max_items):
            self.__semaphore.acquire()
            item = self.__data.pop(0)
            print(f"Consumidor consumio {item}\n", end="")
            #time.sleep(random.uniform(0.5, 1.5))

def main():
    semaphore = threading.Semaphore(0)
    data: list[int] = []
    max_items = 10
    
    producer: Producer = Producer(data, semaphore, max_items)
    consumer: Consumer = Consumer(data, semaphore, max_items)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()