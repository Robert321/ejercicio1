from django.shortcuts import render
# Create your views here.
#1
#1.a
lista = [2,20,3,4,5,6,7,8,9,19,11,12,13,14,17,16,15,18,10,1]
i=0
j=0
aux=0
tam=len(lista)
while i<tam-1:
	j=0
	while j<tam-1:
		if lista[j+1]<lista[j]:
			aux=lista[j+1]
			lista[j+1]=lista[j]
			lista[j]=aux
		j=j+1
	i=i+1
else:
	print "1.a)",lista
#1.b
lista = [2,20,3,4,5,6,7,8,9,19,11,12,13,14,17,16,15,18,10,1]
i=0
j=0
aux=0
tam=len(lista)
while i<tam-1:
	j=0
	while j<tam-1:
		if lista[j]<lista[j+1]:
			aux=lista[j+1]
			lista[j+1]=lista[j]
			lista[j]=aux
		j=j+1
	i=i+1
else:
	print "1.b)",lista


#1.c
def suma(x, y):
    s= int(x) + int(y)
    print "1.c)",+s

a = "20"
b = "10"
suma(a, b)

#1.d
def suma2(x,y):
	s=str(x)+str(y)
	print "1.d)",s

a=20
b=10
suma2(a,b)

#1.e
def suma3(x,y):
	s=float(int(x)+float(y))
	print "1.e)",s

a=int(20)
b=float(0.5)
suma3(a,b)