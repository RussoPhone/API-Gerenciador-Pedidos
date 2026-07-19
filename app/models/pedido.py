from app.models.status_pedido import StatusPedido

class Pedido:
    def __init__(self, id, cliente):
        self.id = id
        self.cliente = cliente
        self.status = StatusPedido.PENDENTE
