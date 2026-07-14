from pydantic import BaseModel
from .enums import StatusPedido

class Pedido(BaseModel):
    cliente: str
    telefone: str
    endereco: str
    itens: list[str]
    observacoes: str | None = None
    status: StatusPedido = StatusPedido.RECEBIDO
