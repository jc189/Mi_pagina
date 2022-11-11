from django.shortcuts import render
from .models import PostTwo
from math import sqrt, pow

# Create your views here.

def post_list(request):
    consulta = PostTwo.objects.all()
    #se supone que consulta tiene los valores de la base de datos
    tupla = ()
    print(consulta)
    
    #con este for lo fui recorriendo los datos para poder sacarlos y sumarlos
    for i in consulta:
        tupla += i.col1 + i.col3 + i.col4,

    #en si a esta tupla le estoy cocatenando los valores de la suma

    contenido = {'datos':consulta,'sumas':tupla}
    #ya aqui dentro del diccionario contenido le agregue la base de datos y aparte la tupla

    return render(request, 'blog/post_list.html', contenido)

def mostrar_datos(request):
    consulta = PostTwo.objects.all

def algoritmo_knn(request):

    consulta = PostTwo.objects.all()
    lista = []
    l = []
    d = []
    n = []
    lista_knn = {}

    if request.method == 'POST':
        entrada = request.POST
        lista = calcularDistancia(entrada,consulta)
        lista.sort(key=lambda x:x[1])
        for i in lista:
            n.append([i[0],i[1]])
        lista_knn = vecinosCercanos(int(entrada['k1']),lista)
        
        
                
    return render(request, 'blog/algoritmo_knn.html',{'dist':lista,'vc':lista_knn})

def index(request):
    return render(request, 'blog/index.html',{})

def C_Bay_ing(request):
    return render(request,'blog/C_Bay_ing.html',{})

def calcularDistancia(entrada,consulta):
    lista = []
    for i in consulta:
        val1 = pow((int(entrada['x1'])-i.col1),2)
        val2 = pow((int(entrada['y1'])-i.col3),2)
        val3 = pow((int(entrada['z1'])-i.col4),2)
        distancia = sqrt(val1 + val2 + val3)
        tupla = (i.col2,round(distancia,4))
        lista.append(tupla)

    return lista

def vecinosCercanos(k,lista):
    
    lista_k = lista[:k]
    lista_knn = {}
    lista_letras = []

    for i in lista_k:
        if i[0] in lista_letras:
            lista_knn[i[0]] += 1
        else:
            lista_letras.append(i[0])
            lista_knn[i[0]] = 1

    return lista_knn    

    