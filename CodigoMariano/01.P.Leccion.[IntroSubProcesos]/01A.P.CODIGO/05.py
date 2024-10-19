# Actualizado 14/08/2024 12:30
import threading

class MyThread(threading.Thread):
    def __init__(self,number):
        super(MyThread, self).__init__()
        self.number = number
    def run(self):
        print (self.name+'\n',end="")

def main():       
    thread_list = []
    for i in range(4):
        thread = MyThread(i)
        thread.name=f'MyThread {thread.number}'
        thread_list.append(thread)
        thread.start()
    #print (thread_list[0].name)
    #print (thread_list)
if __name__ == "__main__":
    main()  
