class Tienda:
    """Clase Tienda."""

    def __init__(self, nombre):
        """Constructor de la clase."""
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nuevo_producto):
        """
        Toma un producto y lo agrega a la tienda.

        Parámetros:
            nuevo_producto: Un objeto Producto
        Retorno:
            self: El objeto Tienda
        """
        self.productos.append(nuevo_producto)
        return self

    def vender_producto(self, id):
        """
        Elimina el producto de la lista de productos de la tienda mediante el
        id (supón que el id es el índice del producto en la lista) e imprime 
        su información.

        Parámetros:
            id: El id del producto a eliminar
        Retorno:
            self: El objeto Tienda
        """
        self.productos.pop(id)
        return self

    def inflacion(self, porcentaje_aumento):
        """
        Aumenta el precio de cada producto por el porcentaje_aumento dado 
        (¡Utiliza el método que escribiste en la clase Producto!)

        Parámetros:
            porcentaje_aumento: El porcentaje de aumento del precio
        Retorno:
            self: El objeto Tienda
        """
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento, True)
        return self

    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        """
        Actualiza todos los productos que coinciden con la categoría dada al 
        reducir el precio por el porcentaje_descuento dado
        (¡Utiliza el método que escribiste en la clase Producto!)

        Parámetros:
            categoria: La categoría de los productos a actualizar
            porcentaje_descuento: El porcentaje de descuento del precio
        Retorno:
            self: El objeto Tienda
        """
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_descuento, False)
        return self


class Producto:
    """Clase Producto."""

    def __init__(self, nombre, precio, categoria):
        """Constructor de la clase."""
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        """
        Actualiza el precio del producto. Si está_elevado es True, el precio 
        debería aumentar en el cambio_porcentaje proporcionado. Si es False, 
        el precio debería disminuir en el cambio_porcentaje proporcionado.

        Parámetros:
            cambio_porcentaje: El porcentaje de cambio del precio
            esta_elevado: Un booleano que indica si el precio debe aumentar o disminuir
        Retorno:
            self: El objeto Producto
        """
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje
        else:
            self.precio -= self.precio * cambio_porcentaje
        return self
    
    def imprimir_info(self):
        """
        Imprime el nombre del producto, categoría y precio.

        Retorno:
            self: El objeto Producto
        """
        print(f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}")
        return self
    

# Crear instancias de Producto:
chocolate = Producto(nombre="Chocolate", precio=100, categoria="Confites")
super_8 = Producto(nombre="Super 8", precio=50, categoria="Confites")

# Crear una instancia de Tienda:
la_tiendita = Tienda(nombre="La tiendita")

# Agregar productos a la tienda:
la_tiendita.agregar_producto(chocolate)
la_tiendita.agregar_producto(super_8)

print("Stock de la tienda:")
for producto in la_tiendita.productos:
    producto.imprimir_info()

# Vendemos un producto. Supón que el id es el índice del producto en la lista.
# la_tiendita.vender_producto(0)

print("Stock de la tienda después de vender un producto:")
for producto in la_tiendita.productos:
    producto.imprimir_info()

# Aumentar el precio de todos los productos en un 20%.
la_tiendita.inflacion(0.2)

print("Stock de la tienda después de inflación:")
for producto in la_tiendita.productos:
    producto.imprimir_info()

# Hacer una liquidación en la categoría "Confites" de 50%.
la_tiendita.hacer_liquidacion("Confites", 0.5)

print("Stock de la tienda después de liquidación:")
for producto in la_tiendita.productos:
    producto.imprimir_info()
