from fastapi import FastAPI, Request
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.roupa_model import RoupaModel
from models.acessorio_model import AcessorioModel
from core.deps import get_session


router = APIRouter()
templates = Jinja2Templates(directory="templates") 

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, db: AsyncSession = Depends(get_session)):
    result_roupas = await db.execute(select(RoupaModel))
    roupas = result_roupas.scalars().all()

    result_acessorios = await db.execute(select(AcessorioModel))
    acessorios = result_acessorios.scalars().all()

    return templates.TemplateResponse("home.html", {
        "request": request,
        "roupas": roupas,
        "acessorios": acessorios
    })
