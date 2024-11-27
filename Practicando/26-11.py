'''Escribir un Programa que solicite al usuario la edad de 2 personas, y diga cuál es mayor. Ejemplo:

- La Primera persona es mayor!

Si la edad de ambos es igual se muestra el siguiente mensaje:

- Ambos tienen la misma edad!'''

# a = int(input("Escribe la Edad de la 1 persona: "))
# b = int(input("Escribe la Edad de la 2 persona: "))

# if a > b:
#     print(f"El mayor es {a}")
# elif a == b:
#     print(f"Ambos tienen la misma edad!")
# else:
#     print(f"El mayor es {b}")

'''Introducir un número por teclado y que se muestre un mensaje indicando si es par o impar.'''

# a = int(input("Escribe la Edad de la 1 persona: "))

# if a % 2 == 0:
#     print("Es par")
# else:
#     print("Es impar")

# '''Introducir un número por teclado y que se muestre un mensaje indicando si es múltiplo de 3.'''

# a = int(input("Escribe un número: "))

# if a % 3 == 0:
#     print(f"Es multiplo de 3")
# else:
#     print("No es Multiplo de 3")

'''Escribir un programa que solicite al usuario 3 números, compararlos y decir cual es mayor.'''

a = int(input("Escribe 1 número: "))
b = int(input("Escribe 2 número: "))
c = int(input("Escribe 3 número: "))

if a > b and a > c:
    print(f"El número mayor es: {a}")
elif b > c and b > a:
    print(f"El número mayor es: {b}")
else:
    print(f"El número mayor es: {c}")