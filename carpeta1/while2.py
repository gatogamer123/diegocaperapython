n=int(input("escriba un numero"))
i=2
suma=0
while i <= n:
    if n % i ==0:
        suma +=n//i
    i += 1

if suma ==n:
    print("el numero es perfecto")
else:
    print("el numero no es perfecto")
