
# """Ejercicio 1: Escribe un programa que solicite al usuario dos números y muestre su
# suma, resta, multiplicación, división, división entera y residuo (módulo)."""

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

print(f"La suma de los números es: {numero_1 + numero_2}")
print(f"La resta de los números es: {numero_1 - numero_2}")
print(f"La Multiplicación de los números es: {numero_1 * numero_2}")
print(f"La División de los números es: {numero_1 / numero_2}")
print(f"La División Entera de los números es: {round(numero_1 / numero_2)}")
print(f"El Residuo de los números es: {numero_1 % numero_2}")

# """Ejercicio 2: Escribe un programa que solicite al usuario un número entero y calcule
# su cuadrado y su cubo."""

numero_1 = int(input("Ingrese el primer número: "))
print(f"El cuadrado del número es: {numero_1 ** 2}")
print(f"El cubo del número es: {numero_1 ** 3}")

# """Ejercico 3: Escribe un programa que lea un número entero y determine si es
# positivo, negativo o cero."""

numero_1 = int(input("Ingrese el primer número: "))


if numero_1 > 0:
    print("El numero es positivo")
elif numero_1 < 0:
    print("El numero es negativo")
elif numero_1 == 0:
    print("El número es cero")

# """Ejercico 4: Escribe un programa que solicite al usuario un número entero y calcule
# si es divisible por 3 y por 5."""


numero_1 = int(input("Ingrese número: "))

if (numero_1 % 3 == 0) or (numero_1 % 5 == 0):
    print("El número si es divisible")
else:
    print("El número no es divisible")
    

# """Ejercico 5: Escribe un programa que tome una calificación numérica de un
# estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:

# - 90-100: A
# - 80-89: B
# - 70-79: C
# - 60-69: D
# - Menos de 60: F        """

numero_1 = int(input("Ingrese la calificación: "))

if (numero_1 < 60):
    print("Desaprobo con nota F")
elif(numero_1 >= 60 and numero_1 <=69):
    print("Tiene nota D")
elif(numero_1 >= 70 and numero_1 <=79):
    print("Tiene nota C")
elif(numero_1 >= 80 and numero_1 <=89):
    print("Tiene nota B")
elif(numero_1 >= 90 and numero_1 <=100):
    print("Aprobado con Nota A")
else:
    print("Ingresaste un número incorrecto")


# """Ejercicio 6: Escribe un programa que solicite al usuario tres números y determine
# cuál de ellos es el mayor."""

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input("Ingrese el tercer número: "))


if numero_1 > numero_2:
    print(f"El número mayor es: {numero_1}")
elif numero_2 > numero_3:
    print(f"El número mayor es: {numero_2}")
elif numero_1 == numero_2 and numero_2 == numero_3 and numero_1 == numero_3:
    print("Los números son iguales.")
else:
    print(f"El número mayor es: {numero_3}")


# """Ejercico 7: Escribe un programa que solicite al usuario un número entero y
# determine si es par o impar."""   

numero_1 = int(input("Ingrese el número: "))

numero_2 = numero_1 % 2

if numero_2 == 0:
    print("Es par")
else:
    print("Es impar")
    

    

