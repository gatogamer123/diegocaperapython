import random
suma=0
mayor=1000000
lista=[]
tam=int(random.randint(10,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)
    suma+=num
print(lista)
print(f'la suma es {suma}')