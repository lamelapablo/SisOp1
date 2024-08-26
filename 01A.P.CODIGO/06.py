import threading
import time
from datetime import datetime
import random

def getTime():
    #Obtiene el valor del tiempo del instante actual
    now = datetime.now()
    hora_actual = now.strftime("%H:%M:%S")
    micro = int(now.microsecond)
    return f'{hora_actual}.{micro:06d}'

class MyThread(threading.Thread):
    def __init__(self,numthread,diRes):
        super(MyThread, self).__init__()
        self.inf=0
        self.sup=999
        self.name=f"thread-{numthread}"
        self.diRes=diRes
        
    def run(self):
        print (f"comienzo {self.name}\n",end="")
        self.diRes[self.name]=[None,getTime(),None] # Almacena en diRes el tiempo de inicio del thread
        self.obtenerValor() #time.sleep(2)
        print (f"finalizado {self.name}\n",end="")  # Almacena en diRes el tiempo de finalización del thread
        self.diRes[self.name][2]=getTime()
        
    def obtenerValor(self):
        #Obtiene un valor aleatorio entre inf y sup, y almacena
        #el valor aleatorio el el diccionario diRes
        self.diRes[self.name][0]=random.randint(self.inf,self.sup)
        
    
def main():
    di={}
    
    t0=MyThread(0,di) # Instancia del thread
    t1=MyThread(1,di) # Instancia del thread
    t2=MyThread(2,di) # Instancia del thread
    t0.start()        # Ejecutar el thread
    t1.start()        # Ejecutar el thread  
    t2.start()        # Ejecutar el thread
    
    print(f"Antes del sleep: {di}\n",end="")
    # Observar que Antes del sleep seguramente el 'di' no está completo
    time.sleep(1) # Espera de 1 segundo para ejecutar siguiente instrucción
    print(f"Despues del sleep: {di}\n",end="")  
    
if __name__ == "__main__":
    main()
        