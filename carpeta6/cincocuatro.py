import random
def lista1(tam,rango):
    mayor=0
    menor=0
    cuartil=[]
    cuartil=[random.randrange(rango)for i in range(tam)]
    return cuartil
def lista2(tam,rango):
    quintil=[]
    quintil=[random.randrange(rango)for i in range(tam)]
    return quintil
def suma(cuartil,quintil):
    resultado=cuartil,quintil
    return resultado
    
lf=lista1(10,10)
print(lf)
pl=suma(suma)
print(pl)
lg=lista2(10,10)
print(suma(100,500))