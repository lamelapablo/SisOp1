class Matematicas:
   
    @staticmethod
    def suma(a, b):
        return a + b
   
    @staticmethod
    def resta(a, b):
        return a - b

# Llamar a los métodos estáticos directamente desde la clase
resultado_suma = Matematicas.suma(5, 3)
print(resultado_suma)  # Salida: 8

resultado_resta = Matematicas.resta(5, 3)
print(resultado_resta)  # Salida: 2
'''SALIDA
8
2
'''
