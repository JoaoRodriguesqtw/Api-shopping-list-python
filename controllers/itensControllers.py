from data.itens import lista_itens
from fastapi import HTTPException

#será a futura rota get
def visualizar_lista():
    return lista_itens

def visualizar_um(id: int):
    for item in lista_itens:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")