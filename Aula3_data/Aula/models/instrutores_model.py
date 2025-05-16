from core.configs import settings
from sqlalchemy import Column, Integer, Boolean, Float, String

class InstrutorModel(settings.DBBaseModel):
    __tablename__ = "instrutor"
    
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(200))
    idade: int = Column(Integer())
    materia: str = Column(String(200))
    foto: str = Column(String(200))