from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Aluno, Curso

def alunos(request):
    aluno = Aluno.objects.all()
    curso = Curso.objects.all()
    if request.method == 'GET':

        dados = {'id':aluno,
        'nome': curso,
        }
        
    return JsonResponse(dados)
        