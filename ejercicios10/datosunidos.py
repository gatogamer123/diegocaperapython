from ejercicio1 import *
import csv
datos=[]

with open('"C:\Users\SENA\Desktop\Saber_11__2019-2.csv"') as filadatos:
    filadatos=csv.reader(filadatos)
    for row in filadatos:
        objeto= (row[0],row[1],row[2],row[3])
        print(objeto.datosVer())
        datos.append(objeto)

for ap in datos:
    print(ap.getdocumento())