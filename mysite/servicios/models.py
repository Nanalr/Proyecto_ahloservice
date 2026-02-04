from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoServicio(models.Model):
    nombre = models.CharField(max_length=200)


class Estado(models.Model):
    nombre = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.nombre
class Clientes(models.Model):
    nombre = models.CharField(max_length=200)
    documento = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    correo = models.EmailField(max_length=200, null=True, blank=True)

    # def __str__(self):
    #     return self.nombre
class Servicios(models.Model):
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pago = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, null=True)
    usuario_asignado = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     return f'Servicio {self.id} - {self.descripcion}'