from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBearer
from schemas import ImportacaoSchema
from typing import List
import services


api_token = HTTPBearer()

router = APIRouter(
    prefix="/importacao",
    tags=["Importação"],
)


@router.get("/", response_model=List[ImportacaoSchema], status_code=200)
async def get_importacao():
    return await services.get_importacao_data()


@router.get("/{id}", response_model=ImportacaoSchema, status_code=200)
async def get_importacao_by_id(id: int):
    produto = await services.get_importacao_by_id(id)
    if produto:
        return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")
