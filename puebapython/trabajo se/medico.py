class medico():
    medicocrea=[]
    def __init__(self):
        self.__nombre_m=input('escriba nombre: ')
        self.__especialidad=input('escriba su especialidad: ')
        self.__direccion_con =input('escriba direccion: ')
        self.__horario =input('escriba horario: ')
        medico.medicocrea.append(self)


    def getnombre(self):
        return self.__nombre_m

    def getespecialidad(self):
        return self.__especialidad

    def getdireccionc(self):
        return self.__direccion_con


    def gethorario(self):
        return self.__horario

    def getdatosmedico(self):
            return f"""Sus datos como medico son:

Nombre: {self.__nombre_m}
especialidad: {self.__especialidad}
direccion del consultorio: {self.__direccion_con}
horrio asignado: {self.__horario}
"""
    def getmedicolist (self):
        cont = 0
        for i in medico.medicocrea:
            cont = cont + 1
            print (f"{cont}. {i.getNombre()}")

    def  setnombre(self,nombre_m):
        self.__nombre_m = nombre_m

    def setespecialidad(self,especialidad):
        self.__especialidad = especialidad

    def setdireccion(self,direccion_con):
        self.__direccion_con = direccion_con

    def sethorario(self,horario):
        self.__horario = horario

    def setdatototal(self):
        print(f"""ingrese los datos requeridos:
            1 nombre{self.__nombre_m}
            2 especialidad{self.__especialidad}
            3 direccion{self.__direccion_con}
            4 horario{self.__horario}
            """)