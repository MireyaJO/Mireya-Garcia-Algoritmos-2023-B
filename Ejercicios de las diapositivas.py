print("Ejercicio de réplica 01")
print("Soy Mireya García")
lista = [1, 3, 2, 7, 9, 8, 6]
print("Respesta:", 4 in lista,"\n") 


print("Ejercicio de réplica 02")
print("Soy Mireya García")
x=4
y=2
lista = [1, 5]
print("Respuesta 1:", x is lista) 
print("Respuesta 2:", x is 4,"\n") 



print("Ejercicio de réplica 03")
print("Soy Mireya García")
#Esto es un comentario 
print("Hola","\n")
"Esto es otro comentario xczczxc"
"""Hola esto
es un 
comentario
s
s
s
s
"""

print("Ejercicio de réplica 04")
print("Soy Mireya García")
a= -1 #a es de tipo int y su valor es -1
b= a + 2 #b es de tipo int y su valor es 1
print(b)
suma=1.1+2.2
print (suma,"\n")


print("Ejercicio de réplica 05")
print("Soy Mireya García")
real = 1.1+2.2 #real es un float
print (real) #representación aproximada de 3.3
print(f'{real:.2f}')
un_real= 1.1 
print(un_real)
otro_real= 1/2 
print(otro_real)
not_cient = 1.23E3 
print(not_cient,"\n")


print("Ejercicio de réplica 06")
print("Soy Mireya García")
complejo = 1+2j
print (complejo.real)
print (complejo.imag,"\n")


print ("Ejercicio de réplica 07")
print("Soy Mireya García")
#Excepciones del "bool"
print(bool(0)) 
print(bool(len("")),"\n")


print("Ejercicio de réplica 08")
print("Soy Mireya García")
print(bool(0.0))
print(bool(0j))
print(bool(''))
print(bool())
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(range(0)),"\n")


print("Ejercicio de réplica 09")
print("Soy Mireya García")
caracter_a='a'
print(caracter_a)
hola = 'Hola "Fythonista"'
hola_2 = 'Hola \'Fythonista\''
hola_3 = "Hola 'Fythonista'"
print(hola)
print(hola_2)
print(hola_3,"\n")


print("Ejercicio de réplica 10")
print("Soy Mireya García")
lista = [1, 2, 3, 8, 9]
tupla = (1, 4, 8, 0, 5)
conjunto = set({1, 3, 1, 4})
diccionario = {'a': 1, 'b':3, 'z':8}
print(lista)
print(tupla)
print(conjunto)
print(diccionario,"\n")


print("Ejercicio de réplica 11")
print("Soy Mireya García")
type(3)
type(2.78)
type('Hola')
isinstance (3,float)
isinstance (3,int)
isinstance (3,bool)
isinstance (False, bool)
print("\n")


print("Ejercicio de réplica 12")
print("Soy Mireya García")
#Tipo de dato entero o largo
numero = 15
print(numero, type(numero))
#Tipo de dato flotante
numero_flotante=15.5
print (numero_flotante, type(numero_flotante))
#Tipo de dato Número complejo 
numero_complejo=5+6j
print(numero_complejo, type(numero_complejo))
#Tipo de dato String 
nombre="Ernesto"
print(nombre, type(nombre))
#Tipo de dato Booleano
verdadero_falso=3==3
print(verdadero_falso, type(verdadero_falso),"\n")


print("Ejercicio de réplica 13")
print("Soy Mireya García")
edad0= '25'
conversión = int(edad0) + 10  #conversión forzada
print(conversión)
edad1=35
print (str(edad1))
num1 = '18.66'
float(num1)
print (num1,"\n")


print("Ejercicio de réplica 14")
print("Soy Mireya García")
mensaje = input("Introduce tu nombre: ")
numeroEntero = int(input("Introduce número entero: "))
numeroFlotante = float(input("Introduce número flotante: "))
numeroComplejo = complex(input("Introduce número complejo: "))
print("Bienvenido:", mensaje)
print("En número entero introducido es:", numeroEntero)
print("En número flotante introducido es:", numeroFlotante)
print("En número complejo introducido es:", numeroComplejo,"\n")
