from fastapi import APIRouter, HTTPException

from app.schemas.pedido import Pedido, PedidoCreate, AtualizarStatusRequest 
from app.services import pedido_service


router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@router.post("", response_model=Pedido)
def criar_pedido(dados: PedidoCreate):
    try:
        return pedido_service.criar_pedido(dados)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

@router.get("", response_model=list[Pedido])
def listar_pedidos():
    return pedido_service.listar_pedidos()

@router.get("/pedido_id}", response_model=Pedido)
def buscar_pedido(pedido_id: int):
    pedido= pedido_service.buscar_por_id(pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")
    return pedido

@router.patch("/{pedido_id}/status", response_model=Pedido)
def atualizar_status(pedido_id: int, corpo: AtualizarStatusRequest):
    pedido = pedido_service.atualizar_status(pedido_id, corpo.status)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido nao encontrado")
    return pedido

@router.post("/{pedido_id}/cancelar", response_model=Pedido)
def cancelar_pedido(pedido_id: int):
    pedido = pedido_service.cancelar_pedido(pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="pedido nao encontrado")
    return pedido 

                                         
