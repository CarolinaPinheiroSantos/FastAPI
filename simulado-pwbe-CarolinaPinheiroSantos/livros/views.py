from django.shortcuts import render
from .models import Livros
from . serializers import LivrosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

def listar_livros(request):
    livros = Livros.objects.all()
    return render(request, 'livros/livros.html', {'livros': livros})

@api_view(['GET', 'POST'])
def listar_adicionar_livros(request):
    if request.method == 'GET':
        livros = Livros.objects.all()
        serializer = LivrosSerializer(livros, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LivrosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    else:
        return Response({'Erro': 'Escolha requisição GET ou PUT'},status=status.HTTP_400_BAD_REQUEST)