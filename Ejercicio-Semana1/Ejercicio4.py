# """Ejercico 4: Escribe un programa que solicite al usuario un número entero y calcule
# si es divisible por 3 y por 5."""


numero = int(input("Ingrese número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("El número",numero, "si es divisible por 3 y 5")
else:
    print("El número",numero, "no es divisible por 3 y 5")
    