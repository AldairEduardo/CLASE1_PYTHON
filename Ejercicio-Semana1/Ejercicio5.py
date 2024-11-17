# """Ejercico 5: Escribe un programa que tome una calificación numérica de un
# estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:

# - 90-100: A
# - 80-89: B
# - 70-79: C
# - 60-69: D
# - Menos de 60: F        """


num = int(input("Ingrese la calificación: "))

if (num < 60):
    print("Desaprobo con nota F")
elif(num >= 60 and num <=69):
    print("Tiene nota D")
elif(num >= 70 and num <=79):
    print("Tiene nota C")
elif(num >= 80 and num <=89):
    print("Tiene nota B")
elif(num >= 90 and num <=100):
    print("Aprobado con Nota A")
else:
    print("Ingresaste una nota incorrecto")