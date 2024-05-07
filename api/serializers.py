from programa_academico.models import ProgramaAcademico
from rest_framework import serializers

class ProgramaAcademicoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProgramaAcademico
        #fields = '__all__'
        fields = ['id', 'nombre', 'descripcion', 'unidad_academica']