from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_unidades_academicas, name='lista_unidades'),
    path('nueva/', views.nueva_unidad, name='nueva_unidad'),
    path('nueva-ajax/', views.nueva_unidad_ajax, name='nueva_unidad_ajax'),
    path('eliminar/<int:id>', views.eliminar_unidad, name='eliminar_unidad'),
    path('editar/<int:id>', views.editar_unidad, name='editar_unidad'),
]
