from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_programas_academicas, name='lista_programas'),
    path('nuevo/', views.nuevo_programa, name='nuevo_programa'),
    path('eliminar/<int:id>', views.eliminar_programa, name='eliminar_programa'),
    path('editar/<int:id>', views.editar_programa, name='editar_programa'),
]
