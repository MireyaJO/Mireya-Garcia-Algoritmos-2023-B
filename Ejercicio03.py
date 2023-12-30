import os

print("Replica hecha por Mireya García")
puntoInicial = int(input("Ingrese el punto inicial: "))
puntoFinal = int(input("Ingrese el punto final: "))
sumatoria = 0

while puntoInicial<0 or puntoFinal<0:
    os.system("cls")
    print("-----------ERROR-----------")
    print("Deben ser valores positivos")
    puntoInicial = int(input("Ingrese el punto inicial: "))
    puntoFinal = int(input("Ingrese el punto final: "))

while puntoInicial > puntoFinal:
    os.system("cls")
    print("-----------ERROR-----------")
    print("El punto inicial debe ser menor que el final")
    puntoInicial = int(input("Ingrese el punto inicial: "))
    puntoFinal = int(input("Ingrese el punto final: "))

    while puntoInicial<0 or puntoFinal<0:
      os.system("cls")
      print("-----------ERROR-----------")
      print("Deben ser valores positivos")
      puntoInicial = int(input("Ingrese el punto inicial: "))
      puntoFinal = int(input("Ingrese el punto final: "))

os.system("cls")
while puntoInicial <= puntoFinal:
    sumatoria += puntoInicial
    puntoInicial += 1

print("La sumatoria es: ", sumatoria)



