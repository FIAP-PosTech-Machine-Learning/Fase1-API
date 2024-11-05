from pydantic import BaseModel
from typing import List
from schemas.commom_schema import AnoValorSchema


class ProducaoSchema(BaseModel):
    id: int
    controle: str
    nome: str
    dados: List[AnoValorSchema]