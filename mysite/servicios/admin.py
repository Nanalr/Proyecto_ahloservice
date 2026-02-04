from django.contrib import admin
# registra los modelos creados
from .models import TipoServicio, Estado, Clientes, Servicios

# Register your models here.
admin.site.register(TipoServicio)
admin.site.register(Estado)
admin.site.register(Clientes)
admin.site.register(Servicios)
