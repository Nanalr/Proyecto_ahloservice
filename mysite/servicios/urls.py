from django.urls import path, include
#importa las vistas del archivo views.py
from .views import *
from rest_framework.routers import DefaultRouter
# Define las rutas de la aplicación servicios
router = DefaultRouter()

router.register(r'tipo_servicios', TipoServicioViewset, basename='tipo_servicios')
router.register(r'estados', EstadoViewset, basename='estados')
router.register(r'clientes', ClientesViewset, basename='clientes')
router.register(r'servicios', ServiciosViewset, basename='servicios')
urlpatterns = [
    path("", include(router.urls)),
]