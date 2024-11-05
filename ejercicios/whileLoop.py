'''
EJERCICIOS CON WHILE, BREAK & CONTINUE
'''
# Imprimir no vocales en una cadena
cadena = "Hola mundo"
i = 0 #Iterable de la cadena

while i < len(cadena): #mientras i sea menor a la cantidad de elementos de la cadena se ejecuta el bloque de abajo
    
    if cadena[i].lower() in 'aeiou': # si cada elemento de la cadena (sea MAYU o minus) esta en 'aeiou' (sea bocal)
        i += 1 # la iteración recorre una posición ...
        continue # salta la impresión si el caracter es una vocal
    
    print(cadena[i], end=' ') # esa iteración 'vocal' que se salta es sustituida por un espacio con (end=' ')
    i += 1 #recorre una posición 'iterable' para detercar de la cadena ingresada 


'''
Sumar solo numeros positivos en una lista 
'''
numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]
suma = 0
i = 0

while i < len(numeros): #
    if numeros[i] < 0: #si el numero iterado es menor a 0 entonces pasa a la siguiente posición
        i += 1
        continue # Salta la suma si el numero es negativo
    suma += numeros[i]
    i += 1
print("\nLa suma de numeros positivos total es: ",suma)


'''
Encontrar la primera posición de un numero en una lista 
'''
numeros = [4, 2, 7, 3, 9, 2, 5, 2]
numero_buscado = 2
i = 0

while i < len(numeros): #mismo procedimiento para recorrer la lista por cada iteración  <---
    if numeros[i] != numero_buscado: #si el primer iterable es diferente al buscado...     -
        i += 1                       #Se pasa a la siguiente posición    <------------------
        continue    
    # Aqui se autodenomina como un else (Si si es igual el numero...) e imprime el mensaje y el break
    print(f"\nEl numero {numero_buscado} está en la posición {i}")
    break


'''
Ejercicio: meter 5 cadenas dentro de una lista
'''
# almacenamiento = []
# print("\nIntroduce 5 cadenas de texto.")
# conteo = 1


# while len(almacenamiento) < 5:
#     print(f"Valor numero: {conteo}")
#     conteo += 1
#     valor = input("-> ")
    
#     if valor:
#         almacenamiento.append(valor)
#     else: 
#         break
#     continue
# print(f"Almacenamiento: {almacenamiento}")

# if len(almacenamiento) == 5:
#     print("Yes, all it's ok") 



