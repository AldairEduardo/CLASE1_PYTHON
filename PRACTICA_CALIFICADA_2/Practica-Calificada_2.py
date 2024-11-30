'''1. Programa de promedio de calificaciones:

Escribir un programa que pida al usuario que ingrese las calificaciones
de varios exámenes y luego calcule y muestre por pantalla el promedio
de esas calificaciones.'''

opcion = ''
nota = []

while opcion != '3':    
    
    if opcion == '1':
        notas = int(input("Ingresa las calificaciones: "))
        nota.append(notas)
        print(nota)
    if opcion == '2':
        suma = 0
        for i in nota:            
            suma += i             
        print(f"El promedio es:  {(suma / len(nota))}")
    
        
    opcion = input("(1) Añadir calificación \n(2) Ver Promedio Nota \n(3) Salir \n")
    

'''2. Calculadora de área y perímetro:

Escribir un programa que pregunte al usuario las dimensiones de un
rectángulo (largo y ancho) y calcule tanto el área como el perímetro del
rectángulo, mostrando ambos valores por pantalla.'''

opcion = ''


while opcion != '3':    
    
    if opcion == '1':
        ancho = int(input("Ingresa el ancho: "))
        largo = int(input("Ingresa el largo: "))
        
        if ancho > 0 and largo > 0:
            print(f"El area del rectangulo es: {ancho*largo}")
        else:
            print("Ingrese un número positivo")
        
    if opcion == '2': 
        if ancho > 0 and largo > 0:
            suma = f'{ancho + ancho + largo + largo} '
            print(f"El promedio es: {suma}")
        else:
            print("Ingrese un número positivo")
        
    
        
    opcion = input("(1) Ver Area \n(2) Ver Promedio \n(3) Salir \n")

'''3. Buscador de números primos en un rango:

Escribir un programa que pida al usuario dos números enteros y luego
muestre por pantalla todos los números primos que se encuentren en el
rango comprendido entre esos dos números.'''

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1


print(f"Los números primos entre {numero1} y {numero2} son:")
for num in range(numero1, numero2 + 1):
    if es_primo(num):
        print(num)
    
'''4. Contador de palabras en un texto:

Escribir un programa que pida al usuario que ingrese un texto y luego
cuente y muestre por pantalla la cantidad de palabras que contiene ese
texto.'''


texto = []        
opcion = ''

while opcion != '3':
    
    if opcion == '1':
        usuario = input("Escribe un texto: ")
        contar = usuario.split()
        cantidad = len(contar)
        texto.append(cantidad) 
        print("Se Agregó correctamente la Palabra")       
    if opcion == '2':
        print(f"La palabra es: {usuario} y la cantidad de palabra es: {texto[0]}")
    
    opcion = input("(1) Agregar Texto \n(2) Ver Texto y Cantidad \n(3) Salir \nElige una opción:")

'''5. Conversor de unidades de temperatura:

Escribir un programa que pregunte al usuario por una temperatura en
grados Celsius y luego convierta esa temperatura a grados Fahrenheit y
Kelvin, mostrando los resultados por pantalla.'''

# Para convertir de ºC a ºF use la fórmula:   ºF = ºC x 1.8 + 32.
# Para convertir de ºC a K use la fórmula: K = ºC + 273.15.

celsius = float(input("Ingrese una temperatura en grados Celsius: "))

fa = celsius * 1.8 + 32
kelvin =  celsius + 273.15
print(f'La temperatura en Fahrenheit es: {fa:.2f} °F y en Kelvin es: {kelvin:.2f} K')




