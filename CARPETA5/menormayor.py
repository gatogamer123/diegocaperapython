import random
def listapesada(tam,rango):
    lista=[]
    lista=[random.randrange(rango)for i in range(tam)]
    return lista
def ordenar_numeros(numeros):
    numeros.sort()
    return numeros

def main():
    numeros = []
    cantidad = int(input("Ingrese la cantidad de números: "))

    for i in range(cantidad):
        numero = int(input("Ingrese un número: "))
        numeros.append(numero)

    numeros_ordenados = ordenar_numeros(numeros)
    print("Números ordenados de menor a mayor:", numeros_ordenados)

main()
