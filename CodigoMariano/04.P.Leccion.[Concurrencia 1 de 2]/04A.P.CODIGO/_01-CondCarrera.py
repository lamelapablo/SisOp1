'''
CONDICION DE CARRERA
En el siguiente programa se puede observar una condición de carrera entre dos threads
compitiendo por la variable global 'x'.
Observar que las llamadas donde las ejecuciones de los threads son concurrentes
se obtiene resultados distintos e incorrectos. Y las llamadas donde las ejecuciones de los
threads son secuenciales se obtiene resultados iguales y correctos.

la función transaccion simula el ingreso y egreso de divisas. Sólo se podrá egresar
divisas si el valor de x > 0

'''

from threading import Thread
import time
x=0 # recurso compartido, 'x' es global (REPRESENTA UNA CUENTA)

def transaccion(val,delay,op):
    # IMPORTANTE: No se puede hacer egreso de divisas SI x<=0
    global x                        # recurso compartido    
    for i in range(10):             # Se realizan 10 transacciones    
        if x>0 and op=="-":           # representa egreso de divisas
            time.sleep(delay)         # tiempo simulado de proceso
            x=x-val
        elif  op=="+":                # representa ingreso de divisas
            time.sleep(delay)         # tiempo simulado de proceso
            x=x+val

def secuencial(cll):
    global x
    
    print(f"\nResultdos de {cll} llamadas secuenciales:\n",end="")
    for _ in range(cll):
        x=0         # recurso compartido 
        t1 = Thread(target=transaccion,args=(1,0.00001,"+"))
        t2 = Thread(target=transaccion,args=(1,0.0000001,"-"))
        t1.run()
        t2.run()         
        print(f"{x:2}",end=",")
    print()
        
def concurrente(cll):
    global x
    cll = 30        # cantidad de llamadas
    print(f"Resultdos de {cll} llamadas concurrentes:\n",end="")
    for _ in range(cll):
        x=0         # recurso compartido (iniciliza en cero para cada llamada)
        t1 = Thread(target=transaccion,args=(1,0.00001,"+"))      # ingresa valores
        t2 = Thread(target=transaccion,args=(1,0.0000001,"-"))    # engresa valor
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(f"{x:2}",end=",")
    print()
        
def main():
    cll = 30        # cantidad de llamadas
    secuencial(cll)
    concurrente(cll)
    
if __name__==main():
    main()
