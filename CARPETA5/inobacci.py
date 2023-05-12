import random
def listapesada(tam,rango):
    lista=[]
    lista=[random.randrange(rango)for i in range(tam)]
    return lista
def num(m,l):
    z=0
    y=1
    x=0
    while i in range(1,10):
        i=int(input("escriba numero"))
        if i>1:
          break
    print("1",end="")
    for i in range(0,10):
        z=x+y
        print(f"{z}",end="")
        x=y
        y=z
    return i 
l1=listapesada(5,6)
print(l1)
l2=num(1,10)
print(l2)