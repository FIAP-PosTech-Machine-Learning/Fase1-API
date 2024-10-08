from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBearer
from schemas import ProducaoSchema
from typing import List
import services


api_token = HTTPBearer()

router = APIRouter(
    prefix="/producao",
    tags=["Produção"],
)

@router.get("/", response_model=List[ProducaoSchema], status_code=200)
async def get_producao_data():
    return await services.get_producao_data()

@router.get("/{id}", response_model=ProducaoSchema, status_code=200)
async def get_producao_by_id(id: int):
    produto = await services.get_producao_by_id(id)
    if produto:
        return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")