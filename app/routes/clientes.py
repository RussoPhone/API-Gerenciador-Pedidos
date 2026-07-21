from fastapi import APIRouter, HTTPException

from app.schemas.cliente import Cliente, ClienteCreate
from app.services import cliente_service

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.post("", response_model=Cliente)
def criar_cliente(dados: ClienteCreate):
    return cliente_service.criar_cliente(dados)

@router.get("", response_model=list[Cliente])
def buscar_cliente(cliente_id: int):
    cliente = cliente_service.buscar_cliente_por_id(cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente


