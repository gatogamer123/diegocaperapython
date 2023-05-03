num1=1
while num1 <=1000:
   cont=1
   x=0
   while cont <= num1:
      if num1 % cont ==0:
        x=x+1
        cont = cont +1
if x ==2:
         print("son numeros primos",num1)