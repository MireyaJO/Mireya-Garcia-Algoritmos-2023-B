print("Ejercicio realizado por Mireya García")
acumuladorMes=0
while True:
    print("----MENÚ AHORROS DE JUAN ALVEAR----")
    print("1. Depositar dinero ", "\n", "2. Consultar dinero", "\n", "3. Salir del menú")
    seleccion=int(input("Porfavor coloque el numero que le corresponde a la actividad que desea realizar: "))
    while (seleccion!=1 and seleccion!=2 and seleccion!=3): 
        print ("Lo sentipos, no contamos con esa opción")
        seleccion=int(input("Porfavor coloque el numero que le corresponde a la actividad que desea realizar: "))
    if seleccion==1:
        print("----DEPÓSITO DE DINERO----")
        print("---MESES---","\n","1. Enero","\n","2. Febrero","\n","3. Marzo",
              "\n","4. Abril","\n","5. Mayo","\n","6. Junio","\n", "7. Julio","\n", "8. Agosto","\n", "9. Septiembre", "\n", 
              "10. Octubre","\n", "11. Noviembre","\n", "12. Diciembre" )
        print ("IMPORTANTE: Porfavor siga el orden de los meses")
        seleccion1 = int(input("¿En qué mes se encuentra realizando el depósito?: "))
        while (seleccion1<1 or seleccion1>12):
            print ("Solo coloque un rango del 1-12")
            seleccion1 = int(input("¿En qué mes se encuentra realizando el depósito?: "))
        deposito = float(input("Ingrese la cantidad que depositará (si ya colocaste la cantidad de dinero del último mes, no podrás ingresar más dinero): "))
        acumuladorMes = acumuladorMes + deposito
    elif seleccion==2:
        print ("---CONSULTA EL DINERO QUE HAS AHORRADO EN TODO EL AÑO---")
        print ("La cantidad de ahorros del año 2023 es de: ", acumuladorMes)
    elif seleccion==3:
        break



