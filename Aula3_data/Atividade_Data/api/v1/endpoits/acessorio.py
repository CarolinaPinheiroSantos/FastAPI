from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.acessorio_model import AcessorioModel
from schemas.acessorio_schema import AcessorioSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AcessorioSchema)
async def post_acessorio(acessorio: AcessorioSchema, db: AsyncSession = Depends(get_session)):
    novo_acessorio = AcessorioModel(**acessorio.dict())
    db.add(novo_acessorio)
    await db.commit()
    return novo_acessorio

@router.get("/", response_model=List[AcessorioSchema])
async def get_acessorios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(AcessorioModel))
        return result.scalars().all()

@router.get("/{acessorio_id}", response_model=AcessorioSchema)
async def get_acessorio(acessorio_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(AcessorioModel).filter(AcessorioModel.id == acessorio_id))
        acessorio = result.scalar_one_or_none()
        if acessorio:
            return acessorio
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Acessório não encontrado")

@router.put("/{acessorio_id}", response_model=AcessorioSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_acessorio(acessorio_id: int, acessorio: AcessorioSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(AcessorioModel).filter(AcessorioModel.id == acessorio_id))
        acessorio_up = result.scalar_one_or_none()
        if acessorio_up:
            for key, value in acessorio.dict().items():
                setattr(acessorio_up, key, value)
            await session.commit()
            return acessorio_up
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Acessório não encontrado")

@router.delete("/{acessorio_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_acessorio(acessorio_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(AcessorioModel).filter(AcessorioModel.id == acessorio_id))
        acessorio_del = result.scalar_one_or_none()
        if acessorio_del:
            await session.delete(acessorio_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Acessório não encontrado")
