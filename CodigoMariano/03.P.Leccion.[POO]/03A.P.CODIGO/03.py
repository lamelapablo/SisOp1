class CarritoDeCompra:
    def __init__(self):
        self.__productos = {}  # Diccionario privado para almacenar productos en el carrito

    # Método para agregar un producto al carrito
    def agregar_producto(self, nombre, precio, cantidad=1):
        if nombre in self.__productos:
            self.__productos[nombre]['cantidad'] += cantidad
        else:
            self.__productos[nombre] = {'precio': precio, 'cantidad': cantidad}
        print(f"Producto '{nombre}' agregado/actualizado en el carrito. Precio: {precio}, Cantidad: {cantidad}")

    # Método para eliminar un producto del carrito
    def eliminar_producto(self, nombre):
        if nombre in self.__productos:
            del self.__productos[nombre]
            print(f"Producto '{nombre}' eliminado del carrito.")
        else:
            print(f"Producto '{nombre}' no encontrado en el carrito.")

    # Método para actualizar la cantidad de un producto
    def actualizar_cantidad(self, nombre, nueva_cantidad):
        if nombre in self.__productos:
            if nueva_cantidad > 0:
                self.__productos[nombre]['cantidad'] = nueva_cantidad
                print(f"Cantidad del producto '{nombre}' actualizada a {nueva_cantidad}.")
            else:
                self.eliminar_producto(nombre)
        else:
            print(f"Producto '{nombre}' no encontrado en el carrito.")

    # Método para calcular el total del carrito
    def calcular_total(self):
        total = sum(producto['precio'] * producto['cantidad'] for producto in self.__productos.values())
        print(f"Total del carrito: {total}")
        return total

    # Método para mostrar los productos en el carrito
    def mostrar_carrito(self):
        if not self.__productos:
            print("El carrito está vacío.")
        else:
            print("Carrito de compras:")
            for nombre, datos in self.__productos.items():
                print(f"Producto: {nombre}, Precio: {datos['precio']}, Cantidad: {datos['cantidad']}")

def main():
    carrito = CarritoDeCompra()

    # Agregar productos
    carrito.agregar_producto("Camisa", 20.0, 2)
    carrito.agregar_producto("Pantalones", 35.0, 1)
    carrito.agregar_producto("Zapatos", 50.0, 1)

    # Mostrar carrito
    carrito.mostrar_carrito()

    # Actualizar cantidad
    carrito.actualizar_cantidad("Camisa", 3)

    # Mostrar carrito actualizado
    carrito.mostrar_carrito()

    # Calcular total del carrito
    carrito.calcular_total()

    # Eliminar un producto
    carrito.eliminar_producto("Pantalones")
    carrito.mostrar_carrito()

if __name__ == "__main__":
    main()