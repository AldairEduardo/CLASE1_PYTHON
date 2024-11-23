'''1. Suma de los elementos de una lista
Crea un programa que recorra una lista y calcule la suma de todos los elementos.

2. Encuentra el número más grande
Escribe un programa que recorra una lista y encuentre el número más grande en ella.

3. Imprime los números pares
Crea un programa que recorra una lista y muestre solo los números pare

'''

# num = [5,2,4,3,6,7,8,5]
# suma = 0

# for i in num:
#     suma += i 
# print(suma)

# num = [5,2,4,3,6,7,8,5]
# mayor = 0

# for i in num:
#     if mayor < i:
#         mayor = i
# print(mayor)

# num = [5,2,4,3,6,7,8,5]
# a = []

# for i in num:
#     if i % 2 ==0:
#         a.append(i)
# print(a)

'''4. Lista de cuadrados
Genera una nueva lista que contenga el cuadrado de cada número de una lista original.

5. Cuenta elementos mayores a un valor
Escribe un programa que cuente cuántos elementos en una lista son mayores a un número dado por el usuario.

6. Invertir una lista
Crea un programa que tome una lista y devuelva otra lista con los elementos en orden inverso.'''

# num = [5,2,4,3,6,7,8,5]
# a = []
# for i in num:
#     i = i**2
#     a.append(i)
# print(a)

# usu=int(input("Ingrese un Número: "))  

# a = [5, 10, 15, 20, 25]
# b=[]
# for i in a:    
#     if i > usu:
#         b.append(i)
# print(b)   

# a = [5, 10, 15, 20, 25]

# for i in a:
#     i = a[::-1]
# print(i)
    
'''7. Eliminar duplicados
Escribe un programa que recorra una lista y elimine los elementos duplicados.

8. Suma de elementos en posiciones pares
Crea un programa que recorra una lista y sume los elementos que se encuentran en posiciones pares.

9. Filtrar números mayores a un valor
Crea una nueva lista que contenga solo los números mayores a un valor especificado por el usuario.

'''

# num = [1,1,2,2,6,4,5,8,4,4,4]
# a = []
# for i in num:
#     if num.count(i) == 1:
#         a.append(i)  
# print(a)       

a = int(input("Ingrese un número: ")) #b + a = c + a = 
b = int(input("Ingrese un número: "))
c = int(input("longitud de número: "))
num = [a,b]

for _ in range(c - 2):
      bucle = num[-1] + num[-2]
      num.append(bucle)
print(num)
      
     
       

       