from typing import Optional
from pydantic import BaseModel as SCBaseModel

class RoupaSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    peca: str
    valor: int
    cor: str
    tamanho: str
    foto: str
    
    class Config:
        from_attributes = True