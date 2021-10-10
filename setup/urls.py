
from django.contrib import admin
from django.urls import path, include
from escola.serializer import ListaAlunosMatriculadosSerializer, MatriculaSerializers
from escola.views import AlunoViewSet, CursoViewSet, ListaAlunosMatriculados, MatriculaViewSet, ListaMatriculasAluno
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('Matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls), name='router'),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]
