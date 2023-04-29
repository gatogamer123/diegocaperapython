#imprimir un numero desde 1 a n pero cadabes que encuentre un mutiplo de 7
n=int(input('ingrese numero'))
i=1
#se hace un while para numerar y hacer que muestre los multiplos de 7
while i<n:
    if i%7==0:
        print(f'{i}es multiplo de 7:')
    else:
        print(i)
        i=+1


