#Ejercicio 01 
#Realice un programa, para calcular la suma de los N primeros números pares.   
#Es decir, si insertamos un 8, nos haga la suma de 2+4+6+8. 
#Recuerda utilizar la sentencia de repetición.
print("Ejercicio realizado por Mireya García")
numero = int(input("Ingresa el número: "))
sumatoria=0
if (numero > 0):
  for i in range(numero+1):
    print(i)
    if(i%2==0):
      sumatoria +=i
else:
  print("Número no válido")
print("La sumatoria es: ", sumatoria)


