# Actualizado 13/08/2024 00:30
import threading

class MyThread(threading.Thread):                           # (1)
    def __init__(self):                                     # (1.1)
        super(MyThread, self).__init__()                    # (1.2)
        # Se pueden configurar otras cosas antes
        #    de que comience el hilo.
    def run(self):                                          # (1.3)
        print ("Ejecutando")

def main():
    thread_list = []
    for i in range(4):
        thread = MyThread()                                 # (2.1)
        thread_list.append(thread)
        thread.start()                                      # (2.2)
    #print(thread_list)
if __name__ == "__main__":
    main()  

'''
thread utilizando la clase 'Thread' que se encuentra en el módulo threading
    La creación de subprocesos en una clase puede resultar muy útil, 
    ya que se pueden tener muchos métodos específicos de un subproceso 
    y es más fácil mantener. 
   

# (1)
    MyThread hereda de threading.Thread
    
# (1.1)
    Método constructor

# (1.2)
    Llamada al método constructor de la superclase.

# (1.3)
    Método que cuando se ejecuta inicia el nuevo thread.

# (2.1)
    thread = MyThread()
    Objeto thread es un instancia de MyThread()

# (2.2)
    .start()
    método que inicia el objeto de la llamada al thread 
    inicializado llamando al método run()

'''

