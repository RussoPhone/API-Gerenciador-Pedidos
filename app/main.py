from fastapi import FastAPI
from app.routes.pedidos import router as pedidos_router

app = FastAPI()

app.include_router(pedidos_router)

@app.get("/")
def home():
    return{
        "mensagem": "Gerenciador funcionando"
    }
