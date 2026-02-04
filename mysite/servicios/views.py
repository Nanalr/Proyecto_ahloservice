
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class TipoServicioViewset(ModelViewSet):
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer
class EstadoViewset(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
class ClientesViewset(ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
class ServiciosViewset(ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer

