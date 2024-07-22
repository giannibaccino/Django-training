from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulos
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def busqueda_productos(request):
    
    return render(request, "busqueda_productos.html")

    
def buscar(request):
    
    if request.GET['prod']:
        
        # mensaje='Articulo buscado: %s' % request.GET['prod']
        producto=request.GET['prod']
        
        if len(producto)>20:
            
            mensaje='Texto de busqueda demasiado largo'
        
        else:
            
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            
            return render(request, "resultados_busqueda.html", {'articulos':articulos, 'query':producto})
        
    else:
        
        mensaje='No se busco nada pajin'
    
    return HttpResponse(mensaje)


def contacto(request):
    
    if request.method=='POST':
        
        subject=request.POST['asunto']
        
        message=request.POST['mensaje'] + ' ' + request.POST['email']
        
        origin_mail=settings.EMAIL_HOST_USER
        
        recipient_list=['giannix13@gmail.com']
        
        send_mail(
            subject, message, origin_mail, recipient_list
        )
        
        return render(request, "gracias.html")
    
    return render(request, "contacto.html")