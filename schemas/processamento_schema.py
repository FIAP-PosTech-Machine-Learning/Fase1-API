from pydantic import BaseModel
from typing import List
from schemas import AnoValorSchema


class ProcessamentoSchema(BaseModel):
    id: int
    controle: str
    cultivar: str
    dados: List[AnoValorSchema]
