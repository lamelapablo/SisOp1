import threading

class Cine:
    def __init__(self):
        self.__salas: list[Sala] = []
        for i in range(5):
            self.__salas.append(Sala(50))

    @property
    def salas(self):
        return self.__salas


class Sala:
    def __init__(self, cantidad_asientos):
        self.__asientos = []
        for i in range(cantidad_asientos):
            self.__asientos.append(False)
        self.__lock = threading.Lock()
        self.__cantidad_asientos = cantidad_asientos

    def reservar_asiento(self, cantidad_a_reservar):
        self.__lock.acquire_lock()
        try:
            reservado = 0
            i = 0
            while i<self.__cantidad_asientos and reservado<cantidad_a_reservar:
                if self.__asientos[i] == False:
                    self.__asientos[i] = True
                    reservado += 1
                i+=1
            res = reservado == cantidad_a_reservar
        finally:
            self.__lock.release_lock()

        return res

class Usuario(threading.Thread):
    def __init__(self, nombre, cine:Cine, sala_id:int, cant_a_reservar:int):
        super().__init__()
        self.__nombre = nombre
        self.__cine: Cine = cine
        self.__sala_id: int = sala_id
        self.__cant_a_reservar: int = cant_a_reservar

    def __reservar_en_cine(self):
        if self.__cine.salas[self.__sala_id].reservar_asiento(self.__cant_a_reservar):
            print(f"{self.__nombre} ha reservado {self.__cant_a_reservar} asientos en la sala {self.__sala_id+1}\n", end="")
        else:
            print(f"{self.__nombre} no pudo reservar {self.__cant_a_reservar} asientos en la sala {self.__sala_id+1}\n", end="")

    def run(self):
        self.__reservar_en_cine()


def main():
    cine: Cine = Cine()
    usuarios: list[Usuario] = []
    for i in range(10):
        usuarios.append(Usuario(f"Usuario {i+1}", cine, i%5, i+1))

    for usuario in usuarios:
        usuario.start()

    for usuario in usuarios:
        usuario.join()

if __name__ == "__main__":
    main()