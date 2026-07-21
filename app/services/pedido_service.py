from app.schemas.pedido import Pedido, PedidoCreate
from app.schemas.enums import StatusPedido
from app.services import cliente_service

_pedidos: list[Pedido] = []
_proximo_id = 1

def criar_pedido(dados: PedidoCreate) -> Pedido:
    global _proximo_id
    cliente = cliente_service.buscar_cliente_por_id(dados.cliente_id)
    if cliente is None:
        raise ValueError(f"Cliente {dados.cliente_id} não encontrado")

    pedido = Pedido(id=_proximo_id, **dados.model_dump())
    _pedidos.append(pedido)
    _proximo_id += 1
    return pedido

def listar_pedidos() -> list[Pedido]:
    return _pedidos 

def buscar_por_id(pedido_id: int) -> Pedido | None:
    for pedido in _pedidos:
        if pedido.id == pedido_id:
            return pedido
    return None

def atualizar_status(pedido_id: int, novo_status: StatusPedido) -> Pedido | None:
    pedido = buscar_por_id(pedido_id)
    if pedido is None:
        return None
    pedido.status = novo_status
    return pedido

def cancelar_pedido(pedido_id: int) -> Pedido | None:
    return atualizar_status(pedido_id, StatusPedido.CANCELADO)
