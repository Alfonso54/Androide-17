from urllib import response
from django.shortcuts import render

from blog.models import BlogsPost #Esto es para la aplicación y sección de blogs

from django.http import HttpResponse

#Prueba de función que muestra contenido estático = (NO MODIFICABLE DESDE LA PROPIA PÁGINA)

def saludo(request): 

    documento = """<html><body><h1>Buenas, este mensaje debería aparecer en la página principal.
    </h1></body></html>"""

    return HttpResponse(documento)

def homepagecolor(request):
    #Ingresar archivo css

    return render (request, 'homepageindex.html')

def blog_index(request):

    Blog_list = BlogsPost.objects.all() # Obtención de todos los datos

    return render (request, 'index.html', {'blog_list': Blog_list})
