from core.configs import settings
from sqlalchemy import Column, Integer, String, Enum as SQLEnum
import enum

class TipoPeca(str, enum.Enum):
    camisa = "camisa"
    calca = "calca"
    short = "shorts"
    regata = "regata"
    blusa_frio = "blusa de frio"

class RoupaModel(settings.DBBaseModel):
    __tablename__ = "roupa"
    
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    peca = Column(SQLEnum(TipoPeca), nullable=False)
    valor: int = Column(Integer())
    cor: str = Column(String(100))
    tamanho: str = Column(String(6))
    foto: str = Column(String(200)) 