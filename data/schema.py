from pydantic import BaseModel



class ItemAtualizar(BaseModel):
    nome: str | None = None
    quantidade: int | None = None
    valor: float | None = None