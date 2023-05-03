num1=int(input("ingrese un numero"))

if num1 < 0:

    for i in range(1,num1+1):

        print("")

        for j in range(1,i+1):

            print(j,end="")
    for i in range(num1-1,0-1):

        print("")
        for j in range(1,i+1):

         print(j,end="")

else:
    print("")