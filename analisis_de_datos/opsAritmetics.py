'''Operaciones aritmeticas con arrays (Numpy)'''
import numpy as np

# Sumas de arrays de 1 dimención
arr_num1 = np.array([1,2,3,4])
arr_num2 = np.array([9,8,7,6])
print(arr_num1 + arr_num2) # [10 10 10 10]

#Con arrays de 2 dimenciones o mas 
arr_num1 = np.array([ [1,2,3,4], [3,2,3,2] ])
arr_num2 = np.array([3,2,4,1])
print(arr_num1 + arr_num2) # mismo caso en multiplicaciones, restas, diviciones, etc
''' Reultado: 
[[4 4 7 5]
 [6 4 7 3]]
'''
# Determinar la media de los valores de un array 
arr_num3 = np.array([12,32,8])
arr_media = arr_num3.mean()
print(f"La media del array es: {arr_media}")
# Lo mismo que hacer...
print((12 + 32 + 8) /3,"\n") 

# Raiz cuadrada "np.sqrt()"
arr_decimales = np.array([ [15,25,36,40]])
print(np.sqrt(arr_decimales))

# Producto escalar entre dos arrays (bidimencionales)
arr_a = np.array([10, 20])
arr_b = np.array([3, 4])
arr_total = np.dot(arr_a, arr_b)
print(arr_total)
arr_d = np.array([5, 6])
print(np.dot(arr_b, arr_d)) # 5*3 + 6*4 = 39