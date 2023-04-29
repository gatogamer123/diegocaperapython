x,y= 3,5
cont=1
while not(x%y==0 or y%x==0):
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))

print(f'{x} y {y} son factores')