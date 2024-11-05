from pydantic import BaseModel
from typing import Optional


class AnoValorSchema(BaseModel):
    ano: int
    valor: Optional[float] = None
