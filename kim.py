# A = int(input("Ingrese el primer Número: "))
# B = int(input("Ingrese el segundo Número: "))
# C = int(input("Ingrese el tercer Número: "))

# if A > B and A > C:
#     print("El número mayor es: ",A)

# elif B > A and B > C:
#     print("El número mayor es: ",B)

# elif C > A and C > B:
#     print("El número mayor es: ",C)

# else:
#     print("Los Numeros son iguales")


# ------------------------
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# Usuario = int(input("Ingrese su edad: "))

# if Usuario >= 18:
#     print("Su edad es",Usuario,", Es mayor de Edad")
# else:
#     print("Es menor de edad")

# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

# Num_1 = int(input("Ingrese un número: "))
# Num_2 = int(input("Ingrese otro número: "))


# if Num_1 == 0 or Num_2 == 0:
#     print("No se puede realizar la División")
# else:
#     print("La división es ",Num_1 / Num_2)


# if Num_1 != 0 and Num_2 != 0:
#     print("La división es ",Num_1 / Num_2)
# else:
#     print("No se puede realizar la División")


# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


# Num_1 = int(input("Ingrese un número: "))

# if Num_1 % 2 == 0:
#     print("Es número Par")
# else:
#     print("Es número Impar")

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales
# o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y
# muestre por pantalla si el usuario tiene que tributar o no.

# a = int(input("Ingrese su edad: "))
# b = int(input("Ingrese su ingreso mensual: "))

# if a > 16 and b >= 1000:
#     print("Usted tiene que tributar")
# else:
#     print("Usted no tributa")


# Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes,
# otro mensaje diferente si es sábado o domingo.
# Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

# a = str(input("Ingrese un día de la semana: "))
# semana = a.lower()

# if semana == "lunes":
#     print("Ingresas el día Lunes")
# elif semana == "martes":
#     print("Ingresas el día Martes")
# elif semana == "miercoles":
#     print("Ingresas el día Miercoles")
# elif semana == "jueves":
#     print("Ingresas el día Jueves")
# elif semana == "viernes":
#     print("Ingresas el día Viernes")
# elif semana == "sabado":
#     print("Ingresas el día Sabado")
# elif semana == "domingo":
#     print("Ingresas el día Domingo")
# else:
#     print("Escribiste mal el día:",semana)


# Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número
# (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

# a = int(input("Ingrese un número: "))


# if a > 0:
#     print(" El número absoluto positivo es", a*1)
# elif a < 0:
#     print("El número absoluto negativo es", a*-1)


# Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables.
# A continuación, imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra.
# Si no es así, imprimir “no hay coincidencia”.

# a = str(input("Ingrese primer nombre: "))
# b = str(input("Ingrese segundo nombre: "))

# if (a[0] == b[0]) or (a[-1] == b[-1]) :
#     print("Coinciden")
# else:
#     print("No hay coincidencia")

# Crear un programa que permita al usuario elegir un candidato por el cual votar.
# Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.
# Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”.
# Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

# a = str(input("elija un candidato: "))

# candidato = a.upper()

# if candidato == "A":
#     print("partido rojo")
# elif candidato == "B":
#     print("partido verde")
# elif candidato == "C":
#     print("partido azul")
# else:
#     print("Opción Erronea")

# Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”.
# Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
# informarle que no se puede procesar el dato.

# a = str(input("Ingrese una letra: "))
# vocal = ["a","e","i","o","u"]

# if (len(a) == 1 and a in vocal):
#     print("Es una vocal")
# elif (len(a) == 1 and a not in vocal):
#     print("No es una vocal")
# else:
#     print("Ingreso una cadena")

# Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100,
# excepto que también sea divisible por 400.

# a = int(input("Ingresa el Año: "))

# if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
#     print("El año:",a, "es bisiesto")
# else:
#     print("No es un año bisiesto")


# def bisiesto(a):
#     if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
#         return True
#     else:
#         return False

# a = int(input("Ingresa el Año: "))
# if bisiesto(a):
#     print("El año:",a, "es bisiesto")

# else:
#     print("No es un año bisiesto")

# Haz una calculadora básica que permita realizar el cálculo de la hipotenusa de un triángulo, 
# vigilando que ningún cateto debe ser menor o igual a cero. Si se diera el caso, imprimir «Error» por pantalla.

# a = int(input("Ingresa el 1 número: "))
# b = int(input("Ingresa el 2 número: "))
# Hipotenusa = (a**2 + b**2)
# resultado = Hipotenusa ** 0.5

# if a != 0 and b != 0 or a < 0 and b < 0:
#    print("La hipotenusa es: ", resultado)     
# elif a == 0 or b == 0 and a < 0 or b < 0:
#     print("Error por pantalla")

lenguajes = ["Python", "C", "C++", "Java"]
i = 0

while i < len(lenguajes):
    print(lenguajes[i])
    i += 1