#Ejercicio 01
print("Hola clase de Algoritmos y Estructuras","\n","Soy Mireya García")
print("\n")

#Ejercicio 02
#Soy Mireya García
print("Programa que suma dos números")
numeroUno=8
numeroDos=9
suma=numeroUno+numeroDos
print(suma)
print("El resultado de la suma es:", suma) 
print("\n")

#Ejercicio 03
#string
print("Programa que imprime cadena de caracteres")
mensaje="Hola"
mensaje+=" "
mensaje+="clase"
mensaje+=" "
mensaje+="de"
mensaje+=" "
mensaje+="Algoritmos"
mensaje+=" "
mensaje+="y"
mensaje+=" "
mensaje+="Estructuras"
mensaje+="."
mensaje+=" "
mensaje+="Soy"
mensaje+=" "
mensaje+="Mireya"
mensaje+=" "
mensaje+="García"
print(mensaje)
print("\n")

#Ejercicio 04
print("Programa que imprime cadena de caracteres")
mensaje01="Hola"
mensaje02="clase"
mensaje03="de"
mensaje04="Algoritmos"
mensaje05="y"
mensaje06="Estructuras"
mensaje07="."
mensaje08="Soy"
nombre="Mireya"
apellido="García"
mensajeCompleto=mensaje01+" "+mensaje02+" "+mensaje03+" "+mensaje04+" "+mensaje05+" "+mensaje06+mensaje07+" "+mensaje08+" "+nombre+" "+apellido
print(mensajeCompleto)
print("\n")

#Ejercicio 05
print("Programa que busca caracteres dentro de una cadena de caracteres")
mensaje="Hola clase de Algoritmos y Estructuras. Soy Mireya García"
subcadena01=mensaje.find("Algoritmos")
print(subcadena01)
print("\n")

#Ejercicio 06
print("Programa que busca un rango de cadena de caracteres")
mensaje=("Hola clase de Algoritmos y Estructuras. Soy Mireya García")
subcadena02=mensaje[14:20]
print(subcadena02)
print("\n")

#Ejercicio 07
print("Programa que compara igualdad")
mensaje001="Hola clase de Algoritmos y Estructuras. Soy Mireya García"
mensaje002="Hola clase de Algoritmos y Estructuras. Soy Mireya García"
print(mensaje001 == mensaje002)
print("\n")

#Deber 01 
#Resta de números (el usuario puede colocar el número que desee)
#Soy Mireya García
print("Programa que reste dos números")
numeroUno=float(input("Coloque cualquier primer número:"))
numeroDos=float(input("Coloque cualquier segundo número:"))
resta=numeroUno-numeroDos
print(resta)
print("El resultado de la resta es:", resta) 
print("\n")

#Multiplicación de números (el usuario puede colocar el número que desee)
#Soy Mireya García
print("Programa que multiplique dos números")
numeroUno=float(input("Coloque cualquier primer número:"))
numeroDos=float(input("Coloque cualquier segundo número:"))
multiplicación=numeroUno*numeroDos
print(multiplicación)
print("El resultado de la multiplicación es:", multiplicación) 
print("\n")

#División de números (el usuario puede colocar el número que desee)
#Soy Mireya García
print("Programa que divide dos números")
Dividendo=float(input("Coloque cualquier numero que sea el dividiendo:"))
Divisor=float(input("Coloque cualquier  número excepto el 0 que sea el divisor:"))
División=Dividendo/Divisor
print(División)
print("El resultado de la división es:", División) 
print("\n")

#Módulo de un número (el usuario puede colocar el número que desee)
#Soy Mireya García
print("Programa que encuentra el residuo de una división entre dos números")
Dividendo=float(input("Coloque cualquier numero que sea el dividiendo:"))
Divisor=float(input("Coloque cualquier  número excepto el 0 que sea el divisor:"))
Cociente=Dividendo//Divisor
Módulo= Dividendo - (Cociente*Divisor)
print("El residuo de la división es:", Módulo)
print("\n")

#Factorial de un número (el usuario puede colocar el número que desee)
#Soy Mireya García
print("Programa para obtener el factorial de un número")
numero= int(input("Coloque cualquier número:"))
factorial=1
for n in range(1, numero+1):
    factorial*=n
print("El factorial del número propuesto es:", factorial)
print("\n")

#Deber 01 (otra manera de realizarlo)
#Resta de números (el usuario NO puede colocar el número 
#que desee, el número ya esta establecido)
#Soy Mireya García
print("Programa que reste dos números")
numeroUno=8
numeroDos=10 
resta=numeroUno-numeroDos
print(resta)
print("El resultado de la resta es:", resta) 
print("\n")

#Multiplicación de números (el usuario NO puede colocar 
#el número que desee, el número ya esta establecido)
#Soy Mireya García
print("Programa que multiplique dos números")
numeroUno=10
numeroDos=20
multiplicación=numeroUno*numeroDos
print(multiplicación)
print("El resultado de la multiplicación es:", multiplicación) 
print("\n")

#División de números (el usuario NO puede colocar 
#el número que desee, el número ya esta establecido)
#Soy Mireya García
print("Programa que dividi dos números")
Dividendo=10
Divisor=5
División=Dividendo/Divisor
print(División)
print("El resultado de la división es:", División) 
print("\n")

#Módulo de un número (el usuario NO puede colocar 
#el número que desee, el número ya esta establecido)
#Soy Mireya García
print("Programa que encuentra el residuo de una división entre dos números")
Dividendo=45
Divisor=7
Cociente=Dividendo//Divisor
print("El resultado de la división es:", Cociente) 
Módulo= Dividendo - (Cociente*Divisor)
print("El residuo de la división es:", Módulo)
print("\n")

#Factorial de un número (el usuario NO puede colocar 
#el número que desee, el número ya esta establecido)
#Soy Mireya García
print("Programa para obtener el factorial de un número")
numero= 10 
factorial01=numero-1
factorial02=numero-2
factorial03=numero-3
factorial04=numero-4
factorial05=numero-5
factorial06=numero-6
factorial07=numero-7
factorial08=numero-8
factorial09=numero-9
factorialTotal= numero*factorial01*factorial02*factorial03*factorial04*factorial05*factorial06*factorial07*factorial08*factorial09
print("El factorial de", numero,"es:", factorialTotal)

