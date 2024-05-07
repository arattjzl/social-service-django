from django.contrib import admin
from django.urls import path, include
from programa_academico.views import bienvenida
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api.views import ProgramaAcademicoViewSet

router = routers.DefaultRouter()
router.register(r'programas-api', ProgramaAcademicoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('unidades/', include('programa_academico.urls')),
    path('instituciones/', include('instituciones.urls')),
    path('programas/', include('programa_academico.urlsPrograma')),
    path('usuarios/', include('usuarios.urls')),
    path('', bienvenida, name='bienvenida'),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
