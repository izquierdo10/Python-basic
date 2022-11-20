from django.http import HttpResponse 
import datetime # libreria fecha,hora y segundos 

#-----------------------------------------------------------------------1
def saludo(request): #hola mundo
  return HttpResponse("hola django!")

#-----------------------------------------------------------------------2
def dinamico(request): # datos dinamicos 

    FechaActual=datetime.datetime.now()

    return HttpResponse(FechaActual)

#-----------------------------------------------------------------------3
def CalcularEdad(request,edad,agno): # parametros de URL
   
    x=datetime.datetime.now()
    AgnoActual=x.year
    periodo=agno-AgnoActual
    EdadFutura=edad+periodo
    
    texto="en el año %s tendras %s años" %(agno ,EdadFutura)

    return HttpResponse(texto)

#-----------------------------------------------------------------------4
from django.template import loader # poder cargar las plantillas
def saludo_plantilla(request):
    
    plantilla=loader.get_template('miplantilla.html')
     
    return HttpResponse(plantilla.render())

#-----------------------------------------------------------------------5
from django.shortcuts import render # cargar las plantillas de una forma mas optima
def segunda_plantilla(request):
    return render(request, 'plantilla2.html')

#-----------------------------------------------------------------------6
def tercera_plantilla(request): # poder llamar valores desde el html
    valor='cadena de texto desde el back'
    suma=1+2+3+4
    lista=[1,2,3,4,'diez','una list']

    return render(request, 'plantilla3.html', {
        'valor':valor,
        'suma':suma,
        'lista':lista
    })

#-----------------------------------------------------------------------7
def cuarta_plantilla(request): #bucles y condicionales
    lista2=["diccionario","atributo","metodo","indice_de_lista",1,2,3]
    lista3=[1,2,3,4,5,6,7,8,9,10]
    num= 45
    filtros="hola"

    return render(request, 'plantilla4.html' ,  {
        'lista2':lista2,
        'lista3':lista3,
        'num':num,
        'filtros':filtros} )

#-----------------------------------------------------------------------8
#plantillas incrustadas, ejemplo en barra.html y plantilla4.html
# {% include "barra.html" %} 
#o {% include "superior/barra.html" %} si nos creamos una subcarpeta en plantillas 

#-----------------------------------------------------------------------9
def herencia(request): # herencia ejemplos en plantillas  base.html y plantilla5.html

    Fecha=datetime.datetime.now()

    return render(request, 'plantilla5.html' , {'Fecha':Fecha})

#-----------------------------------------------------------------------10







