from pydantic import BaseModel
from typing import List
from schemas import AnoValorSchema


class ComercializacaoSchema(BaseModel):
    id: int
    controle: str
    nome: str
    dados: List[AnoValorSchema]