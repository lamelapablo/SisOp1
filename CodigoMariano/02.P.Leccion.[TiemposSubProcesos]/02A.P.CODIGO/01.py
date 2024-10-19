'''
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
import random
def getTime():
    '''
    #ns: nanosegundos -> '10**-9' o comunmente se escribe '1e-09'
    '''
    #return time.perf_counter_ns()      # Usando time en nanosegundos    
    return time.perf_counter()          # Usando time  en segundos
def verTiempos(di):
    '''
    Imprime una tabla con el Analisis de tiempos de ejecución
    '''
    print("\n")
    print("-"*20)
    print("Analisis de tiempos")
    print("....................")
    su=0
    for k in di:
        if k!="Proceso":
            su+=di[k]
        print(f'{k:10}{di[k]:035.25f}')    
    print("....................")
    # DIFERENCIA entre la sumatoria de tiempos de thread y el tiempo del proceso
    dif=su-(di["Proceso"])
    print(f'{"Difer.":10}{dif:+035.25f}')
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
        data = [i*i for i in range(self.cantidad)]
        print(f"{self.name}: Cargo {self.cantidad} numeros\n",end="")
        
def main():
    print("-"*20)
    print("INICIO del Proceso\n",end="")
    print("....................")
    tiempoIni=getTime()                      # Obtener el tiempo de inicio del proceso
    diTiempo={}
    t0=MyThread(0,diTiempo,10000000) # Instancia del thread
    t1=MyThread(1,diTiempo,10000000) # Instancia del thread
    t2=MyThread(2,diTiempo,10000000) # Instancia del thread
    
    t0.start()                       # Ejecutar el thread
    t1.start()                       # Ejecutar el thread
    t2.start()                       # Ejecutar el thread
    
    t0.join()                        # Espera que termine para continuar (secuencial)
    t1.join()                        # Espera que termine para continuar (secuencial)
    t2.join()                        # Espera que termine para continuar (secuencial)

    diTiempo["Proceso"]= getTime()-tiempoIni # Obtener el tiempo de fin del proceso
    print("....................")
    print("FIN del Proceso\n",end="-"*20)
    verTiempos(diTiempo)             # Visualizar tabla resumen de tiempos
    #print(f"Datos: {di}\n",end="")  

if __name__ == "__main__":
    main()
