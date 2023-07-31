def suma_numeros(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0: 
            suma += numero
    return suma

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = suma_numeros(numeros)
print("La suma de los números pares es:", resultado)