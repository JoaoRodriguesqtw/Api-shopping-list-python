from fastapi import FastAPI
from routes.itensRoutes import router as itens_router
from middlewares.log_middleware import registrar_log
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(registrar_log)


@app.get("/")
def raiz():
    return {"mensagem": "API funcionando!"}

app.include_router(itens_router, prefix="/shopping")