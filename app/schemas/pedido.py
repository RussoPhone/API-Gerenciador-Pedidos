from pydantic import BaseModel, Field
from datetime import datetime 
from .enums import StatusPedido, StatusEntrega
from .item import Item

class PedidoCreate(BaseModel):
    cliente_id:int
    itens: list[Item]
    observacoes: str | None = None

class Pedido(PedidoCreate):
    id: int
    status: StatusPedido = StatusPedido.RECEBIDO
    status_entrega: StatusEntrega = StatusEntrega.PENDENTE
    data_criacao: datetime = Field(default_factory=datetime.now)

class AtualizarStatusRequest(BaseModel):
    status: StatusPedido

