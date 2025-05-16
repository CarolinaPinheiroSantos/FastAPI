from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.instrutores_model import InstrutorModel
from schemas.instrutor_schema import InstrutorSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=InstrutorSchema)
async def post_instrutor(instrutor: InstrutorSchema, db: AsyncSession=Depends(get_session)):
    novo_instrutor = InstrutorModel(nome=instrutor.nome, idade=instrutor.idade,
                                    materia=instrutor.materia, foto=instrutor.foto)
    db.add(novo_instrutor)
    await db.commit()
    return novo_instrutor

@router.get("/", response_model=List[InstrutorSchema])
async def get_instrutores(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InstrutorModel)
        result = await session.execute(query)
        
        instrutores: List[InstrutorModel] = result.scalars().all()
        
        return instrutores

@router.get("/{instrutor_id}", response_model=InstrutorSchema)
async def get_instrutor(instrutor_id: int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InstrutorModel).filter(InstrutorModel.id == instrutor_id)
        result = await session.execute(query)
        instrutor = result.scalar_one_or_none
        
        if instrutor:
            return instrutor
        else:
            raise HTTPException(detail="Instrutor nao existe",
                                status_code=status. HTTP_404_NOT_FOUND)
            
@router.put("/{instrutor_id}", response_model=InstrutorSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_instrutor(instrutor_id: int, instrutor: InstrutorSchema, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InstrutorModel).filter(InstrutorModel.id == instrutor_id)
        result = await session.execute(query)
        instrutor_up = result.scalar_one_or_none()
        
        if instrutor_up:
            instrutor_up.nome = instrutor.nome
            instrutor_up.idade = instrutor.idade
            instrutor_up.materia = instrutor.materia
            instrutor_up.foto = instrutor.foto
        else:
            raise HTTPException(detail="Instrutor não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete("/{instrutor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_instrutor(instrutor_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(InstrutorModel).filter(InstrutorModel.id == instrutor_id)
        result = await session.execute(query)
        instrutor_del = result.scalar_one_or_none()
        
        if instrutor_del:
            await session.delete()
            await session.commit()
            return Response(status_code=status.HTTP_404_NOT_FOUND)
        else:
            raise HTTPException(detail="Instrutor não encontrado", status_code=status.HTTP_404_NOT_FOUND)