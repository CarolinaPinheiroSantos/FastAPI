from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    # Configuração Gerais da API
    
    API_V1_STR: str = "/api/v1"
    
    DB_URL: str = "mysql+asyncmy://root@127.0.0.1:3306/ets"
    
    DBBaseModel = declarative_base()
    
settings = Settings()
    
class Config:
    case_sensitive = False
    env_file = "env"
