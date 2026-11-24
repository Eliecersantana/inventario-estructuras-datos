from collections import deque
from arreglos import Producto


class ColaPedidos:
    """Gestiona pedidos de clientes en orden de llegada (FIFO)."""

    def __init__(self):
        self.pedidos: deque[dict] = deque()

    def encolar_pedido(self, cliente: str, producto: Producto, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad del pedido debe ser mayor que cero.")

        pedido = {
            "cliente": cliente.strip(),
            "producto": producto,
            "cantidad": cantidad,
        }
        self.pedidos.append(pedido)
        print(f"Pedido agregado a la cola: {pedido['cliente']} -> {cantidad} x {producto.nombre}")

    def atender_pedido(self) -> dict | None:
        if not self.pedidos:
            print("No hay pedidos pendientes en la cola.")
            return None

        pedido = self.pedidos.popleft()
        print(f"Atendiendo pedido de {pedido['cliente']}: {pedido['cantidad']} x {pedido['producto'].nombre}")
        return pedido

    def ver_siguiente(self) -> dict | None:
        if not self.pedidos:
            print("La cola esta vacia.")
            return None
        return self.pedidos[0]

    def mostrar_cola(self) -> None:
        if not self.pedidos:
            print("No hay pedidos en espera.")
            return

        print("=== Cola de pedidos (orden de llegada) ===")
        for idx, pedido in enumerate(self.pedidos, start=1):
            prod = pedido["producto"]
            print(f"{idx}. Cliente: {pedido['cliente']} | {pedido['cantidad']} x {prod.nombre} (${prod.precio:.2f})")