from core.configs import settings
from core.database import engine
from models import all_model

async def create_table() -> None:
    print("Criando tabelas no banco")
    
    async with engine.begin() as conn:
        
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
        
    print("sucesso")
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(create_table())