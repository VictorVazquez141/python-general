'''
//////////// Indexing 
-Es la forma de acceder a elementos especificos dentro de una estructura de datos
(tuplas, tuplas, strings...)
'''

lista_1 = ["As",2,3,4,5,6,7,8,9,10,"J","Q","K"]

# Aceder a elemtos por indicie (inicia desde el 0 como los array )
print(lista_1[0])
# INDICES NEGATIVOS (toma como referencia el -1 como el ultimo elemento)
print(lista_1[-1])
# SEGMENTACIÓN O SLICING (se definen los rangos de inicio y fin de ciertos elementos)
print(f"solo numeros: {lista_1[1:10]}")
print(f"Escalera real: {lista_1[10:13]}") # SIEMPRE SE INIDCA UN NUMERO MAS DEL LIMITE A ELEGIR 

# Accediendo a diccionarios 
diccionario_a = {
    "nombre": "Victor",
    "edad": 24,
    "ciudad": "Tenancingo"
}
print(diccionario_a["nombre"])
diccionario_a ["signo"] = "Acuario"
print(diccionario_a)


'''
/////////////// SLICING 
-tecnica para cceder a subsección (subparte) en una secuencia, como listas, tupla o string. Extrae elementos de una secuencia
mediante un rango de indices especificados 
---------
secuencia [inicio : fin : paso]
---------
'''
lista_2 = [2,4,8,16,32,64,128,256,512,1024]
print(lista_2[2:7])
# Usando un paso definido (2 en 2)
print(lista_2[1:8:2]) # Devuelve 4 elementos, uno con cada paso 

# Con String
palabra_1 = "Hi, this is my exercise in python"
print(palabra_1[2]) #Devuelve solo un caracter 
print(palabra_1[0:10]) #Devueve hasta donde alcancen los 10 caracteres 
print(palabra_1[0: : 2])



