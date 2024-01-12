print ("García Mireya")
print ("----INICIO DE SECION----")
correo= str(input("Ingrese su correo: "))
contraseña=str(input("Ingrese su contraseña: "))
acceso1="tosh@gmail.com"
acceso2="Secret*"
contadorDescuentos=0
acumuladorPrecio=0
precioProducto=0
while correo!=acceso1 and contraseña!=acceso2:
    print("-------ERROR-------")
    correo= str(input("Ingrese su correo: "))
    contraseña=str(input("Ingrese su contraseña: "))
if correo==acceso1 and contraseña==acceso2:
    while True:
        print("----Bienvenidos a AMAZON----")
        print("-----Menu de opciones------")
        print("1. Ingresar productos al carrito de compras")
        print("2. Facturar")
        print("3. Salir")
        seleccion=int(input("Por favor ingrese el numero que le corresponde a la opcion que desee realizar: "))
        while (seleccion<1 or seleccion>3):
            print("LO SENTIMOS NO CONTAMOS CON ESA OPCION, solo digite los numeros que están en pantalla")
            seleccion=int(input("Por favor ingrese el numero que le corresponde a la opcion que desee realizar: "))
        if (seleccion==1):
           while True:
                productos=int (input("Ingrese el número de productos a registrar: "))
                for i in range (0,productos,1):
                    descuento=int(input("¿El producto tiene descuentos? (1=si 0=no): "))
                    if (descuento==1):
                        print("García Mireya")
                        contadorDescuentos=contadorDescuentos+1
                        print("----REGISTRO PARA EL DESCUENTO----")
                        codigo=str(input("Ingrese el código del producto: "))
                        codigoRestriccion="enero"
                        while codigo!=codigoRestriccion:
                            codigo=str(input("Ingrese el código del producto: "))
                        if codigo==codigoRestriccion:
                            i=0
                            while(i==0):
                                precioProducto=int(input("Ingrese el precio del producto: "))
                                if precioProducto>0:
                                    i+=1
                                else:
                                    print("ERROR  SOLO SE ACEPTAN VALORES POSITIVOS")
                            print("Se le realizo un descuento del 12%")
                            precioProducto=precioProducto-(precioProducto*0.12)
                    elif (descuento==0):
                        print("García Mireya")
                        precioProducto=int(input("Ingrese el precio del producto: "))
                    else:
                        print ("SOLO COLOQUE EL 1 Y EL 0")
                acumuladorPrecio=precioProducto+precioProducto
                eleccion=int (input("¿Deseas seguir comprando? (1=si o 0=no): "))
                if (eleccion==0):
                    break
                else:
                    continue
        elif(seleccion==2):
            print("García Mireya")
            while True:
                print("----FACTURACION ELECTRÓNICA----")
                print("La factura sera enviada a su correo electrónico")
                print("          *El numero de productos son: ", productos)
                print("          *Se realizo un descuento del 12%")
                print("          *El numero de productos con descuento son: ", contadorDescuentos)
                print("          *El precio final de la compra es de $: ", acumuladorPrecio)
                seleccion2=int(input("¿Desea ir al menu principal? (1=si o 0=no): "))
                if (seleccion2==1):
                    break
        if seleccion==3:
            break

