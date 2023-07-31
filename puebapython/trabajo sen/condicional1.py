def contar_cifras(numero):
    return len(numero)

while True:
    try:
        numero = int(input("Ingrese un número entre 0 y 9999: "))

        if 0 <= numero <= 9999:
            cantidad = contar_cifras(numero)
            print(f"El número {numero} tiene {cantidad} cifras.")
        else:
            print("El número ingresado está fuera del rango permitido.")
            break 
    except ValueError:
        print("Por favor, ingrese solo números enteros válidos.")