import random
def lista1(tam,rango):
    cuartil=[]
    cuartil=[random.randrange(rango)for i in range(tam)] 
    return cuartil
def lista2(tam,rango):
    quintil=[]
    quintil=[random.randrange(rango)for i in range(tam)]
    return quintil
def suma(tam,rango):
    suma=[]
    mayor=500
    menor=100
    suma=[random.randrange(rango)for i in range(tam)]
    cuartil=sum,1
    return suma
    
lf=lista1(200,2500)
print(lf)
pl=suma(100,500)
print(pl)
lg=lista2(10,10)
print(lg)