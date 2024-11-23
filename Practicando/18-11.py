# # Lista para ejemplo de demostración
# alguna_lista = [1, 2, 5, 7, 8, 10]

# # Lista vacía que se rellenará con un bucle
# lista_par = []

# for i in alguna_lista:
#   if i % 2 == 0:
#     lista_par.append(i)
# print(lista_par)

"""1. Crear una tabla de multiplicar Escribe un programa 
que pida un número al usuario y genere su tabla de multiplicar del 1 al 10.usando un bucle"""

# num=int(input("Ingrese un número: "))

# for i in range(1,11):
#     print(f"{num} x {i}: {num*i}")
    

'''2. Sumar todos los elementos de un array
Crea un programa que tome una lista de números y calcule la suma de todos sus elementos
'''

# num = [1,10,2,25,10,8,4]
# num2 = 0
# for i in num:
#     num2 += i
# print(num2)
   

'''3.  Encontrar el número más grande en un array
Escribe un programa que determine el mayor número en una lista.
'''
# num = [5,50,10,100,200,65,1000,0,5000,90]
# num2 = 0

# for i in num:
#     if num2 < i:
#         num2 = i
# print(f"El numero mayor es: {num2}")       
     
'''4.  Contar números pares e impares en un array
Haz un programa que cuente cuántos números pares e impares hay en una lista.
'''
# num = [2,5,8,9,15,10]
# par = []
# impar = []

# for i in num:
#     if i %2 == 0:
#         par.append(i)
#     else:
#         impar.append(i)
# print(f"Los números pares son: {par}")
# print(f"Los números impares son: {impar}")

"""5. Crear una lista con los cuadrados de los números del 1 al 10
Usa un bucle para crear una lista que contenga los cuadrados de los números del 1 al 10.
"""

lista =[]

for i in range(1,11):
        i = i**2
        lista.append(i)
print(lista)

'''Asigna a una variable la cadena esto es un ejemplo, y haz que se escriba por pantalla la
cadena un ejemplo es esto utilizando la notaci ́on de slices.'''

# a = "esto es un ejemplo"
# print(f"{a[8:]} {a[5:7]} {a[0:4]}")

# s=[1,2,3,4,5]
# s[2:-1]=[]
# print(s)

'''crea un programa en donde quiero que el usuario ingrese su edad
para saber si es mayor o menor'''


# a= {1:"pepe",2:"Kim",3:"Eduardo",4:"papa"}
# print(a[1])
# print(a.get(2))

# edad = 12
# while edad < 18:
#     edad = edad + 1
#     print ("Felicidades, tienes ",edad)