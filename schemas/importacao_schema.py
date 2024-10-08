from pydantic import BaseModel
from typing import List
from schemas import AnoValorSchema


class ImportacaoSchema(BaseModel):
    id: int
    pais: str
    dados: List[AnoValorSchema]