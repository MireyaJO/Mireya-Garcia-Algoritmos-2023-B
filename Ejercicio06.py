print("Replica hecha por Mireya García")
print("--------- Banco Pichincha ----------")

nombreCliente=input("Ingrese el nombre del cliente: ")
print("Ingrese el tipo de tarjeta")
tipoTarjeta = int(input("1) o 2) o 3) o 4): "))

while (tipoTarjeta!=1 and tipoTarjeta!=2 and tipoTarjeta!=3 and tipoTarjeta!=4):
  print("Tipo de tarjeta no válido")
  print("Ingrese el tipo de tarjeta")
  tipoTarjeta = int(input("1) o 2) o 3) o 4): "))

creditoAnterior= float((input("Ingrese el crédito actual: ")))
creditoActual = 0.0


def creditoBanco (tipoTrajeta):
  if tipoTarjeta == 1:
    creditoActual = creditoAnterior + (creditoAnterior * 0.25)
    print("El nuevo crédito para su tarjeta es de: ",creditoActual)
  elif tipoTarjeta == 2:
    creditoActual = creditoAnterior + (creditoAnterior * 0.35)
    print("El nuevo crédito para su tarjeta es de: ",creditoActual)
  elif tipoTarjeta == 3:
    creditoActual = creditoAnterior + (creditoAnterior * 0.40)
    print("El nuevo crédito para su tarjeta es de: ",creditoActual)
  else:
    creditoActual = creditoAnterior + (creditoAnterior * 0.50)
    print("El nuevo crédito para su tarjeta es de: ",creditoActual)

creditoBanco(tipoTarjeta)