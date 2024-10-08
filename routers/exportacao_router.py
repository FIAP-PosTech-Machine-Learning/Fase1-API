from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBearer
from schemas import ExportacaoSchema
from typing import List
import services


api_token = HTTPBearer()

router = APIRouter(
    prefix="/exportacao",
    tags=["Exportação"],
)

@router.get("/", response_model=List[ExportacaoSchema], status_code=200)
async def get_exportacao():
    return await services.get_exportacao_data()

@router.get("/{id}", response_model=ExportacaoSchema, status_code=200)
async def get_exportacao_by_id(id: int):
    produto = await services.get_exportacao_by_id(id)
    if produto:
        return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")