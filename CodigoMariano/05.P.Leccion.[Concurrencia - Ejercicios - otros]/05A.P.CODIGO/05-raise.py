def dividir(a, b):
    try:
        resultado = a / b
        res = resultado
    except ZeroDivisionError as e:
    #except Exception as e:
        print(f"Error en dividir: {e}")  # Imprime el error
        raise      # Re-lanza la excepción
        #raise  e  
    return res

def main():
    try:
        resultado = dividir(10, 0)
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("La operación de división falló.")
main()
