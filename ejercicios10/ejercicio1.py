class datos_icfest:
    def __init__(self,tipo_documento,nacionalidad,genero,jornada):
        self.__tipo_documento = tipo_documento
        self.__nacionalidad = nacionalidad
        self.__genero = genero
        self.__jornada = jornada

    def datosVer (self):
        return({self.__tipo_documento},{self.__nacionalidad},{self.__genero},{self.__jornada})

    def getdocumento(self):
        return self.__tipo_documento





