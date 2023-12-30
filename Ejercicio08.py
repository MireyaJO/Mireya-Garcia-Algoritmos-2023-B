print("Replica hecha por Mireya García")
print("------------------- LA UNIÓN  ---------------")

numGuaguas = int(input("Ingrese el número de guaguas de pan: "))
sumatoriaGuaguas = 0.0
sumaMora = 0
contadorGuaguas = 0

if (numGuaguas>0):
    while contadorGuaguas <numGuaguas :
        precioGuagua = float(input(f'Ingrese el precio de la guagua de pan {contadorGuaguas+1}: '))
        sumatoriaGuaguas += precioGuagua
        print("¿La guagua de pan es de mora?")
        tipoGuagua = input("si o no: ")
        if tipoGuagua == "si":
            sumaMora += 1   
        contadorGuaguas += 1 
    print("\n----------- Factura electrónica -----------------\n")
    print("El total de guaguas de pan a facturar son de ",numGuaguas)
    print("El pecio final a pagar es del $",sumatoriaGuaguas)
    print("El número de guaguas de mora son de",sumaMora)
else:
    print("El numero de guaguas no es admitido")
    