from fastapi import FastAPI
from routes.itensRoutes import router as itens_router

app = FastAPI()


@app.get("/")
def raiz():
    return {"mensagem": "API funcionando!"}

app.include_router(itens_router, prefix="/shopping")