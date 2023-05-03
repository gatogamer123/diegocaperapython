num1=int(input('ingrese un numero '))
c1= num1 % 10
c2= int ((num1%100)/10)
c3=int ((num1%1000)/100)
c4= int((num1-(num1 % 1000))/1000)
for num1 in range (c1,c4,num1):
    print(str(c1)+str(c2)+str(c3)+str(c4))