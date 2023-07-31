
def pregunta1():
    print("""colon descubrio america?
            1 si
            2 no
            """)
    no=input('elige la respuesta')
    if no =='1':
        return('es correcto')
    elif no == '2':
        return('la repuesta no es correcta')
    else:
        print('escribe algo valido')


def pregunta2():
    print("""la independencia de colombia fue en el año de 1810?
        1 si
        2 no """)
    si=input('elige la respuesta')
    if si == '1':
        return('correcto')
    elif si == '2':
        return('la respuesta no es correcta')
    else:
        print('escribe algo valido')
def pregunta3():
    print("""the doors fue una banda de rock americano? 
        1 si
        2no """)
    me=input('elige la respuesta')
    if me == '1':
        return('correcto')
    elif me == '2':
        return('la respuesta no es correcta')
    else:
        print('escribe algo valido')
print(pregunta1())
print(pregunta2())
print(pregunta3())

