'''
INTERBLOQUEO
En el siguiente programa se puede observar  dos funciones 'thread1' y 'thread2'
que cuando se ejecutan concurrentes se bloquean (entre ellas) disputanto el uso del
recurso compartido 'recurso' en cuyo diccionario se desea escribir en la clave 'val'
Dentro de las funciones se incrementa en 1 el valor de la clave 'val', sólo si el
recurso está disponible, si el recurso no está disponible (ocupado) entonces se pierde
el turno de escribir sobre la clave.

Observar que cuando las funciones son concurrentes se producen bloqueos y el resultado varia
con respecto a la ejecución secuencial donde no se produce bloqueo.

Comentario: Las funciones son "casi iguales", la única diferencia una con respecto a otra es
que se invierten la secuencia de acceso al recurso compartido como para forzar a un
interbloqueo en la concurrencia. 

'''
import threading
import time
import random

# recurso -> Variables de condición compartidas
#   Se desea acceder a la clave 'val' para escribirla
#   sólo una sóla función 'thread1' o 'thread2' podrá acceder
#   True -> recurso OCUPADO , False -> recurso LIBRE
recurso = {'val':0,'thread1': False, 'thread2': False}

def thread1(cant,tini,tfin):
    for i in range(cant):  # Intenta varias veces
        print(f"Thread 1 Intento({i})\n",end="")
        if not recurso['thread1']:
            recurso['thread1'] = True                  # thread1 OCUPA del recurso (obtiene el permiso)
            time.sleep(random.uniform(tini,tfin))      # Simula trabajo extra antes de acceder a recurso compartido
            if not recurso['thread2']:              
                print(f"Thread 1 ACTUACION ({i}).\n",end="")
                recurso['val']+=1                      # ACTUA sobre el recurso compartido
                                                       # en este caso actua modificando la clave val
            else:
                print(f"Thread 1 BLOQUEADO(perdío su turno de intento ({i})).\n",end="")
            recurso['thread1'] = False                 # thread1 LIBERA del recurso
    
def thread2(cant,tini,tfin):
    for i in range(cant):  # Intenta varias veces
        print(f"Thread 2 Intento({i})\n",end="")
        if not recurso['thread2']:
            recurso['thread2'] = True                 # thread2 OCUPA del recurso (obtiene el permiso)
            time.sleep(random.uniform(tini,tfin))     # Simula trabajo extra antes de acceder a recurso compartido
            if not recurso['thread1']:
                print(f"Thread 2 ACTUACION ({i}).\n",end="")
                recurso['val']+=1                     # ACTUA sobre el recurso compartido 
            else:
                print(f"Thread 2 BLOQUEADO(perdío su turno de intento ({i})).\n",end="")
            recurso['thread2'] = False                # thread2 LIBERA del recurso
         
def concurrente():
    print("CONCURRENTE\n",end="")
    t1 = threading.Thread(target=thread1,args=(5,0.03,0.033))  # Creando hilos
    t2 = threading.Thread(target=thread2,args=(5,0.3,0.33))    # 
    t1.start() # Iniciando hilos concurrentes
    t2.start()
    t1.join()  # Espera que termine thread
    t2.join()
    print("Valor final de val:",recurso['val'])
def secuencial():
    print("\nSECUENCIAL\n",end="")
    t1 = threading.Thread(target=thread1,args=(2,0.03,0.033))  # Creando hilos
    t2 = threading.Thread(target=thread2,args=(2,0.3,0.33))
    t1.start() # Iniciando hilos concurrentes
    t1.join()  # Espera que termine thread
    t2.start()
    t2.join()
    print("Valor final de val:",recurso['val'])
def main():
    secuencial()
    print()
    concurrente()
if __name__==main():
    main()

