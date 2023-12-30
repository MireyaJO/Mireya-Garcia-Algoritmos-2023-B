#Replica 02
#Automotores “Chevrolet” desea colocar sensores para detectar fugas de gas y 
#que mande alertas respectivas. En ese sentido, se desea programar un sensor 
#de gas para un Arduino, la tarea consiste en que el sensor obtenga la información 
#de 3 talleres mecánicos y que contabilice si existe fuga de gas. En el que, 
#si el número de talleres es mayor a 1 se debe mandar un correo al usuario 
#alertando de la novedad, caso contrario no se realizará ninguna acción.
print ("Replicado por Mireya García")
print("----- SENSOR DE FUGA -----")
print("Menú de opciones")
print("1.- Verificar el estado de los talleres")
print("2.- Salir")
opcion = int(input("Ingrese la opción: "))
while opcion != 1 and opcion != 2:
  print("Error, verifique las opciones")
  print("1.- Verificar el estado de los talleres")
  print("2.- Salir")
  opcion = int(input("Ingrese la opción: "))
while (opcion != 2):
  print("Ejecutar caso 1")
  contador_fugas = 0
  num_talleres = 1
  while num_talleres <= 3:
    print("Existe fuga en el taller ", num_talleres)
    estado = input("Ingrese si o no: ")
    if estado == "si":
      contador_fugas += 1
    num_talleres += 1
  if contador_fugas >= 1:
    print("Enviar correo")
    print("1.- Verificar el estado de los talleres")
    print("2.- Salir")
  opcion = int(input("Ingrese la opción: "))

  while opcion != 1 and opcion != 2:
    print("Error, verifique las opciones")
    print("1.- Verificar el estado de los talleres")
    print("2.- Salir")
    opcion = int(input("Ingrese la opción: "))
print("Muchas gracias por utilizar nuestro sistema")

