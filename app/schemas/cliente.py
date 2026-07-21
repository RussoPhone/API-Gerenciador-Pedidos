from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    telefone: str 


class Cliente(ClienteCreate):
    id: int
