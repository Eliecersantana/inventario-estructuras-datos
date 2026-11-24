from arreglos import Producto, ordenar_productos
from lista_enlazada import ListaEnlazadaInventario
from pilas import PilaOperaciones
from cola import ColaPedidos
from abb import ArbolBinarioBusqueda


class SistemaInventario:
    """Integra los 5 módulos de estructuras de datos para gestionar el inventario."""

    def __init__(self):
        self.catalogo_lista = ListaEnlazadaInventario()
        self.historial = PilaOperaciones(limite=10)
        self.pedidos = ColaPedidos()
        self.indice_abb = ArbolBinarioBusqueda()

    def agregar_producto(self, producto: Producto) -> None:
        self.catalogo_lista.agregar_producto(producto)
        self.indice_abb.insertar(producto)
        self.historial.registrar_operacion(
            tipo="agregar",
            detalle=f"Agregado {producto.codigo} - {producto.nombre} (x{producto.cantidad})",
            datos_previos=producto,
        )

    def buscar_rapido(self, codigo: str) -> Producto | None:
        return self.indice_abb.buscar_por_codigo(codigo)

    def listar_ordenado_por_codigo(self) -> None:
        self.indice_abb.mostrar_inorden()

    def listar_ordenado_por_criterio(self, productos: list[Producto], criterio: str = "nombre") -> list[Producto]:
        return ordenar_productos(productos, criterio)


def probar_sistema() -> None:
    sistema = SistemaInventario()

    productos_base = [
        Producto("P003", "Teclado Mecanico", 15, 45.00),
        Producto("P001", "Mouse Inalambrico", 30, 18.50),
        Producto("P002", "Monitor 24 Pulgadas", 8, 165.00),
        Producto("P004", "Audifonos USB", 20, 29.99),
    ]

    for prod in productos_base:
        sistema.agregar_producto(prod)

    print("\n--- ABB Inorden (por código) ---")
    sistema.listar_ordenado_por_codigo()

    print("\n--- Arreglo ordenado por precio ---")
    for p in sistema.listar_ordenado_por_criterio(productos_base, "precio"):
        print(p)

    print("\n--- Búsqueda rápida en ABB (P002) ---")
    encontrado = sistema.buscar_rapido("P002")
    print(encontrado if encontrado else "No encontrado")

    print("\n--- Cola de pedidos ---")
    if encontrado:
        sistema.pedidos.encolar_pedido("Ana Gómez", encontrado, 2)
        sistema.pedidos.mostrar_cola()
        sistema.pedidos.atender_pedido()

    print("\n--- Pila de historial ---")
    sistema.historial.mostrar_historial()
    sistema.historial.deshacer_ultima_operacion()


if __name__ == "__main__":
    probar_sistema()