from enum import Enum

class StatusPedido(Enum):
    PENDENTE = "pendente"
    PREPARANDO = "preparando"
    PRONTO = "pronto"
    FINALIZADO = "finalizado"
    CANCELADO = "cancelado"
