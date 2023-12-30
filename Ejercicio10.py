print("Ejercicio hecho por Mireya García")
print("---Sensor infrarrojo de Arduino---")

while True:
    print("1. Prender el Smart TV ")
    print("2. Ver canales nacionales")
    print("3. Ingresar a Youtube")
    print("4. Ingresar a Disney+")
    print("5. Ingresar a Netflix")
    print("6. Acceder a Google")
    print("7. Jugar videojuegos")
    print("8. Vincular el teléfono con la Smart TV")
    print("9. Apagar el Smart TV")

    opciones = int(input("Seleccione una de las opciones proyectadas: "))
    
    while (opciones not in [1, 2, 3, 4, 5, 6, 7, 8, 9]):  
        print("LO SENTIMOS, LA OPCIÓN NO ES VÁLIDA")
        opciones = int(input("Seleccione una de las opciones proyectadas: "))

    if opciones == 1:
        print("Usted ha prendido el Smart TV", "\n", "***BIENVENIDOS A SMART TV***")
    elif opciones == 2:
        print("A continuación se presentarán los 3 canales nacionales:", "\n", "1. Teleamazonas", "\n","2. Ecuavisa", "\n", "3. Gamavision")
        eleccion = int(input("Seleccione una de las opciones proyectadas: "))
        print("***SE PROYECTA EL CANAL DE TELEVISIÓN SELECCIONADO***")
        while (eleccion not in [1, 2, 3]):  
            print("NO DISPONEMOS DE ESE CANAL")
            print("A continuación se presentarán los 3 canales nacionales:", "\n", "1. Teleamazonas", "\n","2. Ecuavisa", "\n", "3. Gamavision")
            eleccion = int(input("Seleccione una de las opciones proyectadas: "))
    elif opciones == 3:
        print("A solicitado el ingreso a Youtube", "\n", "***BIENVENIDOS A YOUTUBE***")
    elif opciones == 4:
        print("A solicitado ingresar a Disney+", "\n", "***BIENVENIDOS A DISNEY+***")
    elif opciones == 5:
        print("A solicitado el ingreso a Netflix", "\n", "***BIENVENIDOS A NETFLIX***", "\n","La mejor plataforma para visualizar series")
    elif opciones == 6:
        print("***GOOGLE***", "\n", "Busqueda___________")
    elif opciones == 7:
        juego = str(input("Ingrese el juego que desea proyectar en pantalla:"))
        print("***Bienvenidos a ", juego, "***")
    elif opciones == 8:
        print("Usted ha solicitado vincular su teléfono con el televisor, para ello: ")          
        celular = str(input("Ingrese el número de su dispositivo: "))
        print("Buscando...", "\n", "El dispositivo ", celular, " ha sido encontrado", "\n", "La televisión Smart TV se conectó con ",celular)
    elif opciones == 9:
        apagar = int(input("¿Está seguro de apagar el televisor? (digite 1=si o 2=no): "))
        while (apagar not in [1, 2]): 
            print("NO EXISTE ESA OPCIÓN")
            apagar = int(input("¿Está seguro de apagar el televisor? (digite 1=si o 2=no): "))
        if apagar == 1:
            break
    continuar = input("¿Desea realizar otra actividad? (digite 1=si o 2=no): ")
    if continuar != 1:
        print("Apagando el control remoto.")
        break


