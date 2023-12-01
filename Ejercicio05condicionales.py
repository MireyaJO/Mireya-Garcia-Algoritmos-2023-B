print("Soy Mireya García")
precio = 0
precio = float(input("Ingrese el precio por kilo de cada uva: "))
kilo = float(input("Ingrese la cantidad de kilos de uva: "))
tipo = input("Ingrese el tipo de uva (a / b): ")
tamano = int(input("Ingrese el tamaño de la uva (1 / 2): "))
precioInicial = precio * kilo
precio2 = 0 

if tipo == "a":
    if tamano == 1:
        precio2 = precioInicial + 0.20
    else:
        precio2 = precioInicial + 0.30
elif tipo == "b":
    if tamano == 1:
        precio2 = precioInicial - 0.30
    else:
        precio2 = precioInicial - 0.50

print("El precio total es: ", precio2)


