def multiplos():
  numero = int(input("Ingrese un número: "))
  limite = int(input("Ingrese el límite máximo: "))
  for i in range(1, limite + 1):
        resultado = numero * i
        print(resultado)
multiplos()