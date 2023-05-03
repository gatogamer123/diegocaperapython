n=(int(input("escriba un numero")))
l=(int(input("escriba numero")))
i=1
suma=0
for i in range (n,l):
    if n%1==0:
        suma += n//i
    i+= 1
    print("el numero es perfecto")
else:
        print("el numero no es correcto")
