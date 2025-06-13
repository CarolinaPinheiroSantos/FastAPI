from typing import Optional
from pydantic import BaseModel as SCBaseModel

class AcessorioSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    tipo: str
    valor: int
    cor: str
    roupa_id: int
    foto: str

    class Config:
        from_attributes = True