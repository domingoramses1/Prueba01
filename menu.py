
#Empresa.......: Instituto Tecnologico de León
#Meta..........: Calculo de áreas de Figuras Geometricas
#Colaborador...: Domingo Garcia Ornelas
#Rol...........: Programador
#Modulo........: Menu principal d
#Descripción...: Programa que realiza la navegabilidad para elegir la opcion de calculo del 
#..............: Area de la figura geometrica selecccionada
#Fecha.........: 16 de enero 2023.

def meta():
       print("Calcular áreas de Circulo, Triangulo y Rectangulo")

def isNum (cad):
   try: 
      int (cad)
      return True
   except ValueError:
      print ("Solo se aceptan numeros enteros\n")
      return False

global opcion
opcion=0
def menu():
   opcion=0
   while (opcion!=4):
      print(" 1 = Calcular el area del circulo.........")
      print(" ")
      print(" 2 = Calcular el área del triangulo.......")
      print(" ")
      print(" 3 = Calcular el area del rectangulo......")
      print(" ")
      print(" 4 = Salir................................")
      print(" ")   
      opcion = ""
      while not isNum(opcion):
         opcion = input("dame un numero [1 al 4]:")
      opcion = int(opcion)  
     
      if (opcion<1 and opcion>4):
          print ("....opcion no validad.....")
      elif  opcion==1:
              # Acirculo()
              print("Circulo")
      elif  opcion==2:
              # Atriangulo():
              print("Triangulo")
      elif  opcion==3:
              # Acuadrado
              print("rectangulo")
      else :
          print("Gracias")

meta()      
menu()
