'''
En este ejercicio se verá cómo leer archvios con pyhton
'''
# Inidicamos la apertura del archivo indicando su ruta de esta forma
# Asignando una variable

# Open es la función que se encarga de ABRIR el archivo
'''
archivo = open("archivos\\texto_1.txt")
print(archivo.read()) 
'''
# Con ayuda de la función 'read()' hacemos que el archivo abireto en la variable ahora lo lea, y lo muestre 'print()'

'''
NOTA.
Una vez que el archivo es abierto (linea 7) y leido (linea 10) ya no
se puede volver a leer
'''
# AL EJECUTAR LO SIGUIENTE SE TIENE que cancelar lo de las lineas anteriores 

archivo_sin_leer = open("archivos\\texto_1.txt")

# Leer linea por linea 
lineas = archivo_sin_leer.readlines()
# Leer una  linea
#print(lineas)

'''
Para leer una sola linea se indica "readline()" 
Dentro de los parametros de "readline()" son la cantidad de caracteres a mostrar del texto
'''

# cerrar el archivo
archivo_cerrado = archivo_sin_leer

archivo_cerrado.close()
print(archivo_cerrado) # Ahora indica en consola que el archivo se cerró 
'''
Para volver a leerlo se tiene que ejecutar nuevamente la función open()
'''

