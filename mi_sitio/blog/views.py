from django.shortcuts import render
from .models import PostTwo

# Create your views here.

def post_list(request):
    consulta = PostTwo.objects.all()

    lista = []
    tupla = ()
    
    for i in consulta:
        lista.append(i.col3 + i.col4)
        tupla += i.col3 + i.col4,

    contenido = {'datos':consulta,'sumas':tupla}

    return render(request, 'blog/post_list.html', contenido)

def mostrar_datos(request):
    consulta = PostTwo.objects.all