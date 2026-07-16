from fastapi import APIRouter

router = APIRouter()

pedidos = []

@router.post("/pedidos")
def criar_pedido(pedido: dict):
    pedidos.append(pedido)

    return {
        "mensagem": "Pedido criado",
        "pedido": pedido
    }
