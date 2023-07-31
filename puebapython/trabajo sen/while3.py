def calcular(numero):
    factorial = 1
    contador = 1

    while contador <= numero:
        factorial *= contador
        contador += 1

    return factorial

numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    factorial = calcular(numero)
    print("El factorial de", numero, "es:", factorial)

        
