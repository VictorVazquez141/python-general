
'''Ejercicio'''
'''Crear un codigo que muestre la cantidad de descuetos por año de cada temporada'''
import numpy as np

arr_temporadas = ["Verano","Primavera","Otoño","Invierno"]

arr_descuentos = np.arange(10, 41, 10)
# Array creado de 0 a 10 con pasos de 2
print(arr_descuentos)

for i in arr_temporadas:
    for j in arr_descuentos:
        print(f"Temporada: {i} -> Descuento: {j}")
