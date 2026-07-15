from pydantic import BaseModel
from .enums import StatusEntrega

class Entrega(BaseModel):
    id: int
    cliente_id: int
    endereco: str
    status: StatusEntrega = StatusEntrega.PENDENTE
