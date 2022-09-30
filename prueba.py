import string
from random import randint, choice


letra = choice(string.ascii_letters)

print(letra)

#archivo = open('datos.txt')


#for i in range(51):
    #archivo.write(str(randint(0,5000)) + ',' + str(choice(string.ascii_letters)) + ',' + str(randint(0,5000)) + ',' + str(randint(0,5000)) + '\n')

#print(len(archivo.readline()))


d1 = {'valor':(1,2,5,7)}
print(d1['valor'][2])