from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Instituciones
from .forms import FormInstituciones

class ListaInstituciones(ListView):
    model = Instituciones
    # template_name = ''


class NuevaInstitucion(CreateView):
    model = Instituciones
    # fields = '__all__'
    form_class = FormInstituciones
    extra_context = {'accion':'Nueva'}
    success_url = reverse_lazy('lista_instituciones')
    
class EditarInstitucion(UpdateView):
    model = Instituciones
    # fields = '__all__'
    extra_context = {'accion':'Editar'}
    form_class = FormInstituciones
    success_url = reverse_lazy('lista_instituciones')
    
class EliminarInstitucion(DeleteView):
    model = Instituciones
    success_url = reverse_lazy('lista_instituciones')
    
    