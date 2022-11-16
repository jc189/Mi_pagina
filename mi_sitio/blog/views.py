from django.shortcuts import render
from .models import PostTwo
from math import sqrt, pow, e, pi
from statistics import mean, pvariance

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

    consulta = PostTwo.objects.all()
    valores = obtenerValores(consulta)
    medias = calcularMedia(valores)
    varianzas = calcularVarianza(valores)

    datos = []

    for i in medias:
        t = (i,medias[i][0],varianzas[i][0],medias[i][1],varianzas[i][1],medias[i][2],varianzas[i][2])
        datos.append(t)

    if request.method == 'POST':
        entrada = request.POST

        x1 = int(entrada['x1'])
        x2 = int(entrada['x2'])
        x3 = int(entrada['x3'])

        resultados = []

        for i in datos:
            X11 = calcularProbabilidad(x1,i[1],i[2])
            x22 = calcularProbabilidad(x2,i[3],i[4])
            x33 = calcularProbabilidad(x3,i[5],i[6])

            resultados.append((i[0],((1/len(datos))*X11*x22*x33)))
        
        resultados.sort(key=lambda x:x[1])
        r = resultados[-1]


    return render(request,'blog/C_Bay_ing.html',{'data':datos,'Resultado':r[0]})



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

def calcularMedia(datos):

    media = {}

    for i in list(datos.keys()):
        media[i] = [round(mean(datos[i][0]),2),round(mean(datos[i][1]),2),round(mean(datos[i][2]),2)]
    return media

def calcularVarianza(datos):
    varianza = {}

    for i in list(datos.keys()):
        varianza[i] = [round(pvariance(datos[i][0]),2),round(pvariance(datos[i][1]),2),round(pvariance(datos[i][2]),2)]

    return varianza

def obtenerValores(consulta):
    valores = {}
    for i in consulta:
        if i.col2 not in valores:
            valores[i.col2] = [[i.col1],[i.col3],[i.col4]]
        else:
            valores[i.col2][0].append(i.col1)
            valores[i.col2][1].append(i.col3)
            valores[i.col2][2].append(i.col4)
    return valores

def calcularProbabilidad(muestra,media,varianza):
    if varianza == 0:
        return 0
    else:
        p = 1/sqrt(2*pi*varianza)
    exp = e*-(pow(muestra-media,2)/(2*varianza))
    return -(p*exp)