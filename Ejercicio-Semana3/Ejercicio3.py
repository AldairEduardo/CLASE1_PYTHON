'''
Escribir un programa que guarde en un diccionario los precios 
de las frutas de la tabla, pregunte al usuario por una fruta,
un número de kilos y muestre por pantalla el precio de ese número 
de kilos de fruta. Si la fruta no está en el diccionario debe mostrar
un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
'''

    
  

opcion = ''
fruta2 = {'Platano':1.35,'Manzana':0.80,'Pera':0.85,'Naranja':0.70}
compras = []
id = {}
condicion = True

while condicion:
    opcion = input("1: Agregar Frutas: \n 2: Listar Compras \n 3: Eliminar Frutas \n 4: Cancelar ")

    if opcion == '1':
        fruta = str(input("Ingrese la fruta: "))
        Kilos = int(input("Ingrese el Kilo: "))
        if fruta in fruta2:
            for clave,valor in fruta2.items():
                if clave == fruta:
                    resultado = f'Fruta: {fruta} - Precio: {fruta2[fruta] * Kilos}'
                    compras.append(resultado)
        else:
            print("No hay esa fruta")
            
    if opcion == '2':
        print(compras)
    
    if opcion == '3':
        delete = int(input("Ingrese la fruta a eliminar: "))
        compras.pop(delete)
    
    if opcion =='4':
        condicion = False
     
    

    

    
    
    

# print(fruta2['Platano'])1
