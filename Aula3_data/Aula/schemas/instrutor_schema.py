from typing import Optional
from pydantic import BaseModel as SCBaseModel

class InstrutorSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    idade:int
    materia: str
    foto: str
    
    class Config:
        orm_mode = True