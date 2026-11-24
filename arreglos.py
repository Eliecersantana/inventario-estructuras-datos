class Producto:
    def __init__(self, codigo: str, nombre: str, cantidad: int, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __repr__(self) -> str:
        return (
            f"[{self.codigo}] {self.nombre} | "
            f"Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"
        )


def ordenar_productos(productos: list[Producto], criterio: str = "nombre") -> list[Producto]:
    """Ordena una lista de productos alfabeticamente o por precio sin modificar la lista original."""
    if criterio == "nombre":
        return sorted(productos, key=lambda p: p.nombre.lower())
    elif criterio == "precio":
        return sorted(productos, key=lambda p: p.precio)
    else:
        raise ValueError("Criterio no valido. Usa 'nombre' o 'precio'.")


# --- Prueba de la parte 1 : Arreglos ---
inventario_inicial: list[Producto] = [
    Producto("P003", "Teclado Mecanico", 15, 45.00),
    Producto("P001", "Mouse Inalambrico", 30, 18.50),
    Producto("P002", "Monitor 24 Pulgadas", 8, 165.00),
    Producto("P004", "Audifonos USB", 20, 29.99),
]

print("=== Listado inicial (Arreglo) ===")
for prod in inventario_inicial:
    print(prod)

print("\n=== Ordenar alfabeticamente (por nombre) ===")
for prod in ordenar_productos(inventario_inicial, "nombre"):
    print(prod)

print("\n=== Ordenar por precio (menor a mayor) ===")
for prod in ordenar_productos(inventario_inicial, "precio"):
    print(prod)