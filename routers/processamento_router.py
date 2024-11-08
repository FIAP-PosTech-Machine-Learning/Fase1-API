from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer
from schemas import ProcessamentoSchema
from typing import List
import services


api_token = HTTPBearer()

router = APIRouter(
    prefix="/processamento",
    tags=["Processamento"],
)


@router.get("/", response_model=List[ProcessamentoSchema], status_code=200)
async def get_processamento_data(token: str = Depends(api_token)):
    from services import authentication_service
    authentication_service.validate_access_token(token)
    return await services.get_processamento_data()


@router.get("/{id}", response_model=ProcessamentoSchema, status_code=200)
async def get_processamento_by_id(id: int, token: str = Depends(api_token)):
    from services import authentication_service
    authentication_service.validate_access_token(token)
    produto = await services.get_processamento_by_id(id)
    if produto:
        return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")
