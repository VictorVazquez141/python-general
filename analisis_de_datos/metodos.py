'''
Retomando temas en python y ejercicios de Analisis de datos 

    Libreria --> NUMPY
'''
import numpy as np

arr = np.array([1,2,3,4,5,6]) # Creacion de array con una lista
# print(arr)
# #   Elevado al cuadrado 
# arr_squared = arr **2
# print(arr_squared)

# print("Suma: ",arr.sum()) #Suma los elementos

'''
Los arrays permiten realizar operaciones con numpy con grandes cantidades de datos
de manera eficiente. Son arreglos multidimencionales que contienen ELEMENTOS DEL MISMO TIPO,
a diferencia de las listas que contienen diferentes tipos de datos.
'''
# Array multidimencional
arr_multi = np.array([ [1,2,3], [4,5,6] ])
print(arr_multi)
print("-------------")
# Funciones comunes para crear arrays 

# Array de ceros 
arr_ceros = np.zeros((3, 4)) # Array de 3 filas y 4 columnas 
print(arr_ceros)
print("------------")

# Array de unos
arr_unos = np.ones((3, 4)) # 3 filas y 3 columnas 
print(arr_unos)
print("------------")

# Array vacio
arr_vacio = np.empty((2, 2)) #Array sin inicializar
print(arr_vacio)
print(arr_vacio.dtype) # Los arrays vacios no devuelven los valores numericos, sino en float (0.)
print("------------")

# Array con rnago de valores
arr_rangoValores = np.arange(0, 10, 2) # Array creado de 0 a 10 con pasos de 2
print(arr_rangoValores)
# Al mostrar tomamos en cuenta las posiciones contadas desde el index = 0 
print("------------")

# Array con valores igualmente espaciados 
arr_espaciados = np.linspace(0, 1, 5) # 5 valores igualmente espaciados entre 0 y 1
print(arr_espaciados)
print("------------")


'''Propiedades de los arrays'''
# Dimenciones
arr_dimenciones = np.array([ [1,2,3,4], [5,6,7,8]])
print(arr_dimenciones.ndim) # 2 dimenciones
print("------------")

# forma (muestra el tamaño de la dimencion)
print(arr_dimenciones.shape) # 2 dimenciones y 4 elementos en cada uno
print("------------")

# Tipos de datos (Mustra el tipo de dato de los elementos)
print(arr_dimenciones.dtype) # int
print("------------")

'''Operaciones comunes con arrays'''
# Aritmeticas 
arr_arit = np.array([10,20,30,40])
print(arr_arit + 2)

print(arr_arit * 3)
print("-------------")

# Full (Rellenar con valores)
arr_full = np.full( (3, 5), 10)
print(arr_full)
print("------------")

# Elementos random 
arr_random = np.random.rand(2,2)
print(arr_random)
print("------------")

''' reestructurar un array 
# Creación de array con numeros enteros y aleatorios
arr_enteros_rand = np.random.randint(0, 100, 20) 
# indicamos: desde X numero a Y numero, con N cantidad de valores
print(arr_enteros_rand)
print(f"Numero de dimenciones: {arr_dimenciones.ndim}")
    [40 47 82 69 60  8 71 71 90 28 31 99 88 43 68 47 67 11 23 13]

## Creamos una nueva forma del array anterior (reshape)
arr_reformado = np.reshape(arr_enteros_rand,(4,5))
# Creamos la nueva forma del array estructurandolo en 4 filas y 5 columnas (para los 20 datos existentes)
print(arr_reformado)
print(f"Numero de dimenciones: {arr_reformado.ndim}")

[[11 43 21 89 12] 
 [11  6 87 45 83]
 [36 61 78 50 80]
 [37 95 20 38 89]]

'''
 
# Acceder a elementos del array 
array_a = np.array([ [12,9,86], [3,56,21] ])
print(array_a[0,2]) # posición 3 del 1er array
# de un elemento hasta... (:)
print(array_a[0:1])
print(array_a[0::])