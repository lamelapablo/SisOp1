class Documento: # Clase Documento
    def __init__(self, contenido):
        self.contenido = contenido

class Impresora: # Clase Impresora
    def imprimir(self, texto):
        # Instancia creada dentro del método, relación de uso
        documento = Documento(texto)    # DEPENDENCIA
        print(f"Imprimiendo documento: {documento.contenido}")

# Ejemplo de uso
def main():
    impresora = Impresora()
    impresora.imprimir("\n.. Este es el contenido del documento...")

if __name__ == "__main__":
    main()
 
'''SALIDA
Imprimiendo documento:  .. Este es el contenido del documento…
'''
