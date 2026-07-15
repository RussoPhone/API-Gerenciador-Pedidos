from pydantic import BaseModel
from .enums import StatusPagamento, FormaPagamento

class Pagamento(BaseModel):
    id: int
    pedido_id: int
    forma_pagamento: FormaPagamento
    valor_pagamento: float
    status_pagamento: StatusPagamento = StatusPagamento.PENDENTE
