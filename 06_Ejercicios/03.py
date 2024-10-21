import threading
import random
import time

class Runner(threading.Thread):
    partieron_todos = True # Atributo de clase que indica si todos los corredores partieron

    def __init__(self, id, barrier):
        super().__init__()
        self.__id = id
        self.__barrier: threading.Barrier = barrier

    def run(self):
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Corredor {self.__id} esta listo ...\n", end="")
        self.__barrier.wait()
        if Runner.partieron_todos:
            Runner.partieron_todos = False
            print("Todos los corredores han partido!\n", end="")

        time.sleep(random.uniform(0.5, 1.5))
        print(f"Corredor {self.__id} ha terminado la carrera\n", end="")

def main():
    cant_runners = 5
    barrier = threading.Barrier(cant_runners)
    runners: list[Runner] = []

    for i in range(cant_runners):
        runners.append(Runner(i+1, barrier))

    for runner in runners:
        runner.start()

    for runner in runners:
        runner.join()

if __name__ == "__main__":
    main()