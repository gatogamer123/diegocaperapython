import random
tam=random.randint(10,30)
lista=[random.randrange(6)for i in range(tam)]
print(lista)
noaprobaron=[i for i in lista if i<3 ]
aprobaron=[i for i in lista if i>=3]
grupo1=[i for i in lista if i==1]
grupo2=[i for i in lista if i==2]
grupo3=[i for i in lista if i==3]
grupo4=[i for i in lista if i==4]
grupo5=[i for i in lista if i==5]
promediomalo=[i+i/tam for i in lista if i<3 ]
promediobueno=[i+i/tam for i in lista if i>=3 ]
nota=aprobaron[0:6]
print(aprobaron,'pasaron')
nota=noaprobaron[0:6]
print(noaprobaron,'perdieron el año')
notaorden1=grupo1[:2]
print(notaorden1)
notaorden2=grupo2[:2]
print(notaorden2)
notaorden3=grupo3[:2]
print(notaorden3)
notaorden4=grupo4[:2]
print(notaorden4)
notaorden5=grupo5[:2]        
print(notaorden5)
promedio=promediomalo[:6]
print(promedio,'pesimo promedio')
promedio1=promediobueno[:6]
print(promedio1,'buen promedio')
