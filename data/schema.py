from pydantic import BaseModel

class ItemNovo(BaseModel):
    nome: str
    quantidade: int