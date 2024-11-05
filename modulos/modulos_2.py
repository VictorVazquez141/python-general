'''
Para movernos entre modulos de otras carpetas: es necesario lo siguiente.
 import 'nomrbe de la carpeta'.'nombre del modulo'
'''
import funciones_buenas.modulo_saludar as fb_saludos

nameUser = input("Inserta tu nombre: ")
print(fb_saludos.saludo_ingles(nameUser))

'''
Para acceder a carpetas mas externas o en otro tipo de carpetas: utilizamos el modulo siguiente.
 
'''
# import sys

# sys.path.append("C:\\Users\\HP\\Documents\\Curso Python\\Curso 2024\\ejercicios_insta.py\\modulosExcercise")

# import numberRand
# print(numberRand())

