from enum import Enum

class StatusPedido(str, Enum):
    RECEBIDO = "recebido"
    PREPARANDO = "preparando"
    SAIU_PARA_ENTREGA = "saiu_para_entrega"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"

class StatusEntrega(str, Enum):
    PENDENTE = "pendente"
    A_CAMINHO = "a_caminho"
    ENTREGUE = "entregue"

class StatusPagamento(str, Enum):
    PENDENTE = "pendente"
    CONCLUIDO = "concluido"

class FormaPagamento(str, Enum):
    PIX = "pix"
    CARTAO = "cartao"
    DINHEIRO = "dinheiro"
