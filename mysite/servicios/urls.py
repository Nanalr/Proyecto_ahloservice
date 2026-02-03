from django.urls import path

#importa las vistas del archivo views.py
from . import views

# Define las rutas de la aplicación servicios
urlpatterns = [
    path('', views.index, name='index'),
]