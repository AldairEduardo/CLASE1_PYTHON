'''* Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".'''
 
# a = 0
# while a >= 100:
#     if a  3 == 0

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} -FizzBuzz")   
    elif i % 3 == 0:
        print(f"{i} -Fizz")  
        
    elif i % 5 == 0:
        print(f"{i} -Buzz")  
    else:
        print(f"{i} no es multiplo de 3 ni de 5")