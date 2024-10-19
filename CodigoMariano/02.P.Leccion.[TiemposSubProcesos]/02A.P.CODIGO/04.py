'''
DEAMON

'''
import threading
import time
import datetime as dt

class BackgroundTask(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True  # Establecer el hilo como demonio

    def run(self):        
        print("Hilo demonio en ejecución...\n",end="")
        while True:
            print(f'{ dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") }\n',end="")
            time.sleep(5)
            
def main():
    # Crear una instancia de la clase BackgroundTask
    background_thread = BackgroundTask()

    # Iniciar el hilo demonio
    background_thread.start()

    time.sleep(20)

    # El hilo principal continúa y finaliza
    print("Hilo principal terminado\n",end="")

if __name__ == "__main__":
    main()


