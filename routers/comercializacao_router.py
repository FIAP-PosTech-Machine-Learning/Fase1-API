from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer
from schemas import ComercializacaoSchema
from typing import List
import services

api_token = HTTPBearer()

router = APIRouter(
    prefix="/comercializacao",
    tags=["Comercialização"],
)


@router.get("/", response_model=List[ComercializacaoSchema], status_code=200, )
async def get_comercializacao(token: str = Depends(api_token)):
    from services import authentication_service
    authentication_service.validate_access_token(token)
    return await services.get_comercializacao_data()


@router.get("/{id}", response_model=ComercializacaoSchema, status_code=200)
async def get_comercializacao_by_id(id: int, token: str = Depends(api_token)):
    from services import authentication_service
    authentication_service.validate_access_token(token)
    produto = await services.get_comercializacao_by_id(id)
    if produto:
        return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")
