def valor_medio(a, b, c):
    if (a - b) * (a - c) < 0:
        return a
    elif (b - a) * (b - c) < 0:
        return b
    return c

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    valor_medio = valor_medio(num1, num2, num3)
    print(f"El valor del medio es: {valor_medio}")

except ValueError:
    print("Por favor, ingrese solo números válidos.")