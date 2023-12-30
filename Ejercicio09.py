print("Replica hecha por Mireya García")
print("------------------- EPN  ---------------")

numEmpleados = int(input("Ingrese el número de empleados a registrar: "))
sumatoriaSueldos = 0.0
sumatoriaHoras = 0
sumaDocentes = 0

for i in range(1,numEmpleados+1):
  sueldo= float(input(f'Ingrese el sueldo del empleado N°{i}: '))
  sumatoriaSueldos += sueldo
  horas= int(input(f'Ingrese el número de horas que ha trabajado el empleado N°{i}: '))
  sumatoriaHoras += horas
  print("¿El empleado es docente?")
  docente = input("si o no: ")
  if docente == "si":
    sumaDocentes +=1

print("--------------- Contabilidad de empleados en la EPN -------------")
print("La cantidad de empleados que se han registrado son: ",numEmpleados)
print("El sueldo de todos los empleados es de",sumatoriaSueldos)
print("El total de horas trabajadas de los empleados es de",sumatoriaHoras)
print("La cantidad de empleados que son docentes son: ",sumaDocentes)

