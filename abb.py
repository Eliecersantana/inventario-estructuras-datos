from arreglos import Producto


class NodoABB:
    """Nodo individual dentro del Árbol Binario de Búsqueda."""

    def __init__(self, producto: Producto):
        self.producto = producto
        self.izquierda: NodoABB | None = None
        self.derecha: NodoABB | None = None


class ArbolBinarioBusqueda:
    """
    Módulo 5: Árbol Binario de Búsqueda (ABB).
    Indexa los productos por su código para búsquedas rápidas y listado ordenado.
    """

    def __init__(self):
        self.raiz: NodoABB | None = None

    def insertar(self, producto: Producto) -> None:
        """Inserta un producto en el árbol o actualiza sus datos si el código ya existe."""
        if self.raiz is None:
            self.raiz = NodoABB(producto)
        else:
            self._insertar_recursivo(self.raiz, producto)

    def _insertar_recursivo(self, actual: NodoABB, producto: Producto) -> None:
        codigo_nuevo = producto.codigo.upper()
        codigo_actual = actual.producto.codigo.upper()

        if codigo_nuevo < codigo_actual:
            if actual.izquierda is None:
                actual.izquierda = NodoABB(producto)
            else:
                self._insertar_recursivo(actual.izquierda, producto)
        elif codigo_nuevo > codigo_actual:
            if actual.derecha is None:
                actual.derecha = NodoABB(producto)
            else:
                self._insertar_recursivo(actual.derecha, producto)
        else:
            # Si el código ya existe, actualiza el producto
            actual.producto = producto

    def buscar_por_codigo(self, codigo: str) -> Producto | None:
        """Busca y retorna un producto por su código. Retorna None si no existe."""
        return self._buscar_recursivo(self.raiz, codigo.upper().strip())

    def _buscar_recursivo(self, actual: NodoABB | None, codigo: str) -> Producto | None:
        if actual is None:
            return None

        codigo_actual = actual.producto.codigo.upper()
        if codigo == codigo_actual:
            return actual.producto
        elif codigo < codigo_actual:
            return self._buscar_recursivo(actual.izquierda, codigo)
        else:
            return self._buscar_recursivo(actual.derecha, codigo)

    def recorrido_inorden(self) -> list[Producto]:
        """Retorna una lista con los productos ordenados ascendentemente por código."""
        resultado: list[Producto] = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, actual: NodoABB | None, resultado: list[Producto]) -> None:
        if actual is not None:
            self._inorden_recursivo(actual.izquierda, resultado)
            resultado.append(actual.producto)
            self._inorden_recursivo(actual.derecha, resultado)

    def mostrar_inorden(self) -> None:
        """Imprime en consola todos los productos ordenados por código."""
        productos = self.recorrido_inorden()
        if not productos:
            print("El arbol de inventario esta vacio.")
            return

        print("=== Catalogo ordenado por código (ABB Inorden) ===")
        for prod in productos:
            print(prod)