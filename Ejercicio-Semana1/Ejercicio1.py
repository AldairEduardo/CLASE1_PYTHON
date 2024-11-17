# numero_1 = float(input("Ingrese el primer número: "))
# numero_2 = float(input("Ingrese el segundo número: "))

# sum = numero_1 + numero_2
# rest=numero_1 - numero_2
# mult=numero_1 * numero_2
# div=numero_1/numero_2 if numero_2 !=0 else "No se puede dividir entre cero"
# divEntera= numero_1 // numero_2 if numero_2 !=0 else "No se puede dividir entre cero"
# Residuo=  numero_1 % numero_2 if numero_2 !=0 else "No se puede dividir entre cero"

# print(f"La suma de los números es: {sum}")
# print(f"La resta de los números es: {rest}")
# print(f"La Multiplicación de los números es: {mult}")
# print(f"La División de los números es: {div}")
# print(f"La División Entera de los números es: {divEntera}")
# print(f"El Residuo de los números es: {Residuo}")

import math

numero_1 = int(input("Ingrese el primer número: "))
cuadrado = math.pow(numero_1,2)
cubo = math.pow(numero_1,3)
print(f"El cuadrado es: {cuadrado} y al cubo es: {cubo}")