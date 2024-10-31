from pydantic import BaseModel


class AnoValorSchema(BaseModel):
    ano: int
    valor: float
