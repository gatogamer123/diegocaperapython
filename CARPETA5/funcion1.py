import random
def listapesada(tam,rango):
    mayor=5
    menor=0
    lista=[]
    lista=[random.randrange(rango)for i in range(tam)]
    return lista

def ordenar_numeros(numeros):
    numeros.sort(reverse=True)
    return numeros

def main():
    numeros = []
    cantidad = 5

    for i in range(cantidad):
        numero = int(input("Ingrese un número: "))
        numeros.append(numero)

    numeros_ordenados = ordenar_numeros(numeros)
    print("Números ordenados de mayor a menor:", numeros_ordenados)

main()

def ordenar_numeros(numeros):
    numeros.sort(reverse=True)
    return numeros

def main():
    numeros = []
    cantidad = 5

    for i in range(cantidad):
        numero = int(input("Ingrese un número: "))
        numeros.append(numero)

    numeros_ordenados = ordenar_numeros(numeros)
    print("Números ordenados de menor a mayor:", numeros_ordenados)

main()


list1=listapesada(6,5)
print(list1)
print((list1))

    