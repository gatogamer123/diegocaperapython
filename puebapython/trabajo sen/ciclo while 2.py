def num():
    mayor=int(input('escriba numero: '))
    con = 0
    while mayor < 10:
        mayor + 1
    if mayor > 10:
        con += 1
        print('no valido')
    else:
        print('no se hiso la operacion correctamente')
conclusion=num()
print(f'la suma es: ',conclusion)
     
