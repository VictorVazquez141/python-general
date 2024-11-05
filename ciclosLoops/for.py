'''
Ciclo For 
-Es utilizado para iterar sobre una secuencia (lista, tupla, diccionario o cadena) o en otros como rangos 
/ESTRUCTURA:

for 'elemento' in 'elemencia':
    #bloque de codigo

- En cada iteración, el 'elemento' toma el valor de un item de la 
  secuencia y el bloque de codigo se ejecuta con ese valor
'''
# /////////// EJEMPLO 1 (Elementos de una lista)
# frutas = ["pera", "manzana", "piña"]
# for x in frutas: 
#     print(x)


# ////////// Ejemplo 2 (iteración de cadena)
# cadena = "Hola"
# for caracter in cadena:
#     print(caracter)         #imprime cada letra de la cadena


#Ejemplo 3 (usar 'range()' para una secuencai de numeros)
# for i in range(10):
#     print(i) # Imprime los numeros del 0 al 9 contando un 'rango de 10' a manos que sea range(1,10) del 1 al 10


# ////////// EJEMPLO 4 (iterar sobre un diccionario)
# diccionario_1 = {
#     "Juanito": 78,
#     "Lupita": 90,
#     "Raul": 89
# }
# # como iterables se seleccionan dos (la calve y el valor)
# for nombre, promedio in diccionario_1.items(): # 'items() ayuda a iterar sobre los pares clave-valor'
#     print(f"{nombre} tiene promedio de {promedio}")
    


# #/// EJEMPLO CON BREAK
# numeros = [1, 2, 3, 4, 5]

# for numero in numeros:
#     if numero == 3:
#         break  # Sale del bucle cuando encuentra el número 3
#     print(numero)


'''
Iteración de mas de dos listas o elemntos 
'''
abecedario = ["A", "B", "C", "D", "E", "F"]
numeros = (1,2,3,4,5,6,7,8,9,0)
contador = 1

for letra, numero in zip(abecedario, numeros):  # zip() nos ayuda a iterar mas de una lista o tupla
    print(f"Lista: Valor {contador} es {letra}")
    print(f"Tupla: valor {contador} es {numero}")
    contador += 1
    
'''
Forma correcta de recorrer una lista con su indice 
'''
for num in enumerate(numeros):
    indice = num[0] # valor del indice a mostrar
    valor = num[1] # valor del valor de cada numero en la tupla
    print(f"El indice es {indice} y el valor es {valor}")


