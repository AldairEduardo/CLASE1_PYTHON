'''1. Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas. (10 p)
'''


# usuario = str(input("Ingrese la contraseña: "))
# passw = usuario.lower()
# pass_secret = "contraseña"

# if passw == pass_secret:
#     print(f"Ingresaste la contraseña correcta!")
# else:
#     print("No coincide la contraseña")
    
'''2. Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte
al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
que tributar o no. (10p)'''

# edad = int(input("Ingrese su edad: "))
# ingreso = int(input("Ingrese su ingreso: "))

# if edad >= 16 and ingreso >= 1000:
#     print(f"usted tiene: {edad} y gana: S/.{ingreso}, ¡Usted Tributa!")
# else:
#     print("Usted no Tributa")

'''3. Los tramos impositivos para la declaración de la renta en un determinado país son los
siguientes:

Renta Tipo impositivo
Menos de 10000€ 5%
Entre 10000€ y 20000€ 15%
Entre 20000€ y 35000€ 20%
Entre 35000€ y 60000€ 30%
Más de 60000€ 45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el
tipo impositivo que le corresponde. (10p)'''

# renta = int(input("Ingrese su renta Anual: "))

# if renta < 10000:
#     print("Le corresponde el tipo imposivo de 5%")
# elif renta >= 10000 and renta <= 20000:
#     print("Le corresponde el tipo imposivo de 15%")
# elif renta > 20000 and renta <= 35000:
#     print("Le corresponde el tipo imposivo de 20%")
# elif renta > 35000 and renta <= 60000:
#     print("Le corresponde el tipo imposivo de 30%")
# elif renta > 60000:
#     print("Le corresponde el tipo imposivo de 45%")
# else:
#     print("Ingreso un dato incorrecto")

'''Escribir un programa para una empresa que tiene salas de juegos para todas las
edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes
por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el
precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre
4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€. (10p)'''

# print("Bienvenidos a las salas de Juegos")
# print("*"*33)
# edad = int(input("Ingrese su edad: "))

# if edad < 4:
#     print("Usted puede ingresar Gratis")
# elif edad >= 4 and edad < 18:
#     print("Usted debe pagar S/.5.00")
# else:
#     print("Usted debe pagar S/.10.00")