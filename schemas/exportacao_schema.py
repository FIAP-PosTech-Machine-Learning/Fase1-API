from pydantic import BaseModel
from typing import List
from schemas.commom_schema import AnoValorSchema


class ExportacaoSchema(BaseModel):
    id: int
    pais: str
    dados: List[AnoValorSchema]