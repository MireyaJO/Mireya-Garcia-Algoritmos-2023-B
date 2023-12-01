#Soy Mireya Garcia 
x1 = float(input("Ingrese x1:"))
x2 = float(input("Ingrese x2:"))
y1 = float(input("Ingrese y1:"))
y2 = float(input("Ingrese y2:"))
import math
restasPotencias1 =(x2-x1)**2
restasPotencias2 =(y2-y1)**2
suma = restasPotencias1 + restasPotencias2
distancia = math.sqrt(suma)
print("La distancia entre los dos puntos es:", distancia)



