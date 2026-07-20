from pydantic import BaseModel
from .enums import StatusPedido, StatusEntrega
from .item import Item

class Pedido(BaseModel):
    cliente_id: int
    itens: list[Item]
    observacoes: str | None = None
    status: StatusPedido = StatusPedido.RECEBIDO
    status_entrega: StatusEntrega = StatusEntrega.PENDENTE

    def finalizar(self):
        self.status = StatusPedido.FINALIZADO

    def cancelar(self):
        self.status = StatusPedido.CANCELADO
