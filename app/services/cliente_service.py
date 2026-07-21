from app.schemas.cliente import Cliente, ClienteCreate

_clientes: list[Cliente] = []
_proximo_id = 1

def criar_cliente(dados: ClienteCreate) -> Cliente:
    global _proximo_id
    cliente = Cliente(id=_proximo_id, **dados.model_dump())
    _clientes.append(cliente)
    _proximo_id += 1
    return cliente

def listar_clientes() -> list[Cliente]:
    return _clientes

def buscar_cliente_por_id(cliente_id: int) -> Cliente | None:
    for cliente in _clientes:
        if cliente.id == cliente_id:
            return cliente
    return None
