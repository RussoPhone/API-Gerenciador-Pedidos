from enum import Enum

class StatusPedido(str, Enum):
    RECEBIDO = "recebido"
    PREPARANDO = "preparando"
    SAIU_PARA_ENTREGA = "saiu_para_entrega"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"
