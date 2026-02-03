from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola, bienvenido a la página de servicios.")