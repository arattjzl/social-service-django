from rest_framework import viewsets
from programa_academico.models import ProgramaAcademico
from .serializers import ProgramaAcademicoSerializer

# Create your views here.

class ProgramaAcademicoViewSet(viewsets.ModelViewSet):
    queryset = ProgramaAcademico.objects.all()
    serializer_class = ProgramaAcademicoSerializer