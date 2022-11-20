from django.http import HttpResponse
from django.shortcuts import render

from gestionPedidos.models import * # poder manipular las tablas de la bd
from .forms import FormularioCliente , Ventrega
# Create your views here.

#------------------------------------------------------------------1
def busquedaProd(request): # plantilla busquedaProd.html

    return render(request, 'busquedaProd.html')

def buscar(request): # enviar los datos de la plantilla busquedaProd.html al servidor y interactue con la BD 
    

     if request.GET["prd"]:
      
      producto=request.GET["prd"]
      
      art=Articulos.objects.filter(nombre__icontains=producto)
      return HttpResponse (art)
     
     else:
      mensaje="busqueda vacia "

     return HttpResponse (mensaje)
#------------------------------------------------------------------2
# metdo GET sirve para: enviar datos no sensible, datos pequeños,se pueden guardar los datos del metodo en la cahe y envia los datos en la URL = + rapido
def formulario(request):#formulario

   return render(request, "formulario2.html")

def resultadoFormulario(request):# proceso con los datos del formulario2

     if request.GET["prd"]: # verifique que si hay contenido en la entrada 
      
      producto=request.GET["prd"] # guardamos contenido en variable 
      
      art=Articulos.objects.filter(nombre__icontains=producto) # instruccion models para la BD: busqueme iconos similares segun lo ingresado en variable producto

      if art: # si en la varible art hay contenido muestrelo
       return render (request, "resultadoFormulario.html", {'art':art})
      else: # muestre el mensaje. se creo este mensaje ya que de no hacerlo enviria un query[]> por pantalla 
        mensaje="no esta en la base de datos" 
        
     else:
       mensaje="busqueda vacia" 

     return render (request, "resultadoFormulario.html", {'mensaje':mensaje}) # por si se hace una busqueda sin txt o int

#------------------------------------------------------------------3
# metdo POST sirve para: enviar datos sensibles, datos grandes,archivos(binarios,imagenes...) y envia los datos en el cuerpo = + seguro
def formulario3(request):

   return render(request, "formulario3.html")

def resultadoFormulario3(request):# con metodo POST ahi que indicar que se usara este.  (request.method=="POST")

     if request.method=="POST" and request.POST["prd"]: # si es metodo POST y a su vez hay contenido en la entrada 
      producto=request.POST["prd"]  

      if len(producto)>20: # limite de caracteres a buscar //sirve para mejor rendimiento o evitar ataques DDoS//
            mensaje="texto de busqueda demasiado largo"
            return render (request, "resultadoFormulario3.html", {'mensaje':mensaje})
      else: 
       art=Articulos.objects.filter(nombre__icontains=producto) 

      if art: 
       return render (request, "resultadoFormulario3.html", {'art':art})
      else: 
        mensaje="no esta en la base de datos" 
        
     else:
       mensaje="busqueda vacia" 

     return render (request, "resultadoFormulario3.html", {'mensaje':mensaje})

#------------------------------------------------------------------4 
# con archivo forms.py 
def archivoform(request):
   if request.GET: # si se esta enviando datos entonces:
     
     Clientes.objects.create(
     nombre=request.GET['nombre'],
     direccion=request.GET['direccion'],
     email=request.GET['email'],
     celular=request.GET['celular'])# se envian los datos del GET  a la BD tabla clientes

     return render(request, "formulario4.html", {'form': FormularioCliente}) # retorna el mismo formulario
   else:
    return render(request, "formulario4.html", {'form': FormularioCliente}) # si aun no a enviado un GET entre al formulario

#------------------------------------------------------------------5
def verificarentrega(request):
   if request.GET:

    consulta=Pedidos.objects.filter(N_Pedido=request.GET['N_pedido']) # si el numero de pedido GET es igual a alguno de la BD, muestre si ya se entrego. 

    if consulta:
     return render(request, "entregas.html", {'form2':Ventrega,'consulta':consulta})
    else:
     Nodato="el numero de pedido no existe"

     return render(request, "entregas.html", {'form2':Ventrega,'Nodato':Nodato})

   else:
    return render(request, "entregas.html", {'form2': Ventrega})



  

