from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Instituciones

# Create your views here.
class ListaInstituciones(ListView):
    model = Instituciones