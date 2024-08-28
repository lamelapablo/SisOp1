import threading
import time

path = "/home/paul1213/UCA/SisOp1/02_Ejercicios"

class MyThread(threading.Thread):
    def __init__(self,numthread,diTiempo,nPrimos,valorInicial):
        super(MyThread, self).__init__()
        self.name=f"Thread-{numthread}"
        self.numthread=numthread
        self.diTiempo=diTiempo
        self.nPrimos=nPrimos
        self.valorInicial=valorInicial

    def run(self):
        self.diTiempo[self.name]=getTime()  # Almacena en diRes el tiempo de inicio del thread
        self.saveListToFile(self.generateList())
        self.diTiempo[self.name]=getTime()-self.diTiempo[self.name] # resta par obtener la cant. en seg. de duración

    def generateList(self):
        ls = []
        copiaValIn = self.valorInicial
        while len(ls)!=self.nPrimos:
            if(self.esPrimo(copiaValIn)):
                ls.append(copiaValIn)
            copiaValIn+=1

        return ls

    def saveListToFile(self, ls):
        with open(f"{path}/ej3_{self.name}.txt", "w") as file:
            for num in ls:
                file.write(f'{num}\n')
    
    def esPrimo(self,num):
        if num > 1:
            # Iterate from 2 to n // 2
            for i in range(2, (num//2)+1):
                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False


def ejecucionSincrona():
    print("-"*20)
    print("INICIO del proceso\n",end="")
    print("....................")

    tiempoIni=getTime()
    diTiempo={}

    t0 = MyThread(0,diTiempo,10,0)
    t1 = MyThread(1,diTiempo,20,50)
    t2 = MyThread(2,diTiempo,3000,100)

    t0.start()
    t0.join()

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    diTiempo["Proceso"]= getTime()-tiempoIni # Obtener el tiempo de fin
    print("....................")
    print("FIN del proceso\n",end="-"*20)
    verTiempos(diTiempo)

def ejecucionAsincrona():
    print("-"*20)
    print("INICIO del proceso\n",end="")
    print("....................")

    tiempoIni=getTime()
    diTiempo={}

    t0 = MyThread(0,diTiempo,10,0)
    t1 = MyThread(1,diTiempo,20,50)
    t2 = MyThread(2,diTiempo,3000,100)

    t0.start()
    t1.start()
    t2.start()

    t0.join()
    t1.join()
    t2.join()

    diTiempo["Proceso"]= getTime()-tiempoIni # Obtener el tiempo de fin
    print("....................")
    print("FIN del proceso\n",end="-"*20)
    verTiempos(diTiempo)


def getTime():
    '''
    #ns: nanosegundos -> '10**-9' o comunmente se escribe '1e-09'
    '''
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

    tp=di["Proceso"]
    difer=stt-tp
    print(f'{"Difer.":10}{difer:+035.25f}')
    print("-"*20)

def main():
    print("* * * I N I C I O  EJECUTA ASINCRONO * * * ")
    ejecucionSincrona()
    print("* * * F I N  EJECUTA ASINCRONO * * *")
    print("# # # # # # # # # # # # # # # # # # # # # # # # ")
    print("* * * I N I C I O  EJECUTA SINCRONA * * * ")
    ejecucionAsincrona()
    print("* * * F I N   EJECUTA SINCRONA * * *")

if __name__ == "__main__":
    main()


#CONCLUSION -> Es mas eficiente la ejecucion asincrona ya que la DIFERENCIA entre la sumatoria de tiempos de thread (stt) 'menos' el tiempo del proceso (tp) es positiva, es decir, HUBO solapamiento de thread en tiempo de ejecución