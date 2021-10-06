
from django.contrib import admin
from django.urls import path, include
from escola.serializer import MatriculaSerializers
from escola.views import AlunoViewSet, CursoViewSet, MatriculaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('Matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls), name='router'),
]
