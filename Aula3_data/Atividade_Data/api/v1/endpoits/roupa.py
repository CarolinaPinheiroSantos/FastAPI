from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.roupa_model import RoupaModel
from schemas.roupa_schema import RoupaSchema
from core.deps import get_session


router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=RoupaSchema)
async def post_roupa(roupa: RoupaSchema, db: AsyncSession = Depends(get_session)):
    nova_roupa = RoupaModel(**roupa.dict())
    db.add(nova_roupa)
    await db.commit()
    return nova_roupa

@router.get("/", response_model=List[RoupaSchema])
async def get_roupas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(RoupaModel))
        return result.scalars().all()

@router.get("/{roupa_id}", response_model=RoupaSchema)
async def get_roupa(roupa_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(RoupaModel).filter(RoupaModel.id == roupa_id))
        roupa = result.scalar_one_or_none()
        if roupa:
            return roupa
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Roupa não encontrada")

@router.put("/{roupa_id}", response_model=RoupaSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_roupa(roupa_id: int, roupa: RoupaSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(RoupaModel).filter(RoupaModel.id == roupa_id))
        roupa_up = result.scalar_one_or_none()
        if roupa_up:
            for key, value in roupa.dict().items():
                setattr(roupa_up, key, value)
            await session.commit()
            return roupa_up
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Roupa não encontrada")

@router.delete("/{roupa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_roupa(roupa_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        result = await session.execute(select(RoupaModel).filter(RoupaModel.id == roupa_id))
        roupa_del = result.scalar_one_or_none()
        if roupa_del:
            await session.delete(roupa_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Roupa não encontrada")
