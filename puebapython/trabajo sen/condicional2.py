def num():
    a=int(input('escriba un numero: '))
    b=int(input('escriba un numero: '))
    c=int(input('escriba un numero: '))
    if (a == b==c):
        print('son iguales')
    elif (a == b or a == c or b == c):
        print('dos numeros son iguales')
    elif (a!=b !=c):
        print('todos los numeros son distintos')
    else:
        print('ninguno es valido')
print(num())