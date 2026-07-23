import pytest 
from app.services import cliente_service 
from app.schemas.cliente import ClienteCreate 

@pytest.fixture(autouse=True)
def limpar_clientes(): 
    cliente_service._clientes.clear() 
    cliente_service._proximo_id = 1
    yield 

def test_criar_cliente():
    cliente = cliente_service.criar_cliente(
        ClienteCreate(nome="Maria", telefone="88999999999")
    )
    assert cliente.id == 1
    assert cliente.nome =="Maria" 

def test_listar_clientes():
    cliente_service.criar_cliente(ClienteCreate(nome="Maria", telefone="8999999999"))
    cliente_service.criar_cliente(ClienteCreate(nome="joao", telefone="8988888888"))
    assert len(cliente_service.listar_clientes()) == 2 

def test_buscar_cliente_inexistente():
    assert cliente_service.buscar_cliente_por_id(999) is None 
