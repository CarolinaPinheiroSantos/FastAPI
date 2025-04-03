from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='livros'),
    path('api/livros/', views.listar_adicionar_livros),
]