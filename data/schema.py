from pydantic import BaseModel

class ItemNovo(BaseModel):
    nome: str
    quantidade: int


class ItemAtualizar(BaseModel):
    nome: str | None = None
    quantidade: int | None = None
    valor: float | None = None