from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self._lista_productos = []
        self._lista_clientes = []

    def registrar_producto(self, producto: Producto):
        self._lista_productos.append(producto)
        print(f"¡Producto '{producto.nombre}' registrado con éxito!")

    def listar_productos(self):
        if not self._lista_productos:
            print("No hay productos registrados en el restaurante.")
            return
        print("\n--- LISTA DE PRODUCTOS ---")
        for prod in self._lista_productos:
            print(prod.mostrar_informacion())

    def buscar_producto(self, nombre_buscar: str) -> Producto:
        for prod in self._lista_productos:
            if prod.nombre.lower() == nombre_buscar.lower():
                return prod
        return None

    def registrar_cliente(self, cliente: Cliente):
        self._lista_clientes.append(cliente)
        print(f"¡Cliente '{cliente.nombre}' registrado con éxito!")

    def listar_clientes(self):
        if not self._lista_clientes:
            print("No hay clientes registrados en el restaurante.")
            return
        print("\n--- LISTA DE CLIENTES ---")
        for cli in self._lista_clientes:
            print(cli.mostrar_informacion())

    def buscar_cliente(self, id_buscar: str) -> Cliente:
        for cli in self._lista_clientes:
            if cli.id_cliente == id_buscar:
                return cli
        return None