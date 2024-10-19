'''
LOCK

Se busca que esté sincronizado los thread. La idea es que en una lista de acceso global
el primer thread realice incrementos o decrementos. Un vez que comienza un thread, bloquea y
hace todo lo que necesita (el incremento o decremento). El proximo thread ejecuta cuando se libera el lock.

Observar que si eliminamos el Lock, o sea thread_lock.acquire()   y thread_lock.release()
el resultado final (la impresión) que se obtendrá serán distinta e impredecible.
Ver que cuando está sincronizado siempre termina el contador en 0.

Métodos de threading.Lock() - 
     .acquire() : Se utiliza para adquirir un Lock  (el bloqueo)
     .release() : Se utiliza para liberar el Lock  (un bloqueo) que un hilo adquirió
                  previamente utilizando .acquire()
'''

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, thread_lock,accion,ls):
        threading.Thread.__init__(self)
        self.name = name
        self.accion=accion
        self.ls=ls
        self.thread_lock=thread_lock

    def run(self):
        print(f'Starting thread {self.name}.\n',end="")
        try:
            self.thread_lock.acquire()                           # Bloquear
            self.thread_count_addsub(self.name)                  # Funcion recurso compartido
        finally:
            self.thread_lock.release()                           # Desbloquear
        print(f'Finished thread {self.name}.\n',end="")

    def thread_count_addsub(self,name):

        for  i in range(5):                              
            if self.accion=="+":
                self.ls[0]+=2
            else:
                self.ls[0]-=2
            # Realiza un trabajo simulado
            time.sleep(0.5)
            print(f'Thread {name} counting: {self.ls[0]}...\n',end="")
            

def main():
    # Crear un Lock para sincronización
    thread_lock = threading.Lock()              # Declaración (instancia) de un Lock. Es un objeto

    # Crear una lista que actuará como contador (listas son mutables)
    lsCounter=[0]
    # Crear los subprocesos
    thread1 = MyThread('A', thread_lock,"+",lsCounter)
    thread2 = MyThread('B', thread_lock,"-",lsCounter)
    
    # Empezar los subprocesos
    thread1.start()                                       
    thread2.start()                                       
    
    # Esperar a que todos los subprocesos terminen
    thread1.join()                                        
    thread2.join()                                        

    print('Finished.')
    
if __name__ == "__main__":
    main()

    
