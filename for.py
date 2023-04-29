m=int(input("escriba un numero"))
j=int(input("escriba un numero"))
k=int(input("escriba numero para incrementar o decrementar"))
n=int(input("escriba el multiplo de un numero"))
for i in range (m,j,k):

    if i in range (m,j,k):
        if i % n == 0:
            print(f'{i}es multiplo de {n}')
        else:
            print(i)
    
    
    