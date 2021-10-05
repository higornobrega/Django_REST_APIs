from rest_framework import viewsets
from .models import Aluno, Curso
from .serializer import AlunoSerializers, CursoSerializers

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializers

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers