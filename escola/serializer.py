from django.db import models
from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno, Curso

class AlunoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

