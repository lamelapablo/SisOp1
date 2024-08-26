'''
EJECUCIÓN SECUENCIAL(SINCRONO) Y CONCURRENTE(ASINCRONO) - 
INTENSIVO EN I/O.

Código python donde se ejecuta 3 thread y se evalúa los tiempos de ejecución.
La función que se ejecuta 'funcionAEjecutar' sólo obtiene un numero aleatorio.
Se utiliza 'time.perf_counter_ns()' para obtener un momento en el tiempo con alta presición.
Se imprime una tabla resumen con el Analisis de tiempos.
    # DIFERENCIA entre la sumatoria de tiempos de thread (stt) 'menos' el tiempo del proceso (tp)
    # Si difer <= 0 , es (-) o (cero) entonces -> stt <= tp
    #                => Significa que NO HUBO solapamiento de thread en tiempo de ejecución 
    #
    # Si difer > 0 , es (+) entonces -> stt > tp
    #                => Significa que HUBO solapamiento  de thread en tiempo de ejecución
    
'''
import threading
import time


def getTime():
    #ns: nanosegundos -> '10**-9' o comunmente se escribe '1e-09'
    #return time.perf_counter_ns()      # Usando time en nanosegundos
    return time.perf_counter()          # Usando time  en segundos
def verTiempos(di):
    print("\n")
    print("-"*20)
    print("Analisis de tiempos")
    print("....................")
    stt=0
    for k in di:
        if k!="Proceso":
            stt+=di[k]
        print(f'{k:10}{di[k]:035.25f}')    
    print("....................")
    # DIFERENCIA entre la sumatoria de tiempos de thread (stt) y el tiempo del proceso (tp)
    # Si difer <= 0 , es (-) o (cero) entonces -> stt <= tp
    #                => Significa que NO HUBO solapamiento de thread en tiempo de ejecución 
    #
    # Si difer > 0 , es (+) entonces -> stt > tp
    #                => Significa que HUBO solapamiento  de thread en tiempo de ejecución
    tp=di["Proceso"]
    difer=stt-tp
    print(f'{"Difer.":10}{difer:+035.25f}')
    print("-"*20)
    
class MyThread(threading.Thread):
    def __init__(self,numthread,diTiempo,cantidad):
        super(MyThread, self).__init__()
        self.inf=0
        self.sup=999
        self.name=f"thread-{numthread}"
        self.diTiempo=diTiempo
        self.cantidad=cantidad
    def run(self):
        #print (f"comienzo {self.name}\n",end="")
        self.diTiempo[self.name]=getTime()                          # Almacena en diRes el tiempo de inicio del thread
        self.funcionAEjecutar()                                     # Llamada a la función que está dentro del thread
        #print (f"finalizado {self.name}\n",end="")   
        self.diTiempo[self.name]=getTime()-self.diTiempo[self.name] # resta par obtener la cant. en seg. de duración
        
    def funcionAEjecutar(self):
        # FUNCION A EJECUTAR EN EL THREAD
        # Carga en una lista una secuencia de 'self.cantidad' de numeros
        
        for i in range(self.cantidad):
            f=open(f"03{self.name}.txt","w")     # Se abre y se cierra archivo en cada vuelta del ciclo para aumentar el acceso I/O
            f.write(f'{i*i}\n') 
            f.close()
        print(f"{self.name}: Cargo {self.cantidad} numeros\n",end="")
        
def ejecucionAsincrona(ct0,ct1,ct2):
    print("-"*20)
    print("INICIO del Proceso\n",end="")
    print("....................")
    tiempoIni=getTime()         # Obtener el tiempo de inicio
    diTiempo={}
    t0=MyThread(0,diTiempo,ct0) # Instancia del thread
    t1=MyThread(1,diTiempo,ct1) # Instancia del thread
    t2=MyThread(2,diTiempo,ct2) # Instancia del thread
    
    # - - - - - - INICIO Ejecución concurrente - - - - - - -
    t0.start()                  # Ejecutar el thread
    t1.start()                  # Ejecutar el thread
    t2.start()                  # Ejecutar el thread
    # - - - - - - - FIN  Ejecución concurrente - - - - - - -
    
    t0.join()                   # Espera que termine para continuar (secuencial)
    t1.join()                   # Espera que termine para continuar (secuencial)
    t2.join()                   # Espera que termine para continuar (secuencial)

    diTiempo["Proceso"]= getTime()-tiempoIni # Obtener el tiempo de fin
    print("....................")
    print("FIN del Proceso\n",end="-"*20)
    verTiempos(diTiempo)        # Visualizar tabla resumen de tiempos
    #print(f"Datos: {di}\n",end="")
    
def ejecucionSincrona(ct0,ct1,ct2):
    print("-"*20)
    print("INICIO del Proceso\n",end="")
    print("....................")
    tiempoIni=getTime()         # Obtener el tiempo de inicio
    diTiempo={}
    t0=MyThread(0,diTiempo,ct0) # Instancia del thread
    t1=MyThread(1,diTiempo,ct1) # Instancia del thread
    t2=MyThread(2,diTiempo,ct2) # Instancia del thread

    # - - - - - - INICIO Ejecución secuencial - - - - - - -
    t0.start()                  # Ejecutar el thread
    t0.join()                   # Espera que termine para continuar (secuencial)

    t1.start()                  # Ejecutar el thread
    t1.join()                   # Espera que termine para continuar (secuencial)

    t2.start()                  # Ejecutar el thread
    t2.join()                   # Espera que termine para continuar (secuencial)
    # - - - - - - FIN Ejecución secuencial - - - - - - -
    # ... continua secuencial
    
    diTiempo["Proceso"]= getTime()-tiempoIni # Obtener el tiempo de fin
    print("....................")
    print("FIN del Proceso\n",end="-"*20)
    verTiempos(diTiempo)                     # Visualizar tabla resumen de tiempos
    #print(f"Datos: {di}\n",end="")
    

def main():
    #Por cada thread, cantidad de elementos que se cargará en un archivo (función que ejecuta el thread)
    ct0=300
    ct1=200
    ct2=100
    
    print("* * * I N I C I O  EJECUTA ASINCRONO * * * ")
    ejecucionAsincrona(ct0,ct1,ct2)       # CONCURRENTE
    print("* * * F I N   EJECUTA ASINCRONO * * *")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("* * * I N I C I O  EJECUTA SINCRONA * * * ")
    ejecucionSincrona(ct0,ct1,ct2)        # SECUENCIAL
    print("* * * F I N   EJECUTA SINCRONA * * *")

if __name__ == "__main__":
    main()
 