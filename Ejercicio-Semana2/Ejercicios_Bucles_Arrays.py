# 1. Crear una tabla de multiplicar Escribe un programa que pida un número al usuario y genere su tabla de multiplicar del 1 al 10.
# usando un bucle

num = int(input("Ingrese un número: "))
print(f"La tabla de Multiplicar del 1 al 10 del {num} es: ")

for i in range(1,11):
    print(f"{num} x {i}: {num*i}")
    

# 2. Sumar todos los elementos de un array
# Crea un programa que tome una lista de números y calcule la suma de todos sus elementos.

numeros = [41,4,1,5,2,4,8,5]
sum=0

for i in numeros:
    sum+=i

print("LA SUMA ES: ",sum)