from pydantic import BaseModel


class Item(BaseModel):
    id: int | None = None
    nome: str
    quantidade: int = 1
    valor: float = 1


lista_itens = [
    Item(id=1, nome="Arroz",quantidade=1, valor=10),
    Item(id=2, nome="Feijão",quantidade=1 ,valor=10),
]