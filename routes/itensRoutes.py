from fastapi import APIRouter
from controllers import itensControllers


router = APIRouter()

# get find all
@router.get("/")
def listar_todos():
    return itensControllers.visualizar_lista()

@router.get("/{id}")
def listar_um(id: int):
    return itensControllers.visualizar_um(id)


# @router.post("/")
#def criar():