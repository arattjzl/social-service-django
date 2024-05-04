from django.urls import path
from . import views

# /unidades/lista
urlpatterns = [
    path('lista/', views.ListaInstituciones.as_view(), name='lista_instituciones'),
    path('nueva/', views.NuevaInstitucion.as_view(), name='nueva_institucion'),
    # path('nueva-ajax/', views.nueva_unidad_ajax, name='nueva_unidad_ajax'),
    path('eliminar/<int:pk>', views.EliminarInstitucion.as_view(), name='eliminar_institucion'),
    path('editar/<int:pk>', views.EditarInstitucion.as_view(), name='editar_institucion'),
]
    