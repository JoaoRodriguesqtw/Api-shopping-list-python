import time
from fastapi import Request

async def registrar_log(request: Request, call_next):
    inicio = time.time()
    print(f"Requisição: {request.method} {request.url.path}")

    resposta = await call_next(request)
    fim = time.time()

    duracao_req = fim - inicio 

    print(f"Resposta: {resposta.status_code} Tempo: {(duracao_req):.3f}")
    return resposta