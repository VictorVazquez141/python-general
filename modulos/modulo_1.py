'''
Modulos.
-Archivos con extención .py que contienen declaraciones y definiciones de python (def, variables, clases) permitiendo 
al codigo ser mas reutilizable y manejable.
-Se crea guardado funciones, lcases y variables dentro de un archivo py, y se invocan sus metodos de la siguiente forma:
'''
#la importación tiene que llevar el nombre del archivo ".py"
import funciones_buenas.modulo_saludar as m_saludo
#Ejemplo con 'as'


userName = input("Ingresa tu nombre: ")
sayHi = m_saludo.saludar(userName)
print(sayHi)


'''
Importar modulo:
 import "nombre del modulo" as "alias"

importar una función(es) en especifica(s):
 from "nombre del modulo" import "función", "funciones"
 

'''



