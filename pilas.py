from collections import deque

 
class PilaOperaciones:
    """Registra las últimas operaciones sobre el inventario y permite deshacer la más reciente."""

    def __init__(self, limite: int = 10):
        self.limite = limite
        self.historial: deque[dict] = deque(maxlen=limite)

    def registrar_operacion(self, tipo: str, detalle: str, datos_previos=None) -> None:
        tipo_limpio = tipo.lower().strip()
        if tipo_limpio not in {"agregar", "eliminar", "editar"}:
            raise ValueError("Tipo de operacion no valido. Usa 'agregar', 'eliminar' o 'editar'.")

        self.historial.append(
            {
                "tipo": tipo_limpio,
                "detalle": detalle,
                "datos_previos": datos_previos,
            }
        )

    def deshacer_ultima_operacion(self) -> dict | None:
        if not self.historial:
            print("No hay operaciones para deshacer.")
            return None

        ultima = self.historial.pop()
        print(f"Deshaciendo [{ultima['tipo']}]: {ultima['detalle']}")
        return ultima

    def mostrar_historial(self) -> None:
        if not self.historial:
            print("El historial de operaciones esta vacio.")
            return

        print(f"=== Historial (ultimas {len(self.historial)}/{self.limite}) ===")
        for idx, op in enumerate(reversed(self.historial), start=1):
            print(f"{idx}. [{op['tipo'].upper()}] {op['detalle']}")