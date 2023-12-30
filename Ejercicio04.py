print("Replica hecha por Mireya García")
print("------ Sistema de calificaciones ------------\n")

print("------ Bienvenido ----------\n")

NUM_CALIFICACIONES= 4
sumaCali = 0.0


for i in range(1,5):
  print(f"Ingresa la calificación {i}: ",end="")
  calificaciones = float(input())
  sumaCali += calificaciones

print("La suma de calificaciones es: ",sumaCali)
promedio = sumaCali/NUM_CALIFICACIONES
print("El promedio de las calificaciones es: ",promedio)

if promedio >=14:
  print("Aprobado")
elif (9 <= promedio <= 13):
  print("Supletorio")
elif promedio <= 8:
  print("Rechazado")
