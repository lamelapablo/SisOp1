# Actualizado 12/08/2024 23:30
import threading

def worker(number):                                         # (1)
    print (f'Soy el thread: {number}\n',end="")

def main():
    thread_list = []
    for i in range(4):
        thread = threading.Thread(target=worker, args=(i,)) # (2)
        thread_list.append(thread)
        thread.start()                                      # (3)
    print(thread_list)

if __name__ == "__main__":
    main()  
    
'''
Se carga una función en un thread. La función recibe parámetro.
https://docs.python.org/3/library/threading.html

# (1)
    Funcíón 'worker' que inprime un string. Está función
    será la ejecutará el 'thread'. Recibe un número por parámetro.
    Con el parámetro se puede identificar el thread que se está 
    ejecutando.
# (2)
    Crea el objeto thread que es un instancia de Thread
    Se inicializa el objeto pasando por parámetro en 'target' 
    la función 'worker' que es la función que se cargará en 
    el 'thread' para su ejecución. Además le pasa por 
    parámetro en 'args' los parámetro que recibe de la función 
    'worker'  en formato de tuple.

# (3)
    Una vez que se crea un objeto de subproceso, se debe iniciar 
    su actividad llamando al start() que es un método del subproceso. 
    Esto invoca al método  run()  en un subproceso de control independiente.
    Una vez que se inicia la actividad del hilo, este se considera "activo". 
    Deja de estar activo cuando el método run() finaliza, ya sea de manera 
    normal o al generar una excepción no controlada. 
    El método is_alive() informa si el hilo está activo.

    Si descomenta #print(thread_list) podrá visualizar en la lista los números de
    proceso y su estado, para un instante de tiempo.
'''
    
    