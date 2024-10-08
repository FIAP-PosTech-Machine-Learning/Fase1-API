from pydantic import BaseModel


class AnoValorSchema(BaseModel):
    ano: str
    valor: int