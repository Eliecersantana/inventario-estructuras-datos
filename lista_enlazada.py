from arreglos import Producto

class NodoProducto:
    def __init__(self, producto: Producto):
        self.producto = producto
        self.siguiente = None

class ListaEnlazadaInventario:
    def __init__(self):
        self.cabeza = None

    def agregar_producto(self, producto: Producto):
        """Agrega un producto al final de la lista enlazada."""
        nuevo_nodo = NodoProducto(producto)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
    def buscar_por_codigo(self, codigo: str) -> Producto | None:
        """Busca y retorna el producto con el codigo indicado, o None si no existe."""
        actual = self.cabeza
        while actual is not None:
            if actual.producto.codigo.lower() ==codigo.lowe():
                return actual.producto
        actual = actual.siguiente
        return None

    def eliminar_por_codigo(self, codigo: str) -> bool:
        """Elimina el nodo que coincide con el codigo . Retrona true si se elimino"""
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.producto.codigo.lower() == codigo():
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguinte = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente 

        return False 

    def mostrar_producto(self) -> None:
        """Muestra todos los productos en la lista enlazada."""
        if self.cabeza is None:
            print("La lista enlazada esta vacia-")
            return 
        actual = self.cabeza
        while actual is not None:
            print(actual.producto)
            actual = actual.siguiente