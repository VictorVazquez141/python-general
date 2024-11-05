'''Manipulación de array'''
import numpy as np 
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

# Creación de array con numeros enteros y aleatorios
arr_enteros_rand = np.random.randint(0, 100, 20) 
# indicamos: desde X numero a Y numero, con N cantidad de valores
print(arr_enteros_rand)
print(f"Numero de dimenciones: {arr_dimenciones.ndim}")
''' [40 47 82 69 60  8 71 71 90 28 31 99 88 43 68 47 67 11 23 13]'''

## Creamos una nueva forma del array anterior (reshape)
arr_reformado = np.reshape(arr_enteros_rand,(4,5))
# Creamos la nueva forma del array estructurandolo en 4 filas y 5 columnas (para los 20 datos existentes)
print(arr_reformado)
print(f"Numero de dimenciones: {arr_reformado.ndim}")
'''
[[11 43 21 89 12] 
 [11  6 87 45 83]
 [36 61 78 50 80]
 [37 95 20 38 89]]'''
 
# 
arr_manipulado = np.arange(9).reshape((3, 3))
print(arr_manipulado)
print(np.argmin(arr_reformado))
print(np.argmax(arr_reformado))
print("------------------------")

#Envolver todas las dimenicones del array (ravel())
arr_envolver = np.array([ [2,4,6,8], [12,14,16,18] ])
print(f"Array normal:\n{arr_envolver}")
print(f"Array envuelto: \n{arr_envolver.ravel()}\n")

# Cambiar las filas por columnas 
arr_formas = np.arange(16).reshape((4, 4)) #16 elementos acomodados en 4 filas y 4 columnas 
print(arr_formas)

arr_formas1 = np.arange(15).reshape((3, 5)) #16 elementos acomodados en 3 filas y 5 columnas 
print(arr_formas1, "\n")

# Crear un array y cambiar su forma 
arr_gpt = np.arange(1,17)
print(arr_gpt)
arr_gpt_x = arr_gpt.reshape(4,4)
print(arr_gpt_x)

#Segmentación de un array 
array_seg = np.arange(1,20)
print("\n",array_seg)
print("\n ",array_seg[8:16])


    
