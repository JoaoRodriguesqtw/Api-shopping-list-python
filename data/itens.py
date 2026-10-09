from pydantic import BaseModel


class Item(BaseModel):
    id: int | None = None
    nome: str
    quantidade: int = 1
    valor: int = 1


lista_itens = [
    Item(id=1, nome="Arroz", valor=10),
    Item(id=2, nome="Feijão", valor=10),
]