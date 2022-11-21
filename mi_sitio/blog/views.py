from django.shortcuts import render
from .models import PostTwo
from math import sqrt, pow, e, pi
from statistics import mean, pvariance
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'blog/index.html',{})

def post_list(request):
    consulta = PostTwo.objects.all()
    #se supone que consulta tiene los valores de la base de datos
    tupla = ()
    
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

        pagina = "<html><body><h1>Tu letra es:" + str(n[0][0]) +"</h1></body></html>"
        return HttpResponse(pagina)
                        
    return render(request, 'blog/algoritmo_knn.html',{'dist':lista,'vc':lista_knn})


def C_Bay_ing(request):

    consulta = PostTwo.objects.all()
    valores = obtenerValores(consulta)
    dc = calc_MedyVar(valores)

    resultados = []

    if request.method == 'POST':
        entrada = request.POST

        x1 = int(entrada['x1'])
        x2 = int(entrada['x2'])
        x3 = int(entrada['x3'])
        porc = 0

        for i in dc:
            x11 = calcularProbabilidad(x1,i[1],i[2])
            x22 = calcularProbabilidad(x2,i[3],i[4])
            x33 = calcularProbabilidad(x3,i[5],i[6])
            pro = len(valores[i[0]][0])/len(consulta)
            resultados.append((i[0],pro*x11*x22*x33))
        
        resultados.sort(key=lambda x:x[1])

        pagina = "<html><body><h1>Tu letra es:" + str(resultados[-1][0]) +"</h1></body></html>"
        return HttpResponse(pagina)

    
    return render(request,'blog/C_Bay_ing.html',{'data':dc,'resul':resultados})

def regresion_lineal(request):

    x1 = [1,2,2,3,4,4,5,6]
    y2 = [2,3,4,4,4,6,5,7]

    val = calc_Reg_Lin(x1,y2)
    print(val)

    return render(request,'blog/regresion_lineal.html',{})

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

def calc_MedyVar(datos):

    dc = []

    for i in datos.keys():
        mX1 = round(mean(datos[i][0]),2)
        vX1 = round(pvariance(datos[i][0]),2)
        mX2 = round(mean(datos[i][1]),2)
        vX2 = round(pvariance(datos[i][1]),2)
        mX3 = round(mean(datos[i][2]),2)
        vX3 = round(pvariance(datos[i][2]),2)
        dc.append([i,mX1,vX1,mX2,vX2,mX2,vX2])

    return dc

def calcularProbabilidad(muestra,media,varianza):
    if varianza == 0:
        return 0
    else:
        p = 1/sqrt(2*pi*varianza)
    exp = e*-(pow(muestra-media,2)/(2*varianza))
    return -(p*exp)

def calc_Reg_Lin(xi,yi):
    
    #Calculando sumatorias de los valores
    sx = sum(xi)
    sy = sum(yi)
    sx2 = 0
    for i in xi:
        sx2 += i**2
    sxy = 0
    for i in range(len(xi)):
        sxy += xi[i]*yi[i]
    
    #APlicando formulas para b1 y b0

    b1 = (sxy-(len(xi)*mean(xi)*mean(yi)))/(sx2-((1/len(yi))*(sx)**2))
    b0 = mean(yi) - (b1*mean(xi))

    return b0,b1