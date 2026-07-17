from fastapi import APIRouter

from app.schemas.pedido import Pedido
from app.services import pedido_service


router = APIRouter()

pedidos = []

@router.post("/pedidos")
def criar_pedido(pedido: Pedido):
    return pedido_service.criar_pedido(pedido)
