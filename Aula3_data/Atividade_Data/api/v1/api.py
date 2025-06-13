from fastapi import APIRouter
from api.v1.endpoits import roupa, acessorio,templates

api_router = APIRouter()

api_router.include_router(roupa.router, prefix="/roupa", tags=["Roupa"])
api_router.include_router(acessorio.router, prefix="/acessorios", tags=["Acessórios"])

api_router.include_router(templates.router, prefix="/templates", tags=["Templates"])
