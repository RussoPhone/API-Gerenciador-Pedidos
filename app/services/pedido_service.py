from app.schemas.pedido import Pedido

pedidos = []

def criar_pedido(pedido:Pedido):
    pedidos.append(pedido)
    return pedido
