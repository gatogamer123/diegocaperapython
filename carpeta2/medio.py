import random
lista=[]
tam=random.randint(10,20)
i=0
while i< tam:
    num=random.randrange(100)
    print("valor numero:",i+1)
    val= float(input())
    lista.append(val)
    i+=1
prom=sum(lista)/len(lista)
print("el promedio es:",prom)



