"""
////// DICCIONARIOS
-Colecciones de pares 'clave-valor' que pueden ser mutables (se agregan, eliminan y cambian elementos clave-valor). Permiten el 
acceso rapido a valores de una clave, ideales para los datos relacionados, conde cada elemento tiene clave unica.
"""
# Con elementos definidos 
diccionario_1 = {
    "nombre": "Victor",
    "apellido": "Vazquez",
    "edad": 24,
    "ciudad": "Tenancingo"
}

# Usando el constructor "dict()"
dic_constructor = dict(auto="Camaro", marca="Chevrolet", motor="V8", nacion="EUA")

# Acceder a valores 
print(diccionario_1["ciudad"]) #Tenancingo
print(diccionario_1["apellido"])

# Con metodo "get()" (evita errores si la clave no existe)
print(diccionario_1.get("nombre")) # Victor 
print(diccionario_1.get("pais")) # <None>
print(diccionario_1.get("lengua", "español")) # español (lo devuelve mas no lo agrega)

# Modificación y adición de elemtos 
diccionario_1["ciudad"] = "Cuajimalpa CDMX" #Modifica valor
diccionario_1["telefono"] = 7221531076 #Agrega clave y valor 
print(list(diccionario_1)) # Solo claves

# Eliminación de elementos 
del diccionario_1["telefono"] #'del' elimina una clave
edad = diccionario_1.pop("edad") #'pop()' elimina una clave y podemos obtener su valor
print(edad), print(diccionario_1)

ultimo_element = diccionario_1.popitem() #'popitem()' elimina y evuelve el utimo par clave-valor 
print(ultimo_element)

# ITERACIÓN SOBRE DICCIONARIOS 
print("\nITERACIONES.\n")
diccionario_2 = {
    "nombre": "Marcus",
    "apellido":"Fenix",
    "edad": 42,
    "cidad": "Ilima"
}
# Sobre claves del dic.
for clave in diccionario_2:
    print(clave)
print("\nValores:")
# valores
for valor in diccionario_2.values():
    print(valor)

# itecación sobre clave-valor
for clave, valor in diccionario_2.items():
    print(clave, valor)
