from fastapi import FastAPI 

from app.routes.clientes import router as clientes_router 
from app.routes.pedidos import router as pedidos_router 

app = FastAPI(title="Gerenciador de Pedidos")

app.include_router(clientes_router) 
app.include_router(pedidos_router) 

@app.get("/")
def home():
    return {"mensagem": "Gerenciador funcionando"}


