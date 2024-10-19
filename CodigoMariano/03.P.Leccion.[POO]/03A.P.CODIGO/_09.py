class Circulo:
    _pi = 3.1416              # Atributo de clase
    def __init__(self, radio):
        self.radio = radio    # Atributo de instancia
    def verpi(cls):
        return "pi es {}".format(cls._pi)
    @classmethod
    def cambiar_pi(cls, nuevo_pi):
        cls._pi = nuevo_pi    # Modifica el atributo de clase
c2=Circulo(2)
c5=Circulo(5)
print("(1) En c2 {}; en c5 {}".format(c2.verpi(),c5.verpi()))
Circulo.cambiar_pi(3.14)      # Modifica a nivel de clase
print("(2) En c2 {}; en c5 {}".format(c2.verpi(),c5.verpi()))

''' SALIDA
(1) En c2 pi es 3.1416; en c5 pi es 3.1416
(2) En c2 pi es 3.14; en c5 pi es 3.14
'''
