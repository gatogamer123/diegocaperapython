class paciente:
    def __init__(self):
        self.__nombre = input('ingrese nombre:')
        self.__motivo = input('ingrese su motivo de la visita: ')

    def getnombre(self):
        return self.__nombre

    def getmotivo(self):
        return self.__motivo

    def getpaciente(self):
        return f""" ingrese los siguientes datos
        nombre:{self.__nombre}
        motivo de la visita:{self.__motivo}
        """


    def setnombre(self,nombre):
        self.__nombre=nombre

    def setmotivo(self,motivo):
        self.__motivo =motivo