from app.models.pedido import Pedido
from app.models.status_pedido import StatusPedido

def test_criar_pedido():
    pedido = Pedido(1, "João")

    print(pedido.status)

    assert pedido.status == StatusPedido.PENDENTE
