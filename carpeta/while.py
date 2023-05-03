num1, num2= 0,0
resta=0
mayor=0
menor=9999999999999
result=0
while (num1-num2)==0:
    print("ingrese un nuevo numero")
    num1 = int(input('ingrese un numero'))
    num2 = int(input('ingrese un numero'))
    if (num1<num2 or num1 > num2):
        if num1 > mayor:
            mayor=num1
        if num2>num1:
            mayor=num2
            print(f'{mayor-num1}es el mayor')
        else:
            print(f'{mayor-num2}es el resultado')
            
