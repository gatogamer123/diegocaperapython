from usuario import *
from paciente import *
from medico import *
while True:
   print("""ingrese lo que necesita
            1 registrar
            2 ya registrado
            """)

   no=input('que necesita')
   if no =='1':
         getnombre:input('escriba su nombre: ')
         getocupacion:input('escriba su ocupacion: ')
         gethora:input('escriba la hora: ')
         getdireccion:input('escriba la direccion:  ')
         print('usuario creado')
   if no == '2':
         print( """elija su tipo de usuario:
            1 medico
            2 paciente
            3 salir
            """)
         usuario=input('que cosa desea hacer ')
         if usuario == "1":
                  medico.medicocrea
                  print("""elija lo que desea hacer :
                           1 consultar
                           2 validar
                           3 actualizar
                           4 salir
                           """)


                  accion=input('que desea realizar: ')

                  if accion == "1":
                     print(medico.medicocrea)

                  if accion =="2":
                        print("""elija si aprueba o no:
                              1 aprobo
                              2 no aprobo
                              3 salir
                              """)
                        aprobacion=input('diga si aprobo o no')

                        if aprobacion =='1':
                           print('esta aprobado')
                        else:
                           print()
                        if aprobacion =='2':
                           print('lo sentimos no fue aprobado')
                        else:
                           print()

                  if accion =="3":
                        print(f"""Datos que puede actualizar
                           1. nombre
                           2  especialidad
                           3 direccion
                           4 horario
                           5 salir
                           """)
                        actual=input('que deseas actualizar')
                        if actual == "1":
                           nombrea = str(input("Ingrese su nombre: "))
                           medico.getnombre(nombrea)
                           print ("cambio realizado")

                        if actual =="2":
                           espe=input("ingrese la especialidad")
                           medico.getespecialidad(espe)
                           print('cambio realizado')

                        if actual =="3":
                           dir=input('ingrese su nueva direccion')
                           medico.getdireccionc(dir)
                           print('cambio realizado')

                        if  actual =="4":
                           hor=input('ingrese la nueva hora de ingreso')
                           medico.gethorario(hor)
                           print('cambio realizado')
                  if usuario == '2':
                     print("""elija que quiere hacer:
                           1 consultar
                           2 eliminar
                           3 actualizar
                           4 salir
                           """)
                     hacer=input('elija que quiere hacer')

                     if hacer =="1":
                        print(medico.medicocrea)

                     if hacer =="2":
                        print('elimine el dato')
                        paci = input('escriba lo que quiere eliminar')
                        for i in range(len(usuario)-1,-1,-1):
                              if usuario[i] == paci:
                                 paciente.pop(i)
                                 paciente.getnombre.pop(i)
                                 paciente.getmotivo.pop(i)
                        print('dato eliminado')

                     if hacer =='3':
                        medico.getdatosmedico
                        print(f"""Datos que puede actualizar
                           1. nombre
                           2 direccion
                           3 horario
                           4 salir
                           """)



