# Actualizado 13/08/2024 11:45
import threading

class MyThread(threading.Thread):                           # (1)
    def __init__(self, number):                             # (1.1)
        super(MyThread, self).__init__()                    # (1.2)
        self.number = number
    def run(self):                                          # (1.3)
        print (f'thread: {self.number}'+'\n',end="")

def main():

    thread_list = []
    for i in range(4):
        thread = MyThread(i)                                # (2.1)
        thread_list.append(thread)
        thread.start()                                      # (2.2)
    print(threading.enumerate())         # Muestra los hilos started
    print(thread_list)
    
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
    Método constructor, recibe por parámetro number cuando 
    la clase MyThread es instanciada.

# (1.2)
    Llamada al método constructor de la superclase.

# (1.3)
    Método que cuando se ejecuta inicia el nuevo thread.

# (2.1)
    thread = MyThread(i)
    Objeto thread es un instancia de MyThread()
    Se pasa i como parámetro de instancia.

# (2.2)
    .start()
    método que inicia el objeto de la llamada al thread 
    inicializado llamando al método run()

'''
