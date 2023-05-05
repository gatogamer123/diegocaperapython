import random
dato=[10,20]
conteo={}
tam=random.randint(10,20)
for numero in dato:
    num=random.randrange(100)
    clave=str(numero)
    if not clave in conteo:
        conteo[clave] = 1
    else:
        conteo[clave] += 1
mayor=0
print(conteo)
for numero in conteo:
    if conteo[numero] > mayor:
        repetido = int(numero)
        mayor = conteo[numero]
print(f"{mayor}se repite")
