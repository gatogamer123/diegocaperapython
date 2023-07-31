
from medico import *
class Usuario:
    def __init__(self,nombre_m,especialidad,):
        medicocrea=[]
        self.__nombre_m=str(input('escriba nombre: '))
        self.__especialidad=str(input('escriba su especialidad: '))
        self.__direccion_con =str(input('escriba direccion: '))
        self.__horario =str(input('escriba horario: '))
        medico.medicocrea.append(self)

