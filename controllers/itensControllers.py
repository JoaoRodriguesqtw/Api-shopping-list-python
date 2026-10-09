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
    novo_id = max(ids,default=0) + 1

    item.id = novo_id
    lista_itens.append(item)
    return item


def deletar_item(id: int):
    for item_d in lista_itens:
        if item_d.id == id:
            lista_itens.remove(item_d)
            return {"mensagem": "Item removido"}
    raise HTTPException(status_code=404, detail="item nao existe")

def editar_item(id: int, item):
    for item_existente in lista_itens:
        if item_existente.id == id:
            if item.nome is not None:
                item_existente.nome = item.nome
            if item.quantidade is not None:
                item_existente.quantidade = item.quantidade
            if item.valor is not None:
                item_existente.valor = item.valor
            return item_existente
    raise HTTPException(status_code=404, detail="item nao existe")
    


     
