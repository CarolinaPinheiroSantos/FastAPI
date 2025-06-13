from core.configs import settings
from sqlalchemy import Column, Integer, String,ForeignKey, Enum as SQLEnum
import enum

class Tipo(str, enum.Enum):
    bolsa = "bolsa"
    colar = "colar"
    brinco = "brinco"
    anel = "anel"

class AcessorioModel(settings.DBBaseModel):
    __tablename__ = "acessorio"
    
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    tipo = Column(SQLEnum(Tipo), nullable=False)
    valor: int = Column(Integer())
    cor: str = Column(String(100))
    foto: str = Column(String(200)) 
    roupa_id: int = Column(Integer, ForeignKey("roupa.id", ondelete="CASCADE"))