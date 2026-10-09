from data.itens import lista_itens
from fastapi import HTTPException
from data.itens import Item

#será a futura rota get
def visualizar_lista():
    return lista_itens

def visualizar_um(id: int):
    for item in lista_itens:
        if item.id == id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

def criar_item(item):
    ids = []
    for item_existente in lista_itens:
        ids.append(item_existente.id)
    novo_id = max(ids) + 1

    item.id = novo_id
    lista_itens.append(item)
    return item