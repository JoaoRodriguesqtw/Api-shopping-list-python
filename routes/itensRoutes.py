from fastapi import APIRouter
from controllers import itensControllers
from data.itens import Item 


router = APIRouter()

# get find all
@router.get("/")
def listar_todos():
    return itensControllers.visualizar_lista()

@router.get("/{id}")
def listar_um(id: int):
    return itensControllers.visualizar_um(id)


@router.post("/")
def criar_item(item: Item):
    return itensControllers.criar_item(item)

@router.delete("/{id}")
def deletar_item(id: int):
    return itensControllers.deletar_item(id)


